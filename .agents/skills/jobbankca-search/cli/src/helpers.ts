// Data source: Job Bank Canada (jobbank.gc.ca) public job search. No authentication.
// Search returns a server-rendered HTML list of <article> job cards; detail returns a
// single posting's HTML. Both are parsed with chunked regex — the markup is shallow,
// stable, and government-maintained, so a DOM parser would be dead weight.
//
// robots.txt (checked 2026-08-07) is `User-agent: *` with `Crawl-delay: 5` and NO
// Disallow rules — every path used here is permitted. The crawl delay is honoured by
// the throttle below; do not remove it.

export const BASE = "https://www.jobbank.gc.ca"
export const SEARCH_URL = `${BASE}/jobsearch/jobsearch`
export const DETAIL_URL = `${BASE}/jobsearch/jobposting`

export function writeError(error: string, code: string): void {
  process.stderr.write(JSON.stringify({ error, code }) + "\n")
}

// Honest self-identification, matching the posture settled upstream in #277/#283:
// name the client rather than impersonating a browser.
const UA = "Mozilla/5.0 (compatible; jobbankca-cli/1.0)"

// robots.txt declares `Crawl-delay: 5`. We serialize requests and hold at least this
// gap between them. The first request in a process is immediate.
const CRAWL_DELAY_MS = 5000
let lastRequestAt = 0

async function respectCrawlDelay(): Promise<void> {
  const waited = Date.now() - lastRequestAt
  if (lastRequestAt !== 0 && waited < CRAWL_DELAY_MS) {
    await new Promise((r) => setTimeout(r, CRAWL_DELAY_MS - waited))
  }
  lastRequestAt = Date.now()
}

/** Fetch HTML with exponential backoff on 429/5xx. Returns "" on a 404. */
export async function htmlFetch(url: string): Promise<string> {
  const maxRetries = 6
  let delay = 500
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    await respectCrawlDelay()
    const response = await fetch(url, {
      headers: {
        "User-Agent": UA,
        Accept: "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-CA,en;q=0.9,fr-CA;q=0.8",
      },
      redirect: "follow",
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
  salary: string | null
  telework: string | null
  url: string
}

export interface JobDetail extends JobCard {
  description: string | null
  eligibility: string | null
  applyUrl: string
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
    // Numeric character references: decimal (&#233;) and hexadecimal (&#xE9;).
    // Job Bank emits both, and Quebec place names depend on them (Montréal).
    .replace(/&#(\d+);/g, (_, dec) => numericEntity(parseInt(dec, 10)))
    .replace(/&#[xX]([0-9a-fA-F]+);/g, (_, hex) => numericEntity(parseInt(hex, 16)))
    .replace(/&nbsp;/g, " ")
}

/**
 * Job Bank labels fields with visually-hidden `wb-inv` spans ("Location", "Salary",
 * "Job number:") for screen readers. They are markup, not data — strip them before
 * cleaning or every location comes back as "Location Laval (QC)".
 */
function stripInvisibleLabels(html: string): string {
  return html.replace(/<span[^>]*class="[^"]*wb-inv[^"]*"[^>]*>[\s\S]*?<\/span>/gi, " ")
}

function stripTags(html: string): string {
  return html.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim()
}

export function clean(html: string): string {
  return decodeHtmlEntities(stripTags(stripInvisibleLabels(html))) || ""
}

/** Pull the text of an <li class="X"> out of a card chunk. */
function liText(chunk: string, cls: string): string | null {
  const m = chunk.match(new RegExp(`<li[^>]*class="[^"]*\\b${cls}\\b[^"]*"[^>]*>([\\s\\S]*?)</li>`, "i"))
  if (!m) return null
  const t = clean(m[1])
  return t || null
}

/**
 * Job Bank card links carry a servlet session id and a tracking param:
 *   /jobsearch/jobposting/49978652;jsessionid=7F8A...?source=searchresults
 * Both are stripped so the stored URL stays stable across runs — a URL that carries a
 * dead jsessionid is exactly the kind of entry that breaks every later run on it.
 */
export function normalizeJobUrl(href: string): string {
  const path = decodeHtmlEntities(href).split("?")[0].split(";")[0]
  return path.startsWith("http") ? path : `${BASE}${path}`
}

/**
 * Parse the search response. We split on the per-result <article id="article-N">
 * boundary and parse each chunk independently, so one malformed card cannot break
 * the rest of the page.
 */
export function parseJobCards(html: string): JobCard[] {
  const results: JobCard[] = []
  const chunks = html.split(/<article id="article-/).slice(1)

  for (const chunk of chunks) {
    const idMatch = chunk.match(/^(\d+)/)
    if (!idMatch) continue
    const id = idMatch[1]

    const titleMatch = chunk.match(/class="noctitle"[^>]*>([\s\S]*?)<\/span>/i)
    const title = titleMatch ? clean(titleMatch[1]) : ""
    if (!title) continue

    const hrefMatch = chunk.match(/href="([^"]*\/jobposting\/[^"]+)"/i)
    const url = hrefMatch ? normalizeJobUrl(hrefMatch[1]) : `${DETAIL_URL}/${id}`

    const teleworkMatch = chunk.match(/class="telework"[^>]*>([\s\S]*?)<\/span>/i)

    results.push({
      id,
      title,
      company: liText(chunk, "business"),
      location: liText(chunk, "location"),
      date: liText(chunk, "date"),
      // On search cards the "Salary" label is bare text next to a decorative icon,
      // not a wb-inv span, so stripInvisibleLabels does not reach it.
      salary: normalizeSalary((liText(chunk, "salary") ?? "").replace(/^Salary\s*/i, "")),
      telework: teleworkMatch ? clean(teleworkMatch[1]) || null : null,
      url,
    })
  }

  return results
}

/**
 * Extract the inner HTML of a container by class name, tracking tag depth so nested
 * elements of the same type do not truncate the block (the depth-tracking fix from
 * upstream #204 — Job Bank nests <div>s several levels deep inside the description).
 */
export function extractByClass(html: string, className: string, tag = "div"): string | null {
  const escaped = className.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
  const openRe = new RegExp(`<${tag}[^>]*class="[^"]*${escaped}[^"]*"[^>]*>`, "i")
  const open = openRe.exec(html)
  if (!open) return null

  let i = open.index + open[0].length
  let depth = 1
  const openTag = `<${tag}`
  const closeTag = `</${tag}>`

  while (depth > 0 && i < html.length) {
    const nextOpen = html.indexOf(openTag, i)
    const nextClose = html.indexOf(closeTag, i)
    if (nextClose === -1) return null
    if (nextOpen !== -1 && nextOpen < nextClose) {
      depth++
      i = nextOpen + openTag.length
    } else {
      depth--
      i = nextClose + closeTag.length
    }
  }
  return html.slice(open.index + open[0].length, i - closeTag.length)
}

/** Convert a block of HTML to readable text, preserving paragraph/list breaks. */
function blockText(html: string): string | null {
  const withBreaks = stripInvisibleLabels(html)
    .replace(/<\s*br\s*\/?>/gi, "\n")
    .replace(/<\/(p|li|ul|ol|div|h\d|dd|dt)>/gi, "\n")
  const text = decodeHtmlEntities(withBreaks.replace(/<[^>]+>/g, " "))
    .replace(/[ \t]+/g, " ")
    .replace(/ *\n */g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim()
  return text || null
}

/**
 * Tidy the salary string assembled from the RDFa block. Two artefacts come from the
 * markup rather than the data: the currency symbol sits in its own span (so cleaning
 * leaves "$ 28.75"), and `unitText` repeats the period as an uppercase token next to
 * the human-readable one ("HOUR hourly").
 */
export function normalizeSalary(raw: string): string | null {
  const s = raw
    .replace(/\$\s+/g, "$")
    .replace(/\b(HOUR|YEAR|WEEK|MONTH|BIWEEKLY)\b\s*/g, "")
    .replace(/\s+/g, " ")
    .trim()
  return s || null
}

/** Parse a single posting page. */
export function parseJobDetail(html: string, id: string): JobDetail {
  const h1 = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i)
  const title = h1 ? clean(h1[1]) : "(untitled)"

  const org = html.match(/property="hiringOrganization"[^>]*>([\s\S]*?)<\//i)
  const company = org ? clean(org[1]) || null : null

  const reqBlock = extractByClass(html, "job-posting-detail-requirements")
  const description = reqBlock ? blockText(reqBlock) : null

  // "Who can apply for this job?" — citizenship / work-permit conditions. Job Bank
  // states these explicitly, which feeds the work-authorization eligibility gate in
  // 04-job-evaluation.md rather than leaving it to be inferred from the prose.
  const applyBlock = extractByClass(html, "job-posting-detail-apply")
  const eligibility = applyBlock ? blockText(applyBlock) : null

  const loc = html.match(/<span[^>]*property="addressLocality"[^>]*>([\s\S]*?)<\/span>/i)

  // The salary is a nested RDFa block: baseSalary > value > {currency, minValue,
  // maxValue, unitText}, with the currency symbol in a `class="hidden"` span. Matching
  // the inner property directly stops at the first `</span>` and yields just "$", so
  // take the whole enclosing <li> and clean it.
  const salaryLi = html.match(/<li[^>]*>(?:(?!<\/li>)[\s\S])*?property="baseSalary"[\s\S]*?<\/li>/i)
  const salary = salaryLi ? normalizeSalary(clean(salaryLi[0])) : null

  // datePosted carries its value as text ("Posted on July 30, 2026"), not a content=
  // attribute. Strip the label so the field holds a date, not a sentence.
  const dateMatch = html.match(/property="datePosted"[^>]*>([\s\S]*?)<\/span>/i)
  const date = dateMatch ? clean(dateMatch[1]).replace(/^Posted on\s*/i, "") || null : null

  return {
    id,
    title,
    company,
    location: loc ? clean(loc[1]) || null : null,
    date,
    salary,
    telework: /\bHybrid\b/.test(title) ? "Hybrid" : null,
    url: `${DETAIL_URL}/${id}`,
    description,
    eligibility,
    applyUrl: `${DETAIL_URL}/${id}`,
  }
}

/**
 * Map a job-age in days onto Job Bank's `fage` parameter. The portal accepts a small
 * set of buckets; anything else is silently ignored server-side (returning unfiltered
 * results), so we snap to the nearest supported bucket rather than pass a value
 * through that would quietly widen the search.
 */
export function jobageToFage(days: number | undefined): string | null {
  if (days === undefined || days <= 0 || days >= 9999) return null
  const buckets = [1, 7, 14, 30]
  for (const b of buckets) if (days <= b) return String(b)
  return null
}
