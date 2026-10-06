"""Erdős–Straus polynomial-identity classes (Elsholtz–Tao Prop 1.9 families).

Task O80 (POINTWISE_MORDELL.md).  Seven families of residue classes; every
sufficiently large n in such a class has an explicit ES solution given by
polynomials in n (ET §10, proof of Prop 1.9; ET (2.1)-(2.22)).

A class is (fam, params); `cls_modulus_residues` returns (M, sorted residues mod M).
`solve(fam, params, n)` returns (x, y, z) via ET's parametrisation and the maps
pi^I (abdn, acd, bcd), pi^II (abd, acdn, bcdn); None if non-integral/non-positive.
"""
from math import gcd
from fractions import Fraction


def inv(a, m):
    return pow(a, -1, m)


def divisors(n):
    ds = [1]
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            ds = [d * p ** i for d in ds for i in range(e + 1)]
        p += 1
    if x > 1:
        ds = [d * q for d in ds for q in (1, x)]
    return sorted(ds)


_SQ = {}


def sqrt_mod_set(t, f):
    """all s mod f with s^2 = t (mod f) (brute force per prime power, CRT)."""
    t %= f
    key = (t, f)
    if key in _SQ:
        return _SQ[key]
    sols, mod = [0], 1
    for p, e in factor_small(f).items():
        q = p ** e
        loc = [s for s in range(q) if (s * s - t) % q == 0]
        new = []
        for s0 in sols:
            for s1 in loc:
                new.append((s0 + mod * (((s1 - s0) * pow(mod, -1, q)) % q)) % (mod * q))
        sols, mod = new, mod * q
    _SQ[key] = sorted(sols) if f > 1 else [0]
    return _SQ[key]


def cls_modulus_residues(fam, P):
    """(M, residues) for a class; residues are those n mod M in the class."""
    if fam == 'I1':
        a, d, f = P
        assert (4 * a * a * d + 1) % f == 0
        M = 4 * a * d
        return M, [(-f) % M]
    if fam == 'I2':
        a, c, f = P
        assert gcd(4 * a * c, f) == 1
        m1 = 4 * a * c
        M = m1 * f
        r1 = (-f) % m1
        r2 = (-c * inv(a, f)) % f if f > 1 else 0
        x = (r1 + m1 * (((r2 - r1) * inv(m1, f)) % f if f > 1 else 0)) % M
        return M, [x]
    if fam == 'I3':
        c, d, f = P
        assert gcd(4 * c * d, f) == 1
        m1 = 4 * c * d
        M = m1 * f
        r1 = (-f) % m1
        res = []
        for s in sqrt_mod_set(-4 * c * c * d, f):
            x = (r1 + m1 * (((s - r1) * inv(m1, f)) % f if f > 1 else 0)) % M
            res.append(x)
        return M, sorted(res)
    if fam == 'I4':
        a, b, e = P
        assert (a + b) % e == 0 and gcd(e, 4 * a * b) == 1
        M = 4 * a * b
        return M, [(-inv(e, M)) % M]
    if fam == 'II1':
        a, b, e = P
        assert (a + b) % e == 0 and gcd(e, 4 * a * b) == 1
        M = 4 * a * b
        return M, [(-e) % M]
    if fam == 'II2':
        a, d, f = P
        assert (f + 1) % (4 * a * d) == 0
        return f, [(-4 * a * a * d) % f]
    if fam == 'II3':
        a, d, e = P
        assert gcd(4 * a * d, e) == 1
        M = 4 * a * d * e
        return M, [(-4 * a * a * d - e) % M]
    raise ValueError(fam)


def _q(num, den):
    if num % den:
        return None
    return num // den


def solve(fam, P, n):
    """ET parametrisation -> (x,y,z) with 4/n = 1/x+1/y+1/z, or None."""
    if fam == 'I1':
        a, d, f = P
        e = (4 * a * a * d + 1) // f
        c = _q(n + f, 4 * a * d)
        if c is None:
            return None
        b = c * e - a
        T = 'I'
    elif fam == 'I2':
        a, c, f = P
        b = _q(n * a + c, f)
        d = _q(n + f, 4 * a * c)
        if b is None or d is None:
            return None
        T = 'I'
    elif fam == 'I3':
        c, d, f = P
        a = _q(n + f, 4 * c * d)
        b = _q(n * n + 4 * c * c * d + n * f, 4 * c * d * f)
        if a is None or b is None:
            return None
        T = 'I'
    elif fam == 'I4':
        a, b, e = P
        c = (a + b) // e
        d = _q(n * e + 1, 4 * a * b)
        if d is None:
            return None
        T = 'I'
    elif fam == 'II1':
        a, b, e = P
        c = (a + b) // e
        d = _q(n + e, 4 * a * b)
        if d is None:
            return None
        T = 'II'
    elif fam == 'II2':
        a, d, f = P
        c = (f + 1) // (4 * a * d)
        ee = _q(n + 4 * a * a * d, f)
        if ee is None:
            return None
        b = c * ee - a
        T = 'II'
    elif fam == 'II3':
        a, d, e = P
        b = _q(n + e, 4 * a * d)
        c = _q(n + 4 * a * a * d + e, 4 * a * d * e)
        if b is None or c is None:
            return None
        T = 'II'
    else:
        raise ValueError(fam)
    if T == 'I':
        x, y, z = a * b * d * n, a * c * d, b * c * d
    else:
        x, y, z = a * b * d, a * c * d * n, b * c * d * n
    if min(x, y, z) <= 0:
        return None
    if Fraction(4, n) != Fraction(1, x) + Fraction(1, y) + Fraction(1, z):
        return None
    return (x, y, z)


def factor_small(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def classes_for_modulus(M):
    """All (fam, params) classes of the seven families whose modulus is exactly M."""
    out = []
    # II2: f = M, M = 3 mod 4, a*d | (M+1)/4
    if M % 4 == 3:
        A = (M + 1) // 4
        for a in divisors(A):
            for d in divisors(A // a):
                out.append(('II2', (a, d, M)))
    if M % 4 == 0:
        Q = M // 4
        # 4ab families (I1 uses 4ad with f | 4a^2 d + 1)
        for a in divisors(Q):
            b = Q // a
            for f in divisors(4 * a * a * b + 1):
                out.append(('I1', (a, b, f)))
            for e in divisors(a + b):
                if gcd(e, 4 * a * b) == 1:
                    out.append(('I4', (a, b, e)))
                    out.append(('II1', (a, b, e)))
        # 4 x y z with third factor coprime: I2 (a,c,f), I3 (c,d,f), II3 (a,d,e)
        for z in divisors(Q):
            if gcd(z, 4 * (Q // z)) != 1:
                continue
            xy = Q // z
            for x in divisors(xy):
                y = xy // x
                out.append(('I2', (x, y, z)))
                out.append(('I3', (x, y, z)))
                out.append(('II3', (x, y, z)))
    return out


def residue_table(M):
    """sorted list of residues mod M covered by classes of exact modulus M,
    with one witness class per residue (dict residue -> (fam, params))."""
    wit = {}
    for fam, P in classes_for_modulus(M):
        MM, R = cls_modulus_residues(fam, P)
        assert MM == M
        for r in R:
            if r not in wit:
                wit[r] = (fam, P)
    return wit
