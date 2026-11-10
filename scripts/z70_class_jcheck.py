# z70 CLASS: check of Corollary J (Z70_CLASS.md §1.6): for d = 1, every pair g, g + J in G_1(n) (J = [2, 2, (n+1)/2]) has
# 2 m(g) m(g+J) >= n, m = least norm among the natural representatives (A, B, e) of the class (all odd).
import sys
sys.path.insert(0, 'scripts')
from sympy import primerange
from z69_twist_i17 import reduce
from z70_class_core import Fact, ClassData, solutions
nl = [p for p in primerange(int(sys.argv[1]), int(sys.argv[2])) if p % 8 == 1]
F = Fact(max(nl)//3 + 10); pairs = viol = classes = 0; smallJ = 0
for n in nl:
    C = ClassData(n, 1); G = C.G; m = {}
    for (a, b, c, e) in solutions(n, 1, F):
        g = G.coords[reduce(4*a*c - 1, 4*a, e)]
        m[g] = min(m.get(g, 10**30), 4*a*c - 1, 4*b*c - 1, e)
    J = G.coords[reduce(2, 2, (n + 1)//2)]
    classes += len(m)
    for g in m:
        y = G.add(g, J)
        if y in m:
            pairs += 1
            if 2*m[g]*m[y] < n: viol += 1
    smallJ += sum(1 for g in m if 2*m[g]*m[g] < n)
print(f"# jcheck d=1 p==1(8) in [{sys.argv[1]},{sys.argv[2]}): primes {len(nl)}, good classes {classes}, J-overlap pairs {pairs}, violations of 2 m m' >= n: {viol}; classes with 2 m^2 < n: {smallJ}")
