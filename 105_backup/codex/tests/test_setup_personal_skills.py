"""Isolated CLI checks: no real home directory or 30/31 checkout is used."""

import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


CODEX_ROOT = Path(__file__).resolve().parents[1]


class PersonalSkillSetupTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="personal skills ")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.codex = self.root / "standalone checkout" / "codex"
        self.codex.mkdir(parents=True)
        shutil.copy2(CODEX_ROOT.parent / ".gitattributes", self.codex.parent)
        shutil.copy2(CODEX_ROOT / "ASSET_CATALOG.json", self.codex)
        shutil.copytree(CODEX_ROOT / "payload" / "skills", self.codex / "payload" / "skills")
        scripts = self.codex / "scripts"
        scripts.mkdir()
        self.script = scripts / "setup_personal_skills.py"
        shutil.copy2(CODEX_ROOT / "scripts" / self.script.name, self.script)
        self.destination = self.root / "personal home" / ".agents" / "skills"

    def run_setup(self, *arguments):
        return subprocess.run([sys.executable, str(self.script), *arguments,
                               "--dest", str(self.destination)],
                              cwd=self.root, capture_output=True, text=True)

    def test_all_install_is_standalone_and_rerun_preserves_files(self):
        result = self.run_setup("install", "--all")
        self.assertEqual(result.returncode, 0, result.stderr)
        catalog = json.loads((self.codex / "ASSET_CATALOG.json").read_text())
        assets = [a for a in catalog["assets"] if a["kind"] == "skill"]
        self.assertEqual(len(list(self.destination.iterdir())), len(assets))
        for asset in assets:
            entries = [asset, *asset.get("required_companion_files", [])]
            for entry in entries:
                relative = Path(entry["source_path"]).relative_to("skills")
                installed = self.destination / relative
                self.assertEqual(hashlib.sha256(installed.read_bytes()).hexdigest(),
                                 entry["sha256"])
        before = {p: p.stat().st_mtime_ns for p in self.destination.rglob("*")}
        result = self.run_setup("install", "--all")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("INSTALLED", result.stdout)
        self.assertEqual(before, {p: p.stat().st_mtime_ns for p in self.destination.rglob("*")})

    def test_dry_run_does_not_create_destination_or_parent(self):
        result = self.run_setup("install", "--all", "--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.destination.parent.exists())

    @unittest.skipUnless(shutil.which("git"), "Git is required for checkout regression")
    def test_autocrlf_checkout_preserves_catalog_bytes_and_installs(self):
        repository = self.codex.parent

        def git(*arguments, cwd=repository):
            result = subprocess.run(["git", *arguments], cwd=cwd,
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)

        git("init", "-q")
        git("-c", "core.autocrlf=false", "add", ".")
        git("-c", "user.name=Setup Fixture", "-c", "user.email=setup@example.invalid",
            "commit", "-qm", "fixture")
        clone = self.root / "autocrlf clone"
        git("-c", "core.autocrlf=true", "clone", "-q", str(repository), str(clone))
        script = clone / "codex" / "scripts" / self.script.name
        result = subprocess.run([sys.executable, str(script), "install", "--all",
                                 "--dest", str(self.destination)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        for source in (self.codex / "payload" / "skills").rglob("*"):
            if source.is_file():
                relative = source.relative_to(self.codex / "payload" / "skills")
                self.assertEqual(source.read_bytes(), (self.destination / relative).read_bytes())

    def test_conflict_prevents_entire_batch_and_preserves_user_content(self):
        self.assertEqual(self.run_setup("install", "--skills", "work-rules").returncode, 0)
        reference = self.destination / "work-rules" / "references" / "operating-rules.md"
        reference.write_text("user edits", encoding="utf-8")
        result = self.run_setup("install", "--skills", "md-link-check", "work-rules")
        self.assertEqual(result.returncode, 1)
        self.assertFalse((self.destination / "md-link-check").exists())
        self.assertEqual(reference.read_text(), "user edits")

    def test_tampered_or_missing_companion_is_rejected_before_writes(self):
        companion = self.codex / "payload" / "skills" / "work-rules" / "references" / "documentation.md"
        companion.write_text("tampered", encoding="utf-8")
        self.assertEqual(self.run_setup("install", "--all").returncode, 1)
        self.assertFalse(self.destination.parent.exists())
        companion.unlink()
        self.assertEqual(self.run_setup("install", "--all").returncode, 1)
        self.assertFalse(self.destination.parent.exists())

    def test_unknown_traversal_and_duplicate_selections_are_rejected(self):
        for names in [("../escape",), ("unknown",), ("work-rules", "work-rules")]:
            with self.subTest(names=names):
                self.assertEqual(self.run_setup("install", "--skills", *names).returncode, 1)
                self.assertFalse(self.destination.parent.exists())

    def test_invalid_companion_path_and_duplicate_json_are_rejected(self):
        path = self.codex / "ASSET_CATALOG.json"
        original = path.read_text()
        catalog = json.loads(original)
        asset = next(a for a in catalog["assets"] if a["id"] == "work-rules")
        asset["required_companion_files"][0]["relative_target"] = "../escape"
        path.write_text(json.dumps(catalog))
        self.assertEqual(self.run_setup("install", "--all").returncode, 1)
        path.write_text(original.replace('"payload_root": "payload",',
                                        '"payload_root": "payload", "payload_root": "payload",'))
        self.assertEqual(self.run_setup("install", "--all").returncode, 1)
        self.assertFalse(self.destination.parent.exists())

    def test_source_and_destination_symlinks_are_preserved_and_rejected(self):
        source = self.codex / "payload" / "skills" / "work-rules" / "SKILL.md"
        outside = self.root / "outside.md"
        outside.write_text("outside", encoding="utf-8")
        source.unlink()
        try:
            source.symlink_to(outside)
        except OSError as error:
            self.skipTest(f"Symlinks unavailable: {error}")
        self.assertEqual(self.run_setup("install", "--skills", "work-rules").returncode, 1)
        self.destination.mkdir(parents=True)
        target = self.destination / "md-link-check"
        target.symlink_to(self.root / "absent", target_is_directory=True)
        self.assertEqual(self.run_setup("install", "--skills", "md-link-check").returncode, 1)
        self.assertTrue(target.is_symlink())
        self.assertEqual(outside.read_text(), "outside")

    def test_existing_setup_lock_is_not_removed(self):
        self.destination.parent.mkdir(parents=True)
        lock = self.destination.parent / ".skills.setup-lock"
        lock.mkdir()
        result = self.run_setup("install", "--all")
        self.assertEqual(result.returncode, 1)
        self.assertTrue(lock.is_dir())
        self.assertFalse(self.destination.exists())

    def test_interrupted_batch_retains_completed_skill_and_cleans_staging_lock(self):
        spec = importlib.util.spec_from_file_location("setup_fixture", self.script)
        setup = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(setup)
        assets = setup.load_skills()
        names = ["md-link-check", "work-rules"]
        snapshots = {n: setup.snapshot(n, assets[n]) for n in names}
        rename = Path.rename

        def fail_second(path, target):
            if path.name == "work-rules":
                raise OSError("simulated publish failure")
            return rename(path, target)

        with mock.patch.object(Path, "rename", fail_second):
            with self.assertRaises(OSError):
                setup.install(self.destination, snapshots, False)
        self.assertEqual((self.destination / "md-link-check" / "SKILL.md").read_bytes(),
                         snapshots["md-link-check"]["SKILL.md"])
        self.assertFalse((self.destination / "work-rules").exists())
        self.assertFalse((self.destination.parent / ".skills.setup-lock").exists())
        self.assertFalse(list(self.destination.parent.glob(".skill-setup-*")))


if __name__ == "__main__":
    unittest.main()
