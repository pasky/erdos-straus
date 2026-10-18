"""R283 from-scratch check of O272 Thm 3.2 (Stickelberger dictionary), m = 3 (Z[w]) and m = 4 (Z[i]).

For primes l, q = 1 (mod m), primary lambda | l, a prime 𝔮 | q (given by an element pi):
  x_a = (sigma_a lambda / 𝔮)_m,  S = (q / lambda)_m,  D = (l / 𝔮)_m.
Claim: S = prod_a x_a^{a^{-1}}  (m = 3: k_S = k1 + 2 k2; m = 4: k_S = k1 + 3 k3), D = prod x_a.
Symbols computed by reduction: O/(pi) = F_p via zeta -> r with pi(r) = 0 mod p; (alpha/pi)_m = alpha(r)^((p-1)/m) = r^k.
Also: (i) primarity of lambda is needed (unit-twisted lambda breaks S-identity); (ii) sharpness: inside fixed q mod l,
all x-vectors with the prescribed S occur, roughly uniformly.
"""
import sys
from collections import Counter, defaultdict
from sympy import primerange, isprime


def mul(m, x, y):
    a, b = x; c, d = y
    if m == 3:  # w^2 = -1 - w
        return (a * c - b * d, a * d + b * c - b * d)
    return (a * c - b * d, a * d + b * c)


def conj(m, x):
    a, b = x
    return (a - b, -b) if m == 3 else (a, -b)


def norm(m, x):
    a, b = x
    return a * a - a * b + b * b if m == 3 else a * a + b * b


def units(m):
    if m == 3:
        u, w = [(1, 0)], (0, 1)
        for _ in range(5):
            u.append(mul(3, u[-1], (1, 1)))  # 1 + w = -w^2, primitive 6th root
        return u
    return [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_primary(m, x):
    a, b = x
    if m == 3:
        return a % 3 == 2 and b % 3 == 0
    return (a % 4 == 1 and b % 4 == 0) or (a % 4 == 3 and b % 4 == 2)


def prime_elt(m, p):
    """some element of norm p (brute force)"""
    import math
    for a in range(0, 2 * math.isqrt(p) + 2):
        for b in range(-2 * math.isqrt(p) - 2, 2 * math.isqrt(p) + 3):
            if norm(m, (a, b)) == p:
                return (a, b)
    raise ValueError


def primary(m, p):
    x = prime_elt(m, p)
    c = [mul(m, u, x) for u in units(m) if is_primary(m, mul(m, u, x))]
    assert len(c) >= 1, (m, p, x)
    return c[0]


def residue_root(m, x, p):
    a, b = x
    r = (-a * pow(b, -1, p)) % p
    assert pow(r, m, p) == 1 and all(pow(r, j, p) != 1 for j in range(1, m))
    return r


def sym(m, alpha, pi, p):
    """(alpha/pi)_m as exponent k of zeta (zeta -> r)"""
    r = residue_root(m, pi, p)
    v = (alpha[0] + alpha[1] * r) % p
    assert v != 0
    z = pow(v, (p - 1) // m, p)
    for k in range(m):
        if pow(r, k, p) == z:
            return k
    raise ValueError


def run(m, LMAX, QMAX):
    fail = tot = disc = 0
    nonprim_fail = 0
    joint = defaultdict(Counter)  # (l, q mod l) -> Counter of x-vector
    lam_cache = {}
    for l in primerange(m + 1, LMAX):
        if l % m != 1:
            continue
        lam = primary(m, l); lamb = conj(m, lam)
        assert mul(m, lam, lamb) == (l, 0)
        for q in primerange(m + 1, QMAX):
            if q % m != 1 or q == l:
                continue
            pi = primary(m, q)
            for P in (pi, conj(m, pi)):  # both primes above q
                k1 = sym(m, lam, P, q); k2 = sym(m, lamb, P, q)  # k2 = x_{-1}
                kD = sym(m, (l, 0), P, q)
                kS = sym(m, (q, 0), lam, l)
                pred = (k1 + (2 if m == 3 else 3) * k2) % m
                tot += 1
                fail += (pred != kS)
                disc += ((k1 + k2) % m != kS)  # S != D cases (shows the identity is discriminating)
                assert kD == (k1 + k2) % m
                # non-primary lambda: multiply by a unit that is not +-1
                u = units(m)[1]
                lu = mul(m, u, lam); lub = conj(m, lu)
                predu = (sym(m, lu, P, q) + (2 if m == 3 else 3) * sym(m, lub, P, q)) % m
                nonprim_fail += (predu != kS)
                if P == pi:
                    joint[(l, q % l)][(k1, k2)] += 1
    print(f"m={m}: pairs(l<{LMAX}, q<{QMAX}, both 𝔮|q) = {tot}; S-identity failures = {fail}; "
          f"S!=D cases = {disc}; identity failures with non-primary lambda = {nonprim_fail}")
    # sharpness: for each (l, q mod l) cell with >= 12 samples, vectors seen vs. expected (all with prescribed S)
    full = cells = 0
    for (l, c), C in joint.items():
        if sum(C.values()) < 4 * m * m:
            continue
        cells += 1
        Ss = {(k1 + (2 if m == 3 else 3) * k2) % m for (k1, k2) in C}
        assert len(Ss) == 1  # S constant on q mod l
        if len(C) == m:  # m vectors (k1,k2) with given S
            full += 1
    print(f"  sharpness: cells (l, q mod l) with >= {4*m*m} samples: {cells}; all {m} S-compatible vectors seen in {full}")


if __name__ == "__main__":
    run(3, 80, 3000)
    run(4, 80, 3000)
    run(3, 20, 60000)
    run(4, 20, 60000)
