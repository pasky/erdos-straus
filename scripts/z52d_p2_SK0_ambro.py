"""Z0243 (pass 2, SK0): Ambro–Barcau (arXiv:1412.3263) Thm 0.2(b) specialised to 4/p = sum of 3 unit fractions.
Thm 0.2(b) (as read from the arXiv PDF; the fraction in the PDF text is garbled -- we take u_{floor(d)+1,q}/(q(1-{d})),
which is the reading that gives equality for k=1, m=q): for 1<=m1<=...<=mk, d>=-1, qd in Z, sum 1/m_i = k-d
=> lcm(m_i) <= u_{floor(d)+1,q} / (q(1-{d})),  u_{1,q}=q, u_{p+1,q}=u_{p,q}(u_{p,q}+1).
For 4/p = sum of three unit fractions: k=3, d=3-4/p, q=p (q*d integer for odd p), so
   lcm(x,y,z) <= u_{3,p}/4 = p(p+1)(p^2+p+1)/4.
Check: for all primes p<=PMAX enumerate all reps x<=y<=z and compare the max lcm with the bound.
Also: equality cases in the theorem are d = s-1/q or d = 2-r/q; 4/p gives d = 3-4/p (s=3, r=4), so equality is not claimed."""
import sys, math
from fractions import Fraction as F
from sympy import primerange
PMAX = int(sys.argv[1])
def reps(p):
    out = []; t = F(4, p); x = -(-p // 4)
    while x <= 3 * p // 4 + 1:
        r = t - F(1, x)
        if r > 0:
            for y in range(max(x, math.floor(1 / r) + 1), math.floor(2 / r) + 1):
                r2 = r - F(1, y)
                if r2 > 0 and r2.numerator == 1 and r2.denominator >= y:
                    out.append((x, y, r2.denominator))
        x += 1
    return out
worst = []; cnt = 0; viol = []
for p in primerange(3, PMAX + 1):
    bound = F(p * (p + 1) * (p * p + p + 1), 4)
    R = reps(p)
    if not R: viol.append((p, 'no reps')); continue
    cnt += 1
    for (x, y, z) in R:
        L = math.lcm(x, y, z)
        if L > bound: viol.append((p, x, y, z, L))
    best = min(math.lcm(*r) for r in R)
    worst.append((float(best / bound), p, best, float(bound)))
print("primes checked:", cnt, "violations:", viol[:5], len(viol))
print("min over reps of lcm / bound, worst five (ratio, p, min-lcm, bound):")
for w in sorted(worst)[-5:]: print(w)
print("ratio of max-lcm over reps to bound, five largest:")
