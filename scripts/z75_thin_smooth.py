"""Extend frozen-period certificate by fixed-window smooth atom witnesses. Run after z75_thin_cyclo.py."""
from z75_conjs_period_helper import order,primes
from math import gcd
from pathlib import Path
import sys,json

def run(k,H,oldH):
    root=Path('data/z75/thin_cyclo'); fname=f'{k}-{oldH}'+('-smooth' if H!=oldH else '')+'.json';base=json.loads((root/fname).read_text());assert H%oldH==0
    left={s for r in base['left'] for s in range(r,H,oldH)};out=[]
    pows=[1<<min(30,2*32-2)];qs=[(2,pows[0])]
    for q in primes(50000):
        if q==2 or H%order(4,q):continue
        z=q
        while z*q<2**32 and pow(4,H,z*q)==1:z*=q
        qs.append((q,z))
    # For each residual s, precompute all offsets f giving a fixed prime in K=(n+f)/4.
    for s in sorted(list(left)):
        a=s+32*H; cache={}; fs={}
        for q,z in qs:
            nmod=(pow(4,a,4*z)+k)%(4*z)
            if q!=2 and nmod%q==0:
                out.append([s,'D',q]);break
            for f in range(3+((-nmod-3)*pow(4,-1,q)%q)*4 if q!=2 else 3,8193,4*q if q!=2 else 4):
                K=(nmod+f)//4; v=gcd(K,z)
                if v>1:fs.setdefault(f,[]).append((q,v))
        else:
            for f,fac in sorted(fs.items()):
                if 2*H%order(2,f):continue
                C={1:1}
                for q,z in fac:
                    t=q;z0=list(C.items());
                    while t<=z:
                        for x,y in z0:C.setdefault(x*t%f,y*t)
                        t*=q
                K0=1
                for q,z in fac:K0*=z
                # Include n and K/K0 separately; denominator K0 requires extra periodicity mod f.
                o=f*(K0//(K0&-K0));
                nmod=(pow(4,a,4*f*K0)+k)%(4*f*K0); K=(nmod+f)//4
                assert K%K0==0
                C={x:(y,0,0) for x,y in C.items()};C0=dict(C)
                for j in [0,1]:
                    if j and pow(4,H,o)!=1:continue
                    for i in [0,1]:
                        for x,(y,_,_) in C0.items():C.setdefault((x*pow(nmod,i,f)*pow(K//K0,j,f))%f,(y,i,j))
                pair=next(((C[x],C[-x%f]) for x in C if -x%f in C),None)
                if pair:
                    out.append([s,'K',f,K0,*pair]);break
                # Complementary divisors of (nK)^2. No restriction d1*d2 | nK:
                # (fy-nK)(fz-nK)=(nK)^2. Search residues of d/(nK)
                # using negative, zero and positive prime valuations.
                if gcd(nmod*K,f)==1:
                    bits=fac+[(nmod,nmod)] if nmod>1 else list(fac)
                    if nmod>1: bits=fac+[(0,nmod)]  # tag 0 means n itself
                    if pow(4,H,o)==1: bits=bits+[(1,(K//K0)%f)]
                    R={1:()}
                    for q,z in bits:
                        opts=[(0,1)];w=1
                        for e in range(1,64):
                            w*=q if q>1 else z
                            opts.extend([(e,w%f),(-e,pow(w,-1,f))]);
                            if q<2 or w==z:break
                        R={x*w%f:L+((q,e),) for x,L in R.items() for e,w in opts}
                        if f-1 in R:break
                    if f-1 in R:
                        out.append([s,'R',f,K0,R[f-1]]);break
            else:continue
        left.remove(s)
    (root/f'{k}-{H}-smooth.json').write_text(json.dumps({'parent':oldH,'rules':out,'left':sorted(left)},separators=(',',':'))+'\n');print(k,H,len(out),len(left),sorted(left)[:80])
if __name__=='__main__':run(*map(int,sys.argv[1:4]))
