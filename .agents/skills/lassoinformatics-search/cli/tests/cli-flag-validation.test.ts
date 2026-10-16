import { describe, expect, test } from "bun:test"
import { runCLI } from "./helpers.js"

describe("flag validation", () => {
  for (const flag of ["page", "limit"]) {
    test(`--${flag} rejects a negative value`, async () => {
      const r = await runCLI(["search", `--${flag}`, "-3"])
      expect(r.exitCode).toBe(1)
      expect(JSON.parse(r.stderr).code).toBe("BAD_ARG")
    })

    test(`--${flag} rejects a fractional value`, async () => {
      const r = await runCLI(["search", `--${flag}`, "2.5"])
      expect(r.exitCode).toBe(1)
      expect(JSON.parse(r.stderr).code).toBe("BAD_ARG")
    })

    test(`--${flag} rejects a non-numeric value`, async () => {
      const r = await runCLI(["search", `--${flag}`, "abc"])
      expect(r.exitCode).toBe(1)
      expect(JSON.parse(r.stderr).code).toBe("BAD_ARG")
    })
  }

  test("--lang rejects an unsupported language", async () => {
    const r = await runCLI(["search", "--lang", "de"])
    expect(r.exitCode).toBe(1)
    expect(JSON.parse(r.stderr).code).toBe("BAD_ARG")
  })

  test("detail with no slug errors", async () => {
    const r = await runCLI(["detail"])
    expect(r.exitCode).toBe(1)
    expect(JSON.parse(r.stderr).code).toBe("NO_ID")
  })

  test("detail rejects an unparseable slug", async () => {
    const r = await runCLI(["detail", "not a slug!"])
    expect(r.exitCode).toBe(1)
    expect(JSON.parse(r.stderr).code).toBe("BAD_ID")
  })

  test("an unknown command errors", async () => {
    const r = await runCLI(["frobnicate"])
    expect(r.exitCode).toBe(1)
    expect(JSON.parse(r.stderr).code).toBe("BAD_CMD")
  })

  test("errors go to stderr, never stdout", async () => {
    const r = await runCLI(["search", "--page", "-1"])
    expect(r.stdout).toBe("")
    expect(r.stderr).not.toBe("")
  })

  test("--help exits 0 and prints usage", async () => {
    const r = await runCLI(["search", "--help"])
    expect(r.exitCode).toBe(0)
    expect(r.stdout).toContain("USAGE")
  })
})
