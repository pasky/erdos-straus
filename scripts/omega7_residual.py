#!/usr/bin/env python3
"""POINTWISE_OMEGA7 (checks + EVIDENCE).

Enumerates all m>1 atoms exactly as scripts/omega6_corner.py (q=l1*l2,
Pi = y-smooth, weight 2/n', survival m | a+b) and
 (1) asserts Lemma 1.1 (i)-(iii),(v'), Lemma 2.0 for every atom;
 (2) splits the m>1 mass into the boxes covered by O7 Cor 2.4 / Cor 3.2
     (constants and log-powers dropped, slack factor Z) and the residual
     boxes of Thm 3.3:  with (S,A) the dyadic box of (s,min(a,b)),
       cov2:  S >= Z*max(A^2, q);   cov3: S >= Z*A*q;   residual: neither.
Output: per hub level X, the max over classes with height > X of
  tot, residual part, corner-residual part.
usage: omega7_residual.py T y l1 l2 [HCAP] [Z]
"""
import sys
from math import gcd
from sympy import factorint, divisors
from omega5_codeg import heights


def sqfree(n):
    return all(e == 1 for e in factorint(n).values())


def dy(x):
    return 1 << (x.bit_length() - 1)


def main():
    T, y, l1, l2 = (int(x) for x in sys.argv[1:5])
    cap = int(sys.argv[5]) if len(sys.argv) > 5 else 2048
    Z = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0
    q = l1 * l2
    tot, res, cres = {}, {}, {}
    nat = nres = nchk = 0
    for N in range(1, T // q + 1):
        M = q * N
        if M % 4 != 3 or N % l1 == 0 or N % l2 == 0:
            continue
        m = 1
        for p, e in factorint(N).items():
            if p <= y:
                m *= p ** e
        if m == 1 or N == m:
            continue
        L = (M + 1) // 4
        Q = q * m
        n1 = N // m
        for s in divisors(L):
            if not sqfree(s):
                continue
            for a in divisors(L // s):
                b = L // (s * a)
                if (a + b) % m:
                    continue
                kap = a * pow(b, -1, q) % q
                # Lemma 1.1 / 2.0 checks
                j = (a + b) // m
                F = 4 * s * a * a + 1
                assert F % m == 0
                ms = F // m
                assert q * n1 == 4 * s * a * j - ms
                assert ms * b == a * q * n1 + j
                assert (a * ms - kap * j) % q == 0
                assert (j * m - (1 + pow(kap, -1, q)) * a) % q == 0
                assert (m * ms - 1) % (4 * a * a) == 0
                g0 = gcd(kap + 1, q)
                for p in factorint(g0):
                    assert j % p == 0
                w = 2.0 / n1
                u = min(a, b)
                assert w <= (4.0 / 3.0) * q / (j * s * u) * (1 + 1e-12)
                nchk += 1
                nat += 1
                S, A = dy(s), dy(u)
                cov = S >= Z * max(A * A, q) or S >= Z * A * q
                tot[kap] = tot.get(kap, 0.0) + w
                if cov:
                    continue
                nres += 1
                res[kap] = res.get(kap, 0.0) + w
                first = True
                for (x1, x2, x) in ((s, a, b), (s, b, a), (a, b, s)):
                    if 4 * x1 * x2 <= y or (x - Q >= 1 and n1 - 4 * x1 * x2 >= y):
                        first = False
                        break
                if first:
                    cres[kap] = cres.get(kap, 0.0) + w
    h = heights(q, cap)
    print(f"T={T} y={y} q={q} Z={Z} m>1 atoms={nat} (all Lemma 1.1/2.0 checks "
          f"passed: {nchk}) residual atoms={nres} HCAP={cap}")
    print(" X    max_tot(h>X)  max_res(h>X)  max_cornres(h>X)")
    X = 1
    while X <= cap // 2:
        f = lambda d: max([v for c, v in d.items() if h.get(c, cap + 1) > X], default=0.0)
        print(f"{X:5d}  {f(tot):11.5f}  {f(res):11.5f}  {f(cres):11.5f}")
        X *= 2
    top = sorted(res.items(), key=lambda t: -t[1])[:5]
    print("heaviest residual sums: (kappa, height, res, tot)")
    for c, v in top:
        print(f"  {c:9d}  h={h.get(c, cap + 1):6d}  {v:.5f}  {tot[c]:.5f}")


if __name__ == "__main__":
    main()
