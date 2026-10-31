"""Z0199 pass-1: does smoothness of p − 1 (p ≡ 1 mod q for many small q) depress U(p) = #solutions of 4/p beyond the
quadratic characters (q/p)? (For p ≡ 1 mod 4 and odd q: q | p−1 ⇒ (q/p) = 1.) Primes p ≡ 1 (4), 100 < p ≤ 2·10⁵.
Model: log(U+1) ~ 1, log p, log log p, (q/p) for q < 80, plus 1[q | p−1] for q ∈ {3,5,7,11,13} and 1[8 | p−1], 1[16 | p−1]."""
import numpy as np, json, os
from sympy import isprime, legendre_symbol, primerange
R = os.environ.get('RAW', '/home/pasky/projects/math/erdos-straus-claude/data/z52b/raw/')
F = np.loadtxt('data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
FP = np.vstack([F[[isprime(int(x)) for x in F[:, 0]]][:, :2], np.loadtxt(R + 'pr_20001_200000.txt', dtype=np.int64)[:, :2]])
FP = FP[np.argsort(FP[:, 0])]; FP = FP[np.concatenate([[True], np.diff(FP[:, 0]) > 0])]
S = FP[(FP[:, 0] % 4 == 1) & (FP[:, 0] > 100)]; P = S[:, 0]; U = S[:, 1]; lp = np.log(P.astype(float))
qs = list(primerange(2, 80))
Xc = np.array([[int(legendre_symbol(q, int(p))) for q in qs] for p in P], float)
div = [3, 5, 7, 11, 13, 8, 16]
Xd = np.array([[1.0 if (p - 1) % d == 0 else 0.0 for d in div] for p in P])
y = np.log(U + 1.0)
X0 = np.hstack([np.vstack([np.ones_like(lp), lp, np.log(lp)]).T, Xc])
X1 = np.hstack([X0, Xd])
def fit(X):
    b = np.linalg.lstsq(X, y, rcond=None)[0]; r = y - X @ b; s2 = r @ r/(len(y) - X.shape[1])
    return b, np.sqrt(np.diag(np.linalg.inv(X.T @ X))*s2), r @ r
b0, se0, rss0 = fit(X0); b1, se1, rss1 = fit(X1)
k = X0.shape[1]
out = dict(n=len(P), rss_chars_only=float(rss0), rss_with_divisibility=float(rss1),
           R2_gain=float((rss0 - rss1)/((y - y.mean()) @ (y - y.mean()))),
           divisibility_coef={str(d): (round(float(b1[k+i]), 4), round(float(se1[k+i]), 4)) for i, d in enumerate(div)})
# raw view: mean residual (chars-only model) vs number of q ∈ {3,5,7,11,13} dividing p−1
r0 = y - X0 @ b0; nd = Xd[:, :5].sum(1)
out['mean_resid_by_ndiv'] = {int(j): (round(float(r0[nd == j].mean()), 4), int((nd == j).sum())) for j in range(6) if (nd == j).any()}
# smooth part of p−1 over {2,3,5,7}
def sm(n):
    m = 1
    for q in (2, 3, 5, 7):
        while n % q == 0: n //= q; m *= q
    return m
smp = np.array([sm(int(p) - 1) for p in P]); ratio = np.log(smp)/lp
out['spearman_resid_vs_log_smoothpart_ratio'] = float(np.corrcoef(np.argsort(np.argsort(ratio)), np.argsort(np.argsort(r0)))[0, 1])
print(json.dumps(out, indent=1)); json.dump(out, open('data/z52b/pass1/H00/pm1smooth.json', 'w'), indent=1)
# Part 2: does adding 1[q | p−1] (q = 5..47) remove the q mod 3 dichotomy of the character weights q·β_q (fingerprint item 152)?
qd = [q for q in qs if 5 <= q <= 47]
Xe = np.array([[1.0 if (p - 1) % q == 0 else 0.0 for q in qd] for p in P])
X2 = np.hstack([X0, Xe]); b2, se2, rss2 = fit(X2)
tab = {q: (round(float(q*b0[3+i]), 3), round(float(q*b2[3+i]), 3)) for i, q in enumerate(qs) if 5 <= q <= 47}
tab1 = {q: (round(float(b2[k+i]), 4), round(float(se2[k+i]), 4)) for i, q in enumerate(qd)}
print('q  q%3  q*beta(chars only)  q*beta(+1[q|p-1])   coef 1[q|p-1] ± se')
for q in qd: print(q, q % 3, tab[q], tab1[q])
out2 = dict(qbeta_before_after=tab, class_of_one_coef=tab1, R2_gain_all=float((rss0 - rss2)/((y - y.mean()) @ (y - y.mean()))))
json.dump(out2, open('data/z52b/pass1/H00/pm1smooth_part2.json', 'w'), indent=1)
# Part 3: within the square coset mod q, is the class of one harder? mean log(U+1) residual (chars-only model) by p mod q.
print('q: mean residual by square residue class r (count)')
part3 = {}
for q in (5, 7, 11, 13, 840):
    rr = {}
    for r in sorted(set((P % q).tolist())):
        sel = (P % q) == r
        if q == 840 or pow(int(r), (q-1)//2, q) == 1:
            if q == 840:
                import math
                if not all(pow(int(r) % m, (m-1)//2, m) == 1 for m in (3, 5, 7)) or r % 8 != 1: continue
            rr[int(r)] = (round(float(r0[sel].mean()), 4), int(sel.sum()))
    part3[q] = rr; print(q, rr)
json.dump(part3, open('data/z52b/pass1/H00/pm1smooth_part3.json', 'w'), indent=1)
