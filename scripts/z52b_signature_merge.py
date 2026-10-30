# Merge raw item files of lane `signature` into data/z52b/signature.jsonl and render BRAINSTORM/z52b_signature.md.
# Filters: literal duplicates (normalised title or connection), ids listed in DROP (obvious nonsense / dup, with reason),
# and applies FIX patches (citation corrections).  Header/summary text lives in data/z52b/signature_header.md.
import json, os, re, collections
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
RAW = os.path.join(ROOT, 'data', 'z52b', 'signature_raw')
ORDER = ['OWN', 'RAW-F', 'RAW-C', 'RAW-B', 'RAW-D', 'RAW-E', 'generic0', 'OWN2']
SRC_TAG = {'OWN': 'gen:integrator', 'RAW-F': 'gen:sub-classical', 'RAW-C': 'gen:sub-arxiv', 'RAW-B': 'gen:sub-erdosproblems',
           'RAW-D': 'gen:sub-oeis-mo-guy', 'RAW-E': 'gen:sub-other-fields', 'generic0': 'gen:sub-generic', 'OWN2': 'gen:integrator'}
DROP = {}   # raw id -> reason
FIX = {}    # raw id -> dict of field overrides
import glob
for dp in sorted(glob.glob(os.path.join(RAW, 'drops*.json'))):
    j = json.load(open(dp)); DROP.update(j.get('drop', {}))
    for k, v in j.get('fix', {}).items(): FIX.setdefault(k, {}).update(v)
FIELDS = ['title', 'connection', 'why', 'first_step', 'refs', 'tags', 'confidence_not_nonsense', 'effort']

def norm(s): return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()

items, seen_t, seen_c, log = [], set(), set(), []
for src in ORDER:
    fn = os.path.join(RAW, src + '.jsonl')
    if not os.path.exists(fn): continue
    for line in open(fn):
        line = line.strip()
        if not line: continue
        d = json.loads(line)
        rid = d.get('id', '?')
        if rid in DROP: log.append((rid, 'drop', DROP[rid])); continue
        if rid in FIX: d.update(FIX[rid])
        t, c = norm(d['title']), norm(d['connection'])
        if t in seen_t or c in seen_c: log.append((rid, 'drop', 'literal duplicate')); continue
        seen_t.add(t); seen_c.add(c)
        e = {k: d.get(k) for k in FIELDS}
        e['refs'] = [r for r in (e['refs'] or []) if r]
        tags = list(dict.fromkeys((e['tags'] or []) + [SRC_TAG[src]]))
        e['tags'] = tags
        if e['confidence_not_nonsense'] not in ('low', 'med', 'high'): e['confidence_not_nonsense'] = 'med'
        if e['effort'] not in ('cheap', 'medium', 'big'): e['effort'] = 'medium'
        e['raw_id'] = rid
        items.append(e)

out = os.path.join(ROOT, 'data', 'z52b', 'signature.jsonl')
with open(out, 'w') as f:
    for k, e in enumerate(items, 1):
        e2 = {'id': f'signature-{k:04d}'}; e2.update(e)
        f.write(json.dumps(e2, ensure_ascii=False) + '\n')
        e['id'] = e2['id']

hdr = open(os.path.join(ROOT, 'data', 'z52b', 'signature_header.md')).read()
tagc = collections.Counter(t for e in items for t in e['tags'])
feat = sorted((t, c) for t, c in tagc.items() if re.fullmatch(r'F\d\d[wpc]?', t))
gen = sorted((t, c) for t, c in tagc.items() if t.startswith('gen:'))
top = [(t, c) for t, c in tagc.most_common() if not re.fullmatch(r'F\d\d[wpc]?', t) and not t.startswith('gen:')][:45]
conf = collections.Counter(e['confidence_not_nonsense'] for e in items)
eff = collections.Counter(e['effort'] for e in items)
hist = (f"**Item count: {len(items)}** (dropped {sum(1 for l in log if l[1]=='drop')} raw items; drop log in "
        f"`data/z52b/signature_raw/drops.json` + literal-duplicate filter).\n\n"
        f"Confidence-not-nonsense: {dict(conf)}; effort: {dict(eff)}.\n\n"
        f"Generators: " + ', '.join(f'{t} {c}' for t, c in gen) + "\n\n"
        f"Feature-tag histogram (features in `data/z52b/signature_features.md`): " + ', '.join(f'{t} {c}' for t, c in feat) + "\n\n"
        f"Top free tags: " + ', '.join(f'{t} {c}' for t, c in top) + "\n")
hdr = hdr.replace('{{HISTOGRAM}}', hist)
lines = [hdr, '\n## Items\n']
for e in items:
    lines.append(f"{int(e['id'].split('-')[1])}. **{e['title']}** [{e['confidence_not_nonsense']}/{e['effort']}] — {e['connection']} "
                 f"— *First step:* {e['first_step']}  \n   `{e['id']}` tags: {', '.join(e['tags'])}\n")
open(os.path.join(ROOT, 'BRAINSTORM', 'z52b_signature.md'), 'w').write('\n'.join(lines))
print(len(items), 'items;', len(log), 'filtered')
for l in log: print('  ', *l)
