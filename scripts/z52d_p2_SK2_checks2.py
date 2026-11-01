"""Pass-2 SK2 small exact checks: (a) Z1308 C=1 identity R_1(p) = (tau(4p+1) - r2(4p+1)/4)/2 for primes p = 1 mod 4 <= 2e4;
(b) Z1767 Coppersmith-regime fraction from the winning-pair file (p <= 1e5, C <= 500).
Inputs: /tmp/z52d_p2_SK2/pairs_*.txt and p7_all.txt (see z52d_p2_SK2_profile.c). Output: data/z52b/pass2/SK2/checks2.json
"""
import math, glob, json
from collections import defaultdict
def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]
def divs(N):
    fs = {}; m = N; f = 2
    while f * f <= m:
        while m % f == 0: fs[f] = fs.get(f, 0) + 1; m //= f
        f += 1
    if m > 1: fs[m] = fs.get(m, 0) + 1
    ds = [1]
    for q, e in fs.items(): ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds
def r2(N):
    c = 0; a = 0
    while a * a <= N:
        b2 = N - a * a; b = math.isqrt(b2)
        if b * b == b2: c += (1 if a == 0 else 2) * (1 if b == 0 else 2)
        a += 1
    return c
ok = bad = 0
for p in primes_upto(20000):
    if p % 4 != 1: continue
    N = 4 * p + 1
    R1 = sum(1 for d in divs(N) if d % 4 == 3)
    if abs(R1 - (len(divs(N)) - r2(N) // 4) / 2) < 1e-9: ok += 1
    else: bad += 1
rows = []
for fn in glob.glob('/tmp/z52d_p2_SK2/pairs_*.txt'):
    for l in open(fn):
        a = l.split(); rows.append((int(a[0]), int(a[1])))
winC = defaultdict(list)
for p, C in rows: winC[p].append(C)
ps = [int(l.split()[0]) for l in open('/tmp/z52d_p2_SK2/p7_all.txt') if int(l.split()[0]) <= 100000]
n_any = n_big = 0
for p in ps:
    Cs = winC.get(p, [])
    if Cs:
        n_any += 1
        if max(Cs) >= p ** (1 / 3) / 4: n_big += 1
res = {"Z1308_C1_identity_ok": ok, "Z1308_C1_identity_bad": bad,
       "Z1767_primes_1mod4_le_1e5": len(ps), "Z1767_with_certificate_C_le_500": n_any,
       "Z1767_with_certificate_C_ge_p^(1/3)/4_le_500": n_big}
json.dump(res, open('data/z52b/pass2/SK2/checks2.json', 'w'), indent=1)
print(res)
