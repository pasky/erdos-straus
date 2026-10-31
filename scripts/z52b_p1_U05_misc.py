"""z52b pass1 U05 misc cheap checks: Z1477 (gcd of levels), Z1561 (C=2 taxonomy), Z2655 (idoneal test
for U(n) sporadics), Z0711 (record primes mod 4), Z0760 (R(3^k)), Z0857 (isosceles, p≡1(4)), Z1581 (409 forensics)."""
import math, sys
from collections import Counter
from math import gcd
def factor(n):
    f = Counter(); d = 2
    while d*d <= n:
        while n % d == 0: f[d] += 1; n //= d
        d += 1
    if n > 1: f[n] += 1
    return f
def isprime(n):
    if n < 2: return False
    d = 2
    while d*d <= n:
        if n % d == 0: return False
        d += 1
    return True
def divisors(f):
    ds = [1]
    for q, e in f.items():
        ds = [d*q**k for d in ds for k in range(e+1)]
    return ds
def wins(p, C):
    N = 4*C*p + 1; m = 4*C
    return any(d % m == m-1 for d in divisors(factor(N)))
# ---- Z1477 gcd lemma
ok = True; maxov = 0
for p in [5, 13, 17, 29, 37, 41, 1009, 2017]:
    for C1 in range(1, 60):
        for C2 in range(C1+1, 60):
            A, B = 4*C1*p+1, 4*C2*p+1
            g = gcd(A, B)
            if (C2 - C1) % g != 0: ok = False
    # overlap of divisor sets S_C = {d | 4Cp+1, d ≡ -1 mod 4C}
print("Z1477 gcd(4Cp+1,4C'p+1) | (C'-C) verified:", ok)
# exact overlap: common divisors d of both with d ≡ -1 mod lcm(4C,4C') ; bounded by tau(C'-C)
viol = 0
for p in [13, 17, 29, 1009]:
    for C1 in range(1, 40):
        for C2 in range(C1+1, 40):
            A, B = 4*C1*p+1, 4*C2*p+1
            common = [d for d in divisors(factor(gcd(A, B)))]
            if len(common) > len(divisors(factor(C2-C1))): viol += 1
print("Z1477 common-divisor count <= tau(C'-C) violations:", viol)
# ---- Z1561 C=2 taxonomy: C=2 wins iff some sub-product of prime factors of 8p+1 ≡ 7 (mod 8)
def sub_prod_hits(fac, m, target):
    S = {1}
    for q, e in fac.items():
        S = {(s*pow(q, k, m)) % m for s in S for k in range(e+1)}
    return target in S
mism = 0; counts = Counter()
for p in [q for q in range(5, 6000) if isprime(q) and q % 4 == 1]:
    fac = factor(8*p+1)
    w = sub_prod_hits(fac, 8, 7)
    res = {q % 8 for q in fac}
    pred_fail = res <= {1, 3} or res <= {1, 5}
    if w == pred_fail: mism += 1
    counts[('win' if w else 'fail', tuple(sorted(res)))] += 1
print("Z1561 C=2: prime p≡1(4)<6000 with win ⟺ NOT(res⊆{1,3} or res⊆{1,5}) mismatches:", mism)
print("Z1561 residue-set patterns of 8p+1 (win/fail):", dict(counts))
# ---- Z2655 idoneal test on U(n) sporadics: h(-4n) == #genera ?  (brute reduced-form count)
def reduced_forms_count(D):
    # count primitive reduced positive definite forms (a,b,c), b^2-4ac=D, |b|<=a<=c, b>=0 if |b|==a or a==c
    cnt = 0
    a = 1
    while 3*a*a <= -D:
        for b in range(-a+1, a+1):
            if (b*b - D) % (4*a) == 0:
                c = (b*b - D)//(4*a)
                if c < a: continue
                if c == a and b < 0: continue
                if gcd(gcd(a, abs(b)), c) != 1: continue
                cnt += 1
        a += 1
    return cnt
def num_genera(n):
    # number of genera for discriminant D=-4n (Gauss): depends on n mod 8 and odd primes of n
    f = factor(n); odd = [q for q in f if q % 2 == 1]
    mu_odd = len(odd)
    # r = number of odd primes dividing n
    if n % 4 == 3: mu = mu_odd            # Cox Thm 3.15 (D=-4n)
    elif n % 4 in (1, 2): mu = mu_odd + 1
    elif n % 8 == 4: mu = mu_odd + 1
    else: mu = mu_odd + 2                 # n ≡ 0 (mod 8)
    return 2**(mu-1)
for n in [105, 2961, 3985, 25305, 111969, 978145, 15, 11, 14, 35, 510]:
    h = reduced_forms_count(-4*n)
    g = num_genera(n)
    print(f"Z2655 n={n}: h(-4n)={h}, genera={g}, idoneal={h==g}")
# ---- Z0711 record primes mod 4
rec = [2,3,7,11,19,23,47,71,167,191,239,359,479,719,839,1319,1439,2399,5039,6719,9239,10079,55439,110879,166319,18719]
print("Z0711 record primes listed (≥3) mod 4:", Counter(q % 4 for q in rec if q > 2), "18719 mod 4 =", 18719 % 4)
# ---- Z0760 R(3^k) with divisor form R(n)=sum_C #{d|4Cn+1 : d≡-1 (4C)} for n=3^k
def R(n, Cmax):
    tot = 0
    for C in range(1, Cmax+1):
        N = 4*C*n+1
        tot += sum(1 for d in divisors(factor(N)) if d % (4*C) == 4*C-1)
    return tot
print("Z0760 R(3^k) k=1..9 (C≤300):", [R(3**k, 300) for k in range(1, 10)])
# ---- Z0857 isosceles: 2/a + 1/b = 4/p solvable for p≡1 (4)?  (x = y case) and 1/a+2/b (y=z)
def iso(p):
    for a in range(p//2+1, 3*p//4+2):
        num = 4*a - 2*p
        if num <= 0: continue
        if (p*a) % num == 0 and (p*a)//num > 0: return True
    for a in range(p//4+1, p//2+2):
        num = 4*a - p
        if num <= 0: continue
        if (2*p*a) % num == 0 and (2*p*a)//num > 0: return True
    return False
bad = [p for p in range(5, 3000) if isprime(p) and ((p % 4 == 1) == iso(p))]
print("Z0857 isosceles: p≡1(4) with an isosceles solution OR p≡3(4) without (should be empty):", bad[:10], len(bad))
