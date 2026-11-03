# z55 P415: Nath-Xie (arXiv:2501.16723) constants C, c1, c2, c3 and the ratio 4 c1 c2^2 c3 sqrt(pi)/C (pen = 2.35)
import math
from sympy import primerange
N=2*10**7
g=0.5772156649015329
C=9/4; c1=1; c2=1; P1=1; P3=1
for p in primerange(3,N):
    if p>3: c1*=1+1/(p-2)**2
    c2*=1-1/(p-1)**2
    if p%4==3:
        if p>3: C*=1-(3*p-1)/(p-1)**3
        P3*=math.sqrt(1-1/p)
    else:
        C*=1-1/(p-2)**2
        P1*=math.sqrt(1-1/p)*(1+p*p/(p-1)**3)
c3=2/math.sqrt(math.pi)*P1*P3
print("C",C,"c1",c1,"c2",c2,"c3",c3)
print("ratio 4c1c2^2c3 sqrt(pi)/C =",4*c1*c2*c2*c3*math.sqrt(math.pi)/C)
