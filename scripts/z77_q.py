"""Q compression in both shifts, then a progression determinant. For F <=n."""
from z77_routes import *

@lru_cache(None)
def qsmall(n,j):
    # shift e < 2^j, M=(eF+1)/4; admissible M in AP difference F.
    if not j:return 0
    i=j-1; m=((1<<j)*n+1)//4; H=ceildiv(1<<i,4)
    opts=[]
    for bits,cost in ((i//2,1),(i,2)):
        G=wheel(bits)
        for k in range(3,8):
            A,B,U=major(k,G); opts.append(cost*ceildiv(rootup(m,k)*(H*A+B),U))
    opts.append(2*(1+2*ceildiv(isqrt(m//(1<<i)),1<<i))*tau_sum(m,H))
    return min(opts)+qsmall(n,j-1)

def qc(b):
    n=1<<b; fcut=b//2; layers=[0]*(b+3)
    # Only f >= 2^(b//2). At large f, e use e<= (4a^2d+1)/f, a<=(n+f)/(4cd).
    # For cd large instead of independently summing the pair cap use fixed f paired with c|M then a or d in one class mod f.
    for j in range(fcut,b+1):
        t=1<<j; hi=min(n+2,2*t-1); H=ceildiv(hi-t+1,4); m=(n+hi)//4
        if hi<t:continue
        fb=lo4(t); acc=[0]*len(layers)
        es=edges(n)
        for ic,C in enumerate(es):
            if 4*C>n+hi:break
            for id,D in enumerate(es):
                u=4*C*D
                if u>n+hi:break
                em=((n+hi)**2+4*C*C*D)//(4*C*C*D*t)
                if em<1<<(b//4):break
                c1,d1=es[ic+1]-1,es[id+1]-1
                w=1+(hi-t)//u
                vd=hi4(n*n+4*c1*c1*d1); bd=(c1-C+1)*(d1-D+1)*cap(vd,fb,w)
                acc[min(len(acc)-1,em.bit_length()-1)]+=2*bd
        for i in reversed(range(len(acc)-1)): acc[i]+=acc[i+1]
        for i in range(b//4,b):layers[i]+=acc[i]
    # small f: f ranges over a single class, h=M*a/c=a²d; both orientations charged
    return min((2*moment(n,fcut)+qsmall(n,i)+layers[i],i) for i in range(b//4,b))
if __name__=='__main__':
    import sys
    for b in map(int,sys.argv[1:]):
        v,i=qc(b);print(b,i,v,flush=True)
