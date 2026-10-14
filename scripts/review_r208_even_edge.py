"""R208 from-scratch check of FRIEZE_ES Lemma 1.1 / Thm 1.2 / transport law (§2).

Independent of scripts/y2_*. Enumerates every positive formal word (c,m,s), letters >= 1,
N = mcs - c - s odd, 0 < N <= X, and checks:
  (P) the five Ptolemy relations;
  L1: exactly two of (h', c, m, s, h) even, cyclically adjacent;
  T:  (h'/N) = (-1/N) * (-1)^[8 | e e'];
  TR: transport law: (h'/N) = -(-1/N)(2/o) if edge in {c,m},{m,s}; -(-2/N)(2/o) otherwise,
      o = vertex opposite the even edge (index i+3 when edge = (i, i+1)).
Usage: review_r208_even_edge.py X [nrandom] [maxletter_random]
"""
import sys, random
from collections import Counter


def jac(a, n):
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


def check(c, m, s, stats):
    N = m * c * s - c - s
    h, hp = c * m - 1, m * s - 1
    q = (hp, c, m, s, h)
    assert hp * c == N + s and c * m == 1 + h and m * s == 1 + hp
    assert s * h == N + c and h * hp == 1 + N * m
    ev = [i for i in range(5) if q[i] % 2 == 0]
    if len(ev) != 2 or (ev[1] - ev[0]) % 5 not in (1, 4):
        return "L1"
    i = ev[0] if (ev[1] - ev[0]) % 5 == 1 else ev[1]  # edge (i, i+1)
    e, ep = q[i], q[(i + 1) % 5]
    J = jac(hp, N)
    pred = jac(-1, N) * (-1 if (e * ep) % 8 == 0 else 1)
    if J != pred:
        return "T"
    o = q[(i + 3) % 5]
    assert o % 2 == 1
    if (i, (i + 1) % 5) in ((1, 2), (2, 3)):
        tr = -jac(-1, N) * jac(2, o)
    else:
        tr = -jac(-2, N) * jac(2, o)
    if J != tr:
        return "TR"
    stats[(i, (i + 1) % 5)] += 1
    if N % 8 == 1 and J != -jac(2, o):
        return "TR8"
    r = int(N ** 0.5)
    while r * r > N:
        r -= 1
    while (r + 1) ** 2 <= N:
        r += 1
    if r * r == N:
        stats["sq"] += 1
        if (e * ep) % 8 != 4:
            return "SQ"
    return None


def main():
    X = int(sys.argv[1])
    nr = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    L = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 4
    stats, fails, n = Counter(), Counter(), 0
    for m in range(1, X + 3):
        c = 1
        any_c = False
        while True:
            d = m * c - 1
            if d <= 0:
                c += 1
                continue
            smin = c // d + 1
            smax = (X + c) // d
            if smin > smax:
                if any_c or c > X + 3:
                    break
                c += 1
                continue
            any_c = True
            for s in range(smin, smax + 1):
                N = m * c * s - c - s
                if N % 2 == 0:
                    continue
                n += 1
                f = check(c, m, s, stats)
                if f:
                    fails[f] += 1
                    if fails[f] <= 3:
                        print("FAIL", f, (c, m, s), N)
            c += 1
        if not any_c:
            break
    print("X", X, "odd-N formal words", n, "positions", dict(stats), "fails", dict(fails))
    rng = random.Random(208)
    nn, rf = 0, Counter()
    rs = Counter()
    while nn < nr:
        c, m, s = (rng.randint(1, L) for _ in range(3))
        N = m * c * s - c - s
        if N <= 0 or N % 2 == 0:
            continue
        nn += 1
        f = check(c, m, s, rs)
        if f:
            rf[f] += 1
    if nr:
        print("random", nr, "letters<=", L, "positions", dict(rs), "fails", dict(rf))


if __name__ == "__main__":
    main()
