"""R186 from-scratch checks of small claims in UNIT_ORBIT_ES.md.
(a) the two explicit identities (no-parity example; ES at 169);
(b) Prop 6.1: z in Z  <=>  g = -1 mod 4Q, on all shots n < N, Q in <S> <= QB, g | n+4Q^2, g = 3 mod 4;
(c) Prop 3.2 over K = Q(sqrt5) (eta = phi^j) and K = Q(sqrt2) (eta = (1+sqrt2)^j): Jacobi symbol (n / N(a)) = 1
    for n = 1 mod 8 (for split/inert/ramified primes (n/q) multiplies to (n/|N a|)); also a mod-8 control n = 5;
(d) Thm 5.1 / Prop 4.1(a) over Q(sqrt5): for split l, the set S_l = {n : -n/4 in phi<phi^2> mod q, (n/l) = -1}
    has size |C| >= ord/2 for good q; the shot criterion "q | a_k for some k and (n/q) = -1" vs direct search;
    and: for split l = 3 mod 4 exactly one q | l has (-phi/q) = -1 (so the Kummer condition only selects q).
"""
import sys
from fractions import Fraction
from math import gcd
from sympy import factorint, divisors, sqrt_mod, isprime
from review_uo_common import *

# (a)
assert Fraction(1, 449) + Fraction(1, 18) + Fraction(3125, 8082) == Fraction(4, 9)
assert vp(Fraction(8082, 3125), 5) == -5 and 9 + 4 * 5 ** 5 == 7 * 1787
assert Fraction(1, 52) + Fraction(1, 234) + Fraction(1, 6084) == Fraction(4, 169)
print("(a) explicit identities OK")

# (b)
S = [3, 5, 7, 11]
QS = smonoid(S, 400)
tot = zint = agree = 0
for n in range(1, 3000, 2):
    if n == 1 or any(n % q == 0 for q in S):
        continue
    for Q in QS:
        a = n + 4 * Q * Q
        for g in divisors(a):
            if g % 4 != 3:
                continue
            e = a // g
            x = Fraction(n + e, 4)
            z = Fraction(n) * x * (g + 1) / (4 * Q * Q)
            y = Fraction(n * (g + 1), 4)
            assert 1 / x + 1 / y + 1 / z == Fraction(4, n) and x.denominator == 1
            isz = z.denominator == 1
            tot += 1
            zint += isz
            agree += (isz == ((g + 1) % (4 * Q) == 0))
print(f"(b) Prop 6.1: {tot} shots, z in Z in {zint}, criterion agrees in {agree}")


# (c) arithmetic in Z[w], w^2 = D (D = 5 with phi=(1+sqrt5)/2 handled via 2*phi = 1+sqrt5 -> use Z[phi] norms)
def jac(a, m):  # Jacobi symbol (a/m), m odd positive
    a %= m
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if m % 8 in (3, 5):
                r = -r
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3:
            r = -r
        a %= m
    return r if m == 1 else 0


def phi_pow(j):  # phi^j = u + v phi, j >= 0 ; norm(u+v phi) = u^2 + uv - v^2
    u, v = 1, 0
    for _ in range(j):
        u, v = v, u + v  # (u + v phi) phi = v + (u+v) phi
    return u, v


bad = 0
cnt = 0
ctrl = {}
for n in list(range(9, 2000, 8)) + list(range(5, 2000, 8)):
    for j in range(0, 14):
        for sgn in (1, -1):
            u, v = phi_pow(j)
            u, v = n + 4 * sgn * u, 4 * sgn * v
            N = abs(u * u + u * v - v * v)
            if gcd(N, n) != 1:
                continue
            J = jac(n, N)
            if n % 8 == 1:
                cnt += 1
                bad += (J != 1)
            else:
                ctrl[J] = ctrl.get(J, 0) + 1
        for sgn in (1, -1):  # Q(sqrt2), eps = 1 + sqrt2 ; a = n + 4 eps^j
            u, v = 1, 0
            for _ in range(j):
                u, v = u + 2 * v, u + v
            u, v = n + 4 * sgn * u, 4 * sgn * v
            N = abs(u * u - 2 * v * v)
            if gcd(N, n) != 1:
                continue
            J = jac(n, N)
            if n % 8 == 1:
                cnt += 1
                bad += (J != 1)
print(f"(c) Prop 3.2: {cnt} shots with n = 1 mod 8, total symbol != 1 in {bad}; Q(sqrt5) n = 5 mod 8 control: {ctrl}")

# (d)
good_sizes_ok = True
kummer_ok = True
crit_ok = 0
crit_tot = 0
for l in primes_upto(3000):
    if l < 7 or l % 5 not in (1, 4):
        continue
    roots = sqrt_mod(5, l, all_roots=True)
    phis = sorted({(1 + r) * pow(2, -1, l) % l for r in roots})
    assert len(phis) == 2
    if l % 4 == 3:
        cnt_m = sum(1 for t in phis if legendre(-t, l) == -1)
        kummer_ok &= (cnt_m == 1)
    for t in phis:  # t = phi mod q
        m = 1
        w = t
        while w != 1:
            w = w * t % l
            m += 1
        C = set()
        w = t
        for _ in range(m):
            C.add(w)
            w = w * t * t % l
        good = (l % 4 == 1 and legendre(t, l) == -1) or (l % 4 == 3 and legendre(t, l) == 1)
        inv4 = pow(4, -1, l)
        Sl = {n for n in range(1, l) if (-n * inv4) % l in C and legendre(n, l) == -1}
        if good:
            good_sizes_ok &= (len(Sl) == len(C) and 2 * len(C) >= m)
        # criterion: n in S_l  <=>  some k with q | a_k and (n/q) = -1 (here (n/q) = (n/l) for split q)
        for n in range(1, l):
            direct = any((n + 4 * pow(t, 2 * k + 1, l)) % l == 0 for k in range(m)) and legendre(n, l) == -1
            crit_tot += 1
            crit_ok += (direct == (n in Sl))
print(f"(d) good q: |S_l| = |C| >= ord/2: {good_sizes_ok}; criterion agrees {crit_ok}/{crit_tot}; "
      f"split l = 3 mod 4: exactly one q|l with (-phi/q) = -1: {kummer_ok}")
