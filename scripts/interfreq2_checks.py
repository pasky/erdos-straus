"""O25 independent checks for EXCEPTIONAL_INTERFREQ2.
(1) Example 3.2: identity and hybrid charge 0 (N=20, mod 21).
(2) Lemma 4.1: window translates [1,N]+kL0 satisfy (2.1) on Z/Q'.
(3) Inequality (5.1) of Thm 5.2 for random nonnegative nu on Z/Q', using a flat F
    saved by interfreq2_flatF.py (N=20, L=100, t=0.1, C=2): checks
    (1+Delta) B_hyb >= M E nu - Delta T_mid + s0 W+_{>CN} with Delta, s0 measured.
Usage: python interfreq2_checks.py Fnpy
"""
import sys, random
import numpy as np
from math import gcd
from sympy import divisors

def u_(N, d): return -(-N // d)
def l_(N, d): return N // d

# (1)
N = 20
n = np.arange(21 * 50)
lhs = (n % 21 == 0).astype(int)
terms = [(1, 0, 7), (-1, 1, 3), (-1, 2, 3)] + [(1, b, 21) for b in range(1, 21) if b % 3 and b % 7]
rhs = sum(a * ((n - b) % d == 0) for a, b, d in terms)
assert (lhs == rhs).all()
charge = 0
for a, b, d in terms:
    c = sum(1 for m in range(1, N + 1) if (m - b) % d == 0)
    if 2 * d <= N: charge += a * c
    else: charge += a * (u_(N, d) if a > 0 else l_(N, d))
print("(1) Example 3.2 identity ok; hybrid charge =", charge, "; #patches =", len(terms) - 3)

# (2)
for N, Qp in [(20, 2520 * 11), (12, 60 * 7 * 11)]:
    L0 = 1
    for d in range(1, N // 2 + 1): L0 = L0 * d // gcd(L0, d)
    lam = np.zeros(Qp)
    for m in range(1, N + 1): lam[m % Qp] += 1
    ok = True
    for k in [1, 2, 5, 7]:
        mu = np.roll(lam, k * L0)
        for d in divisors(Qp):
            sums = np.add.reduceat(np.r_[mu.reshape(-1, d).sum(0)], [0]) if False else mu.reshape(-1, d).sum(0)
            ref = lam.reshape(-1, d).sum(0)
            if 2 * d <= N:
                ok &= np.allclose(sums, ref)
            else:
                ok &= (sums >= l_(N, d) - 1e-9).all() and (sums <= u_(N, d) + 1e-9).all()
    print(f"(2) N={N} Q'={Qp}: translates feasible: {ok}")

# (3)
if len(sys.argv) > 1:
    pts, F = np.load(sys.argv[1])
    pts = pts.astype(int)
    N, t, C = 20, 0.1, 2.0
    M = t * N
    Qp = 2520 * 11 * 13
    Fq = np.zeros(Qp)
    for x, v in zip(pts, F): Fq[x % Qp] += v
    lam = np.zeros(Qp)
    for m in range(1, N + 1): lam[m % Qp] += 1
    divs = divisors(Qp)
    Fcls = {d: Fq.reshape(-1, d).sum(0) for d in divs}
    ccls = {d: lam.reshape(-1, d).sum(0) for d in divs}
    # measured Delta, s0
    Delta = max(abs(Fcls[d] - M / d).max() for d in divs if N / 2 < d <= C * N)
    s0 = min((Fcls[d] - M / d)[ccls[d] > 0].min() for d in divs if d > C * N)
    f4 = min((Fcls[d] - M / d + 1)[ccls[d] == 0].min() for d in divs if d > C * N)
    f2 = max(abs(Fcls[d] - M / d).max() for d in divs if 2 * d <= N)
    print(f"(3) on Z/{Qp}: (F2) err {f2:.2e}, Delta={Delta:.3f}, s0={s0:.4f}, (F4) min {f4:.4f}, F<=1_[1,N]: {(Fq <= lam + 1e-9).all()}")
    rng = random.Random(1)
    worst = 1e9
    for trial in range(200):
        terms = []
        for _ in range(rng.randint(3, 30)):
            d = rng.choice(divs[1:]); b = rng.randrange(d); a = rng.uniform(-3, 3)
            terms.append((a, b, d))
        nu = np.zeros(Qp)
        for a, b, d in terms: nu[b::d] += a
        const = max(0.0, -nu.min()) + rng.uniform(0, 0.5)
        terms.append((const, 0, 1)); nu += const
        B = 0.0; Tmid = 0.0; Wp = 0.0; Enu = nu.mean()
        for a, b, d in terms:
            c = ccls[d][b]
            if 2 * d <= N: B += a * c; continue
            u, l = u_(N, d), l_(N, d)
            B += a * (u if a > 0 else l)
            right = (a > 0 and c == u) or (a < 0 and c == l)
            if N / 2 < d <= C * N and right: Tmid += abs(a)
            if d > C * N and a > 0 and c == u: Wp += a
            if d > N and a < 0 and c == l: pass
        # Lemma 5.0 drop of free negatives is implicit: they only increase the RHS slack
        lhs = (1 + Delta) * B; rhs = M * Enu - Delta * Tmid + s0 * Wp
        worst = min(worst, lhs - rhs)
    print(f"(3) random nu >= 0 (200 trials): min[(1+Delta)B - (M E nu - Delta T_mid + s0 W+)] = {worst:.4f}")
