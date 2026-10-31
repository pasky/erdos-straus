"""Stratified random sample of Haiku Pass-1 verdicts (U00-U09) for the Opus false-negative audit (z52d)."""
import json, random, collections
random.seed(52)
master = {json.loads(l)['mid']: json.loads(l) for l in open('data/z52b/master.jsonl')}
plan = {}  # batch -> {outcome: n}
for b in ['U00', 'U01', 'U03', 'U04', 'U05', 'U06', 'U09']:
    plan[b] = {'nothing': 2, 'skipped': 1, 'covered': 1}
for b in ['U02', 'U07', 'U08']:
    plan[b] = {'nothing': 4, 'skipped': 3, 'covered': 2}
sample = []
for b, want in plan.items():
    outs = [json.loads(l) for l in open(f'data/z52b/pass1/outcome_{b}.jsonl')]
    for oc, n in want.items():
        pool = [o for o in outs if o['outcome'] == oc]
        for o in random.sample(pool, min(n, len(pool))):
            sample.append((b, o))
random.shuffle(sample)
keys = ['mid', 'title', 'connection', 'why', 'first_step', 'alt_first_steps', 'refs', 'tags', 'areas', 'flags']
blind = [{k: master[o['mid']].get(k) for k in keys} for b, o in sample]
reveal = [dict(batch=b, **o) for b, o in sample]
print(len(sample), collections.Counter(b for b, o in sample), collections.Counter(o['outcome'] for b, o in sample))
# split into 4 audit shards
for i in range(4):
    with open(f'data/z52d/audit/blind_A{i}.jsonl', 'w') as f:
        for r in blind[i::4]:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    with open(f'data/z52d/audit/haiku_A{i}.jsonl', 'w') as f:
        for r in reveal[i::4]:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
