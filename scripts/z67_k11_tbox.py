"""z67 K11: the T-box problem for the slice pi = (q1 at every prime outside T, free at T) of K-bar.

T = {2,3,5,7} (default) or {2,3,5,7,11,13} (if exponents for 11, 13 are given).  q1 must be a T-unit.
pi lies in K-bar iff pi_T = 1 mod 840 and the 11-component is a non-residue (q1 itself if 11 not in T).
A class r mod m (m = mT m'') catches the T-box cylinder {pi_T = r mod mT} iff r = q1 mod m'' (rigid) and the
cylinder meets the box (r = 1 mod gcd(mT, 840), r non-residue mod 11 if 11 | mT).  All seven families are enumerated
literally with modulus <= MMAX; the survivor fraction of the box is computed exactly at T-levels dividing LEVEL
(only cylinders with mT | LEVEL are used, so a survivor count is an UPPER bound for the slice; a count of 0 is a
CERTIFIED finite covering of the slice by the listed classes).
Usage: uv run --with sympy --with numpy python scripts/z67_k11_tbox.py MMAX q1 e2 e3 e5 e7 [e11 e13]
"""
import sys
from fractions import Fraction
from math import gcd

import numpy as np
from sympy import divisors
from sympy.ntheory.residue_ntheory import sqrt_mod


TP = (2, 3, 5, 7)


def tsplit(m):
    mt = 1
    for p in TP:
        while m % p == 0:
            m //= p
            mt *= p
    return mt, m


def main():
    MMAX = int(sys.argv[1])
    q1 = Fraction(sys.argv[2])
    global TP
    e = [int(x) for x in sys.argv[3:] if x.lstrip("-").isdigit()][:6]
    if len(e) == 6:
        TP = (2, 3, 5, 7, 11, 13)
    LEVEL = 1
    for p, k in zip(TP, e):
        LEVEL *= p ** k
    u, v = q1.numerator, q1.denominator
    cyl = {}
    cert = {}
    fams = {}

    def test(r, m, tag):
        r %= m
        if gcd(r, m) != 1:
            return
        mt, mo = tsplit(m)
        if mo > 1 and (gcd(v, mo) != 1 or (r * v - u) % mo):
            return
        g = gcd(mt, 840)
        if r % g != 1 % g or LEVEL % mt:
            return
        if mt % 11 == 0 and pow(r % 11, 5, 11) != 10:
            return
        cyl.setdefault(mt, set()).add(r % mt)
        cert.setdefault((mt, r % mt), (tag, m, r))
        fams.setdefault(tag.split()[0], 0)
        fams[tag.split()[0]] += 1
    for a in range(1, MMAX // 4 + 1):
        for d in range(1, MMAX // (4 * a) + 1):
            for f in divisors(4 * a * a * d + 1):
                test(-f, 4 * a * d, f"I1 a={a} d={d} f={f}")
    for a in range(1, MMAX // 4 + 1):
        for c in range(1, MMAX // (4 * a) + 1):
            M1 = 4 * a * c
            for f in range(2, MMAX // M1 + 1):
                if gcd(M1, f) != 1:
                    continue
                inv = pow(M1, -1, f)
                r2 = (-c * pow(a, -1, f)) % f
                test(-f + M1 * (((r2 + f) * inv) % f), M1 * f, f"I2 a={a} c={c} f={f}")
                for x in sqrt_mod((-4 * a * a * c) % f, f, all_roots=True) or []:
                    test(-f + M1 * (((x + f) * inv) % f), M1 * f, f"I3 c={a} d={c} f={f} x={x}")
    for a in range(1, MMAX // 4 + 1):
        for b in range(1, MMAX // (4 * a) + 1):
            m = 4 * a * b
            for ee in divisors(a + b):
                if gcd(ee, m) == 1:
                    test(-pow(ee, -1, m), m, f"I4 a={a} b={b} e={ee}")
                    test(-ee, m, f"II1 a={a} b={b} e={ee}")
    for f in range(3, MMAX + 1, 4):
        P = (f + 1) // 4
        for a in divisors(P):
            for d in divisors(P // a):
                test(-4 * a * a * d, f, f"II2 a={a} d={d} f={f}")
    for a in range(1, MMAX // 4 + 1):
        for d in range(1, MMAX // (4 * a) + 1):
            for ee in range(1, MMAX // (4 * a * d) + 1):
                if gcd(4 * a * d, ee) == 1:
                    test(-4 * a * a * d - ee, 4 * a * d * ee, f"II3 a={a} d={d} e={ee}")
    print(f"# q1={q1} MMAX={MMAX} LEVEL={LEVEL}: {sum(len(s) for s in cyl.values())} T-cylinders, by family {fams}")
    g8 = gcd(LEVEL, 840)
    xs = 1 + g8 * np.arange(LEVEL // g8, dtype=np.int64)   # residues = 1 mod gcd(LEVEL, 840)
    for p in TP:
        if LEVEL % p == 0:
            xs = xs[xs % p != 0]
    if LEVEL % 11 == 0:
        xs = xs[np.isin(xs % 11, [2, 6, 7, 8, 10])]
    alive = np.ones(len(xs), dtype=bool)
    for mt, R in cyl.items():
        alive &= ~np.isin(xs % mt, np.fromiter(R, dtype=np.int64))
    print(f"T-box survivors at LEVEL {LEVEL}: {alive.sum()}/{len(xs)} = {alive.mean():.4f}")
    if "--cert" in sys.argv and alive.sum() == 0:
        # greedy subcover, written as "family params | m r" lines for the independent verifier
        left = np.ones(len(xs), dtype=bool)
        items = sorted(cert.items(), key=lambda kv: kv[0][0])
        out = open(sys.argv[sys.argv.index("--cert") + 1], "w")
        out.write(f"# slice q1={q1} T={TP} LEVEL={LEVEL} box residues {len(xs)}\n")
        while left.any():
            best, bk = None, -1
            for (mt, rt), val in items:
                k = int((left & (xs % mt == rt)).sum())
                if k > bk:
                    best, bk = ((mt, rt), val), k
            (mt, rt), (tag, m, r) = best
            left &= ~(xs % mt == rt)
            out.write(f"{tag} | {m} {r % m}\n")
        out.close()
    for mt in sorted(cyl):
        if len(cyl[mt]) and mt < 3000:
            print("   ", mt, sorted(cyl[mt])[:10])


if __name__ == "__main__":
    main()
