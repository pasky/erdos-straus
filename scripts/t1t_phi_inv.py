"""O183: local invariants of alpha(u) = (-u1/u3, -u2/u3) on V_phi solutions (K = Q(sqrt5)).

Odd places: tame symbol; real places: signs; the place (2) is obtained by Hilbert reciprocity.
Usage: PYTHONPATH=scripts uv run python scripts/t1t_phi_inv.py B2 J n1 n2 ...
"""
import sys
from sympy import factorint
from t1t_phi import mul, add, norm, s1, s2, exact_div, conj
from t1t_phi_search import solve, prime_elements, vq


def residue_pow(w, q, ell, e):
    """w^e in O/q for a q-unit w (element of O), returned as a canonical tuple."""
    if q == (ell, 0):  # inert: F_{ell^2} = F_ell[phi]
        r = (1, 0)
        b = (w[0] % ell, w[1] % ell)
        while e:
            if e & 1:
                r = mul(r, b)
                r = (r[0] % ell, r[1] % ell)
            b = mul(b, b)
            b = (b[0] % ell, b[1] % ell)
            e >>= 1
        return r
    # split or ramified: O/q = F_ell, phi -> rr with q | phi - rr
    for rr in range(ell):
        if exact_div((-rr, 1), q) is not None:
            val = (w[0] + w[1] * rr) % ell
            return (pow(val, e, ell), 0)
    raise ValueError


def strip(a, q):
    v = 0
    while True:
        b = exact_div(a, q)
        if b is None:
            return v, a
        a = b
        v += 1


def hilbert_odd(A, B, q, ell):
    """(A, B)_q with A = A0/A1, B = B0/B1 given as pairs of O-elements. Returns 0 or 1 (additive, in 1/2 Z/Z)."""
    Nq = ell if q != (ell, 0) else ell * ell
    va0, a0 = strip(A[0], q)
    va1, a1 = strip(A[1], q)
    vb0, b0 = strip(B[0], q)
    vb1, b1 = strip(B[1], q)
    al, be = va0 - va1, vb0 - vb1
    # c = (-1)^{al be} a^be / b^al ; a = a0/a1, b = b0/b1 (units)
    num = (1, 0)
    den = (1, 0)
    def pw(x, k):
        r = (1, 0)
        for _ in range(abs(k)):
            r = mul(r, x)
        return r
    if be >= 0:
        num = mul(num, pw(a0, be)); den = mul(den, pw(a1, be))
    else:
        num = mul(num, pw(a1, -be)); den = mul(den, pw(a0, -be))
    if al >= 0:
        num = mul(num, pw(b1, al)); den = mul(den, pw(b0, al))
    else:
        num = mul(num, pw(b0, -al)); den = mul(den, pw(b1, -al))
    if (al * be) % 2:
        num = mul(num, (-1, 0))
    c = mul(num, den)  # num/den has same quadratic character as num*den
    r = residue_pow(c, q, ell, (Nq - 1) // 2)
    return 0 if r == (1, 0) else 1


def invariants(t):
    x, y, z = t
    A = (mul((-1, 0), x), z)  # -u1/u3
    B = (mul((-1, 0), y), z)
    out = {}
    out['s1'] = 1 if (s1(A[0]) / s1(A[1]) < 0 and s1(B[0]) / s1(B[1]) < 0) else 0
    out['s2'] = 1 if (s2(A[0]) / s2(A[1]) < 0 and s2(B[0]) / s2(B[1]) < 0) else 0
    ells = set()
    for w in (x, y, z):
        ells |= set(factorint(abs(norm(w))))
    for ell in sorted(ells):
        if ell == 2:
            continue
        for q in prime_elements(ell):
            out[(ell, q)] = hilbert_odd(A, B, q, ell)
    out['2'] = sum(out.values()) % 2  # reciprocity
    return {k: v for k, v in out.items() if v}


if __name__ == '__main__':
    B2, J = float(sys.argv[1]), int(sys.argv[2])
    for n in map(int, sys.argv[3:]):
        nprimes = set(factorint(n))
        stats = {}
        for t in solve(n, B2, J):
            inv = invariants(t)
            key = tuple(sorted(str(k[0]) + ('' if k[0] in nprimes else '*tame*') if isinstance(k, tuple) else k
                               for k in inv))
            stats[key] = stats.get(key, 0) + 1
        print(n, stats)
