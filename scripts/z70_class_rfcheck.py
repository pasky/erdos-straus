# z70 CLASS Remark RF check: a class g contains a good form [A, B*, dE] (Type II, any A) iff some primitive form [A, B, C] of g
# has B == B* (mod 2A) for a positive B* == 0 (mod 4d) dividing A + 1.  For A < sqrt(dn) that form is the REDUCED form of g
# (or of g^-1).  Check: G_small := {g in G : g has a natural representative of norm < sqrt(dn)} equals
#   R := {reduced forms [A, B, C] (A < sqrt(dn)) with B == B* (mod 2A), 0 < B* == 0 (mod 4d), B* | A + 1}.
import sys, math
sys.path.insert(0, 'scripts')
from sympy import primerange, divisors
from z69_twist_i17 import reduce, classgroup_elems
from z70_class_core import Fact, solutions
d = int(sys.argv[1]); nl = [p for p in primerange(int(sys.argv[2]), int(sys.argv[3])) if p % 8 == 1]
F = Fact(max(nl)//3 + 10); agree = tot = extraR = extraG = 0
for n in nl:
    D = -4*d*n; lim = math.isqrt(d*n)
    Gs = set()
    for (a, b, c, e) in solutions(n, d, F):
        A, B = 4*a*c*d - 1, 4*b*c*d - 1
        g = reduce(A, 4*a*d, d*e)
        if min(A, B, d*e) < lim: Gs.add(g)
    R = set()
    for (A, Bf, C) in classgroup_elems(D):
        if A >= lim: continue
        for Bs in divisors(A + 1):
            if Bs % (4*d) == 0 and (Bf - Bs) % (2*A) == 0: R.add((A, Bf, C))
    # G_small also contains classes whose small natural rep is B or de (they are good via the inverse / the e-side form);
    # compare R with the set of good classes whose reduced form has first coefficient = some natural A-norm < lim
    GA = set()
    for (a, b, c, e) in solutions(n, d, F):
        A = 4*a*c*d - 1
        if A < lim: GA.add(reduce(A, 4*a*d, d*e))
    tot += 1; agree += (GA == R); extraR += len(R - GA); extraG += len(GA - R)
print(f"# rfcheck d={d} [{sys.argv[2]},{sys.argv[3]}): primes {tot}; R == G_A (good classes with natural A < sqrt(dn)) at {agree}; |R - G_A| = {extraR}, |G_A - R| = {extraG}")
