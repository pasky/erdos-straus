# Z3090: candidate invariants of p from level data, for large primes (sample), via the exact level identity
# (scripts/z52d_p2_NC3_levels.py): level 4C words <-> divisors of 4Cp+1.  Candidates:
#   minC(p)  = least C <= CMAX with a level-4C word (CMAX+1 if none);  N(p) = number of level-4C words, C <= CMAX;
#   class(p) = p mod 840 (square class = Mordell-hard).  We report distributions by size and by class, and the primes with no
#   word for C <= CMAX (candidate 'hard' primes for this scan).
import sys, random
from sympy import isprime, divisors
from sympy.ntheory import factorint
from collections import Counter
random.seed(7)
CMAX = 10
HARD = {1, 121, 169, 289, 361, 529}
def divs_fast(N):
    f = factorint(N)
    ds = [1]
    for q, e in f.items():
        ds = [d * q**k for d in ds for k in range(e+1)]
    return ds
def has_words(p, C):
    t = 4*C; N = t*p + 1
    cnt = 0
    for A in divs_fast(N):
        if A % t != t-1 or A < 2*t-1: continue
        B = N // A
        if B % t != t-1 or B < 2*t-1: continue
        cnt += 1
    return cnt
if __name__ == '__main__':
    rows = []
    for lo, hi, m in [(10**6, 10**7, 3000), (10**7, 10**8, 3000), (10**8, 10**9, 1500)]:
        got = 0
        while got < m:
            p = random.randrange(lo, hi)
            if p % 24 != 1 or not isprime(p): continue
            got += 1
            counts = [has_words(p, C) for C in range(1, CMAX+1)]
            minC = next((C for C in range(1, CMAX+1) if counts[C-1] > 0), CMAX+1)
            rows.append((lo, p, minC, sum(counts), p % 840 in HARD))
    for lo in (10**6, 10**7, 10**8):
        sel = [r for r in rows if r[0] == lo]
        c = Counter(r[2] for r in sel)
        print(f"p in [{lo:.0e},{10*lo:.0e}) sample {len(sel)}: P(minC=1)={c[1]/len(sel):.3f}, P(minC<=3)={sum(v for k,v in c.items() if k<=3)/len(sel):.3f}, P(no word C<={CMAX})={c[CMAX+1]/len(sel):.4f}")
    hardr = [r for r in rows if r[4]]; easy = [r for r in rows if not r[4]]
    print("hard (square classes mod 840) P(minC=1):", round(sum(r[2]==1 for r in hardr)/len(hardr),3), " non-hard:", round(sum(r[2]==1 for r in easy)/len(easy),3))
    print("mean words with C<=10 (hard, non-hard):", round(sum(r[3] for r in hardr)/len(hardr),2), round(sum(r[3] for r in easy)/len(easy),2))
    print("primes with no word for C<=10:", [r[1] for r in rows if r[2] == CMAX+1][:20])
