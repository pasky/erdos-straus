"""O149: residue-class bias of f(p) = f_I+f_II versus the (p mod q)-independence of all local data of U_p.
Prints mean f/log^3 p over primes in [LO,HI] split by Legendre symbol (p/q), q=3,5,7, and by p mod 8.
Also a parity table of f_I, f_II on primes p ≡ 9 (mod 2^K) (l-adic continuity probe at the odd square 9)."""
import sys
from math import log
from bs_padic_counts import spf_sieve, counts

LO, HI = int(sys.argv[1]), int(sys.argv[2])
spf = spf_sieve(HI)
ps = [q for q in range(max(LO, 5), HI + 1) if spf[q] == q]
data = {p: counts(p, spf) for p in ps}
def leg(a, q):
    r = pow(a % q, (q - 1) // 2, q); return 0 if r == 0 else (1 if r == 1 else -1)
for q in (3, 5, 7, 11, 13):
    for s in (1, -1):
        v = [(fi + fii) / log(p)**3 for p, (fi, fii) in data.items() if leg(p, q) == s]
        print(f"(p/{q})={s:+d}: n={len(v)} mean f/log^3={sum(v)/len(v):.4f} min={min(v):.4f}")
for r in (1, 3, 5, 7):
    v = [(fi + fii) / log(p)**3 for p, (fi, fii) in data.items() if p % 8 == r]
    print(f"p≡{r} mod 8: n={len(v)} mean={sum(v)/len(v):.4f}")
v = [(fi + fii) / log(p)**3 for p, (fi, fii) in data.items() if p % 840 in (1, 121, 169, 289, 361, 529)]
w = [(fi + fii) / log(p)**3 for p, (fi, fii) in data.items() if p % 840 not in (1, 121, 169, 289, 361, 529)]
print(f"square classes mod 840: n={len(v)} mean={sum(v)/len(v):.4f}; others n={len(w)} mean={sum(w)/len(w):.4f}")
for K in range(3, 9):
    M = 2**K
    sel = [(p, data[p]) for p in ps if p % M == 9 % M]
    par = sorted(set((fi % 2, fii % 2) for p, (fi, fii) in sel))
    print(f"K={K}: #p≡9 mod 2^K = {len(sel)}, parities (fI,fII) seen: {par}")
