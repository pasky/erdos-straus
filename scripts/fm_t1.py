"""FF_MUTE (O195) Theorem 4.2 check: which monic P (all, not only irreducible) coprime to sA are shot-solved.

usage: fm_t1.py p A s N maxd
For every monic P of degree 1..N coprime to s*A: searches all monic irreducible f (deg <= maxd, f = -1 mod A, f != s,
f coprime to P) and records the set of degrees d for which -P/A lies in <s^2> mod f. Reports, separately for squares
and non-squares: #P, #shot-solved, and for solved squares the parities of the degrees d that work.
Every hit is re-verified by the exact identity of Prop 2.1 (lifted j).
"""
import sys
from fm_poly import Fp, parse, show

p = int(sys.argv[1]); F = Fp(p)
A = parse(sys.argv[2]); s = parse(sys.argv[3]); N = int(sys.argv[4]); maxd = int(sys.argv[5])
k = len(A) - 1; h = len(s) - 1
minus1 = F.mod((p - 1,), A)

mods = []
for d in range(1, maxd + 1):
    for f in F.irreducibles(d):
        if f == s or F.mod(f, A) != minus1:
            continue
        s2 = F.mulmod(s, s, f); orb = {}; x = (1,); j = 0
        while x not in orb:
            orb[x] = j; x = F.mulmod(x, s2, f); j += 1
        mods.append((d, f, orb, len(orb), F.egcd_inv(A, f)))


def verify(P, f, j0, ords):
    n = len(P) - 1; d = len(f) - 1; j = j0
    while j < 1 or k + 2 * j * h <= n + d:
        j += ords
    Q2 = (1,)
    for _ in range(2 * j):
        Q2 = F.mul(Q2, s)
    E, r = F.divmod(F.add(P, F.mul(A, Q2)), f); assert not r
    X, r = F.divmod(F.add(P, E), A); assert not r
    f1 = F.add(f, (1,))
    Y, r = F.divmod(F.mul(P, f1), A); assert not r
    Zn, r = F.divmod(F.mul(F.mul(P, X), f1), A); assert not r
    lhs = F.mul(F.mul(F.mul(A, X), Y), Zn)
    rhs = F.mul(P, F.add(F.add(F.mul(Y, Zn), F.mul(X, Zn)), F.mul(Q2, F.mul(X, Y))))
    vz = F.val(Zn, s) - 2 * j
    return lhs == rhs and X[-1] == Y[-1] == Zn[-1] == 1 and (vz >= 0 or vz % 2 == 0) and len(F.gcd(X, P)) == 1


squares = set()
for e in range(1, N // 2 + 1):
    for M in F.monics(e):
        squares.add(F.mul(M, M))

stats = {True: [0, 0, set()], False: [0, 0, set()]}
bad = 0
for n in range(1, N + 1):
    for P in F.monics(n):
        if len(F.gcd(P, F.mul(A, s))) > 1:
            continue
        sq = P in squares
        st = stats[sq]; st[0] += 1
        ds = set(); first = None
        for d, f, orb, ords, Ainv in mods:
            Pm = F.mod(P, f)
            if not Pm:
                continue
            t = F.mod(F.neg(F.mul(Pm, Ainv)), f)
            if t in orb:
                ds.add(d % 2)
                if first is None:
                    first = (f, orb[t], ords)
        if first:
            st[1] += 1
            if sq:
                st[2] |= ds
            if not verify(P, *first):
                bad += 1
print(f"q={p} A={show(A)} s={show(s)} deg P<={N} f-deg<={maxd}: squares {stats[True][0]} shot-solved {stats[True][1]}"
      f" (d parities used {sorted(stats[True][2])}); non-squares {stats[False][0]} shot-solved {stats[False][1]};"
      f" verify failures {bad}")
