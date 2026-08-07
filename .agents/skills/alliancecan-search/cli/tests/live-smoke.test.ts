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
 * Live smoke tests against alliancecan.ca. The Alliance carries only a handful of
 * openings, so these assert shape and parseability rather than a result count that
 * would go stale the moment a posting closes.
 */
describe("live search", () => {
  test("lists current openings with populated, markup-free fields", async () => {
    const r = await runCLI(["search"])
    const data = parseJSON<SearchResponse>(r)

    expect(data.results.length).toBeGreaterThan(0)
    expect(data.meta.count).toBe(data.results.length)

    for (const job of data.results) {
      expect(job.id).toMatch(/^[a-z0-9-]+$/i)
      expect(job.title.length).toBeGreaterThan(0)
      expect(job.title).not.toContain("<")
      expect(job.title).not.toContain("Read More")
      expect(job.url).toMatch(/^https:\/\/alliancecan\.ca\/(en|fr)\/career-opportunities\/.+/)
    }
  }, 60000)

  test("the French edition parses too", async () => {
    const r = await runCLI(["search", "--lang", "fr"])
    const data = parseJSON<SearchResponse>(r)
    expect(data.results.length).toBeGreaterThan(0)
    for (const job of data.results) {
      expect(job.title).not.toContain("Lire en plus")
      expect(job.url).toContain("/fr/")
    }
  }, 60000)

  test("--query filters client-side without dropping everything", async () => {
    const all = parseJSON<SearchResponse>(await runCLI(["search"]))
    const filtered = parseJSON<SearchResponse>(await runCLI(["search", "-q", "o"]))
    expect(filtered.results.length).toBeLessThanOrEqual(all.results.length)
  }, 60000)
})

describe("live detail", () => {
  test("returns Position Details and an apply link for a listed opening", async () => {
    const s = parseJSON<SearchResponse>(await runCLI(["search", "--limit", "1"]))
    const slug = s.results[0]!.id

    const r = await runCLI(["detail", slug])
    const job = parseJSON<{
      title: string
      company: string | null
      location: string | null
      date: string | null
      description: string | null
      applyUrl: string | null
    }>(r)

    expect(job.title.length).toBeGreaterThan(0)
    expect(job.company).toBeTruthy()
    expect(job.description).toBeTruthy()
    expect(job.description!).not.toContain("<")
    // The nav must not leak into the description via the <main> restriction.
    expect(job.description!).not.toContain("Board of Directors")
  }, 90000)

  test("an unknown slug fails loudly rather than returning an empty shell", async () => {
    const r = await runCLI(["detail", "no-such-opening-abcxyz"])
    expect(r.exitCode).toBe(1)
    expect(r.stdout).toBe("")
    expect(["NOT_FOUND", "DETAIL_FAILED"]).toContain(JSON.parse(r.stderr).code)
  }, 60000)
})
