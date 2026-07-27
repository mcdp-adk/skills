---
name: grok-search
compatibility: Requires a Python 3.10+ runner (try python, then platform python, then uv). Stdlib-only.
description: >
  Use when the task requires actually retrieving content from the external Web
  or X: current information, a specified official page or account, a specified
  historical date range, or external verification of a claim or other content
  the user supplied. It also covers the narrow management of this CLI: running,
  configuring, or troubleshooting `grok-search`, and explaining its JSON,
  errors, `response_id`, or continuation behavior. Do not use for general local
  file or repository search, code analysis, analysis of user-provided content
  without external sources, or stable-knowledge answers when external retrieval
  was not requested. Even troubleshooting must not read or display `.env`.
  Current legal or market materials may be retrieved, but this skill does not
  provide legal certification or predict prices.
---

# Grok Search

`{baseDir}` means this skill's root directory: the directory containing
`SKILL.md`. If the harness leaves the placeholder unchanged, substitute that
directory's absolute path in the commands below.

Use the bundled script to search the live Web and X through xAI Grok. It returns
a synthesized answer with source URLs and a continuation ID when available.

## Run the tool

Before the first search, verify runners in this order and use the first one that
succeeds:

1. `python`.
2. The platform runner: `py -3` on Windows or `python3` on Linux/macOS.
3. An already installed `uv`, using `uv run --no-project --python 3.10`.

Each candidate must verify the script with `--help`:

```bash
python "{baseDir}/scripts/search.py" --help
py -3 "{baseDir}/scripts/search.py" --help          # Windows
python3 "{baseDir}/scripts/search.py" --help        # Linux/macOS
uv run --no-project --python 3.10 "{baseDir}/scripts/search.py" --help
```

Verify `--help` once and reuse that runner for the rest of the session. Do not
use an independent installer or install uv or pip packages. If uv is already
available as the final fallback and the requested Python 3.10 is missing, it may
download a managed Python 3.10 on first use and may need network access. If that
download is not allowed, stop and ask the user for an available runner rather
than installing another tool.
The script handles eligible internal retries within the same CLI invocation.

The standard command is:

```bash
python "{baseDir}/scripts/search.py" "your query here"
```

Replace `python` with the verified runner; with uv, keep its `run --no-project
--python 3.10` prefix. The script loads `{baseDir}/.env` automatically. The
agent must not read, display, copy, or parse `.env`. Required configuration is
`XAI_API_KEY`; `HTTPS_PROXY`, `HTTP_PROXY`, `ALL_PROXY`, `NO_PROXY`, and
`--ca-bundle` are optional network settings.

## Choose the request

Use the smallest request that fits the user's needs. The default source is
`both`, and the default preset is `multi-4`, so omit those flags when they fit.

| Control | Decision |
|---|---|
| `--source web\|x\|both` | Choose Web, X, or both. With `both`, date flags affect X only. |
| `--preset single\|multi-4\|multi-16` | `single` is for one fact, a specified page/account, or speed and has the lowest relative cost. Omit the flag for ordinary searches (`multi-4`, the default, with moderate relative cost). Use `multi-16` only when the user explicitly asks for comprehensive/deep work and the task is genuinely multi-faceted; it has the highest relative cost. |
| `--since` / `--until` | Strict date filters for X. Web has no strict date filter: `--source web` with either flag fails, while `both` applies the flags only to X. Put hour-level freshness, such as “in the past 2 hours,” in the query text because the X filter is date-level. |
| Web/X filters | Use `--web-allow` or `--web-exclude` for domains, and `--x-allow` or `--x-exclude` for handles. Keep each filter with a compatible source and do not combine allow and exclude for the same source. |
| `--continue RESPONSE_ID` | Continue a prior response using its `response_id`; use follow-ups to fill a known gap or audit evidence. |
| Media | Add `--image-understanding` for supported images. Add `--video-understanding` for video; it requires `--source x` or `both`. Both are off by default. |

Time values can be relative (`2h`, `7d`, `2w`, `today`, `yesterday`, `now`) or
ISO date/time values; they are interpreted in UTC. For Web recency, state the
time range in the query itself.

## Read and present the result

The normal output is JSON. For a successful response, use these fields:

The script writes its managed success and error JSON to stdout. `Searching...`,
`Done.`, and internal retry notices go to stderr. Parse stdout, not stderr; do
not treat progress lines as JSON or as a parse failure. If the environment
merges the streams, identify the script's single-line JSON and ignore the
corresponding non-JSON progress lines; do not invoke the search again.

- `ok` — whether the search completed successfully.
- `text` — the synthesized answer to present and, when needed, summarize.
- `citations` — candidate source URLs, not fact verification. Check important
  claims against the cited pages when the stakes justify it.
- `response_id` — the ID to pass to `--continue` for a follow-up, when present.
- `request_summary` — the effective source, preset, and time-filter behavior.
- `citation_coverage` — a mechanical comparison of URLs in `text` with API
  citations; it does not show that a source supports a claim.

Separate confirmed findings, conflicting reports, social signals, and evidence
that is still insufficient. An official X account post can establish that the
account made a statement, but it does not by itself verify the statement's
underlying facts; broad factual conclusions need independent support. Treat X
posts as social signals unless independent credible sources support the claim.
Do not claim to identify, filter, or quantify bots or coordinated behavior; the
CLI has no bot-detection capability. Describe discussion or emotional tone
qualitatively; do not invent percentages without a sampling method. In a
multi-turn search, use later requests to close gaps and audit earlier evidence,
not merely to ask for more detail. Present the answer and relevant citations,
not the complete JSON or a long query template.

## Handle failures safely

- `ENV_ERROR` means configuration is missing or malformed. Ask the user to set
  `XAI_API_KEY` in the skill's `.env` (using `.env.example`) or in the OS
  environment; a non-empty OS value takes priority.
- Authentication errors indicate an invalid or expired key. Ask the user to
  replace it through [console.x.ai](https://console.x.ai). Keep keys and
  `.env` contents out of logs and output.
- For a local argument error, report the actual error and exit status, and only
  correct it when the exact fix is clear and does not change the user's intent
  or expected cost.
- After the script returns a final API, connection, or timeout error, do not
  automatically start a second CLI invocation. This does not require adding
  `--max-retries 0` and does not disable the script's internal retries. A
  timeout may have reached the service, so check for possible processing first.
- First report every failed request. Without the user's explicit approval, a
  new call must not change the preset, model, or effort, and must not retry with
  `single`.

## References

Read [references/references.md](references/references.md) only as needed: to
check model or effort semantics, filter limits, retry behavior, proxy
precedence, output formats, or uncommon errors.
