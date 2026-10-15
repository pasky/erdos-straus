# R246: the exp class domain s = 34 (mod 45) is a LOCALLY non-square class: q = 18837001 | 2^90 - 1 = 4^45 - 1,
# so n_s mod q depends only on s mod 45, and (n_s / q) = -1.
import sympy as sp
q = 18837001
assert sp.isprime(q) and (2**90 - 1) % q == 0
print("ord_q(4) =", sp.n_order(4, q))
for s in range(34, 34 + 45*200, 45):
    assert sp.jacobi_symbol((4**s + 105) % q, q) == -1
print("(n_s/18837001) = -1 for all s = 34 + 45j, j < 200")
# contrast: the cubic family 256u^3+105, u = 32 (151), u arbitrary, does hit squares mod q
print("cubic family values mod q that are squares exist:",
      any(sp.jacobi_symbol((256*(32+151*t)**3 + 105) % q, q) == 1 for t in range(50)))
