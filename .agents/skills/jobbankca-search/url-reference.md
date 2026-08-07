# Job Bank Canada — endpoint and parsing reference

Reconnaissance performed 2026-08-07. This is the file to update when the portal changes
its markup: it records what the parsers in `cli/src/helpers.ts` anchor on.

## Access policy

`https://www.jobbank.gc.ca/robots.txt`:

```
User-agent: *
Crawl-delay: 5
```

No `Disallow` rules — every path below is permitted for all user agents. The declared
5-second crawl delay is honoured by `respectCrawlDelay()` in `helpers.ts`. Note the
throttle is per-process: each CLI invocation makes one request, so back-to-back shell
commands are not spaced by it. That is fine at human volumes; do not script a loop.

## Endpoints

| Purpose | URL |
|---------|-----|
| Search | `https://www.jobbank.gc.ca/jobsearch/jobsearch` |
| Detail | `https://www.jobbank.gc.ca/jobsearch/jobposting/<id>` |

### Search parameters

| Param | Meaning | Notes |
|-------|---------|-------|
| `searchstring` | Keyword query | Indexed per language — EN and FR return different sets |
| `locationstring` | Location, e.g. `Montreal, QC` | **Soft filter** — portal widens the radius when local matches are few |
| `fage` | Posting age in days | Accepts `1`, `7`, `14`, `30`. An unsupported value is **silently ignored** and returns unfiltered results, so `jobageToFage()` snaps to a bucket rather than passing through |
| `sort` | Sort order | `M` = most recent first (what the CLI sends) |
| `page` | 1-indexed page | 25 results per page. Verified working via plain GET |

**Pagination caveat.** The page's own "More results" control (`#moreresultbutton`) is a
JSF AJAX POST carrying `jakarta.faces.ViewState`. The CLI does **not** use it — the
`&page=N` GET parameter was verified to return distinct result sets and needs no
session state. If `&page=N` ever stops working, that JSF POST is the fallback, and it
would require carrying a session.

## Search response structure

Server-rendered HTML. Each result is one `<article id="article-<id>">`. The parser
splits on that boundary and parses each chunk independently, so one malformed card
cannot break the page.

| Field | Anchor | Quirk |
|-------|--------|-------|
| `id` | `<article id="article-49978652">` | Numeric; same id used in the detail URL |
| `title` | `<span class="noctitle">` | NOC-normalized title, usually lowercase |
| `company` | `<li class="business">` | |
| `location` | `<li class="location">` | Preceded by a `wb-inv` label span reading "Location" — **must be stripped** or the value becomes `"Location Laval (QC)"` |
| `date` | `<li class="date">` | Human-readable, e.g. `July 30, 2026` |
| `salary` | `<li class="salary">` | The "Salary" label here is **bare text** next to a decorative icon, *not* a `wb-inv` span — it needs its own strip |
| `telework` | `<span class="telework">` | `Hybrid` / `Remote` when present |
| `url` | `<a href="/jobsearch/jobposting/<id>;jsessionid=...?source=searchresults">` | Strip both the `;jsessionid=` segment and the query string |

Accented characters arrive as numeric entities (`Montr&#233;al`, `&#xE9;`), both decimal
and hex — decode both.

## Detail response structure

| Field | Anchor | Quirk |
|-------|--------|-------|
| `title` | `<h1>` | |
| `company` | `property="hiringOrganization"` | |
| `location` | `property="addressLocality"` | City only — no province suffix, unlike the search card |
| `date` | `property="datePosted"` | Value is **text** (`Posted on July 30, 2026`), not a `content=` attribute. Strip the `Posted on` prefix |
| `salary` | `property="baseSalary"` | Nested RDFa: `baseSalary > value > {currency, minValue, maxValue, unitText}`. The currency symbol sits in a `class="hidden"` span, so matching the inner property stops at the first `</span>` and yields just `"$"`. Take the enclosing `<li>` and clean it, then normalize (`"$ 28.75"` → `"$28.75"`, drop the duplicated uppercase `HOUR` unit token) |
| `description` | `.job-posting-detail-requirements` | Contains Overview / Languages / Education / Experience / Responsibilities. Extracted with depth-tracking so nested `<div>`s don't truncate it |
| `eligibility` | `.job-posting-detail-apply` | "Who can apply for this job?" — citizenship / PR / work-permit conditions. Feeds the work-authorization gate in `04-job-evaluation.md` |

An expired or unknown posting returns 404; `htmlFetch` maps that to `""` and the detail
command exits 1 with `NOT_FOUND` rather than emitting an empty shell.
