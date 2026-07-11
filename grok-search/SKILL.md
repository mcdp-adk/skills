---
name: grok-search
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

## How to search

```bash
python3 {baseDir}/scripts/search.py "your query here"
```

The script exposes what the API can do, grouped into 6 parameters. Pick the combination that matches what the user wants.

### The 6 parameters

| Parameter | What it controls | Default |
|---|---|---|
| `--source web\|x\|both` | Where to search | `both` |
| `--depth fast\|deep` | How deep to search | `fast` |
| `--since` / `--until` | Time window | none |
| `--web-allow` / `--web-exclude` / `--x-allow` / `--x-exclude` | Restrict sources | none |
| `--continue RESPONSE_ID` | Continue a previous search | none |
| `--image-understanding` / `--video-understanding` | Analyze media in results | off |

Advanced options (`--model`, `--effort`, `--max-results`, `--timeout`, `--max-retries`, `--env-file`, `--ca-bundle`, `--raw`) are available — run `python3 {baseDir}/scripts/search.py --help` for details.

**Time formats**: relative (`2h`, `7d`, `2w`, `yesterday`, `today`, `now`) or ISO date (`2026-07-01`). All times are UTC.

**Important time fact**: X search supports strict date filtering. Web search does NOT — `--since`/`--until` for web is only a model-level hint, not a strict filter. When web recency matters, also state the time range explicitly in the query text.

**Time precision**: `--since`/`--until` accept hour-level input like `2h`, but the API only accepts date-level (`YYYY-MM-DD`). So `--since 2h` becomes the UTC date containing the resolved timestamp — it's a date-level filter, not an hour-level window. For precise hour-level recency, state the exact time range in the query text (e.g. "in the past 2 hours").

### Depth: fast vs deep

- `fast` (default): single-agent `grok-4.3`, quick live search. Use for most queries.
- `deep`: multi-agent `grok-4.20-multi-agent` with 16 agents. Significantly higher cost (multiple agents, each with its own token usage and tool calls), 9 requests/sec limit, much slower. Only for broad, multi-source research where fast isn't enough.

Don't confuse "I want a longer answer" with "I need deep research". Deep is for breadth and cross-source synthesis, not for depth of a single-topic answer.

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
    "model": "grok-4.3",
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
python3 {baseDir}/scripts/search.py --source both --since "24h" "Track [EVENT] in the past 24 hours. Build a timeline ordered by when things happened. For each item, label it: confirmed (primary source or 2+ independent credible sources), reported (named credible outlet but not independently confirmed), or X-only/unconfirmed (social signal only). List both the event time and the source publication time. Do not treat X posts as fact confirmation."
```

Upgrade to `--depth deep` if sources conflict or the event spans multiple parties.

### X sentiment and reactions

```bash
python3 {baseDir}/scripts/search.py --source x --since "7d" "Analyze X discussion about [TOPIC] in [TIME RANGE]. Give the main viewpoints, disagreements, recurring arguments, and representative posts. Describe the qualitative sentiment shape — do not give percentages without sampling methodology. Distinguish official accounts, domain experts, regular users, and low-quality/coordinated signals."
```

For specific accounts, add `--x-allow handle1 --x-allow handle2`.

### Fact-checking and narrative comparison

```bash
python3 {baseDir}/scripts/search.py --source both "Fact-check this claim: [CLAIM]. Find supporting, refuting, and unconfirmable evidence. For each piece: source URL, publication date, source type, and which part of the claim it supports or refutes. Separately list where X narrative and web/primary sources diverge. End with: conclusion, confidence level, unresolved questions, coverage limitations."
```

For technical claims, add `--web-allow arxiv.org --web-allow github.com` to restrict to authoritative sources.

### Market and competitive intelligence

```bash
python3 {baseDir}/scripts/search.py --source both "Analyze [COMPANY/PRODUCT] in [TIME RANGE]: 1. Official announcements, funding, product launches, pricing changes. 2. Actual user/developer/analyst reactions on X. 3. Competitor responses. Separate confirmed facts, speculation, and social signals."
```

Use `--depth deep` for cross-company or cross-market analysis.

### Deep multi-source research

```bash
# First round
python3 {baseDir}/scripts/search.py --source both --depth deep "Research [QUESTION]. Define scope, time window, key sub-questions, and evidence standards. Give preliminary findings, conflicting evidence, and gaps that still need verification."

# Follow-up rounds (use response_id from previous output)
python3 {baseDir}/scripts/search.py --source both --depth deep --continue resp_abc123 "Address the gaps from the previous round: [SPECIFIC SUB-QUESTION]. Audit whether previous conclusions are supported by primary sources. Revise any conclusions with insufficient evidence."
```

Only use `deep` when the task is broad, has conflicting sources, or needs cross-source synthesis. Multi-turn value is auditing previous gaps, not just asking "more detail".

### Technical documentation lookup

```bash
python3 {baseDir}/scripts/search.py --source web --web-allow docs.python.org --web-allow github.com "Find current official documentation for [TOPIC]. Prefer original docs over blog posts. Note version numbers and publication dates."
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
- Scraping X at scale (rate limits: 37 requests/sec fast, 9 requests/sec deep)
- Legal opinions, compliance certification, or formal fact adjudication (AI-generated citations may not support their attached claims)
- Trading signals or price predictions (latency and rate limits make this unsuitable)

## Limitations

- Breaking news on X can be noisy — early posts often outrun reliable confirmation
- Web search has no strict date filter — express time windows in the query text
- Paywalled or private content is not accessible
- Multi-agent deep research is slow (can take minutes) and has significantly higher cost (multiple agents, each with its own token usage and tool calls)
- Over-filtering can hide the best evidence — start broad, then narrow
- **Verify important citations against the source pages** — not all sources support the claims they're attached to
- Citation hallucination rate is significant — AI-generated citations may not actually support the claims they're attached to. Always verify against source pages.

## References

- [references.md](references/references.md) — API fields, models, constraints, pricing, and parameter-to-API mapping details.
