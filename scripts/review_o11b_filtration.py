"""R44b from-scratch check of OMEGA11 Lemma 1.1 (filtration C-1) and Remark (ii).

Model: "primes" ell, each with base-ell digit coordinates at ABSOLUTE positions i0..f-1
(digits below i0 are fixed: fibre / conditioning).  Digit 0 has alphabet ell-1 (units) or
ell (fibre); higher digits alphabet ell.  Events fix an initial segment i0..v-1 of the
remaining digits at each ell of their support (values arbitrary).
Weights Lambda_{ell,i} = lam_ell^{i+1}; G' = sum_U prod_ell Lambda_{ell,maxU_ell} ||F^{=U}||^2.
Hypothesis (rho=2): every event has prod lam^{2 v_ell} <= 2 (v absolute).

Checks per system:
  (a) G' <= 1;
  (b) identity G' = sum_{selections V} mu'^V ||L_V F||^2;
  (c) per selection: ||L_V F||^2 <= E_x N_{H^(x)}(V)^2.
Usage: review_o11b_filtration.py SEED NSYS [rho] [mode]   mode in {random, climb}
"""
import sys, itertools, math
import numpy as np

def build(rng, cond_prob=0.4):
    nl = rng.integers(1, 4)
    primes = []
    ncoord = 0
    for _ in range(nl):
        ell = int(rng.choice([2, 3, 3, 4, 5]))  # alphabet sizes (4 allowed: model only)
        f = int(rng.integers(1, 4))
        i0 = int(rng.integers(0, f)) if rng.random() < cond_prob else 0
        units = rng.random() < 0.5 and i0 == 0 and ell > 2
        sizes = [(ell - 1 if (i == 0 and units) else ell) for i in range(i0, f)]
        primes.append(dict(ell=ell, f=f, i0=i0, sizes=sizes))
        ncoord += len(sizes)
    if ncoord > 9 or np.prod([s for p in primes for s in p['sizes']]) > 6000:
        return None
    return primes

def coords(primes):
    out = []
    for a, p in enumerate(primes):
        for k, s in enumerate(p['sizes']):
            out.append((a, p['i0'] + k, s))
    return out

def rand_event(rng, primes):
    ev = {}
    for a, p in enumerate(primes):
        if rng.random() < 0.6:
            v = int(rng.integers(p['i0'] + 1, p['f'] + 1))
            vals = [int(rng.integers(0, p['sizes'][k])) for k in range(v - p['i0'])]
            ev[a] = (v, vals)
    if not ev:
        a = int(rng.integers(0, len(primes))); p = primes[a]
        ev[a] = (p['i0'] + 1, [int(rng.integers(0, p['sizes'][0]))])
    return ev

def holds(ev, primes, C, shape):
    h = np.ones(shape, dtype=bool)
    for a, (v, vals) in ev.items():
        for ci, (pa, pos, s) in enumerate(C):
            if pa == a and pos < v:
                idx = [np.newaxis] * len(C); idx[ci] = slice(None)
                h &= (np.arange(s) == vals[pos - primes[a]['i0']])[tuple(idx)]
    return h

def energies(F, n):
    """||F^{=U}||^2 for all U (bitmask) by Moebius inversion of ||E[F|X_W]||^2."""
    cn = np.zeros(1 << n)
    for W in range(1 << n):
        ax = tuple(i for i in range(n) if not (W >> i) & 1)
        g = F.mean(axis=ax) if ax else F
        cn[W] = (g ** 2).mean()
    en = cn.copy()
    for i in range(n):
        for U in range(1 << n):
            if (U >> i) & 1:
                en[U] -= en[U ^ (1 << i)]
    return en

def analyse(primes, events, lam, check_sel=True):
    C = coords(primes); n = len(C); shape = tuple(c[2] for c in C)
    H = [holds(e, primes, C, shape) for e in events]
    F = np.ones(shape)
    for h in H:
        F *= (1 - h)
    en = energies(F, n)
    # G'
    G = 0.0
    for U in range(1 << n):
        w = 1.0
        for a, p in enumerate(primes):
            top = [C[i][1] for i in range(n) if (U >> i) & 1 and C[i][0] == a]
            if top:
                w *= lam[a] ** (max(top) + 1)
        G += w * en[U]
    if not check_sel:
        return G, 0.0, 0.0
    # selections
    levels = [[None] + list(range(p['i0'], p['f'])) for p in primes]
    Gsel = 0.0; worst = -1e9
    for sel in itertools.product(*levels):
        mu = 1.0
        for a, j in enumerate(sel):
            if j is not None:
                L = lambda i: lam[a] ** (i + 1) if i >= primes[a]['i0'] else 1.0
                mu *= L(j) - L(j - 1)
        # ||L_V F||^2
        lhs = 0.0
        for U in range(1 << n):
            ok = True
            for a, j in enumerate(sel):
                if j is None:
                    continue
                top = [C[i][1] for i in range(n) if (U >> i) & 1 and C[i][0] == a]
                if not top or max(top) < j:
                    ok = False; break
            if ok:
                lhs += en[U]
        Gsel += mu * lhs
        # E_x N(V)^2 ; V = {a: sel[a] not None}; trace of E-hat on V: a with v_a(E) > j_a
        Vs = [a for a, j in enumerate(sel) if j is not None]
        traces = []
        for e in events:
            traces.append(frozenset(a for a in Vs if a in e and e[a][0] > sel[a]))
        N = np.zeros(shape)
        for r in range(len(Vs) + 1):
            for R in itertools.combinations(Vs, r):
                Rs = set(R)
                tau = np.ones(shape)
                for h, t in zip(H, traces):
                    if not (t & Rs):
                        tau *= (1 - h)
                N += (-1) ** r * tau
        rhs = (N ** 2).mean()
        worst = max(worst, lhs - rhs)
    return G, Gsel, worst

def weights(rng, primes, events, rho):
    g = rng.random(len(primes)) + 0.05
    m = max(sum(rho * e[a][0] * g[a] for a in e) for e in events)
    return [2 ** (g[a] / m) for a in range(len(primes))]

def main():
    seed = int(sys.argv[1]); nsys = int(sys.argv[2])
    rho = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
    mode = sys.argv[4] if len(sys.argv) > 4 else 'random'
    rng = np.random.default_rng(seed)
    maxG = 0; maxid = 0; maxsel = -1e9; done = 0
    while done < nsys:
        primes = build(rng)
        if primes is None:
            continue
        events = [rand_event(rng, primes) for _ in range(int(rng.integers(1, 7)))]
        lam = weights(rng, primes, events, rho)
        G, Gs, ws = analyse(primes, events, lam, check_sel=(mode == 'random'))
        if mode == 'climb':
            for it in range(150):
                ev2 = [dict(e) for e in events]
                k = int(rng.integers(0, len(ev2) + 1))
                if k == len(ev2):
                    if len(ev2) < 8: ev2.append(rand_event(rng, primes))
                else:
                    ev2[k] = rand_event(rng, primes)
                lam2 = weights(rng, primes, ev2, rho) if rng.random() < 0.3 else None
                if lam2 is None:
                    # rescale existing lam to keep the hypothesis tight
                    g = [math.log2(x) for x in lam]
                    m = max(sum(rho * e[a][0] * g[a] for a in e) for e in ev2)
                    lam2 = [2 ** (x / m) for x in g]
                G2, _, _ = analyse(primes, ev2, lam2, check_sel=False)
                if G2 >= G:
                    events, lam, G = ev2, lam2, G2
            Gs = G
        maxG = max(maxG, G); maxid = max(maxid, abs(G - Gs) if mode == 'random' else 0)
        maxsel = max(maxsel, ws if mode == 'random' else -1e9)
        done += 1
    print(f"seed={seed} n={nsys} rho={rho} mode={mode}: max G'={maxG:.6f}"
          f"  max|G'-sum_sel|={maxid:.2e}  max(||L_VF||^2 - E N^2)={maxsel:.2e}")

if __name__ == '__main__':
    main()
