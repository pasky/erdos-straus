"""O197: cell table for length-3 HJ words n/A = [[v,t,u]] (n = tuv-u-v, A = tu-1, A* = tv-1, t,u,v >= 1).
Jacobi (A/n) from DEDEKIND_ES Cor 4.1: 2(A/n) = n+1 - n(t+u+v-9) - A - A* (mod 8), a function of (t,u,v) mod 8.
(1) brute check of that cell formula on all words with t,u,v < 60 (interior AND boundary words, gcd(A,n)=1);
(2) for m = 4..16: among cells mod lcm(8,m) with n odd, how many lie in the five m-slices
    m | tu-1, m | tv-1, m | t, m | u, m | v, split by the value of chi = (-A/n)."""
from itertools import product
from math import gcd, lcm


def jac_cell(t, u, v):
    n = t*u*v - u - v; A = t*u - 1; As = t*v - 1
    r = (n + 1 - n*(t+u+v-9) - A - As) % 8
    return {2: 1, 6: -1}.get(r)


def slice_hit(m, t, u, v):
    return (t*u-1) % m == 0 or (t*v-1) % m == 0 or t % m == 0 or u % m == 0 or v % m == 0


if __name__ == '__main__':
    from sympy import jacobi_symbol
    bad = tot = 0
    for t, u, v in product(range(1, 60), repeat=3):
        n = t*u*v - u - v; A = t*u - 1
        if n < 3 or n % 2 == 0 or A < 1 or gcd(A, n) != 1: continue
        tot += 1
        bad += jacobi_symbol(A, n) != jac_cell(t % 8, u % 8, v % 8)
    print(f"(1) Jacobi cell formula: {tot} words, {bad} mismatches")
    for m in range(4, 17):
        mod = lcm(8, m); c = {1: [0, 0], -1: [0, 0]}
        for t, u, v in product(range(mod), repeat=3):
            n = (t*u*v - u - v) % mod
            if n % 2 == 0: continue
            j = jac_cell(t % 8, u % 8, v % 8); chi = j if n % 4 == 1 else -j
            c[chi][0] += 1; c[chi][1] += slice_hit(m, t, u, v)
        print(f"(2) m={m:2d} mod {mod:3d}: chi=-1 cells {c[-1][0]}, in slices {c[-1][1]} ({c[-1][1]/c[-1][0]:.3f}); "
              f"chi=+1 cells {c[1][0]}, in slices {c[1][1]} ({c[1][1]/c[1][0]:.3f})")
