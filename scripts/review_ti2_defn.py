"""R69 second engine, straight from the definition of Cl(c,k,F).

For every slice (c,k) with ck<=X (ALL slices, forced or not), factor
N=1+4ck^2, enumerate every divisor F with (F,4ck)=1, build xhat mod 4ckF by
CRT from its prime components (w at 2, -1 at r, +1 elsewhere) and test
  x == -F (mod 4ck)  and  x^2 == -4ck^2 (mod F).
Reports certificates (all, and those with s=sf(c) not in {1,2,3,6}).
usage: review_ti2_defn.py r w X
"""
import sys
from math import gcd
from sympy import factorint
from sympy.ntheory.modular import crt


def sqfree(n):
    s = 1
    for q, e in factorint(n).items():
        if e & 1:
            s *= q
    return s


def xhat_mod(M, r, w):
    mods, res = [], []
    for q, e in factorint(M).items():
        qe = q ** e
        mods.append(qe)
        res.append(w % qe if q == 2 else (-1) % qe if q == r else 1 % qe)
    if not mods:
        return 0
    return int(crt(mods, res)[0])


def divisors(fac):
    ds = [1]
    for q, e in fac.items():
        ds = [d * q ** i for d in ds for i in range(e + 1)]
    return ds


def main():
    r, w, X = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    found = []
    nsl = 0
    for c in range(1, X + 1):
        for k in range(1, X // c + 1):
            nsl += 1
            h = 4 * c * k
            N = 1 + 4 * c * k * k
            for F in divisors(factorint(N)):
                if gcd(F, h) != 1:
                    continue
                x = xhat_mod(h * F, r, w)
                if (x + F) % h == 0 and (x * x + 4 * c * k * k) % F == 0:
                    s = sqfree(c)
                    vr = 0
                    cc = c
                    while cc % r == 0:
                        cc //= r
                        vr += 1
                    found.append((c * k, c, k, F, s, vr))
    found.sort()
    good = [f for f in found if f[4] not in (1, 2, 3, 6)]
    bad_parity = [f for f in good if f[5] % 2 == 0]
    print(f"r={r} w={w} X={X} slices={nsl} all_certs={len(found)} "
          f"certs_s_ok={len(good)} with_v_r_even={len(bad_parity)}")
    import os
    for f in (good if os.environ.get('ALL') else good[:10]):
        print("  ck=%d c=%d k=%d F=%d s=%d v_r(c)=%d" % f)


if __name__ == "__main__":
    main()
