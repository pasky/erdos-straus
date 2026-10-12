"""Independent cross-check of bs_ff_es.py: (1) verify witnesses give A*XYZ = P(XY+YZ+ZX);
(2) brute force over X (deg n-k), Y (deg <= ymax), Z solved from the equation."""
import sys
import bs_ff_es as F


def verify(A, P, X, a, b, E):
    kap = F.divmod_(F.add(a, b), E)
    assert not kap[1]
    kap = kap[0]
    N = F.mul(P, X)
    Y = F.divmod_(F.mul(kap, N), a)
    Z = F.divmod_(F.mul(kap, N), b)
    assert not Y[1] and not Z[1]
    Y, Z = Y[0], Z[0]
    assert X[-1] == Y[-1] == Z[-1] == 1, (X, Y, Z)
    lhs = F.mul(A, F.mul(X, F.mul(Y, Z)))
    rhs = F.mul(P, F.add(F.add(F.mul(X, Y), F.mul(Y, Z)), F.mul(Z, X)))
    assert lhs == rhs
    return Y, Z


def brute(A, P, ymax):
    k, n = len(A) - 1, len(P) - 1
    for X in F.monics(n - k):
        for dy in range(n - k, ymax + 1):
            for Y in F.monics(dy):
                # 1/Z = A/P - 1/X - 1/Y = (AXY - PY - PX)/(PXY)
                num = F.sub(F.sub(F.mul(A, F.mul(X, Y)), F.mul(P, Y)), F.mul(P, X))
                if not num:
                    continue
                Z, r = F.divmod_(F.mul(P, F.mul(X, Y)), num)
                if not r and Z and Z[-1] == 1:
                    return (X, Y, Z)
    return None


if __name__ == "__main__":
    F.Q = int(sys.argv[1])
    A = tuple(int(c) for c in reversed(sys.argv[2]))
    n, ymax = int(sys.argv[3]), int(sys.argv[4])
    agree = 0
    for P in F.irreducibles(n):
        if not F.divmod_(P, A)[1]:
            continue
        w = list(F.es_solutions(A, P, first_only=False))
        for t in w:
            verify(A, P, *t)
        bf = brute(A, P, ymax)
        assert (bf is not None) == bool(w), (P, bf, len(w))
        agree += 1
    print("q", F.Q, "A", sys.argv[2], "n", n, "all", agree, "agree; witnesses verified")
