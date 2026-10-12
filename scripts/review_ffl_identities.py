"""R161: direct verification of the explicit identities of Prop 1.4(i),(ii), Lemma 5.1 and Thm 6.1.

Each check builds X, Y, Z from the stated formulas and verifies A*X*Y*Z == P*(XY+YZ+ZX), monicity and NC
(all degrees >= n - k).
"""
import random
from review_ffl_poly import PolyRing


def check(R, A, P, X, Y, Z):
    n, k = R.deg(P), R.deg(A)
    lhs = R.mul(A, R.mul(X, R.mul(Y, Z)))
    rhs = R.mul(P, R.add(R.add(R.mul(X, Y), R.mul(Y, Z)), R.mul(Z, X)))
    return lhs == rhs and all(R.lc(W) == 1 and R.deg(W) >= n - k for W in (X, Y, Z))


# Thm 6.1: F2, A = T^2, every irreducible P of degree 3..15
R = PolyRing(2)
A = R.parse("100")
T1 = R.parse("11")
tot = 0
for n in range(3, 16):
    for P in R.irreducibles(n):
        if R.mod(P, A) == (1,):  # P = -1 mod T^2: Prop 1.4(i)
            X = R.divmod(R.add(P, (1,)), A)[0]
            PX = R.mul(P, X)
            ok = check(R, A, P, X, R.add(PX, (1,)), R.mul(PX, R.add(PX, (1,))))
        else:
            assert R.mod(P, A) == T1, "P mod T^2 must be 1 or 1+T"
            Rr, rm = R.divmod(R.add(P, T1), A)
            assert not rm
            c, rm2 = R.divmod(R.add(Rr, (1,)), T1)
            assert not rm2 and R.lc(c) == 1
            ok = check(R, A, P, Rr, R.mul(c, P), R.mul(c, R.mul(Rr, P)))
        assert ok, (n, R.show(P))
        tot += 1
print("Thm 6.1: identity + monic + NC verified for all", tot, "irreducible P of degree 3..15 over F2")

# Prop 1.4 (i), (ii) on random monic P (any, not nec. irreducible) in the right classes
rnd = random.Random(161)
for q in (3, 4, 5, 7, 9):
    R = PolyRing(q)
    for _ in range(300):
        k = rnd.randrange(1, 4)
        A = tuple(rnd.randrange(q) for _ in range(k)) + (1,)
        n = rnd.randrange(k + 1, k + 7)
        for shift in ((1,), (2,) if q % 2 else None):
            if shift is None:
                continue
            # P = A*U - shift, U monic of degree n-k
            U = tuple(rnd.randrange(q) for _ in range(n - k)) + (1,)
            P = R.sub(R.mul(A, U), shift)
            X = U
            PX = R.mul(P, X)
            if shift == (1,):
                ok = check(R, A, P, X, R.add(PX, (1,)), R.mul(PX, R.add(PX, (1,))))
            else:
                ok = check(R, A, P, X, PX, PX)
            assert ok
print("Prop 1.4 (i),(ii): verified on random P for q in 3,4,5,7,9 ((ii) only odd q)")

# Lemma 5.1 on random data: choose A, h, g, d, then P := A h g d - 1 - h g
for q in (2, 3, 5):
    R = PolyRing(q)
    for _ in range(300):
        A = tuple(rnd.randrange(q) for _ in range(rnd.randrange(1, 3))) + (1,)
        h = tuple(rnd.randrange(q) for _ in range(rnd.randrange(0, 3))) + (1,)
        g = tuple(rnd.randrange(q) for _ in range(rnd.randrange(0, 3))) + (1,)
        d = tuple(rnd.randrange(q) for _ in range(rnd.randrange(0, 4))) + (1,)
        hg = R.mul(h, g)
        P = R.sub(R.sub(R.mul(A, R.mul(hg, d)), (1,)), hg)
        if R.deg(P) <= R.deg(A) or R.lc(P) != 1:
            continue
        assert check(R, A, P, R.mul(hg, d), R.mul(d, P), R.mul(hg, R.mul(d, P)))
print("Lemma 5.1: identity + monic + NC verified on random data, q = 2, 3, 5")
