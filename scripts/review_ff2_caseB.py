"""R166 from-scratch Case B search at x = u (mod T^inf), x = 1 at every prime != T, A = T^k (q = p prime).
Case B (mixed types): E | D := 1 + T^k a0 b0 = 1 + T^k g L, E monic (lc(s) = 1),
  E = -u (mod T^{k+j}), E = -1 (mod L'),  L = lcm(a0, b0) = T^j L', g = gcd(a0, b0) | L (any g | L occurs).
Since D = 1 (mod M), M := T^{k+j} L', and deg D < 2 deg M, E or E' = D/E is the least residue of its class mod M.
usage: review_ff2_caseB.py p k u(low-first comma list) maxdegL' maxj [brute]
  brute: additionally enumerate ALL monic divisors of D (only for small deg D) to cross-check the reduction."""
import sys
from review_ff2_poly import *

p, k = int(sys.argv[1]), int(sys.argv[2])
setp(p)
u = tr([int(x) for x in sys.argv[3].split(',')])
dl, jm = int(sys.argv[4]), int(sys.argv[5])
brute = len(sys.argv) > 6
found = []
ncases = 0
for dL in range(dl + 1):
    for Lp in monics(dL):
        if Lp[0] == 0:
            continue
        gps = monic_divisors(Lp) if dL > 0 else [(1,)]
        for j in range(jm + 1):
            mT = Tpow(k + j)
            tT = mod(neg(u), mT)
            M = mul(mT, Lp)
            if dL > 0:
                tgt = crt(tT, mT, mod((p - 1,), Lp), Lp)
            else:
                tgt = tT
            itgt = invmod(tgt, M)
            L = mul(Tpow(j), Lp)
            for gp in gps:
                for gam in range(j + 1):
                    g = mul(Tpow(gam), gp)
                    D = add((1,), mul(Tpow(k), mul(g, L)))
                    ncases += 1
                    cands = set()
                    for r in (tgt, itgt):
                        if r and r[-1] == 1 and divides(r, D):
                            cands.add(r if r == tgt else dm(D, r)[0])
                    if brute:
                        bc = set()
                        for E in monic_divisors(D):
                            if mod(sub(E, tT), mT) == () and (dL == 0 or mod(add(E, (1,)), Lp) == ()):
                                bc.add(E)
                        assert bc == cands, (Lp, j, g, bc, cands)
                    for E in cands:
                        found.append((Lp, j, g, E, deg(D)))
print("cases", ncases, "families", len(found))
for f in found[:40]:
    print("L'", f[0], "j", f[1], "g", f[2], "E", f[3], "degE", deg(f[3]), "degD", f[4])
