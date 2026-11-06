#!/usr/bin/env python3
"""z60 SIGNED: ellrank bounds (2-descent, several efforts/tries) of the L = 420 survivor twists G (x) chi_p at given primes.
Line chi21: E = [0,-1,0,-56,-84] twisted by -84p; line chi105: E = [0,1,0,-120,-432] twisted by -420p.
lo >= 2 proves L(G (x) chi_p, 1/2) = 0 (GZK); hi = 0 proves algebraic rank 0.
Usage: uv run --with cypari2 python scripts/z60_signed_zeros_rank.py p1,p2,... [maxeffort]
"""
import sys, time
import cypari2
pari = cypari2.Pari(); pari.allocatemem(1_000_000_000)
PS = [int(x) for x in sys.argv[1].split(",")]
MAXE = int(sys.argv[2]) if len(sys.argv) > 2 else 3
lines = [("chi21", pari.ellinit([0, -1, 0, -56, -84]), -84), ("chi105", pari.ellinit([0, 1, 0, -120, -432]), -420)]
for p in PS:
    for name, E, D in lines:
        t0 = time.time()
        T = pari.ellinit(pari.elltwist(E, D * p))
        best = None
        for eff in range(0, MAXE + 1):
            r = pari.ellrank(T, eff)
            lo, hi = int(r[0]), int(r[1])
            if best is None or lo > best[0] or hi < best[1]:
                best = (max(lo, best[0]) if best else lo, min(hi, best[1]) if best else hi)
            if best[0] == best[1]:
                break
        print(f"p={p} mod840={p%840} {name}: ellrank bounds [{best[0]},{best[1]}] ({time.time()-t0:.0f}s)", flush=True)
