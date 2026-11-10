# z69 TWIST triage I9: p = X^2 + 840 Y^2 (p in the six Mordell classes); classifier
# Q(p) = [exists prime q | X with (840/q) = -1]  (such q has (p/q) = -1)
# hard sets vs matched controls (next NCTL primes of the same six classes above each hard prime).
import sys, math
from sympy import isprime, nextprime, factorint, jacobi_symbol, sqrt_mod
MOR={1,121,169,289,361,529}
def rep840(p):
    r=sqrt_mod(-840%p,p)
    if r is None: return None
    r=int(r); 
    if 2*r>p: r=p-r   # r^2 = -840 mod p ; Cornacchia
    a,b=p,r; L=math.isqrt(p)
    while b>L: a,b=b,a%b
    X=b; t=p-X*X
    if t%840: return None
    Y=math.isqrt(t//840)
    return (X,Y) if Y*Y*840==t else None
def feat(p):
    X,Y=rep840(p); fx=factorint(X) if X>1 else {}
    bad=[q for q in fx if jacobi_symbol(840,q)==-1]
    return X,Y,bad
def load(fn):
    out=[]
    for line in open(fn):
        line=line.split('#')[0].split()
        if line: out.append(int(line[0]))
    return sorted(set(out))
NCTL=int(sys.argv[1]) if len(sys.argv)>1 else 200
sets={'star14':'data/z58/screens/star_prime_zeros.txt','gstar38':'data/z58/screens/gstar_zeros.txt',
      'noprime231':'data/z68/u7f/noprime_primes_1e9.txt','u8zero':'data/z68/u7f/u8zero_primes_1e8.txt'}
for name,fn in sets.items():
    H=[p for p in load(fn) if p%840 in MOR and isprime(p)]
    hq=0; cq=0; cn=0; hsmall=0; csmall=0; rows=[]
    for p in H:
        X,Y,bad=feat(p); hq+= bool(bad); hsmall += any(q<100 for q in bad); rows.append((p,X,Y,bad))
        c=p; k=0
        while k<NCTL:
            c=nextprime(c)
            if c%840 in MOR:
                k+=1; _,_,b2=feat(c); cq+=bool(b2); cn+=1; csmall+=any(q<100 for q in b2)
    n=len(H); f0=cq/cn; sd=math.sqrt(f0*(1-f0)/n) if n else 0
    f1=csmall/cn; sd1=math.sqrt(f1*(1-f1)/n) if n else 0
    print(f"{name}: hard primes in M-classes n={n}; Q freq hard={hq}/{n}={hq/n:.3f} control={f0:.3f} (sd {sd:.3f}, z={(hq/n-f0)/sd if sd else 0:+.2f}); "
          f"Q with q<100: hard={hsmall/n:.3f} control={f1:.3f} (z={(hsmall/n-f1)/sd1 if sd1 else 0:+.2f})")
    for r in rows[:6]: print("   ",r)
