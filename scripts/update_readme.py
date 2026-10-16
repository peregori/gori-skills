#!/usr/bin/env python3
"""Regenerate the skill catalog in README.md from the portable skill manifests."""

import argparse
import json
import re
from pathlib import Path

from install import CORE


ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
SKILLS = ROOT / "skills"
START = "<!-- BEGIN GENERATED SKILLS -->"
END = "<!-- END GENERATED SKILLS -->"


def skill_description(folder: Path) -> str:
    content = (folder / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", content, re.DOTALL)
    if frontmatter is None:
        raise ValueError(f"Missing frontmatter: {folder / 'SKILL.md'}")
    fields = {}
    for line in frontmatter.group(1).splitlines():
        key, separator, value = line.partition(":")
        if separator:
            fields[key] = value.strip()
    if fields.get("name") != folder.name or not fields.get("description"):
        raise ValueError(f"Invalid name or description: {folder / 'SKILL.md'}")
    description = fields["description"]
    if description.startswith('"'):
        description = json.loads(description)
    summary = description.split(". Use ", 1)[0]
    if summary != description:
        summary += "."
    return summary.replace("|", "\\|")


def catalog() -> str:
    folders = {path.name: path for path in SKILLS.iterdir() if (path / "SKILL.md").is_file()}
    missing = set(CORE) - folders.keys()
    if missing:
        raise ValueError(f"Missing core skills: {', '.join(sorted(missing))}")
    groups = (
        ("Core workflow", CORE),
        ("Optional", sorted(folders.keys() - set(CORE))),
    )
    lines = []
    for title, names in groups:
        if not names:
            continue
        lines.extend((f"### {title}", "", "| Skill | What it helps with |", "| --- | --- |"))
        for name in names:
            lines.append(f"| [`{name}`](skills/{name}/SKILL.md) | {skill_description(folders[name])} |")
        lines.append("")
    return "\n".join(lines).rstrip()


def updated_readme(current: str) -> str:
    if current.count(START) != 1 or current.count(END) != 1:
        raise ValueError("README must contain one pair of generated skill markers")
    before, remainder = current.split(START, 1)
    _, after = remainder.split(END, 1)
    return f"{before}{START}\n\n{catalog()}\n\n{END}{after}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the generated catalog is stale")
    args = parser.parse_args()
    current = README.read_text(encoding="utf-8")
    updated = updated_readme(current)
    if current == updated:
        print("README skill catalog is current.")
        return 0
    if args.check:
        print("README skill catalog is stale. Run: python3 scripts/update_readme.py")
        return 1
    README.write_text(updated, encoding="utf-8")
    print("Updated README skill catalog.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
