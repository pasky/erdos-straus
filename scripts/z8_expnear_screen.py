# z8_expnear_screen.py — unit-square screen for n_s = c0*4^s + k: residues s mod L such that n_s is a
# non-zero square modulo every prime q < QMAX with ord_q(4) | L (q odd) [and n_s = 1 mod 8 at 2].
# Survivors = candidate exponents near a profinite unit-square point (Thm 1.4 of EXPONENT_COVERING).
# Usage: PYTHONPATH=scripts uv run python scripts/z8_expnear_screen.py c0 k QMAX L1 L2 ...
import sys
from ec_screen import primes_upto

c0, k, QMAX = map(int, sys.argv[1:4])
Ls = [int(x) for x in sys.argv[4:]]
P = primes_upto(QMAX)
for L in Ls:
    qs = [q for q in P if q > 2 and pow(4, L, q) == 1]
    surv = []
    base = 10 * L + 64
    for s in range(L):
        ss = base + s
        ok = True
        for q in qs:
            r = (c0 * pow(4, ss, q) + k) % q
            if r == 0 or pow(r, (q - 1) // 2, q) != 1:
                ok = False; break
        if ok:
            surv.append(ss % L)
    print('L=%d (%d primes): %d survivors %s' % (L, len(qs), len(surv), sorted(surv)[:30]), flush=True)
