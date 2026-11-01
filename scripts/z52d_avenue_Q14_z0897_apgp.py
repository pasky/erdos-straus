# Z0897: 4/n = 1/(y-d) + 1/y + 1/(y+d) (AP, d>=1) and geometric x,y=xr,z=xr^2 (rational ratio) for n <= NMAX
# AP: n(3y^2 - d^2) = 4y(y^2-d^2). Search y up to n (x>=n/4 => y-d >= n/4 ... y <= 3n/4*? bounded), d < y.
from fractions import Fraction
import math
NMAX=400
ap=[];gp=[]
for n in range(2,NMAX+1):
    found=False
    # x=y-d >= n/4 (smallest denominator >= n/4 as 1/x < 4/n), and x <= 3n/4
    for x in range(n//4+1, 3*n//4+2):
        for d in range(1, 4*x):  # 1/x < 4/n bounds; z=x+2d; need 1/(x+d)+1/(x+2d) = 4/n-1/x
            r=Fraction(4,n)-Fraction(1,x)
            if r<=0: break
            s=Fraction(1,x+d)+Fraction(1,x+2*d)
            if s==r: ap.append((n,x,x+d,x+2*d)); found=True; break
            if s<r: break
        if found: break
    # geometric with integer denominators: y^2 = xz
    gfound=False
    for x in range(n//4+1, 3*n//4+2):
        r=Fraction(4,n)-Fraction(1,x)
        if r<=0: continue
        # 1/y+1/z = r with z=y^2/x; y from x..
        for y in range(x, int(2/r)+2):
            if (y*y)%x: continue
            z=y*y//x
            if Fraction(1,y)+Fraction(1,z)==r: gp.append((n,x,y,z)); gfound=True; break
        if gfound: break
print("AP n:", [t[0] for t in ap][:60], len(ap))
print("AP examples:", ap[:8])
print("GP n:", [t[0] for t in gp][:60], len(gp))
print("GP examples:", gp[:8])
