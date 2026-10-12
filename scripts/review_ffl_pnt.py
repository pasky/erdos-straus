"""R161: numerical sanity check of Fact 5.2 (explicit PNT in progressions):
|pi(n; M, r) - q^n/(n Phi(M))| <= (D + 2) q^{n/2} / n  for all units r mod M.
"""
from collections import Counter
from review_ffl_poly import PolyRing

cases = [(2, "1011", range(4, 15)), (2, "11000", range(5, 14)), (3, "101", range(3, 10)), (3, "1100", range(4, 10)),
         (5, "1001", range(4, 7)), (4, "10010", range(3, 7))]
worst = 0.0
for q, Ms, ns in cases:
    R = PolyRing(q)
    M = R.parse(Ms)
    D = R.deg(M)
    units = [r for r in R.polys_below(D) if r and R.gcd(r, M) == (1,)]
    Phi = len(units)
    for n in ns:
        cnt = Counter(R.mod(P, M) for P in R.irreducibles(n))
        main = q ** n / (n * Phi)
        bound = (D + 2) * q ** (n / 2) / n
        ratio = max(abs(cnt.get(r, 0) - main) for r in units) / bound
        worst = max(worst, ratio)
        assert ratio <= 1.0, (q, Ms, n, ratio)
    print(f"q={q} M={Ms} D={D} Phi={Phi}: max |error|/bound over n in {list(ns)[0]}..{list(ns)[-1]}: ok", flush=True)
print("worst ratio", round(worst, 3))
