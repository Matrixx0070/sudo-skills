#!/usr/bin/env python3
"""Regenerate docs/index.json from every docs/skills/<name>/SKILL.md.
Parses frontmatter, computes the sha256 pin over the exact file bytes, and
emits a schema:1 index the SkillRegistryClient accepts."""
import hashlib, json, os, re, sys

ROOT = os.path.join(os.path.dirname(__file__), 'docs', 'skills')
NAME_RE = re.compile(r'^[a-z0-9][a-z0-9.-]{0,63}$', re.I)

try:
    import yaml
    def parse_fm(t):
        m = re.match(r'^---\n(.*?)\n---\n', t, re.S)
        return yaml.safe_load(m.group(1)) if m else {}
except Exception:
    def parse_fm(t):
        m = re.match(r'^---\n(.*?)\n---\n', t, re.S)
        d = {}
        if not m: return d
        for line in m.group(1).splitlines():
            mm = re.match(r'^(\w[\w-]*):\s*(.*)$', line)
            if mm: d[mm.group(1)] = mm.group(2).strip().strip('"\'')
        return d

skills = []
bad = []
for name in sorted(os.listdir(ROOT)):
    f = os.path.join(ROOT, name, 'SKILL.md')
    if not os.path.isfile(f):
        continue
    raw = open(f, 'rb').read()
    text = raw.decode('utf-8')
    fm = parse_fm(text) or {}
    entry_name = str(fm.get('name') or name).strip()
    if not NAME_RE.match(entry_name):
        bad.append(f'{name}: invalid name {entry_name!r}')
        continue
    tags = fm.get('tags') or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.strip('[]').split(',') if t.strip()]
    caps = fm.get('capabilities') or []
    if isinstance(caps, str):
        caps = [c.strip() for c in caps.strip('[]').split(',') if c.strip()]
    skills.append({
        'name': entry_name,
        'version': str(fm.get('version') or '1.0.0'),
        'description': str(fm.get('description') or '').strip(),
        'author': str(fm.get('author') or 'matrixx0070'),
        'path': f'skills/{name}/SKILL.md',
        'sha256': hashlib.sha256(raw).hexdigest(),
        'capabilities': caps,
        'tags': tags,
    })

if bad:
    print('SKIPPED malformed:', *bad, sep='\n  ', file=sys.stderr)

index = {
    'registry': 'sudo-skills',
    'schema': 1,
    'homepage': 'https://sudoapi.shop',
    'updated': sys.argv[1] if len(sys.argv) > 1 else '2026-07-11T18:00:00Z',
    'skills': skills,
}
out = os.path.join(os.path.dirname(__file__), 'docs', 'index.json')
open(out, 'w').write(json.dumps(index, indent=2) + '\n')
print(f'wrote {out} with {len(skills)} skills')
