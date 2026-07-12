# grok-search

An [Agent Skills](https://agentskills.io) skill for real-time web and X (Twitter) search powered by xAI Grok. Manageable via `npx skills add mcdp-adk/skills --skill grok-search`.

## What it does

- **Web Search** — Real-time web search with domain filtering
- **X Search** — X platform post search with date range and account filtering
- **Preset Selection** — Choose `single` (1 agent), `multi-4` (4 agents), or `multi-16` (16 agents)

## Setup

1. Get an API key from [console.x.ai](https://console.x.ai)
2. Copy `.env.example` to `.env` and set `XAI_API_KEY`
3. Optional: add proxy variables such as `HTTPS_PROXY` or `ALL_PROXY`

## Quick start

Run these commands from the `grok-search` directory:

```bash
uv run --no-project --python 3.10 "scripts/search.py" "what's the latest on EU AI Act enforcement"
uv run --no-project --python 3.10 "scripts/search.py" --source x --since "7d" "developer reactions to MCP"
uv run --no-project --python 3.10 "scripts/search.py" --source web --web-allow docs.python.org "asyncio TaskGroup"
uv run --no-project --python 3.10 "scripts/search.py" --preset multi-16 "competitive analysis of AI coding assistants"
```

Run `uv run --no-project --python 3.10 "scripts/search.py" --help` for all options.

## Time filters and citations

`--since` and `--until` are strict X search time filters. Web search has no date filter: put the web time range in the query text. `--source web --since ...` and `--source web --until ...` are rejected; with `--source both`, these flags constrain only X search.

The JSON `citations` list is collected from `output_text.annotations` URL citations. The request uses Agent Tools as its sole source selector and does not send deprecated top-level live-search configuration, mode, citation-return, or result-limit fields.

See [SKILL.md](SKILL.md#troubleshooting) → Troubleshooting for exit codes, `ENV_ERROR`, and configuration priority.

## Presets and overrides

`single` is the default: `grok-4.3` with `low` effort and 1 agent. `multi-4` uses `grok-4.20-multi-agent` with `low` effort and 4 agents; `multi-16` uses the same model with `high` effort and 16 agents. These presets only select the actual model and agent count; they do not promise broader search, deeper answers, or higher quality.

`--model` and `--effort` override a preset. When `--model` crosses model families without an explicit `--effort`, the script resets effort to `low` for known families; unknown models get no inferred effort. xAI's official default for `grok-4.5` is `high`, while this skill sends `low` unless `--effort` is explicit. The multi-agent model is Beta and does not automatically fall back to `single` if a request fails.

## Requirements

- Python 3.10+
- The script is stdlib-only; no `pip install` is required.
- Preferred runner: `uv run --no-project --python 3.10 "scripts/search.py" [args]`. `uv` is a recommended runner, not a script dependency.
- Without `uv`, use a compatible Python 3.10+ interpreter:
  - Unix/macOS: `python3 "scripts/search.py" [args]`
  - Windows: `py -3 "scripts/search.py" [args]`

## License

[MIT](LICENSE)
