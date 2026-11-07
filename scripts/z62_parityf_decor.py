"""For each prime p = 1 mod 4 (and odd squares), over unordered ES solutions in master form (g; marked set; unmarked set),
count #solutions with various quantities being perfect squares; print parities. Looking for a uniformly odd count."""
import sys
from math import isqrt
from sympy import isprime, primerange
sys.path.insert(0,'scripts')
from z62_parityf_master import master

def issq(n): return isqrt(n)**2 == n

def canon(rows, n):
    seen = {}
    for xyz, m in rows:
        key = tuple(sorted(xyz))
        if key in seen or m is None: continue
        g,a,b,c,eps = m
        marked = sorted(v for v,e in zip((a,b,c),eps) if e == n)
        unmarked = sorted(v for v,e in zip((a,b,c),eps) if e != n)
        seen[key] = (g, tuple(marked), tuple(unmarked), key)
    return list(seen.values())

names = ["g=1","prod(marked) sq","prod(unmarked) sq","g*prod(marked) sq","g*prod(unmarked) sq","abc sq","g*abc sq",
         "min denom sq","max denom sq","x~y~z~ sq","TypeI&g=1","TypeII&c sq","TypeI&c sq","sum a+b+c sq", "any of a,b,c sq", "p-free part of z sq", "T1", "T2"]
def feats(sol, n):
    g, M, U, xyz = sol
    import math
    pm = math.prod(M); pu = math.prod(U)
    a,b,c = sorted(M+U)
    xt = [v//n if v % n == 0 else v for v in xyz]
    T1 = len(M) == 2
    return [g==1, issq(pm), issq(pu), issq(g*pm), issq(g*pu), issq(a*b*c), issq(g*a*b*c), issq(xyz[0]), issq(xyz[2]),
            issq(math.prod(xt)), T1 and g==1, (not T1) and issq(M[0]), T1 and issq(U[0]), issq(a+b+c), any(issq(v) for v in (a,b,c)),
            issq(max(xt)), T1, not T1]

lo, hi = int(sys.argv[1]), int(sys.argv[2])
tot = {k: [] for k in names}
for n in range(lo, hi+1):
    if n % 4 != 1: continue
    if not (isprime(n) or isqrt(n)**2 == n): continue
    sols = canon(master(n), n)
    par = [sum(f[i] for f in (feats(s, n) for s in sols)) % 2 for i in range(len(names))]
    tag = 'P' if isprime(n) else 'SQ'
    print(n, tag, n % 24, ''.join(str(x) for x in par), len(sols))
    for k, v in zip(names, par): tot[k].append((n, tag, v))
print()
for k in names:
    pr = [v for (n,t,v) in tot[k] if t == 'P']; pr24 = [v for (n,t,v) in tot[k] if t == 'P' and n % 24 == 1]; sq = [v for (n,t,v) in tot[k] if t=='SQ']
    print("%-22s primes: odd %d/%d | primes=1(24): odd %d/%d | squares: odd %d/%d" % (k, sum(pr), len(pr), sum(pr24), len(pr24), sum(sq), len(sq)))
