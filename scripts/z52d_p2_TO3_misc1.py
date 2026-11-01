"""Pass-2 TO3 misc checks (part 1): Z0708, Z0748, Z0822, Z0831, Z0966, Z0856, Z0978, Z0870, Z0751, Z0876, Z0927.
Writes data/z52b/pass2/TO3/misc1_results.json. Uses scripts/z52d_p2_TO3_lib.py (exact enumerator)."""
import sys, json, math
import numpy as np
sys.path.insert(0, 'scripts')
from z52d_p2_TO3_lib import sols
from math import gcd
from sympy import primerange, factorint
from fractions import Fraction
out = {}
F = np.loadtxt('data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
Ufull = dict(zip(F[:, 0].tolist(), F[:, 1].tolist()))
minx = dict(zip(F[:, 0].tolist(), F[:, 8].tolist()))
# ---- Z0708: n with no solution having first denominator (n+3)/4 (n = 1 mod 4) ----
bad = [n for n in range(2, 30001) if n % 4 == 1 and minx[n] > n // 4 + 1]
out['Z0708_count_le30000'] = len(bad)
out['Z0708_residues_mod24'] = sorted(set(n % 24 for n in bad))
out['Z0708_first20'] = bad[:20]
out['Z0708_claim_check'] = {'193_in': 193 in bad, '409_in': 409 in bad, '2521_in': 2521 in bad, '5569_in': 5569 in bad, '9601_in': 9601 in bad, '577_in': 577 in bad, '66529_in': 66529 in bad}
# divisor criterion: 12/M = 1/y+1/z (M = n(n+3)) solvable  <=>  exists d | M^2, d = -M mod 12, d<=M, with (M^2/d + M) = 0 mod 12 ... (check numerically)
def two_term(A, B):
    """exists 1/y+1/z = A/B (positive integers)? via (Ay-B)(Az-B)=B^2 ; uses full divisor list (small B)."""
    from sympy import divisors
    for d in divisors(B * B):
        if (d + B) % A == 0 and ((B * B // d) + B) % A == 0:
            return True
    return False
agree = 0; tot = 0
for n in range(5, 2001, 4):
    M = n * (n + 3)
    crit = two_term(12, M)
    truth = (n in bad)
    tot += 1
    if crit == (not truth): agree += 1
out['Z0708_divisor_criterion_agreement_n_le2000'] = [agree, tot]
# ---- Z0748: 4/n = 1/x + 1/y solvable? vs 'n even or has prime factor 3 mod 4' ----
def two_term_4n(n):
    return two_term(4, n)
ok = 0; tot = 0; mism = []
for n in range(2, 3001):
    s = two_term_4n(n)
    fac = factorint(n)
    crit = (n % 2 == 0) or any(p % 4 == 3 for p in fac)
    tot += 1
    if s == crit: ok += 1
    else: mism.append(n)
out['Z0748_two_term_claim_agreement_n_le3000'] = [ok, tot]
out['Z0748_mismatches_first'] = mism[:10]
# the even-n claim: 4/n = 1/x+1/y for n even? check few
out['Z0748_density_note'] = 'all-prime-factors-1mod4 odd n have density 0'
# ---- Z0822: U(m^2) for odd m <= 173 and neighbours ----
odd_m = list(range(1, 174, 2))
rat = []; Um = {}
for m in odd_m:
    n2 = m * m
    if n2 <= 30000 and n2 in Ufull:
        Um[m] = Ufull[n2]
        nb = [Ufull[k] for k in range(max(2, n2 - 10), n2 + 11) if k != n2 and int(math.isqrt(k)) ** 2 != k and k <= 30000]
        rat.append((m, Ufull[n2], float(np.median(nb)), Ufull[n2] / float(np.median(nb))))
out['Z0822_Um_odd_m_first'] = [(m, u) for m, u, _, _ in rat[:12]]
out['Z0822_U_at_m2_m_3_to_9'] = {m: Um[m] for m in [3, 5, 7, 9]}
out['Z0831_median_ratio_U_m2_over_neighbours'] = float(np.median([x[3] for x in rat]))
out['Z0831_mean_ratio'] = float(np.mean([x[3] for x in rat]))
out['Z0831_U_at_225_441'] = [Ufull[225], Ufull[441]]
p3 = {p: Ufull[p ** 3] for p in primerange(3, 31) if p ** 3 <= 30000}
out['Z0822_U_p_cubed'] = p3
# ---- Z0966: lowest U/log^3 among composites <= 30000 ----
comp = [(Ufull[n] / math.log(n) ** 3, n) for n in range(4, 30001) if not all(n % q for q in range(2, int(n ** .5) + 1)) and Ufull[n] > 0]
comp.sort()
out['Z0966_lowest12_composites'] = [(n, round(v, 4)) for v, n in comp[:12]]
out['Z0966_lowest12_prime_square_or_not'] = [bool(math.isqrt(n) ** 2 == n and all(math.isqrt(n) % q for q in range(2, int(math.isqrt(n) ** .5) + 1))) for v, n in comp[:12]]
# ---- Z0856: normal form lemma: in every solution p | z (z largest) for odd primes p ----
bad856 = []
cnt = 0
for p in primerange(3, 1001):
    for (x, y, z) in sols(4, p):
        cnt += 1
        if z % p != 0: bad856.append((p, x, y, z))
out['Z0856_solutions_checked_p_le1000'] = cnt
out['Z0856_violations'] = bad856[:5]
# ---- Z0978: gcd strata for all solutions at primes <= 300 ----
gstrata = {}
for p in primerange(3, 301):
    for (x, y, z) in sols(4, p):
        g = gcd(gcd(x, y), z)
        key = 'g=1' if g == 1 else f'g={g}'
        gstrata[key] = gstrata.get(key, 0) + 1
out['Z0978_gcd_strata_p_le300'] = gstrata
# ---- Z0870: power-of-two denominators (exact) ----
def exists_pow2(p):
    # exists a>=1 with 1/2^a among denominators: 4/p - 1/2^a = A/B has a 2-term representation
    for a in range(1, 40):
        t = 2 ** a
        num = 4 * t - p
        if num <= 0:
            continue
        den = p * t
        g = gcd(num, den); A, B = num // g, den // g
        # divisors of B^2 with B = p^e 2^f (only primes p, 2 can occur)
        fB = factorint(B)
        divs = [1]
        for q, e in fB.items():
            divs = [d * q ** j for d in divs for j in range(2 * e + 1)]
        for d in divs:
            if (d + B) % A == 0 and ((B * B // d) + B) % A == 0:
                return a
    return None
pw2 = []
for p in primerange(3, 100001):
    a = exists_pow2(p)
    if a is not None: pw2.append((p, a))
out['Z0870_primes_le1e5_with_pow2_denominator'] = len(pw2)
out['Z0870_fraction'] = len(pw2) / len(list(primerange(3, 100001)))
out['Z0870_first_pairs'] = pw2[:12]
# ---- Z0751: 4/131 solutions: parity of denominators; 8/131 ----
s131 = sols(4, 131)
ev = {}
for t in s131:
    k = sum(1 for v in t if v % 2 == 0)
    ev[k] = ev.get(k, 0) + 1
out['Z0751_4_131_nsol'] = len(s131)
out['Z0751_even_denominator_count_hist'] = ev
out['Z0751_8_131_nsol'] = len(sols(8, 131))
out['Z0751_all_even_4_131'] = [t for t in s131 if all(v % 2 == 0 for v in t)]
# ---- Z0876: 2521 ----
s2521 = sols(4, 2521)
p = 2521
out['Z0876'] = dict(nsol=len(s2521), xs=sorted(set(t[0] for t in s2521)),
                    x_divides_z=[t for t in s2521 if t[2] % t[0] == 0],
                    n_4_divides_x=sum(1 for t in s2521 if t[0] % 4 == 0),
                    typeI_II=dict(p_divides_exactly_z_only=sum(1 for t in s2521 if t[2] % p == 0 and t[1] % p != 0),
                                  p_divides_y_and_z=sum(1 for t in s2521 if t[1] % p == 0 and t[2] % p == 0),
                                  p_divides_y_only=sum(1 for t in s2521 if t[1] % p == 0 and t[2] % p != 0)),
                    max_z=max(t[2] for t in s2521), min_z=min(t[2] for t in s2521))
# ---- Z0927: 12601 across numerators 4,5,7 ----
out['Z0927'] = {}
for m in (4, 5, 7):
    s = sols(m, 12601)
    out['Z0927'][m] = dict(nsol=len(s))
    out['Z0927'][m]['p_multiplicity_in_denoms'] = {'div_by_p_count': sum(1 for t in s for v in t if v % 12601 == 0),
                                                   'div_by_7': sum(1 for t in s for v in t if v % 7 == 0)}
json.dump(out, open('data/z52b/pass2/TO3/misc1_results.json', 'w'), indent=1, default=str)
for k, v in out.items(): print(k, str(v)[:400])
