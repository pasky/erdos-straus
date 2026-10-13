"""R187: from-scratch enumeration of the Case B tuple set F(s) of DEPTH_ASPECT §2.1 over F_q (q prime, small),
directly from the definition (B):
    m' w C = T^s + v,  w + C = g' v,  T || w, T || C, T does not divide m' g',  v != 0,  m', g', w, C monic.
Enumerates all monic (w, C, m') with T||w, T||C, T∤m', deg w + deg C + deg m' = s, puts v = m'wC - T^s and keeps the
tuple iff v != 0, v | w + C and g' = (w+C)/v is monic with T ∤ g'.
Checks on every tuple: Lemma 2.1 identities (R2) E | 1 + T^s L'g', (R3) E | g'T^s + w, (R4) E | T^s + m'w^2, and the
per-pattern bound of Lemma 2.2 in both forms (16^s q^{min} and the 'fine' min of the four reconstruction bounds).
Prints |F(s)|.  Usage: uv run python scripts/review_da2_caseB_enum.py q SMAX
"""
import sys
from itertools import product
from math import log


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def mul(a, b, p):
    if not a or not b:
        return ()
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                c[i + j] = (c[i + j] + x * y) % p
    return trim(c)


def add(a, b, p):
    n = max(len(a), len(b))
    return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(n)])


def neg(a, p):
    return tuple((-x) % p for x in a)


def divmod_(a, b, p):
    a = list(a)
    inv = pow(b[-1], -1, p)
    qd = [0] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b) and a:
        c = a[-1] * inv % p
        sh = len(a) - len(b)
        qd[sh] = c
        for i, y in enumerate(b):
            a[sh + i] = (a[sh + i] - c * y) % p
        a = list(trim(a))
    return trim(qd), tuple(a)


def monics(deg, p, cond):
    for coeffs in product(range(p), repeat=deg):
        f = tuple(coeffs) + (1,)
        if cond(f):
            yield f


def Tpow(s):
    return tuple([0] * s + [1])


def main(p, SMAX):
    q = p
    for s in range(3, SMAX + 1):
        Ts = Tpow(s)
        tuples = []
        for a in range(1, s):
            W = list(monics(a, p, lambda f: f[0] == 0 and f[1] != 0))
            for b in range(1, s - a + 1):
                z = s - a - b
                Cs = list(monics(b, p, lambda f: f[0] == 0 and f[1] != 0))
                Ms = list(monics(z, p, lambda f: f[0] != 0))
                for w in W:
                    for C in Cs:
                        wC = mul(w, C, p)
                        wpc = add(w, C, p)
                        for m in Ms:
                            v = add(mul(m, wC, p), neg(Ts, p), p)
                            if not v:
                                continue
                            g, rem = divmod_(wpc, v, p)
                            if rem or not g or g[-1] != 1 or g[0] == 0:
                                continue
                            tuples.append((m, g, w, C, v))
        # checks
        nbad = 0
        pat = {}
        for m, g, w, C, v in tuples:
            Lp = mul(g, m, p)
            E = add(mul(Lp, w, p), (p - 1,), p)
            D = add((1,), mul(Ts, mul(Lp, g, p), p), p)
            ok = E[-1] == 1
            for X in (D, add(mul(g, Ts, p), w, p), add(Ts, mul(m, mul(w, w, p), p), p)):
                ok &= not divmod_(X, E, p)[1]
            nbad += not ok
            key = (len(w) - 1, len(C) - 1, len(m) - 1, len(g) - 1, len(v) - 1)
            pat[key] = pat.get(key, 0) + 1
        viol_stated = viol_fine = 0
        for (a, b, z, y, t), cnt in pat.items():
            mn, M = min(a, b), max(a, b)
            assert y + t <= M and t >= 2, (a, b, z, y, t)
            stated = 16 ** s * q ** min(t - 2, y + z, mn - 1 + y, mn - 1 + z)
            fine = min(2 * q ** (t - 2) * 3 ** s, q ** (y + z) * 2 ** (y + z) * 2 ** (s + 2 * y + z),
                       q ** (mn - 1 + y) * 2 ** (s + y), q ** (mn - 1 + z) * 2 ** max(s, z + 2 * mn))
            viol_stated += cnt > stated
            viol_fine += cnt > fine
        print(f"q={p} s={s}: |F(s)| = {len(tuples)}  identity failures {nbad}  patterns {len(pat)}  "
              f"bound violations (stated/fine) {viol_stated}/{viol_fine}  max pattern count {max(pat.values(), default=0)}",
              flush=True)


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
