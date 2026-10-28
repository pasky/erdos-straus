#!/usr/bin/env python3
"""z49 forestinv — word toolkit for n ≡ 1 (mod 4).

A word of n is (t,u,v), all ≥ 1, with n = t u v − u − v.  Numerators A = tu−1 = (n+u)/v, A* = tv−1 = (n+v)/u.
V(n) := {v : 4 | v} ∪ {v ≡ c (mod 8)}, c = −n mod 8 (7 if n ≡ 1, 3 if n ≡ 5 (mod 8)).
U(n) := some word has an endpoint in V(n)  (the T1-exact two-line union of the z49 context).

Vertex form:  v ∈ V is an endpoint  ⟺  n+v has a divisor A ≡ −1 (mod v)  (then u = (n+v)/A, t = (A+1)/v).
Level form:   U(n) ⟺ ∃ t, ∃ A | tn+1 with A ≡ −1 (mod t) and (A+1)/t ∈ V.
"""
from math import isqrt, gcd
from sympy import factorint, jacobi_symbol


def divisors(n, f=None):
    f = factorint(n) if f is None else f
    ds = [1]
    for q, e in f.items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return sorted(ds)


def cls(n):
    return 7 if n % 8 == 1 else 3


def inV(x, n):
    return x % 4 == 0 or x % 8 == cls(n)


def words_at_vertex(n, v):
    """All words (t,u,v) of n with this endpoint v (any t ≥ 1, any u ≥ 1)."""
    out = []
    for A in divisors(n + v):
        if (A + 1) % v == 0:
            u = (n + v) // A
            t = (A + 1) // v
            out.append((t, u, v))
    return out


def all_words(n, vmax=None):
    """All words (t,u,v) of n with v ≤ vmax (default: all, v ≤ n+2), listed once per ordered pair."""
    vmax = n + 2 if vmax is None else vmax
    out = []
    for v in range(1, vmax + 1):
        out.extend(words_at_vertex(n, v))
    return out


def U_witnesses(n, vmax=None):
    """Words with endpoint v ∈ V(n), v ≤ vmax (vertex form; u is unconstrained)."""
    vmax = n + 2 if vmax is None else vmax
    out = []
    c = cls(n)
    for v in range(1, vmax + 1):
        if v % 4 == 0 or v % 8 == c:
            out.extend(words_at_vertex(n, v))
    return out


def U(n):
    return bool(U_witnesses(n))


def slot(t, u, v):
    return [name for name, val in (("t", t), ("u", u), ("v", v), ("tu-1", t * u - 1), ("tv-1", t * v - 1)) if val % 4 == 0]


def es_identity(n, t, u, v):
    """Return the ES triple from the first slot, as a Fraction check."""
    from fractions import Fraction as F
    A, As = t * u - 1, t * v - 1
    if t % 4 == 0:
        C = t // 4
        x = (u * v * C, n * v * C, n * u * C)
    elif u % 4 == 0:
        d = u // 4
        x = (d * As, n * t * d, n * t * d * As)
    elif v % 4 == 0:
        d = v // 4
        x = (d * A, n * t * d, n * t * d * A)
    elif As % 4 == 0:
        m = As // 4
        x = (m * u, m * u * A, n * m * A)
    elif A % 4 == 0:
        m = A // 4
        x = (m * v, m * v * As, n * m * As)
    else:
        return None
    assert sum(F(1, xi) for xi in x) == F(4, n), (n, t, u, v, x)
    return x


if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])
    print(f"n = {n} ≡ {n % 8} (mod 8), c = {cls(n)}, square = {isqrt(n) ** 2 == n}, factors = {factorint(n)}")
    W = U_witnesses(n, int(sys.argv[2]) if len(sys.argv) > 2 else None)
    print(f"{len(W)} U-words (endpoint v ∈ V):")
    for t, u, v in W[:40]:
        A, As = t * u - 1, t * v - 1
        Aodd = A >> ((A & -A).bit_length() - 1)
        print(f"  t={t:6d} u={u:8d} v={v:6d}  A={A:8d} A*={As:8d} gcd(uv,n)={gcd(u*v,n)} (n/A_odd)={int(jacobi_symbol(n, Aodd)) if Aodd>1 else 1:+d} slots={slot(t,u,v)} ES={es_identity(n,t,u,v)}")
