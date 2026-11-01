# z53_thin15_xcheckB.py — brute-force cross-check of the candidate enumeration of z53_thin15_menuB.py int:
# every odd u <= UMAX, odd prime p <= PMAX with c_o = odd(15u^p - 1) <= 2^E + 17 (E = v2(15u^p-1)); and every
# limit-level solution of menu B found by direct divisor enumeration of N = 16 + c (X = -1, X' = -16 mod c_o).
import sys
from z53_thin15_menus import divs
UMAX, PMAX = int(sys.argv[1]), int(sys.argv[2])
ps = [p for p in range(3, PMAX + 1) if all(p % q for q in range(2, p))]
cands = []; lim = []
for p in ps:
    for u in range(1, UMAX + 1, 2):
        c = 15 * u ** p - 1; E = (c & -c).bit_length() - 1; co = c >> E
        if co <= 2 ** E + 17:
            cands.append((E, p, u))
            N = 16 + c
            for X in divs(N):
                if (X + 1) % co == 0 and (N // X + 16) % co == 0: lim.append((E, p, u, X, N // X))
print('brute force: odd u <= %d, p <= %d: candidates %s' % (UMAX, PMAX, cands))
print('limit-level solutions:', lim)
