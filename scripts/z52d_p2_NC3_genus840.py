# Z3095: principal-genus representation of Mordell-hard primes by x^2 + f y^2, f | 840 (discriminants -4f | -3360).
# For each f | 840: h(-4f) (PARI quadclassunit), number of genera (2^(mu-1), mu from the prime divisors of 4f),
# and the fraction of primes p ≤ P, p ≡ 1 (mod 4), p = x^2 + f y^2 solvable, split by Mordell-hard (p mod 840 square class)
# vs the rest.  Genus theory predicts: if h(-4f) = #genera then principal genus = principal class and p is represented by
# x^2+fy^2 iff p lies in the principal genus, i.e. iff all genus characters of p are trivial.
import sys
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
from collections import Counter
P = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
HARD = {1, 121, 169, 289, 361, 529}
pr = [p for p in L.primes_upto(P) if p % 4 == 1 and p > 840]
sq = {(x*x) % 840 for x in range(840)}
hard = [p for p in pr if p % 840 in HARD]
rest = [p for p in pr if p % 840 not in HARD and p % 840 in sq]   # square mod 840 but not in the hard list
other = [p for p in pr if p % 840 not in sq]
def rep(p, f):
    # p = x^2 + f y^2 ?
    y = 0
    while f*y*y < p:
        r = p - f*y*y
        x = int(pari.sqrtint(r))
        if x*x == r: return True
        y += 1
    return False
mu_of = lambda n: len(pari.factor(n)[0])
for f in [d for d in range(1, 841) if 840 % d == 0]:
    D = -4*f
    cyc = [int(c) for c in pari(f"quadclassunit({D}).cyc")]
    h = 1
    for c in cyc: h *= c
    if f % 4 == 0 or f == 1: pass
    nclass_2rank = sum(1 for c in cyc if c % 2 == 0)
    genera = 2**(max(0, mu_of(4*f) - 1))
    if f in (1,): genera = 1
    fh = sum(rep(p, f) for p in hard[:400]) / max(1, len(hard[:400]))
    fo = sum(rep(p, f) for p in other[:400]) / max(1, len(other[:400]))
    if h <= 4 or fh > 0.5:
        print(f"f={f:4d} h(-4f)={h:3d} genera~{genera:2d} P(rep|hard)={fh:.3f}  P(rep|square-mod-840 non-hard)={sum(rep(p,f) for p in rest[:300])/max(1,len(rest[:300])):.3f}  P(rep|non-square)={fo:.3f}")
