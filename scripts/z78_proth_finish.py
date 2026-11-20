"""Gap-rule completion/refinement; takes partial certificate. Use --fixed separately for larger bounds."""
import sys,json
from math import gcd,lcm
from pathlib import Path
from z78_proth_period import pa,root,ds,order

def finish(m,H0,H,maxf=3000):
    data=json.loads((root/f'period-{m}-{H0}.json').read_text());k=4**m-1
    left={i for b in data['left'] for i in range(b,H,H0)};rows=data['rows'][:]
    qs=[]
    for q0 in pa.primes(3,60000):
        q=int(q0)
        if pow(2,H,q)!=1:continue
        z=q
        while z*q<2**32 and pow(2,H,z*q)==1:z*=q
        qs.append((q,z))
    fs=[f for f in range(3,maxf,4) if H%order(f//gcd(f,k))==0]
    for j in sorted(left):
        if j not in left:continue
        def put(M,R,*args):
            o=M//(M&-M);P=order(o//gcd(k,o));assert H%P==0
            rows.append([P,j%P,R,*args]);left.difference_update(range(j%P,H,P))
        ns={q:(k*pow(2,j,z)+1)%z for q,z in qs};div=next((q for q,z in qs if not ns[q]%q),None)
        if div:put(div,'D',div);continue
        for f in fs:
            K0=gcd((1+f)//4,2**24)
            for q,z in qs:
                if not (ns[q]+f)%q:K0*=gcd(ns[q]+f,z)
            md=4*K0*f;odd=md//(md&-md);comp=(pow(2,H,odd//gcd(k,odd))==1%(odd//gcd(k,odd)))
            n=(k*pow(2,j+H,md)+1)%md;K=(n+f)//4;assert not K%K0
            C={d*n**i*(K//K0)**a%f:(d,i,a) for a in range(1+comp) for i in range(2) for d in ds(K0)}
            D=next((D for D in C if -D%f in C),None)
            if D is not None:
                A,B=C[D],C[-D%f];put(md if A[2] or B[2] else 4*lcm(f,K0),'K',f,K0,A,B);break
    data.update(period=H,rows=rows,left=sorted(left));(root/f'period-{m}-{H}.json').write_text(json.dumps(data,separators=(',',':'))+'\n');print(m,H,'uncovered',len(left),sorted(left)[:12],flush=True)
if __name__=='__main__':finish(*map(int,sys.argv[1:]))
