import {
  BASE,
  LISTING_PATH,
  htmlFetch,
  parseListing,
  fold,
  writeError,
  type JobCard,
  type Lang,
} from "../helpers.js"

export interface SearchOpts {
  query?: string
  lang: Lang
  page: number
  limit?: number
  format: "json" | "table" | "plain"
}

const PAGE_SIZE = 25

function renderTable(cards: JobCard[]): string {
  if (cards.length === 0) return "No results."
  const rows = cards.map((c) => {
    const title = (c.title || "").slice(0, 52).padEnd(52)
    return `${title} ${c.id}`
  })
  const header = "TITLE".padEnd(52) + " SLUG"
  return [header, "-".repeat(header.length), ...rows].join("\n")
}

export async function runSearch(opts: SearchOpts): Promise<number> {
  try {
    const html = await htmlFetch(`${BASE}${LISTING_PATH[opts.lang]}`)
    let cards = parseListing(html, opts.lang)

    // The Alliance publishes every opening on one page, so keyword filtering happens
    // here rather than server-side. Accent- and case-folded so "donnees" matches
    // "données".
    if (opts.query) {
      const q = fold(opts.query)
      const terms = q.split(/\s+/).filter(Boolean)
      cards = cards.filter((c) => {
        const hay = fold(c.title)
        return terms.every((t) => hay.includes(t))
      })
    }

    const start = (opts.page - 1) * PAGE_SIZE
    cards = cards.slice(start, start + PAGE_SIZE)
    if (opts.limit !== undefined && opts.limit >= 0) cards = cards.slice(0, opts.limit)

    if (opts.format === "table") {
      process.stdout.write(renderTable(cards) + "\n")
    } else if (opts.format === "plain") {
      process.stdout.write(
        cards.map((c) => `${c.title}\n  ${c.company}\n  id: ${c.id}\n  ${c.url}`).join("\n\n") + "\n",
      )
    } else {
      process.stdout.write(
        JSON.stringify({ meta: { count: cards.length, page: opts.page }, results: cards }, null, 2) +
          "\n",
      )
    }
    return 0
  } catch (e) {
    writeError(e instanceof Error ? e.message : String(e), "SEARCH_FAILED")
    return 1
  }
}
