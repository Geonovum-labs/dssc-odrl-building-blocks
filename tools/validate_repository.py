#!/usr/bin/env python3
"""Small local repository sanity checker.

This is not a replacement for the OGC Building Blocks validation pipeline.
It checks that JSON files parse, every block contains examples.yaml, and
negative test filenames use the required -fail suffix.
"""
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
errors = []

for path in root.glob('**/*.json'):
    try:
        json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'Invalid JSON {path}: {exc}')

for block in [p.parent for p in root.glob('_sources/**/bblock.json')]:
    if not (block / 'examples.yaml').exists():
        errors.append(f'Missing examples.yaml in {block}')
    test_dir = block / 'tests'
    if test_dir.exists():
        for p in test_dir.iterdir():
            if p.is_file() and 'invalid' in p.name.lower() and not p.stem.endswith('-fail'):
                errors.append(f'Invalid negative test filename, expected -fail suffix: {p}')

if errors:
    print('
'.join(errors))
    raise SystemExit(1)
print('OK: JSON parses, examples.yaml present, local naming checks passed')
