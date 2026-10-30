"""Build data/z52b/translate.jsonl and BRAINSTORM/z52b_translate.md from scripts/z52b_translate_items_*.py.
Each items file defines ITEMS = [dict(t=title, c=connection, w=why, f=first_step, r=[refs], g=[tags], k=conf, e=effort, kw=[seen-keywords])].
kw (optional) are git-grep'ed (case-insensitive, fixed string) in *.md excluding z52b files; first hit -> tag seen:<file>."""
import glob, importlib.util, json, subprocess, collections, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
items = []
for fn in sorted(glob.glob(os.path.join(ROOT, 'scripts/z52b_translate_items_*.py'))):
    spec = importlib.util.spec_from_file_location('m', fn); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    items += m.ITEMS
def seen(kw):
    for k in kw:
        r = subprocess.run(['git', 'grep', '-il', '-F', k, '--', '*.md', ':!BRAINSTORM/z52b_*', ':!data/z52b/*'],
                           cwd=ROOT, capture_output=True, text=True, timeout=60)
        hits = [h for h in r.stdout.split('\n') if h]
        if hits:
            hits.sort(key=lambda h: (h.startswith('reviews/'), len(h)))
            return 'seen:' + hits[0]
    return None
out = []; titles = set()
for i, it in enumerate(items, 1):
    assert it['t'] not in titles, it['t']; titles.add(it['t'])
    assert it['k'] in ('low', 'med', 'high') and it['e'] in ('cheap', 'medium', 'big'), it['t']
    tags = list(it['g'])
    s = seen(it.get('kw', []))
    if s and s not in tags: tags.append(s)
    out.append(dict(id=f'translate-{i:04d}', title=it['t'], connection=it['c'], why=it['w'], first_step=it['f'],
                    refs=it.get('r', []), tags=tags, confidence_not_nonsense=it['k'], effort=it['e']))
os.makedirs(os.path.join(ROOT, 'data/z52b'), exist_ok=True)
with open(os.path.join(ROOT, 'data/z52b/translate.jsonl'), 'w') as fh:
    for o in out: fh.write(json.dumps(o, ensure_ascii=False) + '\n')
hdr = open(os.path.join(ROOT, 'scripts/z52b_translate_header.md')).read()
hist = collections.Counter(t for o in out for t in o['tags'] if not t.startswith('seen:'))
nseen = sum(any(t.startswith('seen:') for t in o['tags']) for o in out)
lines = [hdr.replace('{N}', str(len(out))).replace('{NSEEN}', str(nseen)).rstrip(), '',
         '## Tag histogram (tags used ≥ 4 times; `seen:` tags excluded)', '',
         ', '.join(f'`{t}` {c}' for t, c in hist.most_common() if c >= 4), '', '## Items', '']
for o in out:
    lines.append(f"{int(o['id'][-4:])}. **{o['title']}** — {o['connection']} — *First step:* {o['first_step']} "
                 f"[{o['confidence_not_nonsense']}/{o['effort']}; {', '.join(o['tags'])}]")
open(os.path.join(ROOT, 'BRAINSTORM/z52b_translate.md'), 'w').write('\n'.join(lines) + '\n')
print(len(out), 'items;', nseen, 'seen;', 'top tags:', hist.most_common(25))
