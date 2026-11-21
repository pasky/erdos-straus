"""Short-shift divisor budget excluding both outer portions of the dividend's divisor list."""
from z78_bbr import tsum,ceildiv
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt
@lru_cache(None)
def harmonic(b):
    # lower sum of 1/n to b using integer blocks with ratio 1+1/128
    t=1;out=0;R=1<<40
    while t<=b:
        u=min(b,t+t//128);out+=(u-t+1)*R//u;t=u+1
    return F(out,R)
@lru_cache(None)
def band(n,i,j):
    t=1<<i;H=((1<<j)-t)//4;m=(n+(1<<j))//4
    if t**3<m or t*t>n//8 or i<2:return 1<<500
    # H consecutive true M for exact odd N; also valid for n/2 <= N <= n.
    # Any H-length shift band with t divisible by 4 contains exactly H values.
    def lower(b):
        b=min(b,H);return max(0,H*harmonic(b)-b)
    return max(0,4*tsum(n,m,H)-2*lower((t-1)//2)-4*lower(t-1))
