"""R194 from-scratch Z[omega] arithmetic + complete TES solver (no import of tf_* / tw_*).

Elements: tuples (a, b) = a + b*w, w = zeta_3, w^2 = -1 - w.
TES(n): 9/n = w/x + w^2/y + 2/z, x, y, z in O, all ≡ 1 (mod 2O).
Completeness: Prop 1.1(a) (re-derived in the review): some i has N(x_i) <= 9 N(c_i) N(n) / 81;
for that i, with A = 9 x_i - c_i n, B = n x_i, (A x_j - B c_j)(A x_k - B c_k) = B^2 c_j c_k, so x_j, x_k are
read off from ALL divisors d of M = B^2 c_j c_k (all ideal divisors times all 6 units).
"""
import sys, math, time

W = (0, 1)
W2 = (-1, -1)
ONE = (1, 0)
TWO = (2, 0)
UNITS = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1)]


def mul(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def conj(x):
    a, b = x
    return (a - b, -b)


def norm(x):
    a, b = x
    return a * a - a * b + b * b


def divexact(x, y):
    """x / y if y | x in O, else None."""
    n = norm(y)
    p = mul(x, conj(y))
    if p[0] % n or p[1] % n:
        return None
    return (p[0] // n, p[1] // n)


def is2primary(x):
    return x[0] % 2 == 1 and x[1] % 2 == 0


def power(x, e):
    r = ONE
    for _ in range(e):
        r = mul(r, x)
    return r


def disk(R):
    """All nonzero lattice points a + b w with norm <= R."""
    out = []
    bmax = int(math.isqrt(int(4 * R / 3) + 1)) + 1
    for b in range(-bmax, bmax + 1):
        disc = 4 * R - 3 * b * b
        if disc < 0:
            continue
        s = math.isqrt(int(disc)) + 1
        for a in range((b - s) // 2 - 1, (b + s) // 2 + 2):
            if (a, b) != (0, 0) and norm((a, b)) <= R:
                out.append((a, b))
    return out


_prime_of_norm = {}


def prime_above(p):
    """An Eisenstein prime of norm p (p = 3 or p ≡ 1 mod 3)."""
    if p in _prime_of_norm:
        return _prime_of_norm[p]
    for b in range(1, int(math.isqrt(4 * p // 3)) + 2):
        disc = 4 * p - 3 * b * b
        if disc < 0:
            break
        s = math.isqrt(disc)
        if s * s == disc and (b + s) % 2 == 0:
            r = ((b + s) // 2, b)
            assert norm(r) == p
            _prime_of_norm[p] = r
            return r
    raise ValueError(p)


def factor_int(m):
    f = {}
    d = 2
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def factor_O(x):
    """Return (unit, {prime: exp}) with x = unit * prod prime^exp; primes as tuples."""
    res = {}
    rest = x
    for p, _ in factor_int(norm(x)).items():
        if p % 3 == 2:
            cands = [(p, 0)]
        elif p == 3:
            cands = [(1, -1)]  # lambda = 1 - w
        else:
            pi = prime_above(p)
            cands = [pi, conj(pi)]
        for q in cands:
            while True:
                t = divexact(rest, q)
                if t is None:
                    break
                rest = t
                res[q] = res.get(q, 0) + 1
    assert norm(rest) == 1, (x, rest)
    return rest, res


def divisors(fac):
    """All divisors (with all 6 unit multiples) of an element with factorisation fac (prime->exp)."""
    ds = [ONE]
    for q, e in fac.items():
        new = []
        qp = [ONE]
        for _ in range(e):
            qp.append(mul(qp[-1], q))
        for d in ds:
            for t in qp:
                new.append(mul(d, t))
        ds = new
    return [mul(u, d) for d in ds for u in UNITS]


C = [W, W2, TWO]


def check(n, sol):
    x, y, z = sol
    # 9xyz == n (c1 y z + c2 x z + c3 x y)
    lhs = mul((9, 0), mul(x, mul(y, z)))
    rhs = mul(n, add(add(mul(W, mul(y, z)), mul(W2, mul(x, z))), mul(TWO, mul(x, y))))
    return lhs == rhs


def solve_tes(n, nfac):
    """Complete solution set of TES(n). nfac: factorisation dict of n."""
    Nn = norm(n)
    sols = set()
    for i in range(3):
        j, k = [t for t in range(3) if t != i]
        R = 9 * norm(C[i]) * Nn / 81.0
        cjck = mul(C[j], C[k])
        _, cfac = factor_O(cjck)
        for xi in disk(R):
            if not is2primary(xi):
                continue
            A = sub(mul((9, 0), xi), mul(C[i], n))
            assert A != (0, 0)
            B = mul(n, xi)
            M = mul(mul(B, B), cjck)
            _, xfac = factor_O(xi)
            fac = dict(cfac)
            for q, e in nfac.items():
                fac[q] = fac.get(q, 0) + 2 * e
            for q, e in xfac.items():
                fac[q] = fac.get(q, 0) + 2 * e
            # merge associate keys: factor_O always returns canonical prime reps, so keys are consistent
            Bcj = mul(B, C[j]); Bck = mul(B, C[k])
            for d in divisors(fac):
                xj = divexact(add(d, Bcj), A)
                if xj is None or not is2primary(xj):
                    continue
                e2 = divexact(M, d)
                assert e2 is not None
                xk = divexact(add(e2, Bck), A)
                if xk is None or not is2primary(xk):
                    continue
                s = [None] * 3
                s[i], s[j], s[k] = xi, xj, xk
                s = tuple(s)
                assert check(n, s), (n, s)
                sols.add(s)
    return sols


def two_primary_assoc(x):
    for u in UNITS:
        y = mul(u, x)
        if is2primary(y):
            return y
    return None


def canon_factor_prime(n):
    """n is a prime of O; return {canonical prime rep: 1} as factor_O would."""
    _, f = factor_O(n)
    return f


def primes_upto(Nmax, inert_too=True):
    """One 2-primary prime per conjugate pair (split) + inert p, with N(pi) <= Nmax, pi not | 6."""
    out = []
    sieve = bytearray([1]) * (Nmax + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(Nmax ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    for p in range(5, Nmax + 1):
        if not sieve[p]:
            continue
        if p % 3 == 1:
            out.append((p, two_primary_assoc(prime_above(p))))
        elif inert_too and p * p <= Nmax:
            out.append((p * p, (p, 0)))
    out.sort()
    return out


def shape(n, sol):
    return sum(1 for t in sol if divexact(t, n) is not None)


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "census":
        Nmax = int(sys.argv[2])
        zeros = []
        tot = {}
        shapes = {}
        t0 = time.time()
        for N, pi in primes_upto(Nmax):
            S = solve_tes(pi, canon_factor_prime(pi))
            for s in S:
                sh = shape(pi, s); shapes[sh] = shapes.get(sh, 0) + 1
            band = 0 if N <= 1000 else (1 if N <= 3000 else 2)
            c = tot.setdefault(band, [0, 0, 0])
            c[0] += 1; c[1] += len(S); c[2] += (len(S) == 0)
            if not S:
                zeros.append((N, pi))
                print("ZERO", N, pi, flush=True)
        print("zeros:", [z[0] for z in zeros])
        for b, c in sorted(tot.items()):
            print("band", b, "primes", c[0], "sols", c[1], "mean %.2f" % (c[1] / c[0]), "zeros", c[2])
        print("shapes (#coords divisible by pi):", shapes, "time %.0fs" % (time.time() - t0))
    elif mode == "one":
        a, b = int(sys.argv[2]), int(sys.argv[3])
        pi = (a, b)
        t0 = time.time()
        S = solve_tes(pi, canon_factor_prime(pi))
        print("N =", norm(pi), "pi =", pi, "2-primary", is2primary(pi), "#sols", len(S), "%.1fs" % (time.time() - t0))
        for s in sorted(S)[:5]:
            print(" ", s)
    elif mode == "conjcheck":
        Nmax = int(sys.argv[2])
        for N, pi in primes_upto(Nmax, inert_too=False):
            S1 = solve_tes(pi, canon_factor_prime(pi))
            pc = conj(pi)
            S2 = solve_tes(pc, canon_factor_prime(pc))
            S3 = solve_tes((-pi[0], -pi[1]), canon_factor_prime(pi))
            mapped = {(conj(y), conj(x), conj(z)) for (x, y, z) in S1}
            neg = {tuple((-t[0], -t[1]) for t in s) for s in S1}
            assert mapped == S2 and neg == S3, N
        print("conjugation / sign symmetry OK up to", Nmax)
