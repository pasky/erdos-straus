# z52d pass2 TO1 (Z0361, sibling calibration only, not ES): Sun's conjecture odd n = p + 2^a + 2^b + 2^c (a,b,c >= 0), n > 8.
# Counts representations (multiset of exponents, primes p>=2) for odd n <= L; reports min count and min count / log^2 n.
# usage: uv run --with numpy python scripts/z52d_p2_TO1_sun.py L
import sys, math, numpy as np
L=int(sys.argv[1])
s=np.ones(L+1,bool); s[:2]=False
for i in range(2,int(L**0.5)+1):
    if s[i]: s[i*i::i]=False
pw=[2**k for k in range(0,int(math.log2(L))+1)]
# multiset sums of three powers of 2 (exponents a<=b<=c), with the number of ordered-distinct-exponent multiplicities is irrelevant: we count distinct (a,b,c) multisets
sums=set()
for a in range(len(pw)):
    for b in range(a,len(pw)):
        for c in range(b,len(pw)):
            t=pw[a]+pw[b]+pw[c]
            if t<L: sums.add(t)
sums=np.array(sorted(sums),dtype=np.int64)
ns=np.arange(9,L+1,2)
cnt=np.zeros(len(ns),np.int64)
for t in sums:
    q=ns-t
    ok=q>=2
    cnt[ok]+= s[q[ok]]
print("odd n in (8,%d]:"%L, len(ns), " min count:", int(cnt.min()), " at n=", int(ns[cnt.argmin()]), " #n with count 0:", int((cnt==0).sum()))
lg=cnt/np.log(ns)**2
print("min count/log^2 n:", round(float(lg.min()),3), "at n=", int(ns[lg.argmin()]), "; median count/log^2 n:", round(float(np.median(lg)),3))
