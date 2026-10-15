# O240 Theorem B: the Sophie-Germain window class for 3*2^s + 1 through the ET-sterile point mu = 0.
from sympy import symbols, simplify
from fractions import Fraction as F
X=symbols('X'); n=48*X**4+1
x=3*(4*X**4+1); y=6*n*(2*X**2-2*X+1)*(X**2+X+2)/11; z=2*n*(4*X**4+1)*(X**2+X+2)/11
assert simplify(1/x+1/y+1/z-4/n)==0
assert [X0 for X0 in range(11) if (X0**2+X0+2)%11==0]==[4,6]
cnt=0
for s in range(4,4001):
    if s%40 not in (0,12): continue
    Xv=2**((s-4)//4); nv=3*2**s+1; assert nv==48*Xv**4+1
    xv=3*(4*Xv**4+1); yv=F(6*nv*(2*Xv**2-2*Xv+1)*(Xv**2+Xv+2),11); zv=F(2*nv*(4*Xv**4+1)*(Xv**2+Xv+2),11)
    assert yv.denominator==1 and zv.denominator==1 and min(xv,yv,zv)>0 and F(4,nv)==F(1,xv)+1/yv+1/zv
    cnt+=1
print("Theorem B identity OK; exact check of",cnt,"exponents s <= 4000 OK")
