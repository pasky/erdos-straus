"""Lemma 2.5: A ≡ 3 (4), d odd, d | A+1  =>  Jacobi(-d/A) = -1, hence -d mod A ∈ G_A (H4_NOT_POLYLOG def)."""
from sympy import jacobi_symbol
n = bad = 0
for A in range(3, 200001, 4):
    m = A + 1
    for d in range(1, int(m**0.5) + 1):
        if m % d: continue
        for dd in {d, m // d}:
            if dd % 2 == 0 or dd >= A: continue
            n += 1
            if jacobi_symbol(-dd % A, A) != -1: bad += 1
print(f"Lemma 2.5: {n} (A,d) instances with A<=200001, failures={bad}")
