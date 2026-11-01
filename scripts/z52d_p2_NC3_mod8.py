# Z2782 (slot lemma as Gauss-Milgram/van der Blij) — concrete first test: is the sign (A/p) of a word a function of
# (t,u,v) mod 8 together with p mod 8?  Also: is it a function of (t,u,v) mod 4 (+p mod 8)?  Words of all primes p = 1 (8), p<=P.
import sys
from collections import defaultdict
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
P = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
for mod in (4, 8):
    table = defaultdict(set)
    for p in L.primes_upto(P):
        if p < 17 or p % 8 != 1: continue
        for (t, u, v) in L.words(p):
            table[(p % 8, t % mod, u % mod, v % mod)].add(L.legendre(t*u-1, p))
    incons = sum(1 for k, s in table.items() if len(s) > 1)
    print(f"mod {mod}: classes {len(table)}, classes with both signs: {incons}")
# sign as a function of the residues of p, A, A* mod 8 (A = tu-1, A* = tv-1)
t2 = defaultdict(set)
for p in L.primes_upto(P):
    if p < 17 or p % 8 != 1: continue
    for (t, u, v) in L.words(p):
        A = t*u-1; As = t*v-1
        t2[(p % 8, t % 8, A % 8, As % 8)].add(L.legendre(A, p))
print("mod-8 of (p,t,A,A*): classes", len(t2), "inconsistent", sum(1 for s in t2.values() if len(s) > 1))
