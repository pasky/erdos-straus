"""U02 compliance pass (batch S): Gaussian-cone items (Z0268, Z0270, Z0316, Z0564), Lucas divisibility (Z0536), Pell norms (Z0999)."""
import sys, math, json
from fractions import Fraction as Fr
from collections import Counter
from sympy import primerange, isprime
sys.path.insert(0, 'scripts')
R = {}
# Gaussian integers as (a,b). 1/(a+bi) = (a-bi)/(a^2+b^2)
def inv(a, b):
    n = a * a + b * b
    return (Fr(a, n), Fr(-b, n))
def els(H, cone):
    out = []
    B = int(math.isqrt(H)) + 1
    for a in range(-B, B + 1):
        for b in range(-B, B + 1):
            n = a * a + b * b
            if 0 < n <= H and cone(a, b): out.append((a, b))
    return out
def is_gint(x):
    return x[0].denominator == 1 and x[1].denominator == 1
def three_term_exists(p, E, first_only=False):
    """4/p = 1/x + 1/y + 1/z with x,y,z in E (ordered pairs over E, z determined)."""
    Iv = {e: inv(*e) for e in E}
    t = (Fr(4, p), Fr(0))
    sols = []
    for i, x in enumerate(E):
        for y in E[i:]:
            w = (t[0] - Iv[x][0] - Iv[y][0], t[1] - Iv[x][1] - Iv[y][1])
            n = w[0] * w[0] + w[1] * w[1]
            if n == 0: continue
            z = (w[0] / n, -w[1] / n)  # 1/w
            if is_gint(z) and z[0] != 0 or (is_gint(z) and z[1] != 0):
                sols.append((x, y, (int(z[0]), int(z[1]))))
                if first_only: return sols
    return sols
# Z0268: closed Q1 cone (Re>0, Im>=0 as in H00's Z0067), p=41, 137, H=100; plus full Z[i] for comparison
Q1 = els(100, lambda a, b: a > 0 and b >= 0)
Zi = els(100, lambda a, b: True)
R['Z0268'] = {}
for p in (41, 137):
    s1 = three_term_exists(p, Q1, first_only=True)
    R['Z0268'][p] = {'closedQ1_H100_solution_found': bool(s1), 'example': s1[:1] if s1 else None}
# Z0270: Gaussian primes pi, N<=300; x<=y<=200 rationals; alpha = 1/(4/pi - 1/x - 1/y) in Z[i]?
gp = []
for a in range(1, 18):
    for b in range(0, 18):
        n = a * a + b * b
        if 2 <= n <= 300 and isprime(n) or (n == 2 and a == 1 and b == 1):
            gp.append((a, b))
gp = [g for g in gp if (g[0]*g[0] + g[1]*g[1]) in (2,) or isprime(g[0]**2 + g[1]**2)]
hits = []
for (a, b) in gp:
    n = a * a + b * b
    # 4/pi = 4*conj(pi)/n
    t = (Fr(4 * a, n), Fr(-4 * b, n))
    for x in range(1, 201):
        for y in range(x, 201):
            w = (t[0] - Fr(1, x) - Fr(1, y), t[1])
            nn = w[0] * w[0] + w[1] * w[1]
            if nn == 0: continue
            al = (w[0] / nn, -w[1] / nn)
            if is_gint(al) and (al[0] != 0 or al[1] != 0):
                hits.append(((a, b), x, y)); break
        else:
            continue
        break
R['Z0270'] = {'gaussian_primes_norm_le_300': len(gp), 'primes_with_pair_solution': len(hits), 'examples': hits[:6]}
# Z0316: angles of Z[i] solutions of 4/p (H=50), p<=50 (first primes): fraction with denominators in closed Q1
E50 = els(50, lambda a, b: True)
angles = Counter(); tot = 0
import math as m2
for p in [q for q in primerange(5, 50)]:
    sols = three_term_exists(p, E50)
    for (x, y, z) in sols:
        for d in (x, y, z):
            ang = m2.degrees(m2.atan2(d[1], d[0])) % 360
            angles[int(ang // 45)] += 1; tot += 1
R['Z0316'] = {'primes': len([q for q in primerange(5, 50)]), 'denominator_octant_counts(45deg bins)': dict(sorted(angles.items())), 'total': tot}
# Z0564: Gaussian lift: 4/n = 2Re(xi)/N(xi) + 1/z (conjugate pair xi, conj xi), n = N(pi), n<=200 primes
R['Z0564'] = {'n_prime_norms_tested': 0, 'hits': []}
hits = []
for n in [q for q in primerange(5, 201) if q % 4 == 1]:
    found = None
    for a in range(-40, 41):
        for b in range(1, 41):
            N = a * a + b * b
            r = Fr(4, n) - Fr(2 * a, N)
            if r > 0 and r.numerator == 1:
                found = (a, b, r.denominator); break
        if found: break
    R['Z0564']['n_prime_norms_tested'] += 1
    if found: hits.append((n, found))
R['Z0564']['hits'] = hits[:10]; R['Z0564']['n_hits'] = len(hits)
# Z0536: Lucas sequences U_k(P,Q), |P|,|Q|<=3, k<=60; does 4Cp+1 (C<=50, p<=300, p=1 mod 4) divide some U_k?
def lucas_terms(P, Q, K):
    u0, u1 = 0, 1; out = [u0, u1]
    for _ in range(K):
        u0, u1 = u1, P * u1 - Q * u0
        out.append(u1)
    return out
terms = {}
for P in range(-3, 4):
    for Q in range(-3, 4):
        if Q == 0 or P * P - 4 * Q == 0: continue
        terms[(P, Q)] = lucas_terms(P, Q, 60)
ps = [p for p in primerange(5, 300) if p % 4 == 1]
dv = 0; tot = 0
targets = {}
for p in ps:
    for C in range(1, 51):
        N = 4 * C * p + 1; tot += 1
        ok = False
        for key, seq in terms.items():
            if any(abs(t) > 0 and (t % N == 0) for t in seq[1:]):
                ok = True; break
        dv += ok
R['Z0536'] = {'pairs': tot, 'N_divides_some_Lucas_term(|P|,|Q|<=3, k<=60)': dv}
json.dump(R, open('data/z52b/pass1/U02/compl_s.json', 'w'), indent=1, default=str)
print(json.dumps(R, default=str)[:3500])
