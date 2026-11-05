#!/usr/bin/env python3
"""z59 WALDS: Gauss-exceptional scan (Theorem W1 / Cor W2).

For every weight-2 newform phi of trivial character and level M (M in the given list), every complex embedding, and
every negative fundamental discriminant D' in the given list, compute the central value L(phi (x) chi_{D'}, 1) and the
root number of the twist (pari lfuntwist / lfunrootres; numerical, realprecision 38). By Theorem W1, phi can carry a
non-zero coefficient of a T1-valid proxy (nebentypus psi with psi*chi_{-4} = chi_{D'}) at a squarefree n in C1(2N)
only if L(phi (x) chi_{D'}, 1) = 0 ("Gauss-exceptional").

Usage: uv run --with cypari2 python scripts/z59_walds_gauss.py "M1,M2,..." "D1,D2,..."
Output: one line per (M, newform orbit, embedding, D'): M orbit dim emb D' rootno L(1)  [flag]
"""
import sys, time
import cypari2

pari = cypari2.Pari()
pari.allocatemem(2_000_000_000)
pari.default("realprecision", 38)

Ms = [int(x) for x in sys.argv[1].split(",")]
Ds = [int(x) for x in sys.argv[2].split(",")]
twist = pari("(L,D)->lfuntwist(L,D)")
rootno = pari("(L)->lfunrootres(L)[3]")
nexc = 0
for M in Ms:
    mf = pari(f"mfinit([{M},2],0)")
    if int(pari.mfdim(mf)) == 0:
        continue
    eig = pari.mfeigenbasis(mf)
    for io, F in enumerate(eig):
        Ls = pari.lfunmf(mf, F)
        # lfunmf returns one L-datum (rational coefficients; its 2nd entry is an integer) or a vector over embeddings
        Lv = [Ls] if pari.type(Ls[1]) != "t_VEC" else list(Ls)
        for ie, Lf in enumerate(Lv):
            for D in Ds:
                t0 = time.time()
                Lt = twist(Lf, D)
                v = pari.lfun(Lt, 1)
                w = rootno(Lt)
                av = abs(complex(v))
                flag = ""
                if av < 1e-12:
                    flag = "ZERO"
                    nexc += 1
                print(f"{M} orb{io} emb{ie} D'={D} rootno={complex(w).real:+.0f}{complex(w).imag:+.0e}i |L(1)|={av:.6e} {flag} ({time.time()-t0:.1f}s)", flush=True)
print(f"# done; zero central values: {nexc}")
