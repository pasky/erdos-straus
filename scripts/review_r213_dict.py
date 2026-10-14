"""R213 from-scratch check of CAP_TWO Thm 1.1 / 1.2 / 4.1 (hostile review of O214).

Side A: enumerate ALL k = 1 shot data (Q, g), odd n in [3, NMAX], g <= GMAX, with Q = K*Q1 and
rad(Q1) | K, v_l(Q1) <= 3 (superset of cap 2, incl. the prime 2), compute the shot solution exactly
and test ES^{(y,2)} membership directly from EXPONENT_CAP Def 1.1 (den z = q^2, q odd, gcd(q,n)=1,
rad q | y, v_l(q) <= 2).
Side B: enumerate W_n points 4n a^2 + B^2 + E = c a B E with c,B odd squarefree coprime, 4 | a,
gcd(caB, n) = 1, g = caB - 1 <= GMAX, and map them to shots via Q1 = cB^2, Q0 = caB/4.
Compare A-cap2 with B as sets; check E = 3 mod 4 <=> 4|a over ALL c-odd points (no 4|a restriction),
and the D-face identities of Thm 4.1.
"""
import sys
from fractions import Fraction
from math import gcd
from itertools import product

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200
GMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 100000

LIM = GMAX + 2
spf = list(range(LIM))
for i in range(2, int(LIM ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, LIM, i):
            if spf[j] == j:
                spf[j] = i


def fac(m):
    f = {}
    while m > 1:
        p = spf[m]
        f[p] = f.get(p, 0) + 1
        m //= p
    return f


def sqfree(m):
    return all(e == 1 for e in fac(m).values())


def vl(m, l):
    v = 0
    while m % l == 0:
        m //= l
        v += 1
    return v


def es_y2(n, Q, g):
    """Return (in ES^{(y,2)}, q) for shot solution, directly from Def 1.1."""
    assert (n + 4 * Q * Q) % g == 0
    m = (n + 4 * Q * Q) // g
    assert (n + m) % 4 == 0
    x = (n + m) // 4
    y = n * (g + 1) // 4
    z = Fraction(n * x * (g + 1), 4 * Q * Q)
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
    d = z.denominator
    q = int(round(d ** 0.5))
    while q * q > d:
        q -= 1
    while (q + 1) ** 2 <= d:
        q += 1
    if q * q != d or q % 2 == 0 or gcd(q, n) != 1:
        return False, d
    for l in fac(q) if q < LIM else fac_big(q):
        if y % l or vl(q, l) > 2:
            return False, d
    return True, q


def fac_big(m):
    f = {}
    p = 2
    while p * p <= m:
        while m % p == 0:
            f[p] = f.get(p, 0) + 1
            m //= p
        p += 1
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


# ---------- side A ----------
A = set()          # (n, g, Q1) that are in ES^{(y,2)}
defcell = set()    # (n, g, Q1) by CAP_TWO definition: k=1, rad Q1 | Q0, v<=2 (Q1 odd? recorded)
even_q1 = 0
den_mismatch = 0
for g in range(3, GMAX + 1, 4):
    K = (g + 1) // 4
    fk = fac(K)
    ps = list(fk)
    inv4 = pow(4, -1, g)
    for exps in product(range(4), repeat=len(ps)):
        Q1 = 1
        for p, e in zip(ps, exps):
            Q1 *= p ** e
        n0 = (-Q1 * Q1 * inv4) % g
        n = n0
        while n <= NMAX:
            if n >= 3 and n % 2 == 1:
                Q = K * Q1
                if gcd(Q, n) == 1:
                    assert gcd(Q, K) == K  # k = 1
                    ok, q = es_y2(n, Q, g)
                    if ok:
                        A.add((n, g, Q1))
                        if q != Q1:
                            den_mismatch += 1
                    if max(exps, default=0) <= 2:
                        defcell.add((n, g, Q1))
                        if Q1 % 2 == 0:
                            even_q1 += 1
            n += g
print("side A: ES^{(y,2)} k=1 shots:", len(A), " def-cell:", len(defcell),
      " def-cell with Q1 even:", even_q1, " q != Q1 among members:", den_mismatch)
print("  def-cell minus ES^{(y,2)}:", sorted(defcell - A)[:10])
print("  ES^{(y,2)} minus def-cell:", sorted(A - defcell)[:10])

# ---------- side B ----------
Bset = {}
bad_mod4 = 0
cnt_codd_all = 0
dface_fail = 0
for c in range(1, GMAX + 2, 2):
    for B in range(1, (GMAX + 1) // c + 1, 2):
        cB = c * B
        if cB > GMAX + 1:
            break
        for a in range(1, (GMAX + 1) // cB + 1):
            g = cB * a - 1
            if g < 1:
                continue
            # all c-odd points (any a, any B odd, no squarefree/coprime), for the mod-4 claim
            # 4 n a^2 + B^2 = 0 mod g
            if g % 2 == 0 or gcd(a, g) != 1:
                continue  # impossible anyway (caB = 1 mod g)
            inv = pow(4 * a * a % g, -1, g) if g > 1 else 0
            n0 = (-B * B * inv) % g if g > 1 else 1
            n = n0 if n0 > 0 else g
            while n <= NMAX:
                if n >= 3 and n % 2 == 1:
                    E = (4 * n * a * a + B * B) // g
                    assert E * g == 4 * n * a * a + B * B
                    assert 4 * n * a * a + B * B + E == c * a * B * E
                    cnt_codd_all += 1
                    if (E % 4 == 3) != (a % 4 == 0):
                        bad_mod4 += 1
                    canon = (sqfree(c) and sqfree(B) and gcd(c, B) == 1
                             and a % 4 == 0 and gcd(c * a * B, n) == 1)
                    if canon:
                        Q1 = c * B * B
                        Q0 = c * a * B // 4
                        Q = Q0 * Q1
                        K = (g + 1) // 4
                        assert K == Q0 and g % 4 == 3
                        key = (n, g, Q1)
                        assert key not in Bset, key
                        Bset[key] = (a, B, c, E)
                        # D-face
                        w, r = divmod(4 * n * a + c * B ** 3, g)
                        assert r == 0
                        D = c * B * w - 4 * n
                        if not (a * D == w + c * B ** 3 and a * w == E + B * B
                                and D * g == 4 * n + Q1 * Q1 and D % 4 == 3
                                and (w * w + 4 * n * B * B) % D == 0
                                and (64 * n ** 3 + c * c * w ** 4) % D == 0
                                and (D + 4 * n) % (c * w) == 0):
                            dface_fail += 1
                n += g
print("side B: canonical W_n points:", len(Bset), " all c-odd points:", cnt_codd_all,
      " violations of E=3(4)<=>4|a:", bad_mod4, " D-face failures:", dface_fail)
odd_def = {t for t in defcell if t[2] % 2 == 1}
print("A(ES^(y,2)) == B ?", A == set(Bset), " defcell(odd Q1) == B ?", odd_def == set(Bset))
print("  A - B:", sorted(A - set(Bset))[:10])
print("  B - A:", sorted(set(Bset) - A)[:10])
