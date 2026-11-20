"""Fixed-modulus census at common search period; MITM for explicitly bounded masks."""
from z78_proth_period import fixed,ds,root
from math import gcd
import json,sys

def match(m,E,j):
    h=2*m-1;Q=2**h-1;k=2*Q+1;F={};ds0=ds(E)
    if h==1:return None
    for d in ds0:
        z=(pow(2,j*d,Q)+1)%Q
        for b in ds(d)[:-1]:z=z*pow(F[b],-1,Q)%Q
        F[d]=z
    a=ds0[:len(ds0)//2];b=ds0[len(a):];
    def menu(l):
        B={1:0}
        for i,d in enumerate(l):B.update({x*F[d]%Q:t+(1<<i) for x,t in B.items()})
        return B
    A=menu(a);B=menu(b);cs=[c for c in ds(k) if c%16==(14*Q-1)%16]
    for v,t in B.items():
        w=-pow(v,-1,Q)%Q
        for c in cs:
            g=w*pow(c,-1,Q)%Q
            if g in A:return (c,[d for i,d in enumerate(a) if A[g]>>i&1]+[d for i,d in enumerate(b) if t>>i&1])

def main():
    H=55440;rows=[]
    for m in range(1,31):
        F,L=fixed(m,H,30000);ww={}
        for j in range(1,2*m-1):
            if gcd(j,2*m-1)==1:
                w=match(m,3465,j)
                if w:ww[j]=w
        rows.append({'m':m,'period':H,'rows':F,'left':sorted(L),'mask_degree':3465,'witnesses':ww});print('census',m,len(ww),flush=True)
        (root/'census.json').write_text(json.dumps(rows,separators=(',',':'))+'\n')
if __name__=='__main__':main()
