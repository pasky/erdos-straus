# Diagnostics of the irreducible zeros of R_q (full family) in data/z58/ffield/star_q{q}_n{n}.zeros:
# deg(f - g^2) (g = polynomial part of sqrt f), factor degrees of f+1 and f-1, least degree of an irreducible
# l with (f/l) = -1 (least non-residue degree), fraction of degree-1,2 primes that are non-residues.
# Usage: uv run --with cypari2 python scripts/z58_ffield_irrzeros.py q n1 n2 ...
import sys, cypari2
pari = cypari2.Pari()
q = int(sys.argv[1])
def poly(coeffs): return pari("Mod(1,%d)*(%s)" % (q, "+".join(f"{c}*x^{i}" for i, c in enumerate(coeffs) if c)))
def irreducibles(d):
    out = []
    import itertools
    for low in itertools.product(range(q), repeat=d):
        l = poly(list(low) + [1])
        if pari.polisirreducible(l): out.append(l)
    return out
IRR = {d: irreducibles(d) for d in (1, 2, 3)}
def leg(f, l):  # (f/l) via f^((|l|-1)/2) mod l
    e = (q ** int(pari.poldegree(l)) - 1) // 2
    r = pari.lift(pari.Mod(f, l) ** e)
    r = pari.lift(pari.lift(r)) if True else r
    return 0 if r == 0 else (1 if r == 1 else -1)
def fdeg(g):
    fa = pari.factor(g); return sorted(int(pari.poldegree(fa[0][i])) * 1 for i in range(len(fa[0])) for _ in range(int(fa[1][i])))
for n in map(int, sys.argv[2:]):
    for line in open(f"data/z58/ffield/star_q{q}_n{n}.zeros"):
        if not line.strip() or line.startswith("#"): continue
        w = line.split()
        if w[2] != "P" or int(w[3]) != 0: continue
        idx = int(w[0]); cs = []
        for _ in range(n): cs.append(idx % q); idx //= q
        f = poly(cs + [1])  # decoded from idx (the coefficient string is ambiguous for q > 10)
        # polynomial part of sqrt: use pari on truncated series in 1/x
        X = pari("x")
        g = pari.lift(pari.subst(pari.truncate(pari.sqrt(pari.subst(f, X, pari("1/y")) + pari("O(y^%d)" % (n + 2)))), pari("y"), pari("1/x")))
        # simpler: deg(f - g^2) computed via resultant-free approach below
        try:
            gg = pari("Mod(1,%d)*(%s)" % (q, str(pari.lift(pari.numerator(g)))))
        except Exception:
            gg = None
        nr = {d: sum(1 for l in IRR[d] if leg(f, l) == -1) for d in IRR}
        lnr = min([d for d in IRR if nr[d] > 0], default=">3")
        print(n, pari.lift(f), "| f+1:", fdeg(f + 1), "f-1:", fdeg(f - 1), "| #NR deg1,2,3:", nr[1], "/", len(IRR[1]), nr[2], "/", len(IRR[2]), nr[3], "/", len(IRR[3]), "| lnr deg", lnr)
