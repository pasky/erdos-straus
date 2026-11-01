"""Z52D_HYPERBOLA.md Thm 3 check (EVIDENCE for a PROVED statement): the conductor <= D part of the exact additive expansion
N = sum_{(u,B)} (4uB)^{-1} sum_{d | 4uB} c_d(p+u+B) of the balanced block (sharp cutoffs, U = 1000) is the same for all primes,
= J * sum_{d<=D, d odd} mu(d)^2/d^2 up to the O(D/U) boundary error of sharp cutoffs; and the high-conductor remainder carries
all of N - M0.  Usage: uv run --with numpy --with sympy python scripts/z52d_hyperbola_lowcond.py [smooth]"""
import numpy as np, json
from sympy import mobius, primerange, nextprime
U = 1000; D = 40
u = np.arange(U + 1, 2*U + 1, dtype=np.int64)
UU, BB = np.meshgrid(u, u, indexing='ij'); Q4 = 4*UU*BB
import sys
SMOOTH = len(sys.argv) > 1 and sys.argv[1] == 'smooth'
def bump(x):  # C_c^infty((1,2)) bump
    y = np.zeros_like(x, dtype=float); m = (x > 1) & (x < 2); y[m] = np.exp(4.0 - 1.0/((x[m] - 1)*(2 - x[m]))); return y  # max 1 at x = 3/2
W = (bump(UU/U)*bump(BB/U) if SMOOTH else 1.0)/Q4


def ramanujan(d, n):
    """c_d(n) for an integer array n: sum_{f | gcd(n,d)} f mu(d/f)."""
    out = np.zeros(n.shape)
    for f in range(1, d + 1):
        if d % f == 0:
            mu = int(mobius(d//f))
            if mu: out += f*mu*(n % f == 0)
    return out


Jsharp = float(W.sum())          # sum of 1/(4uB) over the block = J for sharp cutoffs (up to O(1/U))
pred = Jsharp*sum(int(mobius(d))**2/d**2 for d in range(1, D + 1, 2))
res = {'U': U, 'D': D, 'J_sharp': Jsharp, 'pred_JxSum_odd_squarefree': pred, 'primes': []}
ps = [nextprime(10**12 + k*7919) for k in range(12)]
for p in ps:
    n = p + UU + BB; L = 0.0
    for d in range(1, D + 1):
        m = (Q4 % d == 0)
        if m.any(): L += float((W[m]*ramanujan(d, n[m])).sum())
    N = float((W*Q4*((n % Q4) == 0)).sum())  # weighted count (= plain count if sharp)
    res['primes'].append(dict(p=int(p), p_mod_840=int(p % 840), L_D=round(L, 9), N=N))
    print(p, p % 840, round(L, 9), N)
Ls = [r['L_D'] for r in res['primes']]
res['L_D_spread'] = [min(Ls), max(Ls)]
print('pred', pred, 'spread', min(Ls), max(Ls))
res['smooth'] = SMOOTH
json.dump(res, open('data/z52d/hyperbola/lowcond_check%s.json' % ('_smooth' if SMOOTH else ''), 'w'), indent=1)
