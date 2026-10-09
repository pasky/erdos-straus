"""O98 §4: does averaging over K help for P?  For pairs (a,b), a<=b, 17∤ab, ab <= B, m = 4ab, and every
e | a+b (e < m automatically), find K_min(a,b,e) = least odd K with 17^K ≡ -e (mod m) and 17^K + e >= m
(the P-condition of M17B Lemma 5.1, ignoring 17∤cd, so an over-count).  Report
  E_inf = #(a,b,e) admitting SOME odd K   (what an argument blind to the size of the discrete log can bound),
  E_K   = #(a,b,e) with K_min <= K          (what the cumulative hypothesis actually counts, restricted to these pairs),
  and sum tau(a+b).
Usage: m17c_dlog.py B
"""
import sys, math
from collections import Counter
B = int(sys.argv[1])
def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n: ds.append(n // i)
        i += 1
    return ds
pairs = Einf = tau_sum = 0; Kmins = Counter()
for a in range(1, int(math.isqrt(B)) + 1):
    if a % 17 == 0: continue
    for b in range(a, B // a + 1):
        if b % 17 == 0: continue
        m = 4 * a * b; pairs += 1
        ds = divisors(a + b); tau_sum += len(ds)
        # odd powers 17^K mod m, K = 1,3,5,...; period in this sequence <= ord_m(17)
        first = {}; x = 17 % m; s289 = 289 % m; K = 1
        start = x
        while True:
            if x not in first: first[x] = [K, None]
            K += 2; x = x * s289 % m
            if x == start: break
        period = K - 1  # K-step period of the odd-power sequence
        for e in ds:
            r = (-e) % m
            if r not in first: continue
            K0 = first[r][0]
            # least K = K0 + j*period with 17^K + e >= m
            while 17 ** K0 + e < m: K0 += period
            Einf += 1; Kmins[K0] += 1
print(f"B={B}: pairs={pairs}, sum tau(a+b)={tau_sum}, E_inf={Einf}, E_inf/(B ln^2 B)={Einf/(B*math.log(B)**2):.4f}")
cum = 0
for K in sorted(Kmins):
    cum += Kmins[K]
    if K <= 13 or K in (21, 41, 81, 161, 321, 641, 1281):
        print(f"  K_min<={K}: {cum}")
ks = sorted(Kmins.elements()); print(f"  median K_min = {ks[len(ks)//2]}, max K_min = {ks[-1]}")
print(f"  log17(4B) = {math.log(4*B, 17):.2f}")
