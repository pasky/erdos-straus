"""U04 pass-1 quick checks on ES counts (Z1508, Z2514, Z2977, Z3143) and Z2985 (hard-set closure under prime factors).
f(n) := #{x<=y<=z positive : 4/n = 1/x+1/y+1/z}. Method: x in [ceil(n/4), floor(3n/4)], then two-term count for
a'/b' = (4x-n)/(nx) via divisors d | b'^2 with d ≡ -b' (mod a'). Memory: divisor lists only. ulimit -v 4000000."""
import json, math, sys
from math import gcd
def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0: f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def divs(fac):
    ds = [1]
    for q, e in fac.items(): ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds
def f_count(n):
    tot = 0
    for x in range((n + 3) // 4, (3 * n) // 4 + 1):
        if 4 * x < n: continue
        a, b = 4 * x - n, n * x
        g = gcd(a, b); a1, b1 = a // g, b // g
        fac = {q: 2 * e for q, e in factor(b1).items()}
        for d in divs(fac):
            if (d + b1) % a1: continue
            y = (d + b1) // a1
            dd = b1 * b1 // d
            if (dd + b1) % a1: continue
            z = (dd + b1) // a1
            if x <= y <= z: tot += 1
    return tot
def isprime(n):
    return n > 1 and all(n % q for q in range(2, int(n**0.5) + 1))
P = [p for p in range(5, 201) if p % 4 == 1 and isprime(p)]
L = [2, 3, 5, 7]
F = {}
for p in P:
    F[p] = f_count(p)
    for l in L: F[l * p] = f_count(l * p)
rows = {}
for l in L:
    ratio = [(p, F[l * p] / F[p]) for p in P]
    mean = sum(r for _, r in ratio) / len(ratio)
    sd = (sum((r - mean) ** 2 for _, r in ratio) / len(ratio)) ** 0.5
    rows[f"l={l}"] = {"mean_ratio_f(lp)/f(p)": round(mean, 3), "sd": round(sd, 3), "min": round(min(r for _, r in ratio), 3), "max": round(max(r for _, r in ratio), 3)}
# Z2977/Z3143: f(p*l^2) vs f(p) f(l) style check: sample 4 primes
rows["sample_f"] = {str(k): F[k] for k in [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97]}
# Z2985 closure check: prime factors of 4p+1, 8p+1, (p+3)/4 for the 9 no-witness primes (C<=30) and 25 hard-profile primes
hard30 = [409, 577, 4357, 4789, 5569, 9601, 12301, 18217, 19141]
hp = json.load(open('data/z52b/hard_profile.json'))
hardset = set(hard30) | set(int(k) for k in hp)
clos = {}
for name, fn in [("4p+1", lambda p: 4 * p + 1), ("8p+1", lambda p: 8 * p + 1), ("(p+3)/4", lambda p: (p + 3) // 4), ("(p-1)/4", lambda p: (p - 1) // 4)]:
    hits = 0; tot = 0; fac_hits = []
    for p in sorted(hardset):
        for q in factor(fn(p)):
            tot += 1
            if q in hardset: hits += 1; fac_hits.append((p, q))
    clos[name] = {"prime_factors_checked": tot, "hard_hits": hits, "examples": fac_hits[:5]}
rows["Z2985_closure"] = clos
rows["n_hardset"] = len(hardset)
print(json.dumps(rows, indent=1))
json.dump(rows, open('data/z52b/pass1/U04/counts_checks.json', 'w'), indent=1)
