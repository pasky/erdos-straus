# z52d P2 TO8: census of (★)-failures (R=0) and b=1 failures (López Type A) among primes p≡1(4), p≤1e6; stats for Z2980/Z3111/Z3138/Z3142
import sys, math
from sympy import factorint, primerange, legendre_symbol
D = 'data/z52b/pass2/TO8/'
R = {int(l.split()[0]): int(l.split()[1]) for l in open(D + 'R_all_1e6.txt')}
B1 = {int(l.split()[0]): int(l.split()[1]) for l in open(D + 'b1_1e6.txt')}
star_fail = sorted(p for p in R if R[p] == 0)
b1_fail = sorted(p for p in B1 if B1[p] == 0)
def lnr(p):
    # least l with (l/p) = -1 (l prime or any l>1 with Legendre -1)
    l = 2
    while True:
        if legendre_symbol(l % p, p) == -1 if l % p else False: return l
        l += 1
print("(★) fail primes ≤1e6:", star_fail)
print("b=1 fail primes ≤1e6:", b1_fail)
def info(p):
    return dict(p=p, p840=p % 840, p24=p % 24, l=lnr(p))
for p in star_fail + b1_fail:
    i = info(p)
    fC = {C: factorint(4 * C * p + 1) for C in range(1, 4)}
    print("p=%d p mod 840=%d (mod 24=%d) least_nonres_l=%d; 4Cp+1 factor C=1,2,3: %s" % (p, i['p840'], i['p24'], i['l'], [fC[C] for C in fC]))
ps = [p for p in R if p > 1000 and p % 24 == 1]
print("controls: number of p≡1 mod 24 primes in (1e3,1e6]:", len(ps))
from collections import Counter
print("p mod 840 for (★)-fail primes:", Counter(p % 840 for p in star_fail))
print("ℓ(p) for (★)-fail:", [lnr(p) for p in star_fail])
print("ℓ(p) for controls (sample 2000):", sorted(Counter(lnr(p) for p in ps[:2000]).items())[:10])
print("ℓ(p) for b1-fail:", [lnr(p) for p in b1_fail])
