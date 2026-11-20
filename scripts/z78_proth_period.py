"""Bounded fixed-rule search; every row carries its own modulus/period. No prior-wave imports."""
from math import gcd,lcm,isqrt
from pathlib import Path
from functools import cache
import sys,json
from collections import Counter
from cypari2 import Pari
pa=Pari(); root=Path('data/z78/proth')
@cache
def ds(n):return list(map(int,pa.divisors(n)))
@cache
def order(n):return 1 if n==1 else int(pa.znorder(pa.Mod(2,n)))
@cache
def dlog(b,M):
    if M==1:return 0
    if gcd(b,M)>1:return None
    a=pa.znlog(b%M,pa.Mod(2,M),order(M));return int(a) if a.type()=='t_INT' else None

def fixed(m,H,bound):
    k=4**m-1; left=set(range(H)); rows=[]
    def put(P,j,R,*args):
        if H%P:return
        if j is not None and not left.isdisjoint(range(j,H,P)):
            rows.append([P,j,R,*args]);left.difference_update(range(j,H,P))
    sqm={a*a%840 for a in range(840) if gcd(840,a)==1}
    for j in range(12):
        if (k*2**(j+36)+1)%840 not in sqm:put(12,j,'M')
    def solve(M,t,R,*args): # k*2^s + 1 == t mod M, s>=64
        two=M&-M
        if (t-1)%two:return
        M//=two;g=gcd(k,M)
        if (t-1)%g:return
        M//=g;P=order(M)
        if H%P:return
        j=dlog((t-1)//g*pow(k//g,-1,M)%M,M);put(P,j,R,*args)
    for q0 in pa.primes(3,min(19999,bound)):
        q=int(q0);solve(q,0,'D',q)
    for f in range(3,bound+1):
        odd=f//(f&-f);M=odd//gcd(odd,k)
        if pow(2,H,M)!=1%M:continue
        for u in ds(f+1)[1:-1]:
            t=(f+1)//u
            for v in range(8):
                if (1+t)*t*u*v%8==0 and (f*v-u)%8==1:solve(8*f,f*v-u,'W',f,u)
        if f%4==3:
            for a in ds((f+1)//4):
                for b in ds((f+1)//(4*a)):solve(f,-a*pow(b,-1,f),'II',f,a,b)
    print(m,H,bound,'fixed',Counter(r[2] for r in rows),len(left),sorted(left)[:12],flush=True)
    return rows,left

def poly(m,j,e): # modular extraction; direct recurrence on polynomial evaluations in odd-order group
    h=2*m-1;Q=2**h-1;u=2*Q;k=u+1;M=8*u;x=pow(2,j+16*h,M);B={c%M:(c,[]) for c in ds(k) if c%16==(7*u-1)%16};F={}
    for d in ds(e):
        a=(1+pow(x,d,M))%M
        for f in ds(d)[:-1]:a=a*pow(F[f],-1,M)%M
        F[d]=a;B.update({b*a%M:(c,T+[d]) for b,(c,T) in B.items()});target=(7*u-1)%M
        if target in B:return B[target]

def run(m,H,bound):
    rows,left=fixed(m,H,bound); h=2*m-1
    # X rows need every unit j. Fractional/mixed rows are not used here.
    if m>1:
        for e in ds(H//4):
            if e%2==0 or not any(not j%(4*e) for j in left):continue
            ww={}
            for j in range(1,h):
                if gcd(j,h)==1:
                    w=poly(m,j,e)
                    if not w:break
                    ww[j]=w
            else:
                rows.append([4*e,0,'X',e,ww]);left.difference_update(range(0,H,4*e))
                if not left:break
    file=root/f'period-{m}-{H}.json';file.write_text(json.dumps({'m':m,'period':H,'bound':bound,'rows':rows,'left':sorted(left)},separators=(',',':'))+'\n');print(m,'left',len(left),sorted(left)[:30],flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
