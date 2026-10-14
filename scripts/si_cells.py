"""si_cells: count cells (t,u,v) mod 8 with K=tuv-u-v odd, and chi=(-A/n) per cell (checked constant on 4 lifts).
Gives the leading constants of sum_{n<=X} N_-(n) ~ (c_-/512) X log^2 X / 2."""
from sympy import jacobi_symbol as J
odd = neg = pos = 0
for t0 in range(8):
    for u0 in range(8):
        for v0 in range(8):
            vals = set()
            for k in range(4):
                t, u, v = t0 + 8 * (k + 1), u0 + 8 * (2 * k + 1), v0 + 8 * (3 * k + 2)
                n = t * u * v - u - v
                if n % 2 == 0:
                    break
                vals.add(J((-(t * u - 1)) % n, n))
            else:
                odd += 1
                assert len(vals) == 1
                if vals == {-1}: neg += 1
                else: pos += 1
print(f"cells mod 8: K odd {odd}, chi=-1 {neg}, chi=+1 {pos}")
