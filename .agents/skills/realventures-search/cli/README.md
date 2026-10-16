# realventures-cli

Zero-dependency CLI for searching Real Ventures' portfolio-company job board
(`jobs.realventures.com`, Getro-powered). No API key, no login.

## Usage

```bash
bun install   # dev types only, no runtime deps
bun run src/cli.ts search -q "data governance" --format table
bun run src/cli.ts detail "<url from a search result>" --format plain
```

## How it works

- `search` calls the board's own public JSON search API directly
  (`POST api.getro.com/api/v2/collections/166/search/jobs`) — no HTML parsing.
- `detail` fetches the SSR detail page and `JSON.parse`s the embedded Next.js
  `__NEXT_DATA__` script tag rather than scraping rendered markup.

See `../url-reference.md` for the full endpoint documentation and portal quirks
(hitsPerPage cap, no id-only lookup, etc).

## Tests

```bash
bun run test
```
