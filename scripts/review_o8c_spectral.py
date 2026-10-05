"""R30c from-scratch check of POINTWISE_OMEGA8 Lemma 6.1 on toy DNFs.

Checks, exactly (full enumeration of restrictions), for random width-w DNFs
on n bits and several p:
  (i)  restriction identity  E_z fhat_rho(S) = fhat(S)
  (ii) sum_S p^|S| |fhat(S)| <= E_rho ||fhat_rho||_1 <= E_rho 2^DT(f_rho)
  (iii) ||fhat_rho||_1 <= 2^DT(f_rho) pointwise.
Then a q-ary toy: pulled-back truncation g_j of a bit-encoded good indicator,
BRW minorant B, checks B<=F, M_1 cell expansion = E|h| per term, and
M_1(B) <= 1+m+2m^2 L + m^3 L^2, L = sum_{|S|<d}|ghat(S)|.
"""
import itertools, random, sys
from functools import lru_cache
import numpy as np

def fwht(v):
    v = v.astype(float).copy(); h = 1; n = len(v)
    while h < n:
        for i in range(0, n, 2 * h):
            a = v[i:i + h].copy(); b = v[i + h:i + 2 * h].copy()
            v[i:i + h] = a + b; v[i + h:i + 2 * h] = a - b
        h *= 2
    return v / n   # fhat(S) = E f(x) (-1)^{S.x}

@lru_cache(maxsize=None)
def DT(tt):
    """exact decision-tree depth of boolean fn given as truth-table tuple (len 2^m)."""
    if min(tt) == max(tt): return 0
    m = len(tt).bit_length() - 1
    best = m
    for i in range(m):
        f0 = tuple(tt[x] for x in range(len(tt)) if not (x >> i) & 1)
        f1 = tuple(tt[x] for x in range(len(tt)) if (x >> i) & 1)
        best = min(best, 1 + max(DT(f0), DT(f1)))
    return best

def rand_dnf(n, w, nterms, rng):
    terms = []
    for _ in range(nterms):
        vs = rng.sample(range(n), w)
        terms.append([(v, rng.randint(0, 1)) for v in vs])
    tt = np.zeros(1 << n)
    for x in range(1 << n):
        tt[x] = any(all(((x >> v) & 1) == b for v, b in t) for t in terms)
    return tt

def restrict(tt, n, I, z):
    """free coords I (list), fixed coords others with bits from z (dict)."""
    m = len(I); out = np.zeros(1 << m)
    base = 0
    for v, b in z.items(): base |= b << v
    for y in range(1 << m):
        x = base
        for k, v in enumerate(I):
            x |= ((y >> k) & 1) << v
        out[y] = tt[x]
    return out

def check_dnf(n, w, nterms, p, rng):
    tt = rand_dnf(n, w, nterms, rng)
    fh = fwht(tt)
    lhs = sum(p ** bin(S).count('1') * abs(fh[S]) for S in range(1 << n))
    El1 = E2dt = 0.0; worst_iii = -1e9; worst_i = 0.0
    for mask in range(1 << n):           # free set I
        I = [v for v in range(n) if (mask >> v) & 1]; J = [v for v in range(n) if not (mask >> v) & 1]
        pI = p ** len(I) * (1 - p) ** len(J)
        acc = np.zeros(1 << len(I))
        for zb in range(1 << len(J)):
            z = {v: (zb >> k) & 1 for k, v in enumerate(J)}
            fr = restrict(tt, n, I, z); frh = fwht(fr)
            acc += frh / (1 << len(J))
            l1 = np.abs(frh).sum(); dt = DT(tuple(fr.astype(int)))
            worst_iii = max(worst_iii, l1 - 2 ** dt)
            El1 += pI * l1 / (1 << len(J)); E2dt += pI * 2 ** dt / (1 << len(J))
        # (i): acc[S'] vs fh[S] where S' indexes subsets of I
        for Sp in range(1 << len(I)):
            S = sum(1 << I[k] for k in range(len(I)) if (Sp >> k) & 1)
            worst_i = max(worst_i, abs(acc[Sp] - fh[S]))
    return lhs, El1, E2dt, worst_i, worst_iii

def main():
    rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
    print("part A: Mansour/Hastad chain on random DNFs")
    bad = 0
    for trial in range(12):
        n = rng.choice([5, 6, 7]); w = rng.choice([1, 2, 3]); nt = rng.randint(1, 6)
        for p in (0.05, 0.2, 0.5):
            lhs, El1, E2dt, wi, wiii = check_dnf(n, w, nt, p, rng)
            ok = (lhs <= El1 + 1e-12) and (El1 <= E2dt + 1e-12) and wi < 1e-12 and wiii <= 1e-12
            bad += not ok
            print(f" n={n} w={w} terms={nt} p={p}: sum p^|S||fh|={lhs:.4f} <= E||fh_rho||1={El1:.4f} <= E2^DT={E2dt:.4f}  id_err={wi:.1e} l1-2^DT max={wiii:.2e} {'OK' if ok else 'FAIL'}")
    print("part A failures:", bad)

if __name__ == "__main__":
    main()


# ---------------- part B: q-ary toy, pulled-back truncation, BRW minorant ----
def partB(seed, N=3, q=3, b=2, nev=5, d=3):
    rng = random.Random(seed)
    # encoding pi: bits u in {0,1}^b -> floor(q*int(u)/2^b)
    pi1 = [(q * u) >> b for u in range(1 << b)]
    nb = N * b
    pts = list(itertools.product(range(q), repeat=N))
    # events: single-value on 1..2 coordinates
    evs = []
    for _ in range(nev):
        supp = rng.sample(range(N), rng.choice([1, 2]))
        evs.append({c: rng.randrange(q) for c in supp})
    A = lambda e, x: float(all(x[c] == v for c, v in e.items()))
    def x_of_u(u):
        return tuple(pi1[(u >> (b * c)) & ((1 << b) - 1)] for c in range(N))
    m = len(evs); res = {}
    gfun = []; Ls = []
    for j in range(m):
        # F^{(j)}(x) := F_{<j} with X_supp E_j pinned to sigma_j (function of others)
        def Fj(x, j=j):
            y = list(x)
            for c, v in evs[j].items(): y[c] = v
            return float(all(A(evs[i], y) == 0 for i in range(j)))
        tt = np.array([Fj(x_of_u(u)) for u in range(1 << nb)])
        fh = fwht(tt)
        keep = [S for S in range(1 << nb) if bin(S).count('1') < d and abs(fh[S]) > 1e-15]
        L = sum(abs(fh[S]) for S in keep); Ls.append(L)
        # pulled-back characters chi~_S(x) = E[chi_S(U) | pi(U)=x]
        fib = {}
        for u in range(1 << nb): fib.setdefault(x_of_u(u), []).append(u)
        chit = {}
        for S in keep:
            chit[S] = {x: np.mean([(-1) ** bin(S & u).count('1') for u in fib[x]]) for x in pts}
            assert max(abs(v) for v in chit[S].values()) <= 1 + 1e-12
            blocks = {c for c in range(N) if (S >> (b * c)) & ((1 << b) - 1)}
            assert all(c not in evs[j] for c in blocks)   # g_j avoids supp E_j
            # depends only on blocks: check
            for x in pts:
                for c in range(N):
                    if c in blocks: continue
                    for v in range(q):
                        y = list(x); y[c] = v
                        assert abs(chit[S][tuple(y)] - chit[S][x]) < 1e-12
        g = {x: sum(fh[S] * chit[S][x] for S in keep) for x in pts}
        gfun.append((keep, fh, chit, g))
        # Jensen under pi_*: E_{pi*}(F-g)^2 <= E_U (Ftilde - gtilde)^2
        gt = np.zeros(1 << nb)
        for S in keep:
            gt += fh[S] * np.array([(-1) ** bin(S & u).count('1') for u in range(1 << nb)])
        lhs = np.mean([(Fj(x_of_u(u)) - g[x_of_u(u)]) ** 2 for u in range(1 << nb)])
        rhs = np.mean((tt - gt) ** 2)
        assert lhs <= rhs + 1e-12, (lhs, rhs)
    # B and F on Haar points
    worst = -1e9; M1 = 1.0 + m   # constant term and -sum A_i
    for x in pts:
        F = float(all(A(e, x) == 0 for e in evs))
        Bv = 1.0
        for i in range(m):
            v = sum(A(evs[jj], x) * gfun[jj][3][x] for jj in range(i))
            Bv -= A(evs[i], x) * (1 - v) ** 2
        worst = max(worst, Bv - F)
    # M_1 of each expanded term = |coef| * E_Haar|h|, h = A..chi~..
    EH = lambda f: np.mean([abs(f(x)) for x in pts])
    for i in range(m):
        for jj in range(i):
            keep, fh, chit, _ = gfun[jj]
            for S in keep:
                M1 += 2 * abs(fh[S]) * EH(lambda x: A(evs[i], x) * A(evs[jj], x) * chit[S][x])
            for jp in range(i):
                k2, fh2, ch2, _ = gfun[jp]
                for S in keep:
                    for S2 in k2:
                        M1 += abs(fh[S] * fh2[S2]) * EH(lambda x: A(evs[i], x) * A(evs[jj], x) * A(evs[jp], x) * chit[S][x] * ch2[S2][x])
    Lmax = max(Ls)
    bound = 1 + m + 2 * m * m * Lmax + m ** 3 * Lmax ** 2
    return worst, M1, bound, Lmax

if __name__ == "__main__":
    print("part B: q-ary toy (N=3,q=3,b=2), pulled-back truncation")
    for seed in range(8):
        for d in (2, 3, 5):
            w, M1, bd, L = partB(seed, d=d)
            print(f" seed={seed} d={d}: max(B-F)={w:.2e}  M1(B)={M1:.3f} <= bound={bd:.1f} (L={L:.3f}) {'OK' if (w<=1e-12 and M1<=bd) else 'FAIL'}")
