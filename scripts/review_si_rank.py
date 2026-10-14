"""R204: from-scratch recomputation of the SIGN_IDENTITY §3 certificate (exact rational rank) for the 8 targets.
Columns rebuilt independently from the document's verbal description (48 columns); words enumerated
independently.  Certificate = exact rank_Q([C|y]) > rank_Q(C) on the first SUB rows (n >= 3) of each class mod 8.
Usage: uv run python scripts/review_si_rank.py SUB"""
import sys
from fractions import Fraction
from math import isqrt

SUB = int(sys.argv[1]) if len(sys.argv) > 1 else 120
NMAX = 8 * SUB + 16
HM = 24 * NMAX + 1

# 12*H(N) for N>=0 (Hurwitz class number of discriminant -N), by reduced forms
H12 = [0] * (HM + 1)
H12[0] = -1
a = 1
while 3 * a * a <= HM:
    for b in range(-a + 1, a + 1):
        c = a
        while True:
            N = 4 * a * c - b * b
            if N > HM:
                break
            if N > 0 and (b >= 0 or (abs(b) < a and a < c)):
                if not (b < 0 and (abs(b) == a or a == c)):
                    w = 12
                    if b == 0 and a == c:
                        w = 6
                    elif b == a and a == c:
                        w = 4
                    H12[N] += w
            c += 1
    a += 1


def jac(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0


def kron(D, m):  # Kronecker (D/m), m >= 1
    r = 1
    while m % 2 == 0:
        m //= 2
        if D % 2 == 0:
            return 0
        if D % 8 in (3, 5):
            r = -r
    if m == 1:
        return r
    return r * jac(D, m)


def divs(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def ndiv(n):
    return len(divs(n))


def kh(k, j, n, sgn=False):
    tot, s = 0, 0
    while k * n - j * s * s >= 0:
        w = 1 if s == 0 else 2
        if sgn and s % 2:
            w = -w
        tot += w * H12[k * n - j * s * s]
        s += 1
    return tot


def rtern(a, b, c, n):
    cnt = 0
    for x in range(-isqrt(n // a), isqrt(n // a) + 1):
        r1 = n - a * x * x
        for y in range(-isqrt(r1 // b), isqrt(r1 // b) + 1):
            r2 = r1 - b * y * y
            if r2 % c == 0:
                z2 = r2 // c
                z = isqrt(z2)
                if z * z == z2:
                    cnt += 1 if z == 0 else 2
    return cnt


def columns(n):
    v = [1, n] + [H12[k * n] for k in (1, 3, 4, 8, 12, 16, 24)]
    v += [kh(1, 1, n), kh(4, 1, n), kh(4, 1, n, True), kh(8, 1, n), kh(8, 1, n, True), kh(4, 2, n), kh(8, 2, n),
          kh(4, 8, n), kh(16, 1, n), kh(3, 1, n), kh(12, 1, n)]
    D_ = divs(n)
    for D in (1, -4, 8, -8, -3, 12, 5, -7):
        v += [sum(kron(D, d) for d in D_), sum(kron(D, d) * d for d in D_)]
    v += [sum(min(d, n // d) for d in D_)]
    v += [ndiv(n + 1), ndiv(n + 2), ndiv(n + 3), ndiv(2 * n + 1)]
    v += [rtern(*q, n) for q in ((1, 1, 1), (1, 1, 2), (1, 2, 2), (1, 1, 3), (1, 2, 3), (1, 3, 5))]
    v += [1 if isqrt(n) ** 2 == n else 0]
    assert len(v) == 48
    return v


def targets(n):
    Np = Nm = NpI = NmI = SpT = SmT = 0
    for u in range(1, n + 3):
        for vv in range(1, n + 3):
            if (u - 1) * (vv - 1) > n + 1:
                break
            s = n + u + vv
            if s % (u * vv):
                continue
            t = s // (u * vv)
            ch = jac(-(t * u - 1), n)
            inter = t >= 2 and u >= 2 and vv >= 2
            if ch == 1:
                Np += 1; NpI += inter; SpT += t
            else:
                Nm += 1; NmI += inter; SmT += t
    return dict(Np=Np, Nm=Nm, S=Np - Nm, X=Np + Nm, NpI=NpI, NmI=NmI, SpT=SpT, SmT=SmT)


def rank(M):
    M = [[Fraction(x) for x in r] for r in M]
    rk, ncol = 0, len(M[0])
    for c in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c] / M[rk][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk


rows = {}
for n in range(3, NMAX, 2):
    rows.setdefault(n % 8, [])
    if len(rows[n % 8]) < SUB:
        rows[n % 8].append((columns(n), targets(n)))
for cls in sorted(rows):
    R = rows[cls]
    C = [r[0] for r in R]
    rC = rank(C)
    res = []
    for tn in ("Np", "Nm", "S", "X", "NpI", "NmI", "SpT", "SmT"):
        rCy = rank([r[0] + [r[1][tn]] for r in R])
        res.append(f"{tn}:{'CERT' if rCy > rC else 'IN-SPAN?'}")
    print(f"class {cls} rows={len(R)} rank_Q(C)={rC} ", " ".join(res))

# sanity: Hurwitz values and a planted in-span target must NOT certify
assert [H12[k] for k in (3, 4, 7, 8, 11, 12, 15, 16, 20, 23)] == [4, 6, 12, 12, 12, 16, 24, 18, 24, 36], H12[:24]
R = rows[1]
C = [r[0] for r in R]
planted = [r[0] + [3 * r[0][2] - 5 * r[0][20] + r[0][47]] for r in R]
assert rank(planted) == rank(C), "planted relation wrongly certified"
print("sanity OK (Hurwitz table, planted relation detected as in-span)")
