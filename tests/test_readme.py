import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import update_readme  # noqa: E402


class ReadmeTests(unittest.TestCase):
    def test_stale_catalog_is_detected_without_writing_and_can_be_regenerated(self):
        current = update_readme.README.read_text(encoding="utf-8")
        stale = current.replace("skills/gori-mode/SKILL.md", "skills/old-mode/SKILL.md", 1)
        self.assertNotEqual(stale, current)
        with tempfile.TemporaryDirectory() as directory:
            readme = Path(directory) / "README.md"
            readme.write_text(stale, encoding="utf-8")
            with patch.object(update_readme, "README", readme), contextlib.redirect_stdout(io.StringIO()):
                with patch.object(sys, "argv", ["update_readme.py", "--check"]):
                    self.assertEqual(update_readme.main(), 1)
                self.assertEqual(readme.read_text(encoding="utf-8"), stale)
                with patch.object(sys, "argv", ["update_readme.py"]):
                    self.assertEqual(update_readme.main(), 0)
                self.assertEqual(readme.read_text(encoding="utf-8"), current)


if __name__ == "__main__":
    unittest.main()
