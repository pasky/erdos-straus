"""R269 from-scratch check of BALANCED_LATTICE Lemma 1.1 / Prop 1.3 / Cor 1.4.

For random primes q = 3 (mod 8) and S = odd primes <= y, computes independently
  * a = discrete logs of s^2 in U_q = (F_q^*)^2 w.r.t. a generator g,
  * D_min = min_{j != 0 mod N} sum_s ||j a_s / N||   (exact rational, integer arithmetic),
  * lambda_1^{(1)}(Lambda*) by enumerating Lambda* via an HNF basis of Lambda and its inverse transpose
    (independent of the character picture),
  * L_min = least L with {sum_s j_s a_s : 0<=j_s<=L} = Z/N (discrete covering),
  * mu_inf(Lambda) (cube covering radius) on a grid (1/m)Z^k: lower bound mu_lo, upper mu_lo + 1/(2m),
and checks 1/(2 min(1,D)) <= mu_inf <= k^{3/2}/(2 min(1,D)),  L_min+1 >= 1/min(1,D),  L_min <= ceil(k^{3/2}/min(1,D)),
Minkowski D_min <= (k!/N)^{1/k} (N > k!).
Usage: PYTHONPATH=scripts uv run --with sympy --with numpy python scripts/review_r269_transference.py y QLO QHI NSAMP M SEED
"""
import sys, math, random, itertools
import numpy as np
from sympy import isprime, primerange, primitive_root, Matrix


def dlogs(q, S):
    N = (q - 1) // 2
    g = pow(primitive_root(q), 2, q)
    tab = np.empty(q, dtype=np.int64)
    x = 1
    for i in range(N):
        tab[x] = i
        x = x * g % q
    return N, [int(tab[s * s % q]) for s in S]


def dmin(N, a):
    j = np.arange(1, N, dtype=np.int64)
    tot = np.zeros(N - 1, dtype=np.int64)
    for s in a:
        r = (j * s) % N
        tot += np.minimum(r, N - r)
    i = int(np.argmin(tot))
    return int(tot[i]), N  # D_min = tot/N


def lmin(N, a):
    def covers(L):
        R = np.zeros(N, dtype=bool); R[0] = True
        for s in a:
            acc = R.copy(); cur = R
            for _ in range(L):
                cur = np.roll(cur, s % N); acc |= cur
            R = acc
        return R.all()
    if math.gcd(math.gcd(*a), N) != 1 if len(a) > 1 else math.gcd(a[0], N) != 1:
        return None
    L = 1
    while not covers(L):
        L *= 2
    lo, hi = L // 2, L
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if covers(mid): hi = mid
        else: lo = mid
    return hi if hi >= 1 and covers(hi) else lo


def lam1_dual_l1(N, a):
    """lambda_1 in l1 of Lambda*, Lambda = {x : a.x = 0 mod N}; via kernel basis + inverse transpose."""
    k = len(a)
    # basis of Lambda: rows of HNF-ish generating set {N e_i} U {e_i - c_i e_0 ...}; use sympy on generators
    # rows (a_i | e_i) and (N | 0); eliminate first column by integer gcd steps; rows with first coord 0 = basis of Lambda
    rows = [[int(a[i])] + [1 if j == i else 0 for j in range(k)] for i in range(k)] + [[N] + [0] * k]
    while sum(1 for r in rows if r[0] != 0) > 1:
        nz = sorted([r for r in rows if r[0] != 0], key=lambda r: abs(r[0]))
        piv = nz[0]
        rows = [r for r in rows if r[0] == 0] + [piv]
        for r in nz[1:]:
            t = r[0] // piv[0]
            rows.append([x - t * y for x, y in zip(r, piv)])
    B = Matrix([r[1:] for r in rows if r[0] == 0])
    assert B.rows == k, B
    B = B.lll()
    Bd = (B.inv()).T  # dual basis rows
    det = abs(B.det())
    # enumerate dual points y = c.Bd with |y|_1 <= 1: points of Lambda* in [-1,1]^k are integer shifts of
    # the |det| coset reps; get reps as frac of c.Bd over c in Z^k/Bd-index -> use Smith-free approach:
    # coset reps of Lambda*/Z^k = {frac(t a/N)} is the character claim we want to TEST, so instead enumerate
    # c in a box large enough: coordinates of y in [-1,1] => c = y.B^T bounded by |B| row norms.
    bound = [max(abs(int(x)) for x in B.row(i)) for i in range(k)]  # |c_i| = |y.B_i| <= |B_i|_inf*|y|_1
    Bdf = np.array(Bd.tolist(), dtype=object)
    best = None
    rng = [range(-b, b + 1) for b in bound]
    # vectorised enumeration over the product box (small for k<=4 if B is reduced)
    Bn = np.array([[float(x) for x in row] for row in Bd.tolist()])
    grids = np.array(np.meshgrid(*[np.arange(-b, b + 1) for b in bound], indexing='ij')).reshape(k, -1).T
    Y = grids @ Bn
    n1 = np.abs(Y).sum(axis=1)
    n1[np.all(grids == 0, axis=1)] = np.inf
    return float(n1.min()), int(det), int(np.prod([2 * b + 1 for b in bound]))


def mu_inf(N, a, R, m):
    k = len(a)
    ax = np.arange(-R, R + 1)
    V = np.array(np.meshgrid(*[ax] * k, indexing='ij')).reshape(k, -1).T
    cls = (V @ np.array(a, dtype=np.int64)) % N
    worst = 0.0
    for f in itertools.product(range(m), repeat=k):
        d = np.abs(V + np.array(f) / m).max(axis=1)
        best = np.full(N, np.inf)
        np.minimum.at(best, cls, d)
        worst = max(worst, best.max())
    return worst


def main():
    y, qlo, qhi, ns, m, seed = map(int, sys.argv[1:7])
    S = list(primerange(3, y + 1)); k = len(S)
    rnd = random.Random(seed)
    viol = 0; rows = []
    tries = 0
    while len(rows) < ns and tries < 100 * ns:
        tries += 1
        q = rnd.randrange(qlo, qhi) | 3
        if q % 8 != 3 or not isprime(q) or q in S: continue
        N, a = dlogs(q, S)
        tot, _ = dmin(N, a)
        D = tot / N
        Lm = lmin(N, a)
        l1, det, nenum = lam1_dual_l1(N, a)
        mn = min(1.0, D)
        ok1 = abs(l1 - mn) < 1e-9 and det == N // math.gcd(N, math.gcd(*a))
        if D == 0:
            rows.append((q, N, D, None, None, None, 'degenerate H!=U_q', l1, det)); continue
        R = (Lm + 1) // 2 + 2
        mu = mu_inf(N, a, R, m)
        lo_ok = mu + 1 / (2 * m) >= 1 / (2 * mn) - 1e-12
        hi_ok = mu <= k ** 1.5 / (2 * mn) + 1e-12
        L_ok = (Lm + 1 >= 1 / mn - 1e-12) and (Lm <= math.ceil(k ** 1.5 / mn))
        mink = (N <= math.factorial(k)) or D <= (math.factorial(k) / N) ** (1 / k) + 1e-12
        ok = ''.join(c for c,f in zip('dlhLM',(ok1,lo_ok,hi_ok,L_ok,mink)) if not f) or True
        viol += (ok is not True)
        rows.append((q, N, D, Lm, mu, mu * mn, ok, l1))
    print(f"y={y} k={k} m={m} samples={len(rows)} violations={viol}")
    print("q N Dmin Lmin mu_lo mu*min(1,D) [k^1.5/2=%.2f] ok" % (k ** 1.5 / 2))
    for r in rows:
        print(*[(f"{x:.4f}" if isinstance(x, float) else x) for x in r])
    prods = [r[5] for r in rows if r[5] is not None]
    if prods:
        print("mu*D range: min %.3f max %.3f (lower bound 0.5, upper k^1.5/2 = %.2f)" % (min(prods), max(prods), k ** 1.5 / 2))


if __name__ == '__main__':
    main()
