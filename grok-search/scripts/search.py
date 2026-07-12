#!/usr/bin/env python3
"""Search the web and X through the xAI Responses API."""

from __future__ import annotations

import argparse
import datetime as dt
import errno
import json
import os
import random
import re
import socket
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


API_URL = "https://api.x.ai/v1/responses"
EXIT_GENERAL, EXIT_AUTH, EXIT_ENV = 1, 2, 3
UTC = dt.timezone.utc
PRESETS = {
    "single": ("grok-4.3", "low"),
    "multi-4": ("grok-4.20-multi-agent", "low"),
    "multi-16": ("grok-4.20-multi-agent", "high"),
}


class SearchError(Exception):
    def __init__(self, code: str, message: str, exit_code: int = EXIT_GENERAL):
        super().__init__(message)
        self.code, self.message, self.exit_code = code, message, exit_code


@dataclass(frozen=True)
class ResolvedConfig:
    query: str
    source: str
    preset: str
    preset_explicit: bool
    preset_overridden: bool
    model: str
    effort: str | None
    since: dt.datetime | None
    until: dt.datetime | None
    web_allow: list[str]
    web_exclude: list[str]
    x_allow: list[str]
    x_exclude: list[str]
    continuation: str | None
    image_understanding: bool
    video_understanding: bool
    timeout: int
    max_retries: int
    env_file: Path
    ca_bundle: str | None
    raw: bool


def default_env_file() -> Path:
    return (Path(__file__).resolve().parent / ".." / ".env").resolve()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Search the web and X using xAI.")
    parser.add_argument("query", nargs="?", help="Query text; reads stdin when omitted.")
    parser.add_argument("--source", default="both", metavar="web|x|both")
    parser.add_argument(
        "--preset",
        choices=PRESETS,
        metavar="single|multi-4|multi-16",
        help="Select a model and reasoning-effort preset (default: single).",
    )
    parser.add_argument("--model", help="Override the preset model.")
    parser.add_argument(
        "--effort",
        choices=["none", "low", "medium", "high", "xhigh"],
        help="Override the preset effort.",
    )
    parser.add_argument("--since", help="X search only; for web, state the time range in your query. UTC relative time or ISO date/time.")
    parser.add_argument("--until", help="X search only; for web, state the time range in your query. UTC relative time or ISO date/time.")
    parser.add_argument("--web-allow", action="append", default=[], metavar="DOMAIN")
    parser.add_argument("--web-exclude", action="append", default=[], metavar="DOMAIN")
    parser.add_argument("--x-allow", action="append", default=[], metavar="HANDLE")
    parser.add_argument("--x-exclude", action="append", default=[], metavar="HANDLE")
    parser.add_argument("--continue", dest="continuation", metavar="RESPONSE_ID")
    parser.add_argument("--image-understanding", action="store_true")
    parser.add_argument("--video-understanding", action="store_true")
    parser.add_argument("--timeout", type=int, metavar="SEC")
    parser.add_argument("--max-retries", type=int, default=3, metavar="N")
    parser.add_argument("--env-file", default=str(default_env_file()), metavar="PATH")
    parser.add_argument("--ca-bundle", metavar="PATH")
    parser.add_argument("--raw", action="store_true", help="Output the raw API response.")
    return parser


def parse_time(value: str, name: str, now: dt.datetime) -> dt.datetime:
    relative = {
        "now": now,
        "today": now.replace(hour=0, minute=0, second=0, microsecond=0),
        "yesterday": (now - dt.timedelta(days=1)).replace(
            hour=0, minute=0, second=0, microsecond=0
        ),
    }
    if value in relative:
        return relative[value]
    if len(value) > 1 and value[-1] in "hdw" and value[:-1].isdigit():
        amount = int(value[:-1])
        unit = {"h": "hours", "d": "days", "w": "weeks"}[value[-1]]
        try:
            return now - dt.timedelta(**{unit: amount})
        except OverflowError as exc:
            raise SearchError("ARGUMENT_ERROR", f"{name} value is too large") from exc
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise SearchError("ARGUMENT_ERROR", f"{name} must be 2h, 7d, 2w, today, yesterday, now, or an ISO date/time") from exc
    return parsed.replace(tzinfo=UTC) if parsed.tzinfo is None else parsed.astimezone(UTC)


def read_query(value: str | None) -> str:
    query = (value if value is not None else sys.stdin.read()).strip()
    if not query:
        raise SearchError("ARGUMENT_ERROR", "A query is required as an argument or via stdin.")
    return query


def clean_domains(items: list[str]) -> list[str]:
    return [item.strip() for item in items if item.strip()]


def clean_handles(items: list[str]) -> list[str]:
    return [handle for item in items if (handle := item.strip().lstrip("@"))]


def model_family(model: str) -> str:
    if model == "grok-4.20-multi-agent" or model.startswith("grok-4.20-multi-agent-"):
        return "multi-agent"
    if model == "grok-4.3" or model.startswith("grok-4.3-"):
        return "grok-4.3"
    if model == "grok-4.5" or model.startswith("grok-4.5-"):
        return "grok-4.5"
    return "unknown"


def default_effort(family: str) -> str | None:
    return "low" if family in {"grok-4.3", "grok-4.5", "multi-agent"} else None


def default_timeout(family: str, effort: str | None) -> int:
    if family in {"grok-4.3", "grok-4.5"}:
        return 60 if effort in {None, "low"} else 120
    if family == "multi-agent":
        return 600 if effort in {"high", "xhigh"} else 300
    return 600


def agent_count(family: str, effort: str | None) -> int | None:
    if family in {"grok-4.3", "grok-4.5"}:
        return 1
    if family == "multi-agent":
        return 16 if effort in {"high", "xhigh"} else 4
    return None


def resolve_config(args: argparse.Namespace) -> ResolvedConfig:
    if args.source not in {"web", "x", "both"}:
        raise SearchError("ARGUMENT_ERROR", "--source must be web, x, or both")
    if args.source == "web" and (args.since or args.until):
        raise SearchError("ARGUMENT_ERROR", "Time filters are not supported for web search. Put the time range in your query text, or use --source x or --source both.")
    web_allow, web_exclude = clean_domains(args.web_allow), clean_domains(args.web_exclude)
    x_allow, x_exclude = clean_handles(args.x_allow), clean_handles(args.x_exclude)
    if (args.web_allow and not web_allow) or (args.web_exclude and not web_exclude):
        raise SearchError("ARGUMENT_ERROR", "Web domains must not be empty")
    if (args.x_allow and not x_allow) or (args.x_exclude and not x_exclude):
        raise SearchError("ARGUMENT_ERROR", "X handles must not be empty")
    if web_allow and web_exclude:
        raise SearchError("ARGUMENT_ERROR", "--web-allow and --web-exclude are mutually exclusive")
    if x_allow and x_exclude:
        raise SearchError("ARGUMENT_ERROR", "--x-allow and --x-exclude are mutually exclusive")
    if len(web_allow) > 5 or len(web_exclude) > 5:
        raise SearchError("ARGUMENT_ERROR", "Web filters support at most 5 domains")
    if len(x_allow) > 20 or len(x_exclude) > 20:
        raise SearchError("ARGUMENT_ERROR", "X filters support at most 20 handles")
    if (web_allow or web_exclude) and args.source == "x":
        raise SearchError("ARGUMENT_ERROR", "Web filters require --source web or both")
    if (x_allow or x_exclude) and args.source == "web":
        raise SearchError("ARGUMENT_ERROR", "X filters require --source x or both")
    if args.video_understanding and args.source == "web":
        raise SearchError("ARGUMENT_ERROR", "--video-understanding requires --source x or both")
    if args.max_retries < 0:
        raise SearchError("ARGUMENT_ERROR", "--max-retries must be 0 or greater")
    preset = args.preset or "single"
    preset_model, preset_effort = PRESETS[preset]
    model = args.model or preset_model
    preset_family, family = model_family(preset_model), model_family(model)
    if args.effort is not None:
        effort = args.effort
    elif args.model and family != preset_family:
        effort = default_effort(family)
    else:
        effort = preset_effort
    if family == "multi-agent" and effort == "none":
        raise SearchError("ARGUMENT_ERROR", "grok-4.20-multi-agent does not support effort none")
    if family == "grok-4.3" and effort == "xhigh":
        raise SearchError("ARGUMENT_ERROR", "grok-4.3 does not support effort xhigh")
    if family == "grok-4.5" and effort in ("none", "xhigh"):
        raise SearchError("ARGUMENT_ERROR", "grok-4.5 does not support effort none or xhigh")
    timeout = args.timeout if args.timeout is not None else default_timeout(family, effort)
    if timeout <= 0:
        raise SearchError("ARGUMENT_ERROR", "--timeout must be greater than 0")
    now = dt.datetime.now(UTC)
    since = parse_time(args.since, "--since", now) if args.since else None
    until = parse_time(args.until, "--until", now) if args.until else None
    if since and until and since > until:
        raise SearchError("ARGUMENT_ERROR", "--since must be earlier than or equal to --until")
    return ResolvedConfig(
        query=read_query(args.query),
        source=args.source,
        preset=preset,
        preset_explicit=args.preset is not None,
        preset_overridden=(model, effort) != (preset_model, preset_effort),
        model=model,
        effort=effort,
        since=since,
        until=until,
        web_allow=web_allow,
        web_exclude=web_exclude,
        x_allow=x_allow,
        x_exclude=x_exclude,
        continuation=args.continuation,
        image_understanding=args.image_understanding,
        video_understanding=args.video_understanding,
        timeout=timeout,
        max_retries=args.max_retries,
        env_file=Path(args.env_file).expanduser(),
        ca_bundle=args.ca_bundle,
        raw=args.raw,
    )


def build_tools(config: ResolvedConfig) -> list[dict[str, Any]]:
    tools: list[dict[str, Any]] = []
    if config.source in {"web", "both"}:
        tool: dict[str, Any] = {"type": "web_search"}
        filters: dict[str, Any] = {}
        if config.web_allow:
            filters["allowed_domains"] = config.web_allow
        if config.web_exclude:
            filters["excluded_domains"] = config.web_exclude
        if filters:
            tool["filters"] = filters
        if config.image_understanding:
            tool["enable_image_understanding"] = True
        tools.append(tool)
    if config.source in {"x", "both"}:
        tool = {"type": "x_search"}
        if config.x_allow:
            tool["allowed_x_handles"] = config.x_allow
        if config.x_exclude:
            tool["excluded_x_handles"] = config.x_exclude
        if config.since:
            tool["from_date"] = config.since.date().isoformat()
        if config.until:
            tool["to_date"] = config.until.date().isoformat()
        if config.image_understanding and config.source == "x":
            tool["enable_image_understanding"] = True
        if config.video_understanding:
            tool["enable_video_understanding"] = True
        tools.append(tool)
    return tools


def build_payload(config: ResolvedConfig) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": config.model,
        "input": [{"role": "user", "content": config.query}],
        "tools": build_tools(config),
    }
    if config.effort is not None:
        payload["reasoning"] = {"effort": config.effort}
    if config.continuation:
        payload["previous_response_id"] = config.continuation
    return payload


def parse_env_value(value: str) -> str:
    value = value.strip()
    return value[1:-1] if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'" else value


def load_env_file(path: Path) -> dict[str, str]:
    if not path.exists(): return {}
    env: dict[str, str] = {}
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"): continue
        if line.startswith("export "): line = line[7:].strip()
        if "=" not in line or not line.split("=", 1)[0].strip():
            raise SearchError("ENV_ERROR", f"Invalid .env line {number} in {path}: expected KEY=value", EXIT_ENV)
        key, value = line.split("=", 1)
        env[key.strip()] = parse_env_value(value)
    return env


def env_value(file_env: dict[str, str], *names: str) -> str | None:
    for source in (os.environ, file_env):
        for name in names:
            if value := source.get(name): return value
    return None


def build_proxy_map(file_env: dict[str, str]) -> dict[str, str] | None:
    proxy = (
        env_value(file_env, "HTTPS_PROXY", "https_proxy")
        or env_value(file_env, "ALL_PROXY", "all_proxy")
        or env_value(file_env, "HTTP_PROXY", "http_proxy")
    )
    return {"http": proxy, "https": proxy} if proxy else None


def build_opener(proxies: dict[str, str] | None, ca_bundle: str | None) -> urllib.request.OpenerDirector:
    handlers: list[Any] = [urllib.request.ProxyHandler(proxies)] if proxies else []
    if ca_bundle: handlers.append(urllib.request.HTTPSHandler(context=ssl.create_default_context(cafile=ca_bundle)))
    return urllib.request.build_opener(*handlers)


def build_request(api_key: str, payload: dict[str, Any]) -> urllib.request.Request:
    request = urllib.request.Request(API_URL, data=json.dumps(payload).encode(), method="POST")
    request.add_header("Authorization", f"Bearer {api_key}")
    request.add_header("Content-Type", "application/json")
    return request


def retry_delay(attempt: int, retry_after: str | None = None) -> float:
    if retry_after and retry_after.strip().isdigit(): return max(float(retry_after), 0)
    return min(.5 * 2 ** attempt, 8) * random.uniform(.75, 1)


def error_body(exc: urllib.error.HTTPError) -> str:
    try: return exc.read().decode("utf-8", errors="replace").strip()
    except Exception: return ""


def is_pre_send_error(reason: Any) -> bool:
    if isinstance(reason, ConnectionRefusedError):
        return True
    if isinstance(reason, OSError):
        return reason.errno in (errno.ENETUNREACH, errno.EHOSTUNREACH, errno.ECONNREFUSED)
    return False


def execute_request(opener: urllib.request.OpenerDirector, api_key: str, payload: dict[str, Any], config: ResolvedConfig) -> dict[str, Any]:
    for attempt in range(config.max_retries + 1):
        try:
            with opener.open(build_request(api_key, payload), timeout=config.timeout) as response:
                data = json.loads(response.read().decode("utf-8"))
                if not isinstance(data, dict):
                    raise SearchError("PARSE_ERROR", "API response is not a JSON object")
                return data
        except urllib.error.HTTPError as exc:
            body, status = error_body(exc), exc.code
            if status == 401:
                raise SearchError("AUTH_ERROR", "Invalid API key. Get one at https://console.x.ai", EXIT_AUTH) from exc
            if status == 400:
                raise SearchError("BAD_REQUEST", f"Bad request: {body}" if body else "Bad request") from exc
            if status != 429 or attempt >= config.max_retries:
                raise SearchError("HTTP_ERROR", body or f"HTTP {status}") from exc
            delay = retry_delay(attempt, exc.headers.get("Retry-After"))
        except (TimeoutError, socket.timeout) as exc:
            raise SearchError("TIMEOUT", "Request timed out and may have been processed. Check your account before retrying.") from exc
        except urllib.error.URLError as exc:
            if isinstance(exc.reason, (TimeoutError, socket.timeout)) or "timed out" in str(exc.reason).lower():
                raise SearchError("TIMEOUT", "Request timed out and may have been processed. Check your account before retrying.") from exc
            if not is_pre_send_error(exc.reason) or attempt >= config.max_retries:
                raise SearchError("CONNECTION_ERROR", f"Connection failed: {exc.reason}") from exc
            delay = retry_delay(attempt)
        eprint(f"Retrying in {delay:.2f}s (attempt {attempt + 1}/{config.max_retries})...")
        time.sleep(delay)
    raise SearchError("REQUEST_FAILED", "Request failed unexpectedly")


def parse_response(data: dict[str, Any]) -> tuple[str, list[str], bool]:
    texts: list[str] = []
    citations: list[str] = []
    found_message = False
    output = data.get("output")
    if isinstance(output, list):
        for item in output:
            if not isinstance(item, dict) or item.get("type") != "message": continue
            found_message = True
            content = item.get("content")
            if not isinstance(content, list): continue
            for part in content:
                if not isinstance(part, dict) or part.get("type") != "output_text": continue
                if isinstance(part.get("text"), str):
                    texts.append(part["text"])
                annotations = part.get("annotations")
                if not isinstance(annotations, list): continue
                for annotation in annotations:
                    if not isinstance(annotation, dict) or annotation.get("type") != "url_citation": continue
                    url = annotation.get("url")
                    if isinstance(url, str) and (url := url.strip()) and url not in citations:
                        citations.append(url)
    return "\n".join(texts), citations, found_message


def normalize_url(value: str) -> str:
    value = value.strip().strip("<>").rstrip(".,;:!\"]}")
    try:
        parts = urllib.parse.urlsplit(value)
    except ValueError:
        return value
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc.lower(), parts.path, parts.query, ""))


def citation_coverage(text: str, citations: list[str]) -> dict[str, list[str]]:
    api_urls = list(dict.fromkeys(normalize_url(url) for url in citations))
    text_urls = [normalize_url(url) for url in citations if url in text]
    for match in re.finditer(r"(?<![\w\]\)])https?://[^\s<>\[\]]+", text):
        url = match.group(0).rstrip(".,;:!\"]}")
        while url.endswith(")") and url.count(")") > url.count("("):
            url = url[:-1]
        normalized = normalize_url(url)
        if normalized not in text_urls:
            text_urls.append(normalized)
    return {
        "text_urls": text_urls,
        "api_citation_urls": api_urls,
        "unmatched_text_urls": [url for url in text_urls if url not in api_urls],
    }


def build_request_summary(config: ResolvedConfig) -> dict[str, Any]:
    has_time = config.since is not None or config.until is not None
    family = model_family(config.model)
    warnings = []
    if family == "grok-4.5":
        warnings.append("grok-4.5 costs more than the default grok-4.3 model.")
        warnings.append("grok-4.5 is unavailable in EU regions.")
    elif family == "unknown":
        warnings.append("Unknown model family; reasoning defaults and agent count are not known.")
    return {
        "source": config.source,
        "preset_used": config.preset,
        "preset_explicit": config.preset_explicit,
        "preset_overridden": config.preset_overridden,
        "model_used": config.model,
        "effort_sent": config.effort,
        "agent_count": agent_count(family, config.effort),
        "timeout_seconds": config.timeout,
        "warnings": warnings,
        "resolved_since": config.since.isoformat() if config.since else None,
        "resolved_until": config.until.isoformat() if config.until else None,
        "x_time_filter": "strict" if has_time and config.source in {"x", "both"} else "not_applied",
        "web_strict_filter_available": False,
    }


def success_payload(data: dict[str, Any], config: ResolvedConfig) -> dict[str, Any]:
    if data.get("status") != "completed":
        raise SearchError("INCOMPLETE", f"Response status is {data.get('status')!r}, not 'completed'")
    text, citations, found_message = parse_response(data)
    if not found_message:
        raise SearchError("EMPTY_RESPONSE", "Completed response contains no message output")
    response_id = data.get("id") if isinstance(data.get("id"), str) and data["id"] else None
    return {
        "ok": True,
        "response_id": response_id,
        "text": text,
        "citations": citations,
        "request_summary": build_request_summary(config),
        "citation_coverage": citation_coverage(text, citations),
        "usage": data.get("usage") if isinstance(data.get("usage"), dict) else {},
    }


def error_payload(exc: SearchError) -> dict[str, Any]:
    return {"ok": False, "error": {"code": exc.code, "message": exc.message}}


def eprint(message: str) -> None: print(message, file=sys.stderr)
def emit(data: dict[str, Any]) -> None: print(json.dumps(data, ensure_ascii=False), flush=True)


def main() -> int:
    parser = build_parser()
    try:
        config = resolve_config(parser.parse_args())
        file_env = load_env_file(config.env_file)
        if no_proxy := env_value(file_env, "NO_PROXY", "no_proxy"): os.environ["NO_PROXY"] = no_proxy
        api_key = env_value(file_env, "XAI_API_KEY")
        if not api_key:
            raise SearchError("ENV_ERROR", f"API key not found. Set XAI_API_KEY in the environment or in {config.env_file}.", EXIT_ENV)
        eprint("Searching...")
        data = execute_request(build_opener(build_proxy_map(file_env), config.ca_bundle), api_key, build_payload(config), config)
        emit(data if config.raw else success_payload(data, config))
        eprint("Done.")
        return 0
    except SearchError as exc:
        emit(error_payload(exc))
        return exc.exit_code
    except FileNotFoundError as exc:
        emit(error_payload(SearchError("ENV_ERROR", str(exc), EXIT_ENV)))
        return EXIT_ENV
    except json.JSONDecodeError as exc:
        emit(error_payload(SearchError("PARSE_ERROR", f"Malformed API response: {exc}")))
        return EXIT_GENERAL
    except Exception as exc:
        emit(error_payload(SearchError("UNEXPECTED_ERROR", str(exc))))
        return EXIT_GENERAL


if __name__ == "__main__": sys.exit(main())
