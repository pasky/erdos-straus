# z70 GEN — registered runs of items 1–3 (Z70_GEN.md §1).  One JSON line per (n, d).
# usage: python scripts/z70_gen_run.py OUT d range P0 P1 [mod]   (primes p = 1 mod 24 in [P0, P1))
#        python scripts/z70_gen_run.py OUT d list n1 n2 ...
#   env Z70_ITEM3=0 disables item 3 (smooth orbits); Z70_P3 = prime bound for item 3 (default 50).
import sys, json, math, os, time
sys.path.insert(0, 'scripts')
import z70_gen_core as C
pari = C.pari

def units(vs, CG):
    """split a negation-closed set of vectors into singletons (2-torsion) and pairs (canonical representative)."""
    s, p = set(), set()
    for v in vs:
        w = CG.neg(v)
        if w == v: s.add(v)
        else: p.add(min(v, w))
    return s, p

def hyp(N, K, n):
    if N <= 1 or n == 0 or K == 0: return (n * K / N if N else 0.0), 0.0
    m = n * K / N
    v = n * (K / N) * (1 - K / N) * (N - n) / (N - 1)
    return m, v

def lognochance(N, K, n):
    # log P(no hit) for hypergeometric: C(N-n, K)/C(N, K)
    if K == 0 or n == 0: return 0.0
    if N - n < K: return float('-inf')
    return (math.lgamma(N - n + 1) - math.lgamma(N - n - K + 1)) - (math.lgamma(N + 1) - math.lgamma(N - K + 1))

def score(S, G, T, CG):
    """hits / null expectation / variance / P(no hit) for seed set S inside target T (all negation-closed)."""
    S = set(S) & T
    Ss, Sp = units(S, CG); Gs, Gp = units(G, CG); Ts, Tp = units(T, CG)
    hs = len(Ss & Gs); hp = len(Sp & Gp)
    m1, v1 = hyp(len(Ts), len(Gs), len(Ss)); m2, v2 = hyp(len(Tp), len(Gp), len(Sp))
    l0 = lognochance(len(Ts), len(Gs), len(Ss)) + lognochance(len(Tp), len(Gp), len(Sp))
    pnull = 1 - math.exp(l0) if l0 > float('-inf') else 1.0
    return dict(n=len(S), hit=hs + 2*hp, E=m1 + 2*m2, V=v1 + 4*v2, cov=int(hs + hp > 0), pcov=pnull)

def alpha_rates(G, T, CG):
    """P(unit good | half-octave bin of its minimal norm alpha) estimated over all target units (alpha-matched null)."""
    Ts, Tp = units(T, CG); tot = {}; good = {}
    for u in Ts | Tp:
        b = int(2 * math.log2(CG.byvec[u][0]))
        tot[b] = tot.get(b, 0) + 1
        if u in G: good[b] = good.get(b, 0) + 1
    return {b: good.get(b, 0) / tot[b] for b in tot}

def score_alpha(S, G, T, CG, rates):
    S = set(S) & T
    Ss, Sp = units(S, CG)
    hit = 0; E = 0.0; V = 0.0; l0 = 0.0; cov = 0
    for w, U in ((1, Ss), (2, Sp)):
        for u in U:
            rho = rates[int(2 * math.log2(CG.byvec[u][0]))]
            g = u in G
            hit += w * g; cov |= g
            E += w * rho; V += w * w * rho * (1 - rho)
            l0 += math.log(1 - rho) if rho < 1 else float('-inf')
    pc = 1 - math.exp(l0) if l0 > float('-inf') else 1.0
    return dict(n=len(S), hit=hit, E=E, V=V, cov=int(cov), pcov=pc)

def two_comp(v, CG):
    out = []
    for x, m in zip(v, CG.cyc):
        t = 1
        while m % (2*t) == 0: t *= 2
        out.append(x % t)
    return tuple(out)

def lift_root(q, r, k, N4):
    # root of x^2 = -N4 mod q^k (q odd, q not dividing N4), Hensel
    x = r; mod = q
    for _ in range(1, k):
        mod *= q
        x = (x - (x*x + N4) * pow(2*x, -1, mod)) % mod
    assert (x*x + N4) % mod == 0
    return x

def run_one(n, d, item3=True, P3=50):
    t0 = time.time()
    rec = dict(n=n, d=d, n840=n % 840)
    CG = C.ClassGroup(n, d); Gn = C.Genus(CG)
    rec.update(h=CG.h, cyc=CG.cyc)
    sols = C.solutions(n, d)
    G = set(); mnat = {}; NR = set()
    for s in sols:
        g = C.good_class(n, d, s); v = CG.vec(g); G.add(v)
        for (N, r) in C.natural_reps(n, d, s):
            NR.add((N, r % N)); NR.add((N, (-r) % N))
            mnat[v] = min(mnat.get(v, N), N)
    T = {v for v in CG.byvec if Gn.of(v) == Gn.target}
    assert G <= T
    rec.update(nsol=len(sols), G=len(G), T=len(T), genera=CG.h // len(T))
    # ---- item 2: 2-primary data
    r2 = sum(1 for m in CG.cyc if m % 2 == 0); r4 = sum(1 for m in CG.cyc if m % 4 == 0); r8 = sum(1 for m in CG.cyc if m % 8 == 0)
    rec.update(r2=r2, r4=r4, r8=r8)
    pos = {}
    for v in G:
        c = two_comp(v, CG); pos[str(c)] = pos.get(str(c), 0) + 1
    Tpos = {}
    for v in T:
        c = two_comp(v, CG); Tpos[str(c)] = Tpos.get(str(c), 0) + 1
    rec['pos'] = pos; rec['npos'] = len(Tpos); rec['Tpos_each'] = sorted(set(Tpos.values()))
    # ---- item 1: seed families (computed without G)
    fam = {}
    fam['AMB'] = {v for v in T if CG.is2tors(v)}
    fam['RED'] = {v for v in T if CG.is2power(v)}
    # least split prime ideal in each genus (search primes up to 20000)
    genus_min = {}
    qstar = None
    for (q, r) in C.split_primes(n, d, 20000):
        v = CG.vec(C.ideal_form(n, d, q, r)); gv = Gn.of(v)
        if gv not in genus_min: genus_min[gv] = (q, v)
        if len(genus_min) == len({Gn.of(u) for u in CG.byvec}): break
    if Gn.target in genus_min:
        qstar, vq = genus_min[Gn.target]
        cyc = set()
        for k in (1, 3, 5, 7, 9):
            cyc.add(CG.mul(k, vq)); cyc.add(CG.mul(-k, vq))
        fam['CYC'] = cyc
        # first entry along k = 1, 3, 5, ...
        fe = None
        for k in range(1, 4 * CG.h, 2):
            if CG.mul(k, vq) in G or CG.mul(-k, vq) in G: fe = k; break
        rec['cyc_first'] = fe; rec['qstar'] = qstar
        o = 1; x = vq
        while any(x): x = CG.add(x, vq); o += 1
        rec['cyc_ord'] = o
    base = {v for v in CG.byvec if CG.is2tors(v)}
    for gv, (q, v) in genus_min.items():
        base.add(v); base.add(CG.neg(v))
    fam['GEN2'] = {CG.add(x, y) for x in base for y in base}
    rec['fam'] = {k: score(S, G, T, CG) for k, S in fam.items()}
    rates = alpha_rates(G, T, CG)
    rec['famA'] = {k: score_alpha(S, G, T, CG, rates) for k, S in fam.items()}
    # data for the pooled exact-alpha null and the hit decomposition (added before W3; does not change registered stats)
    Ts, Tp = units(T, CG); ah = {}
    for w, U in ((1, Ts), (2, Tp)):
        for u in U:
            al = CG.byvec[u][0]
            if al <= 5000:
                x = ah.setdefault(al, [0, 0]); x[0] += 1; x[1] += (u in G)
    rec['ahist'] = ah
    seedinfo = {}
    for k, S in fam.items():
        Ss, Sp = units(set(S) & T, CG); lst = []
        for w, U in ((1, Ss), (2, Sp)):
            for u in U:
                al = CG.byvec[u][0]
                lst.append([al, w, int(u in G), mnat.get(u, 0)])
        seedinfo[k] = lst
    rec['seeds'] = seedinfo
    rec['base_primes'] = sorted(q for gv, (q, v) in genus_min.items())
    # ---- item 3: P3-smooth split ideals of norm <= X (amended after smoke test: X = min(dn, 64 sqrt(dn)),
    #      cumulative profile at thresholds sqrt(dn) * 2^j, j = -4..6)
    if item3:
        N4 = d * n; rt = math.isqrt(N4)
        X = min(N4, 64 * rt)
        sp = C.split_primes(n, d, P3)
        opts = []
        for q, r in sp:
            lst = []; qk = q; k = 1
            while qk <= X:
                x = lift_root(q, r, k, N4)
                lst.append((qk, x)); lst.append((qk, (-x) % qk))
                k += 1; qk *= q
            opts.append(lst)
        seeds = []   # (N, v, isI) for seeds whose class lies in T
        cnt = 0; frviol = 0
        def dfs(i, N, r):
            nonlocal cnt, frviol
            if i == len(opts):
                if N == 1: return
                cnt += 1
                v = CG.vec(C.ideal_form(n, d, N, r % N))
                if v not in T: return
                isI = v in G and (N, r % N) in NR
                if v in G and not isI and N * mnat[v] < N4: frviol += 1
                seeds.append((N, v, isI))
                return
            dfs(i + 1, N, r)
            for (qk, x) in opts[i]:
                if N * qk > X: continue
                rr = int(pari.chinese(pari.Mod(r, N), pari.Mod(x, qk)).lift()) if N > 1 else x
                dfs(i + 1, N * qk, rr)
        dfs(0, 1, 0)
        seeds.sort()
        Iall = {v for (N, v, isI) in seeds if isI}
        firstI = min((N for (N, v, isI) in seeds if isI), default=None)
        firstIII = min((N for (N, v, isI) in seeds if (v in G and not isI)), default=None)
        prof = {}
        rates3 = alpha_rates(G - Iall, T - Iall, CG)
        for j in range(-4, 7):
            Xj = rt * 2.0**j
            if Xj > X: break
            Ij = {v for (N, v, isI) in seeds if isI and N <= Xj}
            Rj = {v for (N, v, isI) in seeds if N <= Xj}
            Cres = Rj - Iall
            sc = score(Cres, G - Iall, T - Iall, CG)
            sa = score_alpha(Cres, G - Iall, T - Iall, CG, rates3)
            prof[j] = dict(I=len(Ij), reach=len(Rj), n=sc['n'], hit=sc['hit'], E=sc['E'], V=sc['V'], EA=sa['E'], VA=sa['V'])
        rec['it3'] = dict(nseeds=cnt, nT=len(seeds), X=X, Icl=len(Iall), firstI=firstI, firstIII=firstIII,
                          frviol=frviol, minnat=(min(mnat.values()) if mnat else None), prof=prof)
    rec['sec'] = round(time.time() - t0, 2)
    return rec

if __name__ == '__main__':
    out, d, mode = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    item3 = os.environ.get('Z70_ITEM3', '1') == '1'; P3 = int(os.environ.get('Z70_P3', '50'))
    if mode == 'range':
        P0, P1 = int(sys.argv[4]), int(sys.argv[5])
        ns = [int(p) for p in pari.primes([P0, P1]) if int(p) % 24 == 1]
    else:
        ns = [int(x) for x in sys.argv[4:]]
    with open(out, 'a') as fo:
        for n in ns:
            if n % d == 0 and d > 1: continue
            try:
                rec = run_one(n, d, item3, P3)
            except ValueError as ex:
                rec = dict(n=n, d=d, skipped=str(ex))
            fo.write(json.dumps(rec) + '\n'); fo.flush()
