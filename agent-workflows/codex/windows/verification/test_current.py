#!/usr/bin/env python3
"""Mutation regressions for the reviewed current distribution in isolated TEMP.

No source edits, installation, personal configuration access or network requests.
"""
import argparse
from contextlib import contextmanager
import io
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

_spec = importlib.util.spec_from_file_location('verify_current', Path(__file__).with_name('verify_current.py'))
verifier = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(verifier)


REPO = Path(__file__).resolve().parents[4]


class CurrentContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory(prefix='current-contract-')
        cls.addClassCleanup(cls.temporary.cleanup)
        cls.repo = Path(cls.temporary.name).resolve()
        cls.verification = cls.repo / 'agent-workflows/codex/windows/verification'
        history = json.loads((REPO / 'agent-workflows/codex/windows/verification/source_manifest.json').read_text(encoding='utf-8'))
        routing_path = 'agent-workflows/codex/2026-10-04-personal-routing-T-WIN-004/preservation-map.json'
        routing = json.loads((REPO / routing_path).read_text(encoding='utf-8'))
        relocated = {item['before']: item['preserved'] for item in routing['relocated_preserved_files']}
        native_map = json.loads((REPO / verifier.NATIVE_MAP).read_text(encoding='utf-8'))
        archived = {'codex_windows/' + item['source']: verifier.NATIVE_RECORD + '/' + item['preserved']
                    for item in native_map['files']}
        files = {routing_path, '.codex/config.toml', 'codex_windows/personal/config.example.toml',
                 'agent-workflows/codex/windows/verification/source_manifest.json',
                 'agent-workflows/codex/windows/verification/current_inventory.json', verifier.NATIVE_MAP}
        files.update(archived.values())
        files.update(counterpart['path'] for item in native_map['files']
                     for counterpart in item['linux_or_kiro_counterparts'])
        files.update(item['preserved'] for item in native_map['linux_script_copies'])
        for item in history['files'] + history['settings']:
            previous = relocated.get(item['preserved'], item['preserved'])
            files.update((item['source'], archived.get(previous, previous)))
        for relative in files:
            target = cls.repo / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / relative, target)
        cls.root = cls.repo / 'codex_windows/skills'
        shutil.copytree(REPO / 'codex_windows/skills', cls.root, dirs_exist_ok=True)
        cls.inventory_path = cls.verification / 'current_inventory.json'
        cls.inventory = verifier.read_current_inventory(cls.inventory_path)
        cls.helper = verifier.markdown_helper(cls.root)
        cls.native = cls.root / 'fact-check'
        cls.compat = cls.root / 'work-rules'
        cls.history = history
        cls.routing_path = cls.repo / routing_path
        cls.native_map_path = cls.repo / verifier.NATIVE_MAP
        cls.native_map = native_map
        cls.archived = archived
        cls.relocated = relocated

    @contextmanager
    def changed(self, path, content):
        before = path.read_bytes()
        try:
            path.write_bytes(content.encode('utf-8') if isinstance(content, str) else content)
            yield
        finally:
            path.write_bytes(before)

    def metadata(self, header):
        verifier.check_metadata('---\n' + header + '\n---\n# Skill\n', 'fact-check')

    def test_full_current_and_history_contract(self):
        result = verifier.verify(self.repo)
        self.assertEqual(result['skills'], len(self.inventory))
        self.assertEqual(result['skills'], 21)
        self.assertEqual(result['compat_skills'], 0)
        self.assertEqual(result['native_skills'], 21)
        self.assertEqual(result['source_and_preserved_hashes'], 368)
        self.assertEqual(result['native_interfaces'], 21)
        self.assertEqual(result['archived_files'], len(self.native_map['files']))
        self.assertEqual(result['linux_tool_copies'], 2)

    def test_missing_native_skill(self):
        moved = self.repo / 'moved-native'
        self.native.rename(moved)
        try:
            with self.assertRaisesRegex(ValueError, 'missing=.*fact-check'):
                verifier.current_entries(self.root, self.inventory)
        finally:
            moved.rename(self.native)

    def test_unlisted_empty_skill_folder(self):
        extra = self.root / 'unreviewed'
        extra.mkdir()
        try:
            with self.assertRaisesRegex(ValueError, 'extra=.*unreviewed'):
                verifier.current_entries(self.root, self.inventory)
        finally:
            extra.rmdir()

    def test_missing_skill_entry(self):
        entry = self.native / 'SKILL.md'
        saved = entry.read_bytes()
        entry.unlink()
        try:
            with self.assertRaisesRegex(ValueError, 'Missing skill entry'):
                verifier.current_entries(self.root, self.inventory)
        finally:
            entry.write_bytes(saved)

    def test_invalid_inventory_variants(self):
        variants = [{}, {'schema_version': 1, 'skills': {}},
                    {'schema_version': 1, 'skills': {'../escape': 'native'}},
                    {'schema_version': 1, 'skills': {'fact-check': 'unknown'}}]
        for value in variants:
            with self.subTest(value=value), self.changed(self.inventory_path, json.dumps(value)):
                with self.assertRaises(ValueError):
                    verifier.read_current_inventory(self.inventory_path)

    def test_valid_quoted_metadata(self):
        self.metadata('name: "fact-check"\ndescription: "A scoped check"')

    def test_quoted_metadata_with_comment(self):
        self.metadata('name: fact-check # name\ndescription: "A # scoped check" # comment')

    def test_wrong_metadata_name(self):
        with self.assertRaisesRegex(ValueError, 'Invalid skill metadata'):
            self.metadata('name: other\ndescription: check')

    def test_empty_or_non_string_description(self):
        for value in ('', '" "', '[]', '{}', 'true', '123', 'null', '|',
                      '# comment', 'true # comment', 'null\t# comment', '123 # comment'):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, 'Missing skill description'):
                self.metadata('name: fact-check\ndescription: ' + value)

    def test_duplicate_metadata(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate skill metadata'):
            self.metadata('name: fact-check\nname: fact-check\ndescription: check')

    def test_unclosed_frontmatter(self):
        with self.assertRaisesRegex(ValueError, 'Invalid skill frontmatter'):
            verifier.check_metadata('---\nname: fact-check\ndescription: check\n', 'fact-check')

    def test_missing_compat_block(self):
        with self.assertRaisesRegex(ValueError, 'compatibility block'):
            verifier.active_skill_body('# Legacy source only', 'compat')

    def test_reversed_compat_block(self):
        with self.assertRaisesRegex(ValueError, 'Reversed'):
            verifier.active_skill_body('<!-- CODEX-COMPAT-END -->\n<!-- CODEX-COMPAT-BEGIN -->', 'compat')

    def test_duplicate_compat_block(self):
        text = '<!-- CODEX-COMPAT-BEGIN -->\nactive\n<!-- CODEX-COMPAT-END -->'
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            verifier.active_skill_body(text + text, 'compat')

    def test_native_body_without_compat_markers(self):
        text = (self.native / 'SKILL.md').read_text(encoding='utf-8')
        self.assertEqual(verifier.active_skill_body(text, 'native'), text)

    def test_native_body_rejects_compat_markers(self):
        with self.assertRaisesRegex(ValueError, 'Native skill'):
            verifier.active_skill_body('<!-- CODEX-COMPAT-BEGIN -->', 'native')

    def test_legacy_broken_example_is_outside_active_scope(self):
        text = '<!-- CODEX-COMPAT-BEGIN -->\n# active\n<!-- CODEX-COMPAT-END -->\n[old](missing.md)'
        body = verifier.active_skill_body(text, 'compat')
        self.assertEqual(verifier.check_links(self.compat / 'SKILL.md', body, self.compat, self.helper), 0)

    def test_missing_native_interface(self):
        interface = self.native / 'agents/openai.yaml'
        saved = interface.read_bytes()
        interface.unlink()
        try:
            with self.assertRaisesRegex(ValueError, 'Missing native interface'):
                verifier.check_native_interface(self.native)
        finally:
            interface.write_bytes(saved)

    def test_invalid_native_interface(self):
        interface = self.native / 'agents/openai.yaml'
        for text in ('interface:\n  display_name: ""\n', 'interface:\n  display_name: []\n',
                     'interface:\n  display_name: x\n  display_name: y\n'):
            with self.subTest(text=text), self.changed(interface, text), self.assertRaises(ValueError):
                verifier.check_native_interface(self.native)

    def test_native_broken_inline_dependency(self):
        with self.assertRaisesRegex(ValueError, 'Broken standalone dependency'):
            verifier.check_links(self.native / 'SKILL.md', '[missing](absent.md)', self.native, self.helper)

    def test_link_escape_to_existing_sibling(self):
        with self.assertRaisesRegex(ValueError, 'Broken standalone dependency'):
            verifier.check_links(self.native / 'SKILL.md', '[sibling](../goal-continuation/SKILL.md)', self.native, self.helper)

    def test_encoded_path_and_quoted_title(self):
        target = self.native / '한국어 (자료).md'
        target.write_text('# test\n', encoding='utf-8')
        try:
            self.assertEqual(verifier.check_links(self.native / 'SKILL.md',
                             '[x](<한국어%20(자료).md> "title")', self.native, self.helper), 1)
        finally:
            target.unlink()

    def test_inline_code_and_nested_fences_are_examples(self):
        text = '`[example](missing.md)`\n````text\n```\n[x](missing.md)\n```\n````\n~~~text\n[x](missing.md)\n~~~\n'
        self.assertEqual(verifier.check_links(self.native / 'SKILL.md', text, self.native, self.helper), 0)

    def test_encoded_fragment_character_is_part_of_filename(self):
        target = self.native / '자료#1.md'
        target.write_text('# test\n', encoding='utf-8')
        try:
            self.assertEqual(verifier.check_links(self.native / 'SKILL.md',
                             '[x](자료%231.md#section)', self.native, self.helper), 1)
        finally:
            target.unlink()

    def test_external_link_and_local_anchor_are_outside_file_scope(self):
        text = '[web](https://example.invalid/missing)\n[anchor](#section)'
        self.assertEqual(verifier.check_links(self.native / 'SKILL.md', text, self.native, self.helper), 0)

    def test_broken_link_after_nested_fence_is_checked(self):
        text = '````text\n```\nexample\n```\n````\n[x](missing.md)\n'
        with self.assertRaisesRegex(ValueError, 'Broken standalone dependency'):
            verifier.check_links(self.native / 'SKILL.md', text, self.native, self.helper)

    def test_unclosed_fence_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Unclosed current Markdown fence'):
            verifier.check_links(self.native / 'SKILL.md', '~~~text\nexample\n', self.native, self.helper)

    def test_native_link_checked_by_full_verifier(self):
        entry = self.native / 'SKILL.md'
        text = entry.read_text(encoding='utf-8') + '\n[missing](absent.md)\n'
        with self.changed(entry, text), self.assertRaisesRegex(ValueError, 'Broken standalone dependency'):
            verifier.verify(self.repo)

    def test_preserved_source_tamper(self):
        path = self.repo / self.history['files'][0]['source']
        with self.changed(path, path.read_bytes() + b'\nchanged'), self.assertRaisesRegex(ValueError, 'changed'):
            verifier.verify(self.repo)

    def test_preserved_setting_tamper(self):
        original = self.history['settings'][0]['preserved']
        previous = self.relocated.get(original, original)
        path = self.repo / self.archived.get(previous, previous)
        with self.changed(path, path.read_bytes() + b'\nchanged'), self.assertRaisesRegex(ValueError, 'changed'):
            verifier.verify(self.repo)

    def test_preserved_native_archive_tamper(self):
        item = self.native_map['files'][0]
        path = self.repo / verifier.NATIVE_RECORD / item['preserved']
        with self.changed(path, path.read_bytes() + b'\nchanged'), self.assertRaisesRegex(ValueError, 'Native preserved file changed'):
            verifier.verify(self.repo)

    def test_linux_tool_copy_tamper(self):
        path = self.repo / self.native_map['linux_script_copies'][0]['preserved']
        with self.changed(path, path.read_bytes() + b'\nchanged'), self.assertRaisesRegex(ValueError, 'changed'):
            verifier.verify(self.repo)

    def test_duplicate_native_mapping(self):
        value = dict(self.native_map)
        value['files'] = [*value['files'], value['files'][0]]
        with self.changed(self.native_map_path, json.dumps(value)), self.assertRaisesRegex(ValueError, 'Duplicate native preservation source'):
            verifier.verify(self.repo)

    def test_duplicate_linux_tool_mapping(self):
        value = dict(self.native_map)
        value['linux_script_copies'] = [*value['linux_script_copies'], value['linux_script_copies'][0]]
        with self.changed(self.native_map_path, json.dumps(value)), self.assertRaisesRegex(ValueError, 'Duplicate Linux tool preservation'):
            verifier.verify(self.repo)

    def test_retired_shell_payload_rejected(self):
        path = self.native / 'retired.sh'
        path.write_text('# unused\n', encoding='utf-8')
        try:
            with self.assertRaisesRegex(ValueError, 'Retired Windows payload'):
                verifier.check_windows_distribution(self.root)
        finally:
            path.unlink()

    def test_retired_execution_example_rejected(self):
        entry = self.native / 'SKILL.md'
        with self.changed(entry, entry.read_text(encoding='utf-8') + '\n```bash\necho example\n```\n'):
            with self.assertRaisesRegex(ValueError, 'Non-native Windows instructions'):
                verifier.check_windows_distribution(self.root)

    def test_native_interface_preserves_boolean_policy(self):
        path = self.native / 'agents/openai.yaml'
        original = path.read_text(encoding='utf-8').split('policy:', 1)[0].rstrip() + '\n'
        for value in ('true', 'false'):
            with self.subTest(value=value), self.changed(path, original + 'policy:\n  allow_implicit_invocation: ' + value + '\n'):
                verifier.check_native_interface(self.native)

    def test_native_interface_rejects_invalid_policy(self):
        path = self.native / 'agents/openai.yaml'
        original = path.read_text(encoding='utf-8').split('policy:', 1)[0].rstrip() + '\n'
        for policy in ('', '  allow_implicit_invocation: "true"\n', '  allow_implicit_invocation: true\n  allow_implicit_invocation: false\n'):
            with self.subTest(policy=policy), self.changed(path, original + 'policy:\n' + policy), self.assertRaises(ValueError):
                verifier.check_native_interface(self.native)

    def test_relocated_source_hash_mismatch(self):
        routing = json.loads(self.routing_path.read_text(encoding='utf-8'))
        routing['relocated_preserved_files'][0]['sha256'] = '0' * 64
        with self.changed(self.routing_path, json.dumps(routing)), self.assertRaisesRegex(ValueError, 'Relocation hash differs'):
            verifier.verify(self.repo)

    def test_missing_historical_file_or_setting(self):
        history_path = self.verification / 'source_manifest.json'
        for key in ('files', 'settings'):
            value = dict(self.history)
            value[key] = value[key][:-1]
            with self.subTest(key=key), self.changed(history_path, json.dumps(value)), self.assertRaisesRegex(ValueError, 'Unexpected preservation inventory'):
                verifier.verify(self.repo)


def main():
    global REPO
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=REPO)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    REPO = args.repo.resolve()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(CurrentContractTests)
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    payload = {'tests': result.testsRun, 'passed': result.testsRun - len(result.failures) - len(result.errors),
               'failed': len(result.failures), 'errors': len(result.errors)}
    if args.output:
        args.output.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(payload))
    if not result.wasSuccessful():
        print(stream.getvalue())
    return int(not result.wasSuccessful())


if __name__ == '__main__':
    raise SystemExit(main())
