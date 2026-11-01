"""Task A sample: 40 negatives (status in NEG, plausibility 0), stratified across batches.
Seed fixed: SEED=520411. Allocation: largest-remainder proportional to batch negative counts,
then random draw within each batch."""
import random, json, collections, os
from z52d_rank_O_common import load_rows, NEG, OUT
SEED = 520411; K = 40
rows = load_rows()
pool = [r for r in rows if r['status'] in NEG and r['plausibility'] == 0]
by = collections.defaultdict(list)
for r in pool: by[r['_batch']].append(r)
tot = len(pool)
quota = {b: K * len(v) / tot for b, v in by.items()}
alloc = {b: int(q) for b, q in quota.items()}
rem = K - sum(alloc.values())
for b in sorted(quota, key=lambda b: (-(quota[b] - alloc[b]), b))[:rem]: alloc[b] += 1
rng = random.Random(SEED)
sample = []
for b in sorted(by):
    v = sorted(by[b], key=lambda r: r['mid'])
    sample += rng.sample(v, alloc[b])
print('pool', tot, 'batches', len(by), 'sample', len(sample))
print(collections.Counter(r['status'] for r in sample))
with open(os.path.join(OUT, 'negsample.json'), 'w') as f:
    json.dump({'seed': SEED, 'pool_size': tot, 'alloc': alloc, 'mids': [r['mid'] for r in sample]}, f, indent=1)
