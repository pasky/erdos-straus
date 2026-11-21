"""Integer geometric tail anchored at N0=2^B: coefficient at N0 times (N0/N)^(G/B)."""
from z76_lift import major,ceildiv,rootup
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

def coef(row):
    B,J,G,H,*cs=row;anchor=1<<B;U=(B+2)//3
    # For S>=2, log N <= B*(S/2)^2. Use B rather than B ln 2.
    # Any linear-log factor (log N+2) <= (B+2)*(S/2)^2.
    def rate(E,log=0):return E+2*log<=B//2-G
    def tau_sum(i): # e<S^i, at most S^i/4+1 positions; M<=N
        return (F(1<<i,4)+1)*(B+2)+2*rootup(anchor,3)*B
    opts=[]
    for i in range(B//5,B//3):
        for k in range(4,8):
            if not rate(i+F(B,k)):continue
            A,D,u=major(k,1)
            c=rootup(anchor,k)*((F(1<<i,4)+1)*A+D)/u
            if not rate(F(B-3*i,2)+U,1) or not rate(J,1):continue
            c+=(6+4*rootup(1<<(B-3*i),2))*tau_sum(U) if B>=3*i else 10*tau_sum(U)
            c+=4*tau_sum(J);opts.append(c)
    assert opts and J>=U
    return (min(opts)+sum(c<<i for i,c in enumerate(cs)))/(1<<(B//2))
if __name__=='__main__':
    import sys
    for line in open(sys.argv[1]):
        row=list(map(int,line.split()));print(row[:4],float(coef(row)))
