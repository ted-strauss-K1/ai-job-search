import { describe, expect, test } from "bun:test"
import { runCLI } from "./helpers.js"

/**
 * Job Bank silently ignores an out-of-range `page` or `fage` and returns unfiltered
 * results, so a rejected flag must fail loudly rather than quietly widen the search.
 * These pin the contract from upstream #191/#281.
 */
describe("flag validation", () => {
  for (const flag of ["page", "limit", "jobage"]) {
    test(`--${flag} rejects a negative value`, async () => {
      const r = await runCLI(["search", "-q", "test", `--${flag}`, "-3"])
      expect(r.exitCode).toBe(1)
      expect(JSON.parse(r.stderr).code).toBe("BAD_ARG")
    })

    test(`--${flag} rejects a fractional value`, async () => {
      const r = await runCLI(["search", "-q", "test", `--${flag}`, "1.5"])
      expect(r.exitCode).toBe(1)
      expect(JSON.parse(r.stderr).code).toBe("BAD_ARG")
    })

    test(`--${flag} rejects a non-numeric value`, async () => {
      const r = await runCLI(["search", "-q", "test", `--${flag}`, "abc"])
      expect(r.exitCode).toBe(1)
      expect(JSON.parse(r.stderr).code).toBe("BAD_ARG")
    })
  }

  test("search with neither --query nor --location errors", async () => {
    const r = await runCLI(["search"])
    expect(r.exitCode).toBe(1)
    expect(JSON.parse(r.stderr).code).toBe("NO_CRITERIA")
  })

  test("detail with no id errors", async () => {
    const r = await runCLI(["detail"])
    expect(r.exitCode).toBe(1)
    expect(JSON.parse(r.stderr).code).toBe("NO_ID")
  })

  test("detail rejects an unparseable id", async () => {
    const r = await runCLI(["detail", "not-an-id"])
    expect(r.exitCode).toBe(1)
    expect(JSON.parse(r.stderr).code).toBe("BAD_ID")
  })

  test("an unknown command errors", async () => {
    const r = await runCLI(["frobnicate"])
    expect(r.exitCode).toBe(1)
    expect(JSON.parse(r.stderr).code).toBe("BAD_CMD")
  })

  test("errors go to stderr, never stdout", async () => {
    const r = await runCLI(["search", "--page", "-1", "-q", "x"])
    expect(r.stdout).toBe("")
    expect(r.stderr).not.toBe("")
  })

  test("--help exits 0 and prints usage", async () => {
    const r = await runCLI(["search", "--help"])
    expect(r.exitCode).toBe(0)
    expect(r.stdout).toContain("USAGE")
  })
})
