#!/usr/bin/env python3
"""R29: are the model's 'true' Type-I data consistent with what BV gives?
For actual hard primes (pre-sifted to x^eps), |A_d| ≈ X g(d) V with no dependence on
the parity of omega(d) (Thm P1: the ± classes have the same data) and only weak
dependence on log d.  In the discrete one-window model, compute the normalised
correlation r(S) = rho_mu(S) / (prod_k w_k^{S_k}/S_k!) / rho_mu(empty) for every
visible S (theta=1/2) and report its spread by |S| parity and size.
Also the same for the 'odd' law (configs with |C| odd), i.e. the (p/3)=-1 analogue.
Usage: review_w2_rhocheck.py EPS K THETA
"""
import sys, itertools
from math import comb, factorial, log, exp, sqrt
eps, K, th = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
E = [exp(log(eps) * (1 - i / K)) for i in range(K + 1)]
g = [sqrt(E[i] * E[i + 1]) for i in range(K)]
w = [0.5 * log(E[i + 1] / E[i]) for i in range(K)]
def vecs(cap, strict):
    return [m for m in itertools.product(*[range(int(cap / x) + 1) for x in g])
            if ((sum(a * b for a, b in zip(m, g)) < cap) if strict else (sum(a * b for a, b in zip(m, g)) <= cap))]
ALL = vecs(1, True)
def mu(m):
    s = sum(a * b for a, b in zip(m, g)); v = max(1 - s, 1e-3) ** -0.5
    for k in range(K): v *= w[k] ** m[k] / factorial(m[k])
    return v
def emb(s, c):
    r = 1
    for a, b in zip(s, c):
        if a > b: return 0
        r *= comb(b, a)
    return r
for name, par in (("even (p/3)=+1", 0), ("odd (p/3)=-1", 1)):
    W = [m for m in ALL if sum(m) % 2 == par]
    rho = lambda S: sum(mu(c) * emb(S, c) for c in W)
    r0 = rho(tuple([0] * K))
    rows = []
    for S in vecs(th, False):
        if not any(S): continue
        base = 1.0
        for k in range(K): base *= w[k] ** S[k] / factorial(S[k])
        rows.append((sum(S) % 2, sum(a * b for a, b in zip(S, g)), rho(S) / base / r0))
    for p in (0, 1):
        v = [x for q, s, x in rows if q == p]
        print(f"{name}: |S| {'even' if p == 0 else 'odd '}: r(S) in [{min(v):.3f}, {max(v):.3f}] ({len(v)} S)")
    for (q, s, x) in sorted(rows, key=lambda t: t[1])[:: max(1, len(rows) // 6)]:
        print(f"    |S| parity {q}, size {s:.3f}: r = {x:.3f}")
