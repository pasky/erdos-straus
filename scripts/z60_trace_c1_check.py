# Independent check of the C=1 corollaries of Theorem 2 (no modular-forms package):
#  (k=2)  24*E_{1,2}(n) + 3*(ES_2+TRIV_2) = sigma(N) + 2*[N square]
#  (k=3)  ES_3 - TRIV_3 = -8*E_{1,3}(n) + (a(N) + 4*lam)/3,  a = coefficients of eta(4z)^6 computed from
#         the Hecke character of Q(i):  a(N) = (1/4) sum_{x^2+y^2=N} (x+iy)^2 * psi,  realised as sum over x odd, y even of (x^2-y^2)
import sys
from fractions import Fraction
from math import isqrt
import cypari2
pari=cypari2.Pari()
def H(D): return Fraction(str(pari.qfbhclassno(D)))
def a_eta6(N):
    # eta(4z)^6 = sum over (x,y), x odd >0? use: a(N) = (1/2) sum_{x odd, y even, x^2+y^2=N} (x^2 - y^2)  (x over +-, y over +-)
    tot=0
    for x in range(-isqrt(N), isqrt(N)+1):
        if x%2==0: continue
        r=N-x*x
        if r<0: continue
        y=isqrt(r)
        if y*y==r and y%2==0:
            for yy in ({y,-y}):
                tot+= x*x-yy*yy
    return Fraction(tot,2)
bad2=bad3=0; nmax=int(sys.argv[1])
for n in range(1,nmax+1):
    N=4*n+1
    E2=Fraction(0);E3=Fraction(0)
    for s in range(max(1,(n-2*isqrt(n)-4)//4), (n+2*isqrt(n)+8)//4+1):
        w=4*s-n
        if w*w<4*s:
            h=H(4*s-w*w); E2+=h; E3+=(4*w-2)*h
    ES2=ES3=TR2=TR3=0
    for d in range(1,isqrt(N)+1):
        if N%d==0:
            e=N//d; mult=1 if d==e else 2
            if d%4==3: ES2+=mult*d; ES3+=mult*d*d
            if d%4==1 and e%4==1: TR2+=mult*d; TR3+=mult*d*d
    sig=int(pari.sigma(N))
    r=isqrt(N); sq=(r*r==N); lam = (r if (r+1)%4==0 else -r) if sq else 0
    if 24*E2+3*(ES2+TR2)!=sig+(2 if sq else 0): bad2+=1
    if ES3-TR3 != -8*E3 + (a_eta6(N)+4*lam)/3: bad3+=1; 
    if bad3==1 and ES3-TR3 != -8*E3 + (a_eta6(N)+4*lam)/3: print("k3 mismatch",n,ES3,TR3,E3,a_eta6(N),lam)
print(f"n<= {nmax}: k=2 mismatches {bad2}, k=3 mismatches {bad3}")
