#!/usr/bin/env python3
"""Reproduce preserved skill examples in temporary local fixtures only."""
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def code_blocks(path, language):
    text = path.read_text()
    return re.findall(r"^```" + language + r"\s*\n(.*?)^```\s*$", text, re.M | re.S)


def selected_block(path, language, needle):
    matches = [b for b in code_blocks(path, language) if needle in b]
    if len(matches) != 1:
        raise ValueError((str(path), needle, len(matches)))
    return matches[0]


def execute(command, cwd):
    completed = subprocess.run(command, cwd=cwd, text=True, capture_output=True, timeout=20)
    return {
        "exit": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    skills = root / "codex/skills"
    original = root / "kiro/skills"
    result = {"observation_date": "2026-10-03", "scope": "temporary Linux fixtures; review, no implementation changes", "cases": {}}
    with tempfile.TemporaryDirectory(prefix="skill-review-fixtures-") as tmp:
        work = Path(tmp)
        py_path = skills / "python-script-template/SKILL.md"
        source_py = original / "python-script-template/SKILL.md"
        parse = selected_block(py_path, "python", "formatter_class=argparse.RawDescriptionHelpFormatter")
        main_code = selected_block(py_path, "python", "if args.quiet:")
        atomic = selected_block(py_path, "python", "def _atomic_write(")
        assert parse == selected_block(source_py, "python", "formatter_class=argparse.RawDescriptionHelpFormatter")
        assert main_code == selected_block(source_py, "python", "if args.quiet:")
        assert atomic == selected_block(source_py, "python", "def _atomic_write(")
        cli = work / "python_cli.py"
        cli.write_text("import argparse, logging, os, sys\nVERSION = 'review-fixture'\nlog = logging.getLogger('review')\n" + parse + "\n" + main_code)
        no_args = execute(["python3", "-I", str(cli)], work)
        help_result = execute(["python3", "-I", str(cli), "--help"], work)
        assert no_args["exit"] != 0 and "NameError" in no_args["stderr"]
        assert "parser" in no_args["stderr"] and help_result["exit"] == 0
        result["cases"]["python_no_args"] = {"status": "confirmed", "source": str(py_path.relative_to(root)), "same_as_kiro": True, "no_arguments": no_args, "help_control": help_result}
        target = work / "executable.sh"
        target.write_text("exit 0\n")
        target.chmod(0o755)
        namespace = {"os": os}
        exec(compile(atomic, str(py_path), "exec"), namespace)
        before = oct(target.stat().st_mode & 0o777)
        namespace["_atomic_write"](str(target), "exit 0\n")
        after = oct(target.stat().st_mode & 0o777)
        assert (before, after) == ("0o755", "0o600")
        result["cases"]["atomic_write_mode"] = {"status": "confirmed", "same_as_kiro": True, "before": before, "after": after}

        bash_path = skills / "bash-script-template/SKILL.md"
        bash_raw = bash_path.read_text()
        function = re.search(r"^run_msg_info\(\) \{\n.*?^\}", bash_raw, re.M | re.S).group()
        assert function in (original / "bash-script-template/SKILL.md").read_text()
        default_script = function + '\nrun_msg_info 1 false\nreturned=$?\nprintf "returned=%s\\n" "$returned"\nprintf "next step executed\\n"\n'
        normal = execute(["bash", "--noprofile", "--norc", "-c", default_script], work)
        errexit = execute(["bash", "--noprofile", "--norc", "-c", "set -e\n" + default_script], work)
        assert normal["exit"] == 0 and "returned=0" in normal["stdout"]
        assert "next step executed" in normal["stdout"]
        assert errexit["exit"] == 1 and not errexit["stdout"]
        result["cases"]["bash_error_propagation"] = {"status": "confirmed", "same_as_kiro": True, "default": normal, "errexit": errexit}

        lock_path = work / "example.lock"
        first = lock_path.open("w")
        waiter = lock_path.open("w")
        third = None
        try:
            fcntl.flock(first, fcntl.LOCK_EX | fcntl.LOCK_NB)
            try:
                fcntl.flock(waiter, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                blocked_before_release = True
            else:
                raise AssertionError("control lock was not exclusive")
            fcntl.flock(first, fcntl.LOCK_UN)
            first.close()
            # Another participant acquires the old inode between close and remove.
            fcntl.flock(waiter, fcntl.LOCK_EX | fcntl.LOCK_NB)
            lock_path.unlink()
            third = lock_path.open("w")
            fcntl.flock(third, fcntl.LOCK_EX | fcntl.LOCK_NB)
            distinct = os.fstat(waiter.fileno()).st_ino != os.fstat(third.fileno()).st_ino
            assert distinct
            result["cases"]["flock_unlink_race"] = {"status": "confirmed", "source": "codex/skills/work-rules/SKILL.md", "scope": "generic fcntl example, not kiro-lock helper", "blocked_before_release": blocked_before_release, "two_independent_locks_held": True, "different_inodes": distinct, "schedule": "A unlocks/closes; B acquires old inode; A removes path; C locks new inode"}
        finally:
            first.close()
            waiter.close()
            if third is not None:
                third.close()

        normal_md = work / "normal.md"
        nested_md = work / "nested.md"
        normal_md.write_text("# Fixture\n\n[Broken](missing.md)\n")
        nested_md.write_text("# Fixture\n\n````markdown\n```python\nsample\n````\n\n[Broken](missing.md)\n")
        copies = []
        for checker in sorted(skills.glob("*/scripts/md-link-check.py")):
            standard = execute(["python3", "-I", str(checker), str(normal_md)], work)
            nested = execute(["python3", "-I", str(checker), str(nested_md)], work)
            assert standard["exit"] == 1 and nested["exit"] == 0
            copies.append({"checker": str(checker.relative_to(root)), "sha256": digest(checker), "normal": standard, "nested": nested})
        assert len(copies) == 7
        result["cases"]["nested_fence_link_omission"] = {"status": "confirmed", "affected_copies": len(copies), "normal_fixture": normal_md.read_text(), "nested_fixture": nested_md.read_text(), "results": copies}

    cases = json.loads((root / "codex/verification/luna-results.json").read_text())["cases"]
    mismatches = []
    excluded = []
    for case in cases:
        name = case["skill"]
        if not (skills / name / "SKILL.md").is_file():
            excluded.append({"skill": name, "group": case["group"]})
            continue
        current = digest(skills / name / "SKILL.md")
        if current != case["skill_sha256_at_test"]:
            mismatches.append({"skill": name, "group": case["group"], "recorded_hash": case["skill_sha256_at_test"], "current_hash": current, "has_followup_report": bool(case.get("followup_result"))})
    result["cases"]["luna_input_hash_mismatch"] = {"status": "confirmed metadata difference; model behavior not rerun", "mismatches": mismatches, "excluded_non_skill_cases": excluded}
    result["implementation_modified"] = False
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "confirmed_runtime_cases": 5, "link_checker_copies": len(copies), "luna_hash_mismatches": [x["skill"] for x in mismatches]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
