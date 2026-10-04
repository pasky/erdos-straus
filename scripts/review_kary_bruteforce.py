"""Independent brute-force test of EXCEPTIONAL_KARY Thm 2.5 / Lemmas 2.3, 2.4.

Written from scratch for the hostile review (does not import kary_check.py).

Setting: coordinates 0..N-1, alphabets [q_l], product law nu.  An *activation
rule* maps the full state (c_<l, y_<l) to a subset F_l of the alphabet.  Rules
tested:
  plain    : F_l from a random pattern family, completed by y_<l (ETw sigma)
  phantom  : completed by some z in prod{c_i, y_i}
  arbitrary: F_l = pseudo-random function of the full state (c_<l, y_<l)
  adversarial: hill-climb over an arbitrary rule table to maximise the LP value
All paths of the coupled process are enumerated exactly.  For each t we form
  w(x) = E_omega[ exp(-Phi(omega)) 1{y = x} ],  Phi = log B(n,t,d) + (4/3) t M
and solve   max sum_x w(x) f(x)  s.t.  sum_x nu(x) f(x) = 1, f >= 0, f d-local.
Thm 2.5 <=> value <= 1.  We use B = B*(n,t,d), the LP-optimal 1-D constant
(B* <= Lagrange B, so this is a stronger test), and also report the
Lagrange-min B of Lemma 2.3 vs B*.
Lemma 2.4 is checked directly: E_omega[W P_rho(y^rho = x | omega)] <= nu(x).
Power checks: the same LP with (a) the (4/3)tM weight removed and (b) degree
d-1 in B*, must exceed 1 on some instances (else the test has no teeth).
"""
import itertools, math, sys, random
import numpy as np
from scipy.optimize import linprog

TOL = 1e-7


def binom_pmf(n, t):
    return np.array([math.comb(n, k) * t**k * (1 - t) ** (n - k) for k in range(n + 1)])


_bstar = {}


def Bstar(n, t, d):
    """max Q(n) / E_{Bin(n,t)} Q over Q >= 0 on {0..n}, deg Q <= d."""
    key = (n, round(t, 12), d)
    if key in _bstar:
        return _bstar[key]
    if d == 0 or n == 0:
        v = 1.0
    elif n <= d:
        v = 1.0 / t**n
    else:
        psi = binom_pmf(n, t)
        A = np.array([[math.comb(k, j) for j in range(d + 1)] for k in range(n + 1)], float)
        # variables a_j; maximize Q(n) = A[n].a ; s.t. psi.A a = 1 ; A a >= 0
        res = linprog(-A[n], A_ub=-A, b_ub=np.zeros(n + 1), A_eq=[psi @ A], b_eq=[1.0],
                      bounds=[(None, None)] * (d + 1), method="highs")
        assert res.status == 0, res.message
        v = -res.fun
    _bstar[key] = v
    return v


def Blagrange(n, t, d):
    """Lemma 2.3's B: min over node sets Y (|Y| = min(d,n)+1) of max |l_y(n)|/psi(y)."""
    if d == 0:
        return 1.0
    psi = binom_pmf(n, t)
    m = min(d, n) + 1
    best = math.inf
    for Y in itertools.combinations(range(n + 1), m):
        worst = 0.0
        for y in Y:
            num = 1.0
            for z in Y:
                if z != y:
                    num *= (n - z) / (y - z)
            worst = max(worst, abs(num) / psi[y])
        best = min(best, worst)
    return best


class System:
    def __init__(self, qs, nus, deltas, rule, d):
        self.N = len(qs)
        self.qs, self.nus, self.deltas, self.rule, self.d = qs, nus, deltas, rule, d
        self.points = list(itertools.product(*[range(q) for q in qs]))
        self.idx = {x: i for i, x in enumerate(self.points)}
        self.nu = np.array([math.prod(nus[l][x[l]] for l in range(self.N)) for x in self.points])

    def paths(self):
        """yield (prob, c, y, R, M)"""
        out = []

        def rec(l, prob, c, y, R, M):
            if l == self.N:
                out.append((prob, tuple(c), tuple(y), tuple(R), M))
                return
            F = self.rule(l, tuple(c), tuple(y))
            p = sum(self.nus[l][a] for a in F)
            light = p <= self.deltas[l] + 1e-15
            for a in range(self.qs[l]):
                pa = self.nus[l][a]
                if pa == 0:
                    continue
                if light and a in F:
                    for b in range(self.qs[l]):
                        if b in F:
                            continue
                        pb = self.nus[l][b] / (1 - p)
                        rec(l + 1, prob * pa * pb, c + [a], y + [b], R + [l], M + p)
                else:
                    rec(l + 1, prob * pa, c + [a], y + [a], R, M + (p if light else 0.0))

        rec(0, 1.0, [], [], [], 0.0)
        return out

    def local_basis(self, d):
        cols = []
        for k in range(d + 1):
            for T in itertools.combinations(range(self.N), k):
                for vals in itertools.product(*[range(self.qs[l]) for l in T]):
                    col = np.array([1.0 if all(x[l] == v for l, v in zip(T, vals)) else 0.0
                                    for x in self.points])
                    cols.append(col)
        return np.array(cols).T  # |Omega| x dim

    def lp_value(self, w, d, basis=None):
        """max w.f s.t. nu.f = 1, f >= 0, f in span(basis)."""
        Bm = self.local_basis(d) if basis is None else basis
        dim = Bm.shape[1]
        res = linprog(-(w @ Bm), A_ub=-Bm, b_ub=np.zeros(len(self.points)),
                      A_eq=[self.nu @ Bm], b_eq=[1.0], bounds=[(None, None)] * dim,
                      method="highs")
        if res.status == 3:
            return math.inf
        assert res.status == 0, res.message
        return -res.fun


def weights(sys_, paths, t, d, Bfun, mass_weight=True):
    w = np.zeros(len(sys_.points))
    for prob, c, y, R, M in paths:
        phi = math.log(Bfun(len(R), t, d)) + ((4.0 / 3.0) * t * M if mass_weight else 0.0)
        w[sys_.idx[y]] += prob * math.exp(-phi)
    return w


def lemma24_max_ratio(sys_, paths, t):
    """max_x E[W P_rho(y^rho = x|omega)] / nu(x)."""
    acc = np.zeros(len(sys_.points))
    for prob, c, y, R, M in paths:
        W = math.exp(-(4.0 / 3.0) * t * M)
        Rs = set(R)
        # distribution of y^rho: product over l of point masses / 2-point mixtures
        opts = []
        for l in range(sys_.N):
            if l in Rs:
                opts.append([(c[l], 1 - t), (y[l], t)])
            else:
                opts.append([(c[l], 1.0)])
        for combo in itertools.product(*opts):
            x = tuple(a for a, _ in combo)
            acc[sys_.idx[x]] += prob * W * math.prod(pp for _, pp in combo)
    return float(np.max(acc / sys_.nu))


# ---------------------------------------------------------------- generators

def rand_nus(rng, qs, heavy_frac=0.0):
    nus = []
    for q in qs:
        # one big symbol, the rest small (so activated sets can be light)
        small = [rng.uniform(0.02, 0.25) for _ in range(q - 1)]
        s = sum(small)
        if s > 0.6:
            small = [v * 0.6 / s for v in small]
        nus.append([1 - sum(small)] + small)
    return nus


def pattern_rule(rng, qs, r, npat, phantom=False):
    N = len(qs)
    pats = []
    for _ in range(npat):
        k = rng.randint(1, min(r, N))
        T = sorted(rng.sample(range(N), k))
        a = tuple(rng.randrange(1, qs[l]) if rng.random() < 0.8 else 0 for l in T)
        pats.append((T, a))

    def rule(l, c, y):
        F = set()
        for T, a in pats:
            if T[-1] != l:
                continue
            ok = True
            for i, ti in enumerate(T[:-1]):
                if phantom:
                    if a[i] != y[ti] and a[i] != c[ti]:
                        ok = False
                        break
                elif a[i] != y[ti]:
                    ok = False
                    break
            if ok:
                F.add(a[-1])
        return F
    return rule, pats


def table_rule(table):
    def rule(l, c, y):
        return table.get((l, c, y), frozenset())
    return rule


def random_table(rng, qs, p_act=0.5):
    """arbitrary rule: F_l depends on the full state (c_<l, y_<l)."""
    table = {}
    N = len(qs)
    for l in range(N):
        for c in itertools.product(*[range(q) for q in qs[:l]]):
            for y in itertools.product(*[range(q) for q in qs[:l]]):
                if rng.random() < p_act:
                    k = rng.randint(1, qs[l] - 1)
                    table[(l, c, y)] = frozenset(rng.sample(range(1, qs[l]), k))
    return table


def evaluate(sys_, d, ts, report_power=False):
    paths = sys_.paths()
    EM = sum(p * M for p, c, y, R, M in paths)
    basis = sys_.local_basis(d)
    out = {}
    tlist = list(ts) + [d / (EM + 4 * d)]
    worst = 0.0
    for t in tlist:
        w = weights(sys_, paths, t, d, Bstar)
        v = sys_.lp_value(w, d, basis)
        l24 = lemma24_max_ratio(sys_, paths, t)
        worst = max(worst, v)
        out[t] = (v, l24)
        assert v <= 1 + TOL, ("THM 2.5 VIOLATED", t, v)
        assert l24 <= 1 + TOL, ("LEMMA 2.4 VIOLATED", t, l24)
    power = None
    if report_power:
        t = tlist[-1]
        w0 = weights(sys_, paths, t, d, Bstar, mass_weight=False)
        v0 = sys_.lp_value(w0, d, basis)
        if d >= 1:
            w1 = weights(sys_, paths, t, d, lambda n, tt, dd: Bstar(n, tt, dd - 1))
            v1 = sys_.lp_value(w1, d, basis)
        else:
            v1 = float("nan")
        # unweighted comparison constant (informational): max E_sigma f / E_nu f
        wu = np.zeros(len(sys_.points))
        for p, c, y, R, M in paths:
            wu[sys_.idx[y]] += p
        vu = sys_.lp_value(wu, d, basis)
        power = (v0, v1, vu)
    return EM, worst, out, power


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    ntrials = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    rng = random.Random(seed)
    ts = [0.02, 0.1, 0.25]
    stats = {"maxval": 0.0, "max_noW": 0.0, "max_dm1": 0.0, "n": 0}
    for trial in range(ntrials):
        kind = ["plain", "phantom", "arbitrary"][trial % 3]
        N = rng.randint(3, 6)
        q = 2 if N >= 6 else rng.choice([2, 3])
        qs = [q] * N
        nus = rand_nus(rng, qs)
        deltas = [0.25] * N
        d = rng.randint(1, min(3, N))
        if kind == "arbitrary":
            if q == 3 and N > 4:
                N = 4
                qs, nus, deltas = qs[:4], nus[:4], deltas[:4]
            rule = table_rule(random_table(rng, qs, rng.uniform(0.3, 0.9)))
        else:
            rule, _ = pattern_rule(rng, qs, r=3, npat=rng.randint(2, 4 * N),
                                   phantom=(kind == "phantom"))
        S = System(qs, nus, deltas, rule, d)
        EM, worst, out, power = evaluate(S, d, ts, report_power=True)
        stats["n"] += 1
        stats["maxval"] = max(stats["maxval"], worst)
        stats["max_noW"] = max(stats["max_noW"], power[0])
        stats["max_dm1"] = max(stats["max_dm1"], power[1] if not math.isnan(power[1]) else 0)
        print(f"trial {trial:3d} {kind:9s} N={N} q={q} d={d} EM={EM:.3f} "
              f"maxLP={worst:.4f} [noW={power[0]:.4f} Bdeg(d-1)={power[1]:.4f} "
              f"unweighted C*={power[2]:.4f}]", flush=True)
    print("SUMMARY", stats)


if __name__ == "__main__" and len(sys.argv) <= 3:
    main()


def adversarial(seed, iters=150, N=5, q=2, d=2):
    """Hill-climb an arbitrary (full-state) activation table to maximise the
    Thm 2.5 LP value at t in {0.25, 0.1, d/(EM+4d)}; also maximise the
    unweighted constant for comparison."""
    rng = random.Random(seed)
    qs = [q] * N
    nus = rand_nus(rng, qs)
    # make many light-able symbols: small symbols of mass ~ 0.1-0.25 total
    deltas = [0.25] * N
    table = random_table(rng, qs, 0.7)
    keys = [(l, c, y) for l in range(N)
            for c in itertools.product(*[range(qq) for qq in qs[:l]])
            for y in itertools.product(*[range(qq) for qq in qs[:l]])]

    def score(tab, nus_):
        S = System(qs, nus_, deltas, table_rule(tab), d)
        paths = S.paths()
        EM = sum(p * M for p, c, y, R, M in paths)
        basis = S.local_basis(d)
        best = 0.0
        for t in (0.25, 0.1, d / (EM + 4 * d)):
            w = weights(S, paths, t, d, Bstar)
            best = max(best, S.lp_value(w, d, basis))
        return best, EM
    cur, EM = score(table, nus)
    for it in range(iters):
        tab2 = dict(table)
        nus2 = [list(v) for v in nus]
        for _ in range(rng.randint(1, 3)):
            k = rng.choice(keys)
            if rng.random() < 0.3:
                tab2.pop(k, None)
            else:
                kk = rng.randint(1, q - 1)
                tab2[k] = frozenset(rng.sample(range(1, q), kk))
        if rng.random() < 0.3:
            l = rng.randrange(N)
            nus2[l] = rand_nus(rng, [q])[0]
        sc, em = score(tab2, nus2)
        if sc >= cur:
            cur, EM, table, nus = sc, em, tab2, nus2
    assert cur <= 1 + TOL, ("THM 2.5 VIOLATED (adversarial)", cur)
    return cur, EM


if __name__ == "__main__" and len(sys.argv) > 3 and sys.argv[3] == "adv":
    for s in range(int(sys.argv[2])):
        for (N, q, d) in [(5, 2, 2), (4, 3, 2), (6, 2, 3), (5, 2, 1)]:
            v, em = adversarial(1000 * int(sys.argv[1]) + s, iters=120, N=N, q=q, d=d)
            print(f"adv seed={s} N={N} q={q} d={d}: max LP after hill-climb = {v:.6f} (EM={em:.3f})",
                  flush=True)


def stress(seed, ntr):
    """q = 2, nu(1) = 1/4 exactly (activation at the cap boundary p = delta),
    larger N, dense binary/ternary families and trigger-type families."""
    rng = random.Random(seed)
    for tr in range(ntr):
        N = rng.randint(7, 12)
        qs = [2] * N
        pm = rng.choice([0.25, 0.2, 0.1])
        nus = [[1 - pm, pm] for _ in range(N)]
        deltas = [0.25] * N
        d = rng.randint(1, 3)
        kind = rng.choice(["dense", "trigger", "chain", "arbitrary"])
        if kind == "dense":
            rule, _ = pattern_rule(rng, qs, r=3, npat=6 * N)
        elif kind == "trigger":
            # coordinate 0 (and maybe 1) trigger all later ones; plus chains
            pats = [([0, l], (1, 1)) for l in range(1, N)]
            pats += [([1, l], (rng.randrange(2), 1)) for l in range(2, N) if rng.random() < .5]

            def rule(l, c, y, pats=pats):
                return {a[-1] for T, a in pats if T[-1] == l and all(a[i] == y[T[i]] for i in range(len(T) - 1))}
        elif kind == "chain":
            pats = [([l - 1, l], (rng.randrange(2), 1)) for l in range(1, N)]
            pats += [([l - 2, l - 1, l], (rng.randrange(2), rng.randrange(2), 1)) for l in range(2, N)]

            def rule(l, c, y, pats=pats):
                return {a[-1] for T, a in pats if T[-1] == l and all(a[i] == y[T[i]] for i in range(len(T) - 1))}
        else:
            h = rng.getrandbits(64)

            def rule(l, c, y, h=h):
                return {1} if (hash((h, l, c, y)) & 3) != 0 else set()
        S = System(qs, nus, deltas, rule, d)
        EM, worst, out, power = evaluate(S, d, [0.02, 0.1, 0.25], report_power=True)
        print(f"stress {tr:3d} {kind:9s} N={N} pm={pm} d={d} EM={EM:.3f} maxLP={worst:.5f} "
              f"[noW={power[0]:.4f} Bdeg(d-1)={power[1]:.4f} unweighted C*={power[2]:.4f}]", flush=True)


if __name__ == "__main__" and len(sys.argv) > 3 and sys.argv[3] == "stress":
    stress(int(sys.argv[1]), int(sys.argv[2]))
