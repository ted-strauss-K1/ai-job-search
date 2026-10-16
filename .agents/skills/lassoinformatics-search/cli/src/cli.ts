#!/usr/bin/env bun
// Self-contained CLI for the Lasso Informatics careers site (careers.lassoinformatics.info).
// Zero runtime dependencies — runs with nothing but `bun`. Reads the site's own public
// JSON API; see helpers.ts for the access notes.

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

const HELP = `lassoinformatics-cli — search openings at Lasso Informatics

USAGE
  bun run src/cli.ts search [flags]
  bun run src/cli.ts detail <slug|url> [--lang en|fr] [--format json|plain]

SEARCH FLAGS
  --query, -q <text>      Filter openings by title/department keyword (accent- and
                          case-insensitive). Omit to list every current opening.
  --page <n>              1-indexed page. Default 1. (Lasso rarely exceeds one page.)
  --limit, -n <n>         Cap results emitted.
  --format <fmt>          json (default) | table | plain.

DETAIL FLAGS
  --lang <en|fr>          Language of the description and screening questions. Default en.

NOTE
  Lasso is a single employer, not a job board — expect about ten openings. There is no
  server-side keyword or date filter, so --query filters client-side and --jobage is not
  offered; the API exposes no posting date (results carry date: null).

EXAMPLES
  bun run src/cli.ts search --format table
  bun run src/cli.ts search -q "data" --format table
  bun run src/cli.ts detail sr-data-operations-specialist --format plain

Public JSON API; no authentication.
`

function parsePositiveInt(name: string, raw: string | boolean | string[]): number | null {
  const s = String(raw)
  if (!/^\d+$/.test(s)) {
    process.stderr.write(
      JSON.stringify({ error: `--${name} must be a positive whole number, got "${s}"`, code: "BAD_ARG" }) + "\n",
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
      lang: lang ?? "en",
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
      JSON.stringify({ error: e instanceof Error ? e.message : String(e), code: "INTERNAL_ERROR" }) + "\n",
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
