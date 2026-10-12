"""O145 (b): constant-level Type I t-families for P = t^2 + k (memo ident_form_families §3).
(t^2+k)^2 + 4m^2(m^2+k) = (t^2-2mt+2m^2+k)(t^2+2mt+2m^2+k); c^2 d = m^2(m^2+k); need f ≡ -p (mod 4cd).
For k<=KMAX, m<=MMAX: does any family class contain t with p=t^2+k Mordell-hard
(p ≡ 1 mod 24, square mod 5 and 7) and gcd(p,4cd)=1 ?  Reports reaching families, with an example
verified as an actual solution of 4/p for a PRIME p."""
import sys
from math import gcd, lcm
from fractions import Fraction
from sympy import isprime
KMAX = int(sys.argv[1]); MMAX = int(sys.argv[2])
def hard(p): return p % 24 == 1 and p % 5 in (1, 4) and p % 7 in (1, 2, 4)
tot = reach = 0
for k in range(1, KMAX + 1):
    for m in range(1, MMAX + 1):
        K = 4 * m * m * (m * m + k)
        for c in range(1, 2 * m * (m + k) + 2):
            if K % (4 * c * c): continue
            d = K // (4 * c * c); Q = 4 * c * d; L = lcm(Q, 840)
            for sg in (1, -1):
                ok = [t for t in range(L) if (2 * (t*t - sg*m*t + m*m + k)) % Q == 0
                      and gcd(t*t + k, Q) == 1 and hard((t*t + k) % L + L)]
                tot += 1
                if not ok: continue
                reach += 1; ex = None
                for t0 in ok:
                    for t in range(t0 + L, t0 + 200 * L, L):
                        p = t*t + k
                        if not isprime(p): continue
                        f = t*t - 2*sg*m*t + 2*m*m + k; fp = (p*p + 4*c*c*d) // f
                        a, b = (f + p) // Q, (fp + p) // Q
                        x, y, z = a*b*d*p, a*c*d, b*c*d
                        assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p)
                        ex = (t, p); break
                    if ex: break
                print(f"k={k} m={m} c={c} d={d} sign={sg}: {len(ok)} hard t-classes mod {L}; prime example {ex}")
print(f"families tested {tot}, reaching Mordell-hard primes {reach}")
