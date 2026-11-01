"""z53_hyp2cycle_brute.py — independent O(U^2) brute force for z53_hyp2cycle_scan.c (columns N2 N4 N5 Nbi Nodd Nk2 N3cyc Ndef).
usage: uv run --with sympy python scripts/z53_hyp2cycle_brute.py <scan-binary>
Checks all odd n in [5, 30000] with U = floor(n^(1/4)) and with U in {7, 12, 20} (when 2U < n)."""
import subprocess, sys
from sympy import jacobi_symbol
from math import isqrt

def root4(n):
    r = isqrt(isqrt(n))
    while (r + 1) ** 4 <= n: r += 1
    while r ** 4 > n: r -= 1
    return r

def brute(n, U):
    box = range(U + 1, 2 * U + 1)
    N2 = N4 = N5 = Nbi = Nodd = Nk2 = 0
    for u in box:
        for B in box:
            if B <= u: continue
            if (n + u + B) % (u * B): continue
            k = (n + u + B) // (u * B)
            N2 += 1
            s4 = k % 4 == 0
            N4 += s4
            N5 += s4 or u % 4 == 0 or B % 4 == 0 or (k * u - 1) % 4 == 0 or (k * B - 1) % 4 == 0
            Nodd += (u + B) % 2
            Nk2 += k % 4 == 2
            ju, jb = jacobi_symbol(u, n), jacobi_symbol(B, n)
            Nbi += (ju != 0 and jb != 0 and ju != jb)
    # f by direct search
    f = {}
    for x in box:
        ys = [y for y in box if (y + n) % x == 0]
        assert len(ys) <= 1
        if ys: f[x] = ys[0]
    N3 = 0
    for x in box:
        y = f.get(x); z = f.get(y) if y else None; w = f.get(z) if z else None
        if w == x and len({x, y, z}) == 3 and x < y and x < z: N3 += 1
    return [N2, N4, N5, Nbi, Nodd, Nk2, N3, len(f)]

def main():
    binary = sys.argv[1]
    cases = []
    for n in range(5, 30001, 2):
        cases.append((n, 0))
        for U in (7, 12, 20):
            if 2 * U < n: cases.append((n, U))
    bad = 0
    for Ufix in (0, 7, 12, 20):
        ns = [n for (n, U) in cases if U == Ufix]
        out = subprocess.run([binary, str(Ufix)], input="\n".join(map(str, ns)) + "\n", capture_output=True, text=True).stdout.split("\n")
        rows = {int(l.split()[0]): list(map(int, l.split()[1:])) for l in out if l.strip()}
        for n in ns:
            U = Ufix or root4(n)
            if 2 * U >= n: continue
            exp = brute(n, U)
            got = rows[n][1:]
            if rows[n][0] != U or got != exp:
                bad += 1
                if bad < 10: print("MISMATCH", n, U, got, exp)
    print("cases", len(cases), "mismatches", bad)

main()
