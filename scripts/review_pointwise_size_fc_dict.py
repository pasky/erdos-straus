"""Hostile review of POINTWISE_SIZE §3.3 (Theorem F as an instance of Theorem M).

Independent of formal2*/formal_closure*/pointwise_size_* code.  Reads the
FORMAL_CLOSURE certificate and asks two questions about the program BFS_inf of
POINTWISE_SIZE §3.3 run formally at the lifted point:

 (1) Which polynomials does BFS_inf actually FACTOR?  It factors 4z-p and pz
     only for NON-dead z.  Polynomials occurring only in dead entries are never
     factored, so they are not in Theorem M's literal S.
 (2) Does the certificate's precision E_l satisfy Theorem M's requirement
     E_l >= v_l(D) for the divmods BFS_inf performs?  We check the exact
     quotients w = (s^2/D+s)/r and the intermediate s^2/D, whose denominators
     are those of the formal integers themselves: den(c*prod (g/C_g)^e).
     Lower bound used: for an output entry W (a formal integer) the program
     computes W by an exact divmod, so Theorem M needs E_l >= v_l(den W).
"""
import gzip, json, sys
from fractions import Fraction
from math import gcd

cert = json.load(gzip.open(sys.argv[1] if len(sys.argv) > 1 else
                           'data/formal_closure/certificate.json.gz'))
E = {int(l): v[1] for l, v in cert['q0_mod'].items()}
S = {}
for coeffs, C, f1, f2 in cert['S']:
    S[tuple(coeffs)] = (C, f1, f2)
P = (1, 24)
X = (0, 1)

def pmul(a, b):
    r = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r

def entry_poly(ent):
    c, fac = ent
    poly = [Fraction(c)]
    for g, e in fac:
        C = S[tuple(g)][0]
        gq = [Fraction(x, C) for x in g]
        for _ in range(e):
            poly = pmul(poly, gq)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly

def is_dead(ent):
    c, fac = ent
    if any(tuple(g) == P for g, e in fac):
        return False
    poly = entry_poly(ent)
    if c < 0:
        return True
    deg = len(poly) - 1
    if deg >= 2:
        return True
    if deg == 1:
        lc = poly[1]
        return lc > 12 or (lc == 12 and poly[0] > 0)
    return False

def vl(n, l):
    v = 0
    while n % l == 0:
        n //= l; v += 1
    return v

flag_stats = {}
for k, (C, f1, f2) in S.items():
    flag_stats[(f1, f2)] = flag_stats.get((f1, f2), 0) + 1
print('S flags (f1,f2) counts:', flag_stats)

nondead_polys, dead_polys = set(), set()
seen = {}
max_excess = 0
viol = {}
for V in cert['vertices']:
    for ent in V:
        key = json.dumps(ent)
        if key in seen:
            continue
        d = is_dead(ent)
        seen[key] = d
        tgt = dead_polys if d else nondead_polys
        for g, e in ent[1]:
            tgt.add(tuple(g))
        # denominator of the formal integer as a Q[X] polynomial
        poly = entry_poly(ent)
        den = 1
        for x in poly:
            den = den * x.denominator // gcd(den, x.denominator)
        for l in list(E):
            if den % l == 0:
                v = vl(den, l)
                if v > E[l]:
                    viol[l] = max(viol.get(l, 0), v - E[l])
n_dead = sum(seen.values())
print('distinct entries:', len(seen), 'dead:', n_dead, 'non-dead:', len(seen) - n_dead)
entry_polys = nondead_polys | dead_polys
only_dead = dead_polys - nondead_polys
print('polys in entries:', len(entry_polys), ' in non-dead entries:', len(nondead_polys),
      ' only in dead entries:', len(only_dead))
aux = {k for k, (C, f1, f2) in S.items() if k not in entry_polys}
print('S polys not in any entry (aux):', len(aux))
print('Theorem M literal S = {P} u non-dead-entry polys u aux:',
      len(nondead_polys | aux | {P}), ' vs |S_FC| =', len(S))
print('E_l < v_l(den W) for some entry W (Theorem M precision violated):',
      len(viol), 'primes; worst excess', max(viol.values()) if viol else 0,
      sorted(viol.items())[:15])
