"""Stand-alone checker for O100 tree certificates (does not import mordell_lib).

usage: m13c_check.py tree.json
Tree (output of m13c_dfs.py): roots [{x, L, ...}], node = leaf [M, res, fam, P] | split p + children | open.
Checks:
 (0) the roots are exactly the six exceptional classes 112561, ... mod 720720 of POINTWISE_MORDELL Thm 3.1(b);
 (1) for every split node (x mod L) at the prime p: L' = L*p, and the children are exactly the residues
     x + L t mod L' (0 <= t < p) with x + L t not divisible by p (the omitted child can contain only the
     prime p itself, checked separately in (3));
 (2) every leaf: the class (fam, P) passes mordell_check.check_class (sympy: ET coordinates, identity
     4xyz = n(xy+yz+zx), positivity for n > n0) and its coordinates are integer-valued on x + L Z
     (mordell_check.integral_on: integrality at s = 0..deg);
 (3) every split prime p with (p/13) = -1 has an explicit ES solution (direct search).
Output: number of leaves/open leaves and the open (exceptional) density relative to the six root classes.
"""
import sys, json
from fractions import Fraction as Fr
import sympy as sp
from mordell_check import check_class, n as NSYM

ROOTS = {112561, 352801, 380881, 418321, 473761, 483841}

def es_small(p):
    for x in range(p // 4 + 1, p + 1):
        r = Fr(4, p) - Fr(1, x)
        if r <= 0:
            continue
        for y in range(max(x, int(1 / r) + 1), int(2 / r) + 1):
            s = r - Fr(1, y)
            if s > 0 and s.numerator == 1 and s.denominator >= y:
                return (x, y, s.denominator)
    return None

POLY = {}
def polys(fam, P):
    k = (fam, tuple(P))
    if k not in POLY:
        (x, y, z), n0 = check_class(fam, tuple(P))
        POLY[k] = ([[Fr(int(c.p), int(c.q)) for c in sp.Poly(v, NSYM).all_coeffs()] for v in (x, y, z)], n0)
    return POLY[k]

def ev(cs, t):
    v = Fr(0)
    for c in cs:
        v = v * t + c
    return v

def integral_on(cs_list, t, L):
    for cs in cs_list:
        for s in range(len(cs)):          # degree = len(cs) - 1; s = 0..deg
            if ev(cs, t + L * s).denominator != 1:
                return False
    return True

def main():
    T = json.load(open(sys.argv[1]))
    roots = T['roots']
    assert {r['x'] % 720720 for r in roots} == ROOTS and all(r['L'] == 720720 for r in roots) and len(roots) == 6
    stats = {'leaf': 0, 'open': 0, 'split': 0}
    openmass = Fr(0); N0 = 0; splitp = set(); opens = []
    stack = [(r, Fr(1, 6)) for r in roots]
    while stack:
        nd, mass = stack.pop()
        x, L = nd['x'], nd['L']
        if 'split' in nd:
            p = nd['split']; splitp.add(p)
            L2 = L * p
            want = sorted((x + L * t) % L2 for t in range(p) if (x + L * t) % p)
            got = sorted(c['x'] % L2 for c in nd['children'])
            assert want == got and all(c['L'] == L2 for c in nd['children']), ('split', x, L, p)
            stats['split'] += 1
            for c in nd['children']:
                stack.append((c, mass / len(want)))
        elif 'leaf' in nd:
            M, res, fam, P = nd['leaf']
            cs, n0 = polys(fam, P)
            N0 = max(N0, n0)
            assert integral_on(cs, x, L), ('leaf', x, L, fam, P)
            stats['leaf'] += 1
        else:
            assert nd.get('open'), nd
            stats['open'] += 1; openmass += mass; opens.append((x, L))
    for p in sorted(splitp):
        if pow(p, 6, 13) == 12:          # (p/13) = -1
            assert es_small(p), p
    print(f"tree OK: {stats}, {len(POLY)} distinct classes (identities OK, coordinates > 0 for n > {N0}), "
          f"split primes {sorted(splitp)} checked")
    print(f"open density relative to the six root classes: {float(openmass):.4e} ({len(opens)} open leaves)")
    print("CERTIFICATE OK")

if __name__ == '__main__':
    main()
