import json, sys, os
from z52d_rank_O_common import load_master, OUT
m = load_master(); F = [json.loads(l) for l in open(os.path.join(OUT, 'F.jsonl'))]
i, j = int(sys.argv[1]), int(sys.argv[2])
for k, r in enumerate(F[i:j], i):
    print(f"#{k} {r['mid']} [{r['_batch']}] {r['status']} p{r['plausibility']} n{r['novelty']} {r['_why']} :: {m[r['mid']]['title'][:110]}")
    print(' Y:', str(r['yield'])[:200]); print(' MT:', r['missing_theorem'][:700])
    if not str(r['new_ingredient']).lower().startswith('none'): print(' ING:', r['new_ingredient'][:300])
    print(' BAR:', str(r['barrier'])[:250]); print(' NEXT:', str(r['next'])[:250])
