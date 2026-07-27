# grok-search

An [Agent Skills](https://agentskills.io) skill for live Web and X (Twitter)
search through xAI Grok. Install it with:

```bash
npx skills add mcdp-adk/skills --skill grok-search
```

## What it does

Use it when you need actual external Web or X retrieval: current information,
recent discussions or events, a specified official document or account, a
historical date range, or outside verification of a claim. It is not a local
file or repository search tool, and it does not provide legal certification or
price predictions.

## Requirements and setup

- A Python 3.10+ runner, either an existing system interpreter or a managed
  interpreter that an already installed uv can obtain.
- The script uses only the Python standard library; no pip package is needed.
- An xAI API key from [console.x.ai](https://console.x.ai).

Copy `.env.example` to `.env` in this directory and set `XAI_API_KEY`, or set
`XAI_API_KEY` in the operating-system environment. A non-empty OS environment
value takes priority over `.env`. Optional proxy variables are
`HTTPS_PROXY`, `HTTP_PROXY`, `ALL_PROXY`, and `NO_PROXY`. A custom CA bundle can
be supplied with `--ca-bundle`.

The script loads `.env` automatically from the skill directory. Keep the file
private and do not put the API key in commands, logs, or source control.

### Runner fallback

Verify the first available runner with `--help`, in this order: `python`, the
platform runner (`py -3` on Windows or `python3` on Linux/macOS), then an
already installed `uv`.

```bash
python "scripts/search.py" --help
py -3 "scripts/search.py" --help          # Windows
python3 "scripts/search.py" --help        # Linux/macOS
uv run --no-project --python 3.10 "scripts/search.py" --help
```

Use the first command whose `--help` verification succeeds, then reuse that
runner for the real query. If the system or platform runner is unavailable, the
already installed uv fallback may download a managed Python 3.10 on its first
`uv run --no-project --python 3.10` and may need network access. Do not install
uv or pip packages, or use an independent installer. If that download is not
allowed, stop and provide an already available runner instead.

## Quick start

Run these commands from the `grok-search` directory:

```bash
python "scripts/search.py" --help
python "scripts/search.py" "what's the latest on EU AI Act enforcement"
python "scripts/search.py" --source x --since "7d" "developer reactions to MCP"
python "scripts/search.py" --source web --preset single --web-allow docs.python.org "asyncio TaskGroup"
```

Use the first runner whose `--help` command succeeds, and reuse it for the
session. The script writes the normal result as JSON to stdout; `Searching...`,
`Done.`, and retry notices are progress lines on stderr.

## Web and X time filters

`--since` and `--until` are strict, date-level filters for X. Web search has no
strict date filter, so `--source web --since ...` and `--source web --until ...`
fail. With `--source both`, the flags constrain only X. For Web freshness or
hour-level X freshness, put the time range directly in the query text, such as
“in the past 2 hours.” Relative values (`2h`, `7d`, `2w`, `today`, `yesterday`,
`now`) and ISO date/time values are interpreted in UTC.

## Presets

- `single`: one fact, specified page/account, or a speed-sensitive request; lowest relative cost.
- `multi-4`: default for ordinary searches; omit `--preset`.
- `multi-16`: highest relative cost; use only for an explicitly requested, genuinely deep and multi-faceted investigation.

## Troubleshooting

- `ENV_ERROR`: set `XAI_API_KEY` in `.env` or the OS environment; start a new
  terminal or agent process after changing environment variables.
- Authentication failure: the key is invalid or expired; replace it at
  [console.x.ai](https://console.x.ai).
- Argument failure: run `python "scripts/search.py" --help` and correct only a
  clearly local flag mistake that does not change the intended request or
  expected cost; Web still rejects `--since` and `--until`.
- After the script returns a final API, connection, or timeout error, do not
  automatically start a second CLI call. Internal retries remain the script's
  responsibility; a timeout may already have been processed.
- The script never automatically changes the preset, model, or effort; any
  retry that changes one requires your explicit decision.

## License

[MIT](LICENSE)

For model/effort semantics, filter limits, retry behavior, proxy precedence,
output formats, and uncommon errors, see
[references/references.md](references/references.md).
