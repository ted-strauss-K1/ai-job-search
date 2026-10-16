import { describe, expect, test } from "bun:test"
import { runCLI, parseJSON } from "./helpers.js"
import { decodeHtmlEntities, htmlToText, normalizeSlug, parseListing } from "../src/helpers.js"

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

describe("parsing", () => {
  test("parseListing skips a malformed posting without dropping the rest", () => {
    const cards = parseListing({
      postings: [{ slug: "a-role", title: "A &amp; B Role", location: "Montréal" }, { title: "no slug" }, {}],
    })
    expect(cards).toHaveLength(1)
    expect(cards[0]!.title).toBe("A & B Role")
    expect(cards[0]!.url).toBe("https://careers.lassoinformatics.info/jobs/a-role")
  })

  test("htmlToText keeps list items and decodes entities", () => {
    const t = htmlToText("<p>Intro &amp; more</p><ul><li><p>one</p></li><li><p>two</p></li></ul>")
    expect(t).toBe("Intro & more\n\n- one\n- two")
  })

  test("decodeHtmlEntities does not double-decode", () => {
    expect(decodeHtmlEntities("&amp;lt;")).toBe("&lt;")
  })

  test("normalizeSlug accepts slugs and URLs, rejects junk", () => {
    expect(normalizeSlug("sr-data-operations-specialist")).toBe("sr-data-operations-specialist")
    expect(normalizeSlug("https://careers.lassoinformatics.info/jobs/devops-specialist/apply")).toBe("devops-specialist")
    expect(normalizeSlug("not a slug!")).toBeNull()
  })
})

/** Live smoke tests: assert shape, not a count that goes stale when a posting closes. */
describe("live search", () => {
  test("lists current openings with populated, markup-free fields", async () => {
    const data = parseJSON<SearchResponse>(await runCLI(["search"]))
    expect(data.results.length).toBeGreaterThan(0)
    expect(data.meta.count).toBe(data.results.length)
    for (const job of data.results) {
      expect(job.id).toMatch(/^[a-z0-9-]+$/i)
      expect(job.title.length).toBeGreaterThan(0)
      expect(job.title).not.toContain("<")
      expect(job.company).toBe("Lasso Informatics")
      expect(job.url).toMatch(/^https:\/\/careers\.lassoinformatics\.info\/jobs\/.+/)
    }
  }, 60000)

  test("--query filters client-side", async () => {
    const all = parseJSON<SearchResponse>(await runCLI(["search"]))
    const none = parseJSON<SearchResponse>(await runCLI(["search", "-q", "zzzznomatch"]))
    expect(none.results).toHaveLength(0)
    expect(all.results.length).toBeGreaterThan(0)
  }, 60000)
})

describe("live detail", () => {
  test("returns readable text and screening questions for a listed opening", async () => {
    const s = parseJSON<SearchResponse>(await runCLI(["search", "--limit", "1"]))
    const job = parseJSON<{ title: string; description: string | null; applyUrl: string }>(
      await runCLI(["detail", s.results[0]!.id]),
    )
    expect(job.title.length).toBeGreaterThan(0)
    expect(job.description).toBeTruthy()
    expect(job.description!).not.toContain("<span")
    expect(job.applyUrl).toContain("/apply")
  }, 90000)

  test("an unknown slug fails loudly rather than returning an empty shell", async () => {
    const r = await runCLI(["detail", "no-such-opening-abcxyz"])
    expect(r.exitCode).toBe(1)
    expect(r.stdout).toBe("")
    expect(["NOT_FOUND", "DETAIL_FAILED"]).toContain(JSON.parse(r.stderr).code)
  }, 60000)
})
