"""Extend preserved emoji regressions with planned-work markers and real CLI."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from uuid import uuid4

scratch = Path(__file__).resolve().parent / 'private/scratch'
scratch.mkdir(parents=True, exist_ok=True)
tempfile.tempdir = str(scratch)
@contextmanager
def preserved_fixture_directory(prefix='fixture-', **kwargs):
    # Keep sandbox-readable fixtures with inherited workspace permissions.
    folder = scratch / (prefix + uuid4().hex)
    folder.mkdir()
    yield str(folder)
tempfile.TemporaryDirectory = preserved_fixture_directory
prior = Path(__file__).resolve().parent.parent / '2026-10-05-emoji-style-T-WIN-004/test_emoji_policy.py'
spec = importlib.util.spec_from_file_location('prior_emoji_regressions', prior)
suite = importlib.util.module_from_spec(spec)
spec.loader.exec_module(suite)
suite.CASES += [
    ('purple_planned_work', '🟣 다음 단계', False),
    ('purple_emoji_selector', '🟣\ufe0f 예정', False),
    ('purple_text_selector', '🟣\ufe0e 예정', False),
    ('purple_quote_literal', '> 🟣원문', False),
    ('purple_inline_literal', '`🟣원문`', False),
]
suite.SPACE_CASES += [
    ('purple_space_required', '🟣예정', True),
    ('purple_space_allowed', '🟣 예정', False),
    ('purple_selector_space_required', '🟣\ufe0f예정', True),
]
suite.main()
args = suite.argparse.ArgumentParser()
args.add_argument('--skills', type=Path, required=True)
args.add_argument('--output', type=Path, required=True)
options = args.parse_args()
result = json.loads(options.output.read_text(encoding='utf-8'))
for checker in sorted(options.skills.resolve().glob('*/scripts/md-style-check.py')):
    with tempfile.TemporaryDirectory(prefix='purple-policy-') as tmp:
        for name, body, expected in [('purple_cli_allowed','🟣 예정',0),
                                     ('purple_cli_space','🟣예정',1),
                                     ('purple_cli_other_rejected','\U0001f7e4 예정',1)]:
            fixture = Path(tmp)/(name+'.md')
            fixture.write_text('# 검사\n\n'+body+'\n',encoding='utf-8')
            run = subprocess.run([sys.executable,'-X','utf8','-B',str(checker),'--no-footer',str(fixture)],
                                 capture_output=True,text=True,encoding='utf-8',cwd=tmp)
            result['checks'].append({'consumer':checker.parent.parent.name,'case':name,
                                     'expected_exit':expected,'actual_exit':run.returncode,
                                     'passed':run.returncode==expected})
failures = [c for c in result['checks'] if not c['passed']]
result['status'] = 'FAIL' if failures else 'PASS'
result['cases'] = len(result['checks'])
options.output.write_text(json.dumps(result,indent=2,ensure_ascii=True),encoding='utf-8')
print(json.dumps({'status':result['status'],'consumers':result['consumers'],
                  'cases':result['cases'],'failures':failures},ensure_ascii=True))
if failures:
    raise SystemExit(1)
