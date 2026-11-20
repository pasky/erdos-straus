"""Search remaining exponent classes by fixed gap and divisors of n(n+gap)/4."""
from z75_conjs_period_helper import primes,order
from math import gcd
from pathlib import Path
import sys,json

def main(k,H,H0):
    root=Path('data/z77/proth');cert=json.loads((root/f'{k}-{H0}-0.json').read_text());res=cert['left'];out=[];bad=[]
    qs=[(2,2**24)];
    for q in primes(20000)[1:]:
        if pow(2,H,q)!=1:continue
        z=q
        while z*q<2**32 and pow(2,H,z*q)==1:z*=q
        qs.append((q,z))
    for j in [j for b in res for j in range(b,H,H0)]:
        s=j+32*H; fs={}
        for q,z in qs:
            n=(k*pow(2,s,4*z)+1)%(4*z)
            if q!=2 and n%q==0:out.append([H,j,'D',q]);break
            for f in range(3+4*((-n-3)*pow(4,-1,q)%q) if q>2 else 3,10000,4*q if q>2 else 4):
                x=gcd((n+f)//4,z)
                if x>1:fs.setdefault(f,[]).append((q,x))
        else:
            for f,ls in sorted(fs.items()):
                if pow(2,H,f)!=1:continue
                K0=1;ds=[1]
                for q,z in ls:
                    v=q;old=ds[:];K0*=z
                    while v<=z:ds += [x*v for x in old];v*=q
                md=4*f*K0;n=(k*pow(2,s,md)+1)%md;K=(n+f)//4;assert K%K0==0
                C={d*n**i*(K//K0)**j2%f:(d,i,j2) for j2 in range(1+(pow(2,H,md//(md&-md))==1)) for i in [0,1] for d in ds}
                pair=next(((C[x],C[-x%f]) for x in C if -x%f in C),None)
                if pair:out.append([H,j,'K',f,K0,*pair]);break
            else:bad.append(j)
    print(k,H,len(out),len(bad),bad[:80]);(root/f'{k}-{H}-extra.json').write_text(json.dumps({'rules':out,'left':bad},separators=(',',':'))+'\n')
if __name__=='__main__':main(*map(int,sys.argv[1:4]))
