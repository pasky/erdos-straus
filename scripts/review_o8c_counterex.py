"""R30c from-scratch check of POINTWISE_OMEGA8 §6.4 counterexample.

f = "two of the N=floor(sqrt q) coordinates (uniform on [q]) coincide".
(1) masses: per-coordinate (N-1)/q, total C(N,2)/q.
(2) exact q-ary decision-tree depth of f_rho when the N-s fixed values are
    distinct and s coordinates are free: claim DT_q(f_rho) = s.
(3) exact Efron-Stein level weights W^{=r}[f_rho] on [q]^s, and Pr[f_rho=1],
    to test the doc's "nearly constant: Pr[f_rho=1] <~ Ns/q" and consistency
    with ESW.
(4) Pr over rho (p-random) of DT_q(f_rho) >= s0, by exact binomial formula
    times Pr[fixed values distinct], against (C'(pk+max w))^{s0}.
"""
import itertools, math, sys
from functools import lru_cache
import numpy as np

def dt_q(q, fixed, s):
    fixed = frozenset(fixed)
    @lru_cache(maxsize=None)
    def rec(assign):  # assign: tuple of values or -1 for free
        vals = [v for v in assign if v >= 0]
        coll = len(set(vals)) < len(vals) or any(v in fixed for v in vals)
        if coll: return 0                     # f=1 determined
        free = [i for i, v in enumerate(assign) if v < 0]
        if not free: return 0                 # f=0 determined
        # is f constant on completions? it is 0-able iff enough fresh values, 1-able always
        best = len(free)
        for i in free:
            worst = 0
            for c in range(q):
                a = list(assign); a[i] = c
                worst = max(worst, 1 + rec(tuple(a)))
                if worst >= best: break
            best = min(best, worst)
        return best
    return rec(tuple([-1] * s))

def es_levels(q, fixed, s):
    """exact ES level weights of f on [q]^s (f=1 iff collision among free or with fixed)."""
    grids = np.meshgrid(*[np.arange(q)] * s, indexing='ij')
    f = np.zeros([q] * s)
    for i in range(s):
        f = np.maximum(f, np.isin(grids[i], list(fixed)).astype(float))
        for j in range(i):
            f = np.maximum(f, (grids[i] == grids[j]).astype(float))
    # ||E[f|X_W]||^2 for all W, Mobius-invert
    cond = {}
    for W in itertools.product([0, 1], repeat=s):
        axes = tuple(i for i in range(s) if not W[i])
        g = f.mean(axis=axes) if axes else f
        cond[W] = float((g ** 2).mean())
    lev = [0.0] * (s + 1)
    for U in cond:
        val = 0.0
        for W in cond:
            if all(W[i] <= U[i] for i in range(s)):
                val += (-1) ** (sum(U) - sum(W)) * cond[W]
        lev[sum(U)] += val
    return f.mean(), lev

def main():
    print("(1)+(2) exact DT_q with distinct fixed values")
    for q in (9, 16, 25):
        N = int(math.isqrt(q))
        print(f" q={q} N={N}: per-coord mass {(N-1)/q:.3f} <= q^-1/2={q**-0.5:.3f}; total {N*(N-1)/2/q:.3f}")
        for s in range(1, N + 1):
            if q == 25 and s > 4: continue
            fixed = list(range(N - s))
            d = dt_q(q, fixed, s)
            print(f"   s={s}: DT_q(f_rho)={d} {'OK' if d == s else 'MISMATCH'}")
    print("(3) exact Efron-Stein level weights of f_rho (fixed values distinct)")
    for q, s in ((49, 2), (49, 3), (49, 4), (100, 3), (144, 3)):
        N = int(math.isqrt(q)); fixed = list(range(N - s))
        P1, lev = es_levels(q, fixed, s)
        print(f" q={q} N={N} s={s}: Pr[f=1]={P1:.4f} (Ns/q={N*s/q:.4f}); W^=r: " + " ".join(f"{x:.2e}" for x in lev))
    print("(4) Pr_rho[DT_q >= s0] lower bound vs hypothetical (C'(pk+max w))^s0, k=2")
    for Cp in (1.0, 5.0):
        p = 1 / (4 * Cp)
        for q in (10**4, 10**6, 10**8):
            N = math.isqrt(q); s0 = max(1, int(p * N / 2))
            # P[Bin(N,p) >= s0]  (normal approx is fine; use exact via scipy-free log sum)
            lp = [math.lgamma(N + 1) - math.lgamma(i + 1) - math.lgamma(N - i + 1) + i * math.log(p) + (N - i) * math.log1p(-p) for i in range(N + 1)]
            tail = sum(math.exp(x) for x in lp[s0:])
            pdist = math.exp(sum(math.log1p(-i / q) for i in range(N)))   # all N values distinct (implies fixed distinct)
            rhs_log10 = s0 * math.log10(Cp * (2 * p + (N - 1) / q))
            print(f" C'={Cp} p={p} q={q}: s0={s0}, Pr>= {tail*pdist:.3f}  vs bound 10^{rhs_log10:.1f}")

if __name__ == "__main__":
    main()
