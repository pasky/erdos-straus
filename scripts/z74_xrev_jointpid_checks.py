#!/usr/bin/env python3
"""Independent finite checks for the Opus cross-review of LOGIC_JOINT_NR_TS.md / LOGIC_FOUR_SQUARES.md.

Standard library only.  Run:
  (ulimit -v 6000000; timeout 1800 uv run --offline --no-project python scripts/z74_xrev_jointpid_checks.py)

Checks (none of them is a proof of the model theorem; they recompute the finite inputs the argument quotes):
 A. ET Prop 1.6 regression: no strict Type I / Type II ES solution at odd squares n=t^2, 3<=t<=T.
 B. Jacobi sign of strict solutions at odd non-squares (LOGIC_SPLIT_SQUARE_TEST): (-g/n) = -1, g = sf(XY).
 C. The point check (636, 69748, 131876031) at p = 2521.
 D. F_q fibre counts: x^2+y^2=b (b!=0) has q - chi(-1) points; sum of 4 squares = t has q^3-q points
    for t!=0 and q^3+q^2-q-1 nonzero points for t=0.
 E. 2-adic lifting recipes: unit s=1 mod 4, free even y chosen 0 mod 4 (s=1 mod 8) or 2 mod 4 (s=5 mod 8)
    leaves s-y^2 = 1 mod 8 (a 2-adic square); every residue mod 2^k is a sum of 4 squares mod 2^k.
 F. The polynomial obstruction argument, replayed on random-free data: G_i = 3T/4 identity is integral only
    on the non-primitive class 0 mod 4, and the CRT step (odd t, t^2 = r mod M) exists for unit squares r.
"""
from math import gcd, isqrt
import sys


def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def merge(*fs):
    out = {}
    for f in fs:
        for p, e in f.items():
            out[p] = out.get(p, 0) + e
    return out


def divisors_upto(fac, bound):
    divs = [1]
    for p, e in fac.items():
        new = []
        for d in divs:
            pk = 1
            for _ in range(e + 1):
                if d * pk > bound:
                    break
                new.append(d * pk)
                pk *= p
        divs = new
    return divs


def es_solutions(n):
    """All x<=y<=z positive with 4/n = 1/x+1/y+1/z."""
    sols = []
    fn = factor(n)
    for x in range(n // 4 + 1, (3 * n) // 4 + 1):
        a = 4 * x - n
        b = n * x
        g = gcd(a, b)
        a //= g
        b //= g
        # factor b
        fb = merge(fn, factor(x))
        fg = factor(g)
        for p, e in fg.items():
            fb[p] -= e
            if fb[p] == 0:
                del fb[p]
        fb2 = {p: 2 * e for p, e in fb.items()}
        for d in divisors_upto(fb2, b):
            if (d + b) % a:
                continue
            y = (d + b) // a
            e2 = b * b // d
            if (e2 + b) % a:
                continue
            z = (e2 + b) // a
            if y < x or z < y:
                continue
            assert 4 * x * y * z == n * (x * y + y * z + z * x)
            sols.append((x, y, z))
    return sols


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


def strict_type(n, t):
    div = [v % n == 0 for v in t]
    cop = [gcd(v, n) == 1 for v in t]
    k = sum(div)
    if k == 1 and all(cop[i] for i in range(3) if not div[i]):
        return "I"
    if k == 2 and all(cop[i] for i in range(3) if not div[i]):
        return "II"
    return None


def sqfree(m):
    s = 1
    for p, e in factor(m).items():
        if e % 2:
            s *= p
    return s


def check_A(T):
    tot = 0
    nonstrict = 0
    for t in range(3, T + 1, 2):
        n = t * t
        sols = es_solutions(n)
        tot += len(sols)
        for s in sols:
            ty = strict_type(n, s)
            if ty is not None:
                print("A FAIL strict solution at odd square", n, s, ty)
                return False
            nonstrict += 1
    print(f"A ok: odd squares t=3..{T}: {tot} ES triples, all non-strict (no Type I/II)")
    return True


def check_B(N):
    cnt = 0
    for n in range(3, N, 2):
        if isqrt(n) ** 2 == n:
            continue
        for s in es_solutions(n):
            ty = strict_type(n, s)
            if ty is None:
                continue
            # remove one denominator divisible by n (type I) or coprime (type II): the other two are X,Y
            if ty == "I":
                i = [v % n == 0 for v in s].index(True)
            else:
                i = [v % n == 0 for v in s].index(False)
            X, Y = [s[j] for j in range(3) if j != i]
            g = sqfree(X * Y)
            if jacobi(-g, n) != -1:
                print("B FAIL", n, s, ty, g)
                return False
            cnt += 1
    print(f"B ok: {cnt} strict Type I/II triples at odd non-squares n<{N}, all with (-g/n)=-1")
    return True


def check_C():
    p = 2521
    x, y, z = 636, 69748, 131876031
    assert 4 * x * y * z == p * (x * y + y * z + z * x)
    # drop x (the unique multiple of p?)
    print("C: divisibility by p:", [v % p == 0 for v in (x, y, z)])
    # reduce (4x-p)/(p x) = d/w for the other two
    for i, v in enumerate((x, y, z)):
        num, den = 4 * v - p, p * v
        g0 = gcd(num, den)
        d, w = num // g0, den // g0
        others = [u for j, u in enumerate((x, y, z)) if j != i]
        g = sqfree(others[0] * others[1])
        if g == 987 or w == 52311:
            print(f"C: removing {v}: d={d}, w={w}, g={g}, (-g)^((p-1)/2) mod p = {pow(-g % p, (p - 1) // 2, p)}")
    return True


def check_D(qs):
    for q in qs:
        sq = [0] * q
        for a in range(q):
            sq[a * a % q] += 1
        chi = 1 if q % 4 == 1 else -1
        two = [0] * q
        for u in range(q):
            for v in range(q):
                two[(u * u + v * v) % q] += 1
        assert all(two[b] == q - chi for b in range(1, q)), q
        four = [0] * q
        for b1 in range(q):
            for b2 in range(q):
                four[(b1 + b2) % q] += two[b1] * two[b2]
        assert all(four[t] == q ** 3 - q for t in range(1, q)), q
        assert four[0] - 1 == q ** 3 + q ** 2 - q - 1, q
    print(f"D ok: two- and four-square fibre counts at q in {qs}")
    return True


def check_E(K):
    M = 1 << K
    sqs = {(y * y) % M for y in range(M)}
    for s in range(1, M, 4):
        ys = range(0, M, 4) if s % 8 == 1 else range(2, M, 4)
        for y in ys:
            assert (s - y * y) % 8 == 1
        # 1 mod 8 units are squares mod 2^K
        assert (s - (0 if s % 8 == 1 else 4)) % M in sqs
    four = set()
    sl = sorted(sqs)
    two = {(a + b) % M for a in sl for b in sl}
    four = {(a + b) % M for a in two for b in two}
    assert len(four) == M
    print(f"E ok: 2-adic recipes mod 2^{K}")
    return True


def check_F():
    # 3T/4 three times: 4/T = 3*(4/(3T)); integral iff T = 0 mod 4 (non-primitive)
    ok = all(((3 * n) % 4 == 0) == (n % 4 == 0) for n in range(1, 200))
    # CRT step: for M=840 and each unit square r mod 840, odd t with t^2=r mod 840 exists
    M = 840
    units = [r for r in range(M) if gcd(r, M) == 1]
    squares = {t * t % M for t in units}
    assert all(any(t * t % M == r and t % 2 == 1 for t in range(M)) for r in squares)
    print(f"F ok: 3T/4 integral only on 0 mod 4: {ok}; unit squares mod 840 = {sorted(squares)}")
    return ok


if __name__ == "__main__":
    T = int(sys.argv[1]) if len(sys.argv) > 1 else 61
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    res = [check_A(T), check_B(N), check_C(), check_D([3, 5, 7, 11, 13, 17, 19, 23]), check_E(12), check_F()]
    print("ALL OK" if all(res) else "SOME FAILED")
