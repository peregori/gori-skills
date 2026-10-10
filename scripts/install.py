#!/usr/bin/env python3
"""Install selected portable skills into a Git repository without overwriting edits."""

import argparse
import filecmp
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


SOURCE = Path(__file__).resolve().parent.parent / "skills"
CORE = (
    "gori-mode",
    "gori-adopt",
    "gori-triage",
    "gori-grill",
    "gori-domain-model",
    "gori-to-spec",
    "gori-implement",
    "gori-code-review",
    "gori-create-verification",
    "gori-verify",
    "gori-maintain-verification",
    "gori-release",
)


def same_tree(source: Path, target: Path) -> bool:
    if target.is_symlink() or not target.is_dir():
        return False
    source_files = {p.relative_to(source) for p in source.rglob("*") if p.is_file()}
    target_files = {p.relative_to(target) for p in target.rglob("*") if p.is_file()}
    return source_files == target_files and all(
        filecmp.cmp(source / path, target / path, shallow=False)
        for path in source_files
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path, help="target Git repository root")
    parser.add_argument("skills", nargs="*", help="skill names; default: core workflow")
    parser.add_argument("--all", action="store_true", help="select every skill")
    parser.add_argument("--apply", action="store_true", help="copy after showing the plan")
    args = parser.parse_args()

    available = {path.name for path in SOURCE.iterdir() if (path / "SKILL.md").is_file()}
    if args.all and args.skills:
        parser.error("use --all or list skill names, not both")
    selected = set(available if args.all else (args.skills or CORE))
    unknown = selected - available
    if unknown:
        parser.error("unknown skill(s): " + ", ".join(sorted(unknown)))
    if selected.intersection(CORE):
        selected.update(CORE)

    repo = args.repo.expanduser().resolve()
    result = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode or Path(result.stdout.strip()).resolve() != repo:
        parser.error("target must be the root of an existing Git repository")

    destination = repo / ".agents" / "skills"
    if (repo / ".agents").is_symlink() or destination.is_symlink():
        parser.error(".agents and .agents/skills must be directories inside the repository")
    pending = []
    conflicts = []
    for name in sorted(selected):
        target = destination / name
        if target.exists() or target.is_symlink():
            if same_tree(SOURCE / name, target):
                print(f"already installed: {name}")
            else:
                conflicts.append(name)
        else:
            pending.append(name)
            print(f"install: {name} -> {target}")

    if conflicts:
        print("Refusing to overwrite differing skill(s): " + ", ".join(conflicts), file=sys.stderr)
        return 2
    if not args.apply:
        print("Read-only plan. Re-run with --apply to install.")
        return 0
    if not pending:
        print("All selected skills are already installed.")
        return 0

    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".gori-skills-", dir=destination) as staged:
        stage = Path(staged)
        for name in pending:
            shutil.copytree(SOURCE / name, stage / name)
        for name in pending:
            (stage / name).rename(destination / name)
    print("Installed. Review and commit .agents/skills in the target repository.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
