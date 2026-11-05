#!/usr/bin/env python3
"""z59 WALDS: exact q-expansion test of Theorem W1 / Cor W2 at small levels.

For level L = 4N and quadratic nebentypus psi = (D/.) (pari/Shimura convention: the ternary theta of a lattice of
determinant d has D = disc Q(sqrt d)), take the FULL space M_{3/2}(Gamma_0(L), psi) (pari mfinit flag 4: Eisenstein +
cusp, incl. unary thetas). Impose the T1 conditions g(l^2) = 0 for all primes l with l0 <= l, l^2 <= B (only large
primes, as in TERNARY Thm F's hypothesis) and compute the kernel K exactly (rational linear algebra).
Then evaluate K on the coefficients n <= B with n in C1(2N) (n = 1 mod 8, n a nonzero square mod every odd q | N),
gcd(n, 2N) = 1, and report the rank of that restriction (0 = every such g vanishes on C1 up to B), and separately
on Mordell's classes (n mod 840 in M) and on the squarefree / prime n.

Usage: uv run --with cypari2 python scripts/z59_walds_halfint.py L D B [l0] [space]   (l0 = 0: all odd squares m^2; l0 = -1: odd m^2 with gcd(m,2N)=1 (cusp space);
       space = pari mfinit flag, default 4 = full space, 1 = cusp forms, 3 = Eisenstein;
       optional 6th arg 1 = add rows g(z) = 0 at all known R-zeros z <= B, so rank 0 on C1 certifies that every valid
       proxy vanishes on C1 up to B)
"""
import sys, time
import cypari2

pari = cypari2.Pari()
pari.allocatemem(3_000_000_000)

L, D, B = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
l0 = int(sys.argv[4]) if len(sys.argv) > 4 else 11
SPACE = int(sys.argv[5]) if len(sys.argv) > 5 else 4   # pari mfinit space flag: 4 full, 1 cusp, 3 Eisenstein
ZROWS = int(sys.argv[6]) if len(sys.argv) > 6 else 0   # 1: also impose g(z) = 0 at every known R-zero z <= B (validity)
assert L % 4 == 0
N = L // 4
MORD = {1, 121, 169, 289, 361, 529}


def in_C1(n):
    if n % 8 != 1:
        return False
    for q in pari.factor(N)[0] if N > 1 else []:
        q = int(q)
        if q == 2:
            continue
        r = n % q
        if r == 0 or pow(r, (q - 1) // 2, q) != 1:
            return False
    return True


t0 = time.time()
mf = pari(f"mfinit([{L},3/2,{D}],{SPACE})")
dim = int(pari.mfdim(mf))
if dim == 0:
    print(f"L={L} D={D} dim=0")
    sys.exit(0)
C = pari.mfcoefs(mf, B)  # (B+1) x dim, row n = coefficient a(n)
t1 = time.time()
if l0 > 0:   # T1 at squares of primes l >= l0 only (TERNARY Thm F hypothesis)
    rows = [int(p) ** 2 for p in pari.primes([l0, int(B ** 0.5)])]
elif l0 == 0:  # validity: g(m^2) = 0 for every odd m (T1: R(m^2) = 0) -- legitimate on the FULL space
    rows = [m * m for m in range(1, int(B ** 0.5) + 1, 2)]
else:          # l0 = -1: good odd squares only, gcd(m, 2N) = 1 (m^2 in C1). Use this on the CUSP space: for a TERNARY-class
               # proxy g = E + h, Thm F gives E = 0 on C1, so h(m^2) = g(m^2) = 0 exactly for these m.
    rows = [m * m for m in range(1, int(B ** 0.5) + 1, 2) if pari.gcd(m, 2 * N) == 1]
sub = pari("(C,r)->vecextract(C, apply(x->x+1, r), [1..matsize(C)[2]])")
A = sub(C, rows)
if ZROWS:
    import gzip
    ROOT = "/home/pasky/projects/math/erdos-straus-claude-agent-worktree-0044/"
    zs = sorted(int(x) for x in gzip.open(ROOT + "data/z58/logic/zeros_1e10.txt.gz", "rt")
                if x.strip() and x[0] != "#" and int(x) <= B)          # all n = 1 (4), n <= 1e10, with R(n) = 0
    if SPACE != 4:  # cusp space (TERNARY class): only zeros in C1 coprime to 2N, where E = 0 by Thm F, so h(z) = g(z)
        zs = [z for z in zs if pari.gcd(z, 2 * N) == 1 and in_C1(z)]
    rows = sorted(set(rows) | set(zs))
    A = sub(C, rows)
K = pari.matker(A)
k = int(pari.matsize(K)[1])
c1 = [n for n in range(1, B + 1) if pari.gcd(n, 2 * N) == 1 and in_C1(n)]
mord = [n for n in c1 if n % 840 in MORD]
sqf = [n for n in c1 if n > 1 and pari.issquarefree(n)]
prm = [n for n in c1 if pari.isprime(n)]


def rank_on(ns):
    if not ns or k == 0:
        return 0, None
    M = sub(C, ns) * K
    r = int(pari.matrank(M))
    first = None
    if r:
        for j, n in enumerate(ns):
            if any(M[j, c] != 0 for c in range(k)):
                first = n
                break
    return r, first


out = [f"L={L} N={N} D={D} space={SPACE} zrows={ZROWS} dim={dim} B={B} l0={l0} #T1-conditions={len(rows)} rank(cond)={int(pari.matrank(A))} dimK={k}"]
for name, ns in (("C1", c1), ("C1-squarefree>1", sqf), ("C1-primes", prm), ("Mordell-classes", mord)):
    r, first = rank_on(ns)
    out.append(f"  rank of K on {name} (n<=B, {len(ns)} indices) = {r}" + (f"  first nonzero n = {first}" if first else ""))
out.append(f"  time {time.time()-t0:.1f}s (coefs {t1-t0:.1f}s)")
print("\n".join(out), flush=True)
