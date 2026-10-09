#!/usr/bin/env python3
"""R100 from-scratch checker for data/mordell13c/tree6_6000.json.gz (POINTWISE_MORDELL13C Thm 6.1).

Independent of scripts/m13c_* and mordell_lib.  For every leaf [M, r, fam, params]:
  * recompute the ET Prop 1.9 class from params (own CRT), check side conditions, M == computed modulus,
    r in class, M | L, x == r (mod M);
  * build the ES solution (x,y,z) from the ET parametrisation pi^I=(abdn,acd,bcd), pi^II=(abd,acdn,bcdn)
    with the auxiliary coordinates re-derived here (see review §A), check integrality + positivity +
    4xyz == n(xy+yz+zx) for n = x + L*s, s = 0..4, and that positivity is monotone (checked at s=0, which is
    the least positive element of the leaf, and the relevant coordinate is increasing in n).
Partition: each split node's children are exactly the units mod L*q lying over x mod L (for q | L: all q
lifts; for q not dividing L: q-1 lifts, the omitted one is the multiple of q, containing only the prime q).
Masses: Haar mass among units relative to root.
"""
import gzip, json, sys
from fractions import Fraction
from math import gcd

def egcd_inv(a, m):
    return pow(a, -1, m)

def crt(r1, m1, r2, m2):
    g = gcd(m1, m2)
    if (r1 - r2) % g: return None
    l = m1 // g * m2
    t = ((r2 - r1) // g * pow(m1 // g, -1, m2 // g)) % (m2 // g) if m2 // g > 1 else 0
    return (r1 + m1 * t) % l, l

def family(fam, P):
    """return (modulus, set_of_residues) of the ET class, after asserting side conditions."""
    if fam == "I1":
        a, d, f = P; assert (4*a*a*d + 1) % f == 0
        m = 4*a*d; return m, {(-f) % m}
    if fam == "I2":
        a, c, f = P; assert gcd(4*a*c, f) == 1
        m1 = 4*a*c; r2 = (-c * pow(a, -1, f)) % f if f > 1 else 0
        r, m = crt((-f) % m1, m1, r2, f); return m, {r}
    if fam == "I3":
        c, d, f = P; assert gcd(4*c*d, f) == 1
        m1 = 4*c*d
        sq = [u for u in range(f) if (u*u + 4*c*c*d) % f == 0]
        out = set()
        for u in sq:
            r, m = crt((-f) % m1, m1, u, f); out.add(r)
        return m1 * f, out
    if fam == "I4":
        a, b, e = P; assert (a + b) % e == 0 and gcd(e, 4*a*b) == 1
        m = 4*a*b; return m, {(-pow(e, -1, m)) % m}
    if fam == "II1":
        a, b, e = P; assert (a + b) % e == 0 and gcd(e, 4*a*b) == 1
        m = 4*a*b; return m, {(-e) % m}
    if fam == "II2":
        a, d, f = P; assert (f + 1) % (4*a*d) == 0
        return f, {(-4*a*a*d) % f}
    if fam == "II3":
        a, d, e = P; assert gcd(4*a*d, e) == 1
        m = 4*a*d*e; return m, {(-4*a*a*d - e) % m}
    raise ValueError(fam)

def solution(fam, P, n):
    """(x,y,z) or None if a coordinate is non-integral / non-positive."""
    def q(num, den):
        if num % den: return None
        return num // den
    if fam == "I1":
        a, d, f = P; c = q(n + f, 4*a*d); e = q(4*a*a*d + 1, f)
        if c is None or e is None: return None
        b = c*e - a; T = "I"
    elif fam == "I2":
        a, c, f = P; b = q(n*a + c, f); d = q(n + f, 4*a*c)
        if b is None or d is None: return None
        T = "I"
    elif fam == "I3":
        c, d, f = P; a = q(n + f, 4*c*d); b = q(n*(n + f) + 4*c*c*d, 4*c*d*f)
        if a is None or b is None: return None
        T = "I"
    elif fam == "I4":
        a, b, e = P; c = q(a + b, e); d = q(n*e + 1, 4*a*b)
        if c is None or d is None: return None
        T = "I"
    elif fam == "II1":
        a, b, e = P; c = q(a + b, e); d = q(n + e, 4*a*b)
        if c is None or d is None: return None
        T = "II"
    elif fam == "II2":
        a, d, f = P; c = q(f + 1, 4*a*d); e = q(n + 4*a*a*d, f)
        if c is None or e is None: return None
        b = c*e - a; T = "II"
    elif fam == "II3":
        a, d, e = P; c = q(n + 4*a*a*d + e, 4*a*d*e)
        if c is None: return None
        b = c*e - a; T = "II"
    if min(a, b, c, d) <= 0: return None
    if T == "I": return (a*b*d*n, a*c*d, b*c*d)
    return (a*b*d, a*c*d*n, b*c*d*n)

def main(path):
    t = json.load(gzip.open(path))
    stats = dict(leaves=0, open=0, splits=0)
    fams = set(); errors = []
    open_mass = {}; cov_mass = {}
    open_list = []
    for root in t["roots"]:
        rx, rL = root["x"], root["L"]
        assert rL == 720720 and 0 <= rx < rL
        om = Fraction(0); cm = Fraction(0)
        stack = [(root, Fraction(1))]
        while stack:
            node, mass = stack.pop()
            x, L = node["x"], node["L"]
            if not (0 < x < L): errors.append(("range", x, L))
            if "children" in node:
                stats["splits"] += 1
                qq = node["split"]
                assert all(qq % p for p in range(2, int(qq**.5) + 1)) and qq > 1
                ch = node["children"]
                exp = {(x + L*s) % (L*qq) for s in range(qq)}
                if L % qq: exp = {u for u in exp if u % qq}
                got = [c["x"] % (L*qq) for c in ch]
                if any(c["L"] != L*qq for c in ch) or sorted(got) != sorted(exp) or len(got) != len(set(got)):
                    errors.append(("partition", x, L, qq))
                cmass = mass / len(exp)
                for c in ch: stack.append((c, cmass))
            elif "open" in node:
                stats["open"] += 1; om += mass; open_list.append((x, L))
            else:
                stats["leaves"] += 1; cm += mass
                M, r, fam, P = node["leaf"]
                try:
                    m, res = family(fam, P)
                except AssertionError:
                    errors.append(("side", node["leaf"])); continue
                fams.add((fam, tuple(P)))
                if m != M or r % M not in res or L % M or (x - r) % M:
                    errors.append(("class", x, L, node["leaf"], m)); continue
                for s in range(5):
                    n = x + L*s
                    sol = solution(fam, P, n)
                    if sol is None or 4*sol[0]*sol[1]*sol[2] != n*(sol[0]*sol[1] + sol[1]*sol[2] + sol[0]*sol[2]):
                        errors.append(("sol", x, L, node["leaf"], s)); break
        if om + cm != 1: errors.append(("mass", rx, om + cm))
        open_mass[rx] = om
    print(stats, "distinct ET classes:", len(fams))
    tot = sum(open_mass.values())
    for k, v in open_mass.items(): print(k, float(v))
    print("open density of the six classes:", float(tot / 6))
    print("errors:", len(errors), errors[:10])
    return open_list, errors

if __name__ == "__main__":
    main(sys.argv[1])
