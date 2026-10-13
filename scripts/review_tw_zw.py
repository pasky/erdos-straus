"""R182 from-scratch Z[w] toolkit (w = primitive cube root of unity, w^2 = -1 - w).
Elements are pairs (a, b) = a + b w.  Independent of scripts/tw_eis*.py.
Provides: arithmetic, factorisation, cubic residue character, tame cubic Hilbert symbols,
and a brute-force lambda-adic (lambda = 1 - w) test "is (a, b)_lambda trivial?" via local norm groups.
Run as a script: self-validation (brute-force cubes, cubic reciprocity, Hilbert reciprocity vs the
brute-force lambda test, conductor facts of Cor 2.2(f), U^(4) in cubes)."""
import random
from math import isqrt
from sympy import factorint

Z0, ONE, W = (0, 0), (1, 0), (0, 1)
LAM = (1, -1)


def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def neg(x): return (-x[0], -x[1])
def mul(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)
def conj(x): return (x[0] - x[1], -x[1])
def norm(x): return x[0] * x[0] - x[0] * x[1] + x[1] * x[1]
def pw(x, k):
    r = ONE
    for _ in range(k): r = mul(r, x)
    return r
def divexact(x, y):
    """x / y if in Z[w] else None"""
    n = norm(y); t = mul(x, conj(y))
    if t[0] % n or t[1] % n: return None
    return (t[0] // n, t[1] // n)
def sc(k, x): return (k * x[0], k * x[1])

UNITS = [ONE, W, mul(W, W), neg(ONE), neg(W), neg(mul(W, W))]


def is_2primary(x): return x[0] % 2 == 1 and x[1] % 2 == 0


def split_prime(p):
    """a prime pi with N(pi) = p (p = 3 or p = 1 mod 3), brute force"""
    for b in range(1, isqrt(4 * p // 3) + 2):
        # a^2 - ab + b^2 = p
        D = 4 * p - 3 * b * b
        if D < 0: break
        s = isqrt(D)
        if s * s == D:
            for a in ((b + s) // 2, (b - s) // 2):
                if norm((a, b)) == p: return (a, b)
    raise ValueError(p)


_pcache = {}
def primes_over(p):
    """list of (prime element, residue degree) over rational prime p"""
    if p in _pcache: return _pcache[p]
    if p == 3: r = [(LAM, 1)]
    elif p % 3 == 2: r = [((p, 0), 2)]
    else:
        pi = split_prime(p); r = [(pi, 1), (conj(pi), 1)]
    _pcache[p] = r
    return r


def val(x, pi):
    k = 0
    while True:
        q = divexact(x, pi)
        if q is None: return k, x
        x = q; k += 1


def factor(x):
    """dict prime -> exponent, and unit u with x = u * prod"""
    assert x != Z0
    f = {}
    for p, e in factorint(norm(x)).items():
        for pi, deg in primes_over(p):
            k, x = val(x, pi)
            if k: f[pi] = k
    assert norm(x) == 1
    return f, x


# ---------------- residue fields and cubic characters ----------------
def reduce_mod(x, pi):
    """canonical representative of x mod pi: split/lambda -> integer mod p ; inert p -> pair mod p"""
    N = norm(pi)
    if pi[1] == 0 and N == pi[0] ** 2:  # inert rational prime
        p = pi[0]; return (x[0] % p, x[1] % p)
    p = N
    # w = r mod pi with r^2 + r + 1 = 0 mod p, r = -a/b where pi = a + b w (b invertible mod p)
    a, b = pi
    r = (-a * pow(b, -1, p)) % p
    return ((x[0] + x[1] * r) % p, 0)


def rmul(x, y, pi):
    N = norm(pi)
    if pi[1] == 0 and N == pi[0] ** 2:
        p = pi[0]; z = mul(x, y); return (z[0] % p, z[1] % p)
    return ((x[0] * y[0]) % N, 0)


def rpow(x, k, pi):
    r = (1, 0); b = x
    while k:
        if k & 1: r = rmul(r, b, pi)
        b = rmul(b, b, pi); k >>= 1
    return r


def chi3(x, pi):
    """cubic residue character exponent k in Z/3: x^((N-1)/3) = w^k mod pi (x a pi-unit)"""
    N = norm(pi)
    assert N % 3 == 1
    t = rpow(reduce_mod(x, pi), (N - 1) // 3, pi)
    for k, u in enumerate([ONE, W, mul(W, W)]):
        if reduce_mod(u, pi) == t: return k
    raise ValueError("not a unit / not a cube root of 1", x, pi)


def tame3(a, b, pi):
    """cubic Hilbert symbol (a, b)_pi at a tame prime pi (N(pi) = 1 mod 3), as exponent in Z/3
    via the tame symbol (-1)^{v(a)v(b)} a^{v(b)} / b^{v(a)} and chi3."""
    va, a1 = val(a, pi); vb, b1 = val(b, pi)
    # (-1) is a cube, drop it; a^{vb} b^{-va} = a1^{vb} b1^{-va} * pi^{va vb - vb va}
    return (vb * chi3(a1, pi) - va * chi3(b1, pi)) % 3


def frac_val(num, den, pi):
    return val(num, pi)[0] - val(den, pi)[0]


def tame3_frac(a, b, pi):
    """a, b given as (num, den) pairs in Z[w]"""
    va = frac_val(*a, pi); vb = frac_val(*b, pi)
    ua = chi3(val(a[0], pi)[1], pi) - chi3(val(a[1], pi)[1], pi)
    ub = chi3(val(b[0], pi)[1], pi) - chi3(val(b[1], pi)[1], pi)
    return (vb * ua - va * ub) % 3


# ---------------- lambda-adic brute force ----------------
NINE = 9  # lambda^4 = 9 * w^2, so O/lambda^4 = O/9
def mod9(x): return (x[0] % 9, x[1] % 9)

_basis = [add(ONE, pw(LAM, i)) for i in (1, 2, 3)]
_table = {}
for i in range(3):
    for j in range(3):
        for k in range(3):
            e = mod9(mul(mul(pw(_basis[0], i), pw(_basis[1], j)), pw(_basis[2], k)))
            _table[e] = (i, j, k)
assert len(_table) == 27, "basis of U1/U4 not independent"


def vcoords(x):
    """coordinates of x in V = K_lam^*/K_lam^{*3} = Z/3 (valuation) x (U1/U4 ~ F_3^3), x in Z[w] nonzero.
    Uses U^(4) in K^{*3} (checked in selftest) and -1 = (-1)^3."""
    v, u = val(x, LAM)
    # u is a lambda-unit; u mod lambda in F_3 = {1, 2}
    r = (u[0] + u[1]) % 3  # w = 1 mod lambda
    assert r != 0
    if r == 2: u = neg(u)
    return (v % 3,) + _table[mod9(u)]


def vcoords_frac(num, den):
    a = vcoords(num); b = vcoords(den)
    return tuple((x - y) % 3 for x, y in zip(a, b))


def _span(vecs):
    """row-reduced basis over F_3"""
    basis = []
    for v in vecs:
        v = list(v)
        for bv, piv in basis:
            if v[piv]: c = v[piv]; v = [(x - c * y) % 3 for x, y in zip(v, bv)]
        nz = [i for i, x in enumerate(v) if x]
        if nz:
            piv = nz[0]; inv = 1 if v[piv] == 1 else 2
            v = [(x * inv) % 3 for x in v]
            nb = []
            for bv, p2 in basis:
                if bv[piv]: c = bv[piv]; bv = [(x - c * y) % 3 for x, y in zip(bv, v)]
                nb.append((bv, p2))
            basis = nb + [(v, piv)]
    return basis


def _in_span(basis, v):
    v = list(v)
    for bv, piv in basis:
        if v[piv]: c = v[piv]; v = [(x - c * y) % 3 for x, y in zip(v, bv)]
    return not any(v)


_ngcache = {}
def norm_group(a, rng=random.Random(1), tries=400):
    """F_3-basis of N(K_lam(a^{1/3})^*) K^{*3}/K^{*3} inside V, a in Z[w]; None if a is a local cube.
    Certified: index of the norm group is exactly 3 (local CFT), so dim 3 reached => exact."""
    ca = vcoords(a)
    if not any(ca): return None
    key = ca
    if key in _ngcache: return _ngcache[key]
    # the extension depends only on the class of a in V: use a small canonical representative
    a = mul(pw(LAM, ca[0]), mul(pw(_basis[0], ca[1]), mul(pw(_basis[1], ca[2]), pw(_basis[2], ca[3]))))
    assert vcoords(a) == ca
    a2 = mul(a, a); vecs = []
    for t in range(5 * tries):
        R = 3 + t // 50
        c = [(rng.randint(-R, R), rng.randint(-R, R)) for _ in range(3)]
        n = add(add(pw(c[0], 3), mul(a, pw(c[1], 3))), mul(a2, pw(c[2], 3)))
        n = sub(n, sc(3, mul(a, mul(c[0], mul(c[1], c[2])))))
        if n == Z0: continue
        vecs.append(vcoords(n))
        if t % 20 == 19 and len(_span(vecs)) == 3: break
    basis = _span(vecs)
    assert len(basis) == 3, ("norm group not found", a, len(basis))
    _ngcache[key] = basis
    return basis


def lam_trivial(a, b):
    """True iff (a, b)_lambda = 0 (a, b in Z[w] nonzero), by the norm-residue definition."""
    B = norm_group(a)
    if B is None: return True
    return _in_span(B, vcoords(b))


def lam_trivial_frac(a, b):
    """a, b as (num, den); scale to integers using cubes: num/den = num*den^2 / den^3"""
    A = mul(a[0], mul(a[1], a[1])); Bb = mul(b[0], mul(b[1], b[1]))
    return lam_trivial(A, Bb)


def tame_places(*elts):
    ps = set()
    for x in elts:
        for p in factorint(norm(x)):
            if p != 3:
                for pi, _ in primes_over(p): ps.add(pi)
    return ps


def tame_sum(a, b):
    """sum over all tame places of (a, b)_v, a, b as (num, den)"""
    ps = tame_places(a[0], a[1], b[0], b[1]) | {(2, 0)}
    return sum(tame3_frac(a, b, pi) for pi in ps if pi != (2, 0) or True) % 3, ps


# ---------------- self-tests ----------------
def selftest():
    rng = random.Random(7)
    # 1. cubic character vs brute force cubes in residue field
    for p in [7, 13, 19, 31, 37, 43, 61, 2, 5, 11]:
        for pi, deg in primes_over(p):
            N = norm(pi)
            if N % 3 != 1: continue
            if deg == 1: elems = [(x, 0) for x in range(1, p)]
            else: elems = [(x, y) for x in range(p) for y in range(p) if (x, y) != (0, 0)]
            cubes = {rpow(e, 3, pi) for e in elems}
            for e in elems:
                assert (chi3(e, pi) == 0) == (reduce_mod(e, pi) in cubes)
            # multiplicativity
            for _ in range(50):
                x, y = rng.choice(elems), rng.choice(elems)
                assert chi3(mul(x, y), pi) == (chi3(x, pi) + chi3(y, pi)) % 3
    print("chi3 == brute-force cube test, multiplicative: OK")
    # 2. cubic reciprocity: primary primes (= 2 mod 3) pi1, pi2 of coprime norm: chi_{pi1}(pi2) = chi_{pi2}(pi1)
    def primary(pi):
        for u in UNITS:
            x = mul(u, pi)
            if x[0] % 3 == 2 and x[1] % 3 == 0: return x
    prs = []
    for p in range(5, 400):
        if all(p % d for d in range(2, isqrt(p) + 1)) and p != 3:
            for pi, _ in primes_over(p): prs.append(primary(pi))
    cnt = 0
    for i in range(len(prs)):
        for j in range(len(prs)):
            a, b = prs[i], prs[j]
            if norm(a) % 3 != 1 or norm(b) % 3 != 1: continue
            if factorint(norm(a)).keys() & factorint(norm(b)).keys(): continue
            assert chi3(a, b) == chi3(b, a), (a, b); cnt += 1
    print(f"cubic reciprocity on {cnt} ordered pairs of primary primes: OK")
    # 3. U^(4) subset of cubes, checked mod lambda^8 = 81
    M = 81
    cubes = {((x * x * x - 3 * x * y * y + y ** 3) % M, (3 * x * x * y - 3 * x * y * y) % M)
             for x in range(M) for y in range(M)}
    # verify formula for cube
    for _ in range(20):
        x, y = rng.randint(-50, 50), rng.randint(-50, 50); c = pw((x, y), 3)
        assert ((c[0]) % M, c[1] % M) == ((x ** 3 - 3 * x * y * y + y ** 3) % M, (3 * x * x * y - 3 * x * y * y) % M)
    L4 = pw(LAM, 4)
    U4 = {((1 + mul(L4, (s, t))[0]) % M, mul(L4, (s, t))[1] % M) for s in range(9) for t in range(9)}
    assert U4 <= cubes
    print(f"U^(4) mod lambda^8 ({len(U4)} classes) all cubes: OK")
    # 4. Hilbert reciprocity: tame sum == 0  <=>  lambda-symbol trivial (brute force norm group)
    agree = [0, 0]
    for _ in range(300):
        a = (rng.randint(-40, 40), rng.randint(-40, 40)); b = (rng.randint(-40, 40), rng.randint(-40, 40))
        if a == Z0 or b == Z0: continue
        s, _ = tame_sum((a, ONE), (b, ONE))
        lt = lam_trivial(a, b)
        assert (s == 0) == lt, (a, b, s, lt)
        agree[lt] += 1
    print(f"Hilbert reciprocity (tame sum vs brute-force lambda symbol) on {sum(agree)} random pairs:"
          f" OK ({agree[0]} with nontrivial lambda symbol)")
    # 5. Cor 2.2(f) facts on the basis of V
    l1, l2, l3 = _basis
    tests = {"(1+l^2,1+l^3)": (l2, l3), "(1+l,1+l^3)": (l1, l3), "(w,1+l^3)": (W, l3),
             "(1+l,1+l^2)": (l1, l2), "(lam,1+l^3)": (LAM, l3), "(w,1+l^2)": (W, l2),
             "(lam,1+l^2)": (LAM, l2), "(w,lam)": (W, LAM), "(w,2)": (W, (2, 0)), "(w,w)": (W, W),
             "(2,2)": ((2, 0), (2, 0)), "(w,-1)": (W, (-1, 0))}
    for k, (a, b) in tests.items():
        print(f"   {k}_lambda trivial: {lam_trivial(a, b)}")


if __name__ == "__main__":
    selftest()
