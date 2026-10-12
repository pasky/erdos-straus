"""O154(b): search for NEW hardness drivers of f_II(p) beyond the known ones.
Sample primes p = 1 (mod 24) in [5e7, 1e8] from /tmp/fII_1e8.bin (READ-ONLY, exact f_II from bs_prob_fII.c).
Response y = log(f_II / L^3). Baseline regressors (known drivers): cell mean of y mod 840 and mod 120120,
log tau(p-1), log sum_{e<=16} tau((p+e)/4). Candidates are tested by partial correlation with the baseline residual.
Run: PYTHONPATH=scripts uv run python scripts/bs_adv_drivers.py [nsample]"""
import sys, math, random
import numpy as np
from sympy import factorint, primerange

ns = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
A = np.fromfile('/tmp/fII_1e8.bin', dtype=np.uint32).reshape(-1, 3)
p_all = A[:, 0].astype(np.int64); f_all = A[:, 1].astype(float)
sel = (p_all >= 5 * 10**7) & (p_all % 24 == 1)
P, Fv = p_all[sel], f_all[sel]
L = np.log(P.astype(float)); yall = np.log(Fv / L**3)
# cell means mod Q over the whole window (leave-in; cells are large)
def cellmean(Q):
    c = P % Q; u, inv = np.unique(c, return_inverse=True)
    return (np.bincount(inv, weights=yall) / np.bincount(inv))[inv]
cm840, cm120120 = cellmean(840), cellmean(120120)
random.seed(1540)
idx = np.array(sorted(random.sample(range(len(P)), ns)))
p = [int(t) for t in P[idx]]; y = yall[idx]; c840 = cm840[idx]; c120 = cm120120[idx]

def tau(n):
    return math.prod(v + 1 for v in factorint(int(n)).values())

SP = list(primerange(3, 20000))
def chi_lsum(n, D):
    """log of truncated Euler product of L(1, chi_D), chi_D(q) = (D/q) Kronecker, primes 3..2e4 (q=2 handled)."""
    s = 0.0
    for q in SP:
        k = pow(D % q, (q - 1) // 2, q)
        if k == 1: s -= math.log(1 - 1 / q)
        elif k == q - 1: s -= math.log(1 + 1 / q)
    return s

def leastnr(n):
    for q in SP:
        if pow(n % q, (q - 1) // 2, q) == q - 1: return q
    return 0

def deadmass(n):
    """sum over f | p-1, f = 3 mod 4 of tau(((f+1)/4)^2)/f: expected Type II mass on dead witness moduli."""
    fa = factorint(int(n) - 1); ds = [1]
    for q, v in fa.items(): ds = [d * q**t for d in ds for t in range(v + 1)]
    s = 0.0
    for f in ds:
        if f % 4 == 3 and f < 10**6:
            A_ = (f + 1) // 4; s += math.prod(2 * v + 1 for v in factorint(A_).values()) / f
    return s

feat = {}
feat['log tau(p-1)'] = [math.log(tau(x - 1)) for x in p]
feat['log S16'] = [math.log(sum(tau((x + e) // 4) for e in (3, 7, 11, 15))) for x in p]
feat['log tau(p+1)'] = [math.log(tau(x + 1)) for x in p]
feat['log tau(2p+1)'] = [math.log(tau(2 * x + 1)) for x in p]
feat['log tau(p+2)'] = [math.log(tau(x + 2)) for x in p]
feat['log tau((3p+1)/4)'] = [math.log(tau((3 * x + 1) // 4)) for x in p]
feat['log tau(p-1) smooth<=100 part'] = [math.log(math.prod(q**v for q, v in factorint(int(x) - 1).items() if q <= 100)) for x in p]
feat['deadmass(p-1)'] = [deadmass(x) for x in p]
feat['v2(p-1)'] = [((int(x) - 1) & -(int(x) - 1)).bit_length() - 1 for x in p]
feat['logL(1,chi_-4p) trunc'] = [chi_lsum(x, -4 * int(x)) for x in p]
feat['logL(1,chi_p) trunc'] = [chi_lsum(x, int(x)) for x in p]
feat['log n_p'] = [math.log(leastnr(x)) for x in p]
import subprocess
g = subprocess.run(['/tmp/bs_adv_global'], input='\n'.join(map(str, p)), capture_output=True, text=True).stdout.split('\n')
g = [list(map(float, l.split())) for l in g if l.strip()]
assert [int(r[0]) for r in g] == p
feat['logL(1,chi_-4p) EXACT (h)'] = [math.log(math.pi * r[1] / (2 * math.sqrt(r[0]))) for r in g]
feat['  tail: exact - trunc'] = [a - b for a, b in zip(feat['logL(1,chi_-4p) EXACT (h)'], feat['logL(1,chi_-4p) trunc'])]
feat['log(CF period sqrt p / sqrt p)'] = [math.log(r[2] / math.sqrt(r[0])) for r in g]
feat['log(R_unit Z[sqrt p] / sqrt p)'] = [math.log(r[3] / math.sqrt(r[0])) for r in g]

X0 = np.column_stack([np.ones(ns), c120, feat['log tau(p-1)'], feat['log S16']])
beta, *_ = np.linalg.lstsq(X0, y, rcond=None); res = y - X0 @ beta
X1 = np.column_stack([np.ones(ns), c120])
r1 = y - X1 @ np.linalg.lstsq(X1, y, rcond=None)[0]
print(f"n={ns}  Var(y)={y.var():.4f}  R2(cell120120)={1-r1.var()/y.var():.3f}  R2(baseline)={1-res.var()/y.var():.3f}  beta={np.round(beta,3)}")
print("feature | corr with y | corr with cell residual | partial corr with baseline residual | R2 gain if added")
for k, v in feat.items():
    v = np.array(v, float)
    cy = np.corrcoef(v, y)[0, 1]; c1 = np.corrcoef(v, r1)[0, 1]
    vr = v - X0 @ np.linalg.lstsq(X0, v, rcond=None)[0]
    cp = np.corrcoef(vr, res)[0, 1] if vr.std() > 1e-12 else float('nan')
    X2 = np.column_stack([X0, v]); r2 = y - X2 @ np.linalg.lstsq(X2, y, rcond=None)[0]
    print(f"{k:32s} {cy:+.3f} {c1:+.3f} {cp:+.3f} {res.var()/y.var()-r2.var()/y.var():.4f}")
np.save('/tmp/bs_adv_drivers_feat.npy', np.column_stack([np.array(p, float), y, c120] + [np.array(v, float) for v in feat.values()]))
# second stage: baseline + all local/lottery-type features; do the GLOBAL invariants add anything?
loc = ['log tau(p-1)', 'log S16', 'log tau(2p+1)', 'log tau(p+2)', 'log tau(p+1)', 'v2(p-1)',
       'log tau(p-1) smooth<=100 part', 'logL(1,chi_p) trunc', 'logL(1,chi_-4p) trunc', 'log n_p']
XB = np.column_stack([np.ones(ns), c120] + [np.array(feat[k], float) for k in loc])
rb = y - XB @ np.linalg.lstsq(XB, y, rcond=None)[0]
print(f"stage 2 baseline (cells + {len(loc)} local/shift features): R2={1-rb.var()/y.var():.3f}")
for k in ['  tail: exact - trunc', 'log(CF period sqrt p / sqrt p)', 'log(R_unit Z[sqrt p] / sqrt p)']:
    v = np.array(feat[k], float); vr = v - XB @ np.linalg.lstsq(XB, v, rcond=None)[0]
    print(f"  global {k:32s} partial corr {np.corrcoef(vr, rb)[0,1]:+.3f}  (null s.e. ~{1/math.sqrt(ns):.3f})")
# stage 3: is the rest explained by MORE shifted-divisor (lottery) data?  compare with the compound-Poisson floor
ex = [np.log([tau((x + e) // 4) for x in p]) for e in range(3, 64, 4)]
ex += [np.log([tau(c * x + a) for x in p]) for a in range(1, 5) for c in range(1, 5) if math.gcd(a, c) == 1]
X3 = np.column_stack([XB] + ex)
r3 = y - X3 @ np.linalg.lstsq(X3, y, rcond=None)[0]
fval = np.exp(y) * np.log(np.array(p, float))**3
floor = np.mean(3.06 / fval)   # Var(log f) of a compound Poisson with kappa = 3.06 (weight-2 units, O142 3.2)
print(f"stage 3 (+{len(ex)} shifted tau features): R2={1-r3.var()/y.var():.3f}; residual var {r3.var():.4f}; "
      f"compound-Poisson floor ~{floor:.4f} (= {floor/y.var():.2f} of Var y)")
for k in ['  tail: exact - trunc', 'log(CF period sqrt p / sqrt p)', 'log(R_unit Z[sqrt p] / sqrt p)']:
    v = np.array(feat[k], float); vr = v - X3 @ np.linalg.lstsq(X3, v, rcond=None)[0]
    print(f"  global {k:32s} partial corr {np.corrcoef(vr, r3)[0,1]:+.3f}")
