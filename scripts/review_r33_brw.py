"""R33 from-scratch check of §5: BRW sandwich (Lemma 5.3), Efron-Stein projection
(eq. energy), the c_W expansion of Lemma 5.4, the cell-expanded B, and the twist
bound mechanism of Lemma 5.5, on small random product systems (exact enumeration)."""
import itertools, random, math
import numpy as np

rng = random.Random(1)

def run(trial):
    N = rng.randint(2, 4)
    sizes = [rng.randint(2, 4) for _ in range(N)]
    pts = list(itertools.product(*[range(s) for s in sizes]))
    P = 1.0 / len(pts)
    k = rng.randint(1, 2)
    m = rng.randint(1, 6)
    events = []
    for _ in range(m):
        supp = sorted(rng.sample(range(N), rng.randint(1, k)))
        events.append({l: rng.randrange(sizes[l]) for l in supp})
    t = rng.randint(0, N)
    occ = lambda E, x: all(x[l] == v for l, v in E.items())

    def cond_exp(phi, W, x):  # E[phi | X_W = x_W]
        vals = [phi(y) for y in pts if all(y[l] == x[l] for l in W)]
        return sum(vals) / len(vals)

    def proj_le_t(phi, coords):
        # Efron-Stein low part via c_W formula of Lemma 5.4, on coordinates `coords`
        Np = len(coords)
        terms = []
        for s in range(0, min(t, Np) + 1):
            for W in itertools.combinations(coords, s):
                cW = sum((-1) ** i * math.comb(Np - s, i) for i in range(0, t - s + 1))
                terms.append((cW, W))
        cache = {}
        def u(x):
            key = x
            if key not in cache:
                cache[key] = sum(cW * cond_exp(phi, W, x) for cW, W in terms)
            return cache[key]
        return u, terms

    us, Fj_list = [], []
    for j, Ej in enumerate(events):
        outside = [l for l in range(N) if l not in Ej]
        def Fj(x, j=j, Ej=Ej):
            y = list(x)
            for l, v in Ej.items(): y[l] = v
            return float(all(not occ(events[i], y) for i in range(j)))
        u, _ = proj_le_t(Fj, outside)
        us.append(u); Fj_list.append((Fj, outside))

    # check u_j is the L2-best approx by sums of <=t-coordinate functions (least squares)
    for j, (Fj, outside) in enumerate(Fj_list):
        cols = []
        for s in range(0, min(t, len(outside)) + 1):
            for W in itertools.combinations(outside, s):
                for vals in itertools.product(*[range(sizes[l]) for l in W]):
                    cols.append([float(all(x[l] == v for l, v in zip(W, vals))) for x in pts])
        Amat = np.array(cols).T
        y = np.array([Fj(x) for x in pts])
        coef, *_ = np.linalg.lstsq(Amat, y, rcond=None)
        best = np.mean((Amat @ coef - y) ** 2)
        mine = np.mean([(Fj(x) - us[j](x)) ** 2 for x in pts])
        assert abs(best - mine) < 1e-9, (best, mine)

    lhs = rhs = 0.0
    for x in pts:
        A = [float(occ(E, x)) for E in events]
        F = float(all(a == 0 for a in A))
        Fl = [float(all(A[i] == 0 for i in range(j))) for j in range(m)]
        u = [us[j](x) for j in range(m)]
        v = [sum(A[j] * u[j] for j in range(i)) for i in range(m)]
        B = 1 - sum(A[i] * (1 - v[i]) ** 2 for i in range(m))
        assert B <= F + 1e-12
        ident = sum(A[i] * sum(A[j] * (Fl[j] - u[j]) for j in range(i)) ** 2 for i in range(m))
        assert abs((F - B) - ident) < 1e-9
        lhs += P * (F - B)
    for j, (Fj, outside) in enumerate(Fj_list):
        pE = 1.0 / math.prod(sizes[l] for l in events[j])
        en = np.mean([(Fj(x) - us[j](x)) ** 2 for x in pts])
        rhs += pE * en
    assert lhs <= m * m * rhs + 1e-12
    return lhs, m * m * rhs

worst = 0
for tr in range(300):
    a, b = run(tr)
    if b > 0: worst = max(worst, a / b)
print("300 trials OK: B<=F, identity, E[F-B] <= m^2 sum P En; c_W projection = least squares; max ratio", worst)

# Lemma 6.2(c) density ratio: (1-1/(4n))^{-n} <= 4/3, and exact per-coordinate ratio
assert all((1 - 1 / (4 * n)) ** (-n) <= 4 / 3 + 1e-15 for n in range(1, 10000))
for q in range(1, 300):
    for b in range(1, 14):
        if 2 ** b < 4 * q: continue
        fib = [sum(1 for u in range(2 ** b) if (q * u) >> b == a) for a in range(q)]
        assert min(fib) >= 1 and max(fib) - min(fib) <= 1
        assert max(2 ** b / (q * f) for f in fib) <= 1 / (1 - q / 2 ** b) + 1e-12
print("density-ratio checks OK")
