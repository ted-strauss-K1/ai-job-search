# lassoinformatics-cli

CLI for the Lasso Informatics careers site (`careers.lassoinformatics.info`). Reads the
site's public JSON API (`/api/postings`). Zero runtime dependencies: plain `bun` + `fetch`.

```bash
bun install           # dev types only
bun run typecheck
bun run test          # includes live smoke tests against the real site
bun run src/cli.ts search --format table
bun run src/cli.ts detail sr-data-operations-specialist --format plain
```

See `../SKILL.md` for flags and `../url-reference.md` for the endpoint notes.
