"""z68 PC2: exact two-prime (in fact any-S) event enumerator built ONLY from the reduction of Z68_PC2.md Theorem A.

Every ET Prop 1.9 family class catching a profile e_{S,gamma} (gamma at S, 1 elsewhere) with S-level N comes from a
solution of the single equation
        Q(alpha, beta):   4 X Y Z W = alpha X + beta Y + Z      (X, Y, Z, W >= 1)
with (alpha, beta, N) of one of two shapes (Theorem A):
  shape I  : (F A, F B), N = A B F, gcd(AB, F) = 1   -> I-2 (all), II-2 (A = B = 1), I-4 / II-1 (F = 1)
             (X, Y, Z, W) = (x, y, w, D):  a = A x, c = B y, F z + 1 = 4 x y D, a + c = w z, f = F z
  shape II : (A^2 D F, F), N = A D F, gcd(AD, F) = 1 -> I-3, II-3 (all), I-1 (F = 1)
             (X, Y, Z, W) = (x, t, u, y):  c (or a) = A x, d = D y, F z + 1 = 4 x y t, f (or e) = F z,
             z s = 4 A^2 D x^2 y + 1 with s = 4 x y u - F;  I-1: (X,Y,Z,W) = (a', C, w, d'), f = 4 a' d' C - 1.
Q is solved COMPLETELY by the divisor case analysis of Lemma Q (every solution has one of P, R, XY, YW, XW, XZ, ZW,
YZ <= T = (4 alpha beta / 3)^(2/5)), then every candidate class is re-tested LITERALLY (primitive, r = 1 mod m',
cylinder recorded).  Nothing here assumes the reduction is correct: a missed class would show up in the comparison
with the literal brute force (z66_ucover_kbrute logic, re-implemented in brute_cylinders below).

Usage:
  uv run --with cypari2 python scripts/z68_pc2_events.py selftest A B          # Q-solver vs brute force, alpha,beta < A,B
  uv run --with cypari2 python scripts/z68_pc2_events.py events L1 K1 L2 K2 OUT  # all cylinders at levels <= (K1,K2)
  uv run --with cypari2 python scripts/z68_pc2_events.py compare L1 K1 L2 K2 MMAX EVENTSFILE  # vs literal brute force
Output lines: k1 k2 rho1 rho2 family m r  (cylinder: g = rho1 mod L1^k1, h = rho2 mod L2^k2).
"""
import sys
from functools import lru_cache
from math import gcd

import cypari2

pari = cypari2.Pari()


@lru_cache(maxsize=1 << 20)
def divs(n):
    return tuple(int(x) for x in pari.divisors(n))


def qsolve(al, be):
    """All (X,Y,Z,W) in N^4 with 4XYZW = al X + be Y + Z (Lemma Q case analysis; complete)."""
    # exact integer cutoff: smallest T with 9 T^5 >= 16 (al be)^2, i.e. T >= (4 al be / 3)^(2/5)
    T = max(1, int((4 * al * be / 3) ** 0.4) - 2)
    while 9 * T ** 5 < 16 * (al * be) ** 2:
        T += 1
    out = set()

    def add(X, Y, Z, W):
        if X >= 1 and Y >= 1 and Z >= 1 and W >= 1 and 4 * X * Y * Z * W == al * X + be * Y + Z:
            out.add((X, Y, Z, W))

    for P in range(1, T + 1):                      # P = 4YZW - al
        n = P + al
        if n % 4 == 0:
            m = n // 4
            for Y in divs(m):
                for Z in divs(m // Y):
                    W = m // Y // Z
                    if (be * Y + Z) % P == 0:
                        add((be * Y + Z) // P, Y, Z, W)
    for R in range(1, T + 1):                      # R = 4XZW - be
        n = R + be
        if n % 4 == 0:
            m = n // 4
            for X in divs(m):
                for Z in divs(m // X):
                    W = m // X // Z
                    if (al * X + Z) % R == 0:
                        add(X, (al * X + Z) // R, Z, W)
    for u in range(1, T + 1):
        for v in range(1, T // u + 1):
            q = 4 * u * v
            num = al * u + be * v                  # (X,Y) = (u,v): E | al X + be Y
            for E in divs(num):
                if (E + 1) % q == 0:
                    add(u, v, num // E, (E + 1) // q)
            num = al + 4 * be * u * u * v          # (Y,W) = (u,v): E | al + 4 be Y^2 W
            for E in divs(num):
                if (E + 1) % q == 0:
                    X = (E + 1) // q
                    if (al * X + be * u) % E == 0:
                        add(X, u, (al * X + be * u) // E, v)
            num = be + 4 * al * u * u * v          # (X,W) = (u,v): E | be + 4 al X^2 W
            for E in divs(num):
                if (E + 1) % q == 0:
                    Y = (E + 1) // q
                    if (al * u + be * Y) % E == 0:
                        add(u, Y, (al * u + be * Y) // E, v)
            num = al * u + v                       # (X,Z) = (u,v): R | al X + Z
            for R in divs(num):
                if (R + be) % q == 0:
                    add(u, num // R, v, (R + be) // q)
            num = al * be + 4 * u * u * v          # (Z,W) = (u,v): P | al be + 4 Z^2 W
            for P in divs(num):
                if (P + al) % q == 0:
                    Y = (P + al) // q
                    if (be * Y + u) % P == 0:
                        add((be * Y + u) // P, Y, u, v)
            num = be * u + v                       # (Y,Z) = (u,v): P | be Y + Z
            for P in divs(num):
                if (P + al) % q == 0:
                    add(num // P, u, v, (P + al) // q)
    return out


def qbrute(al, be):
    out = set()
    lim = max(al, be)
    for Y in range(1, lim + 1):
        for Z in range(1, lim // Y + 1):
            for W in range(1, lim // (Y * Z) + 1):
                P = 4 * Y * Z * W - al
                if P > 0 and (be * Y + Z) % P == 0:
                    out.add(((be * Y + Z) // P, Y, Z, W))
                R = 4 * Y * Z * W - be
                if R > 0 and (al * Y + Z) % R == 0:
                    out.add((Y, (al * Y + Z) // R, Z, W))
    return out


# ---------------------------------------------------------------- literal class test
class Rec:
    def __init__(self, S, K):
        self.S, self.K = S, K
        self.cyl = {}

    def split(self, m):
        ks = []
        for l in self.S:
            k = 0
            while m % l == 0:
                m //= l
                k += 1
            ks.append(k)
        return ks, m

    def test(self, r, m, fam):
        r %= m
        if gcd(r, m) != 1:
            return
        ks, mp = self.split(m)
        if sum(ks) == 0 or r % mp != 1 % mp:
            return
        if any(k > K for k, K in zip(ks, self.K)):
            return
        key = tuple(ks) + tuple(r % l ** k for l, k in zip(self.S, ks))
        old = self.cyl.get(key)
        if old is None or m < old[1]:
            self.cyl[key] = (fam, m, r)


def crt2(r1, m1, r2, m2):
    g = gcd(m1, m2)
    assert g == 1
    t = ((r2 - r1) * pow(m1, -1, m2)) % m2
    return (r1 + m1 * t) % (m1 * m2), m1 * m2


def sqrt_all(a, f):
    """all x mod f with x^2 = a (f odd, gcd(a,f)=1)"""
    if f == 1:
        return [0]
    res = [0]
    mod = 1
    fac = pari.factor(f)
    for i in range(len(fac[0])):
        p, e = int(fac[0][i]), int(fac[1][i])
        pe = p ** e
        loc = [x for x in range(pe) if (x * x - a) % pe == 0] if pe < 5000 else None
        if loc is None:
            if pow(a % p, (p - 1) // 2, p) != 1:
                return []
            r0 = int(pari.Mod(a, p).sqrt().lift())
            pk = p
            for _ in range(1, e):              # Hensel lift (p odd, a unit)
                pk *= p
                r0 = (r0 - (r0 * r0 - a) * pow(2 * r0, -1, pk)) % pk
            assert (r0 * r0 - a) % pe == 0
            loc = sorted({r0 % pe, (-r0) % pe})
        if not loc:
            return []
        res = [crt2(x, mod, y, pe)[0] for x in res for y in loc]
        mod *= pe
    return res


def snum_parts(N, S):
    exps = []
    for l in S:
        k = 0
        while N % l == 0:
            N //= l
            k += 1
        exps.append(k)
    return exps


def sdivisors(exps, S):
    out = [1]
    for l, e in zip(S, exps):
        out = [d * l ** i for d in out for i in range(e + 1)]
    return out


def sfree(x, S):
    return all(x % l for l in S)


def events(S, K, rec):
    """Generate every candidate class from the reduction, at all levels <= K, and test literally."""
    full = 1
    for l, k in zip(S, K):
        full *= l ** k
    levels = [N for N in sdivisors(K, S) if N > 1]
    qcache = {}

    def Q(al, be):
        if (al, be) not in qcache:
            qcache[(al, be)] = qsolve(al, be)
        return qcache[(al, be)]

    for N in levels:
        ex = snum_parts(N, S)
        for F in sdivisors(ex, S):
            rest = N // F
            for A in sdivisors(snum_parts(rest, S), S):
                B = rest // A                          # shape I: (A, B, F);  shape II: (A, D, F) with D := B
                if gcd(A * B, F) != 1:
                    continue
                # ---- shape I
                for (x, y, w, D) in Q(F * A, F * B):
                    if (4 * x * y * D - 1) % F:
                        continue
                    z = (4 * x * y * D - 1) // F
                    a, c, f = A * x, B * y, F * z
                    if (a + c) != w * z:
                        continue
                    # family-specific S-part filters: the S-part of every parameter entering the modulus is fixed
                    if sfree(x, S) and sfree(y, S) and sfree(z, S) and gcd(4 * a * c, f) == 1:   # I-2 (modulus 4acf)
                        r2 = (-c * pow(a, -1, f)) % f if f > 1 else 0
                        rec.test(*crt2((-f) % (4 * a * c), 4 * a * c, r2, f), "I-2")
                    if A == 1 and B == 1 and sfree(z, S):              # II-2 (modulus f; a, c, d unrestricted)
                        if gcd(f, 4 * a * c * D) == 1:
                            rec.test(-4 * a * a * D, f, "II-2")
                    if F == 1 and sfree(x, S) and sfree(y, S):         # I-4 / II-1 (modulus 4ab; e = z unrestricted)
                        e = z
                        if gcd(e, 4 * a * c) == 1:
                            rec.test(-pow(e, -1, 4 * a * c), 4 * a * c, "I-4")
                            rec.test(-e, 4 * a * c, "II-1")
                # ---- shape II  (A, D=B, F)
                Dd = B
                for (x, t, u, y) in Q(A * A * Dd * F, F):
                    if (4 * x * y * t - 1) % F:
                        continue
                    z = (4 * x * y * t - 1) // F
                    if not (sfree(x, S) and sfree(y, S) and sfree(z, S)):
                        continue
                    cc, d, f = A * x, Dd * y, F * z
                    s = 4 * x * y * u - F
                    if s <= 0 or z * s != 4 * A * A * Dd * x * x * y + 1:
                        continue
                    if gcd(4 * cc * d, f) == 1:
                        M1 = 4 * cc * d
                        for root in sqrt_all((-4 * cc * cc * d) % f, f):  # I-3
                            if f == 1 or gcd(root, f) == 1:
                                rec.test(*crt2((-f) % M1, M1, root % f, f), "I-3")
                        rec.test(-4 * cc * cc * d - f, 4 * cc * d * f, "II-3")  # II-3 with (a,d,e) = (cc,d,f)
                if F == 1:                                     # I-1: Q(A^2 D, 1, 1), (a', C, w, d')
                    for (ap, C, w, dp) in Q(A * A * Dd, 1):
                        if not (sfree(ap, S) and sfree(dp, S)):
                            continue
                        a, d = A * ap, Dd * dp
                        f = 4 * ap * dp * C - 1
                        if (4 * a * a * d + 1) % f == 0:
                            rec.test(-f, 4 * a * d, "I-1")


# ---------------------------------------------------------------- literal brute force (kbrute logic, all S)
def brute_cylinders(S, K, MMAX, rec):
    rel = lambda m: any(m % l == 0 for l in S)
    for a in range(1, MMAX // 4 + 1):                       # I-1
        for d in range(1, MMAX // (4 * a) + 1):
            m = 4 * a * d
            if rel(m):
                for f in divs(4 * a * a * d + 1):
                    rec.test(-f, m, "I-1")
    for a in range(1, MMAX // 4 + 1):                       # I-2
        for c in range(1, MMAX // (4 * a) + 1):
            M1 = 4 * a * c
            for f in range(1, MMAX // M1 + 1):
                m = M1 * f
                if not rel(m) or gcd(M1, f) != 1:
                    continue
                r2 = (-c * pow(a, -1, f)) % f if f > 1 else 0
                rec.test(*crt2((-f) % M1, M1, r2, f), "I-2")
    for c in range(1, MMAX // 4 + 1):                       # I-3
        for d in range(1, MMAX // (4 * c) + 1):
            M1 = 4 * c * d
            for f in range(1, MMAX // M1 + 1):
                m = M1 * f
                if not rel(m) or gcd(M1, f) != 1:
                    continue
                for x in sqrt_all((-4 * c * c * d) % f, f):
                    if f == 1 or gcd(x, f) == 1:
                        rec.test(*crt2((-f) % M1, M1, x % f, f), "I-3")
    for a in range(1, MMAX // 4 + 1):                       # I-4, II-1
        for b in range(1, MMAX // (4 * a) + 1):
            m = 4 * a * b
            if not rel(m):
                continue
            for e in divs(a + b):
                if gcd(e, m) == 1:
                    rec.test(-pow(e, -1, m), m, "I-4")
                    rec.test(-e, m, "II-1")
    for f in range(3, MMAX + 1, 4):                         # II-2
        if not rel(f):
            continue
        P = (f + 1) // 4
        for a in divs(P):
            for d in divs(P // a):
                rec.test(-4 * a * a * d, f, "II-2")
    for a in range(1, MMAX // 4 + 1):                       # II-3
        for d in range(1, MMAX // (4 * a) + 1):
            for e in range(1, MMAX // (4 * a * d) + 1):
                m = 4 * a * d * e
                if rel(m) and gcd(4 * a * d, e) == 1:
                    rec.test(-4 * a * a * d - e, m, "II-3")


def main():
    mode = sys.argv[1]
    if mode == "selftest":
        A, B = int(sys.argv[2]), int(sys.argv[3])
        bad = 0
        for al in range(1, A):
            for be in range(1, B):
                if qsolve(al, be) != qbrute(al, be):
                    bad += 1
                    print("MISMATCH", al, be)
        print(f"selftest qsolve == brute for 1 <= alpha < {A}, 1 <= beta < {B}: mismatches = {bad}")
        sys.exit(1 if bad else 0)
    if mode == "events1":                        # single prime S = {L}: UCOVER profiles e_{L,g}
        L, KK = int(sys.argv[2]), int(sys.argv[3])
        rec = Rec((L,), (KK,))
        events((L,), (KK,), rec)
        with open(sys.argv[4], "w") as fh:
            fh.write(f"# z68 PC2 reduction-built single-prime events, S=({L},), levels <= {KK}; k rho family m r\n")
            for key in sorted(rec.cyl):
                fam, m, r = rec.cyl[key]
                fh.write(" ".join(map(str, key)) + f" {fam} {m} {r}\n")
        print(f"{len(rec.cyl)} cylinders written")
        return
    L1, K1, L2, K2 = map(int, sys.argv[2:6])
    S, K = (L1, L2), (K1, K2)
    if mode == "events":
        rec = Rec(S, K)
        events(S, K, rec)
        with open(sys.argv[6], "w") as fh:
            fh.write(f"# z68 PC2 reduction-built events, S={S}, levels <= {K}; k1 k2 rho1 rho2 family m r (min modulus)\n")
            for key in sorted(rec.cyl):
                fam, m, r = rec.cyl[key]
                fh.write(" ".join(map(str, key)) + f" {fam} {m} {r}\n")
        print(f"{len(rec.cyl)} cylinders written")
    elif mode == "compare":
        MMAX = int(sys.argv[6])
        ev = {}
        for line in open(sys.argv[7]):
            if line.startswith("#"):
                continue
            t = line.split()
            ev[tuple(map(int, t[:4]))] = (t[4], int(t[5]), int(t[6]))
        rec = Rec(S, K)
        brute_cylinders(S, K, MMAX, rec)
        br = rec.cyl
        small_ev = {k for k, v in ev.items() if v[1] <= MMAX}   # reduction cylinders whose minimal class has m <= MMAX
        miss = [k for k in br if k not in small_ev]               # bounded sets compared symmetrically
        extra = [k for k in small_ev if k not in br]
        mdiff = [k for k in br if k in ev and ev[k][1] != br[k][1]]  # minimal moduli must agree too
        print(f"S={S} levels<={K} MMAX={MMAX}: brute cylinders {len(br)}, reduction cylinders {len(ev)} "
              f"({len(small_ev)} with a class of modulus <= MMAX)")
        print(f"brute not found by reduction: {len(miss)} {sorted(miss)[:20]}")
        print(f"reduction (modulus <= MMAX) not found by brute: {len(extra)} {sorted(extra)[:20]}")
        print(f"cylinders with different minimal modulus: {len(mdiff)} {sorted(mdiff)[:20]}")
        print("NOTE: compares deduplicated cylinders (with minimal moduli), not every parameter tuple")
        sys.exit(1 if (miss or extra or mdiff) else 0)


if __name__ == "__main__":
    main()
