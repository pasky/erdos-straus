"""O169 §4.5: Jacobi symbol (A/n) on length-3 HJ words n/A=[[v,t,u]] is a function of (t,u,v) mod 8 (Cor 4.1).
List the cells with n = 1 (4) and value -1, and test whether each is covered by an ES slice condition:
 I: 4|tu-1 (A),  I*: 4|tv-1 (A*),  II: 4|t ((A)3),  IIe: 4|u or 4|v (Type II e-slice, b=1).
Usage: uv run python scripts/dk_cells.py
"""
from collections import Counter
cells = Counter()
unc = []
for t in range(8):
    for u in range(8):
        for v in range(8):
            n = t * u * v - u - v
            if n % 4 != 1:
                continue
            val = (n + 1 - (n * (t + u + v - 9) + (t * u - 1) + (t * v - 1))) % 8
            assert val in (2, 6)
            jac = 1 if val == 2 else -1
            es = ((t*u-1) % 4 == 0) or ((t*v-1) % 4 == 0) or t % 4 == 0 or u % 4 == 0 or v % 4 == 0
            cells[(jac, es)] += 1
            if jac == -1 and not es:
                unc.append((t, u, v))
print("cells (jacobi, covered by ES slice):", dict(cells))
print("(-1)-cells not covered:", sorted(set((a % 4, b % 4, c % 4) for a, b, c in unc)))
