# Z2769: I3 failures: n with no word tuv-u-v=n with t,u,v>=3.  Compute the failure set F up to NMAX (exact enumeration),
# then h(-4n) and h(-n) (PARI qfbclassno) and exponent-type data for F versus controls (n in a window of the same size).
import sys
import cypari2
pari = cypari2.Pari(); pari.allocatemem(10**9)
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
hit = bytearray(NMAX + 1)
for u in range(3, NMAX + 3):
    for v in range(3, NMAX + 3):
        # need t >= 3 with t*u*v - u - v <= NMAX
        base = u*v
        if base*3 - u - v > NMAX: break
        t = 3
        while True:
            n = t*u*v - u - v
            if n > NMAX: break
            hit[n] = 1
            t += 1
F = [n for n in range(2, NMAX + 1) if not hit[n]]
print("I3 failures <= %d: count %d; largest: %s" % (NMAX, len(F), F[-12:]))
print("failures:", F)
