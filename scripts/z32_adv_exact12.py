"""O262: at p ~ 1e12 compare the cheap complete-family count S(2047) with the exact f_II (scripts/bs_adv_count.c),
to see how the adversary's depression of S translates into a depression of f_II.  Input /tmp/z32/adv12.jsonl."""
import json, subprocess, collections, math
g = collections.defaultdict(list)
for l in open('/tmp/z32/adv12.jsonl'):
    r = json.loads(l); out = subprocess.run(['/tmp/z32/bs_adv_count', str(r['p'])], capture_output=True, text=True).stdout.split()
    r['fII'] = int(out[1]); g[r['design']].append(r)
m0S = sum(r['S'] for r in g['C0'])/len(g['C0']); m0f = sum(r['fII'] for r in g['C0'])/len(g['C0'])
for d, R in g.items():
    L = math.log(R[0]['p'])
    print(f"{d}: n={len(R)} S/C0={sum(r["S"] for r in R)/len(R)/m0S:.2f}  fII/C0={sum(r['fII'] for r in R)/len(R)/m0f:.2f} "
          f"min fII/L^3={min(r['fII'] for r in R)/L**3:.4f}  min S={min(r['S'] for r in R)} min fII={min(r['fII'] for r in R)}")
