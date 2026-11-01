"""z52d pass2 TO0b: (a) Z0131/Z0130 odd-denominator parity for 4/n; (b) Z0126 numerator-2 identity check;
(c) Z0108 forced large numerators m(p) in {p+1,p+2,...}: 3-term representability of m/p for primes p <= 2000."""
import sys
from math import gcd
from fractions import Fraction as Fr
def divisors(n):
    ds=[]; i=1
    while i*i<=n:
        if n%i==0:
            ds.append(i)
            if i*i!=n: ds.append(n//i)
        i+=1
    return ds
def odd_two_terms(n):
    """4/n = 1/x+1/y with x,y odd (n odd): exists iff ..."""
    m=n*n
    for d in divisors(m):
        if (d+n)%4 or (m//d+n)%4: continue
        x=(n+d)//4; y=(n+m//d)//4
        if x>0 and y>0 and x%2 and y%2 and Fr(1,x)+Fr(1,y)==Fr(4,n): return (x,y)
    return None
def odd_reps3(n, bound=None):
    """all 3-term solutions 4/n = 1/x+1/y+1/z with x,y,z odd, x<=y<=z (brute over x,y)."""
    out=0
    r=Fr(4,n)
    x0=n//4+1
    for x in range(x0, 3*n//4+1):
        if x%2==0: continue
        r1=r-Fr(1,x)
        if r1<=0: continue
        y0=max(x, int(1/r1)+1)
        y1=int(2/r1)+1
        for y in range(y0, y1+1):
            if y%2==0: continue
            r2=r1-Fr(1,y)
            if r2<=0: continue
            if r2.numerator==1 and r2.denominator%2==1 and r2.denominator>=y: out+=1
    return out
print("(a) odd-denominator 4/n, odd n<=3001: 2-term representable count, 3-term count (n<=301)")
ntwo=[n for n in range(3,3002,2) if odd_two_terms(n)]
print("  two odd unit fractions:", len(ntwo), "of", len(range(3,3002,2)), "first non-representable:", [n for n in range(3,200,2) if not odd_two_terms(n)][:12])
bad=[n for n in range(3,302,2) if odd_reps3(n)>0]
print("  odd 3-term solutions exist for n<=301 (should be none, parity: k even):", bad)
print("(b) Z0126 identity 4/n = 2/((n+1)/2) + 1/M + 1/M, M=n(n+1)/2, odd n<=10001:")
ok=all(Fr(4,n)==Fr(2,(n+1)//2)+Fr(2,n*(n+1)//2) for n in range(1,10002,2))
print("  identity holds for all odd n<=10001:", ok)
print("(c) Z0108: 3-term representability of m/p for m in {p+1,p+2,p+3,2p+1,2p-1,p-1} over primes 5<=p<=2000:")
def reps3(a,b,limit_y=None):
    """count solutions of a/b = 1/x+1/y+1/z (x<=y<=z), a/b fraction, brute over x,y."""
    r=Fr(a,b); cnt=0
    x0=int(1/r)+1
    for x in range(x0, int(3/r)+1):
        r1=r-Fr(1,x)
        if r1<=0: continue
        y0=max(x,int(1/r1)+1); y1=int(2/r1)+1
        for y in range(y0,y1+1):
            r2=r1-Fr(1,y)
            if r2<=0: continue
            if r2.numerator==1 and r2.denominator>=y: cnt+=1
    return cnt
def isprime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True
PS=[p for p in range(5,2001) if isprime(p)]
forms={'p+1':lambda p:p+1,'p+2':lambda p:p+2,'p+3':lambda p:p+3,'2p+1':lambda p:2*p+1,'2p-1':lambda p:2*p-1,'p-1':lambda p:p-1}
for name,f in forms.items():
    yes=0; mod4=[0,0,0,0]
    for p in PS:
        m=f(p)
        if reps3(m,p)>0:
            yes+=1
    print(f"  m={name}: 3-term representable for {yes}/{len(PS)} primes")
