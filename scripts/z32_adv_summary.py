"""O262: summary of logs/z32_adv.jsonl: per (size, design) n, mean S(2047), min S, ratio to the C0 mean, W range,
S127 share; and the record (smallest S / C0-mean)."""
import json, math, collections
rows = [json.loads(l) for l in open('logs/z32_adv.jsonl')]
for r in rows: r['size'] = round(math.log10(r['p']))
g = collections.defaultdict(list)
for r in rows: g[(min(r['size'], 25) if r['size'] >= 24 else r['size'], r['design'])].append(r)
sizes = sorted({k[0] for k in g}); best = None
for s in sizes:
    c0 = [r['S'] for r in g.get((s, 'C0'), [])] or [float('nan')]; m0 = sum(c0)/len(c0)
    for d in ('C0', 'D1', 'D2', 'D3', 'D4', 'D4big'):
        R = g.get((s, d))
        if not R: continue
        S = [r['S'] for r in R]; W = [r['W'] for r in R]; sh = sum(r['S127'] for r in R)/sum(S)
        L = math.log(R[0]['p'])
        print(f"~1e{s} {d:6s} n={len(R)} meanS={sum(S)/len(S):7.0f} minS={min(S):5d} mean/C0={sum(S)/len(S)/m0:.2f} "
              f"min/C0={min(S)/m0:.2f} W={min(W)}..{max(W)} share(e<=127)={sh:.2f} minS/L^3={min(S)/L**3:.4f}")
        for r in R:
            if best is None or r['S']/m0 < best[0]: best = (r['S']/m0, r)
b = best[1]; print('RECORD (smallest S/C0-mean):', round(best[0], 3), b['design'], b['p'], 'S =', b['S'], 'W =', b['W'], 'sol =', b['sol'][:2])
