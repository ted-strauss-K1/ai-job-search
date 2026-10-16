import { jsonFetch, parseListing, fold, writeError, type JobCard, type RawPosting } from "../helpers.js"

export interface SearchOpts {
  query?: string
  page: number
  limit?: number
  format: "json" | "table" | "plain"
}

const PAGE_SIZE = 25

function renderTable(cards: JobCard[]): string {
  if (cards.length === 0) return "No results."
  const rows = cards.map((c) => {
    const title = (c.title || "").slice(0, 46).padEnd(46)
    const loc = (c.location || "").slice(0, 38).padEnd(38)
    return `${title} ${loc} ${c.id}`
  })
  const header = "TITLE".padEnd(46) + " " + "LOCATION".padEnd(38) + " SLUG"
  return [header, "-".repeat(header.length), ...rows].join("\n")
}

export async function runSearch(opts: SearchOpts): Promise<number> {
  try {
    const data = await jsonFetch<{ postings?: RawPosting[] }>("/api/postings")
    if (data === null) {
      writeError("Postings endpoint returned no JSON (the site may have changed)", "SEARCH_FAILED")
      return 1
    }
    let cards = parseListing(data)

    // Lasso publishes every opening in one response, so keyword filtering happens here.
    // Matches against title and department, accent- and case-folded.
    if (opts.query) {
      const terms = fold(opts.query).split(/\s+/).filter(Boolean)
      cards = cards.filter((c) => {
        const hay = fold(`${c.title} ${c.department ?? ""}`)
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
        cards
          .map((c) =>
            [
              c.title,
              `  ${c.company} · ${c.location ?? "—"}`,
              `  ${c.department ?? "—"} · ${c.employmentType ?? "—"} · ${c.salaryCAD ?? "salary n/a"}`,
              `  id: ${c.id}`,
              `  ${c.url}`,
            ].join("\n"),
          )
          .join("\n\n") + "\n",
      )
    } else {
      process.stdout.write(
        JSON.stringify({ meta: { count: cards.length, page: opts.page }, results: cards }, null, 2) + "\n",
      )
    }
    return 0
  } catch (e) {
    writeError(e instanceof Error ? e.message : String(e), "SEARCH_FAILED")
    return 1
  }
}
