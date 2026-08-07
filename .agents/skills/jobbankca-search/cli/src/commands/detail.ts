import { DETAIL_URL, htmlFetch, parseJobDetail, writeError } from "../helpers.js"

export interface DetailOpts {
  id: string
  format: "json" | "plain"
}

/** Accept a raw posting ID or any Job Bank jobposting URL (with or without jsessionid). */
function normalizeId(input: string): string | null {
  const fromUrl = input.match(/\/jobposting\/(\d+)/)
  if (fromUrl) return fromUrl[1]
  const bare = input.match(/^(\d{4,})$/)
  if (bare) return bare[1]
  return null
}

export async function runDetail(opts: DetailOpts): Promise<number> {
  const id = normalizeId(opts.id)
  if (!id) {
    writeError(`Could not parse a Job Bank posting ID from "${opts.id}"`, "BAD_ID")
    return 1
  }
  try {
    const html = await htmlFetch(`${DETAIL_URL}/${id}`)
    if (!html) {
      writeError("Job posting not found (it may have expired)", "NOT_FOUND")
      return 1
    }
    const job = parseJobDetail(html, id)

    if (opts.format === "plain") {
      const lines = [
        job.title,
        `${job.company || "—"} · ${job.location || "—"}`,
        job.salary ? `Salary: ${job.salary}` : "",
        job.date ? `Posted: ${job.date}` : "",
        "",
        job.description || "(no description)",
        "",
        job.eligibility ? `— Who can apply —\n${job.eligibility}` : "",
        "",
        `URL: ${job.url}`,
      ].filter((l) => l !== "")
      process.stdout.write(lines.join("\n") + "\n")
    } else {
      process.stdout.write(JSON.stringify(job, null, 2) + "\n")
    }
    return 0
  } catch (e) {
    writeError(e instanceof Error ? e.message : String(e), "DETAIL_FAILED")
    return 1
  }
}
