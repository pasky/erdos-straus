"""R278: pooled ratios + bootstrap SE for review_r278_rss.py outputs. Usage: python review_r278_rss_stats.py out_*.txt"""
import sys, random
random.seed(278)
def load(f): return [tuple(map(float, l.split())) for l in open(f) if l.strip()]
def ratios(D):
    A = sum(d[1] for d in D); W = sum(d[2] for d in D); R = sum(d[3] for d in D); Z = sum(d[4] for d in D)
    return A / W, A / Z, (A / R if R else float('nan'))
data = {f.split('out_')[-1][:-4]: load(f) for f in sys.argv[1:]}
def boot(D, B=2000):
    xs = []
    for _ in range(B):
        S = [random.choice(D) for _ in D]; xs.append(ratios(S))
    return [ (sum((x[i] - sum(y[i] for y in xs) / B) ** 2 for x in xs) / (B - 1)) ** .5 for i in range(3)]
g = data.get('generic')
gr = ratios(g); gse = boot(g)
print(f"{'set':8s} {'#n':>4s} {'W/n':>6s} {'N-/W':>6s} {'N-/M0':>6s} {'N-/MR':>6s} {'se(N-/MR)':>9s} gap0  gapR  share  z(N-/MR vs generic)")
for k, D in data.items():
    r = ratios(D); se = boot(D)
    W = sum(d[2] for d in D) / len(D)
    if k == 'generic' or k == 'sq':
        print(f"{k:8s} {len(D):4d} {W:6.1f} {r[0]:6.3f} {r[1]:6.3f} {r[2]:6.3f} {se[2]:9.4f}"); continue
    g0 = 1 - r[1] / gr[1]; gR = 1 - r[2] / gr[2]
    z = (gr[2] - r[2]) / (se[2] ** 2 + gse[2] ** 2) ** .5
    print(f"{k:8s} {len(D):4d} {W:6.1f} {r[0]:6.3f} {r[1]:6.3f} {r[2]:6.3f} {se[2]:9.4f} {g0:5.2f} {gR:5.2f} {1-gR/g0 if g0 else float('nan'):5.2f} {z:5.1f}")
