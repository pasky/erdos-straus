"""Pass 2 (z52d): redo/complete first-step verdicts after the false-negative audit.
Sets: NC = all Pass-1 needs-compute; SK = all §2 (U*) skipped + 'covered' verdicts that cite no depth file
(data/z52b/pass2/covered_lint.json); TO = touched single-lane items never worked in Pass 1.
Each record carries the item, its repo-status record and its previous Pass-1 record (if any)."""
import json, glob
m = {json.loads(l)['mid']: json.loads(l) for l in open('data/z52b/master.jsonl')}
status = {}
for f in sorted(glob.glob('data/z52b/status/status_*.jsonl')):
    for l in open(f):
        if l.strip():
            r = json.loads(l); status[r['mid']] = r
p1, src = {}, {}
for f in sorted(glob.glob('data/z52b/pass1/outcome_*.jsonl')):
    for l in open(f):
        if l.strip():
            r = json.loads(l); p1[r['mid']] = r; src[r['mid']] = f.split('_')[-1][:3]
lint = set(json.load(open('data/z52b/pass2/covered_lint.json')))
keys = ['mid', 'title', 'connection', 'why', 'first_step', 'alt_first_steps', 'refs', 'tags', 'areas', 'lanes']
def rec(mid):
    d = {k: m[mid].get(k) for k in keys}
    s = status.get(mid, {})
    d['repo_status'] = {k: s.get(k) for k in ('status', 'files', 'evidence', 'note')}
    if mid in p1:
        d['pass1'] = {k: p1[mid].get(k) for k in ('outcome', 'summary', 'evidence', 'next')}
    return d
NC = sorted(k for k, r in p1.items() if r['outcome'] == 'needs-compute')
SK = sorted(k for k, r in p1.items() if (r['outcome'] == 'skipped' and src[k].startswith('U')) or k in lint)
TO = sorted(k for k in m if k not in p1)
def dump(prefix, lst, n):
    k = -(-len(lst) // n)
    for i in range(n):
        with open(f'data/z52b/pass2/batch_{prefix}{i}.jsonl', 'w') as f:
            for mid in lst[i * k:(i + 1) * k]:
                f.write(json.dumps(rec(mid), ensure_ascii=False) + '\n')
dump('NC', NC, 4); dump('SK', SK, 4); dump('TO', TO, 9)
print('NC', len(NC), 'SK', len(SK), 'TO', len(TO))
