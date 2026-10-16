// Data source: Real Ventures' Getro-powered job board (jobs.realventures.com).
// Search hits Getro's public JSON search API directly (no HTML parsing needed).
// Detail fetches the SSR HTML page and JSON.parses the embedded Next.js
// __NEXT_DATA__ blob — the page server-renders full job data into that script
// tag, so there is no markup to scrape.

export const SEARCH_URL = "https://api.getro.com/api/v2/collections/166/search/jobs"
export const BOARD_ORIGIN = "https://jobs.realventures.com"

export function writeError(error: string, code: string): void {
  process.stderr.write(JSON.stringify({ error, code }) + "\n")
}

const UA =
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " +
  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

interface FetchOpts {
  method?: "GET" | "POST"
  body?: string
  headers?: Record<string, string>
}

/** Fetch with exponential backoff on 429/5xx. Returns "" on a 404. */
async function backoffFetch(url: string, opts: FetchOpts = {}): Promise<string> {
  const maxRetries = 6
  let delay = 500
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    const response = await fetch(url, {
      method: opts.method ?? "GET",
      body: opts.body,
      headers: {
        "User-Agent": UA,
        "Accept-Language": "en-US,en;q=0.9",
        ...opts.headers,
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

export async function htmlFetch(url: string): Promise<string> {
  return backoffFetch(url, {
    headers: { Accept: "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" },
  })
}

export async function searchFetch(query: string, page0: number, hitsPerPage: number): Promise<string> {
  return backoffFetch(SEARCH_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      Origin: BOARD_ORIGIN,
    },
    body: JSON.stringify({
      hitsPerPage,
      page: page0,
      filters: { q: query },
      query,
    }),
  })
}

export interface JobCard {
  id: string
  title: string
  company: string | null
  companySlug: string | null
  location: string | null
  date: string | null
  url: string
  applyUrl: string | null
  workMode: string | null
  seniority: string | null
  compensation: string | null
}

export interface JobDetail extends JobCard {
  description: string | null
  employmentType: string | null
}

function centsToAmount(cents: number | null): string | null {
  if (cents === null || cents === undefined) return null
  return String(Math.round(cents / 100))
}

function formatCompensation(job: any): string | null {
  const min = centsToAmount(job.compensation_amount_min_cents ?? job.compensationAmountMinCents)
  const max = centsToAmount(job.compensation_amount_max_cents ?? job.compensationAmountMaxCents)
  const currency = job.compensation_currency ?? job.compensationCurrency
  if (!min && !max) return null
  const range = min && max && min !== max ? `${min}-${max}` : min || max
  return currency ? `${currency} ${range}` : range
}

/** Search responses use unix-seconds `created_at`; detail pages use an ISO `postedAt` string. */
function toISODate(value: number | string | null | undefined): string | null {
  if (value === null || value === undefined || value === "") return null
  const date = typeof value === "number" ? new Date(value * 1000) : new Date(value)
  return isNaN(date.getTime()) ? null : date.toISOString().slice(0, 10)
}

/** Map one search-response job object (snake_case) to a JobCard. */
export function mapSearchJob(job: any): JobCard {
  const orgSlug: string | null = job.organization?.slug ?? null
  const jobSlug: string = job.slug ?? String(job.id)
  const boardUrl = orgSlug
    ? `${BOARD_ORIGIN}/companies/${orgSlug}/jobs/${jobSlug}`
    : `${BOARD_ORIGIN}/companies/${jobSlug}`
  return {
    id: String(job.id),
    title: job.title ?? "(untitled)",
    company: job.organization?.name ?? null,
    companySlug: orgSlug,
    location: Array.isArray(job.locations) && job.locations.length > 0 ? job.locations.join("; ") : null,
    date: toISODate(job.created_at),
    url: boardUrl,
    applyUrl: job.url ?? null,
    workMode: job.work_mode ?? null,
    seniority: job.seniority ?? null,
    compensation: formatCompensation(job),
  }
}

/** Parse the POST /search/jobs response body into JobCards + total count. */
export function parseSearchResponse(raw: string): { jobs: JobCard[]; total: number } {
  const data = JSON.parse(raw)
  const jobs = (data?.results?.jobs ?? []).map(mapSearchJob)
  const total = data?.results?.count ?? jobs.length
  return { jobs, total }
}

/** Extract and JSON.parse the Next.js __NEXT_DATA__ blob from an SSR page. */
function extractNextData(html: string): any | null {
  const m = html.match(/__NEXT_DATA__"\s*type="application\/json">([\s\S]*?)<\/script>/)
  if (!m) return null
  try {
    return JSON.parse(m[1])
  } catch {
    return null
  }
}

function stripHtml(html: string): string {
  return html
    .replace(/<\s*br\s*\/?>/gi, "\n")
    .replace(/<\/(p|li|ul|ol|div|h\d)>/gi, "\n")
    .replace(/<[^>]+>/g, "")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&nbsp;/g, " ")
    .replace(/\n{3,}/g, "\n\n")
    .trim()
}

/** Detail-page `locations` are `{ name, ... }` objects; search's are plain strings. */
function locationNames(locations: unknown): string[] {
  if (!Array.isArray(locations)) return []
  return locations.map((l) => (typeof l === "string" ? l : (l as { name?: string })?.name)).filter((n): n is string => !!n)
}

/** Parse a job detail page's SSR HTML (via embedded __NEXT_DATA__) into a JobDetail. */
export function parseJobDetailHtml(html: string): JobDetail | null {
  const data = extractNextData(html)
  const job = data?.props?.pageProps?.initialState?.jobs?.currentJob
  if (!job) return null

  const orgSlug: string | null = job.organization?.slug ?? null
  const jobSlug: string = job.slug ?? String(job.id)
  const boardUrl = orgSlug
    ? `${BOARD_ORIGIN}/companies/${orgSlug}/jobs/${jobSlug}`
    : `${BOARD_ORIGIN}/companies/${jobSlug}`

  const locNames = locationNames(job.locations)

  return {
    id: String(job.id),
    title: job.title ?? "(untitled)",
    company: job.organization?.name ?? null,
    companySlug: orgSlug,
    location: locNames.length > 0 ? locNames.join("; ") : null,
    date: toISODate(job.postedAt),
    url: boardUrl,
    applyUrl: job.applicationPath ?? job.url ?? null,
    workMode: null,
    seniority: null,
    compensation: formatCompensation(job),
    description: job.description ? stripHtml(job.description) : null,
    employmentType: Array.isArray(job.employmentTypes) && job.employmentTypes.length > 0
      ? job.employmentTypes.join(", ")
      : null,
  }
}

/** Parse a `detail` command target into { orgSlug, jobSlug } path components. */
export function parseDetailRef(input: string): { orgSlug: string; jobSlug: string } | null {
  const urlMatch = input.match(/\/companies\/([^/]+)\/jobs\/([^/?#]+)/)
  if (urlMatch) return { orgSlug: urlMatch[1], jobSlug: urlMatch[2] }

  const shorthand = input.match(/^([^/\s]+)\/([^/\s]+)$/)
  if (shorthand) return { orgSlug: shorthand[1], jobSlug: shorthand[2] }

  return null
}
