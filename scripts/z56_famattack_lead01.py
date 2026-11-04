# Push on the pre-registered F1 lead: negative within-stratum correlation of u-windows 0 and 1.
# Mechanism test ("privacy competition"): a prime l > |u - u'| divides at most one of p+u, p+u'.
# S0 = #{(u, l): u in window 0, l | p+u, l in (L1, Z]},  S1 = same for window 1, with L1 = top of window 1.
# Report corr(S0,S1), corr(W0,S0), corr(W1,S1), corr(W1,S0), and the partial correlation of W0,W1 given S0,S1 (+ mod 840).
import sys, numpy as np
sys.path.insert(0, 'scripts')
from z56_famattack_assoc import load, within_center
from sympy import primerange
fn = sys.argv[1]; Z = int(sys.argv[2]) if len(sys.argv) > 2 else 10000
p, R, g = load(fn); W = g.sum(2).astype(float); N = len(p)
lp = np.log(p.astype(float))
# window bounds per prime: u in [p^{k/10}, p^{(k+1)/10})
u0max = np.floor(np.exp(0.1 * lp)).astype(np.int64)   # window 0: u <= u0max (u < p^.1)
u1max = np.floor(np.exp(0.2 * lp)).astype(np.int64)
Ltop = int(u1max.max()) + 1
S0 = np.zeros(N); S1 = np.zeros(N); Sm0 = np.zeros(N); Sm1 = np.zeros(N)
for l in primerange(Ltop + 1, Z + 1):
    r = (-p) % l   # the unique u mod l with l | p+u; u = r (if r>=1) is the only candidate below l
    in0 = (r >= 1) & (r <= u0max); in1 = (r > u0max) & (r <= u1max)
    S0 += in0; S1 += in1
    Sm0 += in0 * np.log(l); Sm1 += in1 * np.log(l)
strata = p % 840
def pc(a, b): return np.corrcoef(a, b)[0, 1]
X = np.column_stack([W[:, 0], W[:, 1], S0, S1, Sm0, Sm1])
Xc = within_center(X, strata)
print(f"{fn}: N={N}, medium primes in ({Ltop}, {Z}]; mean S0={S0.mean():.3f} S1={S1.mean():.3f}")
names = ["W0", "W1", "S0", "S1", "Sm0", "Sm1"]
C = np.corrcoef(Xc.T)
for i in range(6):
    print("  " + names[i].ljust(4) + " ".join(f"{C[i,j]:+.4f}" for j in range(6)))
# partial correlation of W0, W1 given S0, S1, Sm0, Sm1 (within strata)
A = np.column_stack([np.ones(N), Xc[:, 2:]])
res = Xc[:, :2] - A @ np.linalg.lstsq(A, Xc[:, :2], rcond=None)[0]
r01 = pc(res[:, 0], res[:, 1])
print(f"  within-840 corr(W0,W1) = {C[0,1]:+.4f} (z={C[0,1]*np.sqrt(N):+.1f});  partial given S0,S1,Sm0,Sm1 = {r01:+.4f} (z={r01*np.sqrt(N):+.1f})")
