"""Pass-2 SK2 (items Z1967, Z1663, Z1310, Z1311).
Z1967: x = p t slices. 4/p - 1/(p t) = a/b with a=4t-1, b=p t. a/b = 1/y+1/z solvable (positive ints) iff
  exists divisor d of b^2 with d = -b (mod a) and b^2/d = -b (mod a)   [from (ay-b)(az-b)=b^2].
  Exact, finite (divisors of b^2 = p^2 t^2). Also tests the x=p branch (t=1 gives 3/p).
Z1663: isosceles (x=y) solutions of 4/p = 2/x+1/z  <=> (4x-2p)(4z-p)=2p^2 (exact, 6 divisors of 2p^2 for prime p).
Z1310/1311: local solution counts of F(u,B,C)=4uBC-u-B mod q^k (k=1,2) and singularity check.
Memory: small. Run: uv run --with sympy python scripts/z52d_p2_SK2_slices.py  (no sympy used; plain python)
"""
import json, math
from collections import Counter, defaultdict

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]

def divisors_of_square_factor(p, t):
    # divisors of (p*t)^2 via factorisation of t and p
    fac = defaultdict(int)
    fac[p] += 2
    m = t; f = 2
    while f * f <= m:
        while m % f == 0: fac[f] += 2; m //= f
        f += 1
    if m > 1: fac[m] += 2
    ds = [1]
    for q, e in fac.items():
        ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds

def two_term_solvable(a, b, divs):
    for d in divs:
        e = b * b // d
        if (d + b) % a == 0 and (e + b) % a == 0:
            return True
    return False

out = {}
P = [p for p in primes_upto(100000) if p % 24 == 1]
T = list(range(1, 31))
res = {t: {"n": 0, "solvable": 0} for t in T}
for p in P:
    for t in T:
        divs = divisors_of_square_factor(p, t)
        res[t]["n"] += 1
        if two_term_solvable(4 * t - 1, p * t, divs):
            res[t]["solvable"] += 1
out["Z1967_slice_x_eq_pt_p_1mod24_le1e5"] = {
    "n_primes": len(P),
    "frac_solvable_by_t": {str(t): round(res[t]["solvable"] / res[t]["n"], 4) for t in T},
}
# t = 1 branch (x = p): 3/p = 1/y+1/z solvable iff p = 2 mod 3 (check on all primes <= 1e5, p=1 mod 4)
ok_t1 = []
for p in primes_upto(100000):
    if p < 5 or p % 4 != 1: continue
    s = two_term_solvable(3, p, divisors_of_square_factor(p, 1))
    ok_t1.append((p % 3, s))
out["Z1967_t1_3_over_p_by_p_mod3"] = {str(r): [sum(1 for m, s in ok_t1 if m == r and s), sum(1 for m, s in ok_t1 if m == r)] for r in [1, 2]}

# Z1663: isosceles check for ALL primes <= 1e6 (exact, via divisors of 2p^2)
iso_hits = []
pl = primes_upto(1000000)
for p in pl:
    if p == 2: continue
    divs = [1, 2, p, 2 * p, p * p, 2 * p * p]
    found = False
    for d in divs:  # d = 4x - 2p, e = 4z - p, d*e = 2p^2
        e = 2 * p * p // d
        if (d + 2 * p) % 4 == 0 and (e + p) % 4 == 0:
            x = (d + 2 * p) // 4; z = (e + p) // 4
            if x >= 1 and z >= 1:
                found = True; break
    if found: iso_hits.append(p)
out["Z1663_isosceles_primes_le1e6"] = {
    "n_primes": len(pl) - 1,
    "primes_with_isosceles_solution": len(iso_hits),
    "all_isosceles_are_p_mod4_eq_3": all(p % 4 == 3 for p in iso_hits),
    "first_isosceles_primes": iso_hits[:12],
    "count_p1mod4_with_isosceles": sum(1 for p in iso_hits if p % 4 == 1),
}
# brute-force cross-check of the reduction for p <= 200
bf_ok = True
for p in primes_upto(200):
    if p == 2: continue
    brute = False
    for x in range(1, 4 * p + 2):
        # 4/p - 2/x = 1/z  => z = px/(4x-2p)
        if 4 * x - 2 * p > 0 and (p * x) % (4 * x - 2 * p) == 0:
            brute = True; break
    red = p in iso_hits
    if brute != red: bf_ok = False
out["Z1663_bruteforce_crosscheck_p_le_200"] = bf_ok

# Z1310/1311: local counts of F = 4uBC - u - B over Z/q^k, and singular points mod q
def local_counts(q, k):
    m = q ** k
    cnt = Counter()
    for u in range(m):
        for B in range(m):
            for C in range(m):
                cnt[(4 * u * B * C - u - B) % m] += 1
    return cnt
loc = {}
for q in [3, 5, 7]:
    c1 = local_counts(q, 1)
    loc[f"q={q}"] = {"N_mod_q(a)": {str(a): c1[a] for a in range(q)},
                     "uniform_would_be": q * q}
# singular points: gradient (4BC-1, 4uC-1, 4uB) mod q all zero and F = 0 mod q
sing = {}
for q in [3, 5, 7, 11, 13]:
    s = []
    for u in range(q):
        for B in range(q):
            for C in range(q):
                if (4*B*C-1) % q == 0 and (4*u*C-1) % q == 0 and (4*u*B) % q == 0:
                    s.append((u, B, C))
    sing[str(q)] = len(s)
out["Z1310_singular_points_mod_q"] = sing
out["Z1310_local_counts_q_3_5_7_k1"] = loc
json.dump(out, open("data/z52b/pass2/SK2/slices_checks.json", "w"), indent=1)
print(json.dumps(out, indent=1))
