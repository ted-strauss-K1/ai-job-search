---
name: lassoinformatics-search
version: 1.0.0
description: >
  Use this skill whenever the user asks about jobs, careers, or open positions at Lasso
  Informatics (the research data management and analysis platform for multi-site studies,
  with a Montreal engineering team) — even if they don't name it explicitly. Also invoke
  for questions about research data platform employers, study operations, or data
  operations roles at research-data SaaS companies. Trigger phrases: Lasso Informatics
  jobs, Lasso careers, lassoinformatics hiring, Wranglers, Sr. Data Operations
  Specialist, research data platform jobs Montreal, carrières Lasso Informatics, postes
  vacants Lasso, emplois plateforme de données de recherche.
context: fork
enabled: true  # set to false to keep this portal installed but have /scrape skip it
allowed-tools: Bash(bun run .agents/skills/lassoinformatics-search/cli/src/cli.ts *)
---

# Lasso Informatics — Careers Search Skill

List and read current openings at **Lasso Informatics** (`careers.lassoinformatics.info`),
a research data platform company serving multi-site studies (imaging, genetics,
biospecimens, wearables). No authentication, no API key, **zero runtime dependencies**.

## Scope: single employer, not a job board

Lasso is one organization with roughly **ten openings at a time**, all returned by one
JSON call. That shapes the CLI:

- `--query` filters **client-side** over title and department (the site has no search box).
- There is **no `--jobage`**: the API exposes no posting date, so results carry `date: null`.
- One `search` run is one HTTP request; `detail` is one request per posting.

Its low volume is the point: for a candidate targeting research data management and
study operations roles, this is a small, high-signal list worth checking on every scrape.

## Access

The site is a single-page app that reads its postings from a public JSON API on the same
host (`/api/postings`). The host serves no `robots.txt` (the path returns the SPA shell),
so no restriction is stated. The client identifies itself honestly as
`lassoinformatics-cli/1.0` and keeps volume low. See `url-reference.md`.

## Commands

### List / search openings

```bash
bun run .agents/skills/lassoinformatics-search/cli/src/cli.ts search [flags]
```

Key flags:
- `--query <text>` / `-q <text>` — filter by title or department keyword. Accent- and case-insensitive. Omit to list everything.
- `--page <n>` — 1-indexed page. Default 1.
- `--limit <n>` / `-n <n>` — cap results emitted.
- `--format json|table|plain` — default `json`.

Each result has `id` (the slug), `title`, `company`, `location`, `date` (always `null`),
`url`, plus `department`, `employmentType`, `countries`, `salaryCAD`, `salaryUSD`.

### Fetch an opening's details

```bash
bun run .agents/skills/lassoinformatics-search/cli/src/cli.ts detail <slug|url> [--lang en|fr] [--format json|plain]
```

`slug` is the `id` from `search` results. A full `careers.lassoinformatics.info/jobs/...`
URL also works. Returns the full description as readable text, the **required screening
questions** the application form asks, and the apply URL. `--lang fr` returns the French
description and questions.

## Usage examples

```bash
# Every current opening
bun run .agents/skills/lassoinformatics-search/cli/src/cli.ts search --format table

# Data-related roles only
bun run .agents/skills/lassoinformatics-search/cli/src/cli.ts search -q "data" --format table

# Study Operations department
bun run .agents/skills/lassoinformatics-search/cli/src/cli.ts search -q "study operations" --format plain

# Full details, including the screening questions
bun run .agents/skills/lassoinformatics-search/cli/src/cli.ts detail sr-data-operations-specialist --format plain
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

- **Postings carry a degree bar.** Several roles here state a firm PhD requirement
  (Science Data Analyst, Scientific Collaborator Liaison, Research Data Scientist).
  Check the qualifications block before spending time on a draft.
- **Salary is in the listing**, as `salaryCAD` and `salaryUSD` strings of varying format
  (`$74,000 - $95,000`, `74,000 - 96,000`). They are passed through as-is.
- **Screening questions** are required yes/no fields on the apply form. `detail` lists
  them so they can be answered truthfully before drafting.
- **Descriptions are HTML** with inline colour spans; the CLI converts them to text and
  decodes entities. Headings are bare spans, so the parser starts a new line at each
  opening block tag. Do not remove that step or headings fuse with the next sentence.
- **Slugs**: the page URL is `/jobs/<slug>`, the apply form is `/jobs/<slug>/apply`.
