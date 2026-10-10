"""O130 §3–§5 checks.
(A) Lemma 3.1 identity in (-d,-p) on all Type II solutions p<P (explicit quaternion multiplication).
(B) Fixed-(d,e) residual problem: among (p,d,e) with p prime < P, d<=Dm, e<=Em, 4d | pe+1 (Type I) resp. 4d | p+e
    (Type II), and the quaternionic/genus conditions satisfied, how often does the divisor condition
    'a | m, e | a+m/a' hold?  Also print explicit pairs with identical collision data mod e but opposite ES status.
Run: PYTHONPATH=scripts uv run python scripts/quat_residual.py [P]"""
import sys
from sympy import isprime, divisors, jacobi_symbol
from geo_common import es_solutions
from quat_typeI import abcd

P = int(sys.argv[1]) if len(sys.argv) > 1 else 1500


def qmul(x, y, A, B):
    """(x0+x1 i+x2 j+x3 k)(y...) in (-A,-B): i^2=-A, j^2=-B, k=ij, k^2=-AB."""
    a0, a1, a2, a3 = x; b0, b1, b2, b3 = y
    return (a0*b0 - A*a1*b1 - B*a2*b2 - A*B*a3*b3,
            a0*b1 + a1*b0 + B*(a2*b3 - a3*b2),
            a0*b2 + a2*b0 + A*(a3*b1 - a1*b3),
            a0*b3 + a3*b0 + a1*b2 - a2*b1)


nII = 0
for p in range(5, P):
    if not isprime(p):
        continue
    for sol in es_solutions(p):
        for perm in [(0, 1, 2), (1, 0, 2), (2, 0, 1)]:
            x, y, z = [sol[k] for k in perm]
            if x % p and y % p == 0 and z % p == 0:
                a, b, c, d = abcd(p, x, y//p, z//p)
                e = (a+b)//c
                assert qmul((0, 2*a, 1, 0), (0, 2*b, -1, 0), d, p) == (-e, 0, 0, -2*c*e)
                nII += 1
print(f"(A) Lemma 3.1 identity holds on all {nII} ordered Type II solutions, p<{P}")


def sqrt_m1_over_4d(d, e):  # exists r with 4 r^2 d = -1 mod e ?
    return any((4*r*r*d + 1) % e == 0 for r in range(e))


def good(m, e):
    return any((a + m//a) % e == 0 for a in divisors(m))


for typ in ("I", "II"):
    tot = ok = 0; ex = {}
    for p in range(5, P):
        if not isprime(p) or p % 24 != 1:
            continue
        for d in range(1, 13):
            if typ == "I" and jacobi_symbol((-d) % p, p) != -1:
                continue
            for e in range(1, 60):
                num = p*e + 1 if typ == "I" else p + e
                if num % (4*d) or not sqrt_m1_over_4d(d, e) if typ == "I" else num % (4*d):
                    continue
                if typ == "II" and not any((4*r*r*d + p) % e == 0 for r in range(e)):
                    continue
                m = num // (4*d); g = good(m, e)
                tot += 1; ok += g
                ex.setdefault((d, e), {}).setdefault(g, p)
    pairs = [(k, v[True], v[False]) for k, v in ex.items() if len(v) == 2][:6]
    print(f"(B) Type {typ}, p=1(24)<{P}, d<=12, e<60, collision/genus data OK: divisor condition holds in {ok}/{tot}")
    print("    (d,e): p with ES at (d,e), p' without:", pairs)
