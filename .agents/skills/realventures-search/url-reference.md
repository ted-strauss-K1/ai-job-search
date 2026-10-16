# Real Ventures Job Board URL Reference

`jobs.realventures.com` runs on **Getro** (network/collection id `166`). Public,
unauthenticated endpoints — no API key. Investigated by watching the board's own
network traffic (Chrome DevTools) while typing a query into the search box; the
`query`/`location` values in the page's own initial HTML/`__NEXT_DATA__` are
**not** wired to the SSR render (confirmed: `?query=...` in the URL bar changes
nothing server-side) — real filtering only happens via this JSON API, called
client-side.

## Search

```
POST https://api.getro.com/api/v2/collections/166/search/jobs
Content-Type: application/json
Accept: application/json
Origin: https://jobs.realventures.com
```

Request body:

```json
{ "hitsPerPage": 20, "page": 0, "filters": { "q": "data governance" }, "query": "data governance" }
```

| Field | Meaning | Notes |
|-------|---------|-------|
| `query` / `filters.q` | Free-text search | Matches title, company name, skills, **and** location strings. Send the same value in both. |
| `page` | 0-indexed page number | CLI's `--page` is 1-indexed; subtract 1 before sending. |
| `hitsPerPage` | Requested page size | **Hard-capped at 20 server-side** — sending 50 or 100 still returns 20 jobs. |

Other filter keys tried and confirmed **not functional**: `filters.locations`
(array of location strings — accepted but ignored, result count unchanged),
`filters.ids` / `filters.id` / `filters.job_ids` (no id-based lookup — returns
the same default/unfiltered set regardless of the id given). Only `q`/`query`
does anything.

Response shape:

```json
{ "results": { "jobs": [ { ... } ], "count": 659 } }
```

`results.count` is the **total** hit count across all pages (not the page length,
which is always ≤ 20).

### Job object fields (search response, snake_case)

| Field | Example |
|-------|---------|
| `id` | `90736301` |
| `title` | `"Senior Revenue Operations Analyst - GTM & Data"` |
| `slug` | `"90736301-senior-revenue-operations-analyst-gtm-data"` (numeric id + title slug) |
| `organization.name` | `"Stay22"` |
| `organization.slug` | `"stay22"` |
| `locations` | `["Montreal, QC, Canada"]` |
| `created_at` | `1787321884` (unix seconds) |
| `url` | External ATS apply link, e.g. `https://boards.greenhouse.io/mejuri/jobs/4707170006` — **not** a jobs.realventures.com URL |
| `work_mode` | `"on_site"` \| `"remote"` \| `"hybrid"` |
| `seniority` | `"mid_senior"`, `"senior"`, `"entry_level"`, or `null` |
| `compensation_amount_min_cents` / `_max_cents` | integer cents or `null` |
| `compensation_currency` | `"USD"`, `"CAD"`, or `null` |
| `has_description` | boolean |

**The portal's own internal detail-page URL is not in the response** — construct
it from `organization.slug` and `slug`:

```
https://jobs.realventures.com/companies/{organization.slug}/jobs/{slug}
```

e.g. `https://jobs.realventures.com/companies/stay22/jobs/90736301-senior-revenue-operations-analyst-gtm-data`

## Detail

No JSON detail API is exposed publicly — `GET /api/v2/collections/166/jobs/<id>`
returns `401 Unauthorized`. Instead, fetch the SSR HTML detail page and parse the
embedded Next.js data blob (this is a **Next.js** app; `pageProps.initialState`
is a JSON object server-rendered into a `<script id="__NEXT_DATA__">` tag — no
markup parsing needed, just `JSON.parse` the script contents):

```
GET https://jobs.realventures.com/companies/{orgSlug}/jobs/{jobSlug}
```

`data.props.pageProps.initialState.jobs.currentJob` fields used:

| Field | Notes |
|-------|-------|
| `title`, `id`, `slug`, `url` (external apply link) | |
| `organization` | same shape as search's `organization` |
| `locations` | array of strings |
| `description` | **raw HTML** — strip tags for `plain` format |
| `employmentTypes` | array, e.g. `["full_time"]` |
| `postedAt`, `expiresAt` | unix seconds, `expiresAt` often `null` |
| `applicationPath` | external application URL, may differ from `url` |
| `compensation*` fields | same shape as search |

## Notes

- No `robots.txt` restriction encountered on `/jobs`, `/companies/*`, or
  `/_next/data/*` paths at time of writing; this is a public marketing/recruiting
  page with no login wall.
- CORS on `api.getro.com` restricts the `Origin` header to
  `https://jobs.realventures.com` for browser requests, but this is a
  browser-enforced check — plain server-side `fetch`/`curl` requests work fine
  when the `Origin` header is set to that value manually (confirmed via `curl`).
- If Getro changes the Next.js build (`buildId` in `_next/static/...` paths)
  the SSR HTML parsing still works since we regex out `__NEXT_DATA__` by id, not
  by build-specific chunk URLs.
