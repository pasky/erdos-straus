# z70 GEN — validation of the small-fibre engine against the exhaustive z70_class_core.solutions (O(n) engine),
# of the class dictionary, genus target, natural representatives and FR' on small inputs.
import sys
sys.path.insert(0, 'scripts')
import z70_gen_core as C
import z70_class_core as K
from sympy import isprime

def check(n, d, F):
    s1 = C.solutions(n, d)
    s2 = set(K.solutions(n, d, F))
    assert s1 == s2, (n, d, len(s1), len(s2), sorted(s1 ^ s2)[:5])
    if not isprime(n): return len(s1), None
    CG = C.ClassGroup(n, d); Gn = C.Genus(CG)
    G = set()
    for s in s1:
        g = C.good_class(n, d, s); G.add(g)
        a, b, c, e = s
        gb = C.good_class(n, d, (b, a, c, e))
        assert CG.neg(CG.vec(g)) == CG.vec(gb)
        assert Gn.of(CG.vec(g)) == Gn.target, (n, d, Gn.chars, Gn.of(CG.vec(g)), Gn.target)
        for (N, r) in C.natural_reps(n, d, s):
            assert C.ideal_form(n, d, N, r) == g
    T = [v for v in CG.byvec if Gn.of(v) == Gn.target]
    ng = len({Gn.of(v) for v in CG.byvec})
    sq = {CG.sqclass(v) for v in CG.byvec}
    assert len(T) * ng == CG.h and ng == len(sq), (n, d, len(T), ng, len(sq))
    return len(s1), (CG.h, CG.cyc, len(G), len(T), Gn.chars)

F = K.Fact(200000)
cnt = 0
ns = [73, 409, 577, 1201, 2521, 3361, 5569, 9601, 21841, 23929, 37, 1621, 97, 193, 105, 33, 4545, 9, 25, 225, 1105, 12301]
for n in ns:
    for d in (1, 2, 3, 5, 7):
        if n % d == 0 and d > 1: continue
        out = check(n, d, F); cnt += 1
        print(n, d, out)
import random
random.seed(70)
ps = [p for p in range(10001, 60000, 24) if isprime(p)]
for p in random.sample(ps, 30):
    for d in (1, 2, 3, 5, 7):
        check(p, d, F); cnt += 1
print('OK', cnt, 'checks')
