"""R233: n = 105 — all words, side primes, local symbols (r/3),(r/5),(r/7), and eps_l = (-A/l)."""
from sympy import factorint, legendre_symbol as L
from review_r233_common import jacobi
n = 105
W = [(t, u, (n + u) // (t * u - 1)) for t in range(1, n + 3) for u in range(1, 2 * n + 4)
     if t * u > 1 and (n + u) % (t * u - 1) == 0]
print(len(W), "words")
prs = set()
for t, u, v in W:
    A, B = t * u - 1, t * v - 1
    sides = (t * n + 1, n + u, n + v)
    ps = set().union(*[factorint(s) for s in sides])
    prs |= ps
    eps = tuple(L(-A % l, l) for l in (3, 5, 7))
    print((t, u, v), "A", A, "chi", jacobi(A, n), "sides", sides, "eps(3,5,7)", eps,
          "side-primes ψ", {r: jacobi(r, n) for r in ps})
for r in sorted(prs):
    print(r, [(L(r % l, l) if r % l else 0) for l in (3, 5, 7)])
