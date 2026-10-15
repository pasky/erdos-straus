"""R244 from-scratch Sq^x screen for c0*4^s + k (tests CONJECTURE E / Lemma 3.1 consistency).

For a period L and all odd primes q <= QMAX with ord_q(4) | L, a residue s mod L is killed if (n_s/q) != +1
(n_s = c0*4^s + k mod q, including n_s = 0). A residue surviving all q is a candidate Lambda ∩ Sq^x point
(projection); residues with no survivor PROVE Lambda ∩ Sq^x = ∅ (given k ≡ 1 mod 8). Prints survivors.
usage: review_r244_sqscreen.py C0MAX KMAX L QMAX
"""
import sys
import numpy as np
import sympy as sp


def main():
    C0MAX, KMAX, L, QMAX = map(int, sys.argv[1:5])
    qs = []
    for q in sp.primerange(3, QMAX):
        o = int(sp.n_order(4, q))
        if L % o == 0:
            qs.append((q, o))
    print(f'L={L}: {len(qs)} primes q<={QMAX} with ord_q(4) | L')
    s = np.arange(L)
    for c0 in range(1, C0MAX + 1):
        if c0 % 4 == 0:
            continue
        for k in range(1, KMAX + 1, 8):  # k ≡ 1 mod 8
            if (c0 + k) % 3 == 2 or sp.gcd(c0, k) > 1:
                continue
            alive = np.ones(L, bool)
            for q, o in qs:
                pw = np.array([pow(4, i, q) for i in range(o)], dtype=np.int64)
                v = (c0 * pw + k) % q
                qr = np.array([x != 0 and pow(int(x), (q - 1) // 2, q) == 1 for x in v])
                alive &= qr[s % o]
                if not alive.any():
                    break
            surv = [int(x) for x in np.nonzero(alive)[0]]
            from fractions import Fraction
            from math import isqrt
            def issq(x):
                v = Fraction(c0) * Fraction(4) ** x + k
                return isqrt(v.numerator) ** 2 == v.numerator and isqrt(v.denominator) ** 2 == v.denominator
            surv = [x for x in surv if not (issq(x) or issq(x - L))]
            unit = any(c0 * 4 ** 0 + k == 4 ** j for j in range(20))
            if len(surv) or unit:
                print(f'c0={c0} k={k} c0+k=4^j:{unit} survivors={len(surv)} {surv[:6]}')


if __name__ == '__main__':
    main()
