# z52d pass2 NC1 fix round 5: Z1309 Mahler-relation search (with control), Z1776 small-s ES check for 4^s+297 and 15·2^s+1,
# Z1518 Cao–Xu Theorem 2.1 / Prop 2.2 verification (m ≤ 3000), Z1887 equivalent-form conversions round-trip,
# Z1848 control: C≤2 rate in the class 1 mod 840 among all primes.
import math, json, random
from fractions import Fraction
from collections import defaultdict
from sympy import primerange, isprime, divisors, factorint
out = {}
def witness(n, C):
    N = 4*C*n+1; m = 4*C; d = m-1
    while d*d <= N:
        if N % d == 0: return True
        d += m
    return False
def g_of(n, cap=50):
    for C in range(1, cap+1):
        if witness(n, C): return C
    return 0
# --- Z1309: Mahler-type relation search. F(z) = sum_{n>=1} a(n) z^n, a(n) = [g(n) ≤ 2] (all n; g = least C witness).
# Look for P_{j,k} (j ≤ m, k ≤ D, not all zero) with sum_{j,k} P_{jk}(z) F(z^{2^j}) ≡ 0 (mod z^N): linear system over F_P.
PR = 2147483629
def mahler_nullity(a, m, D, N):
    unknowns = [(j, k) for j in range(m+1) for k in range(D+1)]
    rows = []
    for t in range(1, N):
        row = []
        for (j, k) in unknowns:
            s = t - k
            if s >= 0 and s % (2**j) == 0 and s//(2**j) >= 1 and s//(2**j) < len(a):
                row.append(a[s//(2**j)] % PR)
            else:
                row.append(0)
        rows.append(row)
    # rank mod PR
    M = [r[:] for r in rows]; rk = 0; cols = len(unknowns)
    for c in range(cols):
        piv = next((i for i in range(rk, len(M)) if M[i][c]), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]; inv = pow(M[rk][c], PR-2, PR)
        M[rk] = [(x*inv) % PR for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c]:
                f = M[i][c]; M[i] = [(x-f*y) % PR for x, y in zip(M[i], M[rk])]
        rk += 1
    return cols - rk, cols
Nn = 700
a_wit = [0] + [1 if g_of(n) in (1, 2) and g_of(n) != 0 else 0 for n in range(1, Nn+1)]
a_ctrl = [0] + [1 for n in range(1, Nn+1)]   # control: F = z/(1-z), has a Mahler relation of order 1
res = {}
for m, D in [(1, 2), (2, 2), (2, 3), (3, 3)]:
    nw, cols = mahler_nullity(a_wit, m, D, Nn//2**m - 1 if False else 300)
    nc, _ = mahler_nullity(a_ctrl, m, D, 300)
    res[f'm={m},D={D}'] = {'unknowns': cols, 'witness_indicator_nullity': nw, 'control_all_ones_nullity': nc}
out['Z1309_mahler'] = {'series': 'a(n)=[least witness C ∈{1,2}] over n≤700; relation sum_j,k P_jk(z) F(z^{2^j}) ≡ 0 mod z^300',
                       'results': res, 'note': 'nullity 0 => no Mahler relation of this order; control (all ones) must show nullity ≥1'}
# --- Z1776: ES check for 4^s+297 (s=1..6) and 15·2^s+1 (s=1..11): exact 2-term enumeration (divisors of b^2)
def es_solution(n):
    for x in range((n+3)//4, (3*n)//4+1):
        a = 4*x-n
        if a <= 0: continue
        b = n*x
        g = math.gcd(a, b); a2, b2 = a//g, b//g
        f = factorint(b2)
        ds = [1]
        for q, e in f.items(): ds = [dd*q**k for dd in ds for k in range(e+1)]
        ds2 = [1]
        for q, e in f.items(): ds2 = [dd*q**k for dd in ds2 for k in range(2*e+1)]
        # solve a/b2 = 1/y+1/z via (a y - b2)(a z - b2) = b2^2 ; enumerate d | b2^2
        for dd in ds2:
            if (dd + b2) % a2 == 0:
                dp = b2*b2//dd
                if (dp + b2) % a2 == 0:
                    y = (dd+b2)//a2; z = (dp+b2)//a2
                    if y >= 1 and z >= 1: return (x, y, z)
    return None
fam = {}
for s in range(1, 7):
    n = 4**s+297; sol = es_solution(n); fam[f'4^{s}+297={n}'] = sol is not None
for s in range(1, 12):
    n = 15*2**s+1; sol = es_solution(n); fam[f'15*2^{s}+1={n}'] = sol is not None
out['Z1776_small_cases'] = fam
# --- Z1518: Cao–Xu Theorem 2.1 (24m+1 prime iff none of the 8 conditions) and Prop 2.2 (composite forms), m ≤ 3000
def thm21_prime(m):
    conds = [(1, 0, 1, 0)]  # placeholder
    if m == 0: return False
    # (1) m ≡ s mod 24s+1 for some s≥1 with m≠s ; equivalently (2)-(8): m ≡ a s + b mod (24 s + a) with given a,b
    pairs = [(1, 0), (5, 1), (7, 2), (11, 5), (13, 7), (17, 12), (19, 15), (23, 22)]
    for idx, (a, b) in enumerate(pairs):
        for s in range(0, m+2):   # conditions (2)-(8): s ∈ N including 0 (needed: m=1 gives 25 composite)
            M = 24*s + a
            if idx == 0:
                if s == 0: continue   # condition (1) with s ≥ 1 (s=0 would give modulus 1)
                if m != s and (m - s) % M == 0: return False
            else:
                if (m - (a*s + b)) % M == 0: return False
    return True
mis = []
ok = 0
for m in range(1, 3001):
    n = 24*m+1
    pr = isprime(n)
    if thm21_prime(m) != pr: mis.append(m)
    else: ok += 1
out['Z1518_thm21'] = {'s_range': '(1): s>=1; (2)-(8): s>=0', 'm_checked': 3000, 'agreements': ok, 'disagreements(first 10)': mis[:10]}
# --- Z1887: conversions between C-form, witness (C,d), and Type-II (f,f') form ff' − 4c²dp = 1 ... here: C-form <-> witness <-> (u,v)
def cform_from_witness(p, C, d):
    N = 4*C*p+1; e = N//d; u = (d+1)//(4*C); v = (e+1)//(4*C); return (C, u, v)
def witness_from_cform(n, C, u, v):
    return (4*C*u-1)
rt_ok = 0; rt_tot = 0; rt_fail = []
for p in [q for q in primerange(5, 10000) if q % 4 == 1]:
    for C in range(1, 51):
        N = 4*C*p+1; m = 4*C; d = m-1
        while d*d <= N:
            if N % d == 0:
                Cc, u, v = cform_from_witness(p, C, d)
                rt_tot += 1
                ok1 = (4*Cc*u*v - u - v == p)
                x, y, z = Cc*u*v, p*Cc*v, p*Cc*u
                ok2 = Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p)
                ok3 = witness_from_cform(p, Cc, u, v) == d
                if ok1 and ok2 and ok3: rt_ok += 1
                elif len(rt_fail) < 5: rt_fail.append((p, C, d))
            d += m
out['Z1887_roundtrip'] = {'witnesses_tested': rt_tot, 'round_trip_ok': rt_ok, 'failures_first5': rt_fail}
# --- Z1848 control: C ≤ 2 witness rate among all primes ≡ 1 (mod 840) below 10^6 (same table)
rate840 = []
for p in primerange(5, 10**6):
    if p % 840 == 1:
        rate840.append(1 if (witness(p, 1) or witness(p, 2)) else 0)
out['Z1848_control'] = {'primes_1mod840_below_1e6': len(rate840), 'frac_C<=2': round(sum(rate840)/len(rate840), 3)}
print(json.dumps(out, indent=1, default=str))
