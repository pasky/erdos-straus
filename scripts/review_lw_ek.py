"""R180: sanity check of k! e_k >= G^k - C(k,2) T G^(k-2) (T = sum g^2) on random weights, exact rationals."""
import random
from fractions import Fraction as F
from math import comb, factorial
random.seed(1)
worst = None
for trial in range(300):
    m = random.randint(3, 25); k = random.randint(2, min(m, 8))
    g = [F(random.randint(1, 50), random.randint(50, 400)) for _ in range(m)]
    e = [F(1)] + [F(0)] * k
    for gi in g:
        for j in range(k, 0, -1): e[j] += e[j - 1] * gi
    G = sum(g); T = sum(x * x for x in g)
    lhs = factorial(k) * e[k]; rhs = G ** k - comb(k, 2) * T * G ** (k - 2)
    assert lhs >= rhs, (m, k)
print("ok: k! e_k >= G^k - C(k,2) T G^(k-2) in 300 random exact trials")
