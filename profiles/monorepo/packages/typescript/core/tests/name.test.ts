import { expect, test } from "bun:test";
import { normalizeName } from "../src/index";

test("normalizes external input", () => {
  expect(normalizeName(" Ada ")).toBe("Ada");
  expect(() => normalizeName("   ")).toThrow("Name is required");
});
