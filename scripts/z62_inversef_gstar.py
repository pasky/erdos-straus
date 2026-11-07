# R(p) for the 38 G*-zero primes (data/z58/screens/gstar_zeros.txt) that are not among the 14 R-zeros.
# R = #{(u,B): 4uB | p+u+B}; since 4uB <= p+u+B forces min(u,B) <= U0 := isqrt(p)+2, count via symmetry.
from sympy import divisors
from math import isqrt
Z=set(int(l.split()[0]) for l in open('data/z58/screens/star_prime_zeros.txt') if l[0].isdigit())
G=[int(l.split()[0]) for l in open('data/z58/screens/gstar_zeros.txt') if l[0].isdigit()]
def R(p):
    U0=isqrt(p)+2; both=0; one=0
    for u in range(1,U0+1):
        for d in divisors(p+u):
            if d%(4*u)==4*u-1:
                B=(p+u)//d
                if B<=U0: both+=1
                else: one+=1
    return 2*one+both
assert R(409)==0 and R(449)==6 and R(5)==2
rs=[(p,R(p)) for p in G if p not in Z]
print(len(G),"G*-zeros;",len(rs),"not R-zeros; their R values:",sorted(set(r for _,r in rs)))
print(rs)
