"""Toy LP for CEILINGS_UNIFIED.md Thm 4.1 (EVIDENCE only).

n independent bits, each P(b=1)=p, P = n*p. F = 1[no bit set].
Order-k certificates: by Sym(n)-averaging (KARY Lemma 2.3) an optimal
order-k majorant/minorant may be taken symmetric, i.e. a polynomial of
degree <= k in h = #bits set, written in the basis C(h,j)/C(n,j).
  majorant:  min E G  s.t. G(0) >= 1, G(h) >= 0 (h>=1)
  minorant:  max E B  s.t. B(0) <= 1, B(h) <= 0 (h>=1)
Prints saving log(1/E G) of the best majorant and E B / E F of the best
minorant against k, to exhibit the common threshold k ~ P.
Exact rational LP (sympy.solvers.simplex.linprog); integer basis C(h,j).
Run:  PYTHONPATH=scripts uv run python scripts/unify_toy_lp.py
"""
import math
from fractions import Fraction
from sympy import Matrix, Rational
from sympy.solvers.simplex import linprog


def solve(n, p, k):
    """Exact optimal order-k majorant mean E G and minorant mean E B."""
    A = Matrix(n + 1, k + 1, lambda h, j: math.comb(h, j))
    mean = Matrix(1, k + 1, lambda _, j: math.comb(n, j) * p ** j)
    e0 = Matrix(n + 1, 1, lambda h, _: 1 if h == 0 else 0)
    # free variables as x = x+ - x-, both >= 0 (sympy 1.14's `bounds`
    # with (None, None) silently returned wrong optima in our tests)
    AA, cc = A.row_join(-A), mean.row_join(-mean)
    EG, _ = linprog(cc, -AA, -e0)        # min E G,  G >= F
    negEB, _ = linprog(-cc, AA, e0)      # max E B,  B <= F
    return EG, -negEB


def main():
    n = 40
    for P in (2, 4, 6, 8):
        p = Rational(P, n)
        EF = (1 - p) ** n
        print(f"n={n} p={p} P={P}  log(1/EF)={-math.log(float(EF)):.4f}")
        print("   k   saving(G)    EB/EF")
        for k in range(0, 25, 1):
            EG, EB = solve(n, p, k)
            sav = -math.log(float(EG))
            print(f"  {k:3d}  {sav:9.4f}  {float(EB / EF):9.4f}", flush=True)


if __name__ == "__main__":
    main()
