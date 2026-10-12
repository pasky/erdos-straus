"""R161: independent verification of a linear-family covering certificate (format of data/ffl/cover_*.txt).

Line format: leaf W=<W> r=<r> E=<E> a=(t<i>,<a0>) b=(t<j>,<b0>)   (polys as digit strings, high->low).
Types (doc §6.2): t0: a0, t1: P*a0, t2: X/a0, t3: P*X/a0, with X = (P+E)/A.
Checks:
 (1) every unit class mod every leaf modulus is accounted for: the leaves partition the units mod lcm of leaf moduli
     (for a single-level certificate: the r's are exactly the units mod W);
 (2) W_F = A * monic(E) * lcm(a0,b0) divides the leaf modulus W;
 (3) for every leaf and every degree n in [n_F, n_F + extra], EVERY monic P = r (mod W) of degree n (irreducible or
     not) makes the family valid, and the produced (X,Y,Z) satisfies A XYZ = P(XY+YZ+ZX), monic, NC.
     For irreducible P we additionally only need gcd(E,P)=1, which holds as deg E < n.
Usage: review_ffl_cert.py q A cert_file [extra]
"""
import sys
import itertools
from review_ffl_poly import PolyRing

q, Astr, fn = int(sys.argv[1]), sys.argv[2], sys.argv[3]
extra = int(sys.argv[4]) if len(sys.argv) > 4 else 2
R = PolyRing(q)
A = R.parse(Astr)
k = R.deg(A)


def lcm(a, b):
    return R.divmod(R.mul(a, b), R.gcd(a, b))[0]


leaves = []
for line in open(fn):
    if not line.startswith("leaf"):
        continue
    f = dict(tok.split("=", 1) for tok in line.split()[1:])
    ta, a0 = f["a"].strip("()").split(",")
    tb, b0 = f["b"].strip("()").split(",")
    leaves.append((R.parse(f["W"]), R.parse(f["r"]), R.parse(f["E"]), int(ta[1]), R.parse(a0), int(tb[1]), R.parse(b0)))
print(len(leaves), "leaves")

# (1) partition check without enumerating the lcm modulus: leaves (W_i, r_i) are unit classes; they are pairwise
# disjoint iff r_i != r_j mod gcd(W_i, W_j) (CRT), and they exhaust the units mod L iff sum_i 1/Phi(W_i) == 1.
from fractions import Fraction


def phi(W):
    res = Fraction(R.q ** R.deg(W))
    for l, e in R.factor(W):
        res *= Fraction(R.q ** R.deg(l) - 1, R.q ** R.deg(l))
    return res


assert all(r and R.gcd(r, W) == (1,) and R.deg(r) < R.deg(W) for W, r, *_ in leaves), "leaf class not a unit"
dens = sum(Fraction(1) / phi(W) for W, *_ in leaves)
overlap = 0
for i in range(len(leaves)):
    Wi, ri = leaves[i][0], leaves[i][1]
    for j in range(i + 1, len(leaves)):
        Wj, rj = leaves[j][0], leaves[j][1]
        g = R.gcd(Wi, Wj)
        if R.mod(ri, g) == R.mod(rj, g):
            overlap += 1
print(f"(1) density sum = {dens}, overlapping pairs = {overlap} -> exact partition of units: {dens == 1 and overlap == 0}")
# all leaf moduli must be multiples of a common root containing A*T*(T+1)... (checked by caller via root arg)


def term(t, a0, P, X):
    if t == 0:
        return a0
    if t == 1:
        return R.mul(P, a0)
    qt, rm = R.divmod(X, a0)
    assert not rm
    return qt if t == 2 else R.mul(P, qt)


maxnF = 0
allok = True
nchecks = 0
for W, r, E, ta, a0, tb, b0 in leaves:
    WF = R.mul(A, R.mul(R.monic(E), lcm(a0, b0)))
    ok2 = R.divides(WF, W)
    nF = 1 + max(k + R.deg(a0) + R.deg(b0), R.deg(E))
    maxnF = max(maxnF, nF)
    for n in range(max(nF, R.deg(W) + 1), max(nF, R.deg(W) + 1) + extra + 1):
        for U in R.monics(n - R.deg(W)):
            P = R.add(R.mul(W, U), r)
            PE = R.add(P, E)
            X, rm = R.divmod(PE, A)
            good = not rm and R.divides(a0, X) and R.divides(b0, X)
            if good:
                a, b = term(ta, a0, P, X), term(tb, b0, P, X)
                s = R.add(a, b)
                good = bool(s) and R.lc(s) == R.lc(E) and R.divides(E, s)
            if good:
                kap = R.divmod(s, E)[0]
                N = R.mul(P, X)
                Y, r1 = R.divmod(R.mul(kap, N), a)
                Z, r2 = R.divmod(R.mul(kap, N), b)
                lhs = R.mul(A, R.mul(X, R.mul(Y, Z)))
                rhs = R.mul(P, R.add(R.add(R.mul(X, Y), R.mul(Y, Z)), R.mul(Z, X)))
                good = (not r1 and not r2 and lhs == rhs and all(R.lc(t) == 1 and R.deg(t) >= n - k for t in (X, Y, Z)))
            nchecks += 1
            if not good:
                allok = False
                print("FAIL leaf r=", R.show(r), "n=", n, "P=", R.show(P))
                break
    if not ok2:
        allok = False
        print("W_F does not divide W for leaf r=", R.show(r))
print(f"(2)+(3) all leaves: W_F | W and valid on every P of the class for n in [max(n_F, deg W+1), +{extra}]: {allok};"
      f" {nchecks} P checked; max n_F = {maxnF}")
