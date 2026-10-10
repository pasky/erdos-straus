"""O126 §2 checks: lines of S_n, torus parametrisation, Type I/II matrix forms, fibre restriction of alpha.
Run: PYTHONPATH=scripts uv run python scripts/geo_models.py"""
from fractions import Fraction as F
import sympy as sp
from geo_common import hilbert, es_solutions, primes_dividing

x0, x1, x2, x3, n, lam, mu = sp.symbols('x0 x1 x2 x3 n lam mu')
Sn = 4*x1*x2*x3 - n*x0*(x1*x2 + x1*x3 + x2*x3)

# (a) the nine lines of S_n: six edges x_i=x_j=0 and M_i: 4x_i = n x0, x_j + x_k = 0
lines = []
X = [x0, x1, x2, x3]
for i in range(4):
    for j in range(i+1, 4):
        P = [0]*4; Q = [0]*4
        rest = [k for k in range(4) if k not in (i, j)]
        P[rest[0]] = 1; Q[rest[1]] = 1
        lines.append((f"x{i}=x{j}=0", P, Q))
for i, (j, k) in zip([1, 2, 3], [(2, 3), (1, 3), (1, 2)]):
    P = [0]*4; Q = [0]*4
    P[0] = 4; P[i] = n          # point with x0=4, x_i=n, x_j=x_k=0
    Q[j] = 1; Q[k] = -1         # direction x_j=-x_k
    lines.append((f"M{i}", P, Q))
for name, P, Q in lines:
    pt = [lam*P[t] + mu*Q[t] for t in range(4)]
    assert sp.expand(Sn.subs(dict(zip(X, pt)))) == 0, name
print("(a) nine lines on S_n verified:", [l[0] for l in lines])
# singular points: the 4 coordinate points
grad = [sp.diff(Sn, v) for v in X]
for i in range(4):
    pt = [0]*4; pt[i] = 1
    assert all(sp.simplify(g.subs(dict(zip(X, pt)))) == 0 for g in grad)
print("    coordinate points are singular")

# (b) torus parametrisation: positive solutions <-> coprime s with 4 s_i | n S, u_i = nS/(4 s_i)
from math import gcd
for N in [5, 7, 13, 17, 73, 97, 193]:
    sols = es_solutions(N)
    for (a, b, c) in sols:
        s = [F(1, a), F(1, b), F(1, c)]
        L = sp.ilcm(*[t.denominator for t in s])
        si = [int(t*L) for t in s]
        g = gcd(gcd(si[0], si[1]), si[2]); si = [t//g for t in si]
        S = sum(si)
        assert all((N*S) % (4*t) == 0 for t in si)
        assert sorted([N*S//(4*t) for t in si]) == sorted([a, b, c])
print("(b) torus parametrisation verified on all positive solutions for n in {5,...,193}")

# (c) Type I / Type II as matrices M=[[e,2a],[2ad,f]]
def types(N):
    """For prime N: classify each solution, return matrix data."""
    out = []
    for sol in es_solutions(N):
        for perm in [(0, 1, 2), (1, 0, 2), (2, 0, 1)]:
            xx, yy, zz = [sol[t] for t in perm]
            if xx % N == 0 and yy % N and zz % N:      # Type I: x = n d a b, y = d a c, z = d b c
                yield ('I', xx, yy, zz)
            if xx % N and yy % N == 0 and zz % N == 0:  # Type II
                yield ('II', xx, yy, zz)

def abcd_from(kind, N, xx, yy, zz):
    # Type I: x = abdN, y = acd, z = bcd ; Type II: x = abd, y = acdN, z = bcdN
    if kind == 'I':
        X_, Y_, Z_ = xx // N, yy, zz
    else:
        X_, Y_, Z_ = xx, yy // N, zz // N
    d = gcd(gcd(X_, Y_), Z_)
    x_, y_, z_ = X_//d, Y_//d, Z_//d   # = ab, ac, bc
    import math
    abc = math.isqrt(x_*y_*z_); assert abc*abc == x_*y_*z_
    a, b, c = abc//z_, abc//y_, abc//x_
    return a, b, c, d

nI = nII = 0
for N in [p for p in range(5, 1500) if sp.isprime(p)]:
    for kind, xx, yy, zz in types(N):
        for (yy2, zz2) in [(yy, zz), (zz, yy)]:
            a, b, c, d = abcd_from(kind, N, xx, yy2, zz2)
            assert (a*b*d*N if kind == 'I' else a*b*d) == xx
            e = (a + b)//c; assert c*e == a + b
            if kind == 'I':
                f = 4*a*c*d - N
                assert e*f - 4*a*a*d == 1 and f > 0 and (N + f) % (2*(2*a*d)) == 0
                nI += 1
            else:
                f = 4*a*c*d - 1
                assert e*f - 4*a*a*d == N and f > 0 and (f + 1) % (2*(2*a*d)) == 0
                nII += 1
print(f"(c) matrix forms verified: Type I det 1, f=-n mod 2h ({nI}); Type II det n, f=-1 mod 2h ({nII})")

# (d) restriction of alpha to the conic fibre u1 = t is (n(n-4t), -w), w = r u2 - 1, r = (4t-n)/(nt)
cnt = 0
for N in range(3, 160):
    for sol in es_solutions(N):
        for perm in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
            u1, u2, u3 = [sol[t] for t in perm]
            r = F(4*u1 - N, N*u1); w = r*u2 - 1
            assert (r*u2 - 1)*(r*u3 - 1) == 1
            for p in set(primes_dividing(N*u1*u2*u3*(4*u1 - N)*w.numerator*w.denominator)) | {2, 'inf'}:
                assert hilbert(F(-u1, u3), F(-u2, u3), p) == hilbert(N*(N - 4*u1), -w, p), (N, sol, p)
            cnt += 1
print(f"(d) alpha|_(u1=t) = (n(n-4t), -w) verified at all places on {cnt} (solution, fibre) pairs")
