import { htmlFetch, parseJobDetailHtml, parseDetailRef, writeError, BOARD_ORIGIN } from "../helpers.js"

export interface DetailOpts {
  ref: string
  format: "json" | "plain"
}

export async function runDetail(opts: DetailOpts): Promise<number> {
  const parsed = parseDetailRef(opts.ref)
  if (!parsed) {
    writeError(
      `Could not parse "${opts.ref}" as a job reference. Pass the full "url" from a search result ` +
        `(e.g. ${BOARD_ORIGIN}/companies/quotemachine/jobs/86713566-senior-director-...) or the ` +
        `"company-slug/job-slug" shorthand. Bare numeric IDs are not supported — this portal has no id-only lookup API.`,
      "BAD_REF",
    )
    return 1
  }

  try {
    const html = await htmlFetch(`${BOARD_ORIGIN}/companies/${parsed.orgSlug}/jobs/${parsed.jobSlug}`)
    if (!html) {
      writeError("Job not found", "NOT_FOUND")
      return 1
    }
    const job = parseJobDetailHtml(html)
    if (!job) {
      writeError("Could not parse job data from the detail page (unexpected page structure)", "PARSE_FAILED")
      return 1
    }

    if (opts.format === "plain") {
      const lines = [
        job.title,
        `${job.company || "—"} · ${job.location || "—"}`,
        "",
        job.employmentType ? `Employment: ${job.employmentType}` : "",
        job.workMode ? `Work mode: ${job.workMode}` : "",
        job.compensation ? `Compensation: ${job.compensation}` : "",
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
