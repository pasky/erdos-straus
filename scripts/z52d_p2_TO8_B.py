# z52d P2 TO8 batch B: Z3056 (8/n trial form + 3-term check), Z3064 (3-term exceptions m/n), Z3116 (denominator harmonic sums),
# Z3094 (h(-4p) vs R(p)/2 parity), Z3131 (Jacobi/window), Z3163 (reductions of U_n solutions mod q), Z3053 (hit structure)
import sys, math
from math import gcd
from sympy import factorint, primerange
from fractions import Fraction
D = 'data/z52b/pass2/TO8/'
def divisors(n):
    ds=[1]
    for q,e in factorint(n).items(): ds=[d*q**k for d in ds for k in range(e+1)]
    return ds
def two_term(a, b):
    g = gcd(a, b); a //= g; b //= g
    if a == 1: return True
    ds = divisors(b*b)
    return any((d + b) % a == 0 and ((b*b//d) + b) % a == 0 for d in ds)
def three_term(m, n):
    for x in range(-(-n // m), (3*n)//m + 1):
        a = m*x - n
        if a <= 0: continue
        if two_term(a, n*x): return True
    return False
def R_k(k, n):
    # trial form for k/n: #{(u,B,C)>=1: k u B C - u - B = n} = #{(u,C): (kuC-1) | (n+u)}
    cnt = 0; u = 1
    while k*u*1 - 1 <= n + u:
        C = 1
        while k*u*C - 1 <= n + u:
            if (n+u) % (k*u*C-1) == 0: cnt += 1
            C += 1
        u += 1
    return cnt
# ---- Z3056: 8/n
print("Z3056: 8/n three-term reps:", {n: three_term(8, n) for n in [131, 241]}, " 4/n:", {n: three_term(4, n) for n in [131, 241]})
print("   trial-form counts R_8(n) (should be 0 iff no (u,B,C) with 8uBC-u-B=n):", {n: R_k(8, n) for n in [131, 241, 11, 13, 17, 19, 23, 29, 37, 41]})
print("   R_4(n) controls:", {n: R_k(4, n) for n in [131, 241, 409]})
# which n<=400 odd have R_8(n)=0 vs three_term(8,n)?
bad=[]; z=[]
for n in range(3, 400, 2):
    r = R_k(8, n); tt = three_term(8, n)
    if (r > 0) != tt: bad.append(n)
    if not tt: z.append(n)
print("   odd n<400 with 8/n no 3-term:", z[:30], " mismatch R_8>0 vs 3-term:", bad[:10])
# ---- Z3064: 3-term exceptions of m/n, m<=30, n<=300
exc = {}
for m in range(2, 31):
    ex = [n for n in range(max(2,m), 301) if not three_term(m, n)]
    exc[m] = ex
for m in range(2, 31):
    if exc[m]: print(f"Z3064: m={m}: #exceptions n<=300 = {len(exc[m])}, largest {exc[m][-1]}, first {exc[m][:4]}")
    else: print(f"Z3064: m={m}: no exceptions n<=300")
# ---- Z3116: harmonic sums over denominators of all (★) solutions of 4/p for p<=400, p≡1 mod 4 prime
from sympy import primerange
hs = []
for p in primerange(5, 400):
    if p % 4 != 1: continue
    dens = set(); cnt = 0
    u = 1
    while 4*u - 1 <= p + u:
        C = 1
        while 4*u*C - 1 <= p + u:
            if (p+u) % (4*u*C-1) == 0:
                B = (p+u)//(4*u*C-1); cnt += 1
                dens |= {u*B*C, p*B*C, p*u*C}
            C += 1
        u += 1
    s = sum(Fraction(1, d) for d in dens) if dens else 0
    hs.append((p, cnt, float(s)))
print("Z3116: p, #(★)-solutions, sum of 1/denominator over distinct denominators (first 8):", [(p,c,round(h,3)) for p,c,h in hs[:8]])
print("   max harmonic over p<400:", max(hs, key=lambda t: t[2]), " min nonzero:", min((t for t in hs if t[1]>0), key=lambda t:t[2]))
# ---- Z3094: class number h(-4p) (reduced forms count) vs R(p)/2 parity
def h_neg(Dn):  # class number of discriminant Dn<0 (primitive forms), via reduced forms
    h = 0; a = 1
    while 3*a*a <= -Dn:
        for b in range(-a+1, a+1):
            if (b*b - Dn) % (4*a): continue
            c = (b*b - Dn)//(4*a)
            if c < a: continue
            if c == a and b < 0: continue
            if gcd(gcd(a, abs(b)), c) != 1: continue
            h += 1
        a += 1
    return h
R = {}
for l in open(D+'R_all_1e6.txt'):
    p_, r_, _ = l.split(); R[int(p_)] = int(r_)
rows=[]
for p in primerange(5, 3000):
    if p % 4 != 1: continue
    rows.append((p, h_neg(-4*p), (R[p]//2) % 2, R[p]))
print("Z3094: h(-4p) parity is always even?", all(h % 2 == 0 for _,h,_,_ in rows), "; h(-4p) mod 4 vs p mod 8:", all((h%4==0)==(p%8==1) for p,h,_,_ in rows if p>5), "(checked p%8==1 <=> 4|h)")
print("   R(p)/2 odd fraction among these primes:", round(sum(x for _,_,x,_ in rows)/len(rows),3), " ; correlation with h/2 parity:", round(sum(1 for p,h,x,_ in rows if (h//2)%2==x)/len(rows),3))
