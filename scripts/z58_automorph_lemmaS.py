#!/usr/bin/env python3
"""z58 AUTOMORPH: numerical checks of Lemma S (sign lemma) and Theorem A.

Lemma S: if A(T) = sum_m a(p^m) T^m is a proper rational function with poles in {1/g : g in Gamma},
Gamma ∩ -Gamma = ∅, and a(p^{2j}) = 0 for all j >= 0, then a(p^m) = 0 for all m (in particular a(p) = 0).

Checks:
 (1) generic random Satake data (no collisions): the solution space of the T1 equations forces a(p)=0;
 (2) with a twist collision (beta' = -alpha etc.) a(p) != 0 is possible (necessity of the hypothesis);
 (3) actual modular forms: span{tau, tau*chi_-4, sigma_11, sigma_11*chi_-4, sigma_3, sigma_3*chi_-4,
     n*sigma_1 (quasi-modular D E_2 part), r(n)=sum_{d|n} chi_-4(d) (weight 1), n*r(n)}:
     at each prime p < 200 compute the subspace with a(p^{2j}) = 0 (j = 0..J) and the max |a(p)| on it;
     expect 0 for p ≡ 1 (4) (no collision as tau(p) != 0), nonzero allowed for p ≡ 3 (4).
 (4) the local sign counterexample: a(n) = 5 sigma_1(n) - (2n + 3) r(n): a(p^{2j}) <= 0, a(p) > 0 at p ≡ 1 (4),
     but a(q^2) > 0 at q ≡ 3 (4) (so it is not a T1-sign proxy globally).
"""
import sys
from fractions import Fraction
import sympy as sp

def h(m, a, b):
    return sum(a**j * b**(m - j) for j in range(m + 1))

def nullspace_forces_zero(pairs, J=8):
    # rows: j=0..J equations sum_i c_i h_{2j}(pair_i) = 0 ; test functional h_1
    M = sp.Matrix([[h(2*j, a, b) for (a, b) in pairs] for j in range(J + 1)])
    ns = M.nullspace()
    vals = [sum(v[i] * (pairs[i][0] + pairs[i][1]) for i in range(len(pairs))) for v in ns]
    return [sp.nsimplify(sp.simplify(x)) for x in vals]

def check_generic():
    import random
    random.seed(1)
    out = []
    for trial in range(5):
        pairs = [(sp.Rational(random.randint(2, 50), random.randint(1, 7)), sp.Rational(random.randint(2, 50), random.randint(1, 7))) for _ in range(4)]
        out.append(("generic", nullspace_forces_zero(pairs)))
    # collision: (a,b) and (-a,-b)
    a, b = sp.Rational(3), sp.Rational(5)
    out.append(("twist-collision", nullspace_forces_zero([(a, b), (-a, -b), (sp.Rational(7), sp.Rational(2))])))
    # self-collision alpha=-beta (lambda(p)=0) alone
    out.append(("self-collision", nullspace_forces_zero([(a, -a), (sp.Rational(7), sp.Rational(2))])))
    # mixed: shared one value but no sign collision (3-cycle example)
    out.append(("3-cycle", nullspace_forces_zero([(sp.Rational(2), sp.Rational(3)), (sp.Rational(3), sp.Rational(5)), (sp.Rational(5), sp.Rational(2))])))
    return out

# --- actual coefficient functions -------------------------------------------------
def tau_list(N):
    # Ramanujan tau via q-expansion of Delta = q prod (1-q^n)^24
    P = [0] * (N + 1)
    P[0] = 1
    for n in range(1, N + 1):
        for _ in range(24):
            for k in range(N, n - 1, -1):
                P[k] -= P[k - n]
    t = [0] * (N + 2)
    for k in range(N):
        t[k + 1] = P[k]
    return t

def chi4(n):
    return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)

def sigma(k, n):
    return sum(d**k for d in sp.divisors(n))

def rfun(n):
    return sum(chi4(d) for d in sp.divisors(n))

def check_forms(J=12, pmax=40):
    N = max(p**(2*J) for p in sp.primerange(3, pmax)) if False else None
    res = []
    for p in sp.primerange(3, pmax):
        powers = [p**m for m in range(2*J + 1)]
        Tmax = p**(2*J)
        # tau at p^m via Hecke recursion (avoid huge q-expansions)
        tp = tau_small[p]
        tv = [1, tp]
        for m in range(2, 2*J + 1):
            tv.append(tp * tv[-1] - p**11 * tv[-2])
        funcs = []
        names = []
        def add(name, vals):
            names.append(name); funcs.append(vals)
        add("tau", tv)
        add("tau*chi", [tv[m] * chi4(p**m) for m in range(2*J + 1)])
        for k in (11, 3):
            s = [sigma(k, p**m) for m in range(2*J + 1)]
            add(f"s{k}", s)
            add(f"s{k}*chi", [s[m] * chi4(p**m) for m in range(2*J + 1)])
        s1 = [sigma(1, p**m) for m in range(2*J + 1)]
        add("n*s1", [p**m * s1[m] for m in range(2*J + 1)])
        rv = [rfun(p**m) for m in range(2*J + 1)]
        add("r", rv)
        add("n*r", [p**m * rv[m] for m in range(2*J + 1)])
        M = sp.Matrix([[f[2*j] for f in funcs] for j in range(J + 1)])
        ns = M.nullspace()
        vals = [abs(sum(v[i] * funcs[i][1] for i in range(len(funcs)))) for v in ns]
        mx = max(vals) if vals else 0
        res.append((p, p % 4, len(ns), 'a(p)=0 forced' if mx == 0 else 'a(p)!=0 possible: |a(p)|/p^11 ~ %.3g' % float(mx / sp.Integer(p)**11)))
    return res

def check_local_sign(pmax=60):
    rows = []
    for p in sp.primerange(3, pmax):
        a = lambda n: 5*sigma(1, n) - (2*n + 3)*rfun(n)
        rows.append((p, p % 4, a(p), [a(p**(2*j)) for j in range(4)]))
    return rows

if __name__ == "__main__":
    for name, v in check_generic():
        print(name, "a(p) values on T1-nullspace basis:", v)
    tl = tau_list(60)
    tau_small = {p: tl[p] for p in sp.primerange(3, 60)}
    print("modular-forms check (p, p mod 4, dim T1-nullspace, max|a(p)| over basis):")
    for row in check_forms():
        print(row)
    print("local sign counterexample a(n)=5 sigma_1(n)-(2n+3) r(n): (p, p mod 4, a(p), [a(p^0),a(p^2),a(p^4),a(p^6)])")
    for row in check_local_sign():
        print(row)
