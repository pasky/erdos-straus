#!/usr/bin/env python3
"""z60 SIGNED: base rate of rank >= 2 for the L = 420 survivor twists at Mordell-class primes near X.
For the first `count` primes p >= X with p mod 840 in M, compute pari ellrank bounds [lo, hi] for G (x) chi_p where
G (x) chi_p = E (x) chi_{D p}: line chi21: E = [0,-1,0,-56,-84], D = -84; line chi105: E = [0,1,0,-120,-432], D = -420.
lo >= 2 proves L(G (x) chi_p, 1/2) = 0 (Gross-Zagier-Kolyvagin); hi = 0 gives algebraic rank 0 (L != 0 expected, BSD).
Also prints R(p) = 0 / > 0 via a direct (*) search (early exit).
Usage: uv run --with cypari2 python scripts/z60_signed_baserate.py X count line [effort]
"""
import sys, time
import cypari2
pari = cypari2.Pari(); pari.allocatemem(1_000_000_000)
X, CNT, LINE = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
EFF = int(sys.argv[4]) if len(sys.argv) > 4 else 1
E, D = {"chi21": ([0, -1, 0, -56, -84], -84), "chi105": ([0, 1, 0, -120, -432], -420)}[LINE]
E = pari.ellinit(E)
M = {1, 121, 169, 289, 361, 529}


def R_pos(p):
    # (*) hit: some C >= 1 and divisor d of 4Cp+1 with d = -1 mod 4C, 3 <= d <= sqrt(4Cp+1) suffices (pairs d, e)
    C = 1
    while (4 * C - 1) ** 2 <= 4 * C * p + 1:
        n = 4 * C * p + 1
        d = 4 * C - 1
        while d * d <= n:
            if n % d == 0 and (n // d) % (4 * C) == 4 * C - 1:
                return True
            d += 4 * C
        C += 1
    return False


p = X
done = 0
stats = {"lo>=2": 0, "hi=0": 0, "undecided": 0}
while done < CNT:
    p = int(pari.nextprime(p + 1))
    if p % 840 not in M:
        continue
    t0 = time.time()
    T = pari.ellinit(pari.elltwist(E, D * p))
    r = pari.ellrank(T, EFF)
    lo, hi = int(r[0]), int(r[1])
    key = "lo>=2" if lo >= 2 else ("hi=0" if hi == 0 else "undecided")
    stats[key] += 1
    print(f"p={p} R>0={R_pos(p)} ellrank=[{lo},{hi}] ({time.time()-t0:.0f}s)", flush=True)
    done += 1
print(f"# X={X} line={LINE} count={CNT}: {stats}")
