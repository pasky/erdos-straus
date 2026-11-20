"""Core positive products using SMALL-primary logarithms only. No large prime-order dlogs."""
from cypari2 import Pari
from math import gcd,lcm
from pathlib import Path
import json,sys
pa=Pari();root=Path('data/z78/proth');F=lambda n:[(int(p),int(e)) for p,e in zip(*pa.factor(n))]
def dlogmaker(N,L,p):
    # In (Z/N)^*, N odd prime power, L=phi(N). Project to the p-primary quotient.
    D=1
    while L%(p*D)==0:D*=p
    Y=next(y for y in range(2,N) if gcd(y,N)==1 and pow(y,L//p,N)!=1);G=pow(Y,L//D,N);gi=pow(G,-1,N);tab={pow(G,i*(D//p),N):i for i in range(p)}
    def log(x):
        b=pow(x,L//D,N);e=0;v=1
        while v<D:
            z=tab[pow(b,D//(p*v),N)];b=b*pow(gi,z*v,N)%N;e+=z*v;v*=p
        assert b==1;return e
    return D,log

def solve(h):
    H=2**h-1;k=2*H+1;m=(h+1)//2;o=int(pa.znorder(pa.Mod(2,h)));P=2*o
    B=lambda i:(1+pow(2,i,H))%H
    small=set(p for p,e in F(P));f=F(H);exp=lcm(*[p**(e-1)*(p-1) for p,e in f]);Z=exp
    for q in small:
        while not Z%q:Z//=q
    logs=[dlogmaker(p**e,p**(e-1)*(p-1),q) for p,e in f for q in sorted(small) if not (p**(e-1)*(p-1))%q];ds=[d for d,lg in logs];n=len(ds);R=[a for a in range(h) if a!=gcd(a,h)%h and gcd(a,h)==1];idx={a:i for i,a in enumerate(R)}
    gs=[B(a)*pow(B(gcd(a,h)),-1,H)%H for a in R];A=pa.matrix(n,len(R),[lg(g) for d,lg in logs for g in gs]);cnt=0
    # Try only choices with explicit P-th powers in R. Projection is lossless for each.
    for c in [1,2**m+1]:
        if c%16!=(14*H-1)%16:continue
        for S in [[],[1]]+([[1,3]] if not h%3 else []):
            # Phi_2(2) = Phi_6(2) = 3.
            T=-pow(c*3**len(S),-1,H)%H
            w=pa.matsolvemod(A,pa.Col(ds),pa.Col([lg(T) for d,lg in logs]));cnt+=1
            if w.type()=='t_INT':continue
            # prod(G_i^w_i)^Z = T^Z. Also prod_{i<o} B_{a*2^i}=1 at unit a.
            inv=pow(Z,-1,P);v=(1-Z*inv)//P;e=[int(x)*Z*inv for x in w]
            for a in [1]*len(S)+([m%h] if c!=1 else []):
                # B_a^{-P} = prod_{i<o} (B_{a2^i}/B_a)^2. Use generators to B_1.
                for i in range(o):
                    b=a*pow(2,i,h)%h
                    if b!=1:e[idx[b]]+=2*v
                    if a!=1:e[idx[a]]-=2*v
            e=[i%exp for i in e];assert T==__import__('functools').reduce(lambda x,y:x*y%H,[pow(g,i,H) for g,i in zip(gs,e)],1)
            return dict(h=h,c=c,T0=S,ratios={a:b for a,b in zip(R,e) if b})
    return dict(h=h,miss=cnt)
if __name__=='__main__':
    lo,hi=map(int,sys.argv[1:]);rows=[]
    for h in range(lo,hi+1,2):
        d=solve(h);rows.append(d);print(h,d.get('c'),d.get('T0'),flush=True)
        (root/f'primary-{lo}-{hi}.json').write_text(json.dumps(rows,separators=(',',':'))+'\n')
