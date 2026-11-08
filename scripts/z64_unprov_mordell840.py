"""z64 UNPROV: certify the polynomial-identity half of the mod-840 dichotomy (Z64_UNPROV.md Thm B / Cor C).

For every residue class r mod 840 with r not in M = {1,121,169,289,361,529} we exhibit an explicit triple
P1, P2, P3 in Q[n] such that
  (1) 4*P1*P2*P3 == n*(P1*P2 + P2*P3 + P3*P1) identically (sympy),
  (2) each P_i(r + Q*k) is integer-valued for all integers k (checked on deg+1 consecutive k: finite differences),
      where Q | 840 is the modulus of the family member,
  (3) each P_i(n) > 0 for every real n >= 1 (checked: no real root >= 1 and positive leading coefficient, or
      P_i(1) > 0 with no root in [1, inf)).
Families (Elsholtz-Tao, J. Aust. Math. Soc. 94 (2013), Sigma^I / Sigma^II parametrisations, eqs (2.1)-(2.21)):
  T2a: n = -e mod 4ab, e | a+b:          x=(n+e)/4, y=c n (n+e)/(4b), z=c n (n+e)/(4a), c=(a+b)/e
  T1a: n = -f mod 4ad, f | 4a^2 d+1:     e=(4a^2d+1)/f, c=(n+f)/(4ad), b=(ne+1)/(4ad); (x,y,z)=(abdn, acd, bcd)
  T1d: n e = -1 mod 4ab, e | a+b:        c=(a+b)/e, d=(ne+1)/(4ab); (x,y,z)=(abdn, acd, bcd)
  T2c: n = -4a^2 d - e mod 4ade:         c=(n+4a^2d+e)/(4ade), b=ce-a; (x,y,z)=(abd, acdn, bcdn)
Non-primitive classes (gcd(r,840) > 1) are handled by the scaling identities for 2,3,5,7 (also checked).
Output: data/z64/unprov/mordell840.txt
"""
import itertools, sys
from math import gcd
import sympy as sp

n, k = sp.symbols('n k')
MOD = 840
MCLASS = {1, 121, 169, 289, 361, 529}


def divisors(m):
    return [d for d in range(1, m + 1) if m % d == 0]


def check_triple(P, r, Q):
    """Return True if P=(P1,P2,P3) solves 4/n identically, is integer-valued on n = r mod Q, positive for n >= 1."""
    lhs = sp.expand(4 * P[0] * P[1] * P[2] - n * (P[0] * P[1] + P[1] * P[2] + P[2] * P[0]))
    if lhs != 0:
        return False
    for Pi in P:
        Pk = sp.Poly(sp.expand(Pi.subs(n, r + Q * k)), k)
        deg = Pk.degree()
        for kk in range(0, deg + 1):
            v = Pk.eval(kk)
            if not v.is_integer:
                return False
        Pn = sp.Poly(sp.expand(Pi), n)
        if Pn.LC() <= 0:
            return False
        roots = [rt for rt in sp.real_roots(Pn) if rt >= 1]
        if roots or Pn.eval(1) <= 0:
            return False
    return True


def family_members():
    """Yield (name, Q, residue, P) with Q | 840."""
    out = []
    D = divisors(MOD)
    # T2a: modulus 4ab | 840 -> ab | 210
    for a in range(1, 211):
        for b in range(a, 211):
            Q = 4 * a * b
            if MOD % Q:
                continue
            for e in divisors(a + b):
                if gcd(e, Q) != 1:
                    continue
                c = sp.Rational(a + b, e)
                P = (sp.Rational(1, 4) * (n + e), c * n * (n + e) / (4 * b), c * n * (n + e) / (4 * a))
                out.append(('T2a', Q, (-e) % Q, P, (a, b, e)))
    # T1a: modulus 4ad | 840
    for a in range(1, 211):
        for d in range(1, 211):
            Q = 4 * a * d
            if MOD % Q:
                continue
            for f in divisors(4 * a * a * d + 1):
                e = sp.Rational(4 * a * a * d + 1, f)
                c = (n + f) / (4 * a * d)
                b = (n * e + 1) / (4 * a * d)
                P = (a * b * d * n, a * c * d, b * c * d)
                out.append(('T1a', Q, (-f) % Q, P, (a, d, f)))
    # T1d: n*e = -1 mod 4ab, e | a+b, gcd(e,4ab)=1
    for a in range(1, 211):
        for b in range(a, 211):
            Q = 4 * a * b
            if MOD % Q:
                continue
            for e in divisors(a + b):
                if gcd(e, Q) != 1:
                    continue
                res = (-pow(e, -1, Q)) % Q
                c = sp.Rational(a + b, e)
                dd = (n * e + 1) / (4 * a * b)
                P = (a * b * dd * n, a * c * dd, b * c * dd)
                out.append(('T1d', Q, res, P, (a, b, e)))
    # T2c: modulus 4ade | 840, gcd(4ad, e) = 1
    for a in range(1, 211):
        for d in range(1, 211):
            for e in range(1, 211):
                Q = 4 * a * d * e
                if MOD % Q or gcd(4 * a * d, e) != 1:
                    continue
                c = (n + 4 * a * a * d + e) / (4 * a * d * e)
                b = c * e - a
                P = (a * b * d, a * c * d * n, b * c * d * n)
                out.append(('T2c', Q, (-4 * a * a * d - e) % Q, P, (a, d, e)))
    return out


def main():
    members = family_members()
    covered = {}
    nchecked = 0
    for name, Q, res, P, par in members:
        lifts = [r for r in range(MOD) if r % Q == res and gcd(r, MOD) == 1 and r not in covered]
        if not lifts:
            continue
        nchecked += 1
        if not check_triple(P, res, Q):
            continue
        for r in lifts:
            covered[r] = (name, Q, res, par, [str(sp.factor(p)) for p in P])
    prim = [r for r in range(MOD) if gcd(r, MOD) == 1]
    uncovered = sorted(set(prim) - set(covered))
    lines = []
    lines.append(f"# z64 UNPROV mod-840 dichotomy certificate (scripts/z64_unprov_mordell840.py)")
    lines.append(f"# family members generated: {len(members)}; checked (needed): {nchecked}")
    lines.append(f"# primitive classes mod 840: {len(prim)}; covered by a verified polynomial identity: {len(covered)}")
    lines.append(f"# uncovered primitive classes: {uncovered}")
    lines.append(f"# uncovered == Mordell set M: {set(uncovered) == MCLASS}")
    # squares check
    sq = sorted({(s * s) % MOD for s in range(MOD) if gcd(s, MOD) == 1})
    lines.append(f"# unit squares mod 840: {sq}")
    # non-primitive classes: scaling identities
    scal = {2: (1, 2, 2), 3: (1, 4, 12), 5: (2, 4, 20), 7: (2, 21, 42)}
    for g, (a, b, c) in scal.items():
        assert sp.Rational(4, g) == sp.Rational(1, a) + sp.Rational(1, b) + sp.Rational(1, c)
    lines.append("# non-primitive classes: 4/(g m) = 1/(a m)+1/(b m)+1/(c m) with (g;a,b,c) in "
                 + str(scal) + " (verified)")
    for r in sorted(covered):
        name, Q, res, par, P = covered[r]
        lines.append(f"{r}\t{name}\tQ={Q}\tres={res}\tpar={par}\tP={P}")
    open('data/z64/unprov/mordell840.txt', 'w').write("\n".join(lines) + "\n")
    print("\n".join(lines[:7]))


if __name__ == '__main__':
    main()
