"""Task B: build candidate set F (rank_O). Writes F.jsonl and prints counts per criterion."""
import json, os, collections
from z52d_rank_O_common import load_rows, OUT, is_none_ing
rows = load_rows()
# Overturned negatives: Task A random-sample rows with verdict_ok == false, plus the Task A targeted hunt
# (closure/induction rows citing B1 or 'thin polynomial image', which is wrong for strong induction from all
# smaller n; the valid bar, privacy, is an Assessment, so these are open at plausibility 0–1, not known-false).
NA = [json.loads(l) for l in open(os.path.join(OUT, 'negaudit.jsonl'))]
TARGETED_HUNT = {'Z3016', 'Z3187', 'Z3115', 'Z0223'}
OVERTURNED = {r['mid'] for r in NA if r['verdict_ok'] is False} | TARGETED_HUNT
def ynone(r): return str(r['yield']).strip().lower().startswith('none')
c1 = lambda r: r['plausibility'] >= 2 and r['novelty'] >= 1 and not ynone(r)
c2 = lambda r: str(r['yield']).strip().startswith('ES') and r['status'] in {'open-plausible', 'unclear', 'known-true'} and r['plausibility'] >= 1
c3 = lambda r: not is_none_ing(r['new_ingredient'])
c4 = lambda r: r['mid'] in OVERTURNED
F = []; cnt = collections.Counter()
for r in rows:
    why = [k for k, f in (('c1_p2n1', c1), ('c2_ESopen', c2), ('c3_ingredient', c3), ('c4_overturned', c4)) if f(r)]
    for k in why: cnt[k] += 1
    if why:
        r = dict(r); r['_why'] = why; F.append(r)
print('rows', len(rows), 'F', len(F), dict(cnt))
print('status', collections.Counter(r['status'] for r in F))
with open(os.path.join(OUT, 'F.jsonl'), 'w') as f:
    for r in F: f.write(json.dumps(r, ensure_ascii=False) + '\n')
