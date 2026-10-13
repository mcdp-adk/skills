# DESIGN.md format

Condensed from the DESIGN.md specification, version `alpha`: [`docs/spec.md`](https://github.com/google-labs-code/design.md/blob/9bf8eae67128b6cc55ad9bf86665767deb4c11cd/docs/spec.md) at commit `9bf8eae`, which matches the `designmd spec` output of `@google/design.md` 0.4.0. The lint rules are that version's `designmd spec --rules-only` output.

## File structure

A DESIGN.md file has two parts:

1. **YAML front matter**: the design tokens, the normative values. The block opens with a line containing exactly `---` and closes with a line containing exactly `---`, at the top of the file. The block itself is optional.
2. **Markdown body**: `##` sections giving the rationale and guidance for applying the tokens. An optional `#` heading may title the document; it is not parsed as a section.

Prose may refer to a token by a descriptive name ("Midnight Forest Green") that corresponds to its systematic token name (`primary`).

## Token schema

```yaml
version: <string>          # optional, current version: "alpha"
name: <string>
description: <string>      # optional
omitted: <string[] | OmittedSection[]>  # optional
colors:
  <token-name>: <Color>
typography:
  <token-name>: <Typography>
rounded:
  <scale-level>: <Dimension>
spacing:
  <scale-level>: <Dimension | number>
components:
  <component-name>:
    <property>: <value | token reference>
```

A `<scale-level>` is any descriptive key; common ones are `xs`, `sm`, `md`, `lg`, `xl`, and `full`.

## Token types

- **Color**: any CSS color string: hex (`#RGB`, `#RGBA`, `#RRGGBB`, `#RRGGBBAA`), named (`cornflowerblue`, `transparent`), `rgb()`, `rgba()`, `hsl()`, `hsla()`, `hwb()`, `oklch()`, `oklab()`, `lch()`, `lab()`, or `color-mix(in srgb, ...)`. Hex `#RRGGBB` is the recommended default. Quote values in YAML (`"#1A1C1E"`).
- **Dimension**: a number with a `px`, `em`, or `rem` unit (`48px`, `-0.02em`).
- **Typography**: an object with any of:
  - `fontFamily` (string)
  - `fontSize` (Dimension)
  - `fontWeight` (number such as `400`; a quoted string is equivalent)
  - `lineHeight` (Dimension, or a unitless number as a multiple of `fontSize`, which is recommended)
  - `letterSpacing` (Dimension)
  - `fontFeature` (string, for `font-feature-settings`)
  - `fontVariation` (string, for `font-variation-settings`)
- **Token reference**: `{path.to.token}`, such as `"{colors.primary}"`. It must point to a primitive value, not a group, except inside `components`, where composite values such as `{typography.label-md}` are allowed.
- **Omitted entry**: a token group name (`colors`, `typography`, `rounded`, `spacing`, or `components`), or `{ section: <name>, reason?: <text> }`. Listing a group here declares it intentionally absent and suppresses the missing-section findings for it. The 0.4.0 linter warns on any other name, including prose-only sections such as Overview; leave those out of the body instead.

## Sections

Every section is optional; those present should appear in this order. A duplicate section heading makes the file invalid.

| # | Heading | Accepted alias | Tokens |
| --- | --- | --- | --- |
| 1 | `## Overview` | `## Brand & Style` | none |
| 2 | `## Colors` | | `colors` |
| 3 | `## Typography` | | `typography` |
| 4 | `## Layout` | `## Layout & Spacing` | `spacing` |
| 5 | `## Elevation & Depth` | `## Elevation` | none |
| 6 | `## Shapes` | | `rounded` |
| 7 | `## Components` | | `components` |
| 8 | `## Do's and Don'ts` | | none |

Consumers preserve unknown headings (such as `## Iconography`) and accept token names the spec does not list, such as `surface-container-high` or `telemetry-data`. A `spacing` value that is not a valid Dimension is kept as a string (`grid-columns: '5'`).

### Overview

The holistic look and feel: brand personality, target audience, and the emotional response the UI should evoke (playful or professional, dense or spacious). Agents fall back on it for stylistic decisions no token or rule covers.

### Colors

At least a `primary` palette must be defined. With several palettes, a common convention names them `primary`, `secondary`, `tertiary`, and `neutral`, each with a semantic role. The prose lists each palette with a descriptive name, its value, and its role; the `colors` tokens derive from those palettes under any consistent naming convention.

```markdown
- **Tertiary (#B8422E):** A vibrant earthy red as the sole driver for
  interaction, used exclusively for primary actions and critical highlights.
```

### Typography

Most design systems have 9 to 15 typography levels, often named by semantic category (`headline`, `display`, `body`, `label`, `caption`) and size. The design system may prescribe a role for each level.

### Layout

The layout model and spacing strategy: a grid (fluid, fixed max width, column count) or margins, safe areas, and dynamic padding, plus the spacing scale. `spacing` tokens may also hold unitless numbers such as column counts.

### Elevation & Depth

How visual hierarchy is conveyed. With shadows, define their spread, blur, and color; for flat designs, explain the alternative (borders, tonal layers, color contrast).

### Shapes

The shape language of elements, such as the corner radius of interactive elements, containers, and inputs, and why.

### Components

Style guidance for component atoms. Common types are buttons, chips, lists, tooltips, checkboxes, radio buttons, and input fields; define others the domain needs. This part of the spec is still evolving.

Each component maps to these properties:

| Property | Type |
| --- | --- |
| `backgroundColor` | Color |
| `textColor` | Color |
| `typography` | Typography |
| `rounded` | Dimension |
| `padding` | Dimension |
| `size` | Dimension |
| `height` | Dimension |
| `width` | Dimension |

Values may be literals or token references. Other properties are accepted with a warning. A state variant (hover, active, pressed) may be defined as a separate entry under a related key:

```yaml
components:
  button-primary:
    backgroundColor: "{colors.primary-60}"
    textColor: "{colors.primary-20}"
    rounded: "{rounded.md}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.primary-70}"
```

### Do's and Don'ts

Practical guardrails and common pitfalls, one per bullet:

```markdown
- Do use the primary color only for the single most important action per screen
- Don't mix rounded and sharp corners in the same view
```

## Recommended token names

These names are optional, and they keep files consistent with other design systems:

- **Colors**: `primary`, `secondary`, `tertiary`, `neutral`, `surface`, `on-surface`, `error`
- **Typography**: `headline-display`, `headline-lg`, `headline-md`, `body-lg`, `body-md`, `body-sm`, `label-lg`, `label-md`, `label-sm`
- **Rounded**: `none`, `sm`, `md`, `lg`, `xl`, `full`

## Lint rules

| Rule | Severity | Checks |
| --- | --- | --- |
| `broken-ref` | error | Broken or circular references, and unknown component sub-tokens |
| `missing-primary` | warning | Colors are defined but no `primary` exists |
| `contrast-ratio` | warning | A component's `backgroundColor` and `textColor` pair falls below the WCAG AA minimum of 4.5:1 |
| `orphaned-tokens` | warning | Tokens are defined but no component references them |
| `token-summary` | info | How many tokens each group defines |
| `missing-sections` | info | Optional token groups (`spacing`, `rounded`) are absent |
| `missing-typography` | warning | Colors are defined but no typography tokens exist |
| `section-order` | warning | Sections are out of the canonical order |
| `unknown-key` | warning | A top-level key looks like a typo of a schema key (`colours`) |
| `token-like-ignored` | warning | An unrecognized top-level key holds token-like values that will be ignored |
| `omitted-rules` | info | `omitted` entries are unknown or redundant |

## Example

```markdown
---
version: alpha
name: Heritage
colors:
  primary: "#1A1C1E"
  secondary: "#6C7278"
  tertiary: "#B8422E"
  neutral: "#F7F5F2"
  on-tertiary: "#FFFFFF"
typography:
  headline-lg:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
rounded:
  sm: 4px
spacing:
  sm: 8px
  md: 16px
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-tertiary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px
  card:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
---

## Overview

Architectural minimalism meets journalistic gravitas: the UI evokes a premium
matte finish, like a high-end broadsheet or a contemporary gallery.

## Colors

The palette is rooted in high-contrast neutrals and a single accent color.

- **Primary (#1A1C1E):** Deep ink for headlines and core text.
- **Secondary (#6C7278):** Slate for borders, captions, and metadata.
- **Tertiary (#B8422E):** "Boston Clay", the sole driver for interaction.
- **Neutral (#F7F5F2):** Warm limestone foundation, softer than pure white.
```
