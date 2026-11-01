"""Blind Opus audit of Pass-2 (Haiku, hardened brief + lint fix round) non-interesting verdicts (z52d)."""
import json, random, glob, collections
random.seed(5202)
master = {json.loads(l)['mid']: json.loads(l) for l in open('data/z52b/master.jsonl')}
pool = collections.defaultdict(list)
for f in sorted(glob.glob('data/z52b/pass2/outcome_*.jsonl')):
    b = f.split('_')[-1].split('.')[0]
    if b == 'MANUAL':
        continue
    for l in open(f):
        r = json.loads(l)
        if r['outcome'] != 'interesting':
            pool[b[:2]].append(dict(batch=b, **r))
want = {'NC': 10, 'SK': 10, 'TO': 12}
sample = []
for t, n in want.items():
    sample += random.sample(pool[t], n)
random.shuffle(sample)
keys = ['mid', 'title', 'connection', 'why', 'first_step', 'alt_first_steps', 'refs', 'tags', 'areas', 'flags']
for i in range(2):
    with open(f'data/z52d/audit2/blind_B{i}.jsonl', 'w') as f:
        for r in sample[i::2]:
            f.write(json.dumps({k: master[r['mid']].get(k) for k in keys}, ensure_ascii=False) + '\n')
    with open(f'data/z52d/audit2/haiku_B{i}.jsonl', 'w') as f:
        for r in sample[i::2]:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(collections.Counter(r['batch'][:2] for r in sample), collections.Counter(r['outcome'] for r in sample))
