# grok-search

An [Agent Skills](https://agentskills.io) skill for retrieving live Web and X
content through xAI Grok. Use it for current information, specified pages or
accounts, historical date ranges, and external verification—not for local file
search, legal certification, or price prediction.

## Install

The Vercel Labs `skills` CLI requires Node.js 22.20 or newer.

```bash
npx skills add mcdp-adk/skills --skill grok-search
```

## Set up

You need:

- Python 3.10 or newer. The bundled script uses only the standard library.
- An xAI API key from [console.x.ai](https://console.x.ai).

Copy `.env.example` to `.env` in this directory and set `XAI_API_KEY`, or set it
in the operating-system environment. A non-empty OS environment value takes
priority. Keep the key out of commands, logs, and source control.

The skill also supports `HTTPS_PROXY`, `HTTP_PROXY`, `ALL_PROXY`, `NO_PROXY`,
and a custom CA bundle through `--ca-bundle`.

## Run a search

Once installed and configured, ask your agent for information that requires
live Web or X retrieval. To run the bundled CLI directly, use these commands
from the `grok-search` directory:

```bash
python "scripts/search.py" --help
python "scripts/search.py" "what's the latest on EU AI Act enforcement"
python "scripts/search.py" --source x --since "7d" "developer reactions to MCP"
python "scripts/search.py" --source web --preset single --web-allow docs.python.org "asyncio TaskGroup"
```

If `python` is unavailable, try `py -3` on Windows, `python3` on Linux or macOS,
then an already installed `uv` with `uv run --no-project`. Verify the runner
with `--help` once and reuse it for the session. No pip packages are required.

The CLI writes result JSON to stdout. Progress and retry notices go to stderr.
Treat citations as candidate sources, and check the cited pages before relying
on important claims.

## Choose the request

| Option | Use it for |
|---|---|
| `--source web\|x\|both` | Select Web, X, or both. The default is both. |
| `--preset single\|multi-4\|multi-16` | Use `single` for one fact or speed, omit the option for ordinary searches (`multi-4`), and reserve `multi-16` for explicitly requested deep research. |
| `--since` / `--until` | Apply strict, date-level filters to X. Web search does not support these filters; state Web freshness in the query instead. |
| `--web-allow`, `--web-exclude`, `--x-allow`, `--x-exclude` | Limit Web domains or X accounts. Do not combine allow and exclude for the same source. |
| `--continue RESPONSE_ID` | Continue a previous response to fill a known gap or audit its evidence. |

Relative time values such as `2h`, `7d`, `today`, and `yesterday`, as well as ISO
date and time values, are interpreted in UTC.

## Troubleshoot

- `ENV_ERROR`: set `XAI_API_KEY` in `.env` or the OS environment, then start a
  new terminal or agent process.
- Authentication failure: replace an invalid or expired key at
  [console.x.ai](https://console.x.ai).
- Argument failure: run the script with `--help` and correct the reported flag.
- Final API, connection, or timeout error: report the failure before starting a
  new call. The script manages eligible retries internally, and a timeout may
  already have reached the service.

For model and effort semantics, media options, filter limits, retry behavior,
proxy precedence, output fields, and uncommon errors, see
[references/references.md](references/references.md).
