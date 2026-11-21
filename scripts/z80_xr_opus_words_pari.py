"""Opus cross-lab review of notes/z80/EXTREME.md: own-code word counter for the
two rows of wordfactor.csv beyond the C engines.  Partition labelled (u,t,v),
t*u*v-u-v=n, by the minimal letter (same partition as z80_xr_opus_words.c):
 A u<=t,u<=v: f=tu-1 | n+u;  B mirror of A with u<v;  C t<u,t<v: (tu-1)(tv-1)=tn+1
 (enumerate all divisors f of tn+1, f=-1 mod t, keep t<u<=v, mirror).
Output as words.csv.  Validate on small n first (argument list)."""
import sys
from cypari2 import Pari
P = Pari(); P.allocatemem(512000000, silent=True); P.default('factor_proven', 1)

def stats(n):
    W = R = R8 = U7 = E = 0; H = 0
    def word(u, t, v):
        nonlocal W, R, R8, U7, E, H
        assert t*u*v-u-v == n
        W += 1; R += t % 4 == 0; R8 += t % 8 == 0; U7 += t*u % 8 == 0
        E += any(z % 4 == 0 for z in (u, t, v, t*u-1, t*v-1))
        if min(u, t, v) >= 2 and int(P.kronecker(t*u-1, n)) == -1 and (not H or t*u-1 < H): H = t*u-1
    m = 1
    while m**3-2*m <= n:
        N = n+m
        for f in P.divisors(N).python():        # A/B with u=m
            if (f+1) % m: continue
            t = (f+1)//m; v = N//f
            if t >= m and v >= m:
                word(m, t, v)
                if m < v: word(v, t, m)
        M = m*n+1                               # C with t=m (t=1 included)
        for f in P.divisors(M).python():
            if (f+1) % m: continue
            u = (f+1)//m; g = M//f
            if (g+1) % m: continue
            v = (g+1)//m
            if m < u <= v:
                word(u, m, v)
                if v > u: word(v, m, u)
        m += 1
    return R, R8, U7, E, H, W

print('n,R,R8,U7,ES5,HJmin,words', flush=True)
for n in map(int, sys.argv[1:]):
    print(n, *stats(n), sep=',', flush=True)
