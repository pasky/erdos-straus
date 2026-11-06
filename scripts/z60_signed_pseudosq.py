#!/usr/bin/env python3
"""z60 SIGNED: do Gauss-exceptional survivor lines and R both 'see' pseudo-squareness?

For a level (L, D) with a non-zero C1 T1-survivor line s (as found by z59_walds_diag.py; cusp space, good odd squares),
and the matching rational Gauss-exceptional G = phi (x) chi_{D'} (elliptic curve, given by a-invariants and D'),
compute for every squarefree n in C1(2N), n <= B (gcd(n, 2N) = 1):
  s(n)            exact survivor coefficient (normalised to be primitive integral),
  w(n) = s(n)^2 / sqrt(n)   (Waldspurger: proportional to L(1/2, G (x) chi_n) on C1 when the anchor is non-zero),
  PY(n) = prod_{l <= Y, l good} (1 - a_l(G) chi_n(l)/l + 1/l)^{-1}   (partial Euler product of G (x) chi_n at the centre,
          classical normalisation s = 1), chi_n(l) = (n/l)  [n = 1 mod 8],
  R(n)            the (*) count, by direct enumeration,
  np(n)           least prime l with (n/l) = -1.
Prints summary statistics (vanishing rate of s by PY tercile, Spearman correlations) and dumps a table.
Usage: uv run --with cypari2 python scripts/z60_signed_pseudosq.py L D B "[a1,a2,a3,a4,a6]" Dprime Y outfile
"""
import sys, math
import cypari2

pari = cypari2.Pari()
pari.allocatemem(2_500_000_000)
L, D, B = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
AINV, DP, Y, OUT = sys.argv[4], int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]
N = L // 4
oddp = [int(q) for q in pari.factor(N)[0] if int(q) != 2] if N > 1 else []


def in_C1(n):
    return n % 8 == 1 and all(n % q and pow(n % q, (q - 1) // 2, q) == 1 for q in oddp)


mf = pari(f"mfinit([{L},3/2,{D}],1)")
C = pari.mfcoefs(mf, B)
sub = pari("(C,r)->vecextract(C, apply(x->x+1, r), [1..matsize(C)[2]])")
rows = [m * m for m in range(1, int(B ** 0.5) + 1, 2) if pari.gcd(m, 2 * N) == 1]
K = pari.matker(sub(C, rows))
c1 = [n for n in range(1, B + 1) if pari.gcd(n, 2 * N) == 1 and in_C1(n)]
M = sub(C, c1) * K
r = int(pari.matrank(M))
assert r == 1, f"rank on C1 = {r} (need a single survivor line)"
jj = next(j for j in range(int(pari.matsize(K)[1])) if any(M[i, j] != 0 for i in range(len(c1))))
f = pari("(C,K,j)->C*K[,j]")(C, K, jj + 1)
vals = {n: f[n] for n in c1}
den = pari.denominator(pari.Vec([vals[n] for n in c1]))
g = pari.content(pari.Vec([vals[n] * den for n in c1]))
s = {n: int(vals[n] * den / g) for n in c1}

E = pari.ellinit(pari(AINV))
NG = int(pari.ellglobalred(E)[0]) * DP * DP
primesY = [int(q) for q in pari.primes([2, Y]) if (2 * N * DP * int(pari.ellglobalred(E)[0])) % int(q)]
aphi = {l: int(pari.ellap(E, l)) for l in primesY}


def PY(n):
    pr = 1.0
    for l in primesY:
        a = aphi[l] * int(pari.kronecker(DP, l)) * int(pari.kronecker(n, l))
        pr /= (1 - a / l + 1 / l)
    return pr


# R(n) for n <= B by enumeration of (u, Bv, Cc): n = 4 u Bv Cc - u - Bv
Rc = [0] * (B + 1)
u = 1
while 4 * u - u - 1 <= B:
    Cc = 1
    while 4 * u * Cc - u - 1 <= B:
        Bv = 1
        while True:
            n = 4 * u * Bv * Cc - u - Bv
            if n > B:
                break
            if n > 0:
                Rc[n] += 1
            Bv += 1
        Cc += 1
    u += 1


def leastnr(n):
    for l in pari.primes(200):
        l = int(l)
        if int(pari.kronecker(n, l)) == -1:
            return l
    return 999


sq = [n for n in c1 if n > 1 and pari.issquarefree(n)]
rowsout = []
for n in sq:
    rowsout.append((n, int(pari.isprime(n)), s[n], s[n] ** 2 / math.sqrt(n), PY(n), Rc[n], leastnr(n)))
with open(OUT, "w") as fo:
    fo.write(f"# L={L} D={D} B={B} G=E{AINV} twisted by {DP}; Y={Y}; columns: n isprime s(n) w=s^2/sqrt(n) PY R(n) n_p\n")
    for row in rowsout:
        fo.write(" ".join(str(x) if not isinstance(x, float) else f"{x:.5g}" for x in row) + "\n")


def spearman(xs, ys):
    def rank(v):
        o = sorted(range(len(v)), key=lambda i: v[i])
        rk = [0] * len(v)
        i = 0
        while i < len(o):
            j = i
            while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]:
                j += 1
            for k in range(i, j + 1):
                rk[o[k]] = (i + j) / 2
            i = j + 1
        return rk
    rx, ry = rank(xs), rank(ys)
    mx, my = sum(rx) / len(rx), sum(ry) / len(ry)
    cov = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    return cov / math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))


for label, sel in (("primes", [x for x in rowsout if x[1]]), ("all squarefree", rowsout)):
    n0 = len(sel)
    ws = sorted(x[4] for x in sel)
    t1, t2 = ws[n0 // 3], ws[2 * n0 // 3]
    bins = [[x for x in sel if x[4] <= t1], [x for x in sel if t1 < x[4] <= t2], [x for x in sel if x[4] > t2]]
    print(f"[{label}] n={n0}; vanishing rate of s by PY tercile (low/mid/high): "
          + " / ".join(f"{sum(1 for x in b if x[2] == 0)}/{len(b)}" for b in bins))
    print(f"  Spearman(w, PY) = {spearman([x[3] for x in sel], [x[4] for x in sel]):.3f};  "
          f"Spearman(R, PY) = {spearman([x[5] for x in sel], [x[4] for x in sel]):.3f};  "
          f"Spearman(R, w) = {spearman([x[5] for x in sel], [x[3] for x in sel]):.3f};  "
          f"Spearman(R, n_p) = {spearman([x[5] for x in sel], [x[6] for x in sel]):.3f}")
    zs = [x for x in sel if x[5] == 0]
    print(f"  R-zeros in this set: {[(x[0], x[2], round(x[4], 3)) for x in zs]}  (n, s(n), PY)")
    print(f"  vanishing rate of s at R-zeros: {sum(1 for x in zs if x[2] == 0)}/{len(zs)}; overall {sum(1 for x in sel if x[2]==0)}/{n0}")
