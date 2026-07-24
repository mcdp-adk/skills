# grok-search

An [Agent Skills](https://agentskills.io) skill for real-time web and X (Twitter) search powered by xAI Grok. Manageable via `npx skills add mcdp-adk/skills --skill grok-search`.

## What it does

- **Web Search** — Real-time web search with domain filtering
- **X Search** — X platform post search with date range and account filtering
- **Preset Selection** — Use the default `multi-4` (4 agents), or explicitly choose `single` (1 agent) or `multi-16` (16 agents)

## Setup

1. Get an API key from [console.x.ai](https://console.x.ai)
2. Copy `.env.example` to `.env` and set `XAI_API_KEY`
3. Optional: add proxy variables such as `HTTPS_PROXY` or `ALL_PROXY`

## Quick start

These examples use `python` as the call structure. Before running, pick a runner that works on your machine — see [SKILL.md's How to run](SKILL.md#how-to-run).

Run these commands from the `grok-search` directory:

```bash
python "scripts/search.py" "what's the latest on EU AI Act enforcement"
python "scripts/search.py" --source x --since "7d" "developer reactions to MCP"
python "scripts/search.py" --source web --preset single --web-allow docs.python.org "asyncio TaskGroup"
python "scripts/search.py" --preset multi-16 "competitive analysis of AI coding assistants"
```

Run `python "scripts/search.py" --help` for all options.

## Time filters and citations

`--since` and `--until` are strict X search time filters. Web search has no date filter: put the web time range in the query text. `--source web --since ...` and `--source web --until ...` are rejected; with `--source both`, these flags constrain only X search.

The JSON `citations` list is collected from `output_text.annotations` URL citations. The request uses Agent Tools as its sole source selector and does not send deprecated top-level live-search configuration, mode, citation-return, or result-limit fields.

See [SKILL.md](SKILL.md#troubleshooting) → Troubleshooting for exit codes, `ENV_ERROR`, and configuration priority.

## Presets and overrides

The three-tier selection rules are summarized as: explicit `single` for lightweight work, default `multi-4` for ordinary searches, and explicit `multi-16` only for user-requested comprehensive or deep, multi-faceted research. See [SKILL.md#preset-selection](SKILL.md#preset-selection) for the complete rules. Presets only select the actual model and agent count; they do not promise broader search, deeper answers, or higher quality.

`--model` and `--effort` override a preset. When `--model` crosses model families without an explicit `--effort`, the script resets effort to `low` for known families; unknown models get no inferred effort. xAI's official default for `grok-4.5` is `high`, while this skill sends `low` unless `--effort` is explicit. The multi-agent model is Beta: all agents' tokens are billed, requests may take minutes, and the multi-agent rate limit is 9 requests per second. It does not automatically fall back to `single` if a request fails.

## Requirements

- A Python 3.10+ runner. The script is stdlib-only; no `pip install` required.
- Try `python` first. If it's missing or broken, use `uv run --no-project --python 3.10 "scripts/search.py"` (uv fetches Python itself). No `uv` either? Use `py -3` on Windows, `python3` on Linux/macOS.

## License

[MIT](LICENSE)
