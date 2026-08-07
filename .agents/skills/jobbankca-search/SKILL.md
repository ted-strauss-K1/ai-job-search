---
name: jobbankca-search
version: 1.0.0
description: >
  Use this skill whenever the user wants to search for jobs in Canada, find Canadian
  job listings, look up a specific Canadian job posting, or asks anything about the
  Canadian job market — even if they don't mention Job Bank or jobbank.gc.ca
  explicitly. Invoke for open positions, vacancies, and hiring anywhere in Canada
  (Montreal, Quebec, Toronto, Ottawa, Vancouver, remote), across any sector or role.
  Also invoke for French-language Canadian job queries. Trigger phrases: Canadian
  jobs, jobs in Canada, Job Bank, Guichet-Emplois, jobs in Montreal, Quebec jobs,
  emplois au Canada, offres d'emploi, recherche d'emploi, postes vacants,
  "are there any X jobs in <Canadian city>".
context: fork
enabled: true  # set to false to keep this portal installed but have /scrape skip it
allowed-tools: Bash(bun run .agents/skills/jobbankca-search/cli/src/cli.ts *)
---

# Job Bank Canada Search Skill

Search live job listings from **Job Bank / Guichet-Emplois** (`jobbank.gc.ca`), the
Government of Canada's national public job board. No authentication, no API key, and
**zero runtime dependencies** — it runs with just `bun`.

Job Bank aggregates postings employers submit directly plus feeds from partner boards,
covering every province and territory. It is the highest-volume public-sector-adjacent
board in Canada and is bilingual throughout.

## Access and courtesy

`jobbank.gc.ca/robots.txt` is `User-agent: *` with `Crawl-delay: 5` and **no `Disallow`
rules** — every path this skill uses is explicitly permitted. The CLI honours the
declared 5-second crawl delay between requests within a run, and identifies itself
honestly as `jobbankca-cli/1.0` rather than impersonating a browser. It is a public
service funded by taxpayers; keep volume reasonable.

## When to use this skill

- Search Canadian job openings by keyword and location (any province, city, or remote)
- Filter by recency (posted within 1 / 7 / 14 / 30 days)
- Get the full description, salary, and work-authorization conditions of a posting

## Commands

### Search job listings

```bash
bun run .agents/skills/jobbankca-search/cli/src/cli.ts search [flags]
```

Key flags:
- `--query <text>` / `-q <text>` — keyword search (title, skill, NOC term). Recommended.
- `--location <text>` / `-l <text>` — location string, e.g. `"Montreal, QC"`, `"Quebec"`, `"Ottawa, ON"`. Omit to search all of Canada.
- `--jobage <days>` — posted within N days. Snaps to Job Bank's buckets (`1`, `7`, `14`, `30`); a value above 30 applies no filter.
- `--page <n>` — page number (1-indexed, 25 results per page).
- `--limit <n>` / `-n <n>` — cap total results emitted (client-side).
- `--format json|table|plain` — default `json`.

At least one of `--query` or `--location` is required.

### Fetch full job detail

```bash
bun run .agents/skills/jobbankca-search/cli/src/cli.ts detail <id|url> [--format json|plain]
```

`id` is the posting ID from `search` results (e.g. `49978652`). A full
`jobbank.gc.ca/jobsearch/jobposting/...` URL also works. Returns the full description
(overview, languages, education, experience, responsibilities), salary, posting date,
and the **"Who can apply for this job?"** block.

## Usage examples

```bash
# Data governance roles around Montreal
bun run .agents/skills/jobbankca-search/cli/src/cli.ts search -q "data governance" -l "Montreal, QC" --format table

# Research data management across Quebec, last 30 days
bun run .agents/skills/jobbankca-search/cli/src/cli.ts search -q "research data management" -l "Quebec" --jobage 30 --format table

# Moodle / LMS roles anywhere in Canada
bun run .agents/skills/jobbankca-search/cli/src/cli.ts search -q "Moodle" --format table

# French-language query (Job Bank indexes both official languages)
bun run .agents/skills/jobbankca-search/cli/src/cli.ts search -q "gestion des donnees" -l "Montreal, QC" --format table

# Full details for a specific posting
bun run .agents/skills/jobbankca-search/cli/src/cli.ts detail 49978652 --format plain
```

## Output formats

| Format | Best for |
|--------|----------|
| `json` | Default — programmatic use, passing IDs to `detail` |
| `table` | Quick human-readable scanning |
| `plain` | Reading a single posting's full detail (`detail` command) |

All errors are written to **stderr** as `{ "error": "...", "code": "..." }` and the
process exits with code `1`.

## Notes

- **Search both official languages.** Job Bank indexes English and French postings
  separately — `"data analyst"` and `"analyste de données"` return different result
  sets. Per `04-job-evaluation.md`'s Language Gate, run the query in every language
  from your profile's Languages table.
- **Location is a soft filter.** Job Bank widens the radius when a city has few
  matches, so a `-l "Montreal, QC"` search can return Ontario postings. Check each
  result's `location` field rather than trusting the query to have constrained it.
- **`--jobage` snaps to buckets.** Job Bank silently ignores an unsupported `fage`
  value and returns *unfiltered* results, so the CLI snaps to the nearest supported
  bucket instead of passing a value through that would quietly widen the search.
- **Work authorization is stated explicitly.** The `eligibility` field carries Job
  Bank's "Who can apply" block (Canadian citizen / permanent resident / valid work
  permit). This feeds the work-authorization gate in `04-job-evaluation.md` directly
  rather than leaving it to be inferred from prose.
- **URLs are normalized.** Card links carry a servlet `jsessionid` and a tracking
  param; both are stripped so a stored URL stays fetchable on later runs.
- Page size is fixed at 25 results per page.
- Posting IDs are numeric (e.g. `49978652`) — pass them as-is to `detail`.
