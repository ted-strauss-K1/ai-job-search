import { describe, expect, test } from "bun:test";
import { runCLI, parseJSON } from "./helpers";

describe("search", () => {
  test("returns real results for a live query", async () => {
    const result = await runCLI(["search", "-q", "data governance", "--limit", "5"]);
    const data = parseJSON<{ meta: { count: number; total: number }; results: any[] }>(result);
    expect(data.results.length).toBeGreaterThan(0);
    const first = data.results[0];
    expect(typeof first.id).toBe("string");
    expect(first.id.length).toBeGreaterThan(0);
    expect(typeof first.title).toBe("string");
    expect(first.title.length).toBeGreaterThan(0);
    expect(first.url).toContain("jobs.realventures.com/companies/");
  });

  test("missing detail ref exits 1 with a JSON error on stderr", async () => {
    const result = await runCLI(["detail"]);
    expect(result.exitCode).toBe(1);
    const err = JSON.parse(result.stderr);
    expect(err.code).toBe("NO_REF");
  });

  test("bogus flag value for --page exits 1 with a JSON error on stderr", async () => {
    const result = await runCLI(["search", "-q", "data", "--page", "notanumber"]);
    expect(result.exitCode).toBe(1);
    const err = JSON.parse(result.stderr);
    expect(err.code).toBe("BAD_ARG");
  });
});

describe("detail", () => {
  test("fetches full description for a job from search", async () => {
    const searchResult = await runCLI(["search", "-q", "data governance", "--limit", "1"]);
    const searchData = parseJSON<{ results: any[] }>(searchResult);
    expect(searchData.results.length).toBeGreaterThan(0);
    const url = searchData.results[0].url;

    const detailResult = await runCLI(["detail", url]);
    const job = parseJSON<{ id: string; title: string; description: string | null }>(detailResult);
    expect(job.id).toBe(searchData.results[0].id);
    expect(job.title.length).toBeGreaterThan(0);
  });
});
