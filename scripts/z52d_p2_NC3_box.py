# Z2736: box calibration for COMPOSITION_ES (§2): n odd, mu > sqrt(n), f = mu^2 - n (not a square), O' = Z[2 sqrt f], disc 16 f.
#  |box(mu)| = prod_{l in S(mu)} (2 v_l(mu) + 1),  S(mu) = {l | mu : l ∤ 2n, (-n/l) = 1}.
#  h+(O') = 2 h(O') since O' has no unit of norm -1 (Prop 1.2(c)); h via PARI quadclassunit(16 f).
#  Realised values: D | mu is a V_n value at mu if some primitive (A even, B odd) solves B^2-2 mu A B + n A^2 = -D; with
#  m^2 = f A^2 - D (then B = mu A ± m).  Enumerated over A <= AMAX (small) as the observed V_n values.
#  Output: box size vs h+, and the number of distinct D | mu realised by V_n points with A <= AMAX.
import sys, math
import cypari2
pari = cypari2.Pari(); pari.allocatemem(10**9)
from sympy import factorint, divisors, jacobi_symbol
from math import gcd, isqrt
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 61
W = int(sys.argv[2]) if len(sys.argv) > 2 else 40
AMAX = 400
rows = []
def kron(a, n): return int(pari(f"kronecker({a},{n})"))
for n in range(3, NMAX, 2):
    for mu in range(isqrt(n) + 1, isqrt(n) + 1 + W):
        f = mu*mu - n
        if isqrt(f)**2 == f: continue
        S = [l for l in factorint(mu) if (2*n) % l and l != 2 and kron(-n, l) == 1]
        box = 1
        for l in S: box *= 2*factorint(mu)[l] + 1
        hD = int(pari(f"quadclassunit({16*f}).no"))
        hplus = 2*hD
        # realised D | mu by V_n points with A even, A <= AMAX
        real = set()
        for D in divisors(mu):
            if gcd(D, n) != 1: continue
            for A in range(2, AMAX+1, 2):
                r = f*A*A - D
                if r < 0: continue
                m = isqrt(r)
                if m*m == r and (mu*A + m) % 2 == 1 or (m*m == r and (mu*A - m) % 2 == 1):
                    # need B odd: B = mu*A ± m, mu*A ± m odd; A even so parity = m parity... check B odd
                    B1 = mu*A + m; B2 = mu*A - m
                    if B1 % 2 == 1 or B2 % 2 == 1:
                        real.add(D); break
        rows.append((n, mu, f, len(S), box, hplus, box/hplus, len(divisors(mu)), len(real)))
print("n mu f |S| box h+ box/h+ #divisors(mu) #D realised (A<=%d)" % AMAX)
for r in rows[:40]: print(r)
import statistics
print("rows:", len(rows), " median box/h+:", round(statistics.median(r[6] for r in rows), 3),
      " fraction with box > h+:", round(sum(r[6] > 1 for r in rows)/len(rows), 3))
print("fraction of divisors D|mu realised by V_n (A<=%d): %.3f" % (AMAX, sum(r[8] for r in rows)/max(1,sum(r[7] for r in rows))))
