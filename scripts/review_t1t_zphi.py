"""R183 from-scratch checks over Z[phi] (phi^2 = phi + 1).  Does NOT use the author's t1t_* code.

Checks:
  L11  Lemma 1.1: ray class group mod 4*inf_1 has order 2, (-1,+) is the non-trivial class,
       and for split / ramified primes q: [q non-trivial]  <=>  (-phi / q) = -1.
  P12  Prop 1.2 on every odd prime p < PMAX, p != 5: find k (|k| <= KMAX) and a PRIME q | a_k in the
       non-trivial class (decided by explicit normalisation, not by chi), build x,y,z, verify exactly
       4xyz = n(xy+yz+zx), sigma_1 > 0, sigma_2 signs not all equal, x prime to n, n | y, n | z.
       Also records the sigma_2 sign pattern (sgn x, sgn y) and checks chi(q) = (p/l).
  SQ   T1 control: odd m < MMAX, n = m^2, |k| <= KMAX: every prime factor of a_k is in the trivial class.
Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_t1t_zphi.py PMAX KMAX MMAX
"""
import sys
from math import isqrt
from sympy import factorint, primerange
from sympy.ntheory import sqrt_mod

# ---- Z[phi] arithmetic: (a, b) = a + b*phi ----
def mul(x, y):
    a, b = x; c, d = y
    return (a * c + b * d, a * d + b * c + b * d)

def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def conj(x): return (x[0] + x[1], -x[1])
def norm(x): a, b = x; return a * a + a * b - b * b

def sgn_P_Q5(P, Q):
    """sign of P + Q*sqrt5, exact"""
    if P >= 0 and Q >= 0: return 0 if P == 0 and Q == 0 else 1
    if P <= 0 and Q <= 0: return -1
    # opposite signs
    if P * P > 5 * Q * Q: return 1 if P > 0 else -1
    return 1 if Q > 0 else -1

def s1(x): a, b = x; return sgn_P_Q5(2 * a + b, b)    # sigma_1(phi) = (1+sqrt5)/2
def s2(x): a, b = x; return sgn_P_Q5(2 * a + b, -b)   # sigma_2(phi) = (1-sqrt5)/2

def exdiv(x, y):
    """exact x / y in Z[phi] or None"""
    n = norm(y); u = mul(x, conj(y))
    if u[0] % n or u[1] % n: return None
    return (u[0] // n, u[1] // n)

def divmod_r(x, y):
    n = norm(y); u = mul(x, conj(y))
    if n < 0: n, u = -n, (-u[0], -u[1])
    q = ((2 * u[0] + n) // (2 * n), (2 * u[1] + n) // (2 * n))
    return q, sub(x, mul(q, y))

def gcd(x, y):
    while y != (0, 0):
        q, r = divmod_r(x, y)
        assert abs(norm(r)) < abs(norm(y))
        x, y = y, r
    return x

PHI = (0, 1); ONE = (1, 0); PHI_INV = (-1, 1)
def upow(j):
    r = ONE; b = PHI if j >= 0 else PHI_INV
    for _ in range(abs(j)): r = mul(r, b)
    return r

def mod4(x): return (x[0] % 4, x[1] % 4)

# ---- Lemma 1.1: direct computation of Cl_{4 inf_1} ----
def lemma11():
    units4 = [(a, b) for a in range(4) for b in range(4) if norm((a, b)) % 2]
    assert len(units4) == 12
    # order of phi mod 4
    o, t = 1, mod4(PHI)
    while t != (1, 0): t = mod4(mul(t, PHI)); o += 1
    assert o == 6 and mod4(upow(3)) == (1, 2)
    img = set()
    for j in range(6):
        for s in (1, -1):
            u = mul((s, 0), upow(j))
            img.add((mod4(u), s1(u)))
    full = {(u, s) for u in units4 for s in (1, -1)}
    assert len(full) == 24 and len(img) == 12
    assert ((3, 0), 1) not in img
    print("L11: |(O/4)^* x {+-1}| = 24, unit image 12, (-1,+) not in image -> Cl_{4inf1} = Z/2, phi order 6 mod 4: OK")

def normalise(g):
    """return unit multiple g' of g with g' = -1 mod 4 and sigma1(g') > 0, or None"""
    s = s1(g)
    gg = (s * g[0], s * g[1])
    for j in range(6):
        h = mul(gg, upow(j))
        if mod4(h) == (3, 0): return h
    return None

def legendre(a, l):
    a %= l
    if a == 0: return 0
    return 1 if pow(a, (l - 1) // 2, l) == 1 else -1

def roots_mod(l):
    """roots of x^2 - x - 1 mod odd prime l: (1 +- sqrt5)/2"""
    if l == 5: return [3]
    s = sqrt_mod(5, l)
    if s is None: return []
    i2 = pow(2, -1, l)
    rs = sorted({(1 + s) * i2 % l, (1 - s) * i2 % l})
    assert all((r * r - r - 1) % l == 0 for r in rs)
    return rs

def ev(x, r, l): return (x[0] + x[1] * r) % l

def primes_of(a, l):
    """generators of the degree-one primes above l (split or l = 5) dividing a"""
    out = []
    for r in ROOTS_ALL(l):
        if ev(a, r, l) == 0:
            q = gcd((l, 0), (-r, 1))
            assert abs(norm(q)) == l
            out.append(q)
    return out

def ROOTS_ALL(l):
    return ROOTS[l] if l in ROOTS else roots_mod(l)

def chi_direct(q_gen, l):
    """(-phi / q) for a prime of degree one above l, via the residue map"""
    for r in roots_mod(l):
        if ev(q_gen, r, l) == 0:
            return legendre(-r, l)
    raise ValueError

SMALL = [l for l in primerange(3, 4000) if l % 5 in (0, 1, 4)]
ROOTS = {l: roots_mod(l) for l in SMALL}

def kseq(K):
    yield 0
    for k in range(1, K + 1):
        yield k; yield -k

def solve_prime(p, K, stats):
    for k in kseq(K):
        eta = upow(2 * k + 1)
        a = add((p, 0), mul((4, 0), eta))
        # candidate rational primes l: small split/ramified first, then full factorisation
        cands = [l for l in SMALL if any((p + 4 * pow(r, 2 * k + 1, l)) % l == 0 for r in ROOTS[l])]
        if not cands:
            cands = [l for l in factorint(abs(norm(a))) if l % 5 in (0, 1, 4)]
        for l, q in [(l, q) for l in cands for q in primes_of(a, l)]:
            g = normalise(q)
            ch = chi_direct(q, l)
            stats['chi_checks'] += 1
            # Lemma 1.1 / Thm 1.3 consistency: normalisable <=> chi = -1 <=> (p/l) = -1  (l = 5: (p/5))
            assert (g is not None) == (ch == -1) == (legendre(p, l) == -1), (p, k, l)
            if g is None: continue
            e = exdiv(a, g); assert e is not None
            assert s1(e) > 0
            xn = add((p, 0), e); assert xn[0] % 4 == 0 and xn[1] % 4 == 0
            x = (xn[0] // 4, xn[1] // 4)
            gp1 = add(g, ONE); assert gp1[0] % 4 == 0 and gp1[1] % 4 == 0
            y = (p * gp1[0] // 4, p * gp1[1] // 4)
            z = exdiv(mul(mul((p, 0), x), gp1), mul((4, 0), eta)); assert z is not None
            lhs = mul((4, 0), mul(x, mul(y, z)))
            rhs = mul((p, 0), add(add(mul(x, y), mul(y, z)), mul(z, x)))
            assert lhs == rhs
            assert s1(x) > 0 and s1(y) > 0 and s1(z) > 0
            sg = (s2(x), s2(y), s2(z))
            assert len(set(sg)) == 2, (p, k, sg)
            stats['pat'][sg[:2]] = stats['pat'].get(sg[:2], 0) + 1
            assert norm(x) % p != 0                           # x prime to p
            assert y[0] % p == 0 and y[1] % p == 0 and z[0] % p == 0 and z[1] % p == 0
            return k
    return None

def square_control(m, K):
    n = m * m
    for k in kseq(K):
        eta = upow(2 * k + 1)
        a = add((n, 0), mul((4, 0), eta))
        for l in factorint(abs(norm(a))):
            if l % 5 in (2, 3):  # inert: never contributes a degree-one prime; check class of l itself is trivial
                assert normalise((l, 0)) is None
                continue
            qs = primes_of(a, l)
            assert qs
            for q in qs:
                assert (normalise(q) is not None) == (chi_direct(q, l) == -1)
                if normalise(q) is not None:
                    return k
    return None

if __name__ == "__main__":
    PMAX, K, MMAX = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    lemma11()
    stats = {'chi_checks': 0, 'pat': {}}
    hist = {}; fails = []
    cnt = 0
    for p in primerange(3, PMAX):
        if p == 5: continue
        cnt += 1
        k = solve_prime(p, K, stats)
        if k is None: fails.append(p)
        else: hist[abs(k)] = hist.get(abs(k), 0) + 1
    print(f"P12: primes tested {cnt}, solved {cnt - len(fails)}, failures {fails[:20]}")
    print("P12: min|k| histogram (first k found in order 0,1,-1,2,-2,..):", dict(sorted(hist.items())))
    print("P12: chi/normalisability/(p/l) consistency checks:", stats['chi_checks'])
    print("P12: sigma_2 (sgn x, sgn y) patterns:", stats['pat'])
    bad = [m for m in range(3, MMAX, 2) if square_control(m, K) is not None]
    print(f"SQ: odd m in [3,{MMAX}), |k|<={K}: squares solved by Prop 1.2: {bad}")
