"""Positive integer cutoffs + explicit Dirichlet divisor remainder (BBR 2012)."""
from z77_routes import *
from z77_pfine import pooled
@lru_cache(None)
def tsum(n,m,H):
    if n//8<9995:return tau_sum(m,H)
    # ln 2 < .694; 2 gamma < 1.16. Both endpoints at least n/8 here.
    log=ceildiv(694*m.bit_length(),1000)
    return min(tau_sum(m,H),ceildiv(H*(100*log+116)+153*rootup(m,3)*log,100))
@lru_cache(None)
def fixed(n,j):
    if j==0:return 0
    t=1<<(j-1);m=(n+2*t)//4;H=ceildiv(t,4)
    s=min(moment(n,j)-moment(n,j-1),2*(1+2*ceildiv(isqrt(m//t),t))*tsum(n,m,H))
    return fixed(n,j-1)+s
@lru_cache(None)
def smallshift(n,j):
    m=(n+(1<<j))//4
    return min([fixed(n,j)]+[fixed(n,i)+4*tsum(n,m,ceildiv((1<<j)-(1<<i),4)) for i in range((rootup(m,3)-1).bit_length(),j)])
if __name__=='__main__':
    import sys
    for b in map(int,sys.argv[1:]):
        n=1<<b
        for j in range(b//3-2,b//2):print(b,j,pooled(n,j),smallshift(n,j),flush=True)
