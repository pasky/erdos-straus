"""Independent hostile-review checks for LOWERTAIL_ROUND2_ASTRA (z49 ltastra2).

Does NOT import mordell_lib or the author's script.
Run: ulimit -v 8000000; timeout 600 uv run --with numpy --with sympy --with mpmath python scripts/z49_ltastra2rev_check.py
"""
from fractions import Fraction as F
from math import gcd, log
import numpy as np
from sympy import isprime, nextprime, divisors
import mpmath as mp


def et_maps():
    # ET Prop 1.9 (v): n = -e mod 4ab, e | a+b, gcd(e,4ab)=1; (vii): n = -4a^2 d - e mod 4ade, gcd(4ad,e)=1.
    # Own Type II solution formulas (derived by hand, not from mordell_lib).
    k = 0
    for u in range(1, 30):
        for v in range(1, 30):
            if gcd(u, v) != 1:
                continue
            for C in (1, 2, 3, 7):
                if (u + v) % 2:
                    e = u + v
                    assert gcd(e, 4*u*v) == 1  # II1 parameter condition <=> gcd(u,v)=1, u+v odd
                    n = 4*u*v*C - u - v
                    assert (n + e) % (4*u*v) == 0
                    # 4/n = 1/(uvC) + 1/(nuC) + 1/(nvC)
                    assert F(1, u*v*C) + F(1, n*u*C) + F(1, n*v*C) == F(4, n)
                    k += 1
                if v >= 3 and v % 2:
                    x, y = u, v
                    assert gcd(4*x, y) == 1
                    n = 4*x*y*C - 4*x - y
                    if n <= 0:
                        continue
                    b = C*y - 1
                    # 4/n = 1/(x b) + 1/(n C x) + 1/(n C x b)  (check)
                    assert F(1, x*b) + F(1, n*C*x) + F(1, n*C*x*b) == F(4, n), (x, y, C)
                    k += 1
    return k


def legendre_table(r):
    t = np.full(r, -1, dtype=np.int8)
    sq = (np.arange(1, r, dtype=np.int64) ** 2) % r
    t[sq] = 1
    t[0] = 0
    return t


def menu(Q):
    cells = []
    for m in divisors(Q // 4):
        for u in divisors(m):
            v = m // u
            if gcd(u, v) == 1 and (u + v) % 2:
                cells.append((4*m, (-u - v) % (4*m)))
            if v >= 3 and v % 4 == 3 and gcd(u, v) == 1:
                cells.append((4*m, (-4*u - v) % (4*m)))
    return cells


def fibre_check(r, extra):
    """Q = 24 * r * prod(extra); fibre a=1 (24), (a/r)=-1, (a/l)=+1 for l in extra."""
    Q = 24 * r
    for l in extra:
        Q *= l
    # CRT enumeration of fibre
    leg = legendre_table(r)
    res_r = np.nonzero(leg == -1)[0].astype(np.int64)
    comps = [(24, np.array([1], dtype=np.int64)), (r, res_r)]
    for l in extra:
        lt = legendre_table(l)
        comps.append((l, np.nonzero(lt == 1)[0].astype(np.int64)))
    a = np.array([0], dtype=np.int64)
    M = 1
    for (m, rs) in comps:
        # combine a mod M with rs mod m
        inv = pow(M, -1, m)
        # vectorised: x = a + M*((s - a)*inv mod m)
        A = a[:, None]
        S = rs[None, :]
        x = A + M * (((S - A) % m) * inv % m)
        a = x.reshape(-1)
        M *= m
    assert M == Q
    cells = menu(Q)
    cnt = np.zeros(a.shape[0], dtype=np.int32)
    for q, t in cells:
        cnt += (a % q == t)
    mu = F(int(cnt.sum()), int(a.shape[0]))
    return Q, len(cells), int(a.shape[0]), int(cnt.min()), mu, int(a[int(cnt.argmin())])


def lambert():
    out = []
    for L in (1e2, 1e3, 1e4, 1e6, 1e9):
        c, C, eta = 0.1, 1.0, 0.25
        N = mp.e**L / (2*L)  # ~ #primes = 1 (4) in (X,2X]
        t = mp.log(N)
        m = c*L*L
        d = m - mp.floor(eta*m)
        A = d*d/(C*m)
        kstar = -t / mp.lambertw(-t/A, -1)
        # root check
        assert abs(kstar*mp.log(A/kstar) - t) < 1e-8*t
        D = mp.log(L) + mp.log(mp.log(L)) + mp.log((1-eta)**2*c/C)
        approx = L / D
        # denominator discrepancy L/kstar - D should -> 0 (slowly)
        out.append((L, float(kstar), float(approx), float(L/kstar - D)))
    return out


def lyapunov_compare():
    """Does H^-mom (k2=L/log L) imply the H^-crit moment (k1) with the same C?
    Lyapunov loses factor (k2/k1)^k1; report its log."""
    out = []
    for L in (1e2, 1e4, 1e6, 1e9, 1e15):
        c, C, eta, delta = 0.1, 1.0, 0.25, 1.0
        k2 = L/log(L)
        k1 = L/(log(L)+log(log(L))+log((1-eta)**2*c/C)-delta)
        out.append((L, k1*log(k2/k1)))
    return out


if __name__ == "__main__":
    print("ET map identities:", et_maps())
    r = int(2**21.4375) + 1  # first prime = 3 (4) above r0 of STERILE_LOWER Thm 6.3
    while not (isprime(r) and r % 4 == 3):
        r += 1
    print("r =", r)
    for extra in ((), (5,), (5, 7)):
        print("fibre", extra, fibre_check(r, extra), "4/(r-1)=", F(4, r-1))
    for r_small, extra in ((7, ()), (31, ()), (31, (5, 7)), (43, (5,))):
        print("small", r_small, extra, fibre_check(r_small, extra))
    print("lambert (L, k*, L/D, L/k*-D):")
    for row in lambert():
        print("  ", row)
    print("lyapunov log-loss k1*log(k2/k1):", lyapunov_compare())
