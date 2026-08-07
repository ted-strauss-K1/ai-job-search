import { describe, expect, test } from "bun:test"
import { parseListing, parseJobDetail, normalizeSlug, fold, clean } from "../src/helpers.js"

// Trimmed from the real alliancecan.ca/en/careers response (2026-08-07). Preserves the
// two quirks that matter: the aria-label carries a trailing "Read More", and the
// server-rendered React output injects empty <!-- --> comment markers.
const LISTING_EN = `
<h2>Current Opportunities</h2>
<a class="!no-underline block" aria-label="Coordinator, Events and Engagement Support (Contract), Read More" href="/en/career-opportunities/coordinator-events-and-engagement-support-contract"><div><h3>Coordinator, Events and Engagement Support (Contract)</h3></div></a>
<a aria-label="Chief Research &amp; Data Services Officer, Read More" href="/en/career-opportunities/chief-research-and-data-services-officer"><h3>Chief Research &amp; Data Services Officer</h3></a>
<a aria-label="Chief Research &amp; Data Services Officer, Read More" href="/en/career-opportunities/chief-research-and-data-services-officer"><h3>duplicate card</h3></a>
`

const LISTING_FR = `
<h2>Postes vacants</h2>
<a aria-label="Chef(fe) des services de recherche et de donn&#233;es, Lire en plus" href="/fr/career-opportunities/chef-fe-des-services-de-recherche-et-de-donnees"><h3>Chef(fe)</h3></a>
`

const DETAIL = `
<main><section class="prose"><h1>Chief Research &amp; Data Services Officer</h1><h2>Position Details</h2>
<div class="grid"><div><strong>Organization<!-- -->:</strong> <!-- -->Digital Research Alliance of Canada</div><div><strong>Location<!-- -->:</strong> <!-- -->Remote</div><div><strong>Posted<!-- -->:</strong> <!-- -->June 19, 2026</div></div></section>
<section><p>View the full description and apply here: <a target="_blank" rel="noopener noreferrer" href="https://plusportal.perrettlaver.com/VacancyDetail/616c2941">Perrett Laver</a></p></section></main>
`

describe("parseListing", () => {
  const cards = parseListing(LISTING_EN, "en")

  test("parses each opening once, de-duplicating repeated anchors", () => {
    expect(cards).toHaveLength(2)
  })

  test("strips the 'Read More' call-to-action out of the title", () => {
    expect(cards[0]!.title).toBe("Coordinator, Events and Engagement Support (Contract)")
    expect(cards[0]!.title).not.toContain("Read More")
  })

  test("decodes entities in the title", () => {
    expect(cards[1]!.title).toBe("Chief Research & Data Services Officer")
  })

  test("uses the slug as the id and builds an absolute URL", () => {
    expect(cards[1]!.id).toBe("chief-research-and-data-services-officer")
    expect(cards[1]!.url).toBe(
      "https://alliancecan.ca/en/career-opportunities/chief-research-and-data-services-officer",
    )
  })

  test("fields absent from the listing are null, never omitted", () => {
    const c = cards[0]!
    expect(c.location).toBeNull()
    expect(c.date).toBeNull()
    expect(Object.keys(c)).toEqual(
      expect.arrayContaining(["id", "title", "company", "location", "date", "url"]),
    )
  })

  test("parses the French edition, whose slugs differ but path segment does not", () => {
    const fr = parseListing(LISTING_FR, "fr")
    expect(fr).toHaveLength(1)
    expect(fr[0]!.title).toBe("Chef(fe) des services de recherche et de données")
    expect(fr[0]!.company).toBe("Alliance de recherche numérique du Canada")
  })
})

describe("parseJobDetail", () => {
  const job = parseJobDetail(DETAIL, "chief-research-and-data-services-officer", "en")

  test("reads the Position Details fields past React's empty comment markers", () => {
    expect(job.company).toBe("Digital Research Alliance of Canada")
    expect(job.location).toBe("Remote")
    expect(job.date).toBe("June 19, 2026")
  })

  test("extracts the title", () => {
    expect(job.title).toBe("Chief Research & Data Services Officer")
  })

  test("captures the external recruiter apply link", () => {
    expect(job.applyUrl).toBe("https://plusportal.perrettlaver.com/VacancyDetail/616c2941")
  })

  test("description is readable text with no markup left in it", () => {
    expect(job.description).toBeTruthy()
    expect(job.description!).not.toContain("<")
    expect(job.description!).not.toContain("&amp;")
  })
})

describe("normalizeSlug", () => {
  test("accepts a bare slug and defaults to English", () => {
    expect(normalizeSlug("project-manager")).toEqual({ slug: "project-manager", lang: "en" })
  })

  test("infers the language from a full URL", () => {
    expect(normalizeSlug("https://alliancecan.ca/fr/career-opportunities/gestionnaire-de-projet")).toEqual({
      slug: "gestionnaire-de-projet",
      lang: "fr",
    })
  })

  test("rejects input that is not a slug or URL", () => {
    expect(normalizeSlug("not a slug!")).toBeNull()
  })
})

describe("fold", () => {
  test("folds accents and case so a plain query matches an accented title", () => {
    expect(fold("données")).toBe(fold("DONNEES"))
    expect(fold("Recherche")).toBe("recherche")
  })

  test("clean() strips comments, tags, and collapses whitespace", () => {
    expect(clean("<p>a<!-- -->  <b>b</b></p>")).toBe("a b")
  })
})
