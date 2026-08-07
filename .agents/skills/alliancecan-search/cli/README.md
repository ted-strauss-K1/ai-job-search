# alliancecan-cli

Self-contained CLI for the **Digital Research Alliance of Canada** careers pages
(`alliancecan.ca`), in English and French.

Zero runtime dependencies — plain `bun` + `fetch` + regex parsing. `bun install` pulls
dev types only (`typescript`, `@types/bun`), needed for `typecheck` and the test runner.

## Install

```bash
cd .agents/skills/alliancecan-search/cli && bun install
```

## Use

```bash
# Every current opening
bun run src/cli.ts search --format table

# Data-related roles, French edition
bun run src/cli.ts search -q "donnees" --lang fr --format table

# One opening in full
bun run src/cli.ts detail chief-research-and-data-services-officer --format plain
```

Run `bun run src/cli.ts --help` for the full flag reference.

## Develop

```bash
bun run typecheck   # tsc --noEmit
bun run test        # offline parsing + flag validation + live smoke tests
```

`tests/parsing.test.ts` and `tests/cli-flag-validation.test.ts` are offline.
`tests/live-smoke.test.ts` hits the real site to catch markup drift fixtures cannot.
The live tests assert *shape*, not result counts — the Alliance carries only a handful
of openings and counts go stale as postings close.

If live tests fail while offline ones pass, the site changed: re-check the anchors in
`../url-reference.md`, starting with the `<!-- -->` comment-stripping assumption.

## Scope

The Alliance is a single employer, not a job board. There is no server-side search, so
`--query` filters client-side, and `--jobage` is not offered because the listing carries
no dates.
