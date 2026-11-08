"""z66 UCOVER: literal two-prime brute force for the K-question (all seven ET families; EVIDENCE only).

Profile pi = (g at 11, h at 13, 1 at all other primes).  Enumerates every ET Prop 1.9 family class with modulus
m <= MMAX and 11*13 | ... (11 | m or 13 | m), keeps those with r = 1 mod m' (m' = part of m prime to 143), and
records the cylinder (k, j, r mod 11^k, r mod 13^j).  Then intersects the K-box (g non-residue mod 11) at level
(11^K, 13^J) with the complement of all recorded cylinders (k <= K, j <= J), optionally also using the exact A/E/F
events of z66_ucover_levels2.c.  Survivor counts are UPPER bounds (classes with modulus > MMAX are not seen).
Usage: uv run --with sympy python scripts/z66_ucover_kbrute.py MMAX K J [use_levels2(0/1)]
"""
import subprocess
import sys
from math import gcd

from sympy import divisors
from sympy.ntheory.residue_ntheory import sqrt_mod


def split(m):
    k = j = 0
    while m % 11 == 0:
        m //= 11
        k += 1
    while m % 13 == 0:
        m //= 13
        j += 1
    return k, j, m


def main():
    MMAX, K, J = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    use2 = len(sys.argv) > 4 and sys.argv[4] == "1"
    cyl = set()

    def test(r, m):
        r %= m
        if gcd(r, m) != 1:
            return
        k, j, mp = split(m)
        if k + j == 0 or r % mp != 1 % mp:
            return
        if k > K or j > J:
            return
        cyl.add((k, j, r % 11 ** k, r % 13 ** j))

    rel = lambda m: m % 11 == 0 or m % 13 == 0
    for a in range(1, MMAX // 4 + 1):                       # I-1
        for d in range(1, MMAX // (4 * a) + 1):
            m = 4 * a * d
            if rel(m):
                for f in divisors(4 * a * a * d + 1):
                    test(-f, m)
    for a in range(1, MMAX // 4 + 1):                       # I-2
        for c in range(1, MMAX // (4 * a) + 1):
            M1 = 4 * a * c
            for f in range(1, MMAX // M1 + 1):
                m = M1 * f
                if not rel(m) or gcd(M1, f) != 1:
                    continue
                if f == 1:
                    test(-1, m)
                    continue
                r2 = (-c * pow(a, -1, f)) % f
                test(-f + M1 * (((r2 + f) * pow(M1, -1, f)) % f), m)
    for c in range(1, MMAX // 4 + 1):                       # I-3
        for d in range(1, MMAX // (4 * c) + 1):
            M1 = 4 * c * d
            for f in range(1, MMAX // M1 + 1):
                m = M1 * f
                if not rel(m) or gcd(M1, f) != 1:
                    continue
                if f == 1:
                    test(-1, m)
                    continue
                for x in sqrt_mod((-4 * c * c * d) % f, f, all_roots=True) or []:
                    test(-f + M1 * (((x + f) * pow(M1, -1, f)) % f), m)
    for a in range(1, MMAX // 4 + 1):                       # I-4, II-1
        for b in range(1, MMAX // (4 * a) + 1):
            m = 4 * a * b
            if not rel(m):
                continue
            for e in divisors(a + b):
                if gcd(e, m) == 1:
                    test(-pow(e, -1, m), m)
                    test(-e, m)
    for f in range(3, MMAX + 1, 4):                         # II-2
        if not rel(f):
            continue
        P = (f + 1) // 4
        for a in divisors(P):
            for d in divisors(P // a):
                test(-4 * a * a * d, f)
    for a in range(1, MMAX // 4 + 1):                       # II-3
        for d in range(1, MMAX // (4 * a) + 1):
            for e in range(1, MMAX // (4 * a * d) + 1):
                m = 4 * a * d * e
                if rel(m) and gcd(4 * a * d, e) == 1:
                    test(-4 * a * a * d - e, m)
    nb = len(cyl)
    if use2:
        for k in range(K + 1):
            for j in range(J + 1):
                if k + j == 0:
                    continue
                r = subprocess.run(["/tmp/zlev2", "11", str(k), "13", str(j), "1000000000"],
                                   capture_output=True, text=True, check=True)
                for line in r.stdout.splitlines():
                    t = line.split()
                    cyl.add((k, j, int(t[1]), int(t[2])))
    print(f"# MMAX={MMAX}: {nb} brute cylinders, {len(cyl)} with levels2 events")
    alive = [(g, h) for g in range(11 ** K) if g % 11 and pow(g % 11, 5, 11) == 10 for h in range(13 ** J) if h % 13]
    tot = len(alive)
    for k in range(K + 1):
        for j in range(J + 1):
            if k + j == 0:
                continue
            cs = set((c[2], c[3]) for c in cyl if c[0] == k and c[1] == j)
            alive = [(g, h) for g, h in alive if (g % 11 ** k, h % 13 ** j) not in cs]
    byg = {}
    for g, h in alive:
        byg.setdefault(g % 11, set()).add(h % 13)
    print(f"survivors at (11^{K},13^{J}): {len(alive)}/{tot};  by (g mod 11 -> h mod 13): "
          f"{ {g: sorted(v) for g, v in sorted(byg.items())} }")


if __name__ == "__main__":
    main()
