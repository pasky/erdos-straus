"""R291 from-scratch checker: ET/divisor classes on exponential families.

Independent of scripts/c1_expfam_verify.py.  ET families transcribed from
Elsholtz--Tao arXiv:1107.1010v6, Prop. 1.9 and the parametrisations of Section 10.
For each family c0*b^s+k and each class of the paper's tables we
  * check admissibility of kappa (side condition),
  * derive the exact set of s mod P (s >= s_thr) on which n_s lies in the class
    (membership = ET congruences; P = ord_{M'}(b), s_thr from the 2-adic part),
  * compare with the exponent class printed in the paper (must be a SUBSET of the
    derived set; we report if the derived set is larger),
  * verify the explicit solution exactly for s <= SMAX.
"""
from fractions import Fraction as F
from math import gcd, lcm
import sys

SMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 300


def ordmod(b, m):
    if m == 1:
        return 1
    assert gcd(b, m) == 1
    x, o = b % m, 1
    while x != 1:
        x = x * b % m
        o += 1
    return o


def inv(a, m):
    return pow(a, -1, m)


# ---- ET classes: membership(n) -> bool, coords(n) -> (a,b,c,d), type ----
def et(kind, p):
    """returns (modulus, admissible, member(n), sol(n))"""
    if kind == 'D':
        q = p[0]
        # small solution of 4/q by brute force
        sol = None
        for x in range(q // 4 + 1, q + 1):
            r = F(4, q) - F(1, x)
            if r <= 0:
                continue
            for y in range(x, int(2 / r) + 2):
                r2 = r - F(1, y)
                if r2 > 0 and r2.numerator == 1:
                    sol = (x, y, r2.denominator)
                    break
            if sol:
                break
        assert sol, q
        return q, True, (lambda n: n % q == 0), (lambda n: tuple(v * n // q for v in sol))
    if kind == 'I1':
        a, d, f = p
        adm = (4 * a * a * d + 1) % f == 0
        M = 4 * a * d
        e = (4 * a * a * d + 1) // f
        mem = lambda n: (n + f) % M == 0
        def sol(n):
            c = F(n + f, 4 * a * d); b = c * e - a
            return typeI(a, b, c, d, n)
        return M, adm, mem, sol
    if kind == 'I2':
        a, c, f = p
        adm = gcd(4 * a * c, f) == 1
        M = 4 * a * c * f
        mem = lambda n: (n + f) % (4 * a * c) == 0 and (n * a + c) % f == 0
        def sol(n):
            b = F(n * a + c, f); d = F(n + f, 4 * a * c)
            return typeI(a, b, c, d, n)
        return M, adm, mem, sol
    if kind == 'I3':
        c, d, f = p
        adm = gcd(4 * c * d, f) == 1
        M = 4 * c * d * f
        mem = lambda n: (n + f) % (4 * c * d) == 0 and (n * n + 4 * c * c * d) % f == 0
        def sol(n):
            a = F(n + f, 4 * c * d); b = F(n * n + 4 * c * c * d + n * f, 4 * c * d * f)
            return typeI(a, b, c, d, n)
        return M, adm, mem, sol
    if kind == 'I4':
        a, b, e = p
        adm = (a + b) % e == 0 and gcd(e, 4 * a * b) == 1
        M = 4 * a * b
        mem = lambda n: (n * e + 1) % M == 0
        def sol(n):
            return typeI(a, b, F(a + b, e), F(n * e + 1, M), n)
        return M, adm, mem, sol
    if kind == 'II1':
        a, b, e = p
        adm = (a + b) % e == 0 and gcd(e, 4 * a * b) == 1
        M = 4 * a * b
        mem = lambda n: (n + e) % M == 0
        def sol(n):
            return typeII(a, b, F(a + b, e), F(n + e, M), n)
        return M, adm, mem, sol
    if kind == 'II2':
        a, d, f = p
        adm = (f + 1) % (4 * a * d) == 0
        M = f
        mem = lambda n: (n + 4 * a * a * d) % f == 0
        def sol(n):
            c = F(f + 1, 4 * a * d); b = (n * c + a) / f
            return typeII(a, b, c, d, n)
        return M, adm, mem, sol
    if kind == 'II3':
        a, d, e = p
        adm = gcd(4 * a * d, e) == 1
        M = 4 * a * d * e
        mem = lambda n: (n + 4 * a * a * d + e) % M == 0
        def sol(n):
            return typeII(a, F(n + e, 4 * a * d), F(n + 4 * a * a * d + e, M), d, n)
        return M, adm, mem, sol
    raise ValueError(kind)


def typeI(a, b, c, d, n):
    return (a * b * d * n, a * c * d, b * c * d)


def typeII(a, b, c, d, n):
    return (a * b * d, a * c * d * n, b * c * d * n)


def is_sol(n, t):
    return all(F(v).denominator == 1 and v > 0 for v in t) and sum(F(1) / v for v in t) == F(4, n)


def derived_classes(c0, b, k, kind, p):
    """exact set {s mod P : s>=thr, n_s in class}; returns (P, thr, set)"""
    M, adm, mem, sol = et(kind, p)
    a2 = 0
    Mo = M
    while Mo % 2 == 0:
        Mo //= 2; a2 += 1
    P = ordmod(b, Mo)
    thr = 0
    while (b ** thr) % (2 ** a2):
        thr += 1
    S = set()
    for s in range(thr, thr + P):
        if mem(c0 * b ** s + k):
            S.add(s % P)
    return adm, P, thr, S


def check_family(name, c0, b, k, table, exclude=None, small_from=0):
    """table: list of (kind, params, mod, residues, s_min).  exclude(s)->True for
    exponents deliberately left out.  Returns True if all OK."""
    ok = True
    print(f'== {name}: n = {c0}*{b}^s+{k}')
    L = 1
    classes = []
    for kind, p, mod, res, smin in table:
        adm, P, thr, S = derived_classes(c0, b, k, kind, p)
        if not adm:
            print('  NOT ADMISSIBLE', kind, p); ok = False
        # the paper's class: s = r mod mod; must be contained in derived set
        L2 = lcm(P, mod)
        claimed = {s for s in range(L2) if s % mod in res}
        derived = {s for s in range(L2) if s % P in S}
        if not claimed <= derived:
            print('  CLAIM NOT IN DERIVED', kind, p, mod, res, 'derived mod', P, sorted(S)); ok = False
        if derived != claimed:
            print('  note: derived set larger', kind, p, f'claimed {sorted(res)} mod {mod}', f'derived {sorted(S)} mod {P}')
        classes.append((kind, p, mod, res, max(thr, smin)))
        L = lcm(L, mod)
    # coverage of all residues mod L (for large s) using CLAIMED classes
    unc = [r for r in range(L) if not any(r % mod in res for _, _, mod, res, _ in classes)]
    if exclude:
        bad = [r for r in unc if not exclude(r)]
    else:
        bad = unc
    print(f'  lcm={L}; uncovered residues: {len(unc)} {unc[:12]}; not excused: {bad}')
    if bad:
        ok = False
    # exact check of solutions for small s
    for s in range(small_from, SMAX + 1):
        if exclude and exclude(s):
            continue
        n = c0 * b ** s + k
        found = False
        for kind, p, mod, res, thr in classes:
            if s % mod in res and s >= thr:
                M, adm, mem, sol = et(kind, p)
                if not mem(n):
                    print('  MEMBERSHIP FAIL', s, kind, p); ok = False; continue
                if not is_sol(n, sol(n)):
                    print('  SOLUTION FAIL', s, kind, p); ok = False; continue
                found = True
        if not found and s >= small_from:
            print('  s =', s, 'not solved by an ET/divisor class of the table')
    print('  ', 'OK' if ok else 'PROBLEMS')
    return ok
