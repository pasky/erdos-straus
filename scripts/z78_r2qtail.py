"""Uniform high-Q bound by the 3x3 determinant and the smallest pair."""
from z76_lift import rootup,ceildiv
from fractions import Fraction as F

def qnorm(n):
    # For all F >= n >= 2^80, return A s.t. D_oriented(F)/F <= A (n/F)^(1/4).
    # g=pair<=F^(2/3). V<=5F²; in each f octave at most 2(1+2(5F²)^(1/3)/(4g)).
    # #pairs<=Y(1+ln Y); sum 1/(ij) <= (1+ln Y)^2.
    b=n.bit_length(); l=F(694*b,1000);u=1+2*l/3;bins=b+2
    # Two routes paying per f octave: (ac),(cd); (ad) at most two once.
    # replace 5^(1/3) by 2, giving <=2(1+F^(2/3)/g).
    return (4*u+8*bins*(u+u*u))/(rootup(n,3)-1)

def geom(r,g,b):
    # Upward bound to sum_m r^(-2mg/b) by an exactly rounded 64-bit multiplier
    scale=1<<64;q=rootup(ceildiv(scale**b,r**(2*g)),b);assert q<scale
    return F(scale,scale-q)
