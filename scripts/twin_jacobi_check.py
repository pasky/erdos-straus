"""EXCEPTIONAL_TWIN Lemma 1.1 check: every Case-B forced class -4D mod M
(M = 3 mod 4, A = (M+1)/4, D | A^2) has Jacobi symbol (-4D | M) = -1.
Usage: uv run python scripts/twin_jacobi_check.py [Xmax]"""
import sys
from sympy import jacobi_symbol, divisors

X = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
classes = bad = 0
for M in range(3, X + 1, 4):
    A = (M + 1) // 4
    for D in divisors(A * A):
        classes += 1
        if jacobi_symbol((-4 * D) % M, M) != -1:
            bad += 1
            print("counterexample", M, D)
print(f"M <= {X}: {classes} classes checked, {bad} with Jacobi != -1")
