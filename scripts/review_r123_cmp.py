"""R123: compare review_r123_count.c output (f_I per prime) with an independent Python route-1 count."""
import sys, numpy as np
from math import gcd, isqrt
N = int(sys.argv[1]); arr = np.fromfile(sys.argv[2], dtype=np.uint32)
def divs(m):
    out=[]; i=1
    while i*i<=m:
        if m%i==0: out += [i] + ([m//i] if i*i!=m else [])
        i+=1
    return out
cnt = [0]*(N+1)
for a in range(1, N):
    if 3*a >= 2*N: break
    for d in range(1, N):
        if 3*a*d >= 2*N: break
        F = 4*a*a*d+1
        for f in divs(F):
            for c in range(1, N):
                if 3*a*c*d >= 2*N: break
                n = 4*a*c*d - f
                if n < 5 or n > N or c % n == 0: continue
                if (a*n+c) % f: continue
                b = (a*n+c)//f
                if b >= a and gcd(gcd(a,b),c) == 1: cnt[n] += 1
pr = [p for p in range(5, N+1) if all(p % q for q in range(2, isqrt(p)+1))]
bad = [(p, cnt[p], int(arr[p])) for p in pr if cnt[p] != arr[p]]
print("primes", len(pr), "mismatches", len(bad), bad[:5], "sum", sum(cnt[p] for p in pr))
