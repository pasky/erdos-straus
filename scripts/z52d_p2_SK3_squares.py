# z52d pass2 SK3, item Z2912: among (*) witnesses (u,B,C) at the least level, how often are u, B, C, 4uC-1 sums of 2 or 3 squares,
# vs base rate of integers of the same size.  Also Z3020: entropy of the union indicator over levels C<=12 (from Z2317 run).
import math, numpy as np
from collections import defaultdict
def primes1mod4(hi):
    s = bytearray([1])*(hi+1); s[0]=s[1]=0
    for i in range(2, int(hi**0.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [p for p in range(5, hi+1) if s[p] and p % 4 == 1]
HI = 4*40*10**5 + 10
# sums of two squares indicator and three-squares indicator (r3>0) up to HI
sq = np.zeros(HI+1, dtype=bool); sq[0]=True
s2 = np.zeros(HI+1, dtype=bool)
i = 0
while i*i <= HI:
    j = i
    while i*i + j*j <= HI:
        s2[i*i+j*j] = True; j += 1
    i += 1
# three squares: n not of form 4^a(8b+7)
def is3(n):
    while n % 4 == 0: n //= 4
    return n % 8 != 7
ok = [0,0,0]
P = primes1mod4(10**5)
stats = defaultdict(lambda: [0,0,0,0])  # name -> [n, sum2, sum3, total]
for p in P:
    for C in range(1, 41):
        m = 4*C; N = m*p+1; a = m-1; wit = []
        while a*a <= N:
            if N % a == 0:
                u = (a+1)//m; B = (N//a+1)//m; wit.append((u,B))
            a += m
        wit = [(u,B) for (u,B) in wit if math.gcd(u,B)==1 and (u+B)%2==1]
        if wit:
            for (u,B) in wit:
                for name, val in (('u',u),('B',B),('C',C),('4uC-1',4*u*C-1)):
                    st = stats[name]; st[0]+=1; st[1]+= bool(s2[val]); st[2]+= is3(val); st[3]+=1
            break
# base rate: uniform over integers in each (name)'s observed value-range (use same sample of values' distribution -> approximate by all n<=max)
print("name     n_witness  P(sum2 sq)  P(sum3 sq)   [base: P(sum2)~ all n<=X, P(sum3) all n<=X]")
for name, st in stats.items():
    n = st[0]
    print(f"{name:7s} {n:9d}   {st[1]/n:.4f}      {st[2]/n:.4f}")
# base rates by size class
for name in ('u','B','C','4uC-1'):
    pass
X = 10**5
b2 = s2[1:X+1].mean(); b3 = np.mean([is3(n) for n in range(1, X+1)])
print(f"base rate on [1,{X}]: P(sum2)={b2:.4f}  P(sum3)={b3:.4f}")
# Z3020 entropy of union indicator over C<=12 from the Z2317 computation: P(no level)=0.00745
pn = 0.00745
H = -(pn*math.log2(pn) + (1-pn)*math.log2(1-pn))
print(f"Z3020: H(union indicator) = {H:.4f} bits (P(no level<=12)=0.00745, primes<=10^6)")
