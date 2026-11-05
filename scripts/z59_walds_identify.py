#!/usr/bin/env python3
"""z59 WALDS: Gauss-exceptional test for the RATIONAL weight-2 newforms phi of level M | 2N (via elliptic curves).
Collects elliptic curves with conductor dividing MAXM from a box of Weierstrass coefficients (S-unit discriminant
prefilter), one per a_p-system (isogeny class), and for each listed D' (= discriminant of psi*chi_{-4}) computes
G = E (x) chi_{D'}: conductor, root number, numerical analytic rank (pari ellanalyticrank) and pari ellrank [lo, hi]
(lo >= 2 is a rigorous rank lower bound, so L(G,1) = 0 by Gross-Zagier-Kolyvagin). Prints the a_p (p = 3..23) of E
so the survivors' implied Shimura eigenvalues (scripts/z59_walds_diag.py) can be matched.
Usage: uv run --with cypari2 python scripts/z59_walds_identify.py MAXM "D'1,D'2,..." [A4 A6]
"""
import sys, itertools
import cypari2

pari = cypari2.Pari()
pari.allocatemem(1_500_000_000)
MAXM = int(sys.argv[1])
Ds = [int(x) for x in sys.argv[2].split(",")]
A4 = int(sys.argv[3]) if len(sys.argv) > 3 else 300
A6 = int(sys.argv[4]) if len(sys.argv) > 4 else 3000
PR = [3, 5, 7, 11, 13, 17, 19, 23]


def sunit(n):
    n = abs(n)
    if n == 0:
        return False
    for p in (2, 3, 5, 7):
        while n % p == 0:
            n //= p
    return n == 1


classes = {}
for a1, a2, a3 in itertools.product((0, 1), (-1, 0, 1), (0, 1)):
    b2 = a1 * a1 + 4 * a2
    for a4 in range(-A4, A4 + 1):
        b4 = 2 * a4 + a1 * a3
        for a6 in range(-A6, A6 + 1):
            b6 = a3 * a3 + 4 * a6
            b8 = a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4
            disc = -b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 * b6 + 9 * b2 * b4 * b6
            if not sunit(disc):
                continue
            E = pari.ellinit([a1, a2, a3, a4, a6])
            NE = int(pari.ellglobalred(E)[0])
            if MAXM % NE:
                continue
            key = (NE, tuple(int(pari.ellap(E, p)) for p in PR))
            if key not in classes:
                classes[key] = [a1, a2, a3, a4, a6]
print(f"# {len(classes)} isogeny classes with conductor | {MAXM} found in box |a4|<={A4}, |a6|<={A6}")
for (NE, aps), ai in sorted(classes.items()):
    E = pari.ellinit(ai)
    out = []
    for D in Ds:
        Et = pari.elltwist(E, D)
        w = int(pari.ellrootno(Et))
        r = int(pari.ellanalyticrank(Et)[0])
        lo, hi = (int(x) for x in pari.ellrank(Et)[:2])
        flag = "*" if (w == -1 or r >= 2) else ""
        out.append(f"{D}:{w:+d}/r{r}/[{lo},{hi}]{flag}")
    print(f"N={NE} a={ai} ap(3..23)={list(aps)} | " + " ".join(out), flush=True)
