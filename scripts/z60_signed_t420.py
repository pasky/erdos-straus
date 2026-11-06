#!/usr/bin/env python3
"""z60 SIGNED: prime-only validity screen of the two L = 420 survivor lines at the 9 in-M (*)-zero primes.
Line 1: (420, chi_21), G = E210 (x) chi_{-84};  line 2: (420, chi_105), G = E105 (x) chi_{-420} (WALDS Sec. 5.2).
On C1 the survivor coefficient s(p) vanishes iff L(G (x) chi_p, 1/2) = 0 (Waldspurger Cor. 2, non-zero anchor).
For each zero prime p: conductor, root number, ellrank bounds of G (x) chi_p (rank >= 2 => L = 0 unconditionally by
Gross-Zagier-Kolyvagin); and, if the conductor is small enough, the numerical analytic rank (pari ellanalyticrank).
Usage: uv run --with cypari2 python scripts/z60_signed_t420.py [maxcond_for_analytic]
"""
import sys, time
import cypari2
pari = cypari2.Pari(); pari.allocatemem(1_500_000_000)
MAXC = float(sys.argv[1]) if len(sys.argv) > 1 else 5e13
lines = [("chi21", pari.ellinit([0, -1, 0, -56, -84]), -84), ("chi105", pari.ellinit([0, 1, 0, -120, -432]), -420)]
for p in [5569, 9601, 83449, 102001, 712321, 1724209, 1726201, 5212561, 8813281]:
    for name, E, D in lines:
        t0 = time.time()
        T = pari.ellinit(pari.elltwist(E, D * p))
        N = pari.ellglobalred(T)[0]
        r = pari.ellrank(T)
        an = ""
        if float(N) <= MAXC:
            ar = pari.ellanalyticrank(T)
            an = f" analytic rank {ar[0]} (L^(r)/r! = {pari.precision(ar[1], 10)})"
        print(f"p={p} {name}: cond={N} rootno={pari.ellrootno(T)} ellrank=[{r[0]},{r[1]}]{an}  ({time.time()-t0:.0f}s)", flush=True)
