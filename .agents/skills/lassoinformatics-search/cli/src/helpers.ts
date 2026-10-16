// Data source: Lasso Informatics careers site (careers.lassoinformatics.info).
// The site is a small single-page app that reads its postings from a public,
// unauthenticated JSON API on the same host:
//   GET /api/postings          -> { postings: [...] }   (listing, no descriptions)
//   GET /api/postings/<slug>   -> { posting: {...} }    (full description + questions)
// No login, no API key, zero runtime dependencies.
//
// Access: the host serves no robots.txt (the path returns the SPA shell with HTTP 200),
// so there is no stated restriction. The client identifies itself honestly and issues
// one request per run for `search` and one per posting for `detail`.
//
// Scale note: Lasso is a single employer, not a job board. It carries roughly ten
// openings at a time, so `search` fetches the whole list and filters client-side.

export const BASE = "https://careers.lassoinformatics.info"
export const ORG_NAME = "Lasso Informatics"

export type Lang = "en" | "fr"

export function writeError(error: string, code: string): void {
  process.stderr.write(JSON.stringify({ error, code }) + "\n")
}

const UA = "Mozilla/5.0 (compatible; lassoinformatics-cli/1.0)"

/** Fetch JSON with exponential backoff on 429/5xx. Returns null on a 404. */
export async function jsonFetch<T>(path: string): Promise<T | null> {
  const maxRetries = 6
  let delay = 500
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    const response = await fetch(`${BASE}${path}`, {
      headers: { "User-Agent": UA, Accept: "application/json" },
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
    if (response.status === 404) return null
    if (!response.ok) {
      throw new Error(`Request failed: ${response.status} ${response.statusText}`)
    }
    const text = await response.text()
    try {
      return JSON.parse(text) as T
    } catch {
      // An unknown /api path can come back as the SPA's HTML shell instead of a 404.
      return null
    }
  }
  throw new Error("Request failed after max retries")
}

export interface RawPosting {
  id?: string
  slug?: string
  title?: string
  department?: string | null
  location?: string | null
  employmentType?: string | null
  countries?: string[] | null
  salaryCAD?: string | null
  salaryUSD?: string | null
  descriptionMd?: string | null
  descriptionFr?: string | null
  questions?: Array<{ order?: number; type?: string; questionText?: string; questionTextFr?: string }> | null
}

export interface JobCard {
  id: string
  title: string
  company: string
  location: string | null
  date: string | null
  url: string
  department: string | null
  employmentType: string | null
  countries: string[]
  salaryCAD: string | null
  salaryUSD: string | null
}

export interface JobDetail extends JobCard {
  description: string | null
  screeningQuestions: string[]
  applyUrl: string
}

function numericEntity(cp: number): string {
  return cp >= 0 && cp <= 0x10ffff ? String.fromCodePoint(cp) : ""
}

export function decodeHtmlEntities(text: string): string {
  return text
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&apos;/g, "'")
    .replace(/&#(\d+);/g, (_, dec) => numericEntity(parseInt(dec, 10)))
    .replace(/&#[xX]([0-9a-fA-F]+);/g, (_, hex) => numericEntity(parseInt(hex, 16)))
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&") // last, so "&amp;lt;" is not double-decoded
}

/** Fold accents and case so a French query matches an accented title. */
export function fold(s: string): string {
  return s
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
}

/** Convert the posting's HTML body to readable text, preserving paragraph and list breaks. */
export function htmlToText(html: string): string | null {
  // Headings arrive as bare <span>s directly before the next <p>/<ul>, so an opening
  // block tag must also start a new line or "About the Role" fuses with the text after it.
  const withBreaks = html
    .replace(/<li[^>]*>\s*<p[^>]*>/gi, "<li>")
    .replace(/<\/p>\s*<\/li>/gi, "</li>")
    .replace(/<\s*br\s*\/?>/gi, "\n")
    .replace(/<li[^>]*>/gi, "- ")
    .replace(/<(p|ul|ol|h\d|div|section)[ >]/gi, "\n$&")
    .replace(/<\/(p|li|ul|ol|h\d|div|section)>/gi, "\n")
  const text = decodeHtmlEntities(withBreaks.replace(/<[^>]+>/g, ""))
    .replace(/[ \t]+/g, " ")
    .replace(/ *\n */g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim()
  return text || null
}

export function toCard(p: RawPosting): JobCard | null {
  if (!p.slug || !p.title) return null
  return {
    id: p.slug,
    title: decodeHtmlEntities(p.title).trim(),
    company: ORG_NAME,
    location: p.location ?? null,
    date: null, // the API exposes no posting date
    url: `${BASE}/jobs/${p.slug}`,
    department: p.department ?? null,
    employmentType: p.employmentType ?? null,
    countries: p.countries ?? [],
    salaryCAD: p.salaryCAD ?? null,
    salaryUSD: p.salaryUSD ?? null,
  }
}

/** Parse the listing response. Each posting is mapped independently; a bad one is skipped. */
export function parseListing(data: { postings?: RawPosting[] } | null): JobCard[] {
  const out: JobCard[] = []
  for (const p of data?.postings ?? []) {
    const card = toCard(p)
    if (card) out.push(card)
  }
  return out
}

export function parseDetail(p: RawPosting, lang: Lang): JobDetail | null {
  const card = toCard(p)
  if (!card) return null
  const body = lang === "fr" ? (p.descriptionFr ?? p.descriptionMd) : (p.descriptionMd ?? p.descriptionFr)
  const questions = [...(p.questions ?? [])]
    .sort((a, b) => (a.order ?? 0) - (b.order ?? 0))
    .map((q) => (lang === "fr" ? (q.questionTextFr ?? q.questionText) : q.questionText) ?? "")
    .map((q) => q.replace(/^\s*-\s*/, "").trim())
    .filter(Boolean)
  return {
    ...card,
    description: body ? htmlToText(body) : null,
    screeningQuestions: questions,
    applyUrl: `${BASE}/jobs/${p.slug}/apply`,
  }
}

/** Accept a bare slug or any careers.lassoinformatics.info/jobs/<slug> URL. */
export function normalizeSlug(input: string): string | null {
  const fromUrl = input.match(/\/jobs\/([^/?#]+)/i)
  if (fromUrl) return fromUrl[1]
  if (/^[a-z0-9][a-z0-9-]*$/i.test(input)) return input
  return null
}
