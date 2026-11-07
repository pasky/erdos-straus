# Identity-class coverage mod M.
# Identity classes (each gives an explicit polynomial ES solution for every prime p in the class, p large):
#  case (ii): p+s = 4g'YZ, s | Y+Z  (R = subfamily s=Y+Z)
#   (A) fix (Y,Z,s):   p = -s            (mod 4YZ),        s | Y+Z
#   (B) fix (g',Y,m):  p = -Y m^{-1}     (mod D=4g'Ym-1)   [D=3 mod 4, Ym | (D+1)/4]
#   (C) fix (g',Y,s):  p = -(s+4g'Y^2)   (mod 4g'Ys)
#  case (i): pt+1 = 4abh, gcd(a,b)=1, t | a+b, t=3 mod 4
#   (A') fix (a,b,t):  p = -t^{-1}       (mod 4ab),        t | a+b, gcd(t,2ab)=1
#   (B') fix (a,h,t):  p = -(4a^2h+1)/t  (mod 4ah),        t | 4a^2h+1
# Output: residues a mod M, gcd(a,M)=1, a=1 mod 4, not in any class with modulus | M.
import sys
from math import gcd
from sympy import divisors, factorint, jacobi_symbol
def classes(M):
    cl=set()  # (c mod D, D)
    for D in divisors(M):
        if D%4==0:
            L=D//4
            for Y in divisors(L):
                Z=L//Y
                for s in divisors(Y+Z): cl.add((( -s)%D,D,'A'))
                # (C): D/4 = g' Y s
                for s in divisors(Z):
                    g=Z//s
                    cl.add(((-(s+4*g*Y*Y))%D,D,'C'))
                # (A'): a=Y,b=Z coprime
                if gcd(Y,Z)==1:
                    for t in divisors(Y+Z):
                        if t%4==3 and gcd(t,2*L)==1:
                            cl.add(((-pow(t,-1,D))%D,D,"A'"))
                # (B'): a=Y,h=Z
                a,h=Y,Z
                for t in divisors(4*a*a*h+1):
                    if t%4==3:
                        cl.add(((-(4*a*a*h+1)//t)%D,D,"B'"))
        elif D%4==3:
            e=(D+1)//4
            for Y in divisors(e):
                for m in divisors(e//Y):
                    cl.add(((-Y*pow(m,-1,D))%D,D,'B'))
    return cl
def uncovered(M,cl=None):
    cl=cl if cl is not None else classes(M)
    cov=bytearray(M)
    for c,D,_ in cl:
        for a in range(c,M,D): cov[a]=1
    return [a for a in range(1,M,4) if gcd(a,M)==1 and not cov[a]]
def is_square_class(a,M):
    f=factorint(M)
    for q,e in f.items():
        if q==2:
            if e>=3 and a%8!=1: return False
            if e==2 and a%4!=1: return False
        elif jacobi_symbol(a,q)!=1: return False
    return True
if __name__=="__main__":
    M=int(sys.argv[1])
    cl=classes(M)
    un=uncovered(M,cl)
    nsq=[a for a in un if not is_square_class(a,M)]
    print(f"M={M}: #classes={len(cl)}, uncovered={len(un)}, non-square uncovered={len(nsq)}")
    if len(un)<60: print("uncovered:",un)
    if len(nsq)<60: print("non-square uncovered:",nsq)
