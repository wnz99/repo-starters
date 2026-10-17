"""Distribution contracts for independently copied Coolify adaptation policies."""

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROFILES = ("python", "typescript", "monorepo")


class CoolifyPolicyTests(unittest.TestCase):
    def test_immutable_acquisition(self):
        self.assertIn(
            "git clone --branch v1.1.1 --depth 1 https://github.com/wnz99/repo-starters.git",
            (ROOT / "README.md").read_text(),
        )

    def test_local_adaptation_entrypoints(self):
        for name in PROFILES:
            with self.subTest(profile=name):
                profile = ROOT / "profiles" / name
                self.assertTrue((profile / "docs/coolify.md").is_file())
                self.assertIn("docs/coolify.md", (profile / "POLISH.md").read_text())
                self.assertIn("(coolify.md)", (profile / "docs/index.md").read_text())
                self.assertIn(
                    "(coolify.md#verification-and-rollback)",
                    (profile / "docs/verification.md").read_text(),
                )
                self.assertEqual(
                    json.loads((profile / ".bootstrap.json").read_text())["options"]["cloud"],
                    {"state": "pending", "answer": None, "details": None},
                )

    def test_required_deployment_outcomes(self):
        for name in PROFILES:
            with self.subTest(profile=name):
                policy = (ROOT / "profiles" / name / "docs/coolify.md").read_text()
                for contract in (
                    "Server cache retention", "forced daily purge disabled",
                    "Application build inputs", "COPY/ADD", "runtime dependency closure",
                    "root and member manifests", "lockfiles", "ignore files", "packaged assets",
                    "Dependency layers", "source-only", "cache hit", "cache miss",
                    "Graceful shutdown", "PID 1", "SIGTERM", "SIGINT", "owned child",
                    "Verification and rollback", "negative watch", "read back",
                    "previous image", "Automatic and adapted behavior",
                    "explicit cloud", "Ordinary setup", "pending",
                ):
                    self.assertIn(contract, policy)
                for private in ("/Users/", "roam-support-pilot", "home.wnz.sh", "../profiles/", "../../"):
                    self.assertNotIn(private, policy)
                if name in ("python", "monorepo"):
                    self.assertIn("--no-install-workspace", policy)
                    self.assertIn("--frozen", policy)
                if name in ("typescript", "monorepo"):
                    self.assertIn("bun install --frozen-lockfile", policy)


if __name__ == "__main__":
    unittest.main()
