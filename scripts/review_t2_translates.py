"""R24 from-scratch reproduction of EXCEPTIONAL_TUPLES2 §5(b) (initial segment vs translates).

f(n) = #{l = 3 mod 4, l <= y : n mod l in R(l)},  R(l) = {-4D mod l : D | ((l+1)/4)^2}.
Prints S_j/(N e_j) on windows [t+1, t+N] for given t's, and the avoider ratio
#{f=0}/(N prod(1-p_l)).
usage: review_t2_translates.py N y t1,t2,... [J]
"""
import sys
import numpy as np
from math import comb
from sympy import primerange, divisors

N = int(float(sys.argv[1])); y = int(sys.argv[2])
ts = [int(float(t)) for t in sys.argv[3].split(',')]
J = int(sys.argv[4]) if len(sys.argv) > 4 else 12
P = [l for l in primerange(3, y + 1) if l % 4 == 3]
R = {l: sorted({(-4 * D) % l for D in divisors(((l + 1) // 4) ** 2)}) for l in P}
p = [len(R[l]) / l for l in P]
e = [1.0] + [0.0] * J
for w in p:
    for k in range(J, 0, -1):
        e[k] += w * e[k - 1]
P0 = float(np.prod([1 - w for w in p]))
js = list(range(2, J + 1, 2))
print(f"N={N:.0e} y={y} #P={len(P)}  Pi(1-p)={P0:.4e}")
print("t".rjust(12), "avoid/CRT", *[f"j={j}".rjust(8) for j in js])
for t in ts:
    f = np.zeros(N, dtype=np.int16)
    for l in P:
        start = (t + 1) % l           # residue of first integer in the window
        for b in R[l]:
            off = (b - start) % l     # index i with t+1+i = b mod l
            f[off::l] += 1
    h = np.bincount(f)
    S = [sum(comb(v, j) * int(c) for v, c in enumerate(h)) for j in range(J + 1)]
    row = [f"{S[j] / (N * e[j]):8.4f}" for j in js]
    print(f"{t:12.4g}", f"{h[0] / (N * P0):9.4f}", *row)
