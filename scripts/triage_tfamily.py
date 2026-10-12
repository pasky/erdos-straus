# O156 spot-check of ident_form_families Prop 3.4 example p = 27830^2+21, slice (c,d)=(1,22)
from fractions import Fraction as F
from sympy import isprime
t=27830; p=t*t+21; c,d=1,22
print(p, isprime(p), p%840)
for f in (t*t-2*t+23, t*t+2*t+23):
    if (f+p)%(4*c*d)==0:
        a=(f+p)//(4*c*d)
        if (a*p+c)%f==0:
            b=(a*p+c)//f; x,y,z=a*b*d*p,a*c*d,b*c*d
            print("f",f,"sol",x,y,z, F(1,x)+F(1,y)+F(1,z)==F(4,p))
