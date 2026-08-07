# jobbankca-cli

Self-contained CLI for searching **Job Bank Canada** (`jobbank.gc.ca`), the Government
of Canada's national public job board.

Zero runtime dependencies — plain `bun` + `fetch` + chunked regex parsing. `bun install`
pulls dev types only (`typescript`, `@types/bun`), and they are needed only for
`typecheck` and the test runner.

## Install

```bash
cd .agents/skills/jobbankca-search/cli && bun install
```

## Use

```bash
# Search
bun run src/cli.ts search -q "data governance" -l "Montreal, QC" --format table

# Recent postings only
bun run src/cli.ts search -q "Moodle" --jobage 7 --format table

# Full posting detail
bun run src/cli.ts detail 49978652 --format plain
```

Run `bun run src/cli.ts --help` for the full flag reference.

## Develop

```bash
bun run typecheck   # tsc --noEmit
bun run test        # offline parsing + flag validation + live smoke tests
```

`tests/parsing.test.ts` and `tests/cli-flag-validation.test.ts` are offline.
`tests/live-smoke.test.ts` hits the real portal — that is deliberate, since its job is
to catch markup drift that fixtures cannot. If the live tests fail while the offline
ones pass, the portal changed its markup: re-check the anchors documented in
`../url-reference.md`.

## Access policy

`jobbank.gc.ca/robots.txt` is `User-agent: *` with `Crawl-delay: 5` and no `Disallow`
rules. The crawl delay is honoured in `src/helpers.ts`; the client identifies itself
honestly as `jobbankca-cli/1.0`. Keep volume reasonable.
