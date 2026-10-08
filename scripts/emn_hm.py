"""O94: check Lemma 2.1 of EXCEPTIONAL_MN.md numerically.
S_m(x)=sum_{j<=x,(j,m)=1} 1/j >= (phi(m)/m) log x for x>=m^2;
h_m(K)=sum_{k<=K,(k,m)=1} phi(k)/k^2 >= 0.54 S_m(K);
sum_{k<=K,(k,m)=1,p|k} phi(k)/k^2 <= S_m(K)/p."""
import sys, math
from sympy import totient, primerange
K = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
ph = list(range(K + 1))
for p in primerange(2, K + 1):
    for j in range(p, K + 1, p):
        ph[j] -= ph[j] // p
bad = 0
for m in list(range(4, 61)) + [210, 2310, 30030, 4096, 9973]:
    if m * m > K: continue
    cop = [math.gcd(k, m) == 1 for k in range(K + 1)]
    S = sum(1 / j for j in range(1, K + 1) if cop[j])
    h = sum(ph[k] / k**2 for k in range(1, K + 1) if cop[k])
    rat = int(totient(m)) / m
    for x in (m * m, K):
        Sx = sum(1 / j for j in range(1, x + 1) if cop[j])
        if Sx < rat * math.log(x): bad += 1; print("S fail", m, x)
    if h < 0.54 * S: bad += 1; print("h fail", m)
    for p in (3, 5, 7, 11, 101):
        if m % p == 0: continue
        sp = sum(ph[k] / k**2 for k in range(p, K + 1, p) if cop[k])
        if sp > S / p: bad += 1; print("p fail", m, p)
    print(m, f"S/(rat logK)={S/(rat*math.log(K)):.3f} h/S={h/S:.3f}")
print("failures", bad)
