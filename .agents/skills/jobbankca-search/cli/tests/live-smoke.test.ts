import { describe, expect, test } from "bun:test"
import { runCLI, parseJSON } from "./helpers.js"

interface SearchResponse {
  meta: { count: number; page: number }
  results: Array<{
    id: string
    title: string
    company: string | null
    location: string | null
    date: string | null
    url: string
  }>
}

/**
 * Live smoke tests. These hit jobbank.gc.ca for real — the whole point is to catch
 * markup drift that offline fixtures cannot. Kept to a handful of requests; the CLI
 * itself honours the robots.txt Crawl-delay of 5s between them.
 */
describe("live search", () => {
  test("returns real, fully-populated results", async () => {
    const r = await runCLI(["search", "-q", "data governance", "-l", "Montreal, QC", "--limit", "5"])
    const data = parseJSON<SearchResponse>(r)

    expect(data.results.length).toBeGreaterThan(0)
    expect(data.meta.count).toBe(data.results.length)
    expect(data.meta.page).toBe(1)

    for (const job of data.results) {
      expect(job.id).toMatch(/^\d+$/)
      expect(job.title.length).toBeGreaterThan(0)
      expect(job.title).not.toContain("<")
      expect(job.url).toMatch(/^https:\/\/www\.jobbank\.gc\.ca\/jobsearch\/jobposting\/\d+$/)
      expect(job.url).not.toContain("jsessionid")
    }
  }, 60000)

  test("--limit caps the result count", async () => {
    const r = await runCLI(["search", "-q", "data", "-l", "Montreal, QC", "--limit", "3"])
    expect(parseJSON<SearchResponse>(r).results.length).toBeLessThanOrEqual(3)
  }, 60000)
})

describe("live detail", () => {
  test("returns a readable description for a posting found by search", async () => {
    const s = await runCLI(["search", "-q", "data", "-l", "Montreal, QC", "--limit", "1"])
    const id = parseJSON<SearchResponse>(s).results[0]!.id

    const d = await runCLI(["detail", id, "--format", "plain"])
    expect(d.exitCode).toBe(0)
    expect(d.stdout.length).toBeGreaterThan(100)
    expect(d.stdout).not.toContain("<div")
    expect(d.stdout).not.toContain("&amp;")
    expect(d.stdout).toContain("URL: https://www.jobbank.gc.ca/jobsearch/jobposting/")
  }, 90000)

  test("a non-existent posting id fails loudly rather than returning an empty shell", async () => {
    const r = await runCLI(["detail", "999999999"])
    expect(r.exitCode).toBe(1)
    expect(r.stdout).toBe("")
    expect(["NOT_FOUND", "DETAIL_FAILED"]).toContain(JSON.parse(r.stderr).code)
  }, 60000)
})
