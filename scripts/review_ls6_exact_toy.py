"""R71 from-scratch EXACT toy for LS6 (2.1), Prop 2.2, Prop 4.2 (4.1) and Thm 5.1.

Model (LS5 Setting 2.0 / LS6 §2.2), written independently of the author's script:
  primes POOL ascending, Omega_q = Z/q; classes C=(G,b), G squarefree product of pool primes,
  top(C)=max prime.  F_q(x) = {b mod q : top(C)=q, x_p = b mod p for all other p|G}.
  F~_q = first floor(delta*q) elements of F_q in natural order; p~ = |F~|/q, p = |F|/q.
  Q': x_q ~ U(Omega_q \\ F~_q).  A = avoider set {x_q notin F_q all q}.  Y = sum w_q p~_q.
  sigma = Q' 1_A e^{-2Y} / Z.
Coins for q notin S: c_q ~ U, pi_q uniform ordering; x_q = c_q if c_q notin F~_q, else the first
element of pi_q outside F~_q.  All expectations over coins/v/v' are computed EXACTLY by a DFS
that branches on c_q and lazily on the prefix of pi_q (only as far as needed to decide every
corner's replacement).
Checks for every S with |S|<=2 (and every singleton for Thm 5.1):
  max_{supp theta=S}|sigma^(theta)|  <=  Z^-1 E|D_S Psi(0)|                        (2.1)
                                     <=  Z^-1 4^|S| E sum_partitions prod W_B       (Prop 2.2)
  and  <= Z^-1 4^|S| E sum_T 1[T<=Piv H] max_{A_T} e^{||a||'} XOR-sum              (4.1)
  Thm 5.1 (S={l}): sigma bound and its three sub-bounds (hard, V_dir, per-r tail).
"""
import itertools, math, random, sys, cmath
from functools import lru_cache

DELTA = 0.5

def make_family(rng, pool, ncls):
    fam = set()
    while len(fam) < ncls:
        k = rng.choice([1, 2, 2, 3])
        ps = tuple(sorted(rng.sample(pool, min(k, len(pool)))))
        G = math.prod(ps)
        fam.add((G, ps, rng.randrange(G)))
    return sorted(fam)

class Model:
    def __init__(s, pool, fam, w):
        s.pool, s.fam, s.w = pool, fam, w
        s.bytop = {q: [C for C in fam if C[1][-1] == q] for q in pool}
        s.cap = {q: math.floor(DELTA * q) for q in pool}
    def F(s, q, x):  # x: dict of coordinates < q
        out = set()
        for G, ps, b in s.bytop[q]:
            if all(x[p] == b % p for p in ps[:-1]):
                out.add(b % q)
        return out
    def Ft(s, q, Fq):
        return set(sorted(Fq)[: s.cap[q]])
    def matched_offtop(s, C, x):
        G, ps, b = C
        return all(x[p] == b % p for p in ps[:-1])

    # ---- exact sigma_tilt by enumeration ----
    def exact(s):
        pts = {}
        def rec(i, x, pr, Y, avoid):
            if i == len(s.pool):
                if avoid: pts[tuple(x[q] for q in s.pool)] = pr * math.exp(-2 * Y)
                return
            q = s.pool[i]
            Fq = s.F(q, x); Ftq = s.Ft(q, Fq); pt = len(Ftq) / q
            for a in range(q):
                if a in Ftq: continue
                x[q] = a
                rec(i + 1, x, pr / (q * (1 - pt)), Y + s.w[q] * pt, avoid and a not in Fq)
            del x[q]
        rec(0, {}, 1.0, 0.0, True)
        Z = sum(pts.values())
        return {k: v / Z for k, v in pts.items()}, Z

    def max_fourier(s, sig, S):
        best = 0.0
        idx = [s.pool.index(q) for q in S]
        for th in itertools.product(*[range(1, q) for q in S]):
            c = sum(v * cmath.exp(2j * math.pi * sum(t * k[i] / q for t, i, q in zip(th, idx, S)))
                    for k, v in sig.items())
            best = max(best, abs(c))
        return best

    # ---- corner paths with exact coin DFS ----
    def corner_dfs(s, S, vv, cb):
        """vv: list over corners A (bitmask over S) of pinned values dict.  Calls
        cb(weight, paths) where paths[A] = dict with x, F, Ft per q."""
        nA = len(vv)
        def rec(i, states, wt):
            if i == len(s.pool):
                cb(wt, states); return
            q = s.pool[i]
            Fs = [s.F(q, st["x"]) for st in states]
            Fts = [s.Ft(q, f) for f in Fs]
            def push(xs, w2):
                new = []
                for A, st in enumerate(states):
                    x = dict(st["x"]); x[q] = xs[A]
                    F = dict(st["F"]); F[q] = Fs[A]
                    Ft = dict(st["Ft"]); Ft[q] = Fts[A]
                    new.append({"x": x, "F": F, "Ft": Ft})
                rec(i + 1, new, w2)
            if q in S:
                push([vv[A][q] for A in range(nA)], wt); return
            for c in range(q):
                need = [A for A in range(nA) if c in Fts[A]]
                if not need:
                    push([c] * nA, wt / q); continue
                # lazily enumerate prefix of pi_q
                def pref(used, res, w2):
                    undecided = [A for A in need if A not in res]
                    if not undecided:
                        push([res.get(A, c) for A in range(nA)], w2); return
                    rem = [a for a in range(q) if a not in used]
                    for a in rem:
                        r2 = dict(res)
                        for A in undecided:
                            if a not in Fts[A]: r2[A] = a
                        pref(used | {a}, r2, w2 / len(rem))
                pref(frozenset(), {}, wt / q)
        rec(0, [{"x": {}, "F": {}, "Ft": {}} for _ in range(nA)], 1.0)

def pc(x): return bin(x).count("1")

def Dtop(f, n, A0=0, U=None):
    U = ((1 << n) - 1) if U is None else U
    s = 0.0; B = U
    while True:
        s += (-1) ** pc(U & ~B) * f[A0 | B]
        if B == 0: break
        B = (B - 1) & U
    return s

def piv_mask(vals, n):
    P = 0
    for l in range(n):
        if any(vals[A | 1 << l] != vals[A] for A in range(1 << n) if not A >> l & 1): P |= 1 << l
    return P

def partitions(lst):
    if not lst: yield []; return
    f, rest = lst[0], lst[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[f] + p[i]] + p[i + 1:]
        yield [[f]] + p

def xor_sum(a, U, n):
    """sum over families of nonempty R subset of U with xor = U of prod |a_R| (exact DP)."""
    subs = [R for R in range(1, 1 << n) if R & ~U == 0]
    dp = {0: 1.0}
    for R in subs:
        nd = dict(dp)
        for X, v in dp.items(): nd[X ^ R] = nd.get(X ^ R, 0) + v * abs(a[R])
        dp = nd
    return dp.get(U, 0.0)

def run(seed, pool=(2, 3, 5, 7), ncls=12):
    rng = random.Random(seed)
    fam = make_family(rng, list(pool), ncls)
    w = {q: rng.uniform(0.3, 1.0) for q in pool}
    M = Model(list(pool), fam, w)
    sig, Z = M.exact()
    if Z == 0:
        print(seed, "no avoiders (Z = 0); skipped"); return []
    out = []
    for size in (1, 2):
        for S in itertools.combinations(pool, size):
            n = size; nA = 1 << n
            acc = {"pin": 0.0, "p22": 0.0, "p42": 0.0}
            t51 = {"hard": 0.0, "Vdir": 0.0, "soft": 0.0, "tail": {}}
            Om = [range(q) for q in S]
            tot = math.prod(q * q for q in S)
            for v in itertools.product(*Om):
                for vp in itertools.product(*Om):
                    vv = [{q: (vp[i] if A >> i & 1 else v[i]) for i, q in enumerate(S)} for A in range(nA)]
                    def cb(wt, paths, v=v, vp=vp, vv=vv):
                        wt /= tot
                        # factors per corner
                        H = []; Ystar = []; Psi = []; pt = []; Fsets = []
                        for A, st in enumerate(paths):
                            h = 1
                            for q in M.pool:
                                if q in S:
                                    if st["x"][q] in st["F"][q]: h = 0
                                else:
                                    if st["x"][q] in st["F"][q] - st["Ft"][q]: h = 0
                            pts = {q: len(st["Ft"][q]) / q for q in M.pool}
                            Ysum = sum(M.w[q] * pts[q] for q in M.pool)
                            L = sum(-math.log(1 - pts[l]) for l in S)
                            ys = 2 * Ysum - L
                            # Psi = Phi * prod |Omega| k = 1_A e^{-2Y} prod 1[v notin Ft]/(1-p~)
                            H.append(h); Ystar.append(ys); Psi.append(h * math.exp(-ys)); pt.append(pts)
                            Fsets.append(st["F"])
                        acc["pin"] += wt * abs(Dtop(Psi, n))
                        # Prop 2.2: factors with kappa and pivot masks
                        facs = []
                        for i, l in enumerate(S):
                            facs.append((1.0, piv_mask([int(paths[A]["x"][l] not in paths[A]["F"][l]) for A in range(nA)], n)))
                            dl = max(p[l] for p in pt) - min(p[l] for p in pt)
                            facs.append((2 * dl, piv_mask([p[l] for p in pt], n)))
                        for q in M.pool:
                            if q not in S:
                                lam = [int(paths[A]["x"][q] not in paths[A]["F"][q] - paths[A]["Ft"][q]) for A in range(nA)]
                                facs.append((1.0, piv_mask(lam, n)))
                            dq = max(p[q] for p in pt) - min(p[q] for p in pt)
                            facs.append((M.w[q] * dq, piv_mask([p[q] for p in pt], n)))
                        WB = {}
                        for B in range(1, nA):
                            WB[B] = sum(k for k, P in facs if k > 0 and B & ~P == 0)
                        ps = 0.0
                        for part in partitions(list(range(n))):
                            ps += math.prod(WB[sum(1 << i for i in blk)] for blk in part)
                        acc["p22"] += wt * 4 ** n * ps
                        # Prop 4.2 (4.1)
                        PH = piv_mask(H, n); s42 = 0.0
                        for T in range(nA):
                            if T & ~PH: continue
                            U = (nA - 1) & ~T; best = 0.0
                            AT = T
                            while True:
                                # Walsh coefficients of Y* on subcube AT + A', A' subset U
                                k = pc(U)
                                a = {}
                                for R in range(nA):
                                    if R & ~U: continue
                                    a[R] = sum(Ystar[AT | B] * (-1) ** pc(B & R) for B in range(nA) if B & ~U == 0) / 2 ** k
                                an = sum(abs(a[R]) for R in a if R)
                                val = math.exp(an) * (xor_sum(a, U, n) if U else 1.0)
                                best = max(best, val)
                                if AT == 0: break
                                AT = (AT - 1) & T
                            s42 += best
                        acc["p42"] += wt * 4 ** n * s42
                        if n == 1:
                            l = S[0]; x, xp = paths[0], paths[1]
                            Hd = int(H[0] != H[1])
                            t51["hard"] += wt * Hd
                            Y0 = sum(M.w[q] * pt[0][q] for q in M.pool); Y1 = sum(M.w[q] * pt[1][q] for q in M.pool)
                            t51["soft"] += wt * min(1.0, 2 * abs(Y0 - Y1))
                            vd = sum(M.w[C[1][-1]] / C[1][-1] for C in M.fam if l in C[1] and C[1][-1] > l
                                     and (M.matched_offtop(C, x["x"]) or M.matched_offtop(C, xp["x"])))
                            t51["Vdir"] += wt * vd
                            div = [q for q in M.pool if q != l and x["x"][q] != xp["x"][q]]
                            if div:
                                r = div[0]
                                Yr0 = sum(M.w[q] * pt[0][q] for q in M.pool if q > r)
                                Yr1 = sum(M.w[q] * pt[1][q] for q in M.pool if q > r)
                                t51["tail"][r] = t51["tail"].get(r, 0) + wt * min(1.0, 2 * Yr0 + 2 * Yr1)
                    M.corner_dfs(S, vv, cb)
            lhs = M.max_fourier(sig, S)
            rec = {"S": S, "lhs": lhs, "pin": acc["pin"] / Z, "p22": acc["p22"] / Z, "p42": acc["p42"] / Z}
            assert lhs <= rec["pin"] * (1 + 1e-9), rec
            assert rec["pin"] <= rec["p22"] * (1 + 1e-9), rec
            assert rec["pin"] <= rec["p42"] * (1 + 1e-9), rec
            if n == 1:
                rec.update(thm51(M, S[0], t51, Z))
                assert lhs <= rec["t51"] * (1 + 1e-9), rec
            out.append(rec)
    return out

def thm51(M, l, t, Z):
    G2 = lambda ps: 2.0 ** len(ps)  # Gamma with delta = 1/2
    # E_{Q'} p_l and Lambda_{>l} under Q'^{(l)} (l-kernel uniform), exact
    Ep = 0.0; Lam = 0.0
    def rec(i, x, pr):
        nonlocal Ep, Lam
        if i == len(M.pool): return
        q = M.pool[i]; Fq = M.F(q, x); Ftq = M.Ft(q, Fq); p = len(Fq) / q; pt = len(Ftq) / q
        if q == l: Ep += pr * p
        if q > l and p > DELTA: Lam += pr * p
        for a in range(q):
            if q == l: kk = 1 / q
            elif a in Ftq: continue
            else: kk = 1 / (q * (1 - pt))
            x[q] = a; rec(i + 1, x, pr * kk)
        x.pop(q, None)
    rec(0, {}, 1.0)
    direct = [C for C in M.fam if l in C[1] and C[1][-1] > l]
    mubar = sum(M.w[C[1][-1]] * G2(C[1]) / C[0] for C in direct)
    def nu(r, P):
        return sum(M.w[C[1][-1]] * G2(C[1]) * math.prod(P) / C[0] for C in M.fam
                   if set(P) <= set(C[1]) and C[1][-1] > r)
    per_r = {}
    for C in direct:
        r = C[1][-1]
        sP = sum(nu(r, P) for k in range(len(C[1]) + 1) for P in itertools.combinations(C[1], k))
        per_r[r] = per_r.get(r, 0) + G2(C[1]) / C[0] * sP
    bound = (4 * Ep + 8 * Lam + 8 * mubar + 160 * sum(per_r.values())) / Z
    # sub-checks
    assert t["hard"] <= 2 * Ep + 4 * Lam + 1e-12, (t["hard"], Ep, Lam)
    assert t["Vdir"] <= 2 * mubar + 1e-12
    for r, val in t["tail"].items():
        assert val <= 80 * per_r.get(r, 0) + 1e-12, (r, val, per_r)
    return {"t51": bound, "hard": t["hard"] / (2 * Ep + 4 * Lam + 1e-300),
            "vdir": t["Vdir"] / (2 * mubar + 1e-300),
            "tail": max([v / (80 * per_r[r]) for r, v in t["tail"].items() if per_r.get(r, 0) > 0] or [0])}

if __name__ == "__main__":
    seeds = [int(a) for a in sys.argv[1:]] or [1]
    for sd in seeds:
        for rec in run(sd):
            print(sd, {k: (round(v, 4) if isinstance(v, float) else v) for k, v in rec.items()})
