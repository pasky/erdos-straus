"""O234 T1 control for Prop 5.1: for every M ≡ 3 (4), M < Mmax, and every D ∈ 𝒟_e(M) with 4D < M, the class −4D mod M
contains no square (Jacobi (−D/M) = −1).  Exhaustive over M, all D, all residues m mod M.  usage: Mmax e"""
import sys
from sympy import factorint
Mmax, e = int(sys.argv[1]), int(sys.argv[2]); bad = tot = 0
for M in range(3, Mmax, 4):
    A = (M + 1) // 4; fA = factorint(A); sq = {m * m % M for m in range(M)}
    for D in range(1, (M - 1) // 4 + 1):
        ok = True
        for s, t in factorint(D).items():
            sg = fA.get(s, 0)
            if not sg or not (t <= 2 * sg or (s != 2 and t % 2 == 0 and t <= 2 * sg + 2 * e)): ok = False; break
        if not ok: continue
        tot += 1
        if (-4 * D) % M in sq: bad += 1; print("SQUARE HIT", M, D)
print(f"M<{Mmax}, e={e}: {tot} classes, {bad} containing a square")
