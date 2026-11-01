# 4*3^k+1 ≡ 5 (mod 8) for all k>=1  => (★) with u=1,B=2 (n ≡ -3 mod 8) gives a solution
from fractions import Fraction as F
for k in range(1,40):
    n=4*3**k+1; assert n%8==5
    x=(n+3)//4; m=(n-5)//8
    assert F(4,n)==F(1,x)+F(1,n*(m+1))+F(1,2*n*(m+1))
print('ok k<40')
