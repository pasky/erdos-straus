"""U01 C-form checks: Z1591 (sign variants), Z1784 (canonical-order first success), Z1935/Z1989 (signed slice counts),
Z1731 (mod-q word counts). Certificate equation (standard form in the item): p + u + v = 4Cuv  <=> v = (p+u)/(4Cu-1).
Sign variant (Z1591): p + u - v = 4Cuv <=> v = (p+u)/(4Cu+1)."""
import sys, os, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z52b_p1_U01_common import primes_upto
PR = primes_upto(20000)[2:]
def has_std(p, C):
    for u in range(1, p+1):
        d = 4*C*u - 1
        if (p+u) % d == 0 and (p+u)//d >= 1: return True
    return False
def has_sign(p, C):
    for u in range(1, p+1):
        d = 4*C*u + 1
        if (p+u) % d == 0 and (p+u)//d >= 1: return True
    return False
print("== Z1591: C in 1..20 with a certificate, standard vs sign variant (p≤2000)")
exc_std = {}; exc_sign = {}
for p in PR:
    if p > 2000: break
    for C in range(1, 21):
        if not has_std(p, C): exc_std.setdefault(p, []).append(C)
        if not has_sign(p, C): exc_sign.setdefault(p, []).append(C)
print("primes with no standard certificate for some C≤20:", len(exc_std), "; sign-variant:", len(exc_sign))
print("p with every C≤20 failing (std):", [p for p in exc_std if len(exc_std[p]) == 20][:5], " (sign):", [p for p in exc_sign if len(exc_sign[p]) == 20][:5])
print("first 5 sign-variant failure sets:", list(exc_sign.items())[:5])
print("== Z1784: canonical order (C ascending, then u ascending); index of first success; max index/log^2 p")
best = (0, None); idxs = []
for p in PR:
    if p > 100000: break
    if p < 7: continue
    k = 0; found = None
    for C in range(1, 200):
        for u in range(1, 200):
            k += 1
            d = 4*C*u - 1
            if (p+u) % d == 0: found = k; break
        if found: break
    if found is None: continue
    idxs.append((p, found))
    r = found / (math.log(p)**2)
    if r > best[0]: best = (r, p, found)
print("primes with success in window C,u<200:", len(idxs), "; max index/log^2p =", round(best[0], 3), "at p =", best[1], "index", best[2])
print("sample (p,index):", idxs[:6], " last:", idxs[-3:])
print("== Z1935/Z1989: signed slice counts over N=4Cp+1: S_C(p)=#{d|N: d≡-1 mod 4C} - #{d|N: d≡+1 mod 4C}, C≤30, p≤1e5")
M = 4*30*100000+10
spf = np.zeros(M+1, dtype=np.int32)
for i in range(2, int(M**0.5)+1):
    if spf[i] == 0:
        idx = np.arange(i*i, M+1, i); mask = spf[idx] == 0; spf[idx[mask]] = i
def divs(n):
    f = {}
    while n > 1:
        q = int(spf[n]) if spf[n] else n; e = 0
        while n % q == 0: n //= q; e += 1
        f[q] = e
    ds = [1]
    for q, e in f.items(): ds = [d*q**k for d in ds for k in range(e+1)]
    return ds
Sg = {}
for p in primes_upto(100000)[2:][:3000]:
    row = []
    for C in range(1, 31):
        N = 4*C*p+1
        ds = divs(N)
        row.append(sum(1 for d in ds if d % (4*C) == (4*C-1)) - sum(1 for d in ds if d % (4*C) == 1))
    Sg[p] = row
vals = np.array(list(Sg.values()))
print("S_C(p) for first 3000 primes: fraction zero per C:", [round(float(np.mean(vals[:, c] == 0)), 2) for c in range(0, 30, 6)])
print("sum over C of S_C(p) == 0 for how many primes:", int(np.sum(vals.sum(axis=1) == 0)), "of", len(Sg))
print("== Z1731: N_q(c) = #{(t,u,v) mod q : t·u·v − u − v ≡ c} for prime q≤50, c=1 (p≡1)")
for q in (5, 7, 11, 13, 17, 19, 23):
    cnt = [0]*q
    for t in range(q):
        for u in range(q):
            for v in range(q):
                cnt[(t*u*v - u - v) % q] += 1
    print(q, "N_q(c) range:", min(cnt), max(cnt), "N_q(1)=", cnt[1], "N_q(0)=", cnt[0])
