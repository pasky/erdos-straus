"""R227 from-scratch checks of Lemma S, Lemma G, the u-side / t-side deformations and the K0 = 8 defect mechanism.
Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_r227_lemmas.py
"""
from math import gcd, isqrt
from sympy import factorint, isprime, jacobi_symbol as J


def words(n):
    """All ordered positive words (t,u,v), t*u*v-u-v = n, by brute force over (t,u) (independent of the C code)."""
    out = []
    for u in range(1, n + 2):
        for t in range(1, n + 3):
            A = t * u - 1
            if A <= 0:
                continue
            if A > n + u:
                break
            if (n + u) % A == 0:
                v = (n + u) // A
                assert t * u * v - u - v == n
                out.append((t, u, v))
    return out


def clean(x, n):
    return all(J(r, n) != -1 for r in factorint(x))


def is_sq(x):
    return x >= 0 and isqrt(x) ** 2 == x


bad = {"G": 0, "S": 0, "Sb": 0, "uside": 0, "tside": 0}
nw = 0
for p in range(5, 1200):
    if p % 4 != 1 or not isprime(p):
        continue
    W = words(p)
    nw += len(W)
    for (t, u, v) in W:
        A, B = t * u - 1, t * v - 1
        if gcd(t * p + 1, p + u) != A or gcd(t * p + 1, p + v) != B:
            bad["G"] += 1
        chi = J(-A, p)
        if J(A, p) != chi or J(B, p) != chi:
            bad["S"] += 1
        for X, NX in ((t, t * p + 1), (u, p + u), (v, p + v)):
            for r in factorint(NX):
                if r > 2 and J(r, p) != J(-X, r):
                    bad["Sb"] += 1
            if clean(NX, p) and chi == -1:
                bad["S"] += 1
    # deformations: p = m^2 + K, all m with K > 0 (not only floor sqrt)
    if p % 8 == 1:
        for m in range(1, isqrt(p) + 1):
            K = p - m * m
            # complete list of u >= 1 with u(K+u) = square: u = d a^2, K + u = d b^2, d | K, (b-a)(b+a) = K/d
            us = set()
            for d in range(1, K + 1):
                if K % d:
                    continue
                Q = K // d
                for e in range(1, isqrt(Q) + 1):
                    if Q % e == 0 and (e + Q // e) % 2 == 0 and Q // e > e:
                        a = (Q // e - e) // 2
                        us.add(d * a * a)
            for u in us:
                assert is_sq(u * (K + u))
                if gcd(m, K + u) == 1 and not clean(p + u, p):
                    bad["uside"] += 1
            for t in range(1, 200):
                if is_sq(t * K + 1) and gcd(m, isqrt(t * K + 1)) == 1 and not clean(t * p + 1, p):
                    bad["tside"] += 1
print("words", nw, "defects", bad)

# u-side solution sets for K = 24 (brute force, u up to a generous bound; u(K+u)=square => u <= (K/2)^2)
for K in (8, 24, 16):
    us = [u for u in range(1, K * K) if is_sq(u * (K + u))]
    ts = [t for t in range(1, 60) if is_sq(t * K + 1)]
    print("K", K, "u-side", us, "t-side(<60)", ts)

# K0 = 8 mechanism: p = m^2 + 8 prime => 3 | m; N_u (u=1) = 9 * (clean); t-sides 8t+1 = c^2, t = 1 mod 9
cnt = {"p": 0, "3|m": 0, "u1_exact9_clean": 0, "tside_total": 0, "tside_exact9_clean": 0}
for m in range(1, 3000):
    p = m * m + 8
    if not isprime(p):
        continue
    cnt["p"] += 1
    cnt["3|m"] += (m % 3 == 0)
    f = factorint(p + 1)
    if f.get(3) == 2 and all(J(r, p) == 1 for r in f if r != 3) and J(3, p) == -1:
        cnt["u1_exact9_clean"] += 1
    for c in range(3, 400, 2):
        if (c * c - 1) % 8 == 0 and ((c * c - 1) // 8) % 9 == 1:
            t = (c * c - 1) // 8
            f = factorint(t * p + 1)
            cnt["tside_total"] += 1
            if f.get(3) == 2 and all(J(r, p) == 1 for r in f if r != 3):
                cnt["tside_exact9_clean"] += 1
print("K0=8 mechanism", cnt)
