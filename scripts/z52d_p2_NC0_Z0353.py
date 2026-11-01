"""Z0353: FF analogue of 'P-1 smooth' hardness. Engine: scripts/bs_ff_es.py (Lemma 1.3, A=T, Q=argv[2] default 5).
For each monic irreducible P of degree n not divisible by T, decide ES_5(T,P) (3 monic denominators); record failures.
Profile of P-1 (monic, same degree): number of irreducible factors (with multiplicity), largest irreducible factor degree,
and the degree-profile multiset; compare failing vs non-failing P.
Usage: python3 scripts/z52d_p2_NC0_Z0353.py NMAX"""
import sys, collections, time
sys.path.insert(0, 'scripts')
import bs_ff_es as E
E.Q = int(sys.argv[2]) if len(sys.argv) > 2 else 5
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 5
A = (0, 1)
t0 = time.time()
rows = []
for n in range(2, NMAX + 1):
    irr = [p for p in E.irreducibles(n) if E.divmod_(p, A)[1]]
    stats = collections.Counter()
    for p in irr:
        fail = next(E.es_solutions(A, p), None) is None
        Pm1 = list(p); Pm1[0] = (Pm1[0] - 1) % E.Q  # P-1 (monic, same degree)
        Pm1 = tuple(Pm1)
        if Pm1 == (0,) or len(Pm1) == 1:
            prof = ('const',)
        else:
            f = E.factor(E.trim(Pm1))
            prof = tuple(sorted(len(r) - 1 for r in f.keys() for _ in range(f[r])))
        key = (fail, prof)
        stats[key] += 1
    nf = sum(v for (f, _), v in stats.items() if f)
    print(f"n={n}: irreducible P (T∤P)={len(irr)} failing={nf} time={time.time()-t0:.1f}s", flush=True)
    # profile summary: largest irreducible-degree of P-1 among failing vs non-failing
    def big(prof): return max(prof) if prof and prof != ('const',) else 0
    def nfac(prof): return len(prof) if prof != ('const',) else 0
    for flag in (True, False):
        items = [(k, v) for k, v in stats.items() if k[0] == flag]
        tot = sum(v for _, v in items)
        if tot == 0: continue
        mean_fac = sum(nfac(k[1]) * v for k, v in items) / tot
        frac_irr = sum(1 for k, v in items if k[1] != ('const',) and len(k[1]) == 1 for _ in [0]) / max(1, len(items))
        frac_smooth = sum(v for k, v in items if big(k[1]) < n) / tot
        print(f"   {'FAIL' if flag else 'ok  '}: count={tot} mean #factors(P-1)={mean_fac:.3f} "
              f"frac(P-1 irreducible)={sum(v for k,v in items if len(k[1])==1)/tot:.3f} frac(P-1 not irreducible)={sum(v for k,v in items if len(k[1])!=1)/tot:.3f}",
              flush=True)
    rows.append((n, nf, len(irr)))
    byk = collections.defaultdict(lambda: [0, 0])
    for (f, prof), v in stats.items():
        k = len(prof) if prof != ('const',) else 0
        byk[k][0] += v if f else 0; byk[k][1] += v
    print("   fail rate by #factors(P-1):", {k: f"{a}/{b}" for k, (a, b) in sorted(byk.items())}, flush=True)
print("summary:", rows)

# ---- list failing P and factorisation of P-1 (only for n <= NMAX)
def fmt(p): return " + ".join(f"{c}T^{k}" if k else f"{c}" for k, c in enumerate(p) if c)
print("failing P (low->high coeffs) and factorisation of P-1 over F_5:")
for n in range(2, NMAX + 1):
    for p in [p for p in E.irreducibles(n) if E.divmod_(p, A)[1]]:
        if next(E.es_solutions(A, p), None) is None:
            Pm1 = list(p); Pm1[0] = (Pm1[0] - 1) % E.Q
            f = E.factor(E.trim(tuple(Pm1)))
            print(f"  n={n} P={list(p)} [{fmt(p)}]  P-1 = " + " * ".join(f"({fmt(r)})^{e}" for r, e in f.items()))

# ---- test: does failure coincide with 'P-1 has a root in F_Q' (i.e. P(a)=1 for some a in F_5)?
print("root test: P(a)=1 for some a in F_Q  (failing vs ok), n<=NMAX")
for n in range(2, NMAX + 1):
    irr = [p for p in E.irreducibles(n) if E.divmod_(p, A)[1]]
    c = collections.Counter()
    for p in irr:
        has_root = any(sum(c_ * pow(a, k, E.Q) for k, c_ in enumerate(p)) % E.Q == 1 for a in range(E.Q))
        fail = next(E.es_solutions(A, p), None) is None
        c[(fail, has_root)] += 1
    print(f"  n={n}: fail&root={c[(True,True)]} fail&noroot={c[(True,False)]} ok&root={c[(False,True)]} ok&noroot={c[(False,False)]}")
