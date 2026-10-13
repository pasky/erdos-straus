"""R183: from-scratch check of T1_TEMPLATE §4 over Z[theta], theta^3 = 2 (h = 1, norm-Euclidean, r1 = r2 = 1).
* units: eps = theta - 1 > 0, N(eps) = 1;  ray class group Cl_{4 inf} = ((O/4)^* x {+-1}) / <-1, eps>.
* Prop 1.2 analogue: a_k = n + 4 eps^k = e g, g = -1 (mod 4), g > 0 (real place), e > 0 =>
  x = (n+e)/4, y = n(g+1)/4, z = n x (g+1)/(4 eps^k) solve 4/n = 1/x+1/y+1/z, all positive.  Existence of g
  <=> some sub-product of the prime factors of a_k lies in the class of (-1,+) (exact subset search on classes).
* For each odd prime p < PMAX: find the least |k| <= K with a solution, construct it and verify exactly.
* T1 control: odd m < MMAX, |k| <= K: no sub-product of prime factors of a_k (complete factorisation) is in (-1,+).
Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_t1t_cbrt2.py PMAX K MMAX
"""
import sys, itertools
from fractions import Fraction
from sympy import factorint, primerange
from sympy.ntheory import nthroot_mod
import mpmath
from review_t1t_local import Field

F = Field('Q(cbrt2)', [2, 0, 0], (0, 1, 0), 3, 1, {3: ((1, 1, 0), 2)})
TH = mpmath.cbrt(2)
ONE = (1, 0, 0); EPS = (-1, 1, 0); EPSI = F.exdiv(ONE, EPS)
assert F.norm(EPS) == 1 and EPSI is not None

def sign(a):
    v = a[0] + a[1] * TH + a[2] * TH ** 2
    assert abs(v) > mpmath.mpf(10) ** -40
    return 1 if v > 0 else -1

def upow(k):
    r = ONE
    for _ in range(abs(k)): r = F.mul(r, EPS if k > 0 else EPSI)
    return r

def m4(a): return tuple(x % 4 for x in a)

# ---- ray class group mod 4*inf ----
UNITS4 = [a for a in itertools.product(range(4), repeat=3) if F.norm(a) % 2]
img = set()
u = ONE
for j in range(64):
    img.add((m4(u), 1)); img.add((m4(F.sc(-1, u)), -1))
    u = F.mul(u, EPS)
IMG = set()
for (a, s) in img:      # close (should already be a group)
    IMG.add((a, s))
FULL = [(a, s) for a in UNITS4 for s in (1, -1)]
CL = {}
reps = []
for el in [((1, 0, 0), 1)] + FULL:
    if el in CL: continue
    idx = len(reps); reps.append(el)
    for (b, t) in IMG: CL[(m4(F.mul(el[0], b)), el[1] * t)] = idx
NCL = len(reps)
TARGET = CL[((3, 0, 0), 1)]

def cls(g): return CL[(m4(g), sign(g))]

def clmul(i, j):
    a, s = reps[i]; b, t = reps[j]
    return CL[(m4(F.mul(a, b)), s * t)]

# ---- Euclidean gcd ----
def divround(a, b):
    q = F.div(a, b)
    base = [round(x) for x in q]
    best = None
    for d in itertools.product((-1, 0, 1), repeat=3):
        qq = tuple(base[i] + d[i] for i in range(3))
        r = F.add(a, F.sc(-1, F.mul(qq, b)))
        nr = abs(F.norm(r))
        if best is None or nr < best[0]: best = (nr, qq, r)
    return best

def gcd(a, b):
    while any(b):
        nr, q, r = divround(a, b)
        assert nr < abs(F.norm(b)), 'Euclid step failed'
        a, b = b, r
    return a

def prime_factors(a):
    """list of prime generators (with multiplicity) of the ideal (a), a odd"""
    out = []
    cur = a
    for l, e in factorint(abs(F.norm(a))).items():
        assert l != 2
        if l == 3:
            gens = [(1, 1, 0)]
        else:
            rts = nthroot_mod(2, 3, l, all_roots=True) or []
            gens = []
            for r in rts:
                gens.append(gcd((l, 0, 0), (-r, 1, 0)))
            if len(rts) == 1:            # l = q1 q2, deg q2 = 2
                gens.append(F.exdiv((l, 0, 0), gens[0]))
            if len(rts) == 0:
                gens = [(l, 0, 0)]       # inert
        for g in gens:
            assert abs(F.norm(g)) in (l, l * l, l ** 3)
            while True:
                q = F.exdiv(cur, g)
                if q is None: break
                out.append(g); cur = q
    assert abs(F.norm(cur)) == 1, 'incomplete factorisation'
    return out

def find_subproduct(gs):
    """subset of gs whose product is in TARGET class; returns product element or None"""
    cl = [cls(g) for g in gs]
    reach = {CL[((1, 0, 0), 1)]: ()}
    for i, c in enumerate(cl):
        new = {}
        for k, sub in reach.items():
            k2 = clmul(k, c)
            if k2 not in reach and k2 not in new: new[k2] = sub + (i,)
        reach.update(new)
    if TARGET not in reach: return None
    g = ONE
    for i in reach[TARGET]: g = F.mul(g, gs[i])
    return g

def normalise(g):
    """unit multiple +-eps^j g with = -1 mod 4 and > 0"""
    s = sign(g); g = F.sc(s, g)
    u = g
    for j in range(64):
        if m4(u) == (3, 0, 0) and sign(u) > 0: return u
        u = F.mul(u, EPS)
    raise AssertionError('not normalisable although in target class')

def kseq(K):
    yield 0
    for k in range(1, K + 1): yield k; yield -k

def solve(n, K):
    for k in kseq(K):
        eta = upow(k)
        a = F.add((n, 0, 0), F.sc(4, eta))
        g = find_subproduct(prime_factors(a))
        if g is None: continue
        g = normalise(g)
        e = F.exdiv(a, g); assert e is not None and sign(e) > 0
        xn = F.add((n, 0, 0), e); assert all(c % 4 == 0 for c in xn)
        x = tuple(c // 4 for c in xn)
        gp = F.add(g, ONE); assert all(c % 4 == 0 for c in gp)
        y = tuple(n * c // 4 for c in gp)
        z = F.exdiv(F.mul(F.sc(n, x), gp), F.sc(4, eta)); assert z is not None
        assert F.sc(4, F.mul(x, F.mul(y, z))) == F.sc(n, F.add(F.add(F.mul(x, y), F.mul(y, z)), F.mul(z, x)))
        assert sign(x) > 0 and sign(y) > 0 and sign(z) > 0
        return k, (x, y, z)
    return None

if __name__ == "__main__":
    PMAX, K, MMAX = map(int, sys.argv[1:4])
    print(f"|Cl_(4inf)| = {NCL} (|(O/4)^*| = {len(UNITS4)}, unit image {len(IMG)})")
    # the document's example p = 13, k = 2
    x, y, z = (7, 3, 2), (0, -13, 13), (312, 221, 182)
    assert F.sc(4, F.mul(x, F.mul(y, z))) == F.sc(13, F.add(F.add(F.mul(x, y), F.mul(y, z)), F.mul(z, x)))
    print("example p=13: 4xyz = 13(xy+yz+zx) OK; signs", sign(x), sign(y), sign(z))
    hist = {}; fails = []
    for p in primerange(3, PMAX):
        r = solve(p, K)
        if r is None: fails.append(p)
        else: hist[abs(r[0])] = hist.get(abs(r[0]), 0) + 1
    print("primes: min|k| histogram", dict(sorted(hist.items())), "failures", fails)
    bad = [m for m in range(3, MMAX, 2) if solve(m * m, K) is not None]
    print(f"squares m^2, odd m < {MMAX}, |k| <= {K}: solved by the unit mechanism: {bad}")
