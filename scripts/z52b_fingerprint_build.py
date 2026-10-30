"""Assemble data/z52b/items_src/b*.py (each defines ITEMS = [ (title, connection, why, first_step, refs, tags, conf, effort), ...])
into data/z52b/fingerprint.jsonl and BRAINSTORM/z52b_fingerprint.md (header from data/z52b/items_src/header.md)."""
import json, glob, runpy, collections, os
items = []
for f in sorted(glob.glob('data/z52b/items_src/b*.py')):
    for t in runpy.run_path(f)['ITEMS']:
        title, conn, why, first, refs, tags, conf, eff = t
        assert conf in ('low','med','high') and eff in ('cheap','medium','big'), (title, conf, eff)
        items.append(dict(title=title, connection=conn, why=why, first_step=first, refs=list(refs), tags=list(tags),
                          confidence_not_nonsense=conf, effort=eff))
seen = set()
for it in items:
    assert it['title'] not in seen, 'duplicate title: ' + it['title']; seen.add(it['title'])
with open('data/z52b/fingerprint.jsonl', 'w') as fo:
    for i, it in enumerate(items, 1):
        it = dict(id='fingerprint-%04d' % i, **it); fo.write(json.dumps(it, ensure_ascii=False) + '\n')
hdr = open('data/z52b/items_src/header.md').read()
tagc = collections.Counter(t for it in items for t in it['tags'])
hist = ', '.join(f'{t} {c}' for t, c in tagc.most_common(45))
hdr = hdr.replace('{{COUNT}}', str(len(items))).replace('{{TAGS}}', hist)
import re
def _rid(m):
    pre = m.group(1); hits = [i for i, it in enumerate(items, 1) if it['title'].startswith(pre)]
    assert len(hits) == 1, ('ID ref', pre, hits); return '%04d' % hits[0]
hdr = re.sub(r'\{\{ID:([^}]*)\}\}', _rid, hdr)
lines = [hdr, '\n## Items\n']
for i, it in enumerate(items, 1):
    lines.append(f"{i}. **{it['title']}** — {it['connection']} — *First step:* {it['first_step']} "
                 f"[`fingerprint-{i:04d}`; {it['confidence_not_nonsense']}/{it['effort']}; {', '.join(it['tags'])}]\n")
open('BRAINSTORM/z52b_fingerprint.md', 'w').write('\n'.join(lines))
print(len(items), 'items')
