import email.message
import importlib.util
import io
import json
import os
import pathlib
import sys
import tempfile
import unittest
import urllib.error
from contextlib import contextmanager
from unittest import mock


SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "search.py"
SPEC = importlib.util.spec_from_file_location("grok_search", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Could not load search script")
search = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = search
SPEC.loader.exec_module(search)


def config(*arguments):
    return search.resolve_config(search.build_parser().parse_args([*arguments, "test query"]))


@contextmanager
def capture_main_output():
    stdout = io.StringIO()
    stderr = io.StringIO()
    with mock.patch.object(search.sys, "stdout", stdout), mock.patch.object(search.sys, "stderr", stderr):
        yield stdout


class PresetResolutionTests(unittest.TestCase):
    def test_payload_uses_tools_as_the_only_source_selector(self):
        for source, arguments, expected_tools in (
            ("web", (), ["web_search"]),
            ("x", ("--since", "2026-07-01", "--until", "2026-07-02"), ["x_search"]),
            ("both", ("--since", "2026-07-01", "--until", "2026-07-02"), ["web_search", "x_search"]),
        ):
            with self.subTest(source=source):
                payload = search.build_payload(config("--source", source, *arguments))
                self.assertEqual([tool["type"] for tool in payload["tools"]], expected_tools)
                self.assertNotIn("search_parameters", payload)
                self.assertNotIn("max_search_results", payload)
                web_tool = next((tool for tool in payload["tools"] if tool["type"] == "web_search"), None)
                x_tool = next((tool for tool in payload["tools"] if tool["type"] == "x_search"), None)
                if web_tool:
                    self.assertNotIn("from_date", web_tool)
                    self.assertNotIn("to_date", web_tool)
                if x_tool:
                    self.assertEqual(x_tool["from_date"], "2026-07-01")
                    self.assertEqual(x_tool["to_date"], "2026-07-02")

    def test_web_source_rejects_time_filters(self):
        for arguments in (("--since", "7d"), ("--until", "2026-07-01")):
            with self.subTest(arguments=arguments), self.assertRaisesRegex(search.SearchError, "Put the time range in your query") as raised:
                config("--source", "web", *arguments)
            self.assertEqual(raised.exception.code, "ARGUMENT_ERROR")
        both = config("--source", "both", "--since", "7d")
        both_tools = search.build_tools(both)
        self.assertNotIn("from_date", both_tools[0])
        self.assertIn("from_date", both_tools[1])
        self.assertIsNotNone(config("--source", "x", "--since", "7d").since)

    def test_max_results_is_rejected_by_argparse(self):
        with self.assertRaises(SystemExit) as raised:
            search.build_parser().parse_args(["--max-results", "5", "test query"])
        self.assertEqual(raised.exception.code, 2)

    def test_parse_response_extracts_citations_from_annotations(self):
        annotation_url = "https://annotation.example/source"
        sentinel = "https://legacy-sentinel.example/should-not-appear"
        response = {
            "citations": [sentinel],
            "output": [
                None,
                {"type": "reasoning", "content": []},
                {"type": "message", "content": "not a list"},
                {"type": "message", "content": [None, {"type": "other", "annotations": [{"type": "url_citation", "url": sentinel}]}, {"type": "output_text", "annotations": "not a list"}, {"type": "output_text", "annotations": [None, {}, {"type": "other", "url": sentinel}, {"type": "url_citation"}, {"type": "url_citation", "url": ""}, {"type": "url_citation", "url": "   "}, {"type": "url_citation", "url": f"  {annotation_url}  "}, {"type": "url_citation", "url": annotation_url}]}]},
            ],
        }
        self.assertEqual(search.parse_response(response)[1], [annotation_url])
        self.assertEqual(search.parse_response({"output": [{"type": "message", "content": [{"type": "output_text", "text": "ok"}]}]})[1], [])
        self.assertEqual(search.parse_response({"citations": [sentinel], "output": []})[1], [])

    def test_default_multi_4(self):
        resolved = config()
        self.assertEqual((resolved.preset, resolved.model, resolved.effort, search.agent_count(search.model_family(resolved.model), resolved.effort), resolved.timeout), ("multi-4", "grok-4.20-multi-agent", "low", 4, 300))
        self.assertFalse(resolved.preset_explicit)
        self.assertFalse(resolved.preset_overridden)

    def test_explicit_presets(self):
        for preset, model, effort, count, timeout in (("single", "grok-4.3", "low", 1, 60), ("multi-4", "grok-4.20-multi-agent", "low", 4, 300), ("multi-16", "grok-4.20-multi-agent", "high", 16, 600)):
            resolved = config("--preset", preset)
            family = search.model_family(resolved.model)
            self.assertEqual((resolved.model, resolved.effort, search.agent_count(family, resolved.effort), resolved.timeout, resolved.preset_explicit), (model, effort, count, timeout, True))

    def test_same_family_overrides_keep_preset_effort(self):
        for model in ("grok-4.3-custom", "grok-4.3-0309"):
            resolved = config("--preset", "single", "--model", model)
            self.assertEqual((resolved.effort, resolved.timeout, resolved.preset_overridden), ("low", 60, True))

    def test_default_model_overrides(self):
        resolved = config("--model", "grok-4.3")
        self.assertEqual((resolved.preset, resolved.model, resolved.effort, resolved.timeout, resolved.preset_overridden), ("multi-4", "grok-4.3", "low", 60, True))
        resolved = config("--model", "grok-4.20-multi-agent")
        self.assertEqual((resolved.effort, resolved.timeout, resolved.preset_overridden), ("low", 300, False))

    def test_cross_family_overrides_reset_effort(self):
        resolved = config("--preset", "multi-16", "--model", "grok-4.5")
        self.assertEqual((resolved.effort, search.agent_count("grok-4.5", resolved.effort), resolved.timeout, resolved.preset_overridden), ("low", 1, 60, True))
        resolved = config("--preset", "single", "--model", "grok-4.20-multi-agent")
        self.assertEqual((resolved.effort, search.agent_count("multi-agent", resolved.effort), resolved.timeout, resolved.preset_overridden), ("low", 4, 300, True))

    def test_unknown_models(self):
        resolved = config("--model", "other-model")
        self.assertEqual((resolved.effort, search.agent_count("unknown", resolved.effort), resolved.timeout), (None, None, 600))
        resolved = config("--model", "other-model", "--effort", "high")
        self.assertEqual((resolved.effort, resolved.timeout), ("high", 600))
        self.assertEqual(search.model_family("grok-latest"), "unknown")
        self.assertEqual(search.model_family("grok-4.30"), "unknown")

    def test_explicit_timeout_and_effort_change_agent_count(self):
        self.assertEqual(config("--timeout", "42").timeout, 42)
        resolved = config("--preset", "multi-4", "--effort", "high")
        self.assertEqual((search.agent_count("multi-agent", resolved.effort), resolved.timeout), (16, 600))

    def test_effort_changes_timeout_and_multi_agent_count(self):
        for effort, count, timeout in (("medium", 4, 300), ("high", 16, 600)):
            resolved = config("--effort", effort)
            self.assertEqual((search.agent_count("multi-agent", resolved.effort), resolved.timeout, resolved.preset_overridden), (count, timeout, True))
        for effort, count, timeout in (("medium", 4, 300), ("xhigh", 16, 600)):
            resolved = config("--preset", "multi-4", "--effort", effort)
            self.assertEqual((search.agent_count("multi-agent", resolved.effort), resolved.timeout), (count, timeout))

    def test_invalid_efforts(self):
        for arguments in (("--preset", "single", "--effort", "xhigh"), ("--model", "grok-4.5", "--effort", "none"), ("--model", "grok-4.5", "--effort", "xhigh"), ("--model", "grok-4.20-multi-agent", "--effort", "none")):
            with self.assertRaises(search.SearchError):
                config(*arguments)

    def test_request_summary_and_unknown_payload(self):
        resolved = config()
        summary = search.build_request_summary(resolved)
        self.assertEqual({key: summary[key] for key in ("preset_used", "preset_explicit", "preset_overridden", "model_used", "effort_sent", "agent_count", "timeout_seconds", "warnings")}, {"preset_used": "multi-4", "preset_explicit": False, "preset_overridden": False, "model_used": "grok-4.20-multi-agent", "effort_sent": "low", "agent_count": 4, "timeout_seconds": 300, "warnings": []})
        unknown = config("--model", "other-model")
        self.assertNotIn("reasoning", search.build_payload(unknown))

    def test_summary_warnings(self):
        grok_45 = search.build_request_summary(config("--model", "grok-4.5"))
        self.assertEqual(grok_45["warnings"], ["grok-4.5 has higher per-token pricing than grok-4.3.", "grok-4.5 is unavailable in EU regions."])
        unknown = search.build_request_summary(config("--model", "other-model"))
        self.assertEqual(unknown["warnings"], ["Unknown model family; reasoning defaults and agent count are not known."])
        self.assertIsNone(unknown["agent_count"])

    def test_citation_coverage_normalizes_trailing_punctuation(self):
        wiki = "https://en.wikipedia.org/wiki/XAI_(company)"
        example = "https://example.com"
        coverage = search.citation_coverage(f"[[1]]({wiki}). ({example}). {example}. https://unmatched.example/path.", [wiki, example])
        self.assertEqual(coverage["text_urls"], [wiki, example, "https://unmatched.example/path"])
        self.assertEqual(coverage["api_citation_urls"], [wiki, example])
        self.assertEqual(coverage["unmatched_text_urls"], ["https://unmatched.example/path"])

    def test_multi_agent_failure_does_not_fall_back(self):
        class FailingOpener:
            calls = 0

            def open(self, request, timeout):
                self.calls += 1
                raise urllib.error.HTTPError(request.full_url, 400, "Bad Request", email.message.Message(), None)

        opener = FailingOpener()
        with self.assertRaises(search.SearchError):
            search.execute_request(opener, "key", search.build_payload(config("--preset", "multi-4")), config("--preset", "multi-4"))
        self.assertEqual(opener.calls, 1)


class EnvironmentConfigurationTests(unittest.TestCase):
    def test_env_value_prefers_non_empty_os_value(self):
        with mock.patch.dict(os.environ, {"XAI_API_KEY": "os_key"}, clear=True):
            self.assertEqual(search.env_value({"XAI_API_KEY": "file_key"}, "XAI_API_KEY"), "os_key")
        with mock.patch.dict(os.environ, {"XAI_API_KEY": ""}, clear=True):
            self.assertEqual(search.env_value({"XAI_API_KEY": "file_key"}, "XAI_API_KEY"), "file_key")
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertEqual(search.env_value({"XAI_API_KEY": "file_key"}, "XAI_API_KEY"), "file_key")
            self.assertIsNone(search.env_value({}, "XAI_API_KEY"))

    def test_load_env_file_parses_supported_syntax(self):
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / ".env"
            path.write_text("# comment\n\nKEY=value\nexport EXPORTED=value\nSINGLE='value'\nDOUBLE=\"value\"\nEMPTY=\n", encoding="utf-8")
            self.assertEqual(search.load_env_file(path), {"KEY": "value", "EXPORTED": "value", "SINGLE": "value", "DOUBLE": "value", "EMPTY": ""})

    def test_load_env_file_rejects_malformed_line(self):
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / ".env"
            path.write_text("not a setting\n", encoding="utf-8")
            with self.assertRaisesRegex(search.SearchError, "Invalid .env line 1") as raised:
                search.load_env_file(path)
            self.assertEqual(raised.exception.code, "ENV_ERROR")
            self.assertEqual(raised.exception.exit_code, search.EXIT_ENV)

    def test_default_env_file_is_anchored_to_skill_root(self):
        self.assertEqual(search.default_env_file(), SCRIPT.parents[1] / ".env")

    def test_env_file_is_read_by_main(self):
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / ".env"
            path.write_text("XAI_API_KEY=file_key\n", encoding="utf-8")
            response = {"status": "completed", "output": [{"type": "message", "content": [{"type": "output_text", "text": "ok"}]}]}
            with capture_main_output(), mock.patch.dict(os.environ, {}, clear=True), mock.patch.object(search.sys, "argv", ["search.py", "--env-file", str(path), "test query"]), mock.patch.object(search, "execute_request", return_value=response) as execute:
                self.assertEqual(search.main(), 0)
            self.assertEqual(execute.call_args.args[1], "file_key")

    def test_missing_key_returns_env_error_without_request(self):
        with tempfile.TemporaryDirectory() as directory:
            missing_env = pathlib.Path(directory) / "missing.env"
            with capture_main_output() as output, mock.patch.dict(os.environ, {}, clear=True), mock.patch.object(search.sys, "argv", ["search.py", "--env-file", str(missing_env), "test query"]), mock.patch.object(search, "execute_request") as execute:
                self.assertEqual(search.main(), search.EXIT_ENV)
        self.assertEqual(json.loads(output.getvalue())["error"]["code"], "ENV_ERROR")
        execute.assert_not_called()

    def test_proxy_alias_prefers_uppercase_within_a_source(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertEqual(search.env_value({"HTTPS_PROXY": "upper", "https_proxy": "lower"}, "HTTPS_PROXY", "https_proxy"), "upper")


if __name__ == "__main__":
    unittest.main()
