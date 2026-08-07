# Digital Research Alliance of Canada — endpoint and parsing reference

Reconnaissance performed 2026-08-07. Update this file when the site changes: it records
what the parsers in `cli/src/helpers.ts` anchor on.

## Access policy

`https://alliancecan.ca/robots.txt`:

```
User-agent: *
Allow: /

Disallow: /studio      # Sanity CMS admin
Disallow: /api/
Disallow: /*?preview=*
Disallow: /*?draft=*
```

Every path used by this skill is permitted. Note `robots.txt` itself 307-redirects, so
fetch it with redirects followed.

## Endpoints

| Purpose | URL |
|---------|-----|
| Listing (EN) | `https://alliancecan.ca/en/careers` |
| Listing (FR) | `https://alliancecan.ca/fr/possibilites-de-carriere` |
| Detail | `https://alliancecan.ca/<lang>/career-opportunities/<slug>` |

The FR listing path is **not** a translation of the EN one (`/fr/carrieres` 404s), but
the *detail* path segment is shared: both editions use `/career-opportunities/`, with
different slugs. One anchor pattern therefore covers both.

There is no search endpoint and no query parameter — the listing is a single static
page carrying every opening. Keyword filtering is client-side by design.

## Listing response structure

Server-rendered Next.js/Sanity HTML. Each opening is one anchor:

```html
<a class="!no-underline block"
   aria-label="Chief Research &amp; Data Services Officer, Read More"
   href="/en/career-opportunities/chief-research-and-data-services-officer">
  <div><h3>Chief Research &amp; Data Services Officer</h3></div>
</a>
```

| Field | Anchor | Quirk |
|-------|--------|-------|
| `id` | the `<slug>` from the href | Stable identifier; differs between EN and FR |
| `title` | `aria-label` | Ends with `, Read More` (EN) / `, Lire en plus` (FR) — strip it. Entities are encoded (`&amp;`) |
| `url` | `href` | Relative; prefix with the origin |
| `location`, `date` | — | **Not present on the listing.** Emitted as `null`; available via `detail` |

The same opening can appear in more than one anchor on the page, so the parser
de-duplicates by slug.

Openings are grouped under two `<h2>` sections — "Current Opportunities" / "Postes
vacants" and "Secondments" / "Détachements". The parser does not distinguish them; all
anchors matching the path pattern are returned.

## Detail response structure

The content lives in `<main>`. **Restrict parsing to `<main>`** — the site-wide nav
("About / Board of Directors / Careers / Membership / Services") otherwise leaks into
the description.

```html
<section class="prose">
  <h1>Chief Research &amp; Data Services Officer</h1>
  <h2>Position Details</h2>
  <div class="grid">
    <div><strong>Organization<!-- -->:</strong> <!-- -->Digital Research Alliance of Canada</div>
    <div><strong>Location<!-- -->:</strong> <!-- -->Remote</div>
    <div><strong>Posted<!-- -->:</strong> <!-- -->June 19, 2026</div>
  </div>
</section>
<section><p>View the full description and apply here:
  <a href="https://plusportal.perrettlaver.com/VacancyDetail/...">Perrett Laver</a></p></section>
```

| Field | Anchor | Quirk |
|-------|--------|-------|
| `title` | `<h1>` | |
| `company` | `<strong>Organization:</strong>` / `Organisation:` | |
| `location` | `<strong>Location:</strong>` / **`Lieu de travail:`** | The FR label is *not* a direct translation — matching is prefix-based so `Lieu` also catches `Lieu de travail` |
| `date` | `<strong>Posted:</strong>` / `Date de publication:` | Human-readable, localized (`June 19, 2026` / `19 juin 2026`) |
| `description` | everything else in `<main>` | The Position Details block is stripped back out, since those values are already dedicated fields |
| `applyUrl` | first non-`alliancecan.ca` `<a href>` in `<main>` | External recruiter portal |

**React comment markers.** The server output injects empty `<!-- -->` between a label
and its value. Comments must be stripped before label matching or every Position
Details field returns null. This is the single most breakage-prone assumption in the
parser.

**Stub postings.** Senior roles carry only a summary; the full description lives on the
external recruiter site behind `applyUrl`. Treat the Alliance page as a lead and follow
`applyUrl` for real requirements (`09-web-research.md`).

An unknown slug returns 404; `htmlFetch` maps that to `""` and `detail` exits 1 with
`NOT_FOUND`.
