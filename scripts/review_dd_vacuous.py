"""R176: is the relaxed reading 'level G >= 2 sqrt(h)' (DIFF_DEEP §4 / O176 report) equivalent to Thm 2.1's
'4h | gcd(h,G)^2'?  For each prime p, search pairs f<=f', ff'=1+ph, h<=H, with G>=2sqrt(h), B_T ramified exactly
at p, and 4h !| gcd(h,G)^2 (i.e. NOT a Type II pair)."""
import sys
from math import gcd, isqrt
from sympy import primerange, divisors
sys.path.insert(0,'scripts')
from review_dd_hilbert_lib import ram
P=int(sys.argv[1]); H=int(sys.argv[2]); cnt={}; nopair=[]
for p in primerange(5,P):
    found=None
    for h in range(1,H+1):
        N=1+p*h
        for f in divisors(N):
            if f*f>N: break
            g=N//f; G=gcd(f+1,g+1)
            if G*G>=4*h and (gcd(h,G)**2)%(4*h) and ram(-f,-f*(N-1))==[p]:
                found=(f,g,h,G); break
        if found: break
    r=p%24; cnt.setdefault(r,[0,0]); cnt[r][1]+=1
    if found: cnt[r][0]+=1
    else: nopair.append(p)
    if p in (73,97,193,1201) : print(p,found)
print("p mod 24: [primes with a non-Type-II pair of level >= 2 sqrt h, total]", dict(sorted(cnt.items())))
print("no such pair found (h<=%d):"%H, nopair[:20], len(nopair))
