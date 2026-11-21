"""Discovery only: eight subset lists, two nested local character filters, exact last match."""
import random,itertools,sys,json
from math import prod,gcd
from z78_proth_period import ds,pa
from z80_proth_masks import root

def filters(H,B):
    qs=[int(q) for q in pa.factor(H)[0]];assert prod(qs)==H
    cap=[q-1 for q in qs];atoms=sorted((int(l),i) for i,c in enumerate(cap) for l,n in zip(*pa.factor(c)) for _ in range(int(n)))
    power=[1]*len(qs);stages=[]
    for _ in range(2):
        rem=B
        while True:
            a=next((k for k in range(len(atoms)-1,-1,-1) if atoms[k][0]<=rem),None)
            if a is None:break
            l,i=atoms.pop(a);rem//=l;power[i]*=l
        stages.append([(q,(q-1)//d) for q,d in zip(qs,power) if d>1])
    return stages

def run(m,e,tries):
    h=2*m-1;H=2**h-1;k=2*H+1;file=root/f'mask-{m}.json';rng=random.Random(117*m+e);W={}
    if file.exists():return
    deg=ds(e);bits=(h+3)//4+1;B=2**bits;stages=filters(H,B);c=2**m+1 if h%9==0 else 1
    for j in range(1,h):
        if gcd(j,h)>1:continue
        F={};ids=[];forced=0;v=c
        for a,d in enumerate(deg):
            f=(1+pow(2,j*d,H))%H
            for b in ds(d)[:-1]:f=f*pow(F[b],-1,H)%H
            F[d]=f
            if h%d==0:
                if (h%3==0 and d==1) or (h%9==0 and d==3):forced|=1<<a;v=v*f%H
            elif f!=1:ids.append((a,f))
        target=(-pow(v,-1,H))%H
        if len(ids)<8*bits:print('too few',e,j,len(ids),8*bits);return
        for attempt in range(tries):
            rng.shuffle(ids);lists=[]
            for b in range(8):
                Z=[(target if b==0 else 1,0)] if b==0 else [(1,0)]
                for a,f in ids[b*bits:(b+1)*bits]:
                    inv=pow(f,-1,H) if b==0 else f
                    Z.extend([(x*inv%H,t|1<<a) for x,t in Z])
                if b==0:Z=[(pow(x,-1,H),t) for x,t in Z]
                lists.append(Z)
            def combine(A,C,pr):
                D={};out=[]
                for x,t in A:
                    key=tuple(pow(x,-d,q) for q,d in pr);D.setdefault(key,[]).append((x,t))
                for y,u in C:
                    key=tuple(pow(y,d,q) for q,d in pr)
                    for x,t in D.get(key,()):
                        out.append((x*y%H,t|u))
                        if len(out)>=B:return out
                return out
            for pr in stages:
                lists=[combine(A,C,pr) for A,C in zip(lists[::2],lists[1::2])]
                if any(not L for L in lists):break
            if len(lists)!=2:continue
            A={pow(x,-1,H):t for x,t in lists[0]};hit=next((A[x]|u|forced for x,u in lists[1] if x in A),None)
            if hit is not None:
                mask=[d for a,d in enumerate(deg) if hit>>a&1];assert (c*prod(F[d] for d in mask)+1)%H==0
                W[j]=(c,mask);break
        else:print('miss',m,j,e,flush=True);return
    file.write_text(json.dumps([4*e,0,'X',e,W],separators=(',',':'))+'\n');print('pass',m,e,flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
