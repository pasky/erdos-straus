"""O267 §3: analyse z37_rss outputs. For each set: mean of words W, actual slice words N-, chi=-1 share N-/W,
model-R share mR/W, model-0 share m0/W, and the pooled ratios sum N- / sum mR, sum N- / sum m0.
Usage: uv run python scripts/z37_rss_analyse.py /tmp/z37/out_*.txt"""
import sys, math
rows = []
for f in sys.argv[1:]:
    D = [list(map(float, l.split())) for l in open(f) if l.strip()]
    if not D: continue
    W = sum(d[2] for d in D); A = sum(d[1] for d in D); R = sum(d[3] for d in D); Z = sum(d[4] for d in D)
    C = sum(d[5] for d in D)
    # per-n residual (N- - mR)/W, mean and s.e.
    res = [(d[1] - d[3]) / d[2] for d in D if d[2] > 0]
    mu = sum(res) / len(res); se = (sum((x - mu) ** 2 for x in res) / max(1, len(res) - 1) / len(res)) ** .5
    name = f.split('out_')[-1].replace('.txt', '')
    rows.append((name, len(D), W / len(D), A / W, R / W, Z / W, C / W, A / R if R else float('nan'), mu, se))
print(f"{'set':10s} {'#n':>5s} {'W/n':>6s} {'N-/W':>6s} {'mR/W':>6s} {'m0/W':>6s} {'clean/W':>7s} {'N-/mR':>6s} {'resid':>7s} {'se':>6s}")
for r in rows:
    print(f"{r[0]:10s} {r[1]:5d} {r[2]:6.1f} {r[3]:6.3f} {r[4]:6.3f} {r[5]:6.3f} {r[6]:7.3f} {r[7]:6.3f} {r[8]:+7.4f} {r[9]:6.4f}")
