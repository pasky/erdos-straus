# z70 CLASS: what carries the order-2 overlap A2 = O(T_d) for d > 1 (the FIX-CS control failure for d = 2, §1.10)?
# Every ordered pair (g, g + T_d) of good classes is classified:
#   realised by an ideal identity R_E(sigma1) = D_d * R_A(sigma2) between natural representatives (R_E(sigma1) = D_d conj E_1,
#   so this says: the A-ideal of sigma2 is the ideal (e1, 2 b1 d + sqrt(-dn)), A2 = e1, a2 == b1 (mod e1)), split into
#   CS  : a2 == b1 (the same fibre: Lemma CS seen from the b-side) and XID : a2 != b1 (a cross-fibre identity);
#   (the mirror identity with the B-representative conj(B, 2bd + sqrt) counts as XID too);
#   OTHER : no such identity.
# Usage: python scripts/z70_class_a2check.py d range P0 P1
import sys, math
sys.path.insert(0, 'scripts')
from collections import Counter
from sympy import primerange
from z69_twist_i17 import reduce
from z70_class_core import Fact, ClassData, solutions
from z70_class_repid import vec_of
d = int(sys.argv[1]); nl = [p for p in primerange(int(sys.argv[3]), int(sys.argv[4])) if p % 8 == 1]   # argv[2] = "range"
F = Fact(max(nl)//3 + 10); tot = Counter()
for n in nl:
    sols = solutions(n, d, F)
    if not sols or any(math.gcd(x, d*n) > 1 for (a, b, c, e) in sols for x in (e, 4*a*c*d - 1, 4*b*c*d - 1)): continue
    C = ClassData(n, d); G = C.G; reps = {}; csfib = {}
    for (a, b, c, e) in sols:
        A = 4*a*c*d - 1; g = G.coords[reduce(A, 4*a*d, d*e)]
        B = 4*b*c*d - 1
        reps.setdefault(g, []).append((vec_of(C, F, A, 2*a*d), vec_of(C, F, e, 2*a*d, conj=True, D=True), a, b,
                                       vec_of(C, F, B, 2*b*d, conj=True)))
    for g in reps:
        y = G.add(g, C.Td)
        if y not in reps or y == g: continue
        tot['A2'] += 1; kind = 'OTHER'
        for (RA1, RE1, a1, b1, RB1) in reps[g]:
            for (RA2, RE2, a2, b2, RB2) in reps[y]:
                if RE1 == dict(RB2, D=1) or RE2 == dict(RB1, D=1): kind = 'XID' if kind == 'OTHER' else kind
                if RE1 == dict(RA2, D=1):
                    if a2 == b1: kind = 'CS'; break
                    kind = 'XID'
                if RE2 == dict(RA1, D=1):
                    if a1 == b2: kind = 'CS'; break
                    kind = 'XID'
            if kind == 'CS': break
        tot[kind] += 1
print(f"# a2check d={d} [{sys.argv[3]},{sys.argv[4]}): ordered A2 pairs {tot['A2']}: CS {tot['CS']}, cross-fibre identity XID {tot['XID']}, OTHER {tot['OTHER']}")
