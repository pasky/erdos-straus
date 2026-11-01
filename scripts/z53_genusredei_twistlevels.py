# Levels of the formal-Lemma-P classes (Z53_GENUSREDEI §6.3) for the primes listed in the X=100 scan file.
import sys; sys.path.insert(0, 'scripts')
import z53_genusredei_twist as Z
from sympy import factorint
from collections import Counter
fn = sys.argv[1] if len(sys.argv) > 1 else 'data/z53/genusredei/twist_X100_1e7_1.04e7.txt'
X = 100; cnt = {k: Counter() for k in ("R", "Q", "prot")}
rows = [l.split()[0] for l in open(fn) if not l.startswith('#')]
for ps in rows:
    p = int(ps)
    for C in range(1, X + 1):
        t = 4 * C; N = 4 * C * p + 1; f = factorint(N)
        if (t - 1) not in Z.sigma(list(f.items()), t): continue
        smooth = [(q, e) for q, e in f.items() if q <= X]; rest = 1
        for q, e in f.items():
            if q > X: rest = rest * pow(q, e, t) % t
        Sm = Z.sigma(smooth, t)
        if (t - 1) in Sm or (t - 1) in {x * rest % t for x in Sm}: continue
        tw = [q for q, e in f.items() if q > X and e == 1]; sm = [(q, e) for q, e in f.items() if not (q > X and e == 1)]
        Ss = Z.sigma(sm, t); g = 1
        for q in tw: g = g * q % t
        if (t - 1) in Ss or (t - 1) in {x * g % t for x in Ss}: cnt["R"][C] += 1; continue
        r = Z.exact_twist(t, Ss, [q % t for q in tw], cap=10**6)
        cnt["Q" if r is False else "prot"][C] += 1
print("R (decided by repeated large prime) levels C:", sorted(cnt["R"].items()))
print("Q (quadratic-image-determined) levels C:", sorted(cnt["Q"].items()), "total", sum(cnt["Q"].values()))
print("protected levels C:", sorted(cnt["prot"].items()), "total", sum(cnt["prot"].values()))
