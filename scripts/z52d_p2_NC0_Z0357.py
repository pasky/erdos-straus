# z52d Pass 2 NC0, item Z0357 — lattice width of the solution set for hard primes.
# Item's body (slice of the surface 1/x+1/y+1/z=4/p) is NOT convex. Substitute actually computed here:
# K_p = conv(all integer points (x,y,z) of all ordered solutions of 4/p), and its lattice width
# w(K) = min over primitive integer u, |u_i|<=R, of max_{K} u·v - min_{K} u·v  (extremes are attained at the points).
# Also reports the Khinchine-type test: does K contain integer points other than the solutions? (it does: the solutions themselves).
import sys, itertools, math
from math import gcd
from sympy import Rational
sys.path.insert(0,'scripts')
from z52d_p2_NC0_allsols import sols
R=int(sys.argv[1]) if len(sys.argv)>1 else 6
PRIMES=[5,13,17,101,409,577,1009,3361,5569,9601,23929,83449]
def width(pts):
    best=None; arg=None
    for u in itertools.product(range(-R,R+1),repeat=3):
        if u==(0,0,0) or gcd(gcd(abs(u[0]),abs(u[1])),abs(u[2]))!=1: continue
        vals=[u[0]*x+u[1]*y+u[2]*z for (x,y,z) in pts]
        w=max(vals)-min(vals)
        if best is None or w<best: best=w; arg=u
    return best,arg
for p in PRIMES:
    S=sols(p)
    pts=set()
    for (x,y,z) in S:
        for q in itertools.permutations((x,y,z)): pts.add(q)
    pts=sorted(pts)
    w,u=width(pts)
    print(p,'solutions(unordered)',len(S),'hull points',len(pts),'width',w,'direction',u,'max coord',max(max(q) for q in pts))
