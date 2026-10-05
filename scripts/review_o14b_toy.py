"""R49b from-scratch checks for POINTWISE_OMEGA14 §4 (written independently of omega14_planting.py).

A: Lemma 4.2 uniqueness + exact R(x) identity on a toy instance.
B: Lemma 4.4 W(v,a) >= L^2/(200 v) numerically (no exceptional set), small X.
C: Lemma 4.3 toy: min over classes b of phi(q)*sum_{l=b (q), l in (Y^.6,Y^.7]} 1/(l-1).
D: Lemma 4.1 / Thm 1.3 toy LP: max E B over B in V_k, B<=F, with planting threshold met
   for every small value (expect <= 0) vs not met (positive possible).
"""
import sys, itertools, math
from math import gcd
import numpy as np


def primes_upto(N):
    s = np.ones(N + 1, dtype=bool); s[:2] = False
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0]


def sqfree(n):
    d = 2
    while d * d <= n:
        if n % (d * d) == 0: return False
        d += 1
    return True


def dstar(D):
    r, d, m = 1, 2, D
    while d * d <= m:
        e = 0
        while m % d == 0: m //= d; e += 1
        r *= d ** ((e + 1) // 2); d += 1
    return r * m


def part_A():
    # toy: V<=n<=X, small v<=V y-rough sqfree (y=3 -> v coprime to 2,3), l primes in (Lo,Hi] with Lo > X^2
    V, X, y = 5, 12, 3
    vs = [v for v in range(1, V + 1) if sqfree(v) and all(v % p for p in range(2, y + 1))]
    Ds = [D for D in range(1, X * X + 1) if V <= dstar(D) <= X]
    P = [int(p) for p in primes_upto(4000) if p > X * X]
    viol = 0
    for l in P:
        for D in Ds:
            n = dstar(D)
            c = [v for v in vs if (v * l) % (4 * n) == 4 * n - 1]
            if len(c) > 1: viol += 1
    # R(x) identity: x = residues mod primes of vs (only primes 5 here)
    smallp = sorted({p for v in vs for p in range(2, v + 1) if v % p == 0 and all(p % q for q in range(2, p))})
    maxerr = 0.0
    for xs in itertools.product(*[range(1, p) for p in smallp]):
        xmap = dict(zip(smallp, xs))
        def holds(v, D):
            return all((xmap[p] + 4 * D) % p == 0 for p in smallp if v % p == 0)
        # direct: p_l(x) = (#classes mod l hit)/(l-1)
        direct = 0.0
        for l in P:
            cls = set()
            for D in Ds:
                n = dstar(D)
                for v in vs:
                    if (v * l) % (4 * n) == 4 * n - 1 and holds(v, D):
                        cls.add((-4 * D) % l)
            direct += len(cls) / (l - 1)
        formula = 0.0
        for v in vs:
            for D in Ds:
                n = dstar(D)
                if gcd(v, 2 * n) > 1 or not holds(v, D): continue
                b = (-pow(v, -1, 4 * n)) % (4 * n)
                formula += sum(1 / (l - 1) for l in P if l % (4 * n) == b)
        maxerr = max(maxerr, abs(direct - formula))
    print(f"A: uniqueness violations={viol} (|P|={len(P)}, |D|={len(Ds)}); R(x) identity max err={maxerr:.2e}")
    assert viol == 0 and maxerr < 1e-9


def part_B(X=10 ** 6, y=7, vmax=60):
    # W(v,a) over D with n_D in [V,X], V=X^(1/3); compare to L^2/(200v). Enumerate D=kappa t^2.
    L = math.log(X); V = round(X ** (1 / 3))
    mu = np.ones(X + 1, dtype=np.int8)  # squarefree indicator
    for p in primes_upto(int(X ** 0.5) + 1):
        mu[p * p::p * p] = 0
    mu[0] = 0
    phi = np.arange(X + 1, dtype=np.float64)
    for p in primes_upto(X):
        phi[p::p] *= (1 - 1 / p)
    kap = np.nonzero(mu)[0]
    vs = [v for v in range(1, vmax + 1) if v % 2 and sqfree(v) and all(v % p for p in range(2, y + 1))]
    Ws = {v: np.zeros(v) for v in vs}
    for t in range(1, int(X ** 0.5) + 1):
        kk = kap[(kap * t >= V) & (kap * t <= X)]
        if kk.size == 0: continue
        n = kk * t
        w = 1 / (np.where(n % 2 == 0, 4 * phi[n], 2 * phi[n]))  # phi(4n)
        for v in vs:
            Ws[v] += np.bincount((kk % v) * (t * t % v) % v, weights=w, minlength=v)
    worst = 1e9
    for v in vs:
        r = min(Ws[v][a] for a in range(v) if gcd(a, v) == 1) * v / L ** 2
        worst = min(worst, r)
        print(f"B: X={X} v={v:3d} min_a W(v,a)*v/L^2 = {r:.4f}  (claim >= 0.005)")
    assert worst >= 0.005


def part_C(lo=10 ** 6, hi=10 ** 7, nmax=30):
    P = primes_upto(hi); P = P[P > lo].astype(np.int64)
    w = 1 / (P - 1.0)
    worst = 1e9
    for n in range(1, nmax + 1):
        q = 4 * n
        S = np.bincount(P % q, weights=w, minlength=q)
        ph = sum(1 for b in range(q) if gcd(b, q) == 1)
        m = min(S[b] for b in range(q) if gcd(b, q) == 1) * ph
        worst = min(worst, m)
    print(f"C: primes in ({lo},{hi}]: min_n<= {nmax} min_b phi(4n)*c = {worst:.4f}; log(7/6)={math.log(7/6):.4f}, "
          f"log(log hi/log lo)={math.log(math.log(hi)/math.log(lo)):.4f}")


def lp_maxEB(S, n, m, Omega, k):
    from scipy.optimize import linprog
    # Omega[s][b] = set of bad values of big coord b; uniform laws; s uniform
    Ks = list(itertools.combinations(range(n), k))
    var = {}
    for K in Ks:
        for s in range(S):
            for vals in itertools.product(range(m), repeat=k):
                var[(K, s, vals)] = len(var)
    N = len(var); prob = 1 / (S * m ** n)
    c = np.zeros(N)
    rows, rhs = [], []
    for s in range(S):
        for X in itertools.product(range(m), repeat=n):
            F = 0 if any(X[b] in Omega[s][b] for b in range(n)) else 1
            row = np.zeros(N)
            for K in Ks:
                j = var[(K, s, tuple(X[b] for b in K))]
                row[j] += 1; c[j] -= prob
            rows.append(row); rhs.append(F)
    res = linprog(c, A_ub=np.array(rows), b_ub=np.array(rhs), bounds=[(-50, 50)] * N, method="highs")
    assert res.status == 0
    return -res.fun


def part_D():
    m, n, S = 2, 8, 2
    for k in (1, 2):
        # case 1: every s has all 8 bits with p=1/2 -> r=1, R=8 >= (k+1)+(2k+1)
        Om1 = [[{0}] * n for _ in range(S)]
        # case 2: s=1 has only k active bits (R=k < threshold): F|s=1 is a k-junta
        Om2 = [[{0}] * n, [{0}] * k + [set()] * (n - k)]
        v1, v2 = lp_maxEB(S, n, m, Om1, k), lp_maxEB(S, n, m, Om2, k)
        thr = (k + 1) + (2 * k + 1) * 1
        print(f"D: k={k} thr={thr}: all-R=8 -> max E B={v1:.3e} (expect <=0);  one s with R=k -> {v2:.3e}")
        assert v1 <= 1e-9 and v2 > 1e-6
    # m=3 (p=1/3, r=1/2), n=7: R=3.5 meets k=1 threshold 2+3*0.5=3.5 exactly
    Om = [[{0}] * 7 for _ in range(2)]
    v = lp_maxEB(2, 7, 3, Om, 1)
    print(f"D: m=3,n=7,k=1 (R=3.5=thr): max E B={v:.3e}"); assert v <= 1e-9


if __name__ == "__main__":
    parts = sys.argv[1:] or ["A", "B", "C", "D"]
    for p in parts:
        {"A": part_A, "B": part_B, "C": part_C, "D": part_D}[p]()
