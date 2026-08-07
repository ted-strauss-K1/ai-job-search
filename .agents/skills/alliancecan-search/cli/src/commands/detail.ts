import { BASE, htmlFetch, parseJobDetail, normalizeSlug, writeError, type Lang } from "../helpers.js"

export interface DetailOpts {
  id: string
  lang?: Lang
  format: "json" | "plain"
}

export async function runDetail(opts: DetailOpts): Promise<number> {
  const parsed = normalizeSlug(opts.id)
  if (!parsed) {
    writeError(`Could not parse an Alliance career-opportunity slug from "${opts.id}"`, "BAD_ID")
    return 1
  }
  // An explicit --lang wins over the language inferred from a pasted URL.
  const lang: Lang = opts.lang ?? parsed.lang

  try {
    const html = await htmlFetch(`${BASE}/${lang}/career-opportunities/${parsed.slug}`)
    if (!html) {
      writeError("Career opportunity not found (it may have closed)", "NOT_FOUND")
      return 1
    }
    const job = parseJobDetail(html, parsed.slug, lang)

    if (opts.format === "plain") {
      const lines = [
        job.title,
        `${job.company || "—"} · ${job.location || "—"}`,
        job.date ? `Posted: ${job.date}` : "",
        "",
        job.description || "(no description)",
        "",
        `URL: ${job.url}`,
        job.applyUrl ? `Apply: ${job.applyUrl}` : "",
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
