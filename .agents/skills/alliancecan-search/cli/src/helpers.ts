// Data source: Digital Research Alliance of Canada (alliancecan.ca) careers pages.
// No authentication. The site is a server-rendered Next.js/Sanity build, so both the
// listing and the detail pages arrive as complete HTML — no API, no client hydration
// needed to read them.
//
// robots.txt (checked 2026-08-07) is `User-agent: *` / `Allow: /`, disallowing only
// `/studio` (the Sanity admin) and `/api/`. Every path used here is permitted.
//
// Scale note: the Alliance is a single employer, not a job board. It carries roughly
// half a dozen openings at a time, all on one page — so `search` fetches that one page
// and filters client-side rather than issuing a query per request.

export const BASE = "https://alliancecan.ca"

export const LISTING_PATH: Record<Lang, string> = {
  en: "/en/careers",
  fr: "/fr/possibilites-de-carriere",
}

export type Lang = "en" | "fr"

export const ORG_NAME: Record<Lang, string> = {
  en: "Digital Research Alliance of Canada",
  fr: "Alliance de recherche numérique du Canada",
}

export function writeError(error: string, code: string): void {
  process.stderr.write(JSON.stringify({ error, code }) + "\n")
}

const UA = "Mozilla/5.0 (compatible; alliancecan-cli/1.0)"

/** Fetch HTML with exponential backoff on 429/5xx. Returns "" on a 404. */
export async function htmlFetch(url: string): Promise<string> {
  const maxRetries = 6
  let delay = 500
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    const response = await fetch(url, {
      headers: {
        "User-Agent": UA,
        Accept: "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-CA,en;q=0.9,fr-CA;q=0.8",
      },
      redirect: "follow", // the site 307s bare paths onto their canonical form
      signal: AbortSignal.timeout(15000),
    })
    if (response.status === 429 || response.status >= 500) {
      if (attempt === maxRetries) {
        throw new Error(`Request failed: ${response.status} ${response.statusText}`)
      }
      const jitter = Math.floor(Math.random() * 500)
      await new Promise((r) => setTimeout(r, delay + jitter))
      delay = Math.min(delay * 2, 8000)
      continue
    }
    if (response.status === 404) return ""
    if (!response.ok) {
      throw new Error(`Request failed: ${response.status} ${response.statusText}`)
    }
    return response.text()
  }
  throw new Error("Request failed after max retries")
}

export interface JobCard {
  id: string
  title: string
  company: string | null
  location: string | null
  date: string | null
  url: string
}

export interface JobDetail extends JobCard {
  description: string | null
  applyUrl: string | null
}

function numericEntity(cp: number): string {
  return cp >= 0 && cp <= 0x10ffff ? String.fromCodePoint(cp) : ""
}

export function decodeHtmlEntities(text: string): string {
  return text
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&apos;/g, "'")
    .replace(/&#(\d+);/g, (_, dec) => numericEntity(parseInt(dec, 10)))
    .replace(/&#[xX]([0-9a-fA-F]+);/g, (_, hex) => numericEntity(parseInt(hex, 16)))
    .replace(/&nbsp;/g, " ")
}

/**
 * The site is server-rendered React, which emits empty `<!-- -->` comment markers
 * between a label and its value (`<strong>Location<!-- -->:</strong> <!-- -->Remote`).
 * Strip comments before any label matching or the field parsers miss every value.
 */
function stripComments(html: string): string {
  return html.replace(/<!--[\s\S]*?-->/g, "")
}

function stripTags(html: string): string {
  return html.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim()
}

export function clean(html: string): string {
  return decodeHtmlEntities(stripTags(stripComments(html)))
}

function escapeRegExp(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
}

/** Fold accents and case so a French query matches an accented French title. */
export function fold(s: string): string {
  return s
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
}

/**
 * Parse the careers listing. Every opening is an <a> carrying an aria-label and an
 * href under /<lang>/career-opportunities/<slug>. Both language editions use the same
 * `career-opportunities` path segment (only the slugs differ), so one pattern covers
 * both. Each anchor is parsed independently; a malformed one is skipped, not fatal.
 */
export function parseListing(html: string, lang: Lang): JobCard[] {
  const results: JobCard[] = []
  const seen = new Set<string>()
  const re = /<a[^>]*aria-label="([^"]*)"[^>]*href="(\/(?:en|fr)\/career-opportunities\/([^"]+))"/gi

  let m: RegExpExecArray | null
  while ((m = re.exec(html)) !== null) {
    const slug = m[3]
    if (seen.has(slug)) continue
    seen.add(slug)

    // The aria-label is "<Title>, Read More" / "<Titre>, Lire en plus" — drop the
    // trailing call-to-action so the title is the title.
    const title = decodeHtmlEntities(m[1])
      .replace(/,\s*(Read More|Lire en plus)\s*$/i, "")
      .trim()
    if (!title) continue

    results.push({
      id: slug,
      title,
      company: ORG_NAME[lang],
      location: null, // only stated on the detail page
      date: null, // the listing carries no posting date; `detail` has it
      url: `${BASE}${m[2]}`,
    })
  }
  return results
}

/** Pull a `<strong>Label:</strong> value` pair out of the Position Details block. */
function detailField(html: string, labels: string[]): string | null {
  const stripped = stripComments(html)
  for (const label of labels) {
    // Prefix match: the French edition labels the field "Lieu de travail:", not
    // "Lieu:", and an exact match would silently null the field on label drift.
    const m = stripped.match(
      new RegExp(`<strong>\\s*${label}[^<:]*:?\\s*</strong>\\s*([^<]+)`, "i"),
    )
    if (m) {
      const v = decodeHtmlEntities(m[1]).replace(/\s+/g, " ").trim()
      if (v) return v
    }
  }
  return null
}

/**
 * Drop the "Position Details" header block from the description body. Organization,
 * Location and Posted are already surfaced as dedicated fields, so repeating them in
 * the description is noise — and it pushes the one line that actually matters (the
 * off-site link to the full posting) below the fold.
 */
function stripPositionDetails(text: string): string {
  const labels =
    /^(Position Details|D[ée]tails du poste|Organization|Organisation|Location|Lieu|Emplacement|Posted|Publi[ée]|Date de publication)\s*:?/i
  const lines = text.split("\n")
  let i = 0
  while (i < lines.length && (lines[i]!.trim() === "" || labels.test(lines[i]!.trim()))) i++
  return lines.slice(i).join("\n").trim()
}

/** Convert a block of HTML to readable text, preserving paragraph breaks. */
function blockText(html: string): string | null {
  const withBreaks = stripComments(html)
    .replace(/<\s*br\s*\/?>/gi, "\n")
    .replace(/<\/(p|li|ul|ol|h\d|div|section)>/gi, "\n")
  const text = decodeHtmlEntities(withBreaks.replace(/<[^>]+>/g, " "))
    .replace(/[ \t]+/g, " ")
    .replace(/ *\n */g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim()
  return text || null
}

/** Parse a single career-opportunity page. */
export function parseJobDetail(html: string, slug: string, lang: Lang): JobDetail {
  const h1 = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i)
  const title = h1 ? clean(h1[1]) : "(untitled)"

  // Restrict field parsing to <main> so the site-wide nav ("About / Careers /
  // Membership / Services") cannot leak into the description.
  const mainMatch = html.match(/<main[^>]*>([\s\S]*?)<\/main>/i)
  const main = mainMatch ? mainMatch[1] : html

  const company = detailField(main, ["Organization", "Organisation"]) ?? ORG_NAME[lang]
  const location = detailField(main, ["Location", "Lieu", "Emplacement"])
  const date = detailField(main, ["Posted", "Publié", "Publie", "Date de publication"])

  // The Alliance posts a summary and hands the full description to an external
  // recruiter portal, so the apply link is off-site by design.
  const applyMatch = main.match(
    /<a[^>]*href="(https?:\/\/(?!alliancecan\.ca)[^"]+)"[^>]*>([\s\S]*?)<\/a>/i,
  )

  return {
    id: slug,
    title,
    company,
    location,
    date,
    url: `${BASE}/${lang}/career-opportunities/${slug}`,
    description: (() => {
      const body = blockText(main)
      if (!body) return null
      // Keep the title out of the body too — it is already the `title` field.
      const withoutTitle = body.replace(new RegExp(`^${escapeRegExp(title)}\\s*`, "i"), "")
      return stripPositionDetails(withoutTitle) || null
    })(),
    applyUrl: applyMatch ? decodeHtmlEntities(applyMatch[1]) : null,
  }
}

/** Accept a bare slug or any alliancecan career-opportunity URL. */
export function normalizeSlug(input: string): { slug: string; lang: Lang } | null {
  const fromUrl = input.match(/\/(en|fr)\/career-opportunities\/([^/?#]+)/i)
  if (fromUrl) return { slug: fromUrl[2], lang: fromUrl[1].toLowerCase() as Lang }
  if (/^[a-z0-9][a-z0-9-]*$/i.test(input)) return { slug: input, lang: "en" }
  return null
}
