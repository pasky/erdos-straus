"""review_ff3_cross.py (R173): (1) fast vs brute-force (full factorisation of D) family sets at random slice points;
(2) Lemma 2.1 / 3.1 inequalities on every family found; (3) Lemma 2.3 window N <= 4l - 1 at x*_c for p = 3, 5, 7
with the j-range extended BEYOND the window (j <= JX), so a violation would be seen.
usage: review_ff3_cross.py part   (part = 1, 2 or 3)"""
import random
import sys
import review_ff3_search as S


def lemma_checks(fams, k, tag):
    bad = 0
    keys = {(f[1], f[2], f[3], f[4], f[5]) for f in fams}
    for (l, L, j, gam, g, E) in fams:
        N = k + j - 1
        if not (l <= N + gam - 2 and N + gam >= 3 and l <= 2 * N - k - 1):
            print(f"  VIOLATION Lemma 2.1 {tag}: l={l} j={j} gam={gam}")
            bad += 1
        if gam <= j - 2 and (L, j - 1, gam + 1, g, E) not in keys:
            print(f"  VIOLATION Lemma 3.1 {tag}: l={l} j={j} gam={gam}")
            bad += 1
    return bad


def planted(rng, p, k, lmax, jmax):
    """a random slice point u lying in the cylinder of some Case B family (found by factoring D)."""
    F = S.F
    F.setp(p)
    while True:
        l = rng.randrange(0, lmax + 1)
        L = [rng.randrange(p) for _ in range(l)] + [1]
        if L[0] == 0:
            continue
        j = rng.randrange(0, jmax + 1)
        gam = rng.randrange(0, j + 1)
        g = rng.choice(F.divisors(L))
        N = k + j - 1
        D = F.add([1], F.mul(F.Tpow(N + 1 + gam), F.mul(L, g)))
        Es = [E for E in F.divisors(D) if len(E) >= 2 and E[0] == p - 1 and (l == 0 or not F.mod(F.add(E, [1]), L))]
        Es = [E for E in Es if len(E) >= 2 and (E + [0] * 3)[1] != 0]  # c = -E_1 != 0
        if Es:
            E = rng.choice(Es)
            u = [(-x) % p for x in (E + [0] * (N + 1))[:N + 1]]
            return u + [rng.randrange(p) for _ in range(60)]


def part1():
    rng = random.Random(173)
    tot = 0
    for p, k, lmax, jmax, npts in ((3, 2, 3, 5, 8), (3, 3, 2, 5, 4), (5, 2, 2, 4, 4), (7, 2, 1, 4, 3)):
        for _ in range(npts):
            u = planted(rng, p, k, lmax, jmax)
            fa = S.search(p, k, 0, lmax, jmax, u, log=lambda s: None)
            fb = S.search(p, k, 0, lmax, jmax, u, log=lambda s: None, brute=True)
            tot += len(fa)
            print(f"p={p} k={k} l<={lmax} j<={jmax} u={u[:6]}...: fast {len(fa)} brute {len(fb)} equal={fa == fb}",
                  flush=True)
            assert fa == fb
            lemma_checks(fa, k, f"p={p}")
    print("part1 total families", tot)


def part2():
    # Lemma 2.1 / 3.1 on many families at random slice points (fast search only), larger ranges
    rng = random.Random(1730)
    nf = 0
    bad = 0
    for p, k, lmax, jmax, npts in ((3, 2, 6, 12, 30), (3, 3, 5, 10, 10), (5, 2, 3, 8, 10)):
        for _ in range(npts):
            c = rng.randrange(1, p)
            u = [1, c] + [rng.randrange(p) for _ in range(80)]
            fa = S.search(p, k, 0, lmax, jmax, u, log=lambda s: None)
            nf += len(fa)
            bad += lemma_checks(fa, k, f"p={p} u={u[:8]}")
        print(f"p={p} k={k}: cumulative families {nf}, violations {bad}", flush=True)


def part3():
    for p, k, lmax, extra in ((3, 2, 5, 8), (5, 2, 3, 8), (7, 2, 3, 6), (5, 3, 3, 6), (7, 3, 2, 6)):
        for c in range(1, p):
            fams = set()
            for l in range(0, lmax + 1):
                fams |= S.search(p, k, l, l, 4 * l - k + extra if 4 * l - k + extra >= 0 else 0, [1, c],
                                 log=lambda s: None)
            viol = [f for f in fams if k + f[2] - 1 > 4 * f[0] - 1]
            mx = max(((k + f[2] - 1) - (4 * f[0] - 1) for f in fams), default=None)
            print(f"x*: p={p} k={k} c={c} l<={lmax} j<=4l-k+{extra}: families {len(fams)}, "
                  f"window violations {len(viol)}, max(N-(4l-1))={mx}", flush=True)
            lemma_checks(fams, k, f"x* p={p} c={c}")
            for f in sorted(fams)[:3]:
                print("   e.g.", f)


if __name__ == "__main__":
    {"1": part1, "2": part2, "3": part3}[sys.argv[1]]()
