"""R41 referee: from-scratch census of a_min(p) for p = 1 (mod 24), p < X (default 1e8).
Checks Remark 9.3: counts, max a_min, argmax, a_min/log p, normalised tails."""
import sys, math
import numpy as np

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8

def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n**.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

def spf_upto(n):
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, int(n**.5) + 1):
        if spf[i] == 0:
            blk = spf[i*i::i]
            blk[blk == 0] = i
            spf[i*i::i] = blk
    idx = np.nonzero(spf == 0)[0]
    spf[idx] = idx
    return spf

ps = primes_upto(X)
ps = ps[ps % 24 == 1]
M = (X + 400) // 4
spf = spf_upto(M)
HARD = {1, 121, 169, 289, 361, 529}

def factor(x):
    f = {}
    while x > 1:
        q = int(spf[x]); e = 0
        while x % q == 0: x //= q; e += 1
        f[q] = e
    return f

def window_ok(p, a):
    x = (p + a) // 4
    if x % p == 0: return False
    S = {1}
    for q, e in factor(x).items():
        qi = pow(q, -1, a); pw = [1]
        for _ in range(e): pw.append(pw[-1] * q % a)
        pwi = [1]
        for _ in range(e): pwi.append(pwi[-1] * qi % a)
        mult = set(pw) | set(pwi)
        S = {s * m % a for s in S for m in mult}
    return (a - 1) in S or ((-p) % a) in S

def amin(p):
    a = 3
    while not window_ok(p, a): a += 4
    return a

nhard = 0; best = (0, 0); ratio = 0.0
amins = np.zeros(len(ps), dtype=np.int32)
for i, p in enumerate(ps.tolist()):
    am = amin(p); amins[i] = am
    if p % 840 in HARD: nhard += 1
    if am > best[0]: best = (am, p)
    ratio = max(ratio, am / math.log(p))
print("#p=1(24) <", X, ":", len(ps), " Mordell-hard:", nhard)
print("max a_min", best, " max a_min/log p", round(ratio, 4))
pb = best[1]
print("argmax QR mod primes<=37:", all(pow(pb, (l - 1) // 2, l) == 1 for l in [3,5,7,11,13,17,19,23,29,31,37]))
for Z in (3, 7, 11, 15, 19, 23):
    J = (Z + 1) // 4; row = []
    for x in (10**6, 10**7, 10**8):
        if x > X: continue
        c = int(np.sum((ps < x) & (amins > Z)))
        row.append(c * math.log(x)**(1 + J / 2) / x)
    print("Z", Z, "normalised tails", [round(r, 5) for r in row],
          "spread", round(max(row) / min(row) - 1, 4))
