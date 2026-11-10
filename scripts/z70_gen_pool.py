# z70 GEN — pooling of run_*.jsonl (items 1–3).  usage: python3 scripts/z70_gen_pool.py FILE [FILE ...]
import sys, json, math, collections, os
M840 = {1, 121, 169, 289, 361, 529}

def load(files):
    recs = []
    for f in files:
        for l in open(f):
            r = json.loads(l)
            if 'skipped' in r: continue
            recs.append(r)
    keys = [(r['n'], r['d']) for r in recs]
    assert len(keys) == len(set(keys)), 'duplicate (n, d) records in input'
    return recs

def z(h, E, V):
    return (h - E) / math.sqrt(V) if V > 0 else float('nan')

def item1(recs, label):
    out = []
    for key in [k for k in ('fam', 'famA', 'famAC') if k in recs[0]]:
        for F in ('AMB', 'RED', 'CYC', 'GEN2'):
            H = E = V = cov = pc = pcv = 0.0; n = 0; nG = 0; covG = 0; frac = 0.0
            for r in recs:
                if F not in r[key]: continue
                s = r[key][F]; n += 1
                H += s['hit']; E += s['E']; V += s['V']
                cov += s['cov']; pc += s['pcov']; pcv += s['pcov'] * (1 - s['pcov'])
                frac += s['n'] / r['T']
                if r['G'] > 0: nG += 1; covG += s['cov']
            if n == 0: continue
            out.append('%s %-4s %-4s primes %4d | hits %6d E %8.1f z %+6.2f | coverage %4d/%4d (G>0: %d/%d) exp %.1f z %+6.2f | mean|S|/|T| %.3f'
                       % (label, {'fam': 'U', 'famA': 'A', 'famAC': 'AC'}[key], F, n, H, E, z(H, E, V), cov, n, covG, nG, pc,
                          z(cov, pc, pcv), frac / n))
    fe = [r.get('cyc_first') for r in recs if r['G'] > 0 and 'cyc_first' in r]
    if fe:
        c = collections.Counter(min(k, 99) if k else 0 for k in fe)
        out.append('%s CYC first entry k (G>0, n=%d): k=1: %d, 3: %d, 5: %d, 7: %d, 9: %d, >9: %d, none (G meets no odd multiple): %d' %
                   (label, len(fe), c[1], c[3], c[5], c[7], c[9], sum(v for k, v in c.items() if k > 9), c[0]))
    for F in ('CYC', 'GEN2'):
        if 'seedid' not in recs[0]: break
        t = collections.Counter()
        for r in recs:
            for k, v in r['seedid'].get(F, {}).items(): t[k] += v
        out.append('%s seed-identity %s: hit classes %d | a generating seed ideal is itself natural %d | reduced ideal natural %d | no generating ideal %d'
                   % (label, F, t['hits'], t['seed_ideal_natural'], t['reduced_natural'], t['no_generating_ideal']))
    return out

def demeaned_corr(xs, ys, strata):
    groups = collections.defaultdict(list)
    for x, y, s in zip(xs, ys, strata): groups[s].append((x, y))
    X = []; Y = []
    for s, l in groups.items():
        if len(l) < 2: continue
        mx = sum(a for a, b in l) / len(l); my = sum(b for a, b in l) / len(l)
        for a, b in l: X.append(a - mx); Y.append(b - my)
    sxx = sum(a * a for a in X); syy = sum(b * b for b in Y); sxy = sum(a * b for a, b in zip(X, Y))
    if sxx == 0 or syy == 0: return float('nan'), 0
    r = sxy / math.sqrt(sxx * syy)
    k = len(groups)
    dfree = len(X) - k - 1
    t = r * math.sqrt(dfree / max(1e-12, 1 - r * r)) if dfree > 0 else float('nan')
    return t, len(X)

def item2(recs, label):
    out = []
    ys = [math.log(1 + r['G']) for r in recs]; em = [1.0 if r['G'] == 0 else 0.0 for r in recs]
    st = [r['n840'] for r in recs]
    for nm in ('r4', 'r8'):
        xs = [r[nm] for r in recs]
        if len(set(xs)) < 2: out.append('%s 2a %s constant (%s)' % (label, nm, xs[0])); continue
        t1, n1 = demeaned_corr(xs, ys, st); t2, n2 = demeaned_corr(xs, em, st)
        out.append('%s 2a %s: log(1+|G|) within-p mod 840 t %+6.2f (n %d); 1[G empty] t %+6.2f; dist %s' %
                   (label, nm, t1, n1, t2, dict(collections.Counter(xs))))
    # 2b: positions of good units over the 2-component coset (orbits under negation)
    chi = 0.0; df = 0; efpc = 0.0
    for r in recs:
        if r['npos'] < 2 or r['G'] < 4: continue
        # orbits of positions under c -> -c: positions are tuples of residues mod 2^v_i
        cyc = r['cyc']; mods = []
        for m in cyc:
            t = 1
            while m % (2 * t) == 0: t *= 2
            mods.append(t)
        cnt = collections.Counter()
        for k, v in r['pos'].items():
            c = tuple(int(x) for x in k.strip('()').split(',') if x.strip() != '')
            nc = tuple((-x) % m for x, m in zip(c, mods))
            o = min(c, nc)
            cnt[(o, c == nc)] += v
        # all orbits of the target 2-coset: we only know npos; orbit sizes from observed + assume pairs
        # units: a good pair-unit contributes 2 to its orbit (both members); singleton orbit -> 1 per unit
        units = {o: (v if self_ else v / 2) for (o, self_), v in cnt.items()}
        nU = sum(units.values())
        # number of orbits: positions are pairs except the self-inverse ones (2-torsion in Cl_2 shifted) – estimate
        npairs = r['npos'] / 2.0
        if npairs < 2: continue
        e = nU / npairs
        chi += sum((u - e) ** 2 / e for u in units.values()) + (npairs - len(units)) * e
        df += npairs - 1
        Nu = r['T'] / 2.0
        efpc += (npairs - 1) * (Nu - nU) / (Nu - 1) if Nu > 1 else 0
    if df:
        out.append('%s 2b positions: chi2 %.1f, nominal df %d, finite-population expectation (B-1)(N-K)/(N-1) = %.1f (descriptive; no calibrated z)' % (label, chi, df, efpc))
    em_l = [(r['n'], r['r4'], r['r8']) for r in recs if r['G'] == 0]
    out.append('%s empty G: %d of %d' % (label, len(em_l), len(recs)))
    return out

def item3(recs, label):
    out = []
    for j in ('-2', '-1', '0', '1', '2', '3', '4', '5', '6'):
        H = E = V = EA = VA = 0.0; n = 0; R = 0; I = 0; HL = EL = VL = EAL = VAL = 0.0; loc = True
        for r in recs:
            p = r.get('it3', {}).get('prof', {})
            if j not in p: continue
            s = p[j]; n += 1; H += s['hit']; E += s['E']; V += s['V']; EA += s['EA']; VA += s['VA']
            R += s['n']
            if 'hitL' in s: HL += s['hitL']; EL += s['EL']; VL += s['VL']; EAL += s['EAL']; VAL += s['VAL']
            else: loc = False
        if n:
            out.append('%s it3 j=%2s primes %4d | non-I reached %6d | III hits %5d  E_unif %7.1f z %+6.2f  E_alpha %7.1f z %+6.2f'
                       % (label, j, n, R, H, E, z(H, E, V), EA, z(H, EA, VA)))
            if loc:
                out.append('%s it3L j=%2s (threshold-local censoring, conditional alpha null) | III hits %5d  E_unif %7.1f z %+6.2f  E_alphaC %7.1f z %+6.2f'
                           % (label, j, HL, EL, z(HL, EL, VL), EAL, z(HL, EAL, VAL)))
    tI = tIII = none = 0; fr = 0
    for r in recs:
        i = r.get('it3')
        if not i: continue
        fr += i['frviol']
        if r['G'] == 0: continue
        a, b = i['firstI'], i['firstIII']
        if a is None and b is None: none += 1
        elif b is None or (a is not None and a < b): tI += 1
        else: tIII += 1
    out.append('%s it3 first entry (G>0): type I %d, type III %d, none within X %d; FR-violations %d' % (label, tI, tIII, none, fr))
    return out

def main_basic():
    recs = load(sys.argv[1:])
    byd = collections.defaultdict(list)
    for r in recs: byd[r['d']].append(r)
    for d in sorted(byd):
        R = byd[d]
        for lab, sub in (('all', R), ('M', [r for r in R if r['n840'] in M840]), ('nonM', [r for r in R if r['n840'] not in M840])):
            L = 'd=%d %-4s' % (d, lab)
            for line in item1(sub, L) + item2(sub, L) + item3(sub, L): print(line)
        print()

# ---------- exact-alpha pooled null (leave-one-prime-out) + hit decomposition (added before W3 was scored) ----------
def _rates(recs):
    tot = collections.Counter(); good = collections.Counter()
    for r in recs:
        for a, (u, g) in r['ahist'].items(): tot[int(a)] += u; good[int(a)] += g
    return tot, good

def _exact_eval(evalrecs, F, tot, good, loo, amax):
    """hits / E / V and coverage for family F on evalrecs with rates (tot, good); loo: subtract the evaluated prime."""
    H = E = V = 0.0; nU = dropped = 0; cov = 0; pc = pcv = 0.0; nP = 0
    for r in evalrecs:
        if F not in r.get('seeds', {}): continue
        ah = r['ahist']; l0 = 0.0; anyhit = 0; usable = True
        for al, w, hit, mn in r['seeds'][F]:
            if al > amax: dropped += 1; usable = False; continue
            u0, g0 = ah.get(str(al), [0, 0]) if loo else (0, 0)
            T_ = tot[al] - u0; G_ = good[al] - g0
            rho = G_ / T_ if T_ > 0 else 0.0
            H += w * hit; E += w * rho; V += w * w * rho * (1 - rho); nU += 1
            l0 = l0 + math.log(1 - rho) if (rho < 1 and l0 > float('-inf')) else float('-inf')
            if hit: anyhit = 1
        if usable:
            nP += 1; cov += anyhit; q = 1 - math.exp(l0) if l0 > float('-inf') else 1.0
            pc += q; pcv += q * (1 - q)
    return H, E, V, nU, dropped, cov, nP, pc, pcv

def item1_exact(recs, label, amax=5000):
    """exact-alpha null.  LOO: rates from all other primes (hits) / other G>0 primes (coverage over G>0 primes; review fix:
    training and evaluation populations matched).  XF: 2-fold cross-fitting by prime index parity (external rates)."""
    out = []
    recs = sorted(recs, key=lambda r: r['n'])
    pos = [r for r in recs if r['G'] > 0]
    tA, gA = _rates(recs); tP, gP = _rates(pos)
    for F in ('RED', 'CYC', 'GEN2'):
        H, E, V, nU, dr, _, _, _, _ = _exact_eval(recs, F, tA, gA, True, amax)
        _, _, _, _, _, cov, nP, pc, pcv = _exact_eval(pos, F, tP, gP, True, amax)
        # cross-fitting
        Hx = Ex = Vx = 0.0; covx = 0; nPx = 0; pcx = pcvx = 0.0
        for f in (0, 1):
            tr = [r for i, r in enumerate(recs) if i % 2 != f]; ev = [r for i, r in enumerate(recs) if i % 2 == f]
            t1, g1 = _rates(tr); a = _exact_eval(ev, F, t1, g1, False, amax)
            Hx += a[0]; Ex += a[1]; Vx += a[2]
            trp = [r for r in tr if r['G'] > 0]; evp = [r for r in ev if r['G'] > 0]
            t2, g2 = _rates(trp); b = _exact_eval(evp, F, t2, g2, False, amax)
            covx += b[5]; nPx += b[6]; pcx += b[7]; pcvx += b[8]
        hits = idhit = small = 0
        for r in recs:
            for al, w, hit, mn in r.get('seeds', {}).get(F, []):
                if hit and al <= amax:
                    hits += 1; idhit += (mn == al); small += (mn <= 100)
        out.append('%s X %-4s units %6d (dropped alpha>%d: %d) | LOO: hits %5d E %8.1f z %+6.2f ; coverage(G>0, G>0-trained) %d/%d exp %.1f z %+6.2f | XF: E %8.1f z %+6.2f ; coverage %d/%d exp %.1f z %+6.2f | hit units: reduced ideal natural %d/%d, least natural norm <=100: %d'
                   % (label, F, nU, amax, dr, H, E, z(H, E, V), cov, nP, pc, z(cov, pc, pcv), Ex, z(Hx, Ex, Vx), covx, nPx, pcx, z(covx, pcx, pcvx), idhit, hits, small))
    return out

def union_cov(recs_all, amax=5000):
    """per prime: does any d in {1,2,3,5,7} have a hit for family F?  null: exact-alpha LOO rates, independence."""
    tot = collections.defaultdict(collections.Counter); good = collections.defaultdict(collections.Counter)
    for r in recs_all:
        for a, (u, g) in r['ahist'].items(): tot[r['d']][int(a)] += u; good[r['d']][int(a)] += g
    by = collections.defaultdict(dict)
    for r in recs_all: by[r['n']][r['d']] = r
    out = []
    for F in ('RED', 'CYC', 'GEN2'):
        n = c = nM = cM = 0; pc = pcv = pcM = 0.0; fails = []
        for p, dd in sorted(by.items()):
            if len(dd) < 5: continue
            n += 1; h = 0; l0 = 0.0
            for d, r in dd.items():
                for al, w, hit, mn in r['seeds'][F]:
                    if hit: h = 1
                    if al > amax: continue
                    u0, g0 = r['ahist'].get(str(al), [0, 0])
                    T_ = tot[d][al] - u0; G_ = good[d][al] - g0
                    rho = G_ / T_ if T_ > 0 else 0.0
                    l0 = l0 + math.log(1 - rho) if (rho < 1 and l0 > float('-inf')) else float('-inf')
            q = 1 - math.exp(l0) if l0 > float('-inf') else 1.0
            c += h; pc += q; pcv += q * (1 - q)
            if p % 840 in M840: nM += 1; cM += h; pcM += q
            if not h: fails.append(p)
        out.append('union over d of %-4s: coverage %d/%d, null exp %.1f (z %+.2f) | M: %d/%d exp %.1f | uncovered: %s'
                   % (F, c, n, pc, z(c, pc, pcv), cM, nM, pcM, fails[:12] if F == 'GEN2' else len(fails)))
    return out

if __name__ == '__main__' and os.environ.get('Z70_EXACT', '0') == '1':
    pass

if __name__ == '__main__':
    main_basic()
    recs = load(sys.argv[1:])
    byd = collections.defaultdict(list)
    for r in recs: byd[r['d']].append(r)
    for d in sorted(byd):
        R = byd[d]
        for lab, sub in (('all', R), ('M', [r for r in R if r['n840'] in M840]), ('nonM', [r for r in R if r['n840'] not in M840])):
            for line in item1_exact(sub, 'd=%d %-4s' % (d, lab)): print(line)
    for line in union_cov(recs): print(line)
