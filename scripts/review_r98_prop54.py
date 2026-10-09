"""R98: from-scratch check of paper Prop 5.4 (x* = x(2,2) lies in II3 (8,33,11999) and I2 (125,88,11999)),
using only the ET Prop 1.9 class definitions and the paper's solution table."""
from fractions import Fraction as Fr
from sympy import isprime, factorint
from math import gcd
def part(M,qs):
    r=1
    for q in qs:
        while M%q==0: M//=q; r*=q
    return r
def lift(M,u):  # x(u): 1 off T, u at 11,13
    MT=part(M,(11,13)); Mp=M//MT
    from sympy.ntheory.modular import crt
    return int(crt([Mp,MT],[1%Mp,u%MT])[0])%M
a,d,e=8,33,11999
M=4*a*d*e; r=(-4*a*a*d-e)%M
print('II3 M',M,factorint(M),'r',r, 'gcd(4ad,e)',gcd(4*a*d,e))
MT=part(M,(11,13)); print(' M_T',MT,'M\'',M//MT,'r mod M\'',r%(M//MT),'r mod M_T',r%MT, 'lift==r',lift(M,2)==r)
# I2 (a,c,f): n≡-f (4ac), n≡-c/a (f), (4ac,f)=1
A,C,F=125,88,11999
M2=4*A*C*F; n=lift(M2,2)
print('I2 M',M2,'gcd',gcd(4*A*C,F),'x* in class:',(n+F)%(4*A*C)==0 and (n*A+C)%F==0,'residue',n)
# II3 solution at p
p=r; print('p prime',isprime(p),'p mod 11,13',p%11,p%13)
c=Fr(p+4*a*a*d+e,4*a*d*e); b=c*e-a; assert c.denominator==1 and b==Fr(p+e,4*a*d)
x,y,z=a*b*d, a*c*d*p, b*c*d*p
print('sol',x,y,z,'identity',Fr(4,p)==1/Fr(x)+1/Fr(y)+1/Fr(z))
# I2 solution: d=(n+f)/(4ac), b=(na+c)/f, pi^I=(abdn,acd,bcd)
d2=Fr(p+F,4*A*C); b2=Fr(p*A+C,F)
print('I2 at p: integral',d2.denominator==1 and b2.denominator==1, 'p in I2 class', (p+F)%(4*A*C)==0 and (p*A+C)%F==0)
