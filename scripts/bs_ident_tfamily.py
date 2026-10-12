"""O145 (b): the Type I t-families for p = t^2+1 (BRAINSTORM/ident_form_families.md §3).
(t^2+1)^2 + 4m^2(m^2+1) = (t^2-2mt+2m^2+1)(t^2+2mt+2m^2+1).  With 4c^2 d = 4m^2(m^2+1) and
f = t^2 -+ 2mt + 2m^2+1, Type I needs f ≡ -p (mod 4cd), p = t^2+1.
For each m<=M, each admissible c, each sign: list t mod 4cd satisfying it, check the
resulting x,y,z solve 4/p (for all t<=T in the class, p prime or not), and record t mod 8."""
import sys
from math import gcd
from fractions import Fraction
M = int(sys.argv[1]) if len(sys.argv) > 1 else 8
T = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
bad = 0; fams = 0; tmod8 = set()
for m in range(1, M + 1):
    K = 4 * m * m * (m * m + 1)
    for c in range(1, 2 * m * m + 2):
        if K % (4 * c * c): continue
        d = K // (4 * c * c); Q = 4 * c * d
        for sg in (1, -1):
            cls = [t for t in range(Q) if ((t*t - 2*sg*m*t + 2*m*m + 1) + (t*t + 1)) % Q == 0]
            if not cls: continue
            fams += 1
            for t0 in cls:
                for t in range(t0 if t0 else Q, T, Q):
                    p = t * t + 1
                    if gcd(p, Q) > 1: continue  # not a prime case (p even or shares a factor with 4cd)
                    f = t*t - 2*sg*m*t + 2*m*m + 1
                    fp = (p * p + 4 * c * c * d) // f
                    a, b = (f + p) // Q, (fp + p) // Q
                    if (f + p) % Q or (fp + p) % Q or a <= 0 or b <= 0: bad += 1; continue
                    x, y, z = a * b * d * p, a * c * d, b * c * d
                    if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, p): bad += 1
                    tmod8.add(t % 8)
print(f"families with nonempty class set: {fams}; identity failures: {bad}; t mod 8 values seen: {sorted(tmod8)}")
print("p = t^2+1 ≡ 1 (mod 8) needs t ≡ 0 (mod 4):", "NEVER reached" if not ({0, 4} & tmod8) else "reached")
