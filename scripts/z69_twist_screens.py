# z69 TWIST: (W)/C_n on the z58 falsifier screens (F2: 12 R8-zero primes ~1e10; F3: 285 composite (★)-zeros; F4: 14 (★)-zero
# and 38 G*-zero primes).  For each n: first certificate word found by scanning x = 1..XMAX and divisors f of n + x,
# f == -1 (mod x): word (x, y, z) = (x, (f+1)/x, (n+x)/f); types (i) 4|y, (ii) 4|x or 4|z, (iii) y==3 (4) and (x==3 or z==3 (4)).
# Exhaustive (all x <= n+2) when n <= EXH.  Also reports whether a (★) word (type (i)) was seen.
import sys
from sympy import divisors
def load(fn):
    out=[]
    for line in open(fn):
        t=line.split('#')[0].split()
        if t: out.append(int(t[0]))
    return sorted(set(out))
def scan(n,XMAX):
    first=None; star=False
    for x in range(1,min(n+2,XMAX)+1):
        for f in divisors(n+x):
            if (f+1)%x==0 and f>0:
                y=(f+1)//x; z=(n+x)//f
                if x*y*z-x-z!=n: continue
                t=('i' if y%4==0 else '')+('/ii' if (x%4==0 or z%4==0) else '')+('/iii' if (y%4==3 and (x%4==3 or z%4==3)) else '')
                if y%4==0: star=True
                if t and first is None: first=(x,y,z,t)
    return first,star
EXH=int(sys.argv[1]); XMAX=int(sys.argv[2])
for name,fn in (('F4 star14','data/z58/screens/star_prime_zeros.txt'),('F4 gstar38','data/z58/screens/gstar_zeros.txt'),
                ('F3 composite285','data/z58/screens/composite_zeros_le8e6.txt'),('F2 r8zeros12','data/z58/screens/r8_zeros_1e10.txt')):
    L=load(fn); noC=[]; ex=[]
    for n in L:
        first,star=scan(n, n+2 if n<=EXH else XMAX)
        if first is None: noC.append(n)
        elif len(ex)<2: ex.append((n,first))
    print(f"{name}: {len(L)} numbers; C-certificate found at {len(L)-len(noC)}; none found at {noC} "
          f"({'exhaustive' if max(L)<=EXH else 'x <= %d only for n > %d'%(XMAX,EXH)}); examples {ex}",flush=True)
