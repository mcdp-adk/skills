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


class PresetResolutionTests(unittest.TestCase):
    def test_payload_uses_tools_as_the_only_source_selector(self):
        for source, expected_tools in (
            ("web", ["web_search"]),
            ("x", ["x_search"]),
            ("both", ["web_search", "x_search"]),
        ):
            with self.subTest(source=source):
                payload = search.build_payload(
                    config(
                        "--source",
                        source,
                        "--since",
                        "2026-07-01",
                        "--until",
                        "2026-07-02",
                        "--max-results",
                        "3",
                    )
                )
                self.assertEqual([tool["type"] for tool in payload["tools"]], expected_tools)
                self.assertNotIn("sources", payload["search_parameters"])
                self.assertEqual(payload["search_parameters"]["mode"], "on")
                self.assertIs(payload["search_parameters"]["return_citations"], True)
                self.assertEqual(payload["search_parameters"]["from_date"], "2026-07-01")
                self.assertEqual(payload["search_parameters"]["to_date"], "2026-07-02")
                self.assertEqual(payload["search_parameters"]["max_search_results"], 3)

    def test_default_single(self):
        resolved = config()
        self.assertEqual((resolved.model, resolved.effort, search.agent_count(search.model_family(resolved.model), resolved.effort), resolved.timeout), ("grok-4.3", "low", 1, 60))
        self.assertFalse(resolved.preset_explicit)

    def test_multi_presets(self):
        for preset, effort, count, timeout in (("multi-4", "low", 4, 300), ("multi-16", "high", 16, 600)):
            resolved = config("--preset", preset)
            self.assertEqual((resolved.effort, search.agent_count("multi-agent", resolved.effort), resolved.timeout), (effort, count, timeout))

    def test_same_family_and_date_pinned_overrides_keep_preset_effort(self):
        for model in ("grok-4.3-custom", "grok-4.3-0309"):
            resolved = config("--model", model)
            self.assertEqual((resolved.effort, resolved.timeout, resolved.preset_overridden), ("low", 60, True))

    def test_cross_family_overrides_reset_effort(self):
        resolved = config("--preset", "multi-16", "--model", "grok-4.5")
        self.assertEqual((resolved.effort, search.agent_count("grok-4.5", resolved.effort), resolved.timeout, resolved.preset_overridden), ("low", 1, 60, True))
        resolved = config("--model", "grok-4.20-multi-agent")
        self.assertEqual((resolved.effort, search.agent_count("multi-agent", resolved.effort), resolved.timeout), ("low", 4, 300))

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
        for effort in ("medium", "high"):
            self.assertEqual(config("--effort", effort).timeout, 120)
        for effort, count, timeout in (("medium", 4, 300), ("xhigh", 16, 600)):
            resolved = config("--preset", "multi-4", "--effort", effort)
            self.assertEqual((search.agent_count("multi-agent", resolved.effort), resolved.timeout), (count, timeout))

    def test_invalid_efforts(self):
        for arguments in (("--effort", "xhigh"), ("--model", "grok-4.5", "--effort", "none"), ("--model", "grok-4.5", "--effort", "xhigh"), ("--model", "grok-4.20-multi-agent", "--effort", "none")):
            with self.assertRaises(search.SearchError):
                config(*arguments)

    def test_request_summary_and_unknown_payload(self):
        resolved = config()
        summary = search.build_request_summary(resolved)
        self.assertEqual({key: summary[key] for key in ("preset_used", "preset_explicit", "preset_overridden", "model_used", "effort_sent", "agent_count", "timeout_seconds", "warnings")}, {"preset_used": "single", "preset_explicit": False, "preset_overridden": False, "model_used": "grok-4.3", "effort_sent": "low", "agent_count": 1, "timeout_seconds": 60, "warnings": []})
        unknown = config("--model", "other-model")
        self.assertNotIn("reasoning", search.build_payload(unknown))

    def test_summary_warnings_and_preset_flags(self):
        grok_45 = search.build_request_summary(config("--model", "grok-4.5"))
        self.assertEqual(grok_45["warnings"], ["grok-4.5 costs more than the default grok-4.3 model.", "grok-4.5 is unavailable in EU regions."])
        unknown = search.build_request_summary(config("--model", "other-model"))
        self.assertEqual(unknown["warnings"], ["Unknown model family; reasoning defaults and agent count are not known."])
        self.assertIsNone(unknown["agent_count"])
        self.assertTrue(config("--preset", "single").preset_explicit)
        self.assertFalse(config("--model", "grok-4.3").preset_overridden)

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
            with mock.patch.dict(os.environ, {}, clear=True), mock.patch.object(search.sys, "argv", ["search.py", "--env-file", str(path), "test query"]), mock.patch.object(search, "execute_request", return_value=response) as execute:
                self.assertEqual(search.main(), 0)
            self.assertEqual(execute.call_args.args[1], "file_key")

    def test_missing_key_returns_env_error_without_request(self):
        output = io.StringIO()
        with mock.patch.dict(os.environ, {}, clear=True), mock.patch.object(search.sys, "argv", ["search.py", "test query"]), mock.patch.object(search, "execute_request") as execute, mock.patch.object(search.sys, "stdout", output):
            self.assertEqual(search.main(), search.EXIT_ENV)
        self.assertEqual(json.loads(output.getvalue())["error"]["code"], "ENV_ERROR")
        execute.assert_not_called()

    def test_malformed_env_file_returns_env_error(self):
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / ".env"
            path.write_text("not a setting\n", encoding="utf-8")
            with mock.patch.dict(os.environ, {}, clear=True), mock.patch.object(search.sys, "argv", ["search.py", "--env-file", str(path), "test query"]):
                self.assertEqual(search.main(), search.EXIT_ENV)

    def test_proxy_alias_prefers_uppercase_within_a_source(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertEqual(search.env_value({"HTTPS_PROXY": "upper", "https_proxy": "lower"}, "HTTPS_PROXY", "https_proxy"), "upper")


if __name__ == "__main__":
    unittest.main()
