"""R198 from-scratch check of CHI_FLIP Thm 1.1 / Cor 1.3 (does NOT import cf_*).

For every positive word w=(t,u,v), K(w)=tuv-u-v=n odd, n <= NMAX:
  * Gram G_w = [[v,-1,0],[-1,t,-1],[0,-1,u]]; det computed generically, must equal n.
  * Diagonalise over Q by leading minors (pivots D1, D2/D1, D3/D2), Hilbert symbols at every place
    dividing 2*n*pivots and at infinity -> eps_l (isotropy sign) via Serre IV.2.2 Thm 6:
    ternary <a1,a2,a3> isotropic over Q_l iff c_l = (-1,-d)_l, c_l = prod_{i<j}(ai,aj)_l, d = a1a2a3.
  * Second, independent eps_2: brute force mod 8 (primitive x mod 8 with Q(x) = 0 mod 8 <=> Q_2-isotropic,
    valid since det odd => grad = 2Gx has valuation exactly 1 for primitive x, Hensel needs v(Q) >= 3).
  * Checks: det = n; positive definite; eps_inf = -1; product formula; eps_l = (-A/l)^{v_l(n)} for odd l;
    chi := (-A/n) == -eps_2 (both eps_2 methods); for n prime: C_0 = (-A*, -v A* n) quaternion algebra
    has ramification {n, inf} iff chi=-1 else {2, inf}.
Usage: PYTHONPATH=scripts uv run python scripts/review_cf_hasse.py 2000
"""
import sys
from fractions import Fraction
from itertools import product


def factor(n):
    n = abs(n); f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    return 1 if r == 1 else -1


def jacobi_by_factoring(a, n):  # deliberately via factorisation, not the reciprocity algorithm
    r = 1
    for p, e in factor(n).items():
        r *= legendre(a, p) ** e
    return r


def val(a, p):
    k = 0
    while a % p == 0:
        a //= p; k += 1
    return k, a


def hilbert(a, b, p):
    """(a,b)_p for nonzero integers a,b; p prime or 0 for infinity."""
    if p == 0:
        return -1 if (a < 0 and b < 0) else 1
    al, u = val(a, p); be, w = val(b, p)
    if p == 2:
        eps = lambda x: ((x - 1) // 2) % 2
        om = lambda x: ((x * x - 1) // 8) % 2
        e = eps(u) * eps(w) + al * om(w) + be * om(u)
        return -1 if e % 2 else 1
    s = (-1) ** ((al * be * ((p - 1) // 2)) % 2)
    return s * legendre(u, p) ** be * legendre(w, p) ** al


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def squarefree_int(fr):
    """rational -> integer in the same square class."""
    return fr.numerator * fr.denominator


def eps_place(diag, p):
    a1, a2, a3 = diag
    c = hilbert(a1, a2, p) * hilbert(a1, a3, p) * hilbert(a2, a3, p)
    d = a1 * a2 * a3
    return 1 if c == hilbert(-1, -d, p) else -1


def eps2_brute(t, u, v):
    for x in product(range(8), repeat=3):
        if all(xi % 2 == 0 for xi in x):
            continue
        a, b, c = x
        if (v * a * a + t * b * b + u * c * c - 2 * a * b - 2 * b * c) % 8 == 0:
            return 1
    return -1


def words(NMAX):
    for t in range(1, NMAX + 3):
        for u in range(1, NMAX + 3):
            A = t * u - 1
            if A <= 0:
                continue
            if A - u > NMAX:
                break
            v = 1
            while True:
                n = A * v - u
                if n > NMAX:
                    break
                if n >= 1 and n % 2 == 1:
                    yield t, u, v, n
                v += 1


def main():
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    cnt = bad = 0
    nprime = 0
    cache2 = {}
    for t, u, v, n in words(NMAX):
        cnt += 1
        G = [[v, -1, 0], [-1, t, -1], [0, -1, u]]
        D1, D2, D3 = v, v * t - 1, det3(G)
        assert D3 == n, (t, u, v)
        assert D1 > 0 and D2 > 0 and D3 > 0
        A, As = t * u - 1, t * v - 1
        assert D2 == As and A * As == t * n + 1
        diag = [D1, squarefree_int(Fraction(D2, D1)), squarefree_int(Fraction(D3, D2))]
        places = {2} | set(factor(2 * n * D1 * D2).keys())
        eps = {p: eps_place(diag, p) for p in places}
        eps[0] = eps_place(diag, 0)
        prodall = 1
        for e in eps.values():
            prodall *= e
        chi = jacobi_by_factoring(-A, n)
        key = (t % 8, u % 8, v % 8)
        if key not in cache2:
            cache2[key] = eps2_brute(t, u, v)
        ok = (eps[0] == -1 and prodall == 1 and chi == -eps[2] and cache2[key] == eps[2])
        fn = factor(n)
        for p in places:
            if p in (0, 2):
                continue
            k = fn.get(p, 0)
            ok &= eps[p] == (legendre(-A, p) ** k if k else 1)
        if len(fn) == 1 and list(fn.values())[0] == 1:
            nprime += 1
            a, b = -As, -v * As * n
            ram = {p for p in set(factor(2 * a * b).keys()) | {2} if hilbert(a, b, p) == -1}
            if hilbert(a, b, 0) == -1:
                ram.add(0)
            ok &= ram == ({n, 0} if chi == -1 else {2, 0})
        if not ok:
            bad += 1
            if bad < 10:
                print("FAIL", t, u, v, n, chi, eps)
    print(f"NMAX={NMAX}: words={cnt} (prime-n words {nprime}), failures={bad}, cells mod 8 seen={len(cache2)}")


if __name__ == "__main__":
    main()
