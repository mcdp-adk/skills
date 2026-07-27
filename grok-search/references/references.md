# Current CLI Behavior Reference

This file is an on-demand reference for the runtime agent. It records behavior
that is exposed by, or directly changes the behavior of, the bundled CLI; it is
not a general xAI API maintenance guide.

## Scope and source of truth

CLI behavior is defined by `scripts/search.py` and the deterministic tests in
`tests/test_search.py`. Vendor models, prices, and rate limits change; consult
the official current documentation when needed.

The script performs the API call and secret loading. The agent should invoke the
script rather than construct a direct authenticated request.

## Presets, model families, and effort

The preset selects a model and an initial reasoning effort. The agent count is
derived from the final model family and effort:

| Preset | Model | Effort sent | Agent count | Default timeout |
|---|---|---:|---:|---:|
| `single` | `grok-4.3` | `low` | 1 | 60 seconds |
| `multi-4` (default) | `grok-4.20-multi-agent` | `low` | 4 | 300 seconds |
| `multi-16` | `grok-4.20-multi-agent` | `high` | 16 | 600 seconds |

The CLI accepts `--model` and `--effort` overrides:

- `--model` replaces the preset model. `--effort` always replaces the preset
  effort when supplied.
- If an explicit model changes family and no explicit effort is supplied, the
  script uses `low` for a known family and leaves effort unset for an unknown
  family. A same-family model override retains the preset effort.
- `grok-4.3` accepts `none`, `low`, `medium`, and `high`; `xhigh` is rejected.
- `grok-4.20-multi-agent` accepts `low`/`medium` as 4 agents and `high`/`xhigh`
  as 16 agents; `none` is rejected.
- `grok-4.5` is treated as one agent, accepts `low`, `medium`, and `high`, and
  rejects `none` and `xhigh`. Although the API's documented default is high,
  this CLI sends `low` when no explicit effort is supplied.
- Unknown model families have no inferred effort or agent count. An explicit
  `--effort` only sets the effort value; `agent_count` remains unknown (`null`)
  and is never derived from that effort. Their default timeout is 600 seconds.

Family matching recognizes the exact model names and date/custom suffixes for
`grok-4.3`, `grok-4.20-multi-agent`, and `grok-4.5`. `grok-latest` and an
unrecognized name are therefore treated as unknown by this CLI.

## Timeout and request retries

The timeout is calculated from the final model family and effort, not from the
preset label. Defaults are:

| Final family | Effort | Timeout |
|---|---|---:|
| `grok-4.3` | `none` or `low` | 60 seconds |
| `grok-4.3` | `medium` or `high` | 120 seconds |
| `grok-4.5` | `low` | 60 seconds |
| `grok-4.5` | `medium` or `high` | 120 seconds |
| Multi-agent | `low` or `medium` (4 agents) | 300 seconds |
| Multi-agent | `high` or `xhigh` (16 agents) | 600 seconds |
| Unknown | any | 600 seconds |

`--timeout` overrides the default and must be greater than zero. The default
`--max-retries` is 3; it counts retries after the first attempt and must not be
negative.

Each CLI invocation owns its internal retry loop. The script automatically
handles eligible retries; the agent does not need to issue another CLI
invocation to provide those retries. `--max-retries` controls only this loop
inside the current invocation and does not authorize or require a second one.

Automatic retries are deliberately narrow:

- Retryable HTTP responses are 429 responses, up to the retry limit. A numeric
  `Retry-After` value is honored; otherwise the script uses bounded exponential
  backoff with jitter.
- A small set of pre-send connection failures is retryable: refused,
  unreachable-network, and unreachable-host errors.
- Timeouts are not automatically retried. A timed-out request may already have
  been processed; check for processing or billing before deciding what to do.
  If the invocation ultimately returns an API, connection, or timeout error, the
  agent must not automatically start a second CLI invocation.
- Authentication failures (401), bad requests (400), other HTTP failures, and
  ordinary connection failures are not silently retried.
- A multi-agent failure never triggers an automatic `single` fallback or model
  change. It follows the same narrow retry rules above only when the failure is
  an eligible 429 or pre-send connection error.

After a final error, any new invocation requires explicit user agreement. Unless
the user explicitly agrees to the change, do not alter the preset, model, or
effort, and do not switch to `single`.

## Multi-agent cost and behavior

Multi-agent requests may be slower and take minutes, and all participating
agents' tokens are billed. More agents do not guarantee broader coverage or
better answer quality.
Relative cost is lowest for `single`, higher for the default `multi-4`, and
highest for `multi-16`; use the latter only when the request explicitly calls
for genuinely comprehensive, multi-faceted work.

## Sources, filters, and time semantics

`--source` accepts `web`, `x`, or `both`; the default is `both`. The tools array
is built from this choice.

Web filters:

- `--web-allow DOMAIN` and `--web-exclude DOMAIN` each accept at most 5 domains.
- Allow and exclude are mutually exclusive, and Web filters require `--source
  web` or `--source both`.

X filters:

- `--x-allow HANDLE` and `--x-exclude HANDLE` each accept at most 20 handles.
- Allow and exclude are mutually exclusive, and X filters require `--source x`
  or `--source both`.
- The script trims whitespace and removes a leading `@` before sending handles.

Web has no strict date filter. `--source web` combined with `--since` or
`--until` fails before a request; put a Web time range in the query text.
With `--source both`, those flags constrain only X and the Web tool receives no
date fields.

For X, `--since` becomes an inclusive `from_date` and `--until` becomes an
inclusive `to_date`. The submitted values are date-level `YYYY-MM-DD` values,
even when the input is a relative time. Relative values use the forms `<N>h`,
`<N>d`, or `<N>w`, where `N` is any non-negative integer; `2h`, `7d`, and `2w`
are examples, not the complete set. `today`, `yesterday`, `now`, and ISO date or
date-time values are also accepted. They are interpreted in UTC, and `since`
must not be later than `until`. Hour-level freshness must be stated in the
query rather than assumed to be enforced by the X date fields.

Historical X coverage may be incomplete. Account filters and query wording are
not bot detection: this CLI cannot prove that it identified or filtered bots or
coordinated behavior. A post from an official account can establish that the
account made that statement, but it does not automatically verify the
underlying fact.

## Image, video, and continuation behavior

- Media understanding is off unless requested. `--image-understanding` enables
  image analysis for Web results or X posts. For `both`, the flag is attached to
  the Web tool; the API's documented side effect also enables image
  understanding for X search in that request.
- `--video-understanding` enables X video analysis and is rejected with
  `--source web`; it is valid for `x` and `both`.
- `--continue RESPONSE_ID` sends the value as `previous_response_id` with the
  new query. Use a `response_id` returned by a prior normal result to fill a
  known gap or audit evidence. The script relies on the service's normal stored
  response behavior for continuation.

## Environment and proxy precedence

The default environment file is `{baseDir}/.env`, where `{baseDir}` is the Skill
root directory. `--env-file` can select another file. The script supports blank
lines, comments, `export KEY=value`, and matching single or double quotes. A
malformed assignment is an `ENV_ERROR`.

For each variable, a non-empty operating-system environment value takes
precedence over the value in the selected file. `XAI_API_KEY` is required. The
agent must not open, print, copy, or parse the secret file; let the script load
it.

For proxy selection, the script checks these names in order, using the same
OS-before-file precedence within each name:

1. `HTTPS_PROXY` / `https_proxy`
2. `ALL_PROXY` / `all_proxy`
3. `HTTP_PROXY` / `http_proxy`

The selected proxy is used for both HTTP and HTTPS. `NO_PROXY` / `no_proxy` is
made available to the process for proxy bypass handling. `--ca-bundle` supplies
an explicit custom CA bundle. Do not put keys or proxy credentials in commands,
logs, or result text.

## Exit status, errors, and output

Successful normalized output exits 0. Script-level error statuses are:

- 1: general argument, API, connection, parse, incomplete-response, or
  unexpected failure reported by the script.
- 2: authentication failure. Argument-parser usage errors also exit 2 before
  the normal error wrapper; `--help` exits 0.
- 3: environment/configuration failure such as a missing key or malformed
  environment file.

### Output streams

The script's `emit` function writes the wrapped success or error JSON to stdout.
The `eprint` function writes `Searching...`, `Done.`, and `Retrying in ...`
progress or retry messages to stderr. A handled script failure therefore has a
JSON error on stdout, but an argparse usage error can terminate before the
wrapper runs, print usage and the error only to stderr, and exit 2; not every
failure has JSON output.

Agents and callers parsing structured results should parse stdout. If a harness
merges stdout and stderr, it should recognize the script's single-line JSON
record and treat the non-JSON progress or retry lines as stderr activity; those
lines are not a reason to start another CLI invocation.

Normal successful output is a JSON object with these fields:

- `ok`: `true`.
- `response_id`: the service response ID when present, otherwise `null`.
- `text`: text collected only from message items' `output_text` parts, joined by
  newlines.
- `citations`: deduplicated URLs from `url_citation` annotations in those
  output-text parts. They are candidate URLs, not proof that a claim is true.
- `request_summary`: effective `source`, preset/model/effort, agent count,
  timeout, warnings, resolved X dates, whether X filtering was strict, and the
  fact that Web strict filtering is unavailable. Its concrete keys are
  `source`, `preset_used`, `preset_explicit`, `preset_overridden`,
  `model_used`, `effort_sent`, `agent_count`, `timeout_seconds`, `warnings`,
  `resolved_since`, `resolved_until`, `x_time_filter`, and
  `web_strict_filter_available`.
- `citation_coverage`: a mechanical URL comparison with `text_urls`,
  `api_citation_urls`, and `unmatched_text_urls`. URL presence does not show
  that a cited page supports a claim.
- `usage`: the API usage object when supplied, otherwise `{}`.

For `citation_coverage`, the script normalizes URLs by removing surrounding
punctuation and fragments, lowercasing the network location, and deduplicating
them. The top-level `citations` list retains extracted URL strings after
whitespace stripping and exact de-duplication. A normal error is
`{"ok": false, "error": {"code": "...", "message": "..."}}`.

`--raw` means: emit the parsed API response object instead of the normalized
success wrapper. It does not bypass configuration, network errors, retries, or
secret loading, and it should not be treated as a citation audit format.
