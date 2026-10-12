"""Odd-square test (B5/T1) for the F_q[t] analogue: for P = M^2 (M monic irreducible), classify all
monic solutions of A/P = 1/X+1/Y+1/Z by how many denominators P divides (Type I: one, Type II: two,
other: 'descent' solutions)."""
import sys
from collections import Counter
import bs_ff_es as F


def classify(A, P):
    c = Counter()
    seen = set()
    for X, a, b, E in F.es_solutions(A, P, first_only=False):
        kap = F.divmod_(F.add(a, b), E)[0]
        N = F.mul(P, X)
        Y = F.divmod_(F.mul(kap, N), a)[0]
        Z = F.divmod_(F.mul(kap, N), b)[0]
        key = (X,) + tuple(sorted((Y, Z)))
        if key in seen:
            continue
        seen.add(key)
        t = sum(1 for W in (X, Y, Z) if not F.divmod_(W, P)[1])
        c[t] += 1
    return c


if __name__ == "__main__":
    F.Q = int(sys.argv[1])
    A = tuple(int(x) for x in reversed(sys.argv[2]))
    m = int(sys.argv[3])
    tot = Counter()
    nz = Counter()
    for M in F.irreducibles(m):
        if not F.divmod_(M, A)[1]:
            continue
        c = classify(A, F.mul(M, M))
        tot.update(c)
        for t in (1, 2):
            if c[t]:
                nz[t] += 1
        nz['any'] += 1 if sum(c.values()) else 0
        nz['M'] += 1
    print(f"q={F.Q} A={sys.argv[2]} P=M^2, deg M={m}: #M={nz['M']}, solvable={nz['any']}, "
          f"with TypeI={nz[1]}, with TypeII={nz[2]}; total sols by #(P|denominators): {dict(tot)}")
