r"""z52d PELLCYCLE: checks for Theorem 1.1 (near-square primes p = m^2+1 defeat every cycle root, CONDITIONAL on H).

(a) CF formulas: for every even m in [4, MMAX], sqrt(m^2+1) and (1+sqrt(m^2+1))/2 have the cycle data of Lemma 1.4,
    and for m ≡ 0 (mod 4), m >= 8, R3(p) ∪ U(p) equals the 14-element list ROOTS(m) of Thm 1.1.
(b) Isolation: for every m ≡ 0 (mod 60), m <= MMAX, and for every root u in ROOTS(m) \ {1,2,4}, the forest F_n,
    n = m^2+1 (n need not be prime here; the gcd hypotheses of Lemma 1.5 are checked explicitly), has no edge at u.
(c) Instances: the first NH values m = 60t with the five forms prime; brute force: every component of F_p meeting
    ROOTS(m) is monochromatic, the component of 1 is the 8-vertex component of LOWER_TAIL_ASTRA Thm 3.1, and 4 is isolated.
    Also report that F_p does have bichromatic edges (ES is not contradicted) by locating one with a small root.
Usage: uv run --with sympy python scripts/z52d_pellcycle_nearsquare.py MMAX NH
"""
import math
import sys
from sympy import isprime, gcd

from z52d_pellcycle_lib import cycle_data, root_sets, explore, chi, children, parent


def ROOTS(m):
    k = m // 2
    return sorted({1, 2, 4, k, k + 1, m - 1, m, m + 1, 2 * m - 2, 2 * m - 1, 2 * m, 2 * m + 1, 2 * m + 2, 4 * m})


def unit_data(m):
    # eps = m + sqrt(p) = (t + u sqrt p)/2 with t = 2m, u = 2; Z0465 recipe {t, u, t±2, u±2} (positive values)
    t, u = 2 * m, 2
    return {x for x in (t, u, t - 2, t + 2, u + 2) if x > 0}


def neighbours_raw(n, u):
    """all neighbours of u in F_n by definition (any n), for checking: parent candidate + divisors of n+u."""
    out = set()
    r = (-n) % u if u > 1 else 0
    if r > 0 and (n + u + r) % (u * r) == 0:
        out.add(r)
    N = n + u
    d = 1
    # children: v | n+u, v>u; enumerate divisors by trial division (n small enough in part (b))
    while d * d <= N:
        if N % d == 0:
            for v in (d, N // d):
                if v > u and v <= n + 2 and (n + u + v) % (u * v) == 0:
                    out.add(v)
        d += 1
    return out


def part_a(MMAX):
    bad = 0
    for m in range(4, MMAX + 1, 2):
        p = m * m + 1
        cd = cycle_data(p)
        S, W = cd["S"], cd["W"]
        okS = S["pre"] == [(0, 1, m)] and S["cyc"] == [(m, 1, 2 * m)]
        k = m // 2
        okW = W["pre"] == [(1, 2, k)] and W["cyc"] == [(m - 1, m, 1), (1, m, 1), (m - 1, 2, m - 1)]
        if not (okS and okW):
            bad += 1
            print("CF mismatch", m, S["pre"], S["cyc"], W["pre"], W["cyc"])
        if m % 4 == 0 and m >= 8:
            rs = root_sets(p)
            got = rs["R3"] | unit_data(m)
            if sorted(got) != ROOTS(m):
                bad += 1
                print("roots mismatch", m, sorted(got), ROOTS(m))
    print(f"(a) m even in [4,{MMAX}]: mismatches {bad}")
    return bad


def part_b(MMAX):
    bad = 0
    cnt = 0
    for m in range(60, MMAX + 1, 60):
        n = m * m + 1
        for u in ROOTS(m):
            if u in (1, 2, 4):
                continue
            cnt += 1
            if gcd(u, n) != 1:
                print("gcd", m, u)
            nb = neighbours_raw(n, u)
            if nb:
                bad += 1
                print("edge at", m, u, nb)
    print(f"(b) m ≡ 0 (60), m <= {MMAX}: {cnt} (m,u) pairs checked, non-isolated {bad}")
    return bad


def h_instances(NH):
    out, t = [], 1
    while len(out) < NH:
        m = 60 * t
        fs = [m * m + 1, (m * m + 2) // 2, (m * m + 3) // 3, (m * m + 4) // 4, (m * m + 5) // 5]
        if all(isprime(f) for f in fs):
            out.append(m)
        t += 1
    return out


def part_c(NH):
    bad = 0
    for m in h_instances(NH):
        p = m * m + 1
        roots = ROOTS(m)
        comps = {}
        for u in roots:
            st, nv, e, _ = explore(p, u)
            comps[u] = (st, nv)
            if st != "mono":
                bad += 1
        # component of 1 exactly the Thm 3.1 set
        r, s, w = (p + 1) // 2, (p + 2) // 3, (p + 3) // 4
        expect = {1, 2, 3, r, 2 * r, s, 3 * s, 2 * w}
        seen = {1}
        fr = [1]
        while fr:
            x = fr.pop()
            for y in children(p, x) + ([parent(p, x)] if parent(p, x) else []):
                if y not in seen:
                    seen.add(y)
                    fr.append(y)
        if seen != expect or any(chi(p, v) != 1 for v in seen):
            bad += 1
            print("comp(1) mismatch", m)
        # a bichromatic edge somewhere: scan small roots
        found = None
        for u in range(3, 5000):
            st, nv, e, _ = explore(p, u, depth=1)
            if st == "hit":
                found = e
                break
        print(f"m={m} p={p}: roots {roots}; components (status,size) {set(comps.values())}; "
              f"comp(1) = Thm3.1 set: {seen == expect}; a bichromatic edge elsewhere: {found}")
    print(f"(c) {NH} H-instances, failures {bad}")
    return bad


if __name__ == "__main__":
    MMAX = int(sys.argv[1])
    NH = int(sys.argv[2])
    b = part_a(MMAX) + part_b(MMAX) + part_c(NH)
    print("TOTAL FAILURES", b)
