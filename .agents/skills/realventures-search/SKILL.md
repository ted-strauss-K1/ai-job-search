---
name: realventures-search
version: 1.0.0
description: >
  Use this skill when the user wants to search job openings across Real Ventures'
  portfolio-company network (jobs.realventures.com) — a Montreal-based venture
  capital firm's Getro-powered job board covering startups in Canada, the US, and
  internationally. Trigger phrases: Real Ventures jobs, Real Ventures portfolio
  jobs, jobs.realventures.com, Real Ventures startup jobs, offres d'emploi Real
  Ventures, emplois startups Montréal.
context: fork
enabled: true  # set to false to keep this portal installed but have /scrape skip it
allowed-tools: Bash(bun run .agents/skills/realventures-search/cli/src/cli.ts *)
---

# Real Ventures Job Board Search Skill

Search live job listings across **Real Ventures'** portfolio-company network
(`jobs.realventures.com`), a Montreal-based early-stage VC firm. The board is
powered by **Getro** and covers ~85 portfolio companies (Mejuri, Algolux, Stay22,
Blockstream, QuoteMachine, Busbud, Nomic, and more) with roles across Canada, the
US, and internationally. No authentication required, **zero runtime dependencies**
— it runs with just `bun`.

## When to use this skill

- Search job openings across Real Ventures' portfolio companies by keyword
- Get the full description of a specific job listing

## Commands

### Search job listings

```bash
bun run .agents/skills/realventures-search/cli/src/cli.ts search --query "<text>" [flags]
```

Key flags:
- `--query <text>` / `-q <text>` — free-text keyword search (title, skill, company, **and location** — the portal's search index matches all of these, so include a city/country in the query text to filter by location, e.g. `-q "data governance Montreal"`).
- `--page <n>` — page number (1-indexed, 20 results per page — this is the portal's hard cap, `--hitsPerPage` above 20 is silently ignored server-side).
- `--limit <n>` / `-n <n>` — cap total results emitted (client-side).
- `--format json|table|plain` — default `json`.
- `--jobage` is **not supported** by this portal's search API (no posted-within-N-days filter is exposed) — omit it; results are sorted by recency by default.

### Fetch full job detail

```bash
bun run .agents/skills/realventures-search/cli/src/cli.ts detail <url> [--format json|plain]
```

`<url>` must be the internal board URL returned by `search` results' `url` field
(e.g. `https://jobs.realventures.com/companies/quotemachine/jobs/86713566-senior-director-enterprise-data-governance`),
or the shorthand `<company-slug>/<job-slug>` from that same URL. **Bare numeric job
IDs are not supported** — this portal's public API has no id-only lookup (only a
free-text search endpoint), so the company slug is required to build the detail
page path. Always pass through the `url` a `search` result gave you.

## Usage examples

```bash
# Data governance roles, anywhere in the network
bun run .agents/skills/realventures-search/cli/src/cli.ts search -q "data governance" --format table

# Learning & development / Moodle roles in Montreal
bun run .agents/skills/realventures-search/cli/src/cli.ts search -q "learning management Montreal" --format table

# Second page of results for a broad query
bun run .agents/skills/realventures-search/cli/src/cli.ts search -q "product manager" --page 2 --format table

# Full details for a specific job (url from a prior search result)
bun run .agents/skills/realventures-search/cli/src/cli.ts detail "https://jobs.realventures.com/companies/quotemachine/jobs/86713566-senior-director-enterprise-data-governance" --format plain
```

## Output formats

| Format | Best for |
|--------|----------|
| `json` | Default — programmatic use, passing URLs to `detail` |
| `table` | Quick human-readable scanning |
| `plain` | Reading a single job's full detail (`detail` command) |

All errors are written to **stderr** as `{ "error": "...", "code": "..." }` and the process exits with code `1`.

## Notes

- Data source: the same JSON API the board's own React frontend calls
  (`POST https://api.getro.com/api/v2/collections/166/search/jobs`) — public, no
  auth, no CORS restriction on server-side requests. See `url-reference.md`.
- Server caps `hitsPerPage` at **20 regardless of what's requested**; use `--page`
  for more results.
- The `query` field has no separate location parameter — it full-text-matches
  against title, company, skills, *and* location strings, so put the city/country
  in `--query` (matches the `jobindex-search` pattern for portals without a
  location param).
- `search` results' `url` field is this portal's **internal detail page**, not the
  external ATS apply link — a separate `applyUrl` field carries the real apply
  link (Greenhouse/Ashby/etc.) when present.
- Detail-page description HTML is parsed from embedded Next.js JSON
  (`__NEXT_DATA__`), not scraped from rendered markup — very stable against
  front-end redesigns as long as Getro doesn't change its data shape.
