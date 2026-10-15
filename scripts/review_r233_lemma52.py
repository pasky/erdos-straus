"""R233: Lemma 5.2 from scratch. For odd non-square n < LIM (both n = 1, 5 mod 8) and the automatic families
(t=1, u=1, v=1 on X=n+1; t=2 on X=2n+1; u=2, v=2 on X=n+2), enumerate the family words *by direct search*
(not via divisors), count chi = -1, compare with (tau/2)(1 - prod_{psi(r)=-1} [e even]/(e+1)).
Also sanity-check the three-bit fact chi = -1 <=> 4 | t,u,v,A or B on all words of these families."""
import sys
from fractions import Fraction
from sympy import factorint, divisor_count
from review_r233_common import jacobi

LIM = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
bad = checked = slicebad = 0
rate13 = 0
for n in range(9, LIM, 4):
    r = int(n ** 0.5)
    if r * r == n:
        continue
    fams = {}
    # direct search: t fixed (1 or 2) -> u ranges, v = (n+u)/(tu-1)
    for tfix in (1, 2):
        ws = []
        for u in range(1, 2 * n + 4):
            m = tfix * u - 1
            if m <= 0 or (n + u) % m:
                continue
            ws.append((tfix, u, (n + u) // m))
        fams[('t', tfix)] = ws
    for ufix in (1, 2):  # u fixed: t ranges, v = (n+u)/(tu-1)
        ws = []
        for t in range(1, n + 4):
            m = t * ufix - 1
            if m <= 0 or (n + ufix) % m:
                continue
            ws.append((t, ufix, (n + ufix) // m))
        fams[('u', ufix)] = ws
        fams[('v', ufix)] = [(t, v, u) for (t, u, v) in ws]
    for (kind, s), ws in fams.items():
        assert all(t * u * v - u - v == n for t, u, v in ws)
        X = 2 * n + 1 if (kind, s) == ('t', 2) else (n + 1 if s == 1 else n + 2)
        cert = 0
        for t, u, v in ws:
            A, B = t * u - 1, t * v - 1
            c = jacobi(A, n)
            cert += (c == -1)
            if n % 4 == 1:
                five = any(x % 4 == 0 for x in (t, u, v, A, B))
                slicebad += (five != (c == -1))
        f = factorint(X)
        tau = divisor_count(X)
        assert len(ws) == tau, (n, kind, s, len(ws), tau)
        prod = Fraction(1)
        for q, e in f.items():
            if jacobi(q, n) == -1:
                prod *= Fraction(1 if e % 2 == 0 else 0, e + 1)
        pred = Fraction(tau, 2) * (1 - prod)
        checked += 1
        bad += (pred != cert)
        if (kind, s) == ('u', 1) and pred == Fraction(tau, 3) and cert:
            rate13 += 1
print("families checked", checked, "formula mismatches", bad, "five-slice<->chi=-1 mismatches", slicebad,
      "#n with Div(n+1) rate exactly 1/3", rate13)
