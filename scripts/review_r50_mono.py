"""R50 from-scratch check of Example 6.3 (adding an event can increase G_F).
Uniform measure on [q]^n, constant weight lambda with lambda^n = 2; point events.
G_F = sum_d lambda^d * W_d with W_d rational; compared exactly via sympy.
"""
import itertools
from fractions import Fraction as Fr
import sympy as sp


def levels(q, n, F):
    """W_d = sum_{|U|=d} ||F^{=U}||^2 under uniform measure, via ||L_V F||^2 and Mobius."""
    pts = list(itertools.product(range(q), repeat=n))
    LV = {}
    for V in itertools.product((0, 1), repeat=n):
        # L_V F = prod_{v in V}(I - E_v) F ; compute by successive operators
        f = dict(F)
        for v in range(n):
            if V[v]:
                avg = {}
                for x in pts:
                    key = x[:v] + x[v + 1:]
                    avg[key] = avg.get(key, 0) + Fr(f[x], q)
                f = {x: f[x] - avg[x[:v] + x[v + 1:]] for x in pts}
        LV[V] = sum(Fr(f[x] ** 2) for x in pts) / q ** n
    # ||F^{=U}||^2 = sum_{V >= U} (-1)^{|V|-|U|} ||L_V F||^2
    W = [Fr(0)] * (n + 1)
    for U in LV:
        e = sum((-1) ** (sum(V) - sum(U)) * LV[V] for V in LV if all(V[i] >= U[i] for i in range(n)))
        W[sum(U)] += e
    return W


def G(q, n, events):
    pts = list(itertools.product(range(q), repeat=n))
    F = {x: int(x not in events) for x in pts}
    W = levels(q, n, F)
    lam = sp.root(2, n)
    return sp.nsimplify(sum(sp.Rational(w.numerator, w.denominator) * lam ** d for d, w in enumerate(W)))


if __name__ == "__main__":
    E = {(a, b) for a in range(1, 8) for b in range(1, 8)}
    g0, g1 = G(8, 2, E), G(8, 2, E | {(0, 0)})
    print("[8]^2:", g0, "=", sp.N(g0, 8), "; with A:", g1, "=", sp.N(g1, 8), "; increase:", sp.N(g1 - g0) > 0)
    E3 = {x for x in itertools.product(range(5), repeat=3) if sum(1 for c in x if c) in (2,)}
    g0 = G(5, 3, E3)
    print("[5]^3 base (even #nonzero >=2, i.e. exactly 2):", sp.N(g0, 8))
    for A in [(0, 0, 0), (1, 0, 0), (1, 1, 1), (1, 2, 3)]:
        g1 = G(5, 3, E3 | {A})
        print("   add", A, ":", sp.N(g1, 8), "increase" if sp.N(g1 - g0, 30) > 0 else "no increase")
