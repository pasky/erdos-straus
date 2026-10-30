#!/usr/bin/env python3
"""Build data/z52b/free_opus.jsonl and BRAINSTORM/z52b_free_opus.md from batch files.
Batch files: scripts/z52b_free_opus_batch_*.py, each defining ITEMS = [dict(t,c,w,f,r,g,conf,eff)].
IDs are assigned in order (batches sorted by name, append-only)."""
import glob, json, importlib.util, collections, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
items = []
for fn in sorted(glob.glob(os.path.join(ROOT, 'scripts', 'z52b_free_opus_batch_*.py'))):
    spec = importlib.util.spec_from_file_location('b', fn); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for it in m.ITEMS: it.setdefault('sec', getattr(m, 'SEC', None))
    items += m.ITEMS
import subprocess
def seen(k):
    r = subprocess.run(['git', 'grep', '-l', '-i', '-F', '--', k, '--', 'BRAINSTORM/*.md', '*.md'], cwd=ROOT,
                       capture_output=True, text=True, timeout=60)
    fs = [f for f in r.stdout.split('\n') if f and 'z52b_' not in f and not f.endswith('README.md')]
    bs = [f for f in fs if f.startswith('BRAINSTORM/')]
    return (bs or fs)[:1]
for it in items:
    for k in it.get('k', []):
        for f in seen(k):
            tg = f'seen:{f}'
            if tg not in it['g']: it['g'] = it['g'] + [tg]
    if not it.get('k'): pass
out = []
seen_titles = set()
for i, it in enumerate(items, 1):
    assert it['conf'] in ('low', 'med', 'high'), it
    assert it['eff'] in ('cheap', 'medium', 'big'), it
    assert it['t'] not in seen_titles, ('dup title', it['t']); seen_titles.add(it['t'])
    out.append(dict(id=f'free_opus-{i:04d}', title=it['t'], connection=it['c'], why=it['w'], first_step=it['f'],
                    refs=it.get('r', []), tags=it['g'], confidence_not_nonsense=it['conf'], effort=it['eff']))
with open(os.path.join(ROOT, 'data/z52b/free_opus.jsonl'), 'w') as fh:
    for o in out: fh.write(json.dumps(o, ensure_ascii=False) + '\n')
tagc = collections.Counter(t for o in out for t in o['tags'] if not t.startswith('seen:'))
nseen = sum(any(t.startswith('seen:') for t in o['tags']) for o in out)
hdr = open(os.path.join(ROOT, 'scripts/z52b_free_opus_header.md')).read()
L = [hdr.rstrip(), '', f'**Item count: {len(out)}.**', '', '### Tag histogram (tags used ≥ 3 times)', '']
L.append(', '.join(f'`{t}` {c}' for t, c in tagc.most_common() if c >= 3))
L += ['', f'Items with an auto `seen:` tag: {nseen}.']
L += ['', '## Items', '']
sec = None
for o, it in zip(out, items):
    if it.get('sec') and it['sec'] != sec:
        sec = it['sec']; L += ['', f'### {sec}', '']
    L.append(f"{int(o['id'][-4:])}. **{o['title']}** — {o['connection']} — *First step:* {o['first_step']} "
             f"[{', '.join(o['tags'])}; {o['confidence_not_nonsense']}/{o['effort']}]")
open(os.path.join(ROOT, 'BRAINSTORM/z52b_free_opus.md'), 'w').write('\n'.join(L) + '\n')
print(len(out), 'items;', len(tagc), 'tags')
