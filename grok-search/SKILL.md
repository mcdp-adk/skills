---
name: grok-search
compatibility: Requires Python 3.10+. Prefers uv for automatic Python management.
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

## Setup

The script automatically loads `{baseDir}/.env` for authentication. Do NOT read, display, or copy the contents of `.env` — it contains the API key. If `XAI_API_KEY` is missing, tell the user to get a key at https://console.x.ai and create `{baseDir}/.env` from `{baseDir}/.env.example`.

- Required: `XAI_API_KEY=...`
- Optional: `HTTPS_PROXY`, `HTTP_PROXY`, `ALL_PROXY`, `NO_PROXY`, custom CA bundle via `--ca-bundle`

## Troubleshooting

### Exit codes

- Exit 1: runtime errors and script-level argument validation errors, such as using `--web-allow` with `--source x`.
- Exit 2: authentication failure (an invalid or expired API key), or argparse parsing errors such as an unknown flag or invalid preset value.
- Exit 3: environment configuration errors, such as a missing API key or malformed `.env` file.

### ENV_ERROR: API key not found

- Check that `<skill-root>/.env` exists and contains `XAI_API_KEY=your-key`.
- Or set the `XAI_API_KEY` OS environment variable.
- Priority is: non-empty OS environment variable > `.env` file.

### `--env-file`

Use `--env-file /path/to/.env` to specify a custom `.env` path.

### Windows

After changing an environment variable, restart the terminal or agent process. Running processes do not detect newly set variables.

### Security

- Do not expose API keys in logs or output.
- The script does not echo API keys.

## How to search

The script uses only the Python standard library; no `pip install` is required. Prefer `uv` as the runner:

```bash
uv run --no-project --python 3.10 "{baseDir}/scripts/search.py" "your query here"
```

If `uv` is unavailable, use a compatible Python 3.10+ interpreter:

- Unix/macOS:
  ```bash
  python3 "{baseDir}/scripts/search.py" "your query here"
  ```
- Windows:
  ```powershell
  py -3 "{baseDir}/scripts/search.py" "your query here"
  ```

The script exposes what the API can do, grouped into 6 parameters. Pick the combination that matches what the user wants.

### The 6 parameters

| Parameter | What it controls | Default |
|---|---|---|
| `--source web\|x\|both` | Where to search | `both` |
| `--preset single\|multi-4\|multi-16` | Select the actual model and agent count | `single` |
| `--since` / `--until` | Time window | none |
| `--web-allow` / `--web-exclude` / `--x-allow` / `--x-exclude` | Restrict sources | none |
| `--continue RESPONSE_ID` | Continue a previous search | none |
| `--image-understanding` / `--video-understanding` | Analyze media in results | off |

Advanced options (`--model`, `--effort`, `--max-results`, `--timeout`, `--max-retries`, `--env-file`, `--ca-bundle`, `--raw`) are available — run `uv run --no-project --python 3.10 "{baseDir}/scripts/search.py" --help` for details.

**Time formats**: relative (`2h`, `7d`, `2w`, `yesterday`, `today`, `now`) or ISO date (`2026-07-01`). All times are UTC.

**Important time fact**: X search supports strict date filtering. Web search does NOT — `--since`/`--until` for web is only a model-level hint, not a strict filter. When web recency matters, also state the time range explicitly in the query text.

**Time precision**: `--since`/`--until` accept hour-level input like `2h`, but the API only accepts date-level (`YYYY-MM-DD`). So `--since 2h` becomes the UTC date containing the resolved timestamp — it's a date-level filter, not an hour-level window. For precise hour-level recency, state the exact time range in the query text (e.g. "in the past 2 hours").

### Preset：模型与 agent 数

- `single`（默认）：`grok-4.3`，`low` effort，1 个 agent。
- `multi-4`：`grok-4.20-multi-agent`，`low` effort，4 个 agent。
- `multi-16`：`grok-4.20-multi-agent`，`high` effort，16 个 agent。

这三个 preset 只表示实际使用的模型和 agent 数，不保证搜索范围、答案深度或质量。multi-agent 是 Beta；请求失败时不会自动降级或改用 single。

`--model` 和 `--effort` 可覆盖 preset。若显式 `--model` 切换到不同模型家族且未传 `--effort`，脚本会重置为该家族的 `low`；未知模型则不推断 effort。`grok-4.5` 的官方默认 effort 是 `high`，但本 skill 在未显式传 `--effort` 时使用 `low`。

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
    "model_search_hint": "non_strict",
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
- `request_summary` — tells you what actually happened (especially whether web time was strict or just a hint)
- `citation_coverage` — checks if URLs in the answer text appear in the API's citations list. This is mechanical URL matching, NOT fact verification. A URL being present doesn't mean the source supports the claim.

## Decision guide: what does the user want?

### Real-time events (breaking news, outages, announcements)

```bash
uv run --no-project --python 3.10 "{baseDir}/scripts/search.py" --source both --since "24h" "Track [EVENT] in the past 24 hours. Build a timeline ordered by when things happened. For each item, label it: confirmed (primary source or 2+ independent credible sources), reported (named credible outlet but not independently confirmed), or X-only/unconfirmed (social signal only). List both the event time and the source publication time. Do not treat X posts as fact confirmation."
```

如需使用 multi-agent，可选择 `--preset multi-4` 或 `--preset multi-16`。

### X sentiment and reactions

```bash
uv run --no-project --python 3.10 "{baseDir}/scripts/search.py" --source x --since "7d" "Analyze X discussion about [TOPIC] in [TIME RANGE]. Give the main viewpoints, disagreements, recurring arguments, and representative posts. Describe the qualitative sentiment shape — do not give percentages without sampling methodology. Distinguish official accounts, domain experts, regular users, and low-quality/coordinated signals."
```

For specific accounts, add `--x-allow handle1 --x-allow handle2`.

### Fact-checking and narrative comparison

```bash
uv run --no-project --python 3.10 "{baseDir}/scripts/search.py" --source both "Fact-check this claim: [CLAIM]. Find supporting, refuting, and unconfirmable evidence. For each piece: source URL, publication date, source type, and which part of the claim it supports or refutes. Separately list where X narrative and web/primary sources diverge. End with: conclusion, confidence level, unresolved questions, coverage limitations."
```

For technical claims, add `--web-allow arxiv.org --web-allow github.com` to restrict to authoritative sources.

### Market and competitive intelligence

```bash
uv run --no-project --python 3.10 "{baseDir}/scripts/search.py" --source both "Analyze [COMPANY/PRODUCT] in [TIME RANGE]: 1. Official announcements, funding, product launches, pricing changes. 2. Actual user/developer/analyst reactions on X. 3. Competitor responses. Separate confirmed facts, speculation, and social signals."
```

跨公司或跨市场分析可选择 `--preset multi-4` 或 `--preset multi-16`。

### Multi-agent multi-source research

```bash
# First round
uv run --no-project --python 3.10 "{baseDir}/scripts/search.py" --source both --preset multi-16 "Research [QUESTION]. Define scope, time window, key sub-questions, and evidence standards. Give preliminary findings, conflicting evidence, and gaps that still need verification."

# Follow-up rounds (use response_id from previous output)
uv run --no-project --python 3.10 "{baseDir}/scripts/search.py" --source both --preset multi-16 --continue resp_abc123 "Address the gaps from the previous round: [SPECIFIC SUB-QUESTION]. Audit whether previous conclusions are supported by primary sources. Revise any conclusions with insufficient evidence."
```

Multi-turn value is auditing previous gaps, not just asking "more detail". Multi-agent is Beta and does not automatically fall back to `single` on failure. If a multi-agent request fails, report the failure to the user. Do not retry with `single` or change models without the user's approval.

### Technical documentation lookup

```bash
uv run --no-project --python 3.10 "{baseDir}/scripts/search.py" --source web --web-allow docs.python.org --web-allow github.com "Find current official documentation for [TOPIC]. Prefer original docs over blog posts. Note version numbers and publication dates."
```

Domain whitelist supports max 5 domains.

## Universal evidence rules

Apply these to every search result, regardless of intent:

1. **Citation verification**: The API's `citations` array is a candidate source list, not verified evidence. A URL appearing there doesn't mean the source supports the claim. Only treat a source as evidence after checking the page content actually supports the claim. URLs in `citation_coverage.unmatched_text_urls` are not backed by API citations — treat them as unverified.

2. **Evidence tiering**: Label each source: Tier 1 (official/academic), Tier 2 (industry media), Tier 3 (social media). Don't present Tier 3 as if it were Tier 1.

3. **Uncertainty labeling**: For high-stakes outputs, explicitly state: what's confirmed, what's conflicting, what's social-only, what has insufficient evidence, and what the coverage limitations are.

4. **Anti-bot is heuristic only**: You can ask the query to ignore duplicate text, promotional content, and low-information posts. But this is not bot detection — don't claim you've filtered bots or computed real sentiment statistics.

5. **Time honesty**: X time filtering is strict. Web time is a hint only. If web recency matters, the query text must state the time range, and you should ask the model to note each web source's publication date.

## When NOT to use this skill

- Local file search or code analysis
- Questions where training data is sufficient and freshness doesn't matter
- Historical X coverage may be incomplete — verify coverage before relying on it for older events
- Scraping X at scale (rate limits vary by model; multi-agent is limited to 9 requests/sec)
- Legal opinions, compliance certification, or formal fact adjudication (AI-generated citations may not support their attached claims)
- Trading signals or price predictions (latency and rate limits make this unsuitable)

## Limitations

- Breaking news on X can be noisy — early posts often outrun reliable confirmation
- Web search has no strict date filter — express time windows in the query text
- Paywalled or private content is not accessible
- Multi-agent requests can take minutes and have significantly higher cost (multiple agents, each with its own token usage and tool calls)
- Over-filtering can hide the best evidence — start broad, then narrow
- **Verify important citations against their source pages** — AI-generated citations may not support the claims attached to them.

## References

- [references.md](references/references.md) — API fields, models, constraints, pricing, and parameter-to-API mapping details.
