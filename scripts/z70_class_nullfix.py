# z70 CLASS — corrected symmetry-preserving nulls (after the internal review found that PSC's BFS overwrite broke DL identities
# and CS self-loops, and that PSF skipped rows without a +-1 coefficient).  Pre-registered in Z70_CLASS.md §1.9.
# Variables: the classes x_q of the prime ideals Q_q (least root) for every prime q in the good e-ideal norms and in the norms
# N_a of the imposed fibres.  Every ideal class is computed multiplicatively from the x_q, so EVERY ideal identity (DL, DL',
# REP-ID) holds in every replicate by construction.  Imposed linear relations (one per imposed fibre a):
#     sum_q k_q x_q = T_d     ((2ad + sqrt(-dn)) = D_d * B_a, B_a = prod Q_q^{k_q}; Lemma Phi(iii)),
#   mode CS : the fibres containing a solution with 4ad | n - 1 (these relations are exactly Lemma CS, incl. self-loops A = e);
#   mode ALL: every active fibre (a = first letter of a solution).
# Solver: integer Gauss-Jordan elimination with +-1 pivots, repeated passes until stable; rows left with only non-unit
#   coefficients have all their variables FROZEN at the real classes (so the row holds); fixed variables (q <= 50,
#   translation primes) are real.  Free variables: q <= max good prime -> genus- and size-matched prime swap (injection);
#   larger q -> uniform class in the genus coset of x_q.  Pivots are then solved exactly (coefficient +-1).
# Every replicate is checked: every imposed ORIGINAL fibre equation is asserted.
# Power: for each statistic the number of n whose null variance is > 0 is reported (n with zero variance contribute nothing).
# Mode ALLF (post hoc diagnostic, after the registered FIX-ALL runs): as ALL, but pivots are never primes of good norms; rows
#   whose only unit coefficients sit on good primes are frozen at the real classes.  Purpose: test whether the negative
#   deviations of FIX-ALL come from pivot-solved small good ideals losing their free-region protection (Lemma FR).
# Mode ALLS (post hoc, final pass, after review round 3): as ALL, but no prime of any SMALL natural representative
#   (A-, B- or de-side, norm^2 < dn) is ever a pivot, so all small natural representatives are built from swapped / fixed /
#   frozen prime classes and keep the free-region protection of the real ones (Lemma FR, Cor. FR').
# Usage: python scripts/z70_class_nullfix.py MODE d R seed range P0 P1 [mod res] | list n1 ...
import sys, math, random, os
MATCH2 = os.environ.get('Z70_MATCH2') == '1'   # post hoc: swap only to primes with the same 2-Sylow projection of the class
DIAG = os.environ.get('Z70_DIAG') == '1'   # post hoc diagnostic (final pass): split ideal-pair coincidences by whether an
# ideal involves a pivot-solved or uniformly drawn ("solved") prime class
sys.path.insert(0, 'scripts')
from collections import Counter
from sympy import factorint, primerange
from z70_class_core import Fact, ClassData, solutions, good_ideals
from z70_class_null import stats, translations, SplitPrimes, QFIX, SS

def analyse(n, d, R, rng, F, mode):
    sols = solutions(n, d, F)
    gi = good_ideals(n, d, F, sols)
    if not gi: return dict(n=n, d=d, k=0)
    if any(math.gcd(x, d*n) > 1 for (a, b, c, e) in sols for x in (e, 4*a*c*d - 1)): return dict(n=n, d=d, k=-1)
    C = ClassData(n, d); G = C.G
    vk = {}
    for (e, rho) in gi:
        v = tuple(C.ideal_vector(e, rho, F)); vk[v] = 1; vk[tuple((q, -k) for q, k in v)] = 1
    vecs = list(vk)
    Xobs = [C.vec_class(v) for v in vecs]
    if len(set(Xobs)) < 2: return dict(n=n, d=d, k=len(set(Xobs)))
    tl, tlp = translations(C)
    obs = stats(G, Xobs, tl)
    fib = {}
    for (a, b, c, e) in sols:
        if a in fib: continue
        if mode == 'CS' and not any((n - 1) % (4*a2*d) == 0 for (a2, _, _, _) in sols if a2 == a): continue
        Na = n + 4*a*a*d; A = 4*a*c*d - 1; assert A*e == Na
        fac = dict(F.factor(e))
        for q, k in factorint(A).items(): fac[q] = fac.get(q, 0) + k
        vec = []
        for q, k in sorted(fac.items()):
            r, _ = C.prime_class(q); rr = (2*a*d) % q; assert rr in (r, q - r)
            vec.append((q, k if rr == r else -k))
        assert C.vec_class(vec) == C.Td, (n, d, a)
        fib[a] = vec
    goodprimes = sorted(set(q for v in vecs for q, _ in v))
    allprimes = sorted(set(q for v in fib.values() for q, _ in v) | set(goodprimes))
    fixed = set(q for q in allprimes if q <= QFIX) | set(tlp)
    gp = set(goodprimes)
    # ALLS: primes of every SMALL natural representative (A-, B- or de-side norm N with N^2 < dn) are never pivots
    smallp = set()
    if mode == 'ALLS':
        for (a, b, c, e) in sols:
            for N in (4*a*c*d - 1, 4*b*c*d - 1):
                if N*N < d*n: smallp |= set(F.factor(N)) if N <= F.N else set(factorint(N))
            if (d*e)**2 < d*n: smallp |= set(F.factor(e))
    def gmul(x, m):
        y = G.one; c = x if m > 0 else G.negd[x]
        for _ in range(abs(m)): y = G.add(y, c)
        return y
    realc = {q: C.prime_class(q)[1] for q in allprimes}
    cons = []
    for a, v in fib.items():
        rhs = C.Td; co = {}
        for q, k in v:
            if q in fixed: rhs = G.add(rhs, gmul(realc[q], -k))
            else: co[q] = co.get(q, 0) + k
        cons.append([co, rhs])
    pivot_of = {}            # row index -> (q, coef)
    pivset = set()
    changed = True
    while changed:
        changed = False
        for i in range(len(cons)):
            if i in pivot_of: continue
            co, rhs = cons[i]
            cands = [q for q, k in co.items() if abs(k) == 1 and q not in pivset and not (mode == 'ALLF' and q in gp)
                     and not (mode == 'ALLS' and q in smallp)]
            if not cands: continue
            q = max(cands, key=lambda q: (q not in gp, q)); kq = co[q]
            for j in range(len(cons)):
                if j == i: continue
                cj, rj = cons[j]; m = cj.get(q, 0)
                if m == 0: continue
                f = -m * kq
                for qq, kk in co.items():
                    cj[qq] = cj.get(qq, 0) + f * kk
                    if cj[qq] == 0: del cj[qq]
                cons[j][1] = G.add(rj, gmul(rhs, f))
            pivot_of[i] = (q, kq); pivset.add(q); changed = True
    frozen = set(); nfrozenrows = 0
    for i in range(len(cons)):
        if i in pivot_of: continue
        co, rhs = cons[i]
        if co:
            nfrozenrows += 1; frozen |= set(co)
        else:
            assert rhs == G.one, (n, d, 'inconsistent empty row')
    # a frozen variable must not be a pivot (pivots were eliminated from all other rows, so they cannot occur here)
    assert not (frozen & pivset)
    free = [q for q in allprimes if q not in fixed and q not in frozen and q not in pivset]
    QPOOL = max(goodprimes)
    swap = [q for q in free if q <= QPOOL]; big = [q for q in free if q > QPOOL]
    SP = SplitPrimes(n, d, int(QPOOL * 1.6) + 100) if swap else None
    pools = {q: SP.pool(q) for q in swap}
    if MATCH2:
        m2 = G.h
        while m2 % 2 == 0: m2 //= 2
        def proj(q):
            x = C.prime_class(q)[1]; y = G.one
            for _ in range(m2): y = G.add(y, x)
            return y
        for q in swap:
            pq = proj(q); dl = 0.1; P = []
            while len(P) < 8 and dl <= 3:
                P = [x for x in SP.pool(q, delta=dl, kmin=8) if proj(x) == pq]; dl *= 1.5
            pools[q] = P if P else [q]
    H = set(G.add(u, u) for u in G.coords.values()); Hl = sorted(H)
    acc = {s: [] for s in SS}; first = None; varied = [False]*len(vecs)
    solved = [any(q in pivset or q in big for q, _ in v) for v in vecs]
    def pairsplit(Y):
        out = Counter(); idx = {}
        for i, y in enumerate(Y): idx.setdefault(y, []).append(i)
        for i, y in enumerate(Y):
            for j in idx[y]:
                if j > i: out['coll_' + ('S' if solved[i] or solved[j] else 'P')] += 1
            for t in tl:
                z = G.add(y, t)
                for j in idx.get(z, ()):
                    if j != i: out['L3_' + ('S' if solved[i] or solved[j] else 'P')] += 1
        return out
    dobs = pairsplit(Xobs) if DIAG else None; dnull = Counter()
    for _ in range(R):
        cls = {q: realc[q] for q in allprimes if q in fixed or q in frozen}
        used = set(fixed) | set(frozen)
        for q in rng.sample(swap, len(swap)):
            cand = [x for x in pools[q] if x not in used]
            if not cand and MATCH2: cand = [q] if q not in used else []
            if not cand: cand = [x for x in SP.pool(q, delta=1.0, kmin=len(used) + 8) if x not in used]
            x = rng.choice(cand); used.add(x); cls[q] = C.prime_class(x)[1]
        for q in big: cls[q] = G.add(realc[q], rng.choice(Hl))
        for i, (q, kq) in pivot_of.items():
            co, rhs = cons[i]; rest = G.one
            for qq, kk in co.items():
                if qq != q: rest = G.add(rest, gmul(cls[qq], kk))
            val = G.add(rhs, G.negd[rest]); cls[q] = val if kq > 0 else G.negd[val]
        for a, v in fib.items():   # every imposed ORIGINAL equation holds in this replicate
            tot = G.one
            for q, k in v: tot = G.add(tot, gmul(cls[q], k))
            assert tot == C.Td, (n, d, a, 'imposed fibre equation violated')
        def vc(v):
            x = G.one
            for q, k in v: x = G.add(x, gmul(cls[q], k))
            return x
        Y = [vc(v) for v in vecs]
        if first is None: first = Y
        else: varied = [vv or (y != f_) for vv, y, f_ in zip(varied, Y, first)]
        st = stats(G, Y, tl)
        for k_ in SS: acc[k_].append(st[k_])
        if DIAG: dnull.update(pairsplit(Y))
    nullst = {k_: (sum(v)/R, (sum(x*x for x in v)/R - (sum(v)/R)**2) ** 0.5) for k_, v in acc.items()}
    return dict(n=n, d=d, h=G.h, k=obs['K'], NI=len(vecs), obs=obs, null=nullst, nfib=len(fib), frozen=len(frozen),
                frows=nfrozenrows, nvar=sum(varied), l0=tlp[0] if tlp else None,
                dobs=dobs, dnull={k: v/R for k, v in dnull.items()} if DIAG else None)

def run(mode, d, R, nlist, F, seed, out=sys.stdout, tag=''):
    rng = random.Random(seed)
    agg = {s: [0.0, 0.0] for s in SS}; npr = 0; tot = Counter(); powr = Counter(); skipped = Counter()
    for n in nlist:
        o = analyse(n, d, R, rng, F, mode)
        if 'obs' not in o:
            skipped['gcd' if o['k'] == -1 else 'small'] += 1
            print(f"n={n} d={d} k={o['k']} (skipped)", file=out, flush=True); continue
        npr += 1; ob = o['obs']
        line = (f"n={n} d={d} h={o['h']} NI={o['NI']} k={o['k']} fibres={o['nfib']} frozen_rows={o['frows']} frozen_vars={o['frozen']} "
                f"varied={o['nvar']}/{o['NI']} l0={o['l0']} |")
        for s in SS:
            mu, sd = o['null'][s]; line += f" {s} {ob[s]} ({mu:.3f}±{sd:.3f})"
            agg[s][0] += ob[s] - mu; agg[s][1] += sd*sd; tot['obs_'+s] += ob[s]; tot['null_'+s] += mu
            powr[s] += sd > 0
        for k in ('nfib', 'frozen', 'frows', 'nvar', 'NI'): tot[k] += o[k]
        if DIAG:
            for k in ('coll_S', 'coll_P', 'L3_S', 'L3_P'): tot['dobs_' + k] += o['dobs'][k]; tot['dnull_' + k] += o['dnull'].get(k, 0)
        print(line, file=out, flush=True)
    Z = lambda a: a[0]/math.sqrt(a[1]) if a[1] > 0 else float('nan')
    print(f"# {tag} null=FIX-{mode}{'(MATCH2)' if MATCH2 else ''} d={d} n analysed {npr} (skipped: {dict(skipped)}); R={R}; seed={seed}; imposed fibres {tot['nfib']}, "
          f"frozen rows {tot['frows']} (vars {tot['frozen']}); ideal-class variability {tot['nvar']}/{tot['NI']}; "
          f"n with null variance > 0: " + ', '.join(f"{s} {powr[s]}" for s in ('Mx', 'Ex', 'L1', 'L3', 'C0', 'A2')), file=out)
    if DIAG:
        print(f"# {tag} DIAG ideal-pair coincidences, observed vs null mean, split by involvement of a solved class (S) or not (P): " +
              '; '.join(f"{k} obs {tot['dobs_'+k]} null {tot['dnull_'+k]:.1f}" for k in ('coll_S', 'coll_P', 'L3_S', 'L3_P')), file=out)
    print(f"# {tag} null=FIX-{mode} d={d} EXACT sums: " + '; '.join(f"{s} excess {agg[s][0]:+.4f} var {agg[s][1]:.4f}" for s in SS), file=out)
    print(f"# {tag} null=FIX-{mode} d={d}: " + "; ".join(f"Z_{s} = {Z(agg[s]):+.2f} (obs {tot['obs_'+s]:.0f}, null {tot['null_'+s]:.1f})" for s in SS), file=out, flush=True)

if __name__ == "__main__":
    mode = sys.argv[1]; d = int(sys.argv[2]); R = int(sys.argv[3]); seed = int(sys.argv[4]); spec = sys.argv[5:]
    assert mode in ('CS', 'ALL', 'ALLF', 'ALLS')
    if spec[0] == 'range':
        P0, P1 = int(spec[1]), int(spec[2])
        mod, res = (int(spec[3]), int(spec[4])) if len(spec) > 4 else (8, 1)
        nl = [p for p in primerange(P0, P1) if p % mod == res]
    else:
        nl = sorted(set(int(x) for x in spec[1:]))
    F = Fact(max(nl)//3 + 10)
    run(mode, d, R, nl, F, seed=seed, tag=' '.join(spec[:3]))
