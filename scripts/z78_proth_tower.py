"""Certify a compensated norm product on the old modulus, then lift to an unfactored cubic layer."""
from math import gcd,lcm
from functools import reduce
from z78_proth_primary import dlogmaker,F,pa,root
import json,sys

def solve(j):
    if j<3:raise ValueError('this lifting generator requires j>=3; smaller layers already have direct certificates')
    d=3**(j-1); h=3*d; M=2**d-1; B=lambda a:1+pow(2,a,M);X=lambda a:B(a)**3*pow(B(3*a),-1,M)%M
    o=2*(d//3);rr=[(2**i)%d for i in range(o)];assert len(set(rr))==o and X(1)==3
    G=[X(a)*pow(3,-1,M)%M for a in rr[1:]];f=F(M);ex=lcm(*(p**(e-1)*(p-1) for p,e in f));Z=ex
    while Z%3==0:Z//=3
    logs=[dlogmaker(p**e,p**(e-1)*(p-1),3) for p,e in f if p%3==1];A=pa.matrix(len(logs),len(G),[lg(g) for _,lg in logs for g in G]);t=pow(3,6,M);w=pa.matsolvemod(A,pa.Col([v for v,lg in logs]),pa.Col([lg(t) for v,lg in logs]));assert w.type()!='t_INT'
    # t^(o/6) = 3^o = inverse product of G. o/6 is a power of 3.
    om=o//6;u=pow(Z,-1,om);v=(1-Z*u)//om;e=[(int(x)*Z*u-v)%ex for x in w]
    assert reduce(lambda z,w:z*pow(w[0],w[1],M)%M,zip(G,e),1)==t
    return dict(j=j,d=d,m=(h+1)//2,powers={a:b for a,b in zip(rr[1:],e) if b})
if __name__=='__main__':
    d=solve(int(sys.argv[1]));(root/f'tower-{d["j"]}.json').write_text(json.dumps(d,separators=(',',':'))+'\n');print('old-modulus norm certificate',d['j'],len(d['powers']))
