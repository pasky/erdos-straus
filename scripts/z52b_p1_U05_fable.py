"""z52b pass1 U05 — free_fable items (Z1478, Z1512, Z1596, Z1608, Z1477, Z1561).
C-form: p prime, p≡1 (4), C≥1; win(p,C) iff some divisor d of N=4Cp+1 has d ≡ -1 (mod 4C).
Usage: ulimit -v 4000000; python3 scripts/z52b_p1_U05_fable.py > data/z52b/pass1/U05/fable.txt
"""
import math, sys
from collections import Counter, defaultdict
PMAX, CMAX = 6000, 150
NMAX = 4*CMAX*PMAX + 1
spf = list(range(NMAX+1))
for i in range(2, int(NMAX**0.5)+1):
    if spf[i] == i:
        for j in range(i*i, NMAX+1, i):
            if spf[j] == j: spf[j] = i
def factor(n):
    f = Counter()
    while n > 1:
        q = spf[n]; f[q] += 1; n //= q
    return f
def primes_upto(n):
    s = bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
def full_divisor_hits(fac, m):
    """True iff some divisor of N is ≡ -1 mod m (fac = factorisation of N)."""
    S = {1 % m}
    for q, e in fac.items():
        qm = q % m
        S = {(s*pow(qm, k, m)) % m for s in S for k in range(e+1)}
    return (m-1) % m in S
def subgroup_contains(gens, m):
    H = {1 % m}; frontier = [1 % m]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = (x*g) % m
            if y not in H: H.add(y); frontier.append(y)
    return (m-1) % m in H
def f2_relax(fac, m):
    """Necessary condition: some squarefree subset product of prime factors is ≡ -1 times a square (mod m)."""
    sq = {(x*x) % m for x in range(m) if math.gcd(x, m) == 1}
    D = {1 % m}
    for q in fac:
        qm = q % m
        D = D | {(d*qm) % m for d in D}
    return any(((-d) % m) in sq for d in D)
def distinct_subset_size(fac, m):
    D = {1 % m}
    for q in fac:
        qm = q % m
        D = D | {(d*qm) % m for d in D}
    return len(D)
def phi(n):
    return sum(1 for k in range(1, n+1) if math.gcd(k, n) == 1)
ps = [p for p in primes_upto(PMAX) if p % 4 == 1 and p > 4]
print(f"primes p≡1(4), 5<=p<={PMAX}: {len(ps)}; C<={CMAX}")
# tallies
tot = 0; wins = 0
fail_by_omega = Counter(); fail_total = Counter(); sub_fail_by_omega = Counter()
sub_contains_fail = 0; sub_contains_total = 0; sub_contains_fail_small = 0
# Z1512 subset: p<3000, C<40
z1512 = Counter()
# Z1608: rich failures Omega>=5
rich = Counter(); rich_sub = Counter()
# Z1596: omega>=6 failures
om6 = Counter(); om6_sub = Counter()
# Z1478: F2 relaxation vs full
f2 = Counter()
# subset size vs phi regime (failures with 2^omega >= phi(4C))
regime = Counter()
agree = Counter(); nosub_rel = Counter()
for p in ps:
    for C in range(1, CMAX+1):
        m = 4*C; N = m*p + 1
        fac = factor(N)
        tot += 1
        w = full_divisor_hits(fac, m)
        gens = [q % m for q in fac]
        sub = subgroup_contains(gens, m)
        r = f2_relax(fac, m)
        om = len(fac); Om = sum(fac.values())
        if w: wins += 1
        if sub:
            sub_contains_total += 1
            if not w: sub_contains_fail += 1
        if p < 3000 and C < 40:
            z1512['pairs'] += 1
            if sub: z1512['subgroup_has_minus1'] += 1; z1512['sub_and_fail'] += (not w)
            z1512['fail'] += (not w)
        if not w:
            fail_total[om] += 1
            if sub: sub_fail_by_omega[om] += 1
            if Om >= 5:
                rich['fail'] += 1; rich['sub'] += sub
            if om >= 6:
                om6['fail'] += 1; om6['sub'] += sub
            regime['fail'] += 1
            regime['2^omega>=phi(4C)'] += (2**om >= phi(m))
            regime['2^omega>=phi(4C) & sub'] += (2**om >= phi(m) and sub)
        f2[(w, r)] += 1
        agree[(om, sub, w)] += 1
        if not sub: nosub_rel[(om, r, w)] += 1
print(f"total (p,C): {tot}, wins: {wins}")
print("Z1512 (p<3000,C<40): pairs", z1512['pairs'], "fail", z1512['fail'],
      "| subgroup∋-1:", z1512['subgroup_has_minus1'], "of which fail:", z1512['sub_and_fail'])
print("Fail count by omega(N):", dict(sorted(fail_total.items())))
print("Failures with subgroup∋-1 by omega:", dict(sorted(sub_fail_by_omega.items())))
print("Z1608 rich failures (Omega>=5): fail", rich['fail'], "subgroup-type", rich['sub'],
      f"({rich['sub']/max(1,rich['fail']):.2%})")
print("Z1596 omega>=6 failures:", om6['fail'], "subgroup-type", om6['sub'],
      f"({om6['sub']/max(1,om6['fail']):.2%})")
print("Regime 2^omega>=phi(4C) among failures:", regime['2^omega>=phi(4C)'], "of", regime['fail'],
      "| of those subgroup-type:", regime['2^omega>=phi(4C) & sub'])
print("Z1512 breakdown by omega(N): omega, #pairs, #sub∋-1, #sub∋-1 & no win, #sub∋-1 & win, #no-sub & win (must be 0)")
for om in sorted({k[0] for k in agree}):
    a = sum(v for k,v in agree.items() if k[0]==om)
    s1 = agree[(om,True,False)]+agree[(om,True,True)]
    print(om, a, s1, agree[(om,True,False)], agree[(om,True,True)], agree[(om,False,True)])
print("Z1478 F2-relaxation table (full_win, relax_holds): ", dict(f2))
print("  -> relax fails but win:", f2[(True, False)], "(must be 0 if relaxation is necessary)")
print("  -> relax holds, no win:", f2[(False, True)], "of", f2[(False, True)] + f2[(False, False)], "relax-holds-or-not failures")
