"""Depth = walk length (O233 goal 2).  For chi = -1 words of p and each pentagon vector x with v2(Q(x)) = k >= 2,
build the chain  L1 = L, F1 = L1 + x/2, L2 = edge of F1 through the conic point of x/2, F2 = L2 + x/4, ...
explicitly in coordinates (lattices as integer bases of 2^K * lattice in L-coordinates, compared by HNF), and check:
every step exists, x/2^j stays primitive, non-backtracking (L_{j+1} != L_j, F_{j+1} != F_j), and the chain has exactly
k - 1 steps after L (step = edge->vertex or vertex->edge).  Usage: z9_depth_walk.py pmax"""
import sys
from itertools import product
from fractions import Fraction as Fr
from sympy import Matrix, isprime
from sympy.matrices.normalforms import hermite_normal_form
from z9_lib import words, chi, path_gram, pentagon_vectors

K = 12  # scale


def hnf(rows):
    M = Matrix([[int(c * 2 ** K) for c in r] for r in rows]).T
    return tuple(hermite_normal_form(M))


def Qf(G, x):
    return sum(G[i][j] * x[i] * x[j] for i in range(3) for j in range(3))


def Bf(G, x, y):
    return sum(G[i][j] * x[i] * y[j] for i in range(3) for j in range(3))


def coords(basis, z):
    """coordinates of z in basis (3 rational rows), or None if not integral."""
    M = Matrix([[Fr(c) for c in r] for r in basis]).T
    c = M.solve(Matrix(z))
    return [Fr(int(ci.p), int(ci.q)) for ci in c]


def is_primitive_member(basis, z):
    c = coords(basis, z)
    if any(ci.denominator != 1 for ci in c):
        return False
    from math import gcd
    return gcd(gcd(int(c[0]), int(c[1])), int(c[2])) % 2 == 1


def add_half(basis, z):
    """basis of lattice + Z z/2 (z primitive member, so index 2)."""
    rows = [list(r) for r in basis] + [[c / 2 for c in z]]
    # reduce to 3 rows via HNF over 2^-K Z
    H = Matrix([[int(c * 2 ** K) for c in r] for r in rows]).T
    Hn = hermite_normal_form(H)
    return [[Fr(int(Hn[i, j]), 2 ** K) for i in range(3)] for j in range(Hn.shape[1])]


def edge_through(G, basis, y):
    """F (half-integral) with basis; return the classical index-2 sublattice whose hyperplane mod 2 contains y and
    the radical: L = {w in F : B(w, F) integral...}.  Brute: try the 3 sublattices that are classical, pick the one
    containing y."""
    out = []
    for phi in product((0, 1), repeat=3):
        if not any(phi):
            continue
        i = phi.index(1)
        sub = []
        for j in range(3):
            if j == i:
                sub.append([2 * c for c in basis[j]])
            elif phi[j]:
                sub.append([basis[j][k] + basis[i][k] for k in range(3)])
            else:
                sub.append(list(basis[j]))
        if all(Bf(G, a, b).denominator == 1 for a in sub for b in sub):
            if all(c.denominator == 1 for c in coords(sub, y)):
                out.append(sub)
    assert len(out) == 1, len(out)
    return out[0]


def walk(G, x):
    """returns number of steps."""
    L = [[Fr(int(i == j)) for j in range(3)] for i in range(3)]
    z = [Fr(c) for c in x]
    chain = [hnf(L)]
    cur, kind, steps = L, 'E', 0
    while True:
        q = Qf(G, z)
        if kind == 'E':
            assert is_primitive_member(cur, z)
            if q.denominator != 1 or q % 4 != 0:
                break
            cur = add_half(cur, z)
            z = [c / 2 for c in z]
            kind = 'V'
        else:
            if q.denominator != 1 or q % 2 != 0:
                break
            cur = edge_through(G, cur, z)
            kind = 'E'
        h = hnf(cur)
        assert h not in chain[-2:], "backtrack"
        chain.append(h)
        steps += 1
    return steps


pmax = int(sys.argv[1])
tot = bad = 0
for p in range(5, pmax + 1, 2):
    if not isprime(p):
        continue
    for w in words(p):
        if chi(w, p) != -1:
            continue
        G = [[Fr(c) for c in r] for r in path_gram(w)]
        for vec, ent in pentagon_vectors(w):
            if ent % 4:
                continue
            k = 0
            Qx = Qf(G, vec)
            while Qx % 2 == 0:
                Qx //= 2
                k += 1
            s = walk(G, vec)
            tot += 1
            if s != k - 1:
                bad += 1
                print("MISMATCH", p, w, vec, k, s)
print("checked", tot, "pentagon pointers, mismatches", bad)
