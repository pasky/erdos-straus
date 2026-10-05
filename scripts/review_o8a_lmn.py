"""Review O8 (reviewer 1): from-scratch checks of Lemma 4.1.

(a) interval encoding: fibres are intervals, <=2b dyadic subcubes of codim<=b,
    sizes floor/ceil(2^b/q).
(b) restriction identity E_rho W^{>=k}[f_rho] = sum_U Pr[Bin(|U|,p)>=k] fhat(U)^2
    (exact enumeration), and Haastad's bound Pr[DT(f_rho)>=s] <= (5pw)^s on toy DNFs.
(c) median claim: Pr[Bin(n,p) >= k0] >= 1/2 whenever n*p >= k0.
(d) full Lemma 4.1 chain on a toy good-indicator: Fourier truncation of
    phi~ = phi o pi, pull-back g = E[g~|pi], junta check, Jensen, density.
"""
import itertools, sys, functools
from math import comb, floor, ceil
import numpy as np

out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

# ---------- (a) encoding ----------
def dyadic_cover(lo, hi, b):
    """minimal dyadic decomposition of integer interval [lo,hi) in [0,2^b)."""
    cubes = []
    x = lo
    while x < hi:
        s = 0
        while s < b and x % (1 << (s + 1)) == 0 and x + (1 << (s + 1)) <= hi:
            s += 1
        cubes.append((x, s)); x += 1 << s
    return cubes

worst_cubes = 0; bad = 0
for b in range(1, 11):
    for q in range(1, (1 << b) + 1):
        fib = {}
        for u in range(1 << b):
            fib.setdefault((q * u) >> b, []).append(u)
        assert sorted(fib) == list(range(q))
        for i, us in fib.items():
            if us != list(range(us[0], us[-1] + 1)): bad += 1
            if len(us) not in (floor((1 << b) / q), ceil((1 << b) / q)): bad += 1
            cv = dyadic_cover(us[0], us[-1] + 1, b)
            worst_cubes = max(worst_cubes, len(cv) / (2 * b))
            if len(cv) > 2 * b: bad += 1
say('(a) encoding b<=10, all q<=2^b: violations', bad, ' max #cubes/(2b) =', round(worst_cubes, 3))

# ---------- Fourier utilities (0/1 or real functions on {0,1}^n) ----------
def wht(f):
    a = f.astype(float).copy(); n = int(np.log2(len(a))); h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            x = a[i:i + h].copy(); y = a[i + h:i + 2 * h].copy()
            a[i:i + h] = x + y; a[i + h:i + 2 * h] = x - y
        h *= 2
    return a / len(a)   # fhat(S) with chi_S(x)=(-1)^{<S,x>}

popc = np.vectorize(lambda s: bin(s).count('1'))

# ---------- (b) restriction identity + switching lemma on toy DNFs ----------
def dnf_eval(terms, n):
    xs = np.arange(1 << n)
    val = np.zeros(1 << n, dtype=int)
    for t in terms:   # term: list of (var, bit)
        ok = np.ones(1 << n, dtype=bool)
        for v, bit in t: ok &= ((xs >> v) & 1) == bit
        val |= ok
    return val

def dt_depth(table, n):
    """exact decision-tree depth of f given as tuple over {0,1}^n (memoised)."""
    @functools.lru_cache(maxsize=None)
    def rec(tab, vars_):
        if len(set(tab)) <= 1: return 0
        best = 99
        vl = list(vars_)
        for idx, v in enumerate(vl):
            rest = tuple(vl[:idx] + vl[idx + 1:])
            # split on position idx in the current ordering
            t0 = tuple(tab[j] for j in range(len(tab)) if not (j >> idx) & 1)
            t1 = tuple(tab[j] for j in range(len(tab)) if (j >> idx) & 1)
            best = min(best, 1 + max(rec(t0, rest), rec(t1, rest)))
        return best
    return rec(tuple(table), tuple(range(n)))

def restrict(f, n, J, z):
    """f restricted: free vars J (sorted list), others fixed by z (int)."""
    xs = []
    for y in range(1 << len(J)):
        x = z
        for i, v in enumerate(J):
            x = (x & ~(1 << v)) | (((y >> i) & 1) << v)
        xs.append(x)
    return f[np.array(xs)]

rng = np.random.default_rng(3)
id_err = 0.0; sw_viol = []
for trial in range(12):
    n = 7; w = int(rng.integers(2, 4))
    terms = []
    for _ in range(int(rng.integers(3, 9))):
        vs = rng.choice(n, w, replace=False)
        terms.append([(int(v), int(rng.integers(2))) for v in vs])
    f = dnf_eval(terms, n)
    fh = wht(f); deg = popc(np.arange(1 << n))
    for p in (0.05, 0.1, 0.2):
        PDT = {}; EW = {k: 0.0 for k in range(1, n + 1)}
        for Jmask in range(1 << n):
            J = [v for v in range(n) if (Jmask >> v) & 1]
            pj = p ** len(J) * (1 - p) ** (n - len(J))
            for z in range(1 << n):
                if z & Jmask: continue      # z only matters off J
                pz = pj / (1 << (n - len(J)))
                fr = restrict(f, n, J, z)
                d = dt_depth(fr, len(J))
                PDT[d] = PDT.get(d, 0) + pz
                frh = wht(fr); dg = popc(np.arange(1 << len(J)))
                for k in EW: EW[k] += pz * (frh[dg >= k] ** 2).sum()
        for k in EW:
            rhs = sum(fh[U] ** 2 * sum(comb(int(deg[U]), j) * p ** j * (1 - p) ** (int(deg[U]) - j)
                                        for j in range(k, int(deg[U]) + 1)) for U in range(1 << n))
            id_err = max(id_err, abs(EW[k] - rhs))
        for s in range(1, n + 1):
            tail = sum(v for d, v in PDT.items() if d >= s)
            if tail > (5 * p * w) ** s + 1e-12: sw_viol.append((trial, p, s, tail))
say('(b) restriction identity max err', id_err, '; switching (5pw)^s violations', len(sw_viol))

# ---------- (c) median ----------
viol = 0; tested = 0
for w_ in range(1, 41):
    p = 1 / (10 * w_)
    for k0 in range(1, 31):
        nmin = ceil(k0 / p - 1e-9)
        for n in range(nmin, nmin + 40):
            tested += 1
            # Pr[Bin(n,p) >= k0]
            pr = 1 - sum(comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k0))
            if pr < 0.5 - 1e-12: viol += 1
say('(c) Pr[Bin(n,p)>=k0]>=1/2 when np>=k0, p=1/(10w): tested', tested, 'violations', viol)

# ---------- (d) full chain on toy good indicator ----------
def chain(qs, b, events, seed):
    N = len(qs); nb = N * b
    U = np.arange(1 << nb)
    blocks = [(U >> (i * b)) & ((1 << b) - 1) for i in range(N)]
    X = np.stack([(qs[i] * blocks[i]) >> b for i in range(N)], axis=1)   # pi(U)
    bad_ = np.zeros(len(U), dtype=bool)
    for supp, V in events:
        ok = np.ones(len(U), dtype=bool)
        for c, Vs in zip(supp, V): ok &= np.isin(X[:, c], Vs)
        bad_ |= ok
    phit = (~bad_).astype(float)
    fh = wht(phit); deg = popc(np.arange(1 << nb))
    # how many bit-blocks each character touches
    nblk = np.array([sum(1 for i in range(N) if (S >> (i * b)) & ((1 << b) - 1)) for S in range(1 << nb)])
    # characters as functions: chi_S(U) = (-1)^{popc(S&U)}
    res = []
    keys = X @ np.array([int(np.prod(qs[:i])) for i in range(N)])
    nx = int(np.prod(qs))
    pistar = np.bincount(keys, minlength=nx) / len(U)
    xs_all = np.array(list(itertools.product(*[range(q) for q in reversed(qs)])))[:, ::-1]
    phi_x = np.zeros(nx); np.add.at(phi_x, keys, phit); phi_x /= np.bincount(keys, minlength=nx)
    for d in range(1, nb + 1):
        keep = deg < d
        gt = np.zeros(len(U))
        for S in np.nonzero(keep & (np.abs(fh) > 1e-15))[0]:
            gt += fh[S] * (1 - 2 * (popc(S & U) & 1))
        Wtail = (fh[~keep] ** 2).sum()
        lhs_bits = np.mean((phit - gt) ** 2)
        g = np.zeros(nx); np.add.at(g, keys, gt); g /= np.bincount(keys, minlength=nx)
        e_pi = (pistar * (phi_x - g) ** 2).sum()
        e_haar = np.mean((phi_x - g) ** 2)
        # junta check: max #blocks touched by kept characters
        jmax = nblk[keep & (np.abs(fh) > 1e-15)].max() if (keep & (np.abs(fh) > 1e-15)).any() else 0
        # Haar energy above level d-1 (projection residual on juntas of <=d-1 coords)
        cols = [np.ones(nx)]
        for s in range(1, min(d - 1, N) + 1):
            for W in itertools.combinations(range(N), s):
                for vals in itertools.product(*[range(qs[c]) for c in W]):
                    cols.append(np.all(xs_all[:, list(W)] == np.array(vals), axis=1).astype(float))
        A = np.array(cols).T
        coef, *_ = np.linalg.lstsq(A, phi_x, rcond=None)
        energy = np.mean((phi_x - A @ coef) ** 2)
        # residual of g itself on junta space (should be 0 since g is a <d junta sum)
        cg, *_ = np.linalg.lstsq(A, g, rcond=None)
        g_res = np.abs(g - A @ cg).max()
        ratio = max(1 / qs[i] / (floor((1 << b) / qs[i]) / (1 << b)) for i in range(N))
        dens = np.prod([1 / (1 - qs[i] / (1 << b)) for i in range(N)])
        res.append((d, Wtail, lhs_bits, e_pi, e_haar, energy, jmax, g_res, dens))
    return res

ok_chain = True
for (qs, b) in [([3, 5], 4), ([3, 5, 7], 4), ([7, 5], 5)]:
    rng2 = np.random.default_rng(sum(qs) + b)
    events = []
    for _ in range(4):
        s = int(rng2.integers(1, len(qs) + 1)); supp = sorted(rng2.choice(len(qs), s, replace=False).tolist())
        V = [sorted(rng2.choice(qs[c], int(rng2.integers(1, qs[c])), replace=False).tolist()) for c in supp]
        events.append((supp, V))
    for (d, Wt, lb, epi, eh, en, jm, gr, dens) in chain(qs, b, events, 0):
        good = (abs(Wt - lb) < 1e-10 and epi <= lb + 1e-12 and jm < d and gr < 1e-9
                and en <= eh + 1e-12 and eh <= dens * epi + 1e-12)
        ok_chain &= good
        say(f'(d) qs={qs} b={b} d={d}: W>=d={Wt:.3e} Epi(phi-g)^2={epi:.3e} Haar={eh:.3e} '
            f'energy(<d)={en:.3e} jmax={jm} gres={gr:.1e} densbound={dens:.3f} ok={good}')
say('(d) all chain inequalities ok:', ok_chain)
open('data/review_o8a/lmn.txt', 'w').write('\n'.join(out) + '\n')
sys.exit(0 if (bad == 0 and id_err < 1e-9 and not sw_viol and viol == 0 and ok_chain) else 1)
