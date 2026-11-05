#!/usr/bin/env python3
"""z59 WALDS: independent cross-check of section 6.1 for the survivor at (L, psi) = (168, chi_168).
phi = the conductor-84 curve E: y^2 = x^3 - x^2 - 36x - 72; G = E (x) chi_{-168}; G (x) chi_p = E (x) chi_{-168p}.
For primes p where the exact half-integral survivor coefficient vanishes (resp. not), compute pari ellrank [lo, hi]
(lo >= 2 rigorous => L(G (x) chi_p, 1) = 0 by Gross-Zagier-Kolyvagin) and the numerical analytic rank.
Usage: uv run --with cypari2 python scripts/z59_walds_crosscheck.py
"""
import cypari2
pari = cypari2.Pari()
pari.allocatemem(1_500_000_000)
E = pari.ellinit([0, -1, 0, -36, -72])
vanish = [337, 457, 1009, 1129, 1201, 1297, 1801, 2473, 2713, 3217, 4057, 4201, 4729]       # survivor = 0 (diag_168_168.txt)
nonvan = [193, 673, 1033, 2017, 2137, 2377, 2521, 2689, 5569, 9601]                        # survivor != 0
for tag, ps in (("survivor=0", vanish), ("survivor!=0", nonvan)):
    for p in ps:
        Et = pari.elltwist(E, -168 * p)
        er = pari.ellrank(Et)
        ar = pari.ellanalyticrank(Et)
        print(f"{tag:12s} p={p:<6d} rootno={int(pari.ellrootno(Et)):+d} ellrank=[{int(er[0])},{int(er[1])}] an.rank={int(ar[0])} lead={float(ar[1]):.5g}", flush=True)
