"""Search fixed words and moving square-limit words for (4^m-1)2^s+1.
Output rows are proof suggestions, never used to infer nonexistence.
"""
from math import gcd
from z75_conjs_period_helper import divisors,order
from z75_thin_cyclo import polys


def extract(k,m,j):
    # x=2^r, r>=4 and r=j mod ord_(k-1)/2(2). Try Phi_(2d)(x), d|m, and constants from k.
    w=k-1; M=8*w; x=pow(2,j+order(2,w//2)*16,M)
    B={d:(d,[]) for d in divisors(k)}
    for d,poly in zip(divisors(m),polys(m)):
        a=sum(c*pow(x,i,M) for i,c in enumerate(poly))%M
        B.update({v*a%M:(e,S+[d]) for v,(e,S) in B.items()})
    # t=7 mod 8 is sufficient for n=1 mod 8
    return B.get((7*w-1)%M)

if __name__=='__main__':
    import sys
    k=int(sys.argv[1]);h=order(2,(k-1)//2); m=int(sys.argv[2]); print('order',h,'degree',m)
    for j in range(1,h+1):print(j,extract(k,m,j))
