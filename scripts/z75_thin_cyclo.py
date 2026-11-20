"""Period-certified ES search on 4^s+k. Mode: k period. s>=32. No third-party imports.
For fixed-gap f recover d1,d2 dividing nK from atom exponents; then ES follows from
f|d1+d2, K=(n+f)/4. Search is not exhaustive for ES nor for the chosen period.
"""
import sys,math,itertools,json
from functools import cache
from pathlib import Path
from z75_conjs_period_helper import divisors,order,primes

def build(k,H):
    out=[]; left=set(range(H));
    def record(P,kind,par,res):
        assert H%P==0
        for j,data in res:
            cov=left.intersection(range(j,H,P))
            if cov: out.append([P,j,kind,par,data]);left.difference_update(cov)
    # Mod 840 Mordell and fixed prime divisibility.
    M={1,121,169,289,361,529}
    for j in list(left):
        if (pow(4,j+6,840)+k)%840 not in M:record(6,'M',[],[(j%6,None)])
    for q in primes(3000):
        if q==2:continue
        o=order(4,q)
        if H%o:continue
        st={s%o for s in left}; record(o,'D',[q],[(s,None) for s in sorted(st) if (pow(4,s,q)+k)%q==0])
    print(k,H,'after Mordell/divisors',len(left),file=sys.stderr)
    # fixed t (tu-1)(tv-1)=tn+1; or fixed u and divisor A | n+u. Enumerate fixed A.
    for A in range(3,12001):
        odd=A//(A&-A);o=order(4,odd)
        if H%o:continue
        for j in sorted({s%o for s in left}):
            n=(pow(4,j+H*32,8*A)+k)%(8*A); u=(-n)%A
            if 2<=u and (A+1)%u==0 and (t:=(A+1)//u)>=2 and ((n+t)*t*u*((n+u)//A))%8==0:record(o,'A',[A,u],[(j,None)])
    print('after fixed words',len(left),file=sys.stderr)
    # f with k+f=2^m*a^d (odd d) or 2^m*a^4. K and n positive atoms.
    for f in range(3,25001,4):
        l=order(2,f)
        if (2*H)%l:continue
        g=k+f;m=(g&-g).bit_length()-1;b=g>>m;assert m>=2
        for d in (1,3,5,7,9,11,13,15,21,25,27,35,45,4):
            a=round(b**(1/d));
            if a**d!=b:continue
            P0=d*l if d!=4 else 4*l
            P=P0//math.gcd(2,P0)
            if H%P:continue
            st=sorted({s%P for s in left})
            for j in st:
                s=j+P*32;e=2*s-m
                if d!=4 and e%d:continue
                if d==4 and e%4!=2:continue
                z=pow(2,e//d,f); n=(pow(4,s,f)+k)%f
                atoms=[n]
                if d==4:
                    atoms+=[(2*z*z-2*z*a+a*a)%f,(2*z*z+2*z*a+a*a)%f]
                else:
                    # Homogeneous cyclotomics Phi_{2h}(z,a), product over h|d = z^d+a^d.
                    atoms.extend(sum(c*pow(z,i,f)*pow(a,deg-i,f) for i,c in enumerate(poly))%f for poly in polys(d) for deg in [len(poly)-1])
                # Pick two divisors of nK by independent binary choices; handles shared factors.
                B={1:0}
                for i,v in enumerate(atoms):B.update({(u*v)%f:mask|(1<<i) for u,mask in B.items()})
                C={v*(1<<e2)%f:(mask,e2) for v,mask in B.items() for e2 in range(m-1)}
                match=next(((C[v],C[-v%f]) for v in C if -v%f in C),None)
                if match: record(P,'gap',[f,d],[(j,match)])
    print('after moving gaps',len(left),sorted(left)[:60],file=sys.stderr)
    return out,sorted(left)

@cache
def polys(d):
    arr=[]
    for h in divisors(d):
        a=[1]+[0]*(h-1)+[1]
        for j,b in arr:
            if h%j:continue
            q=[0]*(len(a)-len(b)+1)
            for i in reversed(range(len(q))):
                q[i]=a[i+len(b)-1]
                for k,c in enumerate(b):a[i+k]-=q[i]*c
            assert not any(a);a=q
        arr.append((h,a))
    return [b for j,b in arr]

if __name__=='__main__':
    k,H=map(int,sys.argv[1:3]);assert H%6==0 and H>=32
    out,rem=build(k,H);Path('data/z75/thin_cyclo/%s-%s.json'%(k,H)).write_text(json.dumps({'rules':out,'left':rem},separators=(',',':'))+'\n')
