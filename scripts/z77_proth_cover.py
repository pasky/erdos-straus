"""Certify exponent classes via fixed words, Mordell and product cyclotomics."""
import json,sys,math
from pathlib import Path
from functools import cache
from z75_conjs_period_helper import divisors,order,primes
from z77_proth_words import extract

@cache
def small_div(n):
    return [d for i in range(1,math.isqrt(n)+1) if n%i==0 for d in ({i,n//i})]

def search(k,H,words=False):
    left=set(range(H)); out=[]; n=lambda j,m:(k*pow(2,j+32*H,m)+1)%m
    def rec(P,j,*row):
        if H%P: return
        cover=left.intersection(range(j,H,P))
        if cover: out.append([P,j,*row]);left.difference_update(cover)
    squares={x*x%840 for x in range(1,840,2) if words or math.gcd(x,840)==1}
    for j in range(12):
        if n(j,840) not in squares: rec(12,j,'M')
    if not words:
        for q in primes(3000)[1:]:
            P=order(2,q)
            if H%P:continue
            for j in sorted({i%P for i in left}):
                if not n(j,q):rec(P,j,'D',q)
    for A in range(3,100000):
        o=A//(A&-A)
        if pow(2,H,o)!=1%o:continue
        P=order(2,o)
        for j in sorted({i%P for i in left}):
            v,u=divmod(-n(j,8*A),A);t,r=divmod(A+1,u or 1)
            if u>=2 and t>=2 and r==0 and (1+t)*t*u*(-v)%8==0:rec(P,j,'W',A,u)
            if not words and A%4==3 and j in {i%P for i in left}:
                for b in small_div((A+1)//4):
                    a=-(k*pow(2,j,A)+1)*b%A
                    if a and (A+1)%(4*a*b)==0:rec(P,j,'II',A,a,b);break
    print('fixed',k,H,len(out),len(left),sorted(left)[:70],flush=True)
    h=order(2,(k-1)//( (k-1)&-(k-1) )); assert math.gcd(h,2)==1
    # Strip all h-prime powers if needed, then spend a fixed odd degree m.
    hp=[q for q in small_div(h) if q>1 and all(q%i for i in range(2,math.isqrt(q)+1))]; assert len(hp)==1; p=hp[0]
    for m in [a for a in sorted(small_div(H)) if a%2 and a<=1200]:
        # s/(m*h^a)=r, so x^m+1|2^s+1; if h|m, s must supply those copies too.
        if H%m:continue
        for i in sorted(left):
            if i%m or i%4:continue
            # possible r mod h after stripping h whether or not its exact order is determined.
            j1=i//m;P=H//m
            if P%h or j1%p==0: js=[j for j in range(1,h) if j%p]
            else:js=[j1%h]
            if all(ext(k,m,j) for j in js):rec(H,i,'X',m);continue
    print('with cyclo',len(out),len(left),sorted(left)[:100],flush=True)
    return out, sorted(left)
ext=cache(extract)
if __name__=='__main__':
    k,H=map(int,sys.argv[1:3]);w=len(sys.argv)>3;out,left=search(k,H,w);Path(f'data/z77/proth/{k}-{H}-{int(w)}.json').write_text(json.dumps({'rules':out,'left':left},separators=(',',':'))+'\n')
