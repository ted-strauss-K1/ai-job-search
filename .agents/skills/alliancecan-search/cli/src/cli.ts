#!/usr/bin/env bun
// Self-contained CLI for the Digital Research Alliance of Canada's careers pages
// (alliancecan.ca). Zero runtime dependencies — runs with nothing but `bun`.
//
// Access: alliancecan.ca/robots.txt is `User-agent: *` / `Allow: /`, disallowing only
// /studio and /api/. Every path used here is permitted.

import { runSearch, type SearchOpts } from "./commands/search.js"
import { runDetail, type DetailOpts } from "./commands/detail.js"
import type { Lang } from "./helpers.js"

interface Flags {
  _: string[]
  [k: string]: string | boolean | string[]
}

function parseFlags(argv: string[]): Flags {
  const flags: Flags = { _: [] }
  const alias: Record<string, string> = { q: "query", n: "limit", L: "lang" }
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i]
    if (a.startsWith("--") || a.startsWith("-")) {
      const key = alias[a.replace(/^-+/, "")] ?? a.replace(/^-+/, "")
      const next = argv[i + 1]
      if (next === undefined || next.startsWith("-")) {
        flags[key] = true
      } else {
        flags[key] = next
        i++
      }
    } else {
      ;(flags._ as string[]).push(a)
    }
  }
  return flags
}

const HELP = `alliancecan-cli — search careers at the Digital Research Alliance of Canada

USAGE
  bun run src/cli.ts search [flags]
  bun run src/cli.ts detail <slug|url> [--lang en|fr] [--format json|plain]

SEARCH FLAGS
  --query, -q <text>      Filter openings by title keyword (accent- and case-insensitive).
                          Omit to list every current opening.
  --lang <en|fr>          Language edition of the careers page. Default en.
  --page <n>              1-indexed page. Default 1. (The Alliance rarely exceeds one page.)
  --limit, -n <n>         Cap results emitted.
  --format <fmt>          json (default) | table | plain.

NOTE
  The Alliance is a single employer, not a job board — expect a handful of openings.
  There is no server-side keyword or date filter, so --query filters client-side and
  --jobage is not offered; posting dates are on the detail page.

EXAMPLES
  bun run src/cli.ts search --format table
  bun run src/cli.ts search -q "data" --format table
  bun run src/cli.ts search --lang fr --format table
  bun run src/cli.ts detail chief-research-and-data-services-officer --format plain

Public pages; robots.txt permits all paths used here.
`

function parsePositiveInt(name: string, raw: string | boolean | string[]): number | null {
  const s = String(raw)
  if (!/^\d+$/.test(s)) {
    process.stderr.write(
      JSON.stringify({
        error: `--${name} must be a positive whole number, got "${s}"`,
        code: "BAD_ARG",
      }) + "\n",
    )
    return null
  }
  const val = parseInt(s, 10)
  if (val < 1) {
    process.stderr.write(
      JSON.stringify({ error: `--${name} must be 1 or greater, got "${s}"`, code: "BAD_ARG" }) + "\n",
    )
    return null
  }
  return val
}

function parseLang(raw: string | boolean | string[] | undefined): Lang | null | "INVALID" {
  if (raw === undefined) return null
  const s = String(raw).toLowerCase()
  if (s === "en" || s === "fr") return s
  process.stderr.write(
    JSON.stringify({ error: `--lang must be "en" or "fr", got "${s}"`, code: "BAD_ARG" }) + "\n",
  )
  return "INVALID"
}

async function main(): Promise<number> {
  const argv = process.argv.slice(2)
  const flags = parseFlags(argv)
  const cmd = (flags._ as string[])[0]

  if (!cmd || flags.help || flags.h) {
    process.stdout.write(HELP)
    return cmd ? 0 : 1
  }

  const lang = parseLang(flags.lang)
  if (lang === "INVALID") return 1

  if (cmd === "search") {
    let page = 1
    let limit: number | undefined
    if (flags.page !== undefined) {
      const v = parsePositiveInt("page", flags.page)
      if (v === null) return 1
      page = v
    }
    if (flags.limit !== undefined) {
      const v = parsePositiveInt("limit", flags.limit)
      if (v === null) return 1
      limit = v
    }

    const fmt = (flags.format as string) || "json"
    const opts: SearchOpts = {
      query: typeof flags.query === "string" ? flags.query : undefined,
      lang: lang ?? "en",
      page,
      limit,
      format: (["json", "table", "plain"].includes(fmt) ? fmt : "json") as SearchOpts["format"],
    }
    return runSearch(opts)
  }

  if (cmd === "detail") {
    const id = (flags._ as string[])[1]
    if (!id) {
      process.stderr.write(JSON.stringify({ error: "detail requires a <slug|url>", code: "NO_ID" }) + "\n")
      return 1
    }
    const fmt = (flags.format as string) || "json"
    const opts: DetailOpts = {
      id,
      lang: lang ?? undefined,
      format: fmt === "plain" ? "plain" : "json",
    }
    return runDetail(opts)
  }

  process.stderr.write(JSON.stringify({ error: `Unknown command "${cmd}"`, code: "BAD_CMD" }) + "\n")
  return 1
}

main()
  .then((code) => process.exit(code))
  .catch((e) => {
    process.stderr.write(
      JSON.stringify({
        error: e instanceof Error ? e.message : String(e),
        code: "INTERNAL_ERROR",
      }) + "\n",
    )
    process.exit(1)
  })

// Unhandled rejections must not exit 0 with empty stdout (upstream #203).
process.on("unhandledRejection", (reason) => {
  process.stderr.write(
    JSON.stringify({
      error: reason instanceof Error ? reason.message : String(reason),
      code: "UNHANDLED_REJECTION",
    }) + "\n",
  )
  process.exit(1)
})
