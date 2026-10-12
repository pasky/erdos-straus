"""R161: own covering-tree search (independent of ffl_tree.c) producing certificates in the same line format.

Root W = A*T*(T+1)*... (given), unit classes r mod W. A leaf needs a linear family F = (E; ta,a0; tb,b0) with
W_F = A*monic(E)*lcm(a0,b0) | W and n_F = 1 + max(k + deg a0 + deg b0, deg E) <= NTH, valid at a representative P
of the class of degree max(n_F, deg W + 1) (validity is then class-constant by Lemma 6.2, re-derived in the review;
review_ffl_cert.py re-checks every P of several degrees). Otherwise refine by the next prime in REF.
Usage: review_ffl_tree.py q A root NTH maxdepth out_file
"""
import sys
import itertools
from review_ffl_poly import PolyRing

q, Astr, rootS, NTH, maxdepth, out = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
q = int(q)
R = PolyRing(q)
A = R.parse(Astr)
k = R.deg(A)
REF = [R.parse(s) for s in ["10", "11", "111", "10", "11", "1011", "1101", "10", "11", "111", "10011", "11001", "11111",
                            "10", "11"]]
root = (1,)
for s in rootS.split("*"):
    root = R.mul(root, R.parse(s))


def lcm(a, b):
    return R.divmod(R.mul(a, b), R.gcd(a, b))[0]


def term(t, a0, P, X):
    if t == 0:
        return a0
    if t == 1:
        return R.mul(P, a0)
    qt = R.divmod(X, a0)[0]
    return qt if t == 2 else R.mul(P, qt)


_fam = {}


def families(W):
    key = W
    if key in _fam:
        return _fam[key]
    WA, rm = R.divmod(W, A)
    assert not rm
    divs = sorted(set(R.divisors(WA)), key=lambda d: (len(d), d))
    fams = []
    units = [c for c in range(1, q)]
    for Em in divs:
        rest = R.divmod(WA, Em)[0]
        rdivs = [d for d in divs if R.divides(d, rest)]
        for u in units:
            E = R.scal(u, Em)
            for a0, b0 in itertools.combinations_with_replacement(rdivs, 2):
                if not R.divides(lcm(a0, b0), rest):
                    continue
                nF = 1 + max(k + R.deg(a0) + R.deg(b0), R.deg(E))
                if nF > NTH:
                    continue
                for ta in range(4):
                    for tb in range(4):
                        fams.append((E, ta, a0, tb, b0, nF))
    fams.sort(key=lambda f: f[5])
    _fam[key] = fams
    return fams


def valid(P, fam):
    E, ta, a0, tb, b0, nF = fam
    X, rm = R.divmod(R.add(P, E), A)
    if rm or not R.divides(a0, X) or not R.divides(b0, X):
        return False
    s = R.add(term(ta, a0, P, X), term(tb, b0, P, X))
    return bool(s) and R.lc(s) == R.lc(E) and R.divides(E, s)


leaves, uncovered = [], []


def solve(W, r, depth):
    for fam in families(W):
        n = max(fam[5], R.deg(W) + 1)
        P = R.add(R.mul(W, (0,) * (n - R.deg(W)) + (1,)), r)
        if valid(P, fam):
            leaves.append((W, r, fam))
            return
    if depth >= maxdepth:
        uncovered.append((W, r))
        return
    l = REF[depth]
    W2 = R.mul(W, l)
    for t in R.polys_below(R.deg(l)):
        r2 = R.add(r, R.mul(W, t))
        if R.gcd(r2, W2) == (1,):
            solve(W2, r2, depth + 1)


for r in R.polys_below(R.deg(root)):
    if r and R.gcd(r, root) == (1,):
        solve(root, r, 0)
with open(out, "w") as fh:
    for W, r, (E, ta, a0, tb, b0, nF) in leaves:
        fh.write(f"leaf W={R.show(W)} r={R.show(r)} E={R.show(E)} a=(t{ta},{R.show(a0)}) b=(t{tb},{R.show(b0)})\n")
    for W, r in uncovered:
        fh.write(f"uncovered W={R.show(W)} r={R.show(r)}\n")
print(f"q={q} A={Astr} root={rootS} NTH={NTH}: leaves={len(leaves)} uncovered={len(uncovered)} "
      f"maxleafdeg={max((R.deg(W) for W, *_ in leaves), default=0)}", flush=True)
