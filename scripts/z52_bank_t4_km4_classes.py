"""T4 helper (z52 bank): run from the repo root."""
import math
from sympy import isprime
rows=[tuple(map(int,l.split())) for l in open('data/z52_bank/pencil_km4_counts_n1mod4_le6000.txt')]
by={}
for n,c in rows:
    key=(n%3==0, n%8)
    by.setdefault(key,[]).append((c/math.log(n)**2,c,n))
for k in sorted(by):
    v=by[k]; print('3|n' if k[0] else '3∤n', 'n%8=',k[1],' #n=',len(v),' mean c/log^2 n=%.3f'%(sum(x[0] for x in v)/len(v)),' min c=',min(x[1] for x in v),' zeros',[x[2] for x in v if x[1]==0])
pr=[(c/math.log(n)**2,c,n) for n,c in rows if isprime(n)]
print('primes: mean c/log^2 p = %.3f, min c = %d (n=%d), #=%d'%(sum(x[0] for x in pr)/len(pr), min(pr,key=lambda x:x[1])[1], min(pr,key=lambda x:x[1])[2], len(pr)))
