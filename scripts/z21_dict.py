"""O249 (ASTRA_BRIDGE §3): exact checks of the source/shot/slice dictionary.
For primes p = 1 (4) <= P, admissible primes q = 3 (4), (q/p) = -1, q <= QM, and all lifts m <= LM of the two
root classes of p m^2 = -1 (mod q):
 (1) Astra identity 4/(pm^2) = 1/(sh) + 1/(Nsh) + 1/(Nh) exactly (Fractions);
 (2) even m: s = -1 (mod 2m)  <=>  m | (q+1)/2 ("ES-ready"), and then the EXPONENT_CAP Prop 1.3 (Q1 = 1, k = m/2,
     D = s, g = q) solution is an exact ES solution with y = p h;
 (3) genuine (gcd(m,h)=1) and m even > 2 => never ES-ready;
 (4) slice criterion: ES with y = p h  <=>  some d | (p h)^2 with d = -p h (mod q); and -p h = (2m)^{-2} (mod q).
Usage: z21_dict.py P QM LM
"""
import sys
from fractions import Fraction as F
from math import gcd
from sympy import primerange, isprime, factorint, divisors

P, QM, LM = (int(a) for a in sys.argv[1:4])
cnt = dict(src=0, even=0, ready=0, ready_ok=0, genuine_even_ready=0, slice_es=0, slice_checked=0)
for p in primerange(5, P + 1):
    if p % 4 != 1:
        continue
    for q in primerange(3, QM + 1):
        if q % 4 != 3 or q == p or pow(p, (q - 1) // 2, q) != q - 1:  # (p/q) = -1  <=>  (-p/q) = 1
            continue
        h = (q + 1) // 4
        roots = [m for m in range(1, q) if (p * m * m + 1) % q == 0]
        assert len(roots) == 2
        # (4) slice criterion, once per (p,q)
        tgt = (-p * h) % q
        for m in roots:
            assert tgt == pow(2 * m, -2, q)
        cnt['slice_checked'] += 1
        ph = p * h
        crit = any(d % q == tgt for d in divisors(ph * ph))
        brute = False
        for d in divisors(ph * ph):          # q/(ph) = 1/x + 1/z  <=>  x = (ph+d)/q, z = ph x / d
            if (ph + d) % q == 0:
                x = (ph + d) // q
                if (ph * x) % d == 0:
                    z = ph * x // d
                    assert F(4, p) == F(1, x) + F(1, ph) + F(1, z)
                    brute = True
        assert crit == brute
        cnt['slice_es'] += brute
        for m0 in roots:
            for m in range(m0, LM + 1, q):
                N = p * m * m
                s = (N + 1) // q
                assert F(4, N) == F(1, s * h) + F(1, N * s * h) + F(1, N * h)
                cnt['src'] += 1
                if m % 2:
                    continue
                cnt['even'] += 1
                ready = ((q + 1) // 2) % m == 0
                assert ready == ((s + 1) % (2 * m) == 0)
                if ready:
                    cnt['ready'] += 1
                    if gcd(m, h) == 1 and m > 2:
                        cnt['genuine_even_ready'] += 1
                    k, D, g = m // 2, s, q
                    j = (D + 1) // k
                    assert (D + 1) % k == 0 and (4 * k * p + j) % (4 * D) == 0
                    Q0 = (4 * k * p + j) // (4 * D)
                    assert g == 4 * Q0 * k - 1 and (p + 4 * Q0 * Q0) % g == 0
                    if gcd(Q0, p) != 1:
                        continue
                    mc = (p + 4 * Q0 * Q0) // g
                    x, y = (p + mc) // 4, p * (g + 1) // 4
                    z = F(p * x * (g + 1), 4 * Q0 * Q0)
                    assert (p + mc) % 4 == 0 and z.denominator == 1 and y == p * h
                    assert F(4, p) == F(1, x) + F(1, y) + 1 / z
                    cnt['ready_ok'] += 1
print(cnt)
