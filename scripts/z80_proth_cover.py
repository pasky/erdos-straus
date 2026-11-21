"""Discovery: refine only gaps, scan fixed divisors of smooth periods and K windows.
Keep compressed lists, not a bitset on the final (sometimes very large) period.
"""
from math import gcd,lcm
from pathlib import Path
import sys,json
from z78_proth_period import pa,ds,order
root=Path('data/z80/proth');old=Path('data/z78/proth')
def run(m,maxf):
    C=json.loads((old/'census.json').read_text())[m-1];mask=json.loads((root/f'mask-{m}.json').read_text());k=4**m-1
    H0=C['period'];left=C['left'];rows=C['rows']+[mask];fout=root/f'cover-{m}.json'
    if fout.exists():
        c=json.loads(fout.read_text());rows=c['rows'];left=c['left'];H0=c['period']
    if not left:return
    H=lcm(H0,mask[0],*map(int,sys.argv[3:]));left={j for b in left for j in range(b,H,H0) if j%mask[0]};assert len(left)<1000000
    if H%(2*m+1)==0 and any(j%(2*m+1)==1 for j in left):
        rows.append([2*m+1,1,'D',2**(2*m+1)-1]);left={j for j in left if j%(2*m+1)!=1}
    qs=[]
    for q in map(int,pa.primes(3,200000)):
        if pow(2,H,q)!=1:continue
        z=q
        while z*q<2**60 and pow(2,H,z*q)==1:z*=q
        qs.append((q,z))
    fs=[f for f in range(3,maxf+1,4) if pow(2,H,f//gcd(k,f))==1%(f//gcd(k,f))];print(m,H,'start',len(left),len(fs),flush=True)
    def put(M,R,*args):
        o=M//(M&-M);P=order(o//gcd(k,o));assert H%P==0
        rows.append([P,j%P,R,*args]);left.difference_update(v for v in list(left) if (v-j)%P==0)
    for j in sorted(left):
        if j not in left:continue
        ns={q:(k*pow(2,j,z)+1)%z for q,z in qs};div=next((q for q,z in qs if not ns[q]%q),None)
        if div:put(div,'D',div);continue
        for f in fs:
            K0=gcd((1+f)//4,2**30)
            for q,z in qs:
                if not (ns[q]+f)%q:K0*=gcd(ns[q]+f,z)
            md=4*K0*f;odd=md//(md&-md);comp=(pow(2,H,odd//gcd(k,odd))==1%(odd//gcd(k,odd)))
            n=(k*pow(2,j+H,md)+1)%md;K=(n+f)//4;assert not K%K0
            C={d*n**i*(K//K0)**a%f:(d,i,a) for a in range(1+comp) for i in range(2) for d in ds(K0)}
            D=next((D for D in C if -D%f in C),None)
            if D is not None:
                A,B=C[D],C[-D%f];put(md if A[2] or B[2] else 4*lcm(f,K0),'K',f,K0,A,B);break
    fout.write_text(json.dumps(dict(m=m,period=H,rows=rows,left=sorted(left)),separators=(',',':'))+'\n');print(m,'left',len(left),sorted(left)[:60],flush=True)
if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]))
