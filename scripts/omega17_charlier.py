"""O68 / POINTWISE_OMEGA17 Prop 3.1(iv): least integer R with 1-C_n(j;R) >= 0 for 1<=j<=4R+6n+20
(exact rationals; n odd). n<=25 by linear scan, n in {31,41,61,81} by bisection."""
from fractions import Fraction as Fr
from math import comb
def C(n,x,a):
    s=Fr(0); ff=Fr(1)
    for r in range(n+1):
        s+=comb(n,r)*(-1)**r*ff/Fr(a)**r
        ff*= (x-r)
    return s
for n in [1,3,5,7,9,11,13,15,17,21,25]:
    # minimal integer R with 1-C_n(j;R)>=0 for all 1<=j<=J
    for R in range(1,400):
        J=int(4*R+6*n+20)
        vals=[1-C(n,j,R) for j in range(1,J+1)]
        if min(vals)>=0:
            mx=max(vals[:int(2*R)])
            print(f"n=k+1={n:3d}  R_min={R:4d}  R_min/n={R/n:.2f}  max psi on j<=2R: {float(mx):.3f}",flush=True)
            break

def ok(n, R):
    J = int(4 * R + 6 * n + 20)
    return all(1 - C(n, j, R) >= 0 for j in range(1, J + 1))

for n in [31, 41, 61, 81]:
    lo, hi = n, 8 * n
    assert ok(n, hi)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if ok(n, mid):
            hi = mid
        else:
            lo = mid
    print(f"n={n:3d}  R_min={hi:4d}  R_min/n={hi/n:.3f} (bisection)", flush=True)
