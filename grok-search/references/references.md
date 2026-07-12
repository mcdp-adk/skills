# API Reference

Details for the xAI Responses API as used by this skill. Sourced from [docs.x.ai](https://docs.x.ai), 2026-07.

Key pages: [models](https://docs.x.ai/developers/models), [web-search](https://docs.x.ai/developers/tools/web-search), [x-search](https://docs.x.ai/developers/tools/x-search), [citations](https://docs.x.ai/developers/tools/citations), [multi-agent](https://docs.x.ai/developers/model-capabilities/text/multi-agent)

## Endpoint

```
POST https://api.x.ai/v1/responses
```

Headers: `Authorization: Bearer <key>`, `Content-Type: application/json`

## Models

| Model | Context | Input $/M | Output $/M | Req/sec | Use for |
|---|---|---|---|---|---|
| `grok-4.3` (skill default) | 1M | $1.25 | $2.50 | 37 | Single-agent live search |
| `grok-4.20-multi-agent` | 1M | $1.25 | $2.50 | 9 | Beta multi-agent model |
| `grok-4.5` | 500K | $2.00 | $6.00 | 150 | Reasoning always on; unavailable in the EU |

### Skill presets

| Preset | Model | effort | Agent count |
|---|---|---|---|
| `single` (default) | `grok-4.3` | `low` | 1 |
| `multi-4` | `grok-4.20-multi-agent` | `low` | 4 |
| `multi-16` | `grok-4.20-multi-agent` | `high` | 16 |

Presets only select the actual model and agent count; they do not promise search scope, answer depth, or quality. `--model` and `--effort` override the preset. When an explicit model changes family without an explicit effort, this skill resets effort to `low` for known families and leaves it unset for unknown models. The Beta multi-agent model does not automatically fall back to `single` after a failure.

### Timeout

Timeout is computed from the final model and effort, not the preset name:

| Model family | Effort | Default timeout |
|---|---|---|
| grok-4.3 | none / low | 60s |
| grok-4.5 | low | 60s |
| grok-4.3 / grok-4.5 | medium / high | 120s |
| multi-agent | low / medium (4 agents) | 300s |
| multi-agent | high / xhigh (16 agents) | 600s |
| unknown | any | 600s |

`--timeout` always overrides the default.

### Effort semantics

**grok-4.3**: `reasoning.effort` controls reasoning depth: `none`/`low`/`medium`/`high`. `xhigh` not supported.

**grok-4.20-multi-agent**: `reasoning.effort` controls agent count: `low`/`medium` = 4 agents, `high`/`xhigh` = 16 agents. `none` not supported. Must use Responses API (not Chat Completions). No client-side function calling.

**grok-4.5**: xAI's official default effort is `high`. This skill deliberately sends `low` when no explicit `--effort` is supplied, including after a cross-family model override.

### Aliases

- `grok-4.3-latest` — tracks latest grok-4.3 release
- `grok-latest` — tracks xAI's latest Grok model (may change without notice); this skill treats it as an unknown family
- Fixed date aliases (e.g. `grok-4.20-multi-agent-0309`) — never change

`grok-4.3` is a stable alias that tracks the latest 4.3 release — suitable as default, but may update when xAI publishes new versions. For absolute reproducibility, use date-pinned versions (e.g. `grok-4.20-multi-agent-0309`).

`grok-4-1-fast` is retired; do not select it for new requests.

## Tools

### web_search

| Parameter | Constraints | Description |
|---|---|---|
| `filters.allowed_domains` | Max 5, mutually exclusive with `excluded_domains` | Only search these domains |
| `filters.excluded_domains` | Max 5, mutually exclusive with `allowed_domains` | Skip these domains |
| `enable_image_understanding` | Default false | Analyze images found on pages. **Side effect**: also enables image understanding for x_search in the same request |
| `enable_image_search` | Default false | Embed image search results in response |

**No date filtering.** Web search has no `from_date`/`to_date`; state time ranges in the query text. The script rejects `--source web` combined with `--since` or `--until`.

### x_search

| Parameter | Constraints | Description |
|---|---|---|
| `allowed_x_handles` | Max 20, mutually exclusive with `excluded_x_handles` | Only search these accounts |
| `excluded_x_handles` | Max 20, mutually exclusive with `allowed_x_handles` | Skip these accounts |
| `from_date` | ISO8601 `YYYY-MM-DD`, inclusive | Strict start date filter |
| `to_date` | ISO8601, inclusive | Strict end date filter |
| `enable_image_understanding` | Default false | Analyze images in posts |
| `enable_video_understanding` | Default false, x_search only | Analyze videos in posts |

The `tools` array is the sole source selector. This skill does not send the deprecated top-level live-search configuration object or its mode, citation-return, and result-limit fields.

## Multi-turn

- `previous_response_id`: continue a previous conversation. Requires `store: true` (default). 30-day retention. Cannot combine with `instructions`.
- `x-grok-conv-id` / `prompt_cache_key`: cache routing for performance. Different purpose — not conversation continuation.

## Other request parameters

| Parameter | Description |
|---|---|
| `max_output_tokens` | Max output tokens (includes reasoning tokens). NOT `max_tokens` |
| `temperature` | 0-2 sampling temperature |
| `top_p` | 0-1 nucleus sampling |
| `max_turns` | Cap on agentic tool-calling rounds |
| `parallel_tool_calls` | Default true |
| `store` | Default true. Set false to disable response storage (breaks multi-turn) |

## Response structure

The `output` array contains multiple item types. Only `type == "message"` items contain the final answer:

```
output[].type == "message"
  → content[].type == "output_text"
    → text: the answer
    → annotations[]: {type: "url_citation", url, start_index, end_index}
```

Other output types (`reasoning`, `web_search_call`, `function_call`, etc.) are intermediate — skip them.

Citations are collected from `output_text.annotations` entries with `type: "url_citation"`.

### usage object

```json
{
  "input_tokens": 125,
  "output_tokens": 48,
  "total_tokens": 173,
  "input_tokens_details": {"cached_tokens": 98},
  "output_tokens_details": {"reasoning_tokens": 30},
  "num_server_side_tools_used": 2,
  "server_side_tool_usage_details": {
    "web_search_calls": 1,
    "x_search_calls": 1
  }
}
```

## Pricing

| Component | Cost per million tokens |
|---|---|
| Input tokens (grok-4.3) | $1.25 |
| Cached input tokens | $0.20 |
| Output tokens | $2.50 |

Tool calls: $5.00 per 1,000 calls (web_search, x_search).

Multi-agent cost: all agents' tokens are billed. 16-agent deep research costs significantly more than a single-agent call (all agents' tokens are billed).

## Common gotchas

- Use `max_output_tokens`, not `max_tokens` (includes reasoning tokens)
- Web search has no date filter — put its time range in the query text
- `instructions` and `previous_response_id` are mutually exclusive
- `store: false` disables multi-turn
- `enable_image_understanding` on web_search also affects x_search (side effect)
- Multi-agent model doesn't support Chat Completions API or client-side function calling
- Use a date-pinned model (e.g. `grok-4.20-multi-agent-0309`) for absolute reproducibility.
