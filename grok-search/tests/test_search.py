import email.message
import importlib.util
import pathlib
import sys
import unittest
import urllib.error


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

    def test_explicit_timeout_and_effort_change_agent_count(self):
        self.assertEqual(config("--timeout", "42").timeout, 42)
        resolved = config("--preset", "multi-4", "--effort", "high")
        self.assertEqual((search.agent_count("multi-agent", resolved.effort), resolved.timeout), (16, 600))

    def test_invalid_efforts(self):
        for arguments in (("--effort", "xhigh"), ("--model", "grok-4.5", "--effort", "none"), ("--model", "grok-4.20-multi-agent", "--effort", "none")):
            with self.assertRaises(search.SearchError):
                config(*arguments)

    def test_request_summary_and_unknown_payload(self):
        resolved = config()
        summary = search.build_request_summary(resolved)
        self.assertEqual({key: summary[key] for key in ("preset_used", "preset_explicit", "preset_overridden", "model_used", "effort_sent", "agent_count", "timeout_seconds", "warnings")}, {"preset_used": "single", "preset_explicit": False, "preset_overridden": False, "model_used": "grok-4.3", "effort_sent": "low", "agent_count": 1, "timeout_seconds": 60, "warnings": []})
        unknown = config("--model", "other-model")
        self.assertNotIn("reasoning", search.build_payload(unknown))

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


if __name__ == "__main__":
    unittest.main()
