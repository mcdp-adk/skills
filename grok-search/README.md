# grok-search

An [Agent Skills](https://agentskills.io) skill for real-time web and X (Twitter) search powered by xAI Grok. Manageable via `npx skills add mcdp-adk/skills --skill grok-search`.

## What it does

- **Web Search** — Real-time web search with domain filtering
- **X Search** — X platform post search with date range and account filtering
- **Deep Research** — Optional multi-agent search and synthesis (`--depth deep`, 16 agents, 5-20x cost)

## Setup

1. Get an API key from [console.x.ai](https://console.x.ai)
2. Copy `.env.example` to `.env` and set `XAI_API_KEY`
3. Optional: add proxy variables such as `HTTPS_PROXY` or `ALL_PROXY`

## Quick start

```bash
python3 scripts/search.py "what's the latest on EU AI Act enforcement"
python3 scripts/search.py --source x --since "7d" "developer reactions to MCP"
python3 scripts/search.py --source web --web-allow docs.python.org "asyncio TaskGroup"
python3 scripts/search.py --depth deep "competitive analysis of AI coding assistants"
```

Run `python3 scripts/search.py --help` for all options.

## Requirements

- Python 3.10+
- No external dependencies (stdlib only)

## License

[MIT](LICENSE)
