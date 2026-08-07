---
name: alliancecan-search
version: 1.0.0
description: >
  Use this skill whenever the user asks about jobs, careers, or open positions at the
  Digital Research Alliance of Canada (also called the Alliance, DRAC, or by its French
  name Alliance de recherche numérique du Canada) — even if they don't name it
  explicitly. Also invoke for questions about Canadian research computing, digital
  research infrastructure, or national research data management employers. Trigger
  phrases: Alliance jobs, alliancecan careers, Digital Research Alliance of Canada
  hiring, DRAC opportunities, research data management jobs Canada, digital research
  infrastructure careers, possibilités de carrière, postes vacants Alliance,
  emplois recherche numérique.
context: fork
enabled: true  # set to false to keep this portal installed but have /scrape skip it
allowed-tools: Bash(bun run .agents/skills/alliancecan-search/cli/src/cli.ts *)
---

# Digital Research Alliance of Canada — Careers Search Skill

List and read current openings at the **Digital Research Alliance of Canada**
(`alliancecan.ca`), the national non-profit that coordinates Canada's digital research
infrastructure — advanced research computing, research data management, and research
software. No authentication, no API key, **zero runtime dependencies**.

Available in both official languages (`--lang en|fr`).

## Scope: single employer, not a job board

The Alliance is one organization, not an aggregator. Expect **roughly half a dozen
openings at a time**, all published on one page. That shapes the CLI:

- `--query` filters **client-side** over the fetched list (the site has no search box).
- There is **no `--jobage`** — the listing carries no posting date. Dates are on the
  detail page.
- One `search` run is one HTTP request regardless of how many results come back.

Its low volume is the point: for a candidate targeting Canadian research
infrastructure, this is a small, high-signal list worth checking on every scrape rather
than a firehose to filter.

## Access

`alliancecan.ca/robots.txt` is `User-agent: *` / `Allow: /`, disallowing only `/studio`
(the Sanity CMS admin) and `/api/`. Every path this skill uses is explicitly permitted.
The client identifies itself honestly as `alliancecan-cli/1.0`.

## Commands

### List / search openings

```bash
bun run .agents/skills/alliancecan-search/cli/src/cli.ts search [flags]
```

Key flags:
- `--query <text>` / `-q <text>` — filter openings by title keyword. Accent- and case-insensitive, so `donnees` matches `données`. Omit to list everything.
- `--lang <en|fr>` — language edition. Default `en`.
- `--page <n>` — 1-indexed page. Default 1 (the Alliance rarely exceeds one page).
- `--limit <n>` / `-n <n>` — cap results emitted.
- `--format json|table|plain` — default `json`.

### Fetch an opening's details

```bash
bun run .agents/skills/alliancecan-search/cli/src/cli.ts detail <slug|url> [--lang en|fr] [--format json|plain]
```

`slug` is the `id` from `search` results (e.g. `chief-research-and-data-services-officer`).
A full `alliancecan.ca/en/career-opportunities/...` URL also works, and the language is
inferred from it. Returns organization, location, posting date, the summary, and the
**external apply link**.

## Usage examples

```bash
# Every current opening
bun run .agents/skills/alliancecan-search/cli/src/cli.ts search --format table

# Data-related roles only
bun run .agents/skills/alliancecan-search/cli/src/cli.ts search -q "data" --format table

# French edition
bun run .agents/skills/alliancecan-search/cli/src/cli.ts search --lang fr --format table

# Full details for one opening
bun run .agents/skills/alliancecan-search/cli/src/cli.ts detail chief-research-and-data-services-officer --format plain
```

## Output formats

| Format | Best for |
|--------|----------|
| `json` | Default — programmatic use, passing slugs to `detail` |
| `table` | Quick human-readable scanning |
| `plain` | Reading a single opening (`detail` command) |

All errors are written to **stderr** as `{ "error": "...", "code": "..." }` and the
process exits with code `1`.

## Notes

- **Postings are summaries, not full descriptions.** For senior roles especially, the
  Alliance publishes a Position Details block and hands the full description to an
  external executive-search portal (Perrett Laver at time of writing). The `applyUrl`
  field carries that off-site link. When evaluating one of these with `/apply` or
  `/rank`, follow `applyUrl` for the real requirements — treat the Alliance page as a
  lead, not the source. See `09-web-research.md`.
- **EN and FR are separate listings with different slugs** (`project-manager` vs
  `gestionnaire-de-projet`), but both live under the same `/career-opportunities/` path
  segment. A slug from one edition will not resolve in the other.
- **Titles come from the anchor's `aria-label`**, which ends in "Read More" / "Lire en
  plus"; the CLI strips that.
- **The site is server-rendered React** and injects empty `<!-- -->` markers between a
  label and its value. The parsers strip comments before matching — do not remove that
  step or every Position Details field returns null.
- The listing has no posting date, so search results carry `date: null`. Use `detail`
  when the date matters.
