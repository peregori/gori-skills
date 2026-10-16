import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INSTALLER = ROOT / "scripts" / "install.py"


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.repo = Path(self.directory.name) / "product"
        self.repo.mkdir()
        subprocess.run(["git", "init", "-q", str(self.repo)], check=True)

    def run_install(self, *args):
        return subprocess.run(
            [sys.executable, str(INSTALLER), str(self.repo), *args],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_plan_is_read_only_and_core_has_named_phases(self):
        result = self.run_install()
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in ("gori-mode", "gori-triage", "gori-grill", "gori-domain-model", "gori-design", "gori-to-spec", "gori-implement", "gori-code-review", "gori-verify", "gori-release"):
            self.assertIn(name, result.stdout)
        self.assertFalse((self.repo / ".agents").exists())

    def test_apply_is_repeatable(self):
        first = self.run_install("--apply")
        self.assertEqual(first.returncode, 0, first.stderr)
        for name in ("gori-mode", "gori-adopt", "gori-triage", "gori-grill", "gori-domain-model", "gori-design", "gori-to-spec", "gori-implement", "gori-code-review", "gori-create-verification", "gori-verify", "gori-maintain-verification", "gori-release"):
            self.assertTrue((self.repo / ".agents" / "skills" / name / "SKILL.md").is_file())
        installed_router = (self.repo / ".agents" / "skills" / "gori-mode" / "SKILL.md").read_text()
        self.assertIn("maintained by [Pere Gregori](https://github.com/peregori)", installed_router)
        second = self.run_install("--apply")
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertIn("already installed: gori-mode", second.stdout)

    def test_existing_edit_blocks_all_new_copies(self):
        target = self.repo / ".agents" / "skills" / "gori-verify"
        target.mkdir(parents=True)
        (target / "SKILL.md").write_text("local edit\n")
        result = self.run_install("--all", "--apply")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Refusing to overwrite", result.stderr)
        self.assertEqual((target / "SKILL.md").read_text(), "local edit\n")
        self.assertFalse((self.repo / ".agents" / "skills" / "gori-mode").exists())

    def test_installs_only_requested_optional_skill(self):
        result = self.run_install("gtm", "--apply")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.repo / ".agents" / "skills" / "gtm" / "SKILL.md").is_file())
        self.assertFalse((self.repo / ".agents" / "skills" / "gori-mode").exists())

    def test_named_phase_keeps_router_and_peer_links_available(self):
        result = self.run_install("gori-verify", "--apply")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.repo / ".agents" / "skills" / "gori-mode" / "SKILL.md").is_file())
        self.assertTrue((self.repo / ".agents" / "skills" / "gori-maintain-verification" / "SKILL.md").is_file())

    def test_all_includes_optional_skills(self):
        result = self.run_install("--all", "--apply")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.repo / ".agents" / "skills" / "gtm" / "SKILL.md").is_file())
        self.assertTrue((self.repo / ".agents" / "skills" / "vercel-resend-default" / "SKILL.md").is_file())

    def test_refuses_symlinked_skill_destination(self):
        outside = Path(self.directory.name) / "outside"
        outside.mkdir()
        (self.repo / ".agents").symlink_to(outside, target_is_directory=True)
        result = self.run_install("--apply")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must be directories inside the repository", result.stderr)
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
