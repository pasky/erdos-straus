"""Pass-2 SK2 Z1863: compare the (star)/C-form existence R(p)>0 with Lopez's Theorem 1 (arXiv:2404.01508 v3):
  p = 4k+1 prime has a solution (du,dv,duv) iff there is t >= 0 and a divisor w of k+1+t with w = -1 (mod 3+4t).
Also tests the shift form of the task (p + B has a divisor = -1 mod 4B) against R(p)>0.
Exact for primes p = 1 mod 4 <= 3000 (t ranges over 0..k; Lopez's bound says t <= (k-13)/3 suffices, checked by brute force).
"""
import json
def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n: ds.append(n // i)
        i += 1
    return ds
def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]
def star_exists(p):
    # exists C>=1, d | 4Cp+1 with d = -1 mod 4C (the (star) / C-form)
    for C in range(1, (p + 2) // 4 + 2):
        N = 4 * C * p + 1
        if any(d % (4 * C) == 4 * C - 1 for d in divisors(N)): return True
    return False
def lopez_exists(p, tmax):
    k = (p - 1) // 4
    for t in range(0, tmax + 1):
        n = k + 1 + t; M = 3 + 4 * t
        if any(w % M == M - 1 for w in divisors(n)): return True
    return False
def shift_exists(p):
    # exists B>=1 with p + B having a divisor = -1 (mod 4B)
    for B in range(1, p + 2):
        n = p + B
        if any(d % (4 * B) == 4 * B - 1 for d in divisors(n)): return True
    return False
res = {"primes": 0, "star_yes": 0, "lopez_yes": 0, "shift_yes": 0,
       "star_vs_lopez_disagree": [], "star_vs_shift_disagree": []}
for p in primes_upto(3000):
    if p < 5 or p % 4 != 1: continue
    res["primes"] += 1
    s = star_exists(p); l = lopez_exists(p, (p - 1) // 4); h = shift_exists(p)
    res["star_yes"] += s; res["lopez_yes"] += l; res["shift_yes"] += h
    if s != l: res["star_vs_lopez_disagree"].append(p)
    if s != h: res["star_vs_shift_disagree"].append(p)
res["star_vs_lopez_disagree_count"] = len(res["star_vs_lopez_disagree"])
res["star_vs_shift_disagree_count"] = len(res["star_vs_shift_disagree"])
json.dump(res, open("data/z52b/pass2/SK2/lopez_check.json", "w"), indent=1)
print({k: v for k, v in res.items() if not isinstance(v, list)}, res["star_vs_lopez_disagree"][:10], res["star_vs_shift_disagree"][:10])
