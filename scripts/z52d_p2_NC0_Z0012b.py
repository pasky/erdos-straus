"""Z0012 (corrected normalisation): ES over A = F_5[E minus O], E: y^2 = x^3+x+1, numerator 4, denominators normalised by
their Laurent leading coefficient at O (uniformiser t = x/y; x ~ t^-2, y ~ -t^-3), i.e. lead_O(u+vy) = lc(u) if 2deg u > 2deg v+3,
else -lc(v).  Units F_5^* are the only scalars; without normalisation 4/P = 1/(P/4) is trivial (4 is a unit).
Question: for principal primes P (N(P) irreducible; all four generators c*P, c in F_5^*) and X,Y,Z with lead_O = 1 and ord <= MX,
does 4/P = 1/X+1/Y+1/Z hold?  Leading-term prediction (PROVED sketch): all terms have leading coefficient 1 at O, so the
coefficient of t^{e_min} is k in {1,2,3} (k = multiplicity of the minimal order); matching 4/P forces lead_O(P) = 4/k in {4,2,3}.
So solutions can only exist for lead_O(P) in {2,3,4} and never for lead_O(P)=1.
Usage: python3 scripts/z52d_p2_NC0_Z0012b.py MP MX"""
import sys, collections, time
sys.argv_ = sys.argv
import importlib.util
spec = importlib.util.spec_from_file_location('z12', 'scripts/z52d_p2_NC0_Z0012.py')
Z = importlib.util.module_from_spec(spec); spec.loader.exec_module(Z)
E = Z.E; Q = Z.Q
def lead_O(a):
    if not a[0] and not a[1]: return 0
    du = 2 * (len(a[0]) - 1) if a[0] else -1
    dv = 2 * (len(a[1]) - 1) + 3 if a[1] else -1
    return a[0][-1] if du > dv else (-a[1][-1]) % Q
def scale(c, a): return Z.esc(c, a)
MP = int(sys.argv[1]) if len(sys.argv) > 1 else 5
MX = int(sys.argv[2]) if len(sys.argv) > 2 else 4
t0 = time.time()
# principal primes up to units (use Z.principal_primes, which returns one generator per ideal normalised by lead(.)=1 in the old
# convention; we re-derive the ideal list from the norm instead, then take all four generators)
ideals = {}
for a in Z.all_elems(MP):
    n = Z.enorm(a)
    if len(n) - 1 < 1 or not Z.irreducible_poly(n): continue
    key = tuple(n)
    ideals.setdefault(key, []).append(a)
# each irreducible norm g determines the ideal (pi) up to units only if g is irreducible and (pi) prime: take all generators
gens = []
seen = set()
for key, lst in ideals.items():
    for a in lst:
        for c in range(1, Q):
            b = scale(c, a)
            t = (tuple(b[0]), tuple(b[1]))
            if t in seen: continue
            seen.add(t); gens.append(b)
print(f"principal-prime generators (all four units, N irreducible, ord<={MP}): {len(gens)}  ideals(distinct norms): {len(ideals)}  t={time.time()-t0:.1f}s", flush=True)
cands = [a for a in Z.all_elems(MX) if lead_O(a) == 1]
print(f"normalised denominators with ord<={MX}: {len(cands)}", flush=True)
tab = collections.Counter()
ex = {}
for P in gens:
    cP = lead_O(P)
    found = None
    for i, X in enumerate(cands):
        for Y in cands[i + 1:]:          # X != Y (distinct); Z may equal X or Y
            XY = Z.emul(X, Y)
            D = Z.eadd(Z.esc(4, XY), Z.esc(Q - 1, Z.emul(P, Z.eadd(X, Y))))
            if Z.is_zero(D): continue
            Nn = Z.emul(P, XY)
            W = Z.divides_A(D, Nn)
            if W is None or Z.is_zero(W): continue
            if lead_O(W) != 1: continue
            found = (X, Y, W); break
        if found: break
    tab[(cP, found is not None)] += 1
    if found and cP not in ex: ex[cP] = (P, found)
print("lead_O(P) -> (has normalised ES witness, count):", dict(sorted(tab.items())), flush=True)
for c, (P, w) in sorted(ex.items()):
    X, Y, W = w
    lhs = Z.esc(4, Z.emul(Z.emul(X, Y), W)); rhs = Z.emul(P, Z.eadd(Z.eadd(Z.emul(X, Y), Z.emul(Y, W)), Z.emul(X, W)))
    assert lhs == rhs
    print(f"  example lead_O(P)={c}: P={P} X={X} Y={Y} Z={W}  (identity verified)", flush=True)
print(f"time {time.time()-t0:.1f}s")
