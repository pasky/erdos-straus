"""z67 K11: probe two-prime profiles with RATIONAL components (g at 11, h at 13, 1 elsewhere), EVIDENCE only.

Builds the cylinder list of z66_ucover_kbrute.py (all seven families, modulus <= MMAX, rigid r = 1 mod m') plus the
exact two-prime A/E/F events of z66_ucover_levels2.c (levels k <= K, j <= J), then reports which small-height
rationals g = u/v (non-residue mod 11) and h = s/t (mod 13) are caught by none of them.
Usage: uv run --with sympy python scripts/z67_k11_ratprobe.py MMAX K J HMAX
"""
import subprocess
import sys
from math import gcd

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import z66_ucover_kbrute as kb  # noqa: E402


def cylinders(MMAX, K, J):
    cyl = set()
    # reuse the brute force by monkeypatching argv and capturing the set: re-implement call
    import builtins
    src = open(kb.__file__).read()
    ns = {}
    exec(compile(src.replace("if __name__ == \"__main__\":\n    main()", ""), kb.__file__, "exec"), ns)
    return ns


def main():
    MMAX, K, J, HMAX = map(int, sys.argv[1:5])
    from sympy import divisors
    from sympy.ntheory.residue_ntheory import sqrt_mod
    cyl = set()

    def test(r, m):
        r %= m
        if gcd(r, m) != 1:
            return
        k, j, mp = kb.split(m)
        if k + j == 0 or r % mp != 1 % mp or k > K or j > J:
            return
        cyl.add((k, j, r % 11 ** k, r % 13 ** j))
    rel = lambda m: m % 11 == 0 or m % 13 == 0
    for a in range(1, MMAX // 4 + 1):
        for d in range(1, MMAX // (4 * a) + 1):
            m = 4 * a * d
            if rel(m):
                for f in divisors(4 * a * a * d + 1):
                    test(-f, m)
    for a in range(1, MMAX // 4 + 1):
        for c in range(1, MMAX // (4 * a) + 1):
            M1 = 4 * a * c
            for f in range(2, MMAX // M1 + 1):
                m = M1 * f
                if not rel(m) or gcd(M1, f) != 1:
                    continue
                r2 = (-c * pow(a, -1, f)) % f
                test(-f + M1 * (((r2 + f) * pow(M1, -1, f)) % f), m)
                for x in sqrt_mod((-4 * a * a * c) % f, f, all_roots=True) or []:
                    test(-f + M1 * (((x + f) * pow(M1, -1, f)) % f), m)
    for a in range(1, MMAX // 4 + 1):
        for b in range(1, MMAX // (4 * a) + 1):
            m = 4 * a * b
            if not rel(m):
                continue
            for e in divisors(a + b):
                if gcd(e, m) == 1:
                    test(-pow(e, -1, m), m)
                    test(-e, m)
    for f in range(3, MMAX + 1, 4):
        if not rel(f):
            continue
        P = (f + 1) // 4
        for a in divisors(P):
            for d in divisors(P // a):
                test(-4 * a * a * d, f)
    for a in range(1, MMAX // 4 + 1):
        for d in range(1, MMAX // (4 * a) + 1):
            for e in range(1, MMAX // (4 * a * d) + 1):
                m = 4 * a * d * e
                if rel(m) and gcd(4 * a * d, e) == 1:
                    test(-4 * a * a * d - e, m)
    nb = len(cyl)
    for k in range(K + 1):
        for j in range(J + 1):
            if k + j == 0:
                continue
            r = subprocess.run(["/tmp/zlev2", "11", str(k), "13", str(j), "1000000000"],
                               capture_output=True, text=True, check=True)
            for line in r.stdout.splitlines():
                t = line.split()
                cyl.add((k, j, int(t[1]), int(t[2])))
    print(f"# MMAX={MMAX} K={K} J={J}: {nb} brute cylinders, {len(cyl)} total")
    rats = set()
    for u in range(-HMAX, HMAX + 1):
        for v in range(1, HMAX + 1):
            if u and gcd(u, v) == 1:
                rats.add((u, v))
    def val(u, v, M):
        return (u * pow(v, -1, M)) % M if v % (11 if M % 11 == 0 else 13) else None
    G = [(u, v) for (u, v) in rats if u % 11 and v % 11 and pow((u * pow(v, -1, 11)) % 11, 5, 11) == 10]
    H = [(u, v) for (u, v) in rats if u % 13 and v % 13]
    surv = []
    for (u, v) in G:
        gk = [(u * pow(v, -1, 11 ** k)) % 11 ** k for k in range(K + 1)]
        for (s, t) in H:
            hj = [(s * pow(t, -1, 13 ** j)) % 13 ** j for j in range(J + 1)]
            if not any((k, j, gk[k], hj[j]) in cyl for k in range(K + 1) for j in range(J + 1) if k + j):
                surv.append(((u, v), (s, t)))
    print(f"# {len(G)} g-candidates x {len(H)} h-candidates; survivors {len(surv)}")
    surv.sort(key=lambda x: max(abs(x[0][0]), x[0][1]) + max(abs(x[1][0]), x[1][1]))
    for x in surv[:60]:
        print(f"g={x[0][0]}/{x[0][1]} h={x[1][0]}/{x[1][1]}")


if __name__ == "__main__":
    main()
