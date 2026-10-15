import { expect, test } from "bun:test";
import { normalizeName } from "starter-typescript";

test("installed public API normalizes input", () => {
  expect(normalizeName(" Ada ")).toBe("Ada");
});
