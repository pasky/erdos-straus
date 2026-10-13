"""R184 from-scratch check of LORENZINI_W Thm 9.1 covering (reviewer 2).
For each family: derive the m-condition by direct computation of 2^m mod modulus over a full period,
check coverage of all odd m mod 36, and check explicit solutions for all odd m in [11, M]."""
import sys
from math import lcm
M = int(sys.argv[1]) if len(sys.argv) > 1 else 3001
# family kinds: ('xy', x, y) -> d = xy-1, z = (n+x)/d ; ('xz', x, z) -> y = (n+x+z)/(x z)
fams = [('xz',3,3),('xz',6,12),('xy',7,2),('xz',3,9),('xy',10,11),('xz',8,74)]
def mod_shift(f):
    k,a,b = f
    return (a*b-1, a) if k=='xy' else (a*b, a+b)
def ord2(q):
    k=1; v=2%q
    while v!=1: v=v*2%q; k+=1
    return k
for q in (9,13,27,37,109): print('ord_%d(2)=%d'%(q,ord2(q)))
# which m mod 36 (m large, say m>=10 to kill 2-adic small-m issues) each family covers
cov = {}
for f in fams:
    d,s = mod_shift(f)
    cls = sorted({m%36 for m in range(11, 11+36*4) if ((1<<m)-2+s) % d == 0})
    # periodicity check: classes stable over a further window
    cls2 = sorted({m%36 for m in range(1001, 1001+36*4) if ((1<<m)-2+s) % d == 0})
    assert cls == cls2, (f, cls, cls2)
    cov[f]=cls; print(f, 'mod', d, 'shift', s, 'covers m mod 36:', cls)
odd = set(range(1,36,2)); got=set().union(*[set(c) for c in cov.values()])
print('odd classes uncovered:', sorted(odd-got))
# explicit check
def sol(n):
    for f in fams:
        k,a,b=f; d,s=mod_shift(f)
        if (n+s)%d==0:
            t=(n+s)//d
            x,y,z = (a,b,t) if k=='xy' else (a,t,b)
            if min(x,y,z)>=2 and x*y*z-x-z==n: return (x,y,z)
    return None
bad=[m for m in range(1,M+1,2) if sol((1<<m)-2) is None]
print('odd m <=',M,'with no family solution:', bad)
# small m by brute force
def brute(n):
    out=[]
    for x in range(2,n+3):
        for y in range(2,n+3):
            d=x*y-1
            if d>n+x: break
            if (n+x)%d==0 and (n+x)//d>=2: out.append((x,y,(n+x)//d))
    return out
for m in range(1,12,2):
    n=(1<<m)-2; print('m',m,'n',n,'brute solutions',brute(n))
