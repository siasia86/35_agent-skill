#!/usr/bin/env python3
"""Install standalone personal skills from this checkout (Python 3.9+).

Uses only the local catalog and standard library. No network, governance
profile, subprocess, agent configuration, or policy installation is required.
Existing differing skills are preserved; identical installs are skipped.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
from pathlib import PurePosixPath
import re
import sys
import tempfile


CODEX_ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z][a-z0-9-]*\Z")
DIGEST = re.compile(r"[0-9a-f]{64}\Z")


class SetupError(Exception):
    """An invalid input or an installation conflict."""


def unique_object(pairs):
    """Reject duplicate JSON keys instead of silently choosing one."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise SetupError(f"Duplicate catalog key: {key}")
        result[key] = value
    return result


def safe_relative(value):
    """Accept only normalized, relative catalog paths."""
    if not isinstance(value, str):
        raise SetupError("Catalog paths must be strings")
    path = PurePosixPath(value)
    if (not value or not path.parts or path.is_absolute() or ".." in path.parts
            or "\\" in value or ":" in value or str(path) != value):
        raise SetupError(f"Unsafe catalog path: {value}")
    return path


def load_skills():
    """Read only this checkout's standalone skill catalog."""
    catalog = json.loads((CODEX_ROOT / "ASSET_CATALOG.json").read_text(
        encoding="utf-8"), object_pairs_hook=unique_object)
    if (not isinstance(catalog, dict)
            or catalog.get("catalog_version") != "0.2-draft"
            or catalog.get("payload_root") != "payload"
            or catalog.get("checksum_algorithm") != "sha256"):
        raise SetupError("Unsupported local catalog format")
    skills = {}
    seen = set()
    for asset in catalog["assets"]:
        name = asset["id"]
        if not isinstance(name, str) or name in seen:
            raise SetupError("Invalid or duplicate catalog asset ID")
        seen.add(name)
        if asset["kind"] != "skill":
            continue
        if not NAME.fullmatch(name):
            raise SetupError(f"Unsafe skill name: {name}")
        if asset["source_path"] != f"skills/{name}/SKILL.md":
            raise SetupError(f"Unexpected skill entrypoint: {name}")
        files = {"SKILL.md": asset["sha256"]}
        for companion in asset.get("required_companion_files", []):
            relative = str(safe_relative(companion["relative_target"]))
            if (companion["source_path"] != f"skills/{name}/{relative}"
                    or relative in files):
                raise SetupError(f"Invalid companion layout: {name}")
            files[relative] = companion["sha256"]
        if any(not isinstance(h, str) or not DIGEST.fullmatch(h)
               for h in files.values()):
            raise SetupError(f"Invalid SHA-256: {name}")
        skills[name] = files
    if not skills:
        raise SetupError("No standalone skills in the catalog")
    return skills


def inventory(root):
    """Enumerate regular files without following symlinks."""
    if root.is_symlink() or not root.is_dir():
        raise SetupError(f"Not a regular skill directory: {root}")
    files = set()
    def read_error(error):
        raise error

    for current, directories, filenames in os.walk(root, followlinks=False, onerror=read_error):
        for name in directories + filenames:
            path = Path(current) / name
            if path.is_symlink():
                raise SetupError(f"Symlink is not supported: {path}")
            if name in filenames:
                if not path.is_file():
                    raise SetupError(f"Not a regular file: {path}")
                files.add(path.relative_to(root).as_posix())
    return files


def snapshot(name, expected):
    """Verify the complete source inventory and retain verified bytes."""
    payload = CODEX_ROOT / "payload"
    if payload.is_symlink() or (payload / "skills").is_symlink():
        raise SetupError("Symlinked payload roots are not supported")
    root = payload / "skills" / name
    if inventory(root) != set(expected):
        raise SetupError(f"Catalog/source file inventory differs: {name}")
    content = {}
    for relative, digest in expected.items():
        data = (root / relative).read_bytes()
        if hashlib.sha256(data).hexdigest() != digest:
            raise SetupError(f"Source hash mismatch: {name}/{relative}")
        content[relative] = data
    return content


def destination_state(target, content):
    """Return new/same or refuse to overwrite a differing installation."""
    if not target.exists() and not target.is_symlink():
        return "new"
    if inventory(target) == set(content) and all(
            (target / relative).read_bytes() == data
            for relative, data in content.items()):
        return "same"
    raise SetupError(f"Existing skill differs; back up and compare: {target}")


def install(destination, snapshots, dry_run):
    """Stage verified bytes and publish only previously absent skill folders."""
    if destination.is_symlink() or (destination.exists() and not destination.is_dir()):
        raise SetupError(f"Invalid destination directory: {destination}")
    states = {name: destination_state(destination / name, content)
              for name, content in snapshots.items()}
    for name, state in states.items():
        print(f"{'SKIP' if state == 'same' else 'INSTALL'} {destination / name}")
    if dry_run or all(state == "same" for state in states.values()):
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    lock = destination.parent / f".{destination.name}.setup-lock"
    try:
        lock.mkdir()
    except FileExistsError as error:
        raise SetupError(f"Another setup may be active; inspect lock: {lock}") from error
    try:
        # Recheck after locking; a competing setup may have just completed.
        states = {name: destination_state(destination / name, content)
                  for name, content in snapshots.items()}
        with tempfile.TemporaryDirectory(prefix=".skill-setup-", dir=destination.parent) as temporary:
            staging = Path(temporary)
            for name, content in snapshots.items():
                if states[name] == "same":
                    continue
                for relative, data in content.items():
                    target = staging / name / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(data)
                if destination_state(staging / name, content) != "same":
                    raise SetupError(f"Staging verification failed: {name}")
            destination.mkdir(exist_ok=True)
            for name, content in snapshots.items():
                if states[name] == "same":
                    continue
                target = destination / name
                if target.exists() or target.is_symlink():
                    raise SetupError(f"Destination changed during setup: {target}")
                (staging / name).rename(target)
                print(f"INSTALLED {target}")
    finally:
        lock.rmdir()


def parse_args():
    """Parse explicit selection and an optional destination override."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("list", "install"))
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--all", action="store_true", help="select every standalone skill")
    selection.add_argument("--skills", nargs="+", metavar="NAME", help="select skill folder names")
    parser.add_argument("--dest", type=Path, default=Path.home() / ".agents" / "skills")
    parser.add_argument("--dry-run", action="store_true", help="validate and preview without writes")
    args = parser.parse_args()
    if args.operation == "install" and not (args.all or args.skills):
        parser.error("install requires --all or --skills NAME ...")
    if args.operation == "list" and (args.all or args.skills or args.dry_run):
        parser.error("list does not take selection or --dry-run options")
    return args


def main():
    """Validate local inputs before any installation writes."""
    args = parse_args()
    try:
        skills = load_skills()
        if args.operation == "list":
            for name, files in sorted(skills.items()):
                print(f"{name} ({len(files)} files)")
            return 0
        names = sorted(skills) if args.all else args.skills
        if len(names) != len(set(names)) or any(name not in skills for name in names):
            raise SetupError("Unknown or duplicate skill selection; use list")
        snapshots = {name: snapshot(name, skills[name]) for name in names}
        install(args.dest.expanduser().absolute(), snapshots, args.dry_run)
        if args.dry_run:
            print("Dry run: no files written")
        else:
            print("Setup complete. Check /skills in a new Codex session.")
        return 0
    except (SetupError, OSError, ValueError, KeyError, TypeError) as error:
        print(f"Setup failed: {error}", file=sys.stderr)
        print("Existing skills were not updated. On a mid-install failure, completed new skills may remain; inspect the destination before retrying.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
