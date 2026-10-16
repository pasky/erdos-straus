"""O249 (ASTRA_BRIDGE Prop 5.2): for primes p = 1 (4) <= P:
 (b) least admissible prime q0 (q = 3 mod 4, (q/p) = -1); least-root window shot Q = (even root of -p mod q0)/2,
     G = (p+4Q^2)/q0, K = (G+1)/4, U = (p+q0)/4; point (U, pK, pUK/Q^2): check 4/p exactly, den z = Q1^2,
     Q1 = Q/gcd(Q,K) <= (q0-1)/2;  also min over admissible q <= QM of Q1 (twist 1 = ES square shot).
 (a) least prime m in a root class of p m^2 = -1 (mod q0) with m not dividing p h: Astra source with prime twist,
     check 4/p = m^2/(sh) + 1/(psh) + 1/(ph) and den x = m^2 exactly.
Usage: z21_phase.py P QM
"""
import sys
from fractions import Fraction as F
from math import gcd, isqrt
from sympy import primerange, isprime

P, QM = int(sys.argv[1]), int(sys.argv[2])
adm_cache = list(primerange(3, max(QM, 2000) + 1))
st = dict(n=0, maxq0=0, maxQ1=0, es_sq=0)
mintw_hist = {}
for p in primerange(5, P + 1):
    if p % 4 != 1:
        continue
    st['n'] += 1
    best = None
    q0 = None
    for q in adm_cache:
        if q % 4 != 3 or q == p or pow(p % q, (q - 1) // 2, q) != q - 1:
            continue
        if q0 is None:
            q0 = q
        if q > QM and q0 is not None:
            break
        root = next(z for z in range(1, q) if (z * z + p) % q == 0)
        z = root if root % 2 == 0 else q - root
        Q = z // 2
        if Q % p == 0:
            continue  # gcd(Q,p)=1 needed (automatic for q < 2p)
        G = (p + 4 * Q * Q) // q
        assert (p + 4 * Q * Q) % q == 0 and G % 4 == 3
        K, U = (G + 1) // 4, (p + q) // 4
        pt = (F(U), F(p * K), F(p * U * K, Q * Q))
        assert sum(1 / x for x in pt) == F(4, p)
        Q1 = Q // gcd(Q, K)
        assert pt[2].denominator == Q1 * Q1 and Q1 <= (q - 1) // 2, (p, q, Q, K, U, pt[2])
        if q == q0:
            st['maxq0'] = max(st['maxq0'], q0)
            st['maxQ1'] = max(st['maxQ1'], Q1)
            h = (q + 1) // 4
            r0 = next(m for m in range(1, q) if (p * m * m + 1) % q == 0)
            m = None
            for base in (r0, q - r0):
                mm = base
                while not (isprime(mm) and (p * h) % mm):
                    mm += q
                m = mm if m is None else min(m, mm)
            s = (p * m * m + 1) // q
            x = F(s * h, m * m)
            assert x.denominator == m * m and F(4, p) == 1 / x + F(1, p * s * h) + F(1, p * h)
        best = Q1 if best is None else min(best, Q1)
    mintw_hist[best] = mintw_hist.get(best, 0) + 1
    st['es_sq'] += (best == 1)
print(st)
print('min least-root twist over admissible q <=', QM, ':', dict(sorted(mintw_hist.items())[:15]))
