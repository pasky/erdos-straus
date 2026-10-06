"""Stand-alone checker for O80 covering certificates (does not import mordell_lib).

usage: mordell_check.py cert.json
Certificate: {r, variant, L, classes: [[fam, params]], exceptions: [...]}.
Checks:
 (1) for every class, ET's coordinates (a,b,c,d,e,f) as polynomials in n (sympy, exact),
     the map pi^I=(abdn, acd, bcd) or pi^II=(abd, acdn, bcdn), and the identity
     4xyz = n(xy+yz+zx) identically in n; positivity of x,y,z for n > n0 (computed);
 (2) Sigma residues mod L (recomputed here from the definition) minus the exceptions:
     each residue t has a class whose coordinates are integer-valued on t + L*Z
     (a polynomial of degree k in s is integer-valued iff integral at s=0..k).
Conclusion if OK: every n > n0 with n mod L in Sigma \\ exceptions has a positive ES solution.
"""
import sys, json
import sympy as sp
from math import gcd

n = sp.symbols('n')

def coords(fam, P):
    """ET Prop 1.9 proof (§10): coordinates (a,b,c,d,e,f) in terms of n; type I or II."""
    R = sp.Rational
    if fam == 'I1':
        a, d, f = P; e = R(4 * a * a * d + 1, f)
        c = (n + f) / (4 * a * d); b = c * e - a
        return 'I', (a, b, c, d)
    if fam == 'I2':
        a, c, f = P
        return 'I', (a, (n * a + c) / f, c, (n + f) / (4 * a * c))
    if fam == 'I3':
        c, d, f = P
        return 'I', ((n + f) / (4 * c * d), (n**2 + 4 * c * c * d + n * f) / (4 * c * d * f), c, d)
    if fam == 'I4':
        a, b, e = P; c = R(a + b, e)
        return 'I', (a, b, c, (n * e + 1) / (4 * a * b))
    if fam == 'II1':
        a, b, e = P; c = R(a + b, e)
        return 'II', (a, b, c, (n + e) / (4 * a * b))
    if fam == 'II2':
        a, d, f = P; c = R(f + 1, 4 * a * d); e = (n + 4 * a * a * d) / f
        return 'II', (a, c * e - a, c, d)
    if fam == 'II3':
        a, d, e = P
        return 'II', (a, (n + e) / (4 * a * d), (n + 4 * a * a * d + e) / (4 * a * d * e), d)
    raise ValueError(fam)

def xyz(T, a, b, c, d):
    if T == 'I':
        return a * b * d * n, a * c * d, b * c * d
    return a * b * d, a * c * d * n, b * c * d * n

def check_class(fam, P):
    T, (a, b, c, d) = [coords(fam, P)[0], tuple(sp.sympify(v) for v in coords(fam, P)[1])]
    x, y, z = [sp.expand(t) for t in xyz(T, a, b, c, d)]
    assert sp.expand(4 * x * y * z - n * (x * y + y * z + z * x)) == 0, (fam, P)
    # positivity threshold: x, y, z positive for n > n0
    n0 = 0
    for v in (x, y, z):
        v = sp.Poly(sp.expand(v), n)
        assert v.LC() > 0, (fam, P, v)
        rts = [r for r in sp.real_roots(v)] if v.degree() > 0 else []
        if rts:
            n0 = max(n0, int(sp.floor(max(rts))) + 1)
    return (x, y, z), n0

def integral_on(polys, t, L):
    s = sp.symbols('s')
    for v in polys:
        w = sp.expand(sp.sympify(v).subs(n, t + L * s))
        deg = sp.Poly(w, s).degree() if w.has(s) else 0
        for s0 in range(deg + 1):
            if sp.Rational(w.subs(s, s0)).q != 1:
                return False
    return True

def is_sq(t, l):
    return pow(t % l, (l - 1) // 2, l) == 1

def sigma(r, variant, L):
    pr = [l for l in range(5, r + 1) if all(l % q for q in range(2, l))]
    for l in [8, 3] + pr:
        assert L % l == 0
    out = []
    for t in range(1, L, 2):
        if gcd(t, L) != 1 or t % 8 != 1 or t % 3 != 1:
            continue
        if not (is_sq(t, 5) and is_sq(t, 7)) or is_sq(t, r):
            continue
        if variant == 'np' and not all(is_sq(t, l) for l in pr if l < r):
            continue
        out.append(t)
    return out

def main():
    C = json.load(open(sys.argv[1]))
    r, variant, L = C['r'], C['variant'], C['L']
    exc = set(C['exceptions'])
    cls = []
    N0 = 0
    for fam, P in C['classes']:
        co, n0 = check_class(fam, tuple(P))
        N0 = max(N0, n0)
        cls.append((fam, tuple(P), co))
    print(f"{len(cls)} classes: identities OK; all coordinates positive for n > {N0}")
    S = sigma(r, variant, L)
    assert exc <= set(S)
    bad = []
    # quick prefilter: the class modulus divides lcm of coefficient denominators; just test
    for t in S:
        if t in exc:
            continue
        if not any(integral_on(co, t, L) for _, _, co in cls):
            bad.append(t)
    print(f"Sigma_{r} ({variant}) mod L={L}: {len(S)} residues, {len(exc)} exceptions, "
          f"uncovered non-exceptions: {len(bad)}")
    print("CERTIFICATE OK" if not bad else f"FAIL {bad[:10]}")

if __name__ == '__main__':
    main()
