"""O132 check: can p | e occur in a Type I solution 4abd = pe+1, a+b = ce, gcd(c,p)=1?
(QUATERNION_ES Prop 1.3's ramification-at-p step needs v_p(dpe) odd.)
Enumerate via ef = 4a^2 d + 1 with p | e, f = 4acd - p >= 1.
Result: no hits (p < 60, a, d < 4p). Proof that p never divides e: e | 4a^2 d + 1 would give (-d/p) = +1,
contradicting the Type I genus condition (-d/p) = -1 (GEOMETRY_ES Prop 5.1)."""
import sys
from sympy import primerange, divisors
P = int(sys.argv[1]) if len(sys.argv) > 1 else 60
R = int(sys.argv[2]) if len(sys.argv) > 2 else 4
hits = 0
for p in primerange(3, P):
    for a in range(1, R*p):
        for d in range(1, R*p):
            N = 4*a*a*d + 1
            if N % p: continue
            for e in divisors(N):
                if e % p: continue
                f = N // e
                if (f + p) % (4*a*d): continue
                c = (f + p)//(4*a*d)
                b = c*e - a
                if b < 1 or c % p == 0: continue
                assert 4*a*b*d == p*e + 1
                hits += 1
                if hits <= 5: print("p|e:", p, dict(a=a, b=b, c=c, d=d, e=e))
print("hits with p|e:", hits)
