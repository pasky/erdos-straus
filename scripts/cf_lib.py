"""cf_lib: words of X_n (tuv - u - v = n), Jacobi sign, Hilbert symbols, ternary isotropy (O198)."""
from math import gcd


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def words(n):
    """All (t,u,v) in Z_{>=1}^3 with t*u*v - u - v = n (positive points of X_n)."""
    out = []
    # (tu-1)(tv-1) = tn+1 ; t <= n+2
    for t in range(1, n + 3):
        N = t * n + 1
        # A = tu-1 ranges over divisors of N with A = -1 mod t, A >= t-1
        u = 1
        while True:
            A = t * u - 1
            if A * A > N and A > 0 and False:
                break
            if A > N:
                break
            if A >= 1 and N % A == 0:
                B = N // A
                if (B + 1) % t == 0:
                    v = (B + 1) // t
                    if v >= 1 and t * u * v - u - v == n:
                        out.append((t, u, v))
            u += 1
    return out


def words_fast(n):
    """Same as words(n) but via divisor enumeration of tn+1 (needs factor)."""
    from sympy import divisors
    out = []
    for t in range(1, n + 3):
        N = t * n + 1
        for A in divisors(N):
            if (A + 1) % t == 0:
                B = N // A
                if (B + 1) % t == 0:
                    u, v = (A + 1) // t, (B + 1) // t
                    if u >= 1 and v >= 1:
                        out.append((t, u, v))
    return out


def chi(w, n):
    t, u, v = w
    return jacobi(-(t * u - 1), n)


def v_p(a, p):
    k = 0
    while a % p == 0:
        a //= p
        k += 1
    return k, a


def hilbert(a, b, p):
    """Hilbert symbol (a,b)_p for nonzero integers a, b; p prime or p = -1 (meaning infinity)."""
    if p == -1:
        return -1 if (a < 0 and b < 0) else 1
    al, u = v_p(a, p)
    be, w = v_p(b, p)
    if p != 2:
        def leg(x):
            return 1 if pow(x % p, (p - 1) // 2, p) == 1 else -1
        s = (-1) ** (al * be * ((p - 1) // 2) % 2)
        return s * (leg(u) ** be) * (leg(w) ** al)
    eps = lambda x: ((x - 1) // 2) % 2
    om = lambda x: ((x * x - 1) // 8) % 2
    e = (eps(u) * eps(w) + al * om(w) + be * om(u)) % 2
    return -1 if e else 1


def ternary_aniso(diag, p):
    """Is <a1,a2,a3> (rational diagonal entries given as integers) anisotropic over Q_p?
    q isotropic iff <a1,a2> represents -a3 iff (-a1*a3, -a2*a3)_p = 1."""
    a1, a2, a3 = diag
    return hilbert(-a1 * a3, -a2 * a3, p) == -1


def word_diag(w):
    """Integral diagonalisation of Gram [[v,-1,0],[-1,t,-1],[0,-1,u]] up to squares:
    <v, v*A*, A*n> (from <d1, d2/d1, d3/d2> times squares), A* = tv-1."""
    t, u, v = w
    n = t * u * v - u - v
    As = t * v - 1
    return (v, v * As, As * n)


def ram_set(w):
    """Finite primes where the ternary form of the word is anisotropic (ramification of C0)."""
    from sympy import primefactors
    d = word_diag(w)
    ps = set([2])
    for x in d:
        ps |= set(primefactors(abs(x)))
    return sorted(p for p in ps if ternary_aniso(d, p))
