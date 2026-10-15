# R229: S_6 on norm-one triples is a residue function of (a,b) mod 6; S_6 splits a single genus (prime p, chi=-1 words).
from math import gcd
import sys
sys.path.insert(0, 'scripts')
from review_r229_marking import words, P, inS
from review_r229_words import jacobi
bad = 0; used = 0
for a in range(6):
    for b in range(6):
        n = a * b - 1
        if gcd(n, 6) != 1: continue
        used += 1
        # membership depends only on (a,b) mod 6: entries are polynomials in a,b
        for A in range(a + 6, a + 61, 6):
            for Bb in range(b + 6, b + 61, 6):
                s = {inS(w, 6) for w in [(1, A + 1, Bb + 1), (A + 1, 1, Bb), (Bb + 1, 1, A)]}
                if len(s) > 1: bad += 1
print("S6 norm-one residue pairs coprime:", used, "disagreements:", bad)
# single prime with chi=-1 words both in and out of S6 (genus = chi at primes)
def isprime(p): return p > 1 and all(p % q for q in range(2, int(p**.5) + 1))
for p in range(5, 200):
    if not isprime(p): continue
    ws = [w for w in words(p) if jacobi(-(w[0]*w[1]-1), p) == -1]
    ins = [w for w in ws if inS(w, 6)]; outs = [w for w in ws if not inS(w, 6)]
    wp = [w for w in words(p) if jacobi(-(w[0]*w[1]-1), p) == 1]
    if ins and outs and any(inS(w, 6) for w in wp) and any(not inS(w, 6) for w in wp):
        print("p", p, "chi=-1 in/out", ins[0], outs[0], "chi=+1 in/out", [w for w in wp if inS(w,6)][0], [w for w in wp if not inS(w,6)][0]); break
