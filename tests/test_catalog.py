import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"


class CatalogTests(unittest.TestCase):
    def test_router_names_every_core_phase(self):
        router = (SKILLS / "gori-mode" / "SKILL.md").read_text()
        for phase in (
            "gori-adopt",
            "gori-triage",
            "gori-grill",
            "gori-domain-model",
            "gori-design",
            "gori-to-spec",
            "gori-implement",
            "gori-code-review",
            "gori-create-verification",
            "gori-verify",
            "gori-maintain-verification",
            "gori-release",
        ):
            self.assertIn(f"../{phase}/SKILL.md", router, phase)

    def test_each_skill_has_identity_and_resolved_local_links(self):
        folders = sorted(path for path in SKILLS.iterdir() if path.is_dir())
        self.assertGreaterEqual(len(folders), 5)
        for folder in folders:
            manifest = folder / "SKILL.md"
            self.assertTrue(manifest.is_file(), folder.name)
            body = manifest.read_text()
            self.assertTrue(body.startswith("---\n"), folder.name)
            frontmatter = body.split("---\n", 2)[1]
            self.assertRegex(frontmatter, rf"(?m)^name:\s*{re.escape(folder.name)}\s*$")
            self.assertRegex(frontmatter, r"(?m)^description:\s*\S+")
            for document in folder.rglob("*.md"):
                content = document.read_text()
                for link in re.findall(r"\[[^]]+\]\(([^)]+)\)", content):
                    if link.startswith(("https://", "http://", "#", "mailto:")):
                        continue
                    self.assertTrue((document.parent / link.split("#", 1)[0]).exists(), f"{document}: {link}")

    def test_published_skills_have_no_local_product_or_home_paths(self):
        for document in SKILLS.rglob("*"):
            if not document.is_file() or document.suffix not in {".md", ".yaml"}:
                continue
            content = document.read_text().lower()
            for forbidden in ("/users/peregregorii", "posthut", "next-saas-starter"):
                self.assertNotIn(forbidden, content, str(document))


if __name__ == "__main__":
    unittest.main()
