"""R266 from-scratch checks for O253 Thm 1.3(b) model, Thm 1.3(a)/(d) bounds on synthetic trees,
and Prop 3.4(a),(c) (valuation patterns of W(p^2); m = 3 killed by reciprocity).
"""
import sys, math, random
from sympy import isprime, primerange, divisors
from review_r266_ek import sols


def model_13b(b, r, A, delta, p0, levels):
    """Build the Thm 1.3(b) configuration; check out-degree = b, children in (p, A p], in-degree <= r."""
    assert b / r < A / (1 + delta) ** 2
    X = [p0]; m = [1]
    for k in range(levels):
        X.append(A * X[-1] / (1 + delta)); m.append(max(b, -(-b * m[-1] // r)))
    lev = [[p0]]
    for k in range(1, levels + 1):
        lo, hi = X[k], (1 + delta) * X[k]
        t = int(lo) + (1 - int(lo)) % 840
        P = []
        while len(P) < m[k] and t <= hi:
            if isprime(t): P.append(t)
            t += 840
        assert len(P) == m[k], ('not enough primes', k)
        lev.append(P)
    indeg = {}
    bad = 0
    for k in range(levels):
        slots = [(par, s) for par in lev[k] for s in range(b)]
        ch = lev[k + 1]
        kids = {}
        for i, (par, s) in enumerate(slots):
            c = ch[i % len(ch)]
            kids.setdefault(par, set()).add(c)
            indeg[c] = indeg.get(c, 0) + 1
        for par, cs in kids.items():
            if len(cs) != b or not all(par < c <= A * par for c in cs):
                bad += 1
    print(f'model b={b} r={r} A={A} delta={delta}: level sizes {m}; parents violating out-degree/window: {bad}; '
          f'max in-degree {max(indeg.values())} (<= r={r}); all primes = 1 mod 840: '
          f'{all(q % 840 == 1 for L in lev[1:] for q in L)}')


def patterns(P):
    occ = {}
    allmixed = True
    for p in primerange(3, P):
        n = p * p
        pats = set()
        for t in sols(4, n):
            v = []
            for x in t:
                k = 0
                while x % p == 0: x //= p; k += 1
                v.append(min(k, 2))   # cap at 2 ("\u2265 2")
            pats.add(tuple(sorted(v, reverse=True)))
        occ[p] = pats
        if (2, 1, 0) not in pats: allmixed = False
    union = set().union(*occ.values())
    print(f'Prop 3.4(a): patterns (capped at 2) occurring for 3<=p<{P}: {sorted(union)}; '
          f'mixed (2,1,0) present for every p: {allmixed}')


def m3(P):
    bad = 0
    for p in primerange(5, P):
        if p % 3 != 1: continue
        z = (p * p + 3) // 4
        D = divisors(z)
        if any((A + p * B) % 3 == 0 for A in D for B in D): bad += 1
    print(f'Prop 3.4(c): primes p=1 (3), p<{P}, with an m=3 mixed solution: {bad}')


if __name__ == '__main__':
    model_13b(3, 1, 4, 0.05, 10**6, 7)
    model_13b(5, 2, 3, 0.04, 10**6, 8)
    model_13b(2, 3, 2, 0.1, 10**6, 10)   # b <= r case
    patterns(80)
    m3(3000)
