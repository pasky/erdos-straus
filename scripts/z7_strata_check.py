"""O231 §5: N- and U split by min(t,u,v) <= 2 vs >= 3 at given n (Jacobi psi).  usage: z7_strata_check.py n1 n2 ..."""
import sys
from sympy import factorint, divisors, jacobi_symbol as J
for n in map(int, sys.argv[1:]):
    cl = {}
    def clean(x):
        if x not in cl: cl[x] = all(J(r % n, n) != -1 for r in factorint(x))
        return cl[x]
    S = {k: [0, 0, 0] for k in ('min<=2', 'min>=3')}
    u = 1
    while (u - 2) * u <= n:
        for v in divisors(n + u):
            if v < u or (n + u + v) % (u * v): continue
            t = (n + u + v) // (u * v); m = 1 if u == v else 2
            k = 'min<=2' if min(t, u) <= 2 else 'min>=3'
            cert = J((t * u - 1) % n, n) == -1
            unf = not clean(t * n + 1) and not clean(n + u) and not clean(n + v)
            S[k][0] += m; S[k][1] += m * cert; S[k][2] += m * unf
        u += 1
    print(n, {k: f"N={a} Nm={b} U={c}" for k, (a, b, c) in S.items()})
