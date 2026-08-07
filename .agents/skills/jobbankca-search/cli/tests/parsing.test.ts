import { describe, expect, test } from "bun:test"
import {
  parseJobCards,
  normalizeJobUrl,
  jobageToFage,
  decodeHtmlEntities,
  clean,
} from "../src/helpers.js"

// Trimmed from a real jobbank.gc.ca search response (2026-08-07). Keeps the exact
// quirks the parser has to survive: the jsessionid in the href, the visually-hidden
// wb-inv label spans, and the flag spans that precede the title.
const CARD_FIXTURE = `
<article id="article-49978652" class="action-buttons"><a href="/jobsearch/jobposting/49978652;jsessionid=7F8AED926DE44514FFFAE0D5C8C175B8.jobsearch75?source=searchresults" class="resultJobItem">
  <h3 class="title">
    <span class="flag"><span class="telework">Hybrid</span><span class="appmethod">Direct Apply</span></span>
    <span class="job-source job-source-icon-16"><span class="wb-inv">Job Bank</span></span>
    <span class="noctitle"> data management specialist
    </span>
  </h3>
  <ul class="list-unstyled">
    <li class="date">July 30, 2026
    </li>
    <li class="business">Boutique LinenChest (Phase II) inc</li>
    <li class="location"><span class="fas fa-map-marker-alt" aria-hidden="true"></span> <span class="wb-inv">Location</span>
              Laval (QC)
    </li>
    <li class="salary"><span class="fa fa-dollar" aria-hidden="true"></span>
          Salary
          $28.75 to $36.00 hourly (to be negotiated)</li>
  </ul></a></article>
<article id="article-49999538" class="action-buttons"><a href="/jobsearch/jobposting/49999538?source=searchresults" class="resultJobItem">
  <h3 class="title"><span class="noctitle">analyste de donn&#233;es</span></h3>
  <ul class="list-unstyled">
    <li class="date">August 06, 2026</li>
    <li class="business">Universit&#233; de Montr&#233;al</li>
    <li class="location"><span class="wb-inv">Location</span> Montr&#233;al (QC)</li>
  </ul></a></article>
`

describe("parseJobCards", () => {
  const cards = parseJobCards(CARD_FIXTURE)

  test("parses every card on the page", () => {
    expect(cards).toHaveLength(2)
  })

  test("extracts the contract-required fields", () => {
    const c = cards[0]!
    expect(c.id).toBe("49978652")
    expect(c.title).toBe("data management specialist")
    expect(c.company).toBe("Boutique LinenChest (Phase II) inc")
    expect(c.date).toBe("July 30, 2026")
    expect(c.url).toBe("https://www.jobbank.gc.ca/jobsearch/jobposting/49978652")
  })

  test("strips the visually-hidden wb-inv label out of location and salary", () => {
    const c = cards[0]!
    expect(c.location).toBe("Laval (QC)")
    expect(c.location).not.toContain("Location")
    expect(c.salary).toContain("$28.75 to $36.00 hourly")
    expect(c.salary).not.toMatch(/^Salary/)
  })

  test("captures the telework flag", () => {
    expect(cards[0]!.telework).toBe("Hybrid")
    expect(cards[1]!.telework).toBeNull()
  })

  test("decodes accented French place and employer names", () => {
    const c = cards[1]!
    expect(c.title).toBe("analyste de données")
    expect(c.company).toBe("Université de Montréal")
    expect(c.location).toBe("Montréal (QC)")
  })

  test("missing fields are null, never omitted", () => {
    const c = cards[1]!
    expect(c.salary).toBeNull()
    expect(Object.keys(c)).toEqual(
      expect.arrayContaining(["id", "title", "company", "location", "date", "url"]),
    )
  })

  test("a malformed card does not break the rest of the page", () => {
    const broken = `<article id="article-notanumber"><h3></h3></article>` + CARD_FIXTURE
    expect(parseJobCards(broken)).toHaveLength(2)
  })

  test("a card with no title is skipped rather than emitted untitled", () => {
    expect(parseJobCards(`<article id="article-123"><h3 class="title"></h3></article>`)).toHaveLength(0)
  })
})

describe("normalizeJobUrl", () => {
  test("strips the servlet jsessionid so stored URLs stay valid across runs", () => {
    expect(normalizeJobUrl("/jobsearch/jobposting/123;jsessionid=ABC.jobsearch75?source=searchresults")).toBe(
      "https://www.jobbank.gc.ca/jobsearch/jobposting/123",
    )
  })

  test("strips tracking query params", () => {
    expect(normalizeJobUrl("/jobsearch/jobposting/456?source=searchresults")).toBe(
      "https://www.jobbank.gc.ca/jobsearch/jobposting/456",
    )
  })

  test("leaves an already-absolute URL absolute", () => {
    expect(normalizeJobUrl("https://www.jobbank.gc.ca/jobsearch/jobposting/789")).toBe(
      "https://www.jobbank.gc.ca/jobsearch/jobposting/789",
    )
  })
})

describe("jobageToFage", () => {
  test("snaps to Job Bank's supported buckets", () => {
    expect(jobageToFage(1)).toBe("1")
    expect(jobageToFage(5)).toBe("7")
    expect(jobageToFage(7)).toBe("7")
    expect(jobageToFage(20)).toBe("30")
    expect(jobageToFage(30)).toBe("30")
  })

  test("returns null (no filter) rather than passing through a value the portal ignores", () => {
    expect(jobageToFage(undefined)).toBeNull()
    expect(jobageToFage(0)).toBeNull()
    expect(jobageToFage(-1)).toBeNull()
    expect(jobageToFage(60)).toBeNull()
  })
})

describe("entity decoding", () => {
  test("decodes decimal, hex, and named references", () => {
    expect(decodeHtmlEntities("Montr&#233;al")).toBe("Montréal")
    expect(decodeHtmlEntities("Montr&#xE9;al")).toBe("Montréal")
    expect(decodeHtmlEntities("R&amp;D")).toBe("R&D")
  })

  test("drops out-of-range code points instead of throwing", () => {
    expect(() => decodeHtmlEntities("&#1114112;")).not.toThrow()
  })

  test("clean() collapses whitespace and strips tags", () => {
    expect(clean("<span>  a   <b>b</b>  </span>")).toBe("a b")
  })
})
