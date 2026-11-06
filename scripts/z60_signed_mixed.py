#!/usr/bin/env python3
"""z60 SIGNED: mixed-nebentypus T1-kernel and validity certificate (Theorem S2 test, Prop S5 data).

Space: V = direct sum over all quadratic psi = (D/.) (D = 1 or a positive fundamental discriminant dividing L) of
M_{3/2}(Gamma_0(L), psi) (pari mfinit flag `space`: 4 full, 1 cusp).  A mixed proxy is g = sum_psi g_psi.
Rows (linear conditions on g):
  * T1: g(m^2) = 0 for every odd m <= sqrt(B)            (l0 = 0; legitimate on the full space)
         or only for odd m with gcd(m, 2N) = 1              (l0 = -1; for the cusp space / TERNARY class)
  * optional zrows=1: g(z) = 0 at every known R-zero z <= B (data/z58/logic/zeros_1e10.txt.gz; all n = 1 (4) with R = 0)
    (cusp space: only zeros in C1(2N) coprime to 2N, as in z59_walds_halfint.py)
Output: dim V, rank of the mixed kernel K restricted to n in C1(2N) (n <= B, gcd(n,2N)=1), and for comparison the
sum over psi of the per-psi kernel ranks on C1.  If zrows=1 and rank on C1 = 0: every valid mixed proxy in V
vanishes on C1(2N) cap [1, B] (CERTIFIED, exact rational linear algebra).
Optionally dumps the C1-restricted kernel (basis of the mixed T1-kernel restricted to C1) to a file.

Usage: uv run --with cypari2 python scripts/z60_signed_mixed.py L B l0 space zrows [dumpfile]
"""
import sys, time, gzip, pathlib
import cypari2

pari = cypari2.Pari()
pari.allocatemem(2_500_000_000)
L, B, l0, SPACE, ZROWS = (int(x) for x in sys.argv[1:6])
DUMP = sys.argv[6] if len(sys.argv) > 6 else None
N = L // 4
ROOT = str(pathlib.Path(__file__).resolve().parents[1]) + "/"


def fund(D):
    if D == 1:
        return True
    if D % 4 == 1:
        return all(D % (p * p) for p in range(2, int(D ** .5) + 1))
    if D % 4 == 0:
        m = D // 4
        return m % 4 in (2, 3) and all(m % (p * p) for p in range(2, int(m ** .5) + 1))
    return False


oddN = [int(q) for q in pari.factor(N)[0]] if N > 1 else []
oddN = [q for q in oddN if q != 2]


def in_C1(n):
    if n % 8 != 1:
        return False
    for q in oddN:
        r = n % q
        if r == 0 or pow(r, (q - 1) // 2, q) != 1:
            return False
    return True


t0 = time.time()
Ds = [D for D in range(1, L + 1) if L % D == 0 and fund(D)]
blocks = []
for D in Ds:
    mf = pari(f"mfinit([{L},3/2,{D}],{SPACE})")
    d = int(pari.mfdim(mf))
    if d == 0:
        continue
    blocks.append((D, d, pari.mfcoefs(mf, B)))
sub = pari("(C,r)->vecextract(C, apply(x->x+1, r), [1..matsize(C)[2]])")
C = pari.matconcat(pari.Vec([b[2] for b in blocks]))  # (B+1) x dimV
dimV = int(pari.matsize(C)[1])
if l0 == 0:
    rows = [m * m for m in range(1, int(B ** .5) + 1, 2)]
else:
    rows = [m * m for m in range(1, int(B ** .5) + 1, 2) if pari.gcd(m, 2 * N) == 1]
zs = []
if ZROWS:
    zs = sorted(int(x) for x in gzip.open(ROOT + "data/z58/logic/zeros_1e10.txt.gz", "rt")
                if x.strip() and x[0] != "#" and int(x) <= B)
    if SPACE != 4:
        zs = [z for z in zs if pari.gcd(z, 2 * N) == 1 and in_C1(z)]
allrows = sorted(set(rows) | set(zs))
c1 = [n for n in range(1, B + 1) if pari.gcd(n, 2 * N) == 1 and in_C1(n)]


def kernel_rank(Cm, rws):
    K = pari.matker(sub(Cm, rws))
    k = int(pari.matsize(K)[1])
    if k == 0:
        return 0, K, k
    return int(pari.matrank(sub(Cm, c1) * K)), K, k


r_mixed, K, k = kernel_rank(C, allrows)
per = []
for D, d, Cb in blocks:
    r, _, kb = kernel_rank(Cb, allrows)
    per.append((D, d, kb, r))
print(f"L={L} N={N} space={SPACE} l0={l0} zrows={ZROWS} B={B} #psi={len(blocks)} dimV={dimV} #rows={len(allrows)} "
      f"(#zero rows={len(zs)}) dimK={k}  rank(K on C1, {len(c1)} idx) = {r_mixed};  "
      f"sum of per-psi ranks = {sum(p[3] for p in per)}  per-psi(D:dim,dimK,rankC1) = "
      + " ".join(f"{D}:{d},{kb},{r}" for D, d, kb, r in per) + f"  time {time.time()-t0:.0f}s", flush=True)
if DUMP and r_mixed:
    M = sub(C, c1) * K
    # reduce to a basis of the row space restricted to C1 (columns = kernel vectors)
    Mt = pari.mattranspose(M)
    H = pari.matimage(M)  # columns spanning the image (C1-restricted functions)
    with open(DUMP, "w") as f:
        f.write(f"# L={L} space={SPACE} l0={l0} zrows={ZROWS} B={B}; columns = basis of C1-restrictions of the mixed T1-kernel\n")
        f.write("# n " + " ".join(f"v{j}" for j in range(int(pari.matsize(H)[1]))) + "\n")
        for i, n in enumerate(c1):
            f.write(f"{n} " + " ".join(str(H[i, j]) for j in range(int(pari.matsize(H)[1]))) + "\n")
