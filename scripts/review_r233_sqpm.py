"""R233: from-scratch SQ_± split. Signed words (t,u,v), tuv != 0, tuv - u - v = n, |t| <= T; enumerated by
(t, u): v = (n + u)/(tu - 1) must be a nonzero integer, u ranging over the finite set where tu - 1 | n + u,
found via signed divisors D = tu - 1 of n + u?  (u unknown) -> instead via A | tn + 1 (A = tu - 1 = D, both signs).
Clean: |side| has no prime r with (r/n) = -1; zero side clean. usage: [strict] T n..."""
import sys
from sympy import factorint
from review_r233_common import jacobi
strict = sys.argv[1] == 'strict'
args = sys.argv[2:] if strict else sys.argv[1:]
T = int(args[0])
for n in map(int, args[1:]):
    def clean(x):
        return x == 0 or all(jacobi(r, n) != -1 for r in factorint(abs(x)))
    W = Nm = U = 0
    tc = tu = None
    for t in sorted([s * a for a in range(1, T + 1) for s in (1, -1)], key=abs):
        Nt = t * n + 1
        f = factorint(abs(Nt))
        pos = [1]
        for r, e in f.items():
            pos = [d * r ** k for d in pos for k in range(e + 1)]
        for A in pos + [-d for d in pos]:
            B = Nt // A
            if (A + 1) % t or (B + 1) % t:
                continue
            u, v = (A + 1) // t, (B + 1) // t
            if u == 0 or v == 0:
                continue
            assert t * u * v - u - v == n
            if strict and min(t, u, v) > 0:
                continue
            W += 1
            c = jacobi(A, n) == -1
            unf = not (clean(Nt) or clean(n + u) or clean(n + v))
            assert not (c and not unf)
            Nm += c; U += unf
            if c and tc is None: tc = abs(t)
            if unf and tu is None: tu = abs(t)
    print(n, "strict" if strict else "incl+", "W", W, "N-", Nm, "U", U, "forced %.2f" % (1 - U / W),
          "N-/U %d/%d" % (Nm, U), "least|t| cert", tc, "unforced", tu)
