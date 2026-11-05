#!/usr/bin/env python3
"""z59 WALDS: diagnose a level where the T1-kernel does NOT vanish on C1 (found by z59_walds_halfint.py).
Computes the cusp space S_{3/2}(Gamma_0(L), (D/.)), the exact kernel K of the T1 rows g(m^2) = 0 (all odd m <= sqrt B),
the subspace of K that is non-zero on C1 (modulo forms vanishing on C1 up to B), and for a survivor f the implied
Shimura eigenvalues lambda_l = a(t l^2)/a(t) + psi(l)(-t/l) at the first non-zero C1 index t (valid when f is a
T(l^2)-eigenform; checked by the consistency across two anchors t). Lists the C1 indices n <= B where f != 0, flags
the Mordell classes and the known R-zeros / a=1 (Lopez-line) zeros.
Usage: uv run --with cypari2 python scripts/z59_walds_diag.py L D B
"""
import sys
import cypari2

pari = cypari2.Pari()
pari.allocatemem(3_000_000_000)
L, D, B = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
N = L // 4
MORD = {1, 121, 169, 289, 361, 529}
ROOT = "/home/pasky/projects/math/erdos-straus-claude-agent-worktree-0044/"
RZ = set(int(x) for x in open(ROOT + "data/z58/screens/star_prime_zeros.txt") if x.strip() and x[0] != "#")
oddp = [int(q) for q in pari.factor(N)[0] if int(q) != 2] if N > 1 else []


def in_C1(n):
    return n % 8 == 1 and all(n % q and pow(n % q, (q - 1) // 2, q) == 1 for q in oddp)


mf = pari(f"mfinit([{L},3/2,{D}],1)")
C = pari.mfcoefs(mf, B)
k0 = int(pari.matsize(C)[1])
sub = pari("(C,r)->vecextract(C, apply(x->x+1, r), [1..matsize(C)[2]])")
rows = [m * m for m in range(1, int(B ** 0.5) + 1, 2)]
K = pari.matker(sub(C, rows))
c1 = [n for n in range(1, B + 1) if pari.gcd(n, 2 * N) == 1 and in_C1(n)]
M = sub(C, c1) * K                       # rows: C1 indices, cols: kernel basis
r = int(pari.matrank(M))
print(f"L={L} D={D} cusp dim={k0} dimK={int(pari.matsize(K)[1])} rank on C1 (n<=B={B}) = {r}")
if r == 0:
    sys.exit(0)
# pick a kernel vector v with non-zero C1 restriction
img = pari.matimage(pari.mattranspose(M))  # column space of M^T ~ combinations
kk = int(pari.matsize(K)[1])
for j in range(kk):
    col = [M[i, j] for i in range(len(c1))]
    if any(x != 0 for x in col):
        v = K[:, j] if False else pari.matsolve(pari.matid(kk), pari.matid(kk)[:, j]) if False else None
        jj = j
        break
f = C * K[:, jj] if False else pari("(C,K,j)->C*K[,j]")(C, K, jj + 1)  # coefficient column of the survivor
a = lambda n: f[n]
nz = [n for n in c1 if a(n) != 0]
print("non-zero C1 indices (first 30):", nz[:30])
print("of which in Mordell classes:", [n for n in nz if n % 840 in MORD][:20])
print("of which known (star)-zero primes:", [n for n in nz if n in RZ])
pr = [n for n in c1 if pari.isprime(n)]
prz = [n for n in pr if a(n) == 0]
print(f"C1 primes <= B: {len(pr)}; survivor coefficient = 0 at {len(prz)} of them (each such p has L(G (x) chi_p, 1/2) = 0 "
      f"by Waldspurger Cor. 2 with a non-zero anchor): {prz[:40]}")
print("  of which in Mordell classes:", [n for n in prz if n % 840 in MORD][:40])
t = nz[0]
psi = lambda l: int(pari.kronecker(D, l))
for t in nz[:2]:
    lam = {}
    for l in [int(q) for q in pari.primes([3, 60])]:
        if (2 * N * t) % l == 0 or t * l * l > B:
            continue
        lam[l] = a(t * l * l) / a(t) + psi(l) * int(pari.kronecker(-t, l))
    print(f"anchor t={t}: implied lambda_l:", {l: str(x) for l, x in lam.items()})
