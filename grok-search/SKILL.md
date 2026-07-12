---
name: grok-search
compatibility: Requires a Python 3.10+ runner (try python, then uv, then platform python). Stdlib-only.
description: >
  Real-time web and X (Twitter) search powered by xAI Grok. Use this skill whenever
  the user wants current information, recent news, live data, X/Twitter posts, trending
  topics, sentiment, fact-checking, or anything requiring up-to-date internet data.
  Trigger when the user says "search for", "look up", "what's the latest on", "find
  recent", "what are people saying about", "check X/Twitter for", "news about",
  "current status of", "is this true", "verify this claim", or asks about something
  time-sensitive that a language model wouldn't know from training data alone.
  Also trigger proactively when a question clearly needs current information,
  real-time data, social media sentiment, or fact verification against live sources.
  Do NOT trigger for local file search, code analysis, or tasks that don't need
  live internet data.
---

# Grok Search

Search the live web and X with xAI's Grok. Use it when freshness matters — static model knowledge is often wrong or incomplete for breaking news, active discussions, and fast-moving facts.

## How to run

All examples below use `python "{baseDir}/scripts/search.py"` as the call structure — it is platform- and backend-agnostic, not a copy-paste command. Before the first search, pick a runner that actually works on this machine, in this order:

1. `python` — try it first.
2. No `python`, or it's a broken stub (e.g. the Windows Store placeholder that silently no-ops)? Use `uv`, which can fetch Python 3.10 on its own:
   ```bash
   uv run --no-project --python 3.10 "{baseDir}/scripts/search.py" --help
   ```
3. No `uv` either? Use the platform Python: `py -3` on Windows, `python3` on Linux/macOS.

Verify once with `--help`, then keep that runner for the whole session. Don't install `uv`, Python, or `pip`. Don't switch runners after a real query starts — the script retries internally.

## Setup

The script automatically loads `{baseDir}/.env` for authentication. Do NOT read, display, copy, or parse `.env`; the agent must leave it to the script. If the key is missing, follow the script's `ENV_ERROR` guidance and tell the user to configure it.

- Required: `XAI_API_KEY=...`
- Optional: `HTTPS_PROXY`, `HTTP_PROXY`, `ALL_PROXY`, `NO_PROXY`, custom CA bundle via `--ca-bundle`

## How to search

```bash
python "{baseDir}/scripts/search.py" "your query here"
```

The script exposes what the API can do, grouped into 6 parameters. Pick the combination that matches what the user wants.

### The 6 parameters

| Parameter | What it controls | Default |
|---|---|---|
| `--source web\|x\|both` | Where to search | `both` |
| `--preset single\|multi-4\|multi-16` | Select the actual model and agent count | `single` |
| `--since` / `--until` | X search time window | none |
| `--web-allow` / `--web-exclude` / `--x-allow` / `--x-exclude` | Restrict sources | none |
| `--continue RESPONSE_ID` | Continue a previous search | none |
| `--image-understanding` / `--video-understanding` | Analyze media in results | off |

Advanced options (`--model`, `--effort`, `--timeout`, `--max-retries`, `--env-file`, `--ca-bundle`, `--raw`) are available — run `python "{baseDir}/scripts/search.py" --help` for details.

**Time formats**: relative (`2h`, `7d`, `2w`, `yesterday`, `today`, `now`) or ISO date (`2026-07-01`). All times are UTC.

**X vs web time**: X search supports strict date filtering via `--since`/`--until`. Web search does NOT — `--source web --since ...` is rejected. When web recency matters, state the time range explicitly in the query text. With `--source both`, the flags constrain only X search. Note: `--since 2h` resolves to a date-level filter (the UTC date containing that timestamp), not an hour-level window — for precise hour-level recency, state the exact range in the query text (e.g. "in the past 2 hours").

### Preset: model and agent count

- `single` (default): `grok-4.3`, `low` effort, 1 agent.
- `multi-4`: `grok-4.20-multi-agent`, `low` effort, 4 agents.
- `multi-16`: `grok-4.20-multi-agent`, `high` effort, 16 agents.

Presets only select the model and agent count; they do not promise broader search, deeper answers, or higher quality. multi-agent is Beta and does not auto-fall back to `single` on failure. `--model` and `--effort` override a preset — see [references.md](references/references.md) for override and effort semantics.

### Reading the result

The script outputs JSON to stdout:

```json
{
  "ok": true,
  "response_id": "resp_abc123",
  "text": "The synthesized answer...",
  "citations": ["https://example.com/source1"],
  "request_summary": {
    "source": "both",
    "preset_used": "single",
    "preset_explicit": false,
    "preset_overridden": false,
    "model_used": "grok-4.3",
    "effort_sent": "low",
    "agent_count": 1,
    "timeout_seconds": 60,
    "warnings": [],
    "x_time_filter": "strict",
    "web_strict_filter_available": false
  },
  "citation_coverage": {
    "text_urls": [],
    "api_citation_urls": [],
    "unmatched_text_urls": []
  },
  "usage": {"input_tokens": 1234, "output_tokens": 567}
}
```

- `response_id` — use with `--continue` for follow-up questions on the same topic
- `request_summary.x_time_filter` — tells you whether X time filtering was applied; web search has no time filter, so put its time range in the query text
- `citation_coverage` — checks if URLs in the answer text appear in the API's citations list. This is mechanical URL matching, NOT fact verification. A URL being present doesn't mean the source supports the claim.

## Decision guide: what does the user want?

### Real-time events (breaking news, outages, announcements)

```bash
python "{baseDir}/scripts/search.py" --source both --since "24h" "Track [EVENT] in the past 24 hours. Build a timeline ordered by when things happened. For each item, label it: confirmed (primary source or 2+ independent credible sources), reported (named credible outlet but not independently confirmed), or X-only/unconfirmed (social signal only). List both the event time and the source publication time. Do not treat X posts as fact confirmation."
```

For multi-agent, choose `--preset multi-4` or `--preset multi-16`.

### X sentiment and reactions

```bash
python "{baseDir}/scripts/search.py" --source x --since "7d" "Analyze X discussion about [TOPIC] in [TIME RANGE]. Give the main viewpoints, disagreements, recurring arguments, and representative posts. Describe the qualitative sentiment shape — do not give percentages without sampling methodology. Distinguish official accounts, domain experts, regular users, and low-quality/coordinated signals."
```

For specific accounts, add `--x-allow handle1 --x-allow handle2`.

### Fact-checking and narrative comparison

```bash
python "{baseDir}/scripts/search.py" --source both "Fact-check this claim: [CLAIM]. Find supporting, refuting, and unconfirmable evidence. For each piece: source URL, publication date, source type, and which part of the claim it supports or refutes. Separately list where X narrative and web/primary sources diverge. End with: conclusion, confidence level, unresolved questions, coverage limitations."
```

For technical claims, add `--web-allow arxiv.org --web-allow github.com` to restrict to authoritative sources.

### Market and competitive intelligence

```bash
python "{baseDir}/scripts/search.py" --source both "Analyze [COMPANY/PRODUCT] in [TIME RANGE]: 1. Official announcements, funding, product launches, pricing changes. 2. Actual user/developer/analyst reactions on X. 3. Competitor responses. Separate confirmed facts, speculation, and social signals."
```

For cross-company or cross-market analysis, choose `--preset multi-4` or `--preset multi-16`.

### Multi-agent multi-source research

```bash
# First round
python "{baseDir}/scripts/search.py" --source both --preset multi-16 "Research [QUESTION]. Define scope, time window, key sub-questions, and evidence standards. Give preliminary findings, conflicting evidence, and gaps that still need verification."

# Follow-up rounds (use response_id from previous output)
python "{baseDir}/scripts/search.py" --source both --preset multi-16 --continue resp_abc123 "Address the gaps from the previous round: [SPECIFIC SUB-QUESTION]. Audit whether previous conclusions are supported by primary sources. Revise any conclusions with insufficient evidence."
```

Multi-turn value is auditing previous gaps, not just asking "more detail". Multi-agent is Beta and does not automatically fall back to `single` on failure. If a multi-agent request fails, report the failure to the user. Do not retry with `single` or change models without the user's approval.

### Technical documentation lookup

```bash
python "{baseDir}/scripts/search.py" --source web --web-allow docs.python.org --web-allow github.com "Find current official documentation for [TOPIC]. Prefer original docs over blog posts. Note version numbers and publication dates."
```

Domain whitelist supports max 5 domains.

## Guardrails

### When NOT to use this skill

- Local file search or code analysis
- Questions where training data is sufficient and freshness doesn't matter
- Legal opinions, compliance certification, or formal fact adjudication
- Trading signals or price predictions (latency and rate limits make this unsuitable)

### Handling results

- **Citations are candidates, not verified evidence.** The `citations` list comes from `output_text.annotations` — a URL there doesn't mean the source supports the claim. Verify against source pages. URLs in `citation_coverage.unmatched_text_urls` are unverified.
- **Tier your sources:** Tier 1 (official/academic), Tier 2 (industry media), Tier 3 (social media). Don't present Tier 3 as if it were Tier 1.
- **Label uncertainty:** For high-stakes outputs, state what's confirmed, conflicting, social-only, or has insufficient evidence.
- **Anti-bot is heuristic only:** You can ask the query to ignore duplicates and spam, but this isn't bot detection — don't claim filtered bots or computed sentiment statistics.

### Constraints

- Web search has no date filter — state time ranges in the query text
- Breaking news on X is noisy — early posts often outrun confirmation
- Paywalled or private content is not accessible
- Multi-agent requests take minutes and cost significantly more (all agents' tokens are billed)
- Over-filtering hides the best evidence — start broad, then narrow
- Historical X coverage may be incomplete — verify coverage before relying on it for older events
- Scraping X at scale is limited by rate (multi-agent: 9 req/sec)

## Troubleshooting

### Exit codes

- Exit 1: runtime errors and script-level argument validation errors, such as using `--web-allow` with `--source x`.
- Exit 2: authentication failure (an invalid or expired API key), or argparse parsing errors such as an unknown flag or invalid preset value.
- Exit 3: environment configuration errors, such as a missing API key or malformed `.env` file.

### ENV_ERROR: API key not found

- Tell the user to get a key at https://console.x.ai and configure `XAI_API_KEY` in `<skill-root>/.env` using `.env.example`, or set the `XAI_API_KEY` OS environment variable.
- Priority is: non-empty OS environment variable > `.env` file.

### `--env-file`

Use `--env-file /path/to/.env` to specify a custom `.env` path.

### Windows

After changing an environment variable, restart the terminal or agent process. Running processes do not detect newly set variables.

### Security

- Do not expose API keys in logs or output.
- The script does not echo API keys.

## References

- [references.md](references/references.md) — API fields, models, constraints, pricing, and parameter-to-API mapping details.
