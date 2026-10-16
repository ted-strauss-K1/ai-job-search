import { jsonFetch, parseDetail, normalizeSlug, writeError, type Lang, type RawPosting } from "../helpers.js"

export interface DetailOpts {
  id: string
  lang: Lang
  format: "json" | "plain"
}

export async function runDetail(opts: DetailOpts): Promise<number> {
  const slug = normalizeSlug(opts.id)
  if (!slug) {
    writeError(`Could not parse a Lasso Informatics job slug from "${opts.id}"`, "BAD_ID")
    return 1
  }

  try {
    const data = await jsonFetch<{ posting?: RawPosting }>(`/api/postings/${encodeURIComponent(slug)}`)
    const job = data?.posting ? parseDetail(data.posting, opts.lang) : null
    if (!job) {
      writeError("Posting not found (it may have closed)", "NOT_FOUND")
      return 1
    }

    if (opts.format === "plain") {
      const lines = [
        job.title,
        `${job.company} · ${job.location || "—"}`,
        `${job.department || "—"} · ${job.employmentType || "—"}`,
        job.salaryCAD ? `Salary (CAD): ${job.salaryCAD}` : "",
        "",
        job.description || "(no description)",
        "",
        job.screeningQuestions.length
          ? "Screening questions:\n" + job.screeningQuestions.map((q, i) => `  ${i + 1}. ${q}`).join("\n")
          : "",
        "",
        `URL: ${job.url}`,
        `Apply: ${job.applyUrl}`,
      ].filter((l, i, a) => l !== "" || (a[i - 1] ?? "") !== "")
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
