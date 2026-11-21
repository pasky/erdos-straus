"""Discovery, meet two half products. All masks are replayed by z78_proth_check."""
from math import gcd,prod
from pathlib import Path
import json,sys,random
from z78_proth_period import ds
root=Path('data/z80/proth')
def one(m,j,e):
    h=2*m-1;H=2**h-1;k=2*H+1;F={};atoms=[]
    for d in ds(e):
        a=(1+pow(2,j*d,H))%H
        for b in ds(d)[:-1]:a=a*pow(F[b],-1,H)%H
        F[d]=a
        if a!=1:atoms.append((d,a))
    cs=[c for c in ds(k) if c%16==1];rng=random.Random(j)
    rng.shuffle(atoms)
    # Choose a balanced table of up to 2^17 lhs products. In big degrees use
    # random batches on the other side, still reconstructing exact masks.
    L=atoms[:min(17,len(atoms)//2)];R=atoms[len(L):]
    def pset(L):
        Z=[1]
        for d,a in L:Z += [z*a%H for z in Z]
        return Z
    A={z:i for i,z in enumerate(pset(L))}
    def sub(L,i):return [d for k,(d,a) in enumerate(L) if i>>k&1]
    R=[(d,pow(a,-1,H)) for d,a in R]
    n=min(16,len(R));Z=pset(R[:n]);Q=R[n:];C=[(c,(-pow(c,-1,H))%H) for c in cs]
    for b in range(min(1<<len(Q),128)):
        v=prod(a for i,(d,a) in enumerate(Q) if b>>i&1)%H
        for c,inv in C:
            g=v*inv%H
            for i,z in enumerate(Z):
                x=A.get(g*z%H)
                if x is not None:return c,sub(L,x)+sub(R[:n],i)+sub(Q,b)

def run(m,elist):
    h=2*m-1;f=root/f'mask-{m}.json'
    if f.exists():return
    for e in elist:
        W={}
        for j in range(1,h):
            if gcd(j,h)>1:continue
            a=one(m,j,e)
            if a is None:break
            W[j]=a
        else:
            f.write_text(json.dumps([4*e,0,'X',e,W],separators=(',',':'))+'\n');print('PASS',m,e,flush=True);return
        print('miss',m,e,j,flush=True)
if __name__=='__main__':run(int(sys.argv[1]),list(map(int,sys.argv[2:])))
