# Lasso Informatics careers — URL reference

Recorded 2026-10-02. This is what a future maintainer needs if the site changes.

## Architecture

`https://careers.lassoinformatics.info/` is a single-page app: every route returns the
same HTML shell (HTTP 200) and the browser JS calls a JSON API on the same host. That
includes unknown paths such as `/robots.txt`, which therefore returns the shell rather
than a 404. The routing code in the shell recognises `/jobs`, `/jobs/<slug>`,
`/jobs/<slug>/apply` and `/jobs/<slug>/thanks`.

## Endpoints used

| Purpose | Request | Response |
|---|---|---|
| Listing | `GET /api/postings` (`Accept: application/json`) | `{ "postings": [ ... ] }` |
| Detail | `GET /api/postings/<slug>` | `{ "posting": { ... } }` |

No authentication. Paths under `/api/manage/` and `/.auth/` belong to the admin side and
are not used.

## Listing fields (per posting)

| Field | Example | Notes |
|---|---|---|
| `id` | `posting_yjxe9tnmulpdjyi` | Internal id; the CLI uses `slug` as its `id` |
| `slug` | `sr-data-operations-specialist` | Page is `/jobs/<slug>` |
| `title` | `Sr. Data Operations Specialist` | |
| `department` | `Study Operations` | |
| `location` | `Canada \| USA`, `Montréal, Quebec` | Free text |
| `employmentType` | `Full-Time`, `Full Time` | Inconsistent spelling |
| `countries` | `["CANADA","USA"]` | |

The listing does **not** include descriptions, questions, or salary.

## Detail fields (adds to the above)

| Field | Notes |
|---|---|
| `salaryCAD`, `salaryUSD` | Strings, inconsistent format; may be absent on some postings |
| `descriptionMd` | HTML (despite the name) with inline `<span style="color:...">` |
| `descriptionFr` | French HTML edition; may be absent |
| `questions[]` | `{ id, order, type: "YES_NO", questionText, questionTextFr, required }` |

There is no posting date or closing date field anywhere in the API.

## Parsing anchors

- Descriptions: headings are bare `<span>`s followed directly by `<p>` or `<ul>`. Start a
  new line at every opening `p/ul/ol/h*/div/section` tag, and unwrap `<li><p>...</p></li>`.
- French questions sometimes begin with a stray `- `; the CLI strips it.
- Entity decode order: decode `&amp;` last.
