"""R41 referee: from-scratch N_3(x)/(x (log x)^{-3/2}) at x=1e6..1e9 (Remark 6.4).
Works on the progression p = 840k+1, n = (p+3)/4 = 210k+1."""
import sys, math
import numpy as np

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9
K = X // 840 + 1                      # k = 0..K-1, p = 840k+1
def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n**.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

isp = np.ones(K, dtype=bool); isp[0] = False          # p=1 not prime
for l in primes_upto(int(X**.5) + 1).tolist():
    if 840 % l == 0: continue
    k0 = (-pow(840, -1, l)) % l                        # 840k+1 = 0 mod l
    start = k0 if 840 * k0 + 1 > l else k0 + l          # do not strike p = l
    isp[start::l] = False
bad = np.zeros(K, dtype=bool)                         # n has a prime factor = 2 (3)
for l in primes_upto(X // 4 + 1).tolist():
    if l % 3 != 2 or 210 % l == 0: continue           # 2,5 never divide n
    k0 = (-pow(210, -1, l)) % l                        # 210k+1 = 0 mod l
    bad[k0::l] = True
good = isp & ~bad
ks = np.arange(K, dtype=np.int64); ps = 840 * ks + 1
x = 10**6
while x <= X:
    c = int(np.sum(good & (ps <= x)))
    print(f"x=1e{round(math.log10(x))}: N3={c}  ratio={c * math.log(x)**1.5 / x:.5f}")
    x *= 10
