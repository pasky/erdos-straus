"""z52b pass1 U05 Z2840 follow-up: configuration-model giant-component prediction (Molloy–Reed / Newman–Strogatz–Watts)
for the degree sequence of F_p vs the observed largest-component fraction, for p≡1(4), p<2500 (sample 60 primes)."""
import numpy as np
from collections import Counter
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
def forest_deg(p):
    V = p + 2; deg = Counter(); edges = 0; par = list(range(V+1))
    def f_(x):
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    for u in range(1, V+1):
        for v in range(u+1, V+1):
            if (p+u+v) % (u*v) == 0:
                deg[u] += 1; deg[v] += 1; par[f_(u)] = f_(v)
    cnt = Counter(f_(x) for x in range(1, V+1))
    return [deg[x] for x in range(1, V+1)], max(cnt.values())/V
def giant_config(deg):
    d = np.array(deg); n = len(d)
    kmax = d.max(); P = np.bincount(d, minlength=kmax+1)/n
    k = np.arange(len(P))
    mean = (k*P).sum()
    if mean == 0: return 0.0
    q = (k*(k-1)*P).sum()/mean if mean > 0 else 0  # excess-degree mean
    if q <= 1: return 0.0
    # generating functions: G0(x)=Σ P_k x^k, G1(x)=Σ k P_k x^{k-1}/mean ; solve u=G1(u) (smallest root), giant = 1-G0(u)
    u = 0.5
    for _ in range(2000):
        u_new = (k*P*np.power(u, np.maximum(k-1,0))).sum()/mean
        if abs(u_new-u) < 1e-12: break
        u = u_new
    return float(1 - (P*np.power(u, k)).sum())
rows = []
for p in [q for q in range(5, 2500) if all(q % d for d in range(2, int(q**.5)+1)) and q % 4 == 1][:60]:
    deg, lc = forest_deg(p)
    g = giant_config(deg)
    rows.append((p, round(g, 3), round(lc, 3)))
pred = np.array([r[1] for r in rows]); obs = np.array([r[2] for r in rows])
log(f"Z2840 configuration-model giant predicted vs observed largest component (60 primes ≡1(4), p<2500): "
    f"predicted median {np.median(pred):.3f} (>0 in {(pred>0).sum()}); observed median {np.median(obs):.3f}")
log("  first 6 (p, predicted giant, observed largest):", rows[:6])
open("data/z52b/pass1/U05/2nd/config_out.txt","w").write("\n".join(out)+"\n")
