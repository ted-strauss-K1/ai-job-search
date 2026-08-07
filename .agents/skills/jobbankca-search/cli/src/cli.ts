#!/usr/bin/env bun
// Self-contained CLI for searching Job Bank Canada (jobbank.gc.ca), the Government of
// Canada's public job board. No external CLI framework and zero runtime dependencies,
// so it runs anywhere `bun` is available with nothing but the repo clone.
//
// Access: jobbank.gc.ca/robots.txt is `User-agent: *` + `Crawl-delay: 5` with no
// Disallow rules. Every path used here is permitted; the crawl delay is honoured in
// helpers.ts. Keep volume reasonable anyway — it is a public service.

import { runSearch, type SearchOpts } from "./commands/search.js"
import { runDetail, type DetailOpts } from "./commands/detail.js"

interface Flags {
  _: string[]
  [k: string]: string | boolean | string[]
}

function parseFlags(argv: string[]): Flags {
  const flags: Flags = { _: [] }
  const alias: Record<string, string> = { q: "query", l: "location", n: "limit" }
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

const HELP = `jobbankca-cli — search Job Bank Canada (jobbank.gc.ca)

USAGE
  bun run src/cli.ts search [flags]
  bun run src/cli.ts detail <id|url> [--format json|plain]

SEARCH FLAGS
  --query, -q <text>      Keywords (job title, skill, NOC term). Recommended.
  --location, -l <text>   Location string, e.g. "Montreal, QC", "Quebec", "Ottawa, ON".
                          Omit to search all of Canada.
  --jobage <days>         Posted within N days. Snaps to Job Bank's buckets: 1, 7, 14, 30.
  --page <n>              1-indexed page (25 results/page). Default 1.
  --limit, -n <n>         Cap results emitted (client-side).
  --format <fmt>          json (default) | table | plain.

EXAMPLES
  bun run src/cli.ts search -q "data governance" -l "Montreal, QC" --format table
  bun run src/cli.ts search -q "research data management" -l "Quebec" --jobage 30 --format table
  bun run src/cli.ts search -q "Moodle" --format table
  bun run src/cli.ts search -q "gestion des donnees" -l "Montreal, QC" --format table
  bun run src/cli.ts detail 49978652 --format plain

Public Government of Canada data. robots.txt permits all paths used here (Crawl-delay: 5,
honoured automatically).
`

/**
 * Parse a flag that must be a positive whole number. Job Bank silently ignores an
 * out-of-range `page`/`fage` and returns unfiltered results, so a mistyped value would
 * otherwise produce wrong results rather than an error (upstream #191/#281).
 */
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

async function main(): Promise<number> {
  const argv = process.argv.slice(2)
  const flags = parseFlags(argv)
  const cmd = (flags._ as string[])[0]

  if (!cmd || flags.help || flags.h) {
    process.stdout.write(HELP)
    return cmd ? 0 : 1
  }

  if (cmd === "search") {
    const query = typeof flags.query === "string" ? flags.query : undefined
    const location = typeof flags.location === "string" ? flags.location : undefined
    if (!query && !location) {
      process.stderr.write(
        JSON.stringify({
          error: 'provide at least --query/-q or --location/-l (e.g. -q "data governance" -l "Montreal, QC")',
          code: "NO_CRITERIA",
        }) + "\n",
      )
      return 1
    }

    let jobage: number | undefined
    let page = 1
    let limit: number | undefined

    if (flags.jobage !== undefined) {
      const v = parsePositiveInt("jobage", flags.jobage)
      if (v === null) return 1
      jobage = v
    }
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
      query,
      location,
      jobage,
      page,
      limit,
      format: (["json", "table", "plain"].includes(fmt) ? fmt : "json") as SearchOpts["format"],
    }
    return runSearch(opts)
  }

  if (cmd === "detail") {
    const id = (flags._ as string[])[1]
    if (!id) {
      process.stderr.write(JSON.stringify({ error: "detail requires an <id|url>", code: "NO_ID" }) + "\n")
      return 1
    }
    const fmt = (flags.format as string) || "json"
    const opts: DetailOpts = { id, format: fmt === "plain" ? "plain" : "json" }
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
