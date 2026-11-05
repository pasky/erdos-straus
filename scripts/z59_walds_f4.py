#!/usr/bin/env python3
"""z59 WALDS: F1/F3/F4 screen for Gauss-exceptional eigensystems.

G runs over elliptic curves (rational weight-2 newforms) with conductor supported on {2,3,5,7}, root number +1 and
numerical analytic rank 2 (found by scripts/z59_walds_rank2_search.py). By Theorem W1 such G = phi (x) psibar chi_{-4}
are exactly the eigensystems that can survive T1 on C1(2N) (for suitable N, psi). For squarefree t in C1(2N), coprime to
cond(G), Waldspurger's twist at t is G (x) chi_t (chi_t = Kronecker character of Q(sqrt t), t = 1 mod 4).
Validity of a proxy supported on one such eigensystem requires L(G (x) chi_t, 1) = 0 at every R-zero t in C1(2N)
(Waldspurger Cor. 2, see memo Prop. W4). We compute root number and numerical analytic rank (pari ellanalyticrank,
not a certified computation) of G (x) chi_t for t = 1 (F1 sanity: must be rank >= 2), the 14 (star)-zero primes, the
squarefree composite zeros, and controls (non-zero primes in the same classes). Conductor cap 5e13 (else 'skip'); composites only t <= 30000; 8 controls.
Also pari ellrank [lo, hi]: lo >= 2 is a rigorous rank lower bound, hence (Gross-Zagier-Kolyvagin) analytic rank >= 2.

Usage: uv run --with cypari2 python scripts/z59_walds_f4.py
"""
import gzip, time
import cypari2

pari = cypari2.Pari()
pari.allocatemem(2_000_000_000)

CURVES = [(-27, 90), (36, 144), (6, 16), (-18, 8), (-56, 0), (-28, 112), (42, 92)]  # y^2 = x^3 + a x + b
MORD = {1, 121, 169, 289, 361, 529}
ROOT = "/home/pasky/projects/math/erdos-straus-claude-agent-worktree-0044/"
zp = [int(x) for x in open(ROOT + "data/z58/screens/star_prime_zeros.txt") if x.strip() and x[0] != "#"]
zc_all = [int(x) for x in gzip.open(ROOT + "data/z58/logic/zeros_1e10.txt.gz", "rt") if x.strip() and x[0] != "#"]
zc = [n for n in zc_all if not pari.isprime(n) and pari.issquarefree(n) and n > 1]


def in_C1(n, oddprimes):
    if n % 8 != 1:
        return False
    return all(n % q and pow(n % q, (q - 1) // 2, q) == 1 for q in oddprimes)


for a, b in CURVES:
    E = pari.ellinit([0, 0, 0, a, b])
    NE = int(pari.ellglobalred(E)[0])
    odd = [q for q in (3, 5, 7) if NE % q == 0]
    ar = pari.ellanalyticrank(E)
    print(f"# G: y^2 = x^3 + ({a})x + ({b}), conductor {NE} = {pari.factor(NE)}, rootno {pari.ellrootno(E)}, "
          f"analytic rank {ar[0]}, C1 = (n = 1 mod 8, QR mod {odd})", flush=True)
    zprime = [p for p in zp if in_C1(p, odd)]
    zcomp = [n for n in zc if in_C1(n, odd) and pari.gcd(n, NE) == 1 and n <= 30000]
    ctrl, p = [], 10007
    while len(ctrl) < 8:
        p = int(pari.nextprime(p + 1))
        if in_C1(p, odd) and p % 840 in MORD and p not in zp:
            ctrl.append(p)
    for tag, ts in (("t=1", [1]), ("zero-prime", zprime), ("zero-composite", zcomp), ("control-prime", ctrl)):
        for t in ts:
            if NE * t * t > 5 * 10 ** 13:
                print(f"  {tag:15s} t={t:<11d} skip (conductor > 5e13)")
                continue
            t0 = time.time()
            Et = E if t == 1 else pari.elltwist(E, t)
            w = int(pari.ellrootno(Et))
            r = pari.ellanalyticrank(Et)
            mord = "M" if t % 840 in MORD else "-"
            er = pari.ellrank(Et)  # [lower bound, upper bound, ...]; lower bound is rigorous (independent points found)
            print(f"  {tag:15s} t={t:<11d} {mord} rootno={w:+d} an.rank={int(r[0])} lead={float(r[1]):.6g} "
                  f"ellrank=[{int(er[0])},{int(er[1])}] ({time.time()-t0:.1f}s)", flush=True)
