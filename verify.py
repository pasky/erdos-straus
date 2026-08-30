#!/usr/bin/env python3
"""Erdős–Straus conjecture: numerical companion to notes.md.

All computations are cheap (seconds). We verify:
  (a) the Case-B/Case-A witness criterion resolves every prime p < LIMIT,
      recording minimal witnesses;
  (b) explicit solutions reconstructed from witnesses are exact (Fraction check);
  (c) the Jacobi obstruction lemma is consistent with observed witness failures;
  (d) a concrete finite system of "guaranteed" congruence families covers all
      primes except a residue concentrated in the six square classes mod 840,
      and every leftover prime is nevertheless solvable (factorization luck);
  (e) the classical identity families are exactly valid (symbolic spot checks).
"""
from fractions import Fraction
from sympy import primerange, factorint, jacobi_symbol, primitive_root
from collections import Counter
from itertools import combinations, product as cartesian_product
from math import gcd, lcm, log, exp, ceil, prod, isqrt
import cmath

LIMIT = 100_000
SIX = {1, 121, 169, 289, 361, 529}  # squares of units mod 840, all ≡ 1 mod 24


def divisors_of_square(x):
    f = factorint(x)
    divs = [1]
    for r, e in f.items():
        divs = [d * r**k for d in divs for k in range(2 * e + 1)]
    return divs


def caseB_witness(p, qmax=400):
    """Smallest q ≡ -p (mod 4) with a divisor d | x², x=(p+q)/4, q | d+x."""
    q0 = (-p) % 4
    for q in range(q0, qmax + 1, 4):
        if q == 0:
            continue
        x = (p + q) // 4
        for d in sorted(divisors_of_square(x)):
            if (d + x) % q == 0:
                return q, d, x
    return None


def caseB_failed_qs(p, qfound):
    q0 = (-p) % 4
    return [q for q in range(q0, qfound, 4) if q != 0]


def caseB_solution(p, q, d, x):
    y1 = (x + d) // q
    z1 = (x + x * x // d) // q
    return (x, p * y1, p * z1)


def check_solution(p, sol):
    x, y, z = sol
    assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p), (p, sol)


# ---------------------------------------------------------------- (a)+(b)
print("== (a) witness search over all primes 3 <= p < %d ==" % LIMIT)
minq = {}
worst = (0, 0)
six_primes = []
for p in primerange(3, LIMIT):
    w = caseB_witness(p)
    assert w is not None, f"no Case-B witness for {p} below qmax -- investigate!"
    q, d, x = w
    minq[p] = w
    sol = caseB_solution(p, q, d, x)
    check_solution(p, sol)          # (b) every reconstructed solution exact
    if q > worst[1]:
        worst = (p, q)
    if p % 840 in SIX:
        six_primes.append(p)
print(f"all primes solvable; every reconstructed solution verified exactly")
print(f"worst minimal q: p={worst[0]}, q={worst[1]}")

hist = Counter(minq[p][0] for p in six_primes)
print(f"\nprimes in the six hard classes mod 840: {len(six_primes)}")
print("minimal-q histogram (hard classes):",
      dict(sorted(hist.items())[:10]), "... max q =", max(hist))

p = 1201  # stubborn example from the play session
q, d, x = minq[p]
print(f"\np=1201 witness: q={q}, d={d}, x={x}, solution {caseB_solution(p,q,d,x)}")

# ---------------------------------------------------------------- (c)
print("\n== (c) Jacobi obstruction lemma consistency (hard-class primes) ==")
jac_obstructed = coset_miss = 0
for p in six_primes:
    qf = minq[p][0]
    for q in caseB_failed_qs(p, qf):
        x = (p + q) // 4
        if all(jacobi_symbol(r, q) == 1 for r in factorint(x)):
            jac_obstructed += 1     # provably no witness for this q (Lemma)
        else:
            coset_miss += 1         # QNR factor exists but coset still missed
tot = jac_obstructed + coset_miss
print(f"failed (p,q) pairs: {tot}; Jacobi-obstructed: {jac_obstructed} "
      f"({100*jac_obstructed/tot:.1f}%), coset-miss: {coset_miss}")

# sanity: the lemma claims Jacobi obstruction => no witness. Verify directly on
# a sample: recheck that no divisor works for obstructed pairs.
sample = 0
for p in six_primes[:200]:
    qf = minq[p][0]
    for q in caseB_failed_qs(p, qf):
        x = (p + q) // 4
        if all(jacobi_symbol(r, q) == 1 for r in factorint(x)):
            assert not any((d0 + x) % q == 0 for d0 in divisors_of_square(x))
            sample += 1
print(f"lemma re-verified directly on {sample} obstructed pairs")

# ---------------------------------------------------------------- (d)
print("\n== (d) coverage by guaranteed congruence families ==")


def rad_root(d):
    return 1 if d == 1 else __import__("math").prod(
        r ** -(-e // 2) for r, e in factorint(d).items())


families = []
for q in range(1, 60, 2):                    # constant-(q,d) Case-B families
    for d in range(1, 101):
        families.append(("B", q, d, rad_root(d)))
for j in range(1, 51):                       # linear d=1 families p≡-4 (4j-1)
    families.append(("L", 4 * j - 1, None, None))
for u in range(1, 21):                       # F1: p ≡ -(u+v) (mod 4uv)
    for v in range(u, 21):
        families.append(("F1", 4 * u * v, u + v, None))


def covered(p):
    for kind, a, b, c in families:
        if kind == "B":
            q, d, R = a, b, c
            if (p + q) % 4 == 0:
                x = (p + q) // 4
                if x % R == 0 and (x + d) % q == 0:
                    return True
        elif kind == "L":
            if p % a == (-4) % a and p > a:
                return True
        else:
            m, s = a, b
            if p % m == (-s) % m and p > m:
                return True
    return False


unc = [p for p in primerange(3, LIMIT) if not covered(p)]
cls = Counter(p % 840 for p in unc)
n_six = sum(1 for p in primerange(3, LIMIT) if p % 840 in SIX)
print(f"primes uncovered by the finite family system: {len(unc)} "
      f"of {len(minq)} ({100*len(unc)/len(minq):.2f}%)")
print("their classes mod 840:", dict(cls.most_common(8)))
print("all uncovered classes inside six hard classes?",
      set(cls) <= SIX)
print(f"(for scale: {n_six} primes < {LIMIT} lie in the six classes; "
      f"{n_six - sum(cls[c] for c in SIX)} of them got covered 'accidentally')")
# every uncovered prime is still solvable (checked in (a)); state it:
print("every uncovered prime nevertheless has a witness (checked in (a))")

# ---------------------------------------------------------------- (e)
print("\n== (e) identity family exactness (symbolic) ==")
from sympy import symbols, simplify, Rational

g, u, v = symbols("g u v", positive=True)
pF1 = 4 * g * u * v - u - v
expr = 1 / (g * u * v) + 1 / (pF1 * g * u) + 1 / (pF1 * g * v) - 4 / pF1
assert simplify(expr) == 0
print("F1: p = 4guv - u - v  =>  4/p = 1/(guv) + 1/(pgu) + 1/(pgv)   [exact]")

k = symbols("k", positive=True)
pm3 = 3 * k - 1  # p ≡ 2 (mod 3), k = (p+1)/3
expr = 1 / pm3 + 1 / k + 1 / (k * pm3) - 4 / pm3
assert simplify(expr) == 0
print("mod 3: p = 3k-1  =>  4/p = 1/p + 1/k + 1/(kp)                 [exact]")

h = symbols("h", positive=True)
pm4 = 4 * h - 1  # p ≡ 3 (mod 4), h = (p+1)/4
expr = 1 / h + 1 / (2 * h * pm4) + 1 / (2 * h * pm4) - 4 / pm4
assert simplify(expr) == 0
print("mod 4: p = 4h-1  =>  4/p = 1/h + 1/(2hp) + 1/(2hp)            [exact]")
# ---------------------------------------------------------------- (f)
print("\n== (f) Phase-1 necessary slices and distinct affine roots ==")


def signed_residues(n, w):
    """Products ∏ ell^k mod w over -e <= k <= e for ell^e || n."""
    residues = {1}
    for ell, e in factorint(n).items():
        powers = {pow(ell, k, w) for k in range(-e, e + 1)}
        residues = {(a * b) % w for a in residues for b in powers}
    return residues


def direct_target_hit(n, w):
    return any((d + n) % w == 0 for d in divisors_of_square(n))


slice_checks = centered_checks = 0
phase_moduli = (3, 7, 11, 15, 19, 23, 27, 31)
for p in primerange(5, 5000):
    if p % 24 != 1:
        continue
    for w in phase_moduli:
        if p <= w:
            continue
        for n in ((p + w) // 4, (p * w + 1) // 4):
            assert gcd(n, w) == 1
            centered = (w - 1) in signed_residues(n, w)
            assert centered == direct_target_hit(n, w)
            centered_checks += 1
            a = n % w
            for ell in factorint(n):
                candidates = []
                if ell % w == w - 1:
                    candidates.append(n * ell)
                if ell % w == (-a) % w:
                    candidates.append(ell)
                if ell * ell % w == (-a) % w:
                    candidates.append(ell * ell)
                for d in candidates:
                    assert n * n % d == 0 and (d + n) % w == 0
                    slice_checks += 1
print(f"necessary-slice witnesses checked: {slice_checks}; "
      f"centered equivalences: {centered_checks}")

# Full avoidance is not multiplicative, even after the target is fixed.
assert (6 not in signed_residues(8, 7)
        and 6 not in signed_residues(15, 7)
        and 6 in signed_residues(120, 7))
print("nonmultiplicativity mod 7: F(8)=F(15)=1 but F(120)=0")

# Condition on p = r (mod M) and check the determinant-based assertion that
# every active root is distinct at primes ell > W^2.
ws = (3, 7, 11, 15)
W = max(ws)
L = lcm(*ws)
M = lcm(24, 4 * L)
R = M // 4
r = 1
root_checks = 0
for ell in primerange(W * W + 1, W * W + 500):
    roots = {(-r * pow(M, -1, ell)) % ell}  # primality form Mt+r
    expected = 1
    for w in ws:
        cb = {(-1) % w, (-r * pow(4, -1, w)) % w}
        ca = {(-1) % w, (-pow(4, -1, w)) % w}
        if ell % w in cb:
            roots.add((-(r + w) // 4 * pow(R, -1, ell)) % ell)
            expected += 1
        if ell % w in ca:
            roots.add((-(w * r + 1) // 4 * pow(w * R, -1, ell)) % ell)
            expected += 1
    assert len(roots) == expected
    root_checks += 1
print(f"distinct local-root counts checked at {root_checks} primes > W^2")

# Numerical sanity for the Markov truncation in Lemma 12.1.
sieve_primes = (11, 13, 17, 19)
nu = {11: 2, 13: 1, 17: 3, 19: 2}
gfun = {ell: nu[ell] / (ell - nu[ell]) for ell in sieve_primes}
Lambda = sum(nu[ell] * log(ell) / ell for ell in sieve_primes)
Q = ceil(exp(2 * Lambda))
Z = prod(1 + gfun[ell] for ell in sieve_primes)
H = 0.0
for j in range(len(sieve_primes) + 1):
    for subset in combinations(sieve_primes, j):
        q = prod(subset)
        if q <= Q:
            H += prod(gfun[ell] for ell in subset)
assert H + 1e-12 >= Z / 2
print(f"large-sieve truncation sanity: H(Q)/Z={H/Z:.3f} >= 1/2")

# ---------------------------------------------------------------- (g)
print("\n== (g) Phase-2 signed products and Fourier reduction ==")

# Check Fourier inversion and the character averages (12.12) in cyclic unit
# groups.  This is numerical verification, not an input to the proof.
fourier_checks = 0
for w in (7, 11, 19):
    h = w - 1
    gen = primitive_root(w)
    dlog = {}
    cur = 1
    for j in range(h):
        dlog[cur] = j
        cur = cur * gen % w

    def chi(j, value):
        return cmath.exp(2j * cmath.pi * j * dlog[value % w] / h)

    for j in range(1, h):
        avg = sum(abs((1 + chi(j, value) + chi(j, value).conjugate()) / 3) ** 2
                  for value in range(1, w)) / h
        order = h // gcd(j, h)
        target_avg = 5 / 9 if order == 2 else 1 / 3
        assert abs(avg - target_avg) < 1e-10

    for p in list(primerange(max(w + 1, 25), 300))[:12]:
        if p % 4 != 1:
            continue
        n = (p + w) // 4
        copies = [ell % w for ell, e in factorint(n).items() for _ in range(e)]
        counts = {1: 1}
        for value in copies:
            nxt = Counter()
            for old, count in counts.items():
                for power in (-1, 0, 1):
                    nxt[old * pow(value, power, w) % w] += count
            counts = nxt
        direct_prob = counts.get(w - 1, 0) / (3 ** len(copies))
        fourier_prob = 0j
        for j in range(h):
            qprod = 1 + 0j
            for value in copies:
                qprod *= (chi(j, value) ** -1 + 1 + chi(j, value)) / 3
            fourier_prob += chi(j, w - 1).conjugate() * qprod
        fourier_prob /= h
        assert abs(fourier_prob.real - direct_prob) < 1e-10
        assert abs(fourier_prob.imag) < 1e-10
        fourier_checks += 1
print(f"Fourier inversion checks: {fourier_checks}; character averages exact")

# Exact finite-group checks of the first/second moments in Lemma 12.5.
random_model_checks = 0
for h, K in ((6, 3), (8, 3), (10, 4)):
    tau = h // 2
    values = []
    for gs in cartesian_product(range(h), repeat=K):
        representations = 0
        for coeffs in cartesian_product((-1, 0, 1), repeat=K):
            if sum(c * g for c, g in zip(coeffs, gs)) % h == tau:
                representations += 1
        values.append(representations)
    mean = sum(values) / len(values)
    second = sum(value * value for value in values) / len(values)
    t = 2  # |(Z/hZ)[2]| for even h
    second_bound = (9 ** K / h ** 2 + 2 * (3 ** K - 1) / h
                    + t * 5 ** K / h ** 2)
    paley_bound = ((3 ** K - 1) ** 2
                    / (9 ** K + 2 * h * (3 ** K - 1) + t * 5 ** K))
    success_rate = sum(value > 0 for value in values) / len(values)
    assert abs(mean - (3 ** K - 1) / h) < 1e-12
    assert second <= second_bound + 1e-12
    assert success_rate + 1e-12 >= paley_bound
    random_model_checks += 1
print(f"random signed-product moment checks: {random_model_checks} groups")

# Empirical per-modulus failure rates for the full condition, separately for
# both criterion halves.  These support no theorem.
print("full-condition failure rates on the six hard classes:")
for w in phase_moduli:
    eligible = [p for p in six_primes if p > w]
    fail_b = fail_a = fail_joint = 0
    for p in eligible:
        b = (w - 1) not in signed_residues((p + w) // 4, w)
        a = (w - 1) not in signed_residues((p * w + 1) // 4, w)
        fail_b += b
        fail_a += a
        fail_joint += b and a
    total = len(eligible)
    print(f"  w={w:2}: B={fail_b/total:.3f}, A={fail_a/total:.3f}, "
          f"joint={fail_joint/total:.3f} ({total} primes)")

# ---------------------------------------------------------------- (h)
print("\n== (h) Phase-6 rate certificate and hard thresholds (§13) ==")
from math import acos, pi, sqrt

GAMMA, S0C, C1 = 0.125, 0.84, 0.015
D0 = 3000
MU_GRID = [j / 100 for j in range(0, 301)]
K1, K2 = 1 / 3, 1 / 20


BAND = 1e-9  # pessimistic safety band around the 1/20 boundary


def level_sigmas(d):
    """(sigma0, sigma1, sigma2) for a character of exact order d.

    Rigor: q_chi = 0 iff 3a in {d, 2d} (cos = -1/2), and |q| <= 1/3 iff
    cos(2*pi*a/d) <= 0 iff d <= 4a <= 3d -- both EXACT integer tests.
    Only the interior 1/20-level split uses binary64 cosines; borderline
    values (within BAND of the boundary) go to S1, the side with the
    smaller penalty, i.e. the pessimistic direction for the rate R(d).
    """
    s0 = s1 = s2 = 0
    for a in range(1, d):
        if 3 * a == d or 3 * a == 2 * d:
            s0 += 1                      # exact: q = 0
        elif d <= 4 * a <= 3 * d:        # exact: |q| <= 1/3
            c = cmath.cos(2 * pi * a / d).real
            # |q| <= 1/20 iff c in [-23/40, -17/40]
            if -23 / 40 + BAND <= c <= -17 / 40 - BAND:
                s2 += 1
            else:
                s1 += 1                  # includes borderline: pessimistic
    return s0 / d, s1 / d, s2 / d


def rate(sig, gamma=GAMMA, s0c=S0C):
    s0, s1, s2 = sig
    return max(s0c * (s0 + (1 - 3 ** -mu) * s1 + (1 - 20 ** -mu) * s2)
               - mu * gamma for mu in MU_GRID)


def sig_inf_leq(k):  # measure of {theta: |1+2cos theta| <= 3k}
    lo, hi = max(-1.0, -(1 + 3 * k) / 2), -(1 - 3 * k) / 2
    return (acos(lo) - acos(hi)) / pi


SIG2_INF = sig_inf_leq(K2)
SIG1_INF = sig_inf_leq(K1) - SIG2_INF
SIG_INF = (0.0, SIG1_INF, SIG2_INF)
R_INF = rate(SIG_INF)

worst = (9.0, None)
max_disc = 0.0
for d in range(2, D0 + 1):
    sig = level_sigmas(d)
    r = rate(sig)
    if r < worst[0]:
        worst = (r, d)
    disc = max(abs(sig[j] - SIG_INF[j]) * d for j in range(3))
    max_disc = max(max_disc, disc)
# (C1): every exact order d>=2 has rate >= c1 (worst small d checked directly,
# d > D0 via the arc-discrepancy bound R(d) >= R_inf - 24*s0/d).  Asserted
# margins dwarf binary64 arithmetic error (~1e-15) by >= 13 orders.
assert worst[0] >= 0.098 > C1, worst
assert R_INF - 24 * S0C / D0 >= C1 + 1e-6
# (C2): high-order ceiling with tail margin.
assert R_INF >= GAMMA + 2 * C1 + 24 * S0C / D0 + 1e-6, R_INF
# arc-discrepancy claim |sigma_j(d)-sigma_j_inf| <= 8/d, verified exhaustively
assert max_disc <= 8.0, max_disc
print(f"(C1) min_d R(d) = {worst[0]:.4f} at d={worst[1]} (>= c1={C1})")
print(f"(C2) R_inf = {R_INF:.4f} >= gamma+2c1+tail = "
      f"{GAMMA + 2*C1 + 24*S0C/D0:.4f}")
print(f"arc discrepancy: max_d d*|sigma_d - sigma_inf| = {max_disc:.2f} <= 8")

# Chernoff ceiling gamma* of the fully level-refined method (§13.3(1)).
THETA_N = 4096
QVALS = [abs(1 + 2 * cmath.cos(pi * (2 * j + 1) / THETA_N).real) / 3
         for j in range(THETA_N // 2)]


def chernoff_rate(gamma):
    best = 0.0
    for mu in MU_GRID:
        m = sum(v ** mu for v in QVALS) / len(QVALS)
        best = max(best, (1 - gamma) * (1 - m) - mu * gamma)
    return best


lo, hi = 0.05, 0.5
for _ in range(40):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if chernoff_rate(mid) > mid else (lo, mid)
gamma_star = (lo + hi) / 2
assert 0.19 < gamma_star < 0.22, gamma_star
print(f"Chernoff ceiling of the route: gamma* = {gamma_star:.3f}")

# Lemma 13.1 on real data: whenever full failure holds at (w, half), some
# nontrivial character satisfies the hard thresholds (i)+(ii).
checked = tight = 0
for w in (7, 11, 19, 23, 31):
    h = w - 1
    gen = primitive_root(w)
    dlog = {}
    cur = 1
    for j in range(h):
        dlog[cur] = j
        cur = cur * gen % w
    for p in six_primes[:150]:
        if p <= w:
            continue
        for n in ((p + w) // 4, (p * w + 1) // 4):
            if (w - 1) in signed_residues(n, w):
                continue  # no full failure here
            copies = [ell % w for ell, e in factorint(n).items()
                      for _ in range(e)]
            found = False
            for j in range(1, h):
                O0 = O1 = O2 = 0
                for g in copies:
                    v = abs(1 + 2 * cmath.cos(2 * pi * j * dlog[g] / h).real) / 3
                    if v < 1e-12:
                        O0 += 1
                    elif v <= K2:
                        O2 += 1
                    elif v <= K1 + 1e-12:
                        O1 += 1
                if O0 == 0 and 3 ** O1 * 20 ** O2 <= h - 1:
                    found = True
                    if 3 ** (O1 + 1) > h - 1:
                        tight += 1
                    break
            assert found, (p, w, n)
            checked += 1
print(f"Lemma 13.1 verified on {checked} full-failure pairs "
      f"({tight} with tight thresholds)")

# ---------------------------------------------------------------- (i)
print("\n== (i) Unconditioned moment lemmas (§13.4, Lemmas 13.3-13.6) ==")
XMAX = 30_000
phi_tab = list(range(XMAX + 1))
for ell in range(2, XMAX + 1):
    if phi_tab[ell] == ell:  # ell prime
        for k in range(ell, XMAX + 1, ell):
            phi_tab[k] -= phi_tab[k] // ell

# Lemma 13.3: |A_chi(X)| = |sum_{d<=X,(d,6)=1} chi(d)/phi(d)| << log(6w),
# uniformly in X.  Check at several checkpoints for several prime w.
worst_ratio = 0.0
for w in (7, 11, 43, 103):
    h = w - 1
    gen = primitive_root(w)
    dlog = {}
    cur = 1
    for jj in range(h):
        dlog[cur] = jj
        cur = cur * gen % w
    checkpoints = {300, 3000, XMAX}
    acc = [0.0] * w                     # acc[g] = sum over d = g (mod w)
    snaps = []
    for d in range(1, XMAX + 1):
        if d % 2 and d % 3 and d % w:
            acc[d % w] += 1.0 / phi_tab[d]
        if d in checkpoints:
            snaps.append(list(acc))
    for jj in range(1, h):              # nonprincipal characters
        for acc_x in snaps:
            a_chi = sum(acc_x[g] * cmath.exp(2j * cmath.pi * jj * dlog[g] / h)
                        for g in range(1, w) if g in dlog)
            worst_ratio = max(worst_ratio, abs(a_chi) / log(6 * w))
assert worst_ratio <= 2.0, worst_ratio
print(f"Lemma 13.3: max |A_chi(X)|/log(6w) over 4 moduli, all chi, 3 "
      f"checkpoints = {worst_ratio:.3f} (<= 2)")

# Lemma 13.4 shape (informational, toy scale): S1*h/(pi_{24,1}(N) log N)
# should be roughly stable in N for fixed w.
# (w = 7 only: for larger w and toy N, no d <= N^{1/4} is both = -1 mod w
# and coprime to 6, so T' is identically zero at this scale.)
w = 7
rows = []
for n_cap in (60_000, 240_000, 960_000):
    x_cap = int(round(n_cap ** 0.25))
    s1 = cnt = 0
    for p in primerange(w + 1, n_cap):
        if p % 24 != 1:
            continue
        cnt += 1
        n = (p + w) // 4
        s1 += sum(1 for d in range(1, x_cap + 1)
                  if n % d == 0 and d % 2 and d % 3 and d % w == w - 1)
    rows.append(s1 * (w - 1) / (cnt * log(n_cap)))
print(f"Lemma 13.4 ratio S1*h/(pi_(24,1)(N) log N), w=7: "
      + " -> ".join(f"{r:.3f}" for r in rows) + "  (toy scale, informational)")

# ---------------------------------------------------------------- (j)
print("\n== (j) Tilted subset-product moments (§13.4, Lemma 13.7) ==")
import random
from math import comb


def subset_target_count(gs, h, tau):
    """#subsets of gs (additive Z/h) summing to tau, via group-ring DP."""
    vec = [0] * h
    vec[0] = 1
    for g in gs:
        vec = [vec[a] + vec[(a - g) % h] for a in range(h)]
    return vec[tau]


# Exact conditional moments E[T|K=k] = (2^k-1)/h and the bound
# E[T^2|K=k] <= (4^k + 3h 2^k + h)/h^2, by full enumeration over multisets.
for h, tau, k in ((6, 5, 4), (6, 5, 8), (10, 3, 5)):
    et = et2 = 0.0
    total = h ** k
    from itertools import combinations_with_replacement
    for ms in combinations_with_replacement(range(h), k):
        cnt = Counter(ms)
        weight = 1
        rem = k
        for val, c in cnt.items():
            weight *= comb(rem, c)
            rem -= c
        t = subset_target_count(ms, h, tau)
        et += weight * t
        et2 += weight * t * t
    et /= total
    et2 /= total
    assert abs(et - (2 ** k - 1) / h) < 1e-9, (h, k, et)
    assert et2 <= (4 ** k + 3 * h * 2 ** k + h) / h ** 2 + 1e-9, (h, k, et2)
print("exact conditional moments: E[T|k]=(2^k-1)/h and the E[T^2|k] bound "
      "verified by enumeration (3 cases)")

# Poisson-mixed simulation: untilted PZ ratio collapses, theta=1/2 cures it.
random.seed(11)


def pz_ratios(L, w, trials=4000):
    units = [a for a in range(1, w) if gcd(a, w) == 1]
    stats = {1.0: [0.0, 0.0], 0.5: [0.0, 0.0]}
    for _ in range(trials):
        k, pacc, sacc, u = 0, exp(-L), exp(-L), random.random()
        while u > sacc:
            k += 1
            pacc *= L / k
            sacc += pacc
        vec = [0.0] * w
        vec[1 % w] = 1.0
        for _ in range(k):
            g = random.choice(units)
            nxt = vec[:]
            for a in range(w):
                if vec[a]:
                    nxt[a * g % w] += vec[a]
            vec = nxt
        t = vec[w - 1]
        for th in stats:
            uval = th ** k * t
            stats[th][0] += uval
            stats[th][1] += uval * uval
    return {th: (s[0] * s[0] / trials) / s[1] for th, s in stats.items()}


for w in (7, 31):
    r16, r32 = pz_ratios(16, w), pz_ratios(32, w)
    assert r16[0.5] > 0.9 and r32[0.5] > 0.99, (w, r16, r32)
    assert r32[1.0] < 0.01, (w, r32)
    print(f"w={w:2}: tilted PZ ratio {r16[0.5]:.3f}@L=16 -> {r32[0.5]:.4f}"
          f"@L=32; untilted collapses to {r32[1.0]:.4f}@L=32")

# ---------------------------------------------------------------- (k)
print("\n== (k) Window-tilted transfer H1''/H2'' (§13.5, Lemmas 13.9-13.11) ==")

# (k1) Exact local-factor factorization of the completed density sums
# (step (5) of Lemmas 13.9 and 13.10): enumerate all squarefree W-smooth
# d, m (resp. d1, d2, m) over a toy window and compare with the products
# prod_q F_q(chi) and prod_q F_q(chi1, chi2), for every character.
WSET = [5, 11, 13, 17]
WK = 7
HK = WK - 1
_g = primitive_root(WK)
_dlog = {}
_cur = 1
for _j in range(HK):
    _dlog[_cur] = _j
    _cur = _cur * _g % WK


def chi_k(j, x):
    return cmath.exp(2 * cmath.pi * 1j * j * _dlog[x % WK] / HK)


def subsets(xs):
    out = [()]
    for x in xs:
        out += [s + (x,) for s in out]
    return out


SUBS = subsets(WSET)
worst1 = worst2 = 0.0
for j1 in range(HK):
    direct = 0j
    for d in SUBS:
        for m in SUBS:
            un = set(d) | set(m)
            phi_u = prod(q - 1 for q in un) if un else 1
            direct += (chi_k(j1, prod(d) if d else 1)
                       * (-0.5) ** len(m) / phi_u)
    local = prod(1 + (chi_k(j1, q) - 1) / (2 * (q - 1)) for q in WSET)
    worst1 = max(worst1, abs(direct - local))
    if j1 == 0:
        assert abs(local - 1) < 1e-12  # principal factor telescopes to 1
for j1 in range(HK):
    for j2 in range(HK):
        direct = 0j
        for d1 in SUBS:
            for d2 in SUBS:
                for m in SUBS:
                    un = set(d1) | set(d2) | set(m)
                    phi_u = prod(q - 1 for q in un) if un else 1
                    direct += (chi_k(j1, prod(d1) if d1 else 1)
                               * chi_k(j2, prod(d2) if d2 else 1)
                               * (-0.75) ** len(m) / phi_u)
        local = prod(1 + ((1 + chi_k(j1, q)) * (1 + chi_k(j2, q)) / 4 - 1)
                     / (q - 1) for q in WSET)
        worst2 = max(worst2, abs(direct - local))
        if j1 == j2 == 0:
            assert abs(local - 1) < 1e-12
assert worst1 < 1e-12 and worst2 < 1e-12, (worst1, worst2)
print(f"(k1) local-factor factorization spot-check (toy window, mod 7): "
      f"defects {worst1:.2e} (H1''), {worst2:.2e} (H2''); principal == 1")

# (k2) Real shifted-prime data at toy scale: UNCAPPED tilted moments vs
# the model values of Lemma 13.7, the Paley-Zygmund inequality, and
# failure rates.  The d <= X cap of T'' is dropped (X = N^{1/8} < 6 here,
# so the capped statistic itself is untestable at toy scale; the cap is
# Rankin-inactive asymptotically).  Toy scale cannot make h*e^{-lam/2}
# small either: informational tracking with loose brackets, NOT a
# verification of Lemmas 13.9-13.10.
NK = 1_000_000
WIN = list(primerange(21, 5000))
LAM = sum(1.0 / q for q in WIN)
EL2 = exp(-LAM / 2)
EL34 = exp(-3 * LAM / 4)
print(f"(k2) N={NK}, window (20,5000], lam={LAM:.3f}, e^-lam/2={EL2:.3f}")
for w in (3, 7, 11):
    h = sum(1 for a in range(1, w) if gcd(a, w) == 1)
    s1 = s2 = pi0 = succ = 0.0
    samples = []
    for p in primerange(w + 1, NK):
        if p % 24 != 1:
            continue
        pi0 += 1
        n = (p + w) // 4
        divs = [q for q in WIN if n % q == 0]
        vec = [0] * w
        vec[1 % w] = 1
        for q in divs:
            nxt = vec[:]
            for a in range(w):
                if vec[a]:
                    nxt[a * q % w] += vec[a]
            vec = nxt
        t = vec[w - 1]  # subset products = -1 (mod w)
        u = t / 2 ** len(divs)
        s1 += u
        s2 += t * t / 4 ** len(divs)
        if t:
            succ += 1
            if len(samples) < 20:
                samples.append((p, n, divs))
    model1 = (1 - EL2) / h
    bound2 = (1 + 3 * h * EL2 + h * EL34) / h / h
    pz = s1 * s1 / (pi0 * s2)
    assert succ >= s1 * s1 / s2 - 1e-9          # Paley-Zygmund inequality
    assert 0.3 * model1 < s1 / pi0 < 3 * model1  # loose model bracket
    assert s2 / pi0 < 3 * bound2
    print(f"  w={w:2}: EU*h={s1 / pi0 * h:.3f} (model {model1 * h:.3f}), "
          f"EU2*h^2={s2 / pi0 * h * h:.3f} (model bound {bound2 * h * h:.3f}), "
          f"PZ={pz:.3f}, success={succ / pi0:.3f}")

    # (k3) criterion sufficiency: reconstruct exact solutions from window
    # witnesses via Theorem 3.1(B) with q = w.
    for p, n, divs in samples:
        wit = next(s for s in subsets(divs)
                   if s and prod(s) % w == w - 1 and n % prod(s) == 0)
        d = prod(wit)
        D = n // d
        assert (n * n) % D == 0 and (D + n) % w == 0
        y = p * (n + D) // w
        z_ = p * (n + n * n // D) // w
        assert p * (n + D) % w == 0 and p * (n + n * n // D) % w == 0
        assert Fraction(4, p) == (Fraction(1, n) + Fraction(1, y)
                                  + Fraction(1, z_))
print("(k3) exact Erdos-Straus solutions reconstructed from window "
      "witnesses (20 samples per modulus)")

# ---------------------------------------------------------------- (l)
print("\n== (l) Integer-side signed stack (§14, Lemmas 14.1-14.3, Thm 14.4) ==")

# (l1) Signed local-factor identities (Lemma 14.2 steps (2)-(3)): direct
# enumeration over a toy window vs the products prod_q F_q, every
# character (pair) mod 7.  Float spot-check, tolerance 1e-12.
worst1 = worst2 = 0.0
for j1 in range(HK):
    direct = 0j
    for a in SUBS:
        for b in SUBS:
            if set(a) & set(b):
                continue
            for mp in SUBS:
                un = set(a) | set(b) | set(mp)
                lcm_u = prod(un) if un else 1
                direct += (chi_k(j1, prod(a) if a else 1)
                           * chi_k(j1, prod(b) if b else 1).conjugate()
                           * (-2 / 3) ** len(mp) / lcm_u)
    local = prod(1 + (chi_k(j1, q) + chi_k(j1, q).conjugate() - 2)
                 / (3 * q) for q in WSET)
    worst1 = max(worst1, abs(direct - local))
    if j1 == 0:
        assert abs(local - 1) < 1e-12


def pat_iter():
    for a in SUBS:
        for b in SUBS:
            if not (set(a) & set(b)):
                yield a, b


PATS = list(pat_iter())
for j1 in range(HK):
    for j2 in range(HK):
        direct = 0j
        for a1, b1 in PATS:
            for a2, b2 in PATS:
                for mp in SUBS:
                    un = set(a1) | set(b1) | set(a2) | set(b2) | set(mp)
                    lcm_u = prod(un) if un else 1
                    direct += (chi_k(j1, prod(a1) if a1 else 1)
                               * chi_k(j1, prod(b1) if b1 else 1).conjugate()
                               * chi_k(j2, prod(a2) if a2 else 1)
                               * chi_k(j2, prod(b2) if b2 else 1).conjugate()
                               * (-8 / 9) ** len(mp) / lcm_u)
        local = 1
        for q in WSET:
            s = sum(chi_k(j1, q) ** e1 * chi_k(j2, q) ** e2
                    for e1 in (-1, 0, 1) for e2 in (-1, 0, 1))
            local *= 1 + (s / 9 - 1) / q
        worst2 = max(worst2, abs(direct - local))
        if j1 == j2 == 0:
            assert abs(local - 1) < 1e-12
assert worst1 < 1e-12 and worst2 < 1e-11, (worst1, worst2)
print(f"(l1) signed local-factor identities: defects {worst1:.2e} (mu1), "
      f"{worst2:.2e} (mu2); principal factors == 1")

# (l2) Toy integer-side stack.  (a) EXCLUSIVITY (Lemma 14.3): a shared
# window prime q cannot serve two shifts — the joint divisibility count
# is exactly zero while the independence model predicts N/q^2.  (b) The
# joint mean of prod_w (1-theta_w U_w)^2 vs the product of per-w means:
# equal up to second-order exclusion corrections (O(sum 1/q^2) over
# shared primes) and finite-sample noise; informational, loose assert.
# Signed U via group DP.
NK2 = 2_000_000
STACK = {3: list(primerange(26, 700)), 7: list(primerange(26, 3000))}


def u_signed(n, w, win):
    ps = [q for q in win if n % q == 0]
    vec = [0] * w
    vec[1 % w] = 1
    for q in ps:
        qi = pow(q, -1, w)
        nxt = vec[:]
        for r in range(w):
            if vec[r]:
                nxt[r * q % w] += vec[r]
                nxt[r * qi % w] += vec[r]
        vec = nxt
    return vec[w - 1] / 3 ** len(ps), vec[w - 1], ps


# (l1b) The CAPPED sieve variable U_w (truncated tilt, the actual
# definition in §14.1): (i) vanishes identically on witness-free n;
# (ii) equals 3^{-omega} * (witness count) whenever the caps are
# inactive.  Checked on real shifted integers.


def u_capped(n, w, win, cap):
    ps = [q for q in win if n % q == 0]
    tot = 0.0
    for ia in range(len(ps) + 1):
        for asub in combinations(ps, ia):
            rest = [q for q in ps if q not in asub]
            for ib in range(len(rest) + 1):
                for bsub in combinations(rest, ib):
                    ab = prod(asub) * prod(bsub)
                    if ab > cap:
                        continue
                    va = prod(asub) % w
                    vb = prod(bsub) % w
                    if va * pow(vb, -1, w) % w != w - 1:
                        continue
                    for mp_size in range(len(ps) + 1):
                        for mp in combinations(ps, mp_size):
                            if prod(mp) <= cap:
                                tot += (-2 / 3) ** len(mp)
    return tot


chk = eq = fails = 0
for m in range(1, 200_000, 24):
    w = 7
    n = (m + w) // 4
    u_unc, t, ps = u_signed(n, w, STACK[7])
    if len(ps) > 4:
        continue
    uc = u_capped(n, w, STACK[7], 10 ** 12)
    if t == 0:
        assert abs(uc) < 1e-12, (m, uc)
        fails += 1
    elif abs(uc - u_unc) < 1e-9:  # caps inactive at this scale
        eq += 1
    chk += 1
assert fails > 100 and eq > 100
print(f"(l1b) capped U: vanishes on all {fails} witness-free n; equals "
      f"3^-omega*T on {eq} witnessed n (caps inactive at toy scale)")



q_sh = 29  # shared window prime; check exclusivity vs independence
both = sum(1 for m in range(1, NK2, 24)
           if (m + 3) // 4 % q_sh == 0 and (m + 7) // 4 % q_sh == 0)
single3 = sum(1 for m in range(1, NK2, 24) if (m + 3) // 4 % q_sh == 0)
assert both == 0 and single3 > 0
print(f"(l2a) exclusivity at q={q_sh}: joint count 0 (model would give "
      f"~{single3 ** 2 * 24 // NK2}), single count {single3}")

sums = {w: [0.0, 0.0] for w in STACK}
vals = []
for m in range(1, NK2, 24):
    row = {}
    for w, win in STACK.items():
        u, t, _ = u_signed((m + w) // 4, w, win)
        row[w] = u
        sums[w][0] += u
        sums[w][1] += u * u
    vals.append(row)
cnt = len(vals)
theta = {w: s[0] / s[1] for w, s in sums.items()}
marg = {w: 1 - 2 * theta[w] * sums[w][0] / cnt
        + theta[w] ** 2 * sums[w][1] / cnt for w in STACK}
joint = sum(prod((1 - theta[w] * row[w]) ** 2 for w in STACK)
            for row in vals) / cnt
ratio = joint / prod(marg.values())
assert abs(ratio - 1) < 0.2, ratio
lam_free = sum(1 for row in vals if all(row[w] == 0 for w in STACK))
print(f"(l2) joint/product-of-marginals = {ratio:.4f} (exclusion corrections are second-order; "
      f"toy scale), delta_w = {[f'{marg[w]:.3f}' for w in STACK]}, "
      f"witness-free fraction {lam_free / cnt:.3f}")

# (l3) Signed-witness sufficiency: reconstruct exact solutions via
# d = n*a/b | n^2, Theorem 3.1(B) with q = w.
done = 0
for p in primerange(10 ** 5, 2 * 10 ** 5):
    if p % 24 != 1 or done >= 25:
        continue
    w = 7
    n = (p + w) // 4
    u, t, ps = u_signed(n, w, STACK[7])
    if not t:
        continue
    found = None
    for ks in cartesian_product((-1, 0, 1), repeat=len(ps)):
        v = 1
        for q, k in zip(ps, ks):
            v = v * pow(q, k % (w - 1) if k < 0 else k, w) % w  # q^k mod w
        if v % w == w - 1:
            found = ks
            break
    assert found is not None
    a = prod(q for q, k in zip(ps, found) if k == 1)
    b = prod(q for q, k in zip(ps, found) if k == -1)
    d = n * a // b
    assert n % b == 0 and (n * n) % d == 0 and (d + n) % w == 0
    y = p * (n + d) // w
    z_ = p * (n + n * n // d) // w
    assert Fraction(4, p) == Fraction(1, n) + Fraction(1, y) + Fraction(1, z_)
    done += 1
assert done == 25
print("(l3) exact solutions from signed witnesses d = n*a/b via Thm 3.1(B) "
      "(25 samples, w=7)")

# ---------------------------------------------------------------- (m)
print("\n== (m) Subset-only exact minima and signed reachability (§14.6) ==")

# SUBSET-ONLY CHECK.  For a prime-set pattern P, let f(P)=1 exactly when no
# subset product is -1 mod w.  Mobius inversion on the Boolean lattice gives
# the unique
# coefficients xi with sum_{V subset P} xi(V)=f(P).  The admissible support
# condition predicts xi(V)=0 for every nonempty witness-free V.  We verify
# this with integer arithmetic, and verify Q(xi)=P(failure) over the exact
# Bernoulli probabilities p_q=1/q (a common denominator prod q).
def _mul_reachable(bits, a, w):
    out = 0
    for x in range(1, w):
        if (bits >> x) & 1:
            out |= 1 << (x * a % w)
    return out


# A direct discriminator: modulo 7, factors 2 and 5 miss -1 by subsets but
# hit it using a negative exponent.  This guards the inverse transition below.
_subset_bits = _signed_bits = 1 << 1
for _a in (2, 5):
    _subset_bits |= _mul_reachable(_subset_bits, _a, 7)
    _signed_old = _signed_bits
    _signed_bits |= (_mul_reachable(_signed_old, _a, 7)
                     | _mul_reachable(_signed_old, pow(_a, -1, 7), 7))
assert not ((_subset_bits >> 6) & 1) and ((_signed_bits >> 6) & 1)


def subset_restricted_minimum_exact(w, r):
    qs = list(primerange(w + 1, 200))[:r]
    assert len(qs) == r
    size = 1 << r
    reachable = [0] * size
    reachable[0] = 1 << 1
    weights = [0] * size
    weights[0] = prod(q - 1 for q in qs)
    failure = [0] * size
    for mask in range(size):
        if mask:
            bit = mask & -mask
            i = bit.bit_length() - 1
            rest = mask ^ bit
            reachable[mask] = (reachable[rest]
                               | _mul_reachable(reachable[rest], qs[i] % w, w))
            weights[mask] = weights[rest] // (qs[i] - 1)
        failure[mask] = 1 - ((reachable[mask] >> (w - 1)) & 1)

    xi = failure[:]
    for i in range(r):
        bit = 1 << i
        for mask in range(size):
            if mask & bit:
                xi[mask] -= xi[mask ^ bit]
    assert xi[0] == 1
    assert all(mask == 0 or not failure[mask] or xi[mask] == 0
               for mask in range(size))

    lambda_values = xi[:]
    for i in range(r):
        bit = 1 << i
        for mask in range(size):
            if mask & bit:
                lambda_values[mask] += lambda_values[mask ^ bit]
    assert lambda_values == failure

    denominator = prod(qs)
    failure_numerator = sum(weights[mask] for mask in range(size)
                            if failure[mask])
    q_numerator = sum(weights[mask] * lambda_values[mask] ** 2
                      for mask in range(size))
    assert q_numerator == failure_numerator  # exact restricted minimum
    return (sum(1 / q for q in qs), failure_numerator / denominator,
            sum(x != 0 for x in xi) - 1)


for wm in (7, 11, 19, 23, 31):
    row = []
    for rm in (8, 12, 16):
        lamm, failm, suppm = subset_restricted_minimum_exact(wm, rm)
        row.append(f"r={rm}: lam/logh={lamm / log(wm - 1):.3f}, "
                   f"minQ={failm:.3f}, |supp|={suppm}")
    print(f"(m1-subset-only) w={wm}: " + "; ".join(row))

# Exact fixed-k iid-uniform reachability for three small cyclic unit groups,
# followed by Poisson(lambda) mixing.  The subset transition is S -> S union
# S*a.  The signed transition also includes S*a^{-1}, and therefore reaches
# all products with exponents in {-1,0,1}.  These centered finite-toy tables
# are informational, not evidence for an asymptotic transition; the proof is
# Lemma 14.6.
def iid_fixed_k_failures(w, kmax, *, signed):
    states = {1 << 1: 1.0}
    values = []
    units = [a for a in range(1, w) if gcd(a, w) == 1]
    for _ in range(kmax + 1):
        values.append(sum(p for bits, p in states.items()
                          if not ((bits >> (w - 1)) & 1)))
        nxt = {}
        for bits, p in states.items():
            for a in units:
                newbits = bits | _mul_reachable(bits, a, w)
                if signed:
                    newbits |= _mul_reachable(bits, pow(a, -1, w), w)
                nxt[newbits] = nxt.get(newbits, 0.0) + p / len(units)
        states = nxt
    return values


def poisson_mixture(lam, values):
    pk = exp(-lam)
    ans = pk * values[0]
    for k0 in range(1, len(values)):
        pk *= lam / k0
        ans += pk * values[k0]
    return ans


thresholds = (("subset", False, 1 / log(2)),
              ("signed", True, 1 / log(3)))
for wm in (7, 11, 19):
    for label, signed, threshold in thresholds:
        fixed = iid_fixed_k_failures(wm, 50, signed=signed)
        ratios = (threshold - 0.25, threshold, threshold + 0.25)
        vals = [poisson_mixture(ratio * log(wm - 1), fixed)
                for ratio in ratios]
        assert vals[0] > vals[1] > vals[2]
        assert 0.35 < vals[1] < 0.70  # entropy scale lies in the toy transition
        print(f"(m2-{label}) iid-Poisson w={wm}: P(miss) at lam/logh="
              + ",".join(f"{ratio:.3f}" for ratio in ratios) + " is "
              + ", ".join(f"{x:.3f}" for x in vals))

print("(m) subset-only Mobius support and Q=min=P(miss) checked exactly; "
      "signed S*a^{-1} reachability checked; centered toy transitions are "
      "informational")

# ---------------------------------------------------------------- (n)
print("\n== (n) auxiliary-prime declustering (§15) ==")


def pw_class_count(ell):
    """PW (4.1), m=4: floor(1/2 sum_{T|a} mu^2(T) tau(a/T))."""
    a = (ell + 1) // 4
    squarefree = [1]
    for prime in factorint(a):
        squarefree += [T * prime for T in squarefree]
    raw = sum(prod(e + 1 for e in factorint(a // T).values())
              for T in squarefree)
    assert raw == prod(2 * e + 1 for e in factorint(a).values())
    return raw // 2


def reconstructed_classes(ell):
    """Return (r,D,u,v,w) for D|a^2, D<a and uvw=a, D=u^2w."""
    a = (ell + 1) // 4
    rows = []
    for D in sorted(divisors_of_square(a)):
        if D >= a:
            continue
        g0 = gcd(D, a)
        u0, v0, w0 = D // g0, a // g0, g0 * g0 // D
        assert gcd(u0, v0) == 1 and u0 * v0 * w0 == a and u0 * u0 * w0 == D
        rows.append(((-4 * D) % ell, D, u0, v0, w0))
    return rows


ladder = (103, 199, 431, 863, 1699, 3467, 6899, 13799)
expected_f = (4, 7, 17, 24, 7, 7, 22, 67)
for ell, expected in zip(ladder, expected_f):
    rows = reconstructed_classes(ell)
    assert pw_class_count(ell) == expected == len(rows)
    assert len({row[0] for row in rows}) == expected
print("PW class counts on ell ladder:", dict(zip(ladder, expected_f)))


def check_reconstructed_classes(ell, expected_rows):
    """Check the closed form for five j, including even/composite n."""
    rows = reconstructed_classes(ell)
    assert [row[:2] for row in rows] == expected_rows
    identity_checks = 0
    for r, D, u0, v0, w0 in rows:
        for j in (0, 1, 2, 17, 101):
            n = r + ell * j
            s0 = v0 - u0 + j * v0
            assert ell * s0 == n * v0 + u0
            q0 = j + 1
            assert q0 == (s0 + u0) // v0 == 4 * s0 * u0 * w0 - n
            x0, d0 = s0 * u0 * w0, s0 * s0 * w0
            assert x0 * x0 % d0 == 0
            assert (d0 + x0) % q0 == 0
            assert (x0 + x0 * x0 // d0) % q0 == 0
            sol = (x0, n * s0 * v0 * w0, n * u0 * v0 * w0)
            assert sum((Fraction(1, value) for value in sol), Fraction()) == Fraction(4, n)
            identity_checks += 1
    return rows, identity_checks


rows103, checks103 = check_reconstructed_classes(
    103, [(99, 1), (95, 2), (87, 4), (51, 13)])
rows199, checks199 = check_reconstructed_classes(
    199, [(195, 1), (191, 2), (183, 4), (179, 5),
          (159, 10), (119, 20), (99, 25)])
print(f"independently reconstructed ell=103 classes {[row[0] for row in rows103]} "
      f"and ell=199 classes {[row[0] for row in rows199]}; "
      f"{checks103 + checks199} exact closed-form identity checks")

# Fast replay of Phase 0 at ell=103.  We only test n == 1 (mod 4), the
# hard slice; q=k*ell and m=k*ell are admissible there only for k == 1 (mod 4).
from random import Random


def fixed_multiple_witness(n, ell, k0, half):
    modulus = k0 * ell
    value = ((n + modulus) // 4 if half == "B" else (n * modulus + 1) // 4)
    return any((d0 + value) % modulus == 0
               and (value + value * value // d0) % modulus == 0
               for d0 in divisors_of_square(value))


# Composite-n regression: d=x^2 passes the first divisibility but does not
# reconstruct an integral second denominator.
assert (205 * 205 + 205) % 515 == 0
assert (205 + 205 * 205 // (205 * 205)) % 515 != 0
assert not fixed_multiple_witness(305, 103, 5, "B")

ell = 103
ks = (1, 5, 9, 13, 17)
rng = Random(20260819 + ell)
states = {r: {(half, k0): True for half in "BA" for k0 in ks}
          for r in range(1, ell)}
union = {r: True for r in range(1, ell)}
bases = {r: r + ell * (((1 - r) * pow(ell, -1, 4)) % 4) for r in states}
for _ in range(40):
    alive = [r for r in states if union[r] or any(states[r].values())]
    for r in alive:
        base = bases[r]
        lo = max(0, (1_000_000 - base + 4 * ell - 1) // (4 * ell))
        hi = (100_000_000 - base) // (4 * ell)
        n = base + 4 * ell * rng.randint(lo, hi)
        any_now = False
        for half in "BA":
            for k0 in ks:
                key = (half, k0)
                if states[r][key] or union[r]:
                    hit = fixed_multiple_witness(n, ell, k0, half)
                    states[r][key] &= hit
                    any_now |= hit
        union[r] &= any_now
assert [r for r in union if union[r]] == [ell - 4]
assert [(half, k0) for half in "BA" for k0 in ks
        if any(states[r][(half, k0)] for r in states)] == [("B", 1)]
print("fast fixed-multiple replay (ell=103): one reduced candidate r=-4; "
      "no extra class from k<=20")

# ---------------------------------------------------------------- (o)
print("\n== (o) generalized multiplier identity and class counts ==")


def multiplier_rows(ell, K, cutoff=None, floor=0, omega_cutoff=None):
    """(residue,u,v,k) rows, with the Lemma-16.2 floor/cutoff if given."""
    classes = {}
    bound = cutoff if cutoff is not None else int(ell ** (1 / 3))
    while (bound + 1) ** 3 <= ell:
        bound += 1
    while bound ** 3 > ell:
        bound -= 1
    for k0 in range(1, K + 1, 4):
        A0 = (k0 * ell + 1) // 4
        for u0 in divisors_of_square(A0):
            if not floor < u0 <= bound or A0 % u0:
                continue
            omega_u = len(factorint(u0))
            for v0 in divisors_of_square(A0 // u0):
                if (not floor < v0 <= bound or A0 % (u0 * v0)
                        or gcd(u0, v0) != 1):
                    continue
                if (omega_cutoff is not None
                        and omega_u + len(factorint(v0)) > omega_cutoff):
                    continue
                r0 = (-u0 * pow(v0, -1, ell)) % ell
                classes.setdefault(r0, []).append((u0, v0, k0))
    return classes


# Lemma 16.1: include odd primes, odd composites, even/composite n, and every
# ordered factorization in a modest exhaustive range.
multiplier_identity_checks = 0
saw_even_n = saw_composite_n = saw_composite_ell = False
for ell in list(primerange(3, 80)) + [9, 15, 21, 25, 27, 35]:
    if ell % 2 == 0:
        continue
    saw_composite_ell |= not __import__("sympy").isprime(ell)
    for k0 in range(1, 18):
        if k0 * ell % 4 != 3:
            continue
        A0 = (k0 * ell + 1) // 4
        for u0 in divisors_of_square(A0):
            if A0 % u0:
                continue
            for v0 in divisors_of_square(A0 // u0):
                if A0 % (u0 * v0):
                    continue
                w0 = A0 // (u0 * v0)
                modulus = k0 * ell
                r0 = (-u0 * pow(v0, -1, modulus)) % modulus
                for j in range(1, 5):
                    n = r0 + j * modulus
                    s0 = (n * v0 + u0) // modulus
                    assert s0 * modulus == n * v0 + u0 and s0 > 0
                    rhs = (Fraction(1, s0 * u0 * w0)
                           + Fraction(1, n * s0 * v0 * w0)
                           + Fraction(1, n * u0 * v0 * w0))
                    assert rhs == Fraction(4, n)
                    saw_even_n |= n % 2 == 0
                    saw_composite_n |= not __import__("sympy").isprime(n)
                    multiplier_identity_checks += 1
assert saw_even_n and saw_composite_n and saw_composite_ell
print(f"generalized identity: {multiplier_identity_checks} exact checks "
      "(including even/composite n and composite ell)")

# INFORMATIONAL small-scale version of the actual Lemma-16.2/16.3 object.
# H_TOY^2>K0 preserves cross-k distinctness; DISTINCT_PRIME_CUTOFF_TOY is a
# real, nonvacuous distinct-prime cutoff.  The tested classes are reduced c = 1
# (mod 4) modulo this toy M0=4*L_K, not all classes modulo the theorem's full
# 24*L_K modulus.  We also average over a dyadic-ish range of ell.
K0, H_TOY, DISTINCT_PRIME_CUTOFF_TOY = 13, 4, 3
# cutoff 3 (not 4) so the omega-truncation is NONVACUOUS at toy scale: some
# raw rows must actually be removed, and the omega-vs-Omega distinction is
# exercised (e.g. ell=10079, (u,v,k)=(9,8,1): omega(uv)=2 survives although
# Omega(uv)=5) — referee round 3 requirement.
ks0 = tuple(range(1, K0 + 1, 4))
M0 = 4
for k0 in ks0:
    M0 = lcm(M0, k0)
all_c = tuple(range(1, M0, 4))
reduced_c = tuple(c for c in all_c if gcd(c, M0) == 1)
ells_toy = tuple(ell for ell in primerange(10_000, 30_000) if ell % 4 == 3)
observed_by_k = {k0: 0.0 for k0 in ks0}
predicted_by_k = {k0: 0.0 for k0 in ks0}
observed_dedup = 0.0
for ell in ells_toy:
    by_residue = multiplier_rows(
        ell, K0, floor=H_TOY, omega_cutoff=DISTINCT_PRIME_CUTOFF_TOY)
    # The toy floor has exactly the inequality used in the proof.
    assert H_TOY * H_TOY > K0
    assert all(len(entries) == 1 for entries in by_residue.values())
    rows = [(r0, u0, v0, k0) for r0, entries in by_residue.items()
            for u0, v0, k0 in entries]
    per_k = {k0: 0 for k0 in ks0}
    dedup_total = 0
    for c in reduced_c:
        hits = []
        for r0, u0, v0, k0 in rows:
            if (c * v0 + u0) % k0 == 0:
                hits.append(r0)
                per_k[k0] += 1
        assert len(hits) == len(set(hits))
        dedup_total += len(hits)
    for k0 in ks0:
        observed_by_k[k0] += per_k[k0] / len(reduced_c)
        phi_k = k0
        for p0 in factorint(k0):
            phi_k = phi_k // p0 * (p0 - 1)
        z0 = int(ell ** (1 / 3))
        while (z0 + 1) ** 3 <= ell:
            z0 += 1
        while z0 ** 3 > ell:
            z0 -= 1
        predicted_by_k[k0] += phi_k / k0**2 * log(z0 / H_TOY) ** 2
    observed_dedup += dedup_total / len(reduced_c)

n_ells = len(ells_toy)
ratios_by_k = {
    k0: observed_by_k[k0] / predicted_by_k[k0] for k0 in ks0
}
total_predicted = sum(predicted_by_k.values()) / n_ells
total_ratio = (observed_dedup / n_ells) / total_predicted
assert n_ells == 1014 and observed_dedup > 0
# Deliberately broad scale guards catch catastrophic counting regressions.
assert all(0.02 <= ratio <= 50 for ratio in ratios_by_k.values())
assert 0.02 <= total_ratio <= 50
toy_comparison = {
    k0: (round(observed_by_k[k0] / n_ells, 3),
         round(predicted_by_k[k0] / n_ells, 3),
         round(ratios_by_k[k0], 3))
    for k0 in ks0
}
print("INFORMATIONAL actual-object toy average over 1014 primes ell and all "
      f"{len(reduced_c)} reduced c=1 (mod 4) "
      f"(H={H_TOY}, omega<={DISTINCT_PRIME_CUTOFF_TOY}); "
      "k: (classes, phi(k)/k^2 scale, ratio) =", toy_comparison,
      "; total =", (round(observed_dedup / n_ells, 3),
                     round(total_predicted, 3), round(total_ratio, 3)))

# Spot-check both parts of distinctness by design at a prime where k=1 and
# k=13 both contribute with u,v>K.  Reduced-ratio equality is checked too.
ell, K0 = 13259, 13
rows = []
for r0, entries in multiplier_rows(ell, K0).items():
    for u0, v0, k0 in entries:
        if u0 > K0 and v0 > K0:
            rows.append((r0, u0, v0, k0))
assert {k0 for _, _, _, k0 in rows} == {1, 13}
assert len(rows) == len({r0 for r0, _, _, _ in rows}) == 8
crt_checks = 0
for i, (r0, u0, v0, k0) in enumerate(rows):
    for r1, u1, v1, k1 in rows[i + 1:]:
        assert r0 != r1
        assert u0 * v1 != u1 * v0
        if k0 != k1:
            A0, A1 = (k0 * ell + 1) // 4, (k1 * ell + 1) // 4
            assert gcd(A0, A1) <= abs(k0 - k1) // 4 < K0
    # Choose a compatible subsequence c and solve its ell-class for n.  This
    # spot-checks that the k-part is absorbed and the residue becomes a class
    # modulo ell for the affine subsequence variable.
    c = next(c0 for c0 in all_c if (c0 * v0 + u0) % k0 == 0)
    n = c + M0 * (((r0 - c) * pow(M0, -1, ell)) % ell)
    if n == 0:
        n += M0 * ell
    assert n % M0 == c and n % ell == r0
    assert (n * v0 + u0) % (k0 * ell) == 0
    A0 = (k0 * ell + 1) // 4
    w0, s0 = A0 // (u0 * v0), (n * v0 + u0) // (k0 * ell)
    assert Fraction(4, n) == (Fraction(1, s0 * u0 * w0)
                              + Fraction(1, n * s0 * v0 * w0)
                              + Fraction(1, n * u0 * v0 * w0))
    crt_checks += 1
# referee round-3 nonvacuousness checks for the omega-cutoff
_raw = multiplier_rows(10079, K0, floor=H_TOY, omega_cutoff=None)
_cut = multiplier_rows(10079, K0, floor=H_TOY,
                       omega_cutoff=DISTINCT_PRIME_CUTOFF_TOY)
_nraw = sum(len(t) for t in _raw.values())
_ncut = sum(len(t) for t in _cut.values())
assert _ncut < _nraw, "omega cutoff must remove some raw rows"
assert any(u == 9 and v == 8 and k == 1 for tl in _cut.values()
           for (u, v, k) in tl), "omega(72)=2 row must survive"

print(f"distinctness/CRT spot-check: 8/8 classes distinct across k=1,13; "
      f"{crt_checks} subsequence reconstructions")


# ---------------------------------------------------------------- (p)
def check_p():
    """Companions for §17: four-parameter completeness, parity inertness,
    Mahler integral, entropy-wall toy."""
    import random as _rnd
    from math import gcd as _gcd, log as _log
    import cmath as _cmath
    from sympy import symbols, simplify, Rational, expand, jacobi_symbol, divisors, primerange
    print("\n== (p) pointwise-frontier companions (sec 17) ==")
    _rnd.seed(17)

    # (p1) symbolic identities (17.1)/(17.2)/(17.3)
    a, b, c, k, p = symbols('a b c k p', positive=True)
    pII = (4*a*b*c*k - a - b)/k
    r1 = simplify((1/(a*b*c) + 1/(pII*a*c*k) + 1/(pII*b*c*k)) - 4/pII)
    pI = k*(4*a*b*c - 1)/(a + b)
    r2 = simplify((1/(a*c*k) + 1/(b*c*k) + 1/(pI*a*b*c)) - 4/pI)
    r3 = expand((4*a*c*k - 1)*(4*b*c*k - 1) - (4*pII*c*k**2 + 1))
    assert r1 == 0 and r2 == 0 and r3 == 0, (r1, r2, r3)

    # (p1b) random Type-II tuples -> exact unit fractions; decomposition round-trip
    nII = 0
    for _ in range(300):
        a0 = _rnd.randint(1, 30); b0 = _rnd.randint(1, 30)
        if _gcd(a0, b0) != 1:
            continue
        c0 = _rnd.randint(1, 30); k0 = _rnd.randint(1, 6)
        num = 4*a0*b0*c0*k0 - a0 - b0
        if num % k0:
            continue
        p0 = num // k0
        s = Rational(1, a0*b0*c0) + Rational(1, p0*a0*c0*k0) + Rational(1, p0*b0*c0*k0)
        assert s == Rational(4, p0)
        nII += 1
    assert nII > 40, nII

    # (p1c) criterion-B witness -> (a,b,c,k) decomposition (Thm 17.1(i) direction =>)
    ndec = 0
    for p0 in (97, 1201, 409, 577, 61681):
        for q in range(3, 44, 4):
            if (p0 + q) % 4:
                continue
            x = (p0 + q)//4
            for d in divisors(x*x):
                if (d + x) % q:
                    continue
                g0 = _gcd(d, x); a0 = d//g0
                assert g0 % a0 == 0, (p0, q, d)
                c0 = g0//a0; b0 = x//(a0*c0)
                assert _gcd(a0, b0) == 1 and d == a0*a0*c0 and x == a0*b0*c0
                assert (a0 + b0) % q == 0
                k0 = (a0 + b0)//q
                assert k0*p0 == 4*a0*b0*c0*k0 - a0 - b0
                ndec += 1
    assert ndec >= 30, ndec

    # (p2) parity inertness (Lemma 17.2): lambda_p = +1 on both families
    npar = 0
    for p0 in primerange(2000, 4000):
        if p0 % 4 != 1:
            continue
        for c0 in (1, 2, 3):
            for k0 in (1, 2):
                assert jacobi_symbol(4*p0*c0*k0*k0 + 1, p0) == 1
                npar += 1
        for m0 in range(3, 24, 4):
            if (p0*m0 + 1) % 4 == 0:
                assert jacobi_symbol((p0*m0 + 1)//4, p0) == 1
                npar += 1
    assert npar > 300

    # (p3) Mahler integral of the Dirichlet kernel: numerically ~ 0 (informational)
    vals = []
    for E in (2, 5, 10):
        n = 200001
        tot = 0.0
        for j in range(n):
            th = (j + 0.5)/n
            z = _cmath.exp(2j*_cmath.pi*th)
            D = (z**(E + 1) - 1)/(z - 1)
            tot += _log(abs(D))
        vals.append(tot/n)
    assert all(abs(v) < 5e-3 for v in vals), vals

    # (p4) entropy-wall toy: single-generator assignment reaches exactly sum(2a_r)+1 values
    q0 = 101  # cyclic group (Z/101)^* of order 100
    g = 2     # primitive root mod 101
    caps = [2, 4, 6]          # 2a_r for three "primes" all assigned residue g
    reach = {1}
    for cap in caps:
        reach = {(v*pow(g, e, q0)) % q0 for v in reach for e in range(cap + 1)}
    assert len(reach) == sum(caps) + 1, len(reach)

    # (p5) the p=409 first witness needs k=2
    p0 = 409; a0, b0, c0, k0 = 1, 13, 8, 2
    assert k0*p0 + a0 + b0 == 4*a0*b0*c0*k0
    s = Rational(1, a0*b0*c0) + Rational(1, p0*a0*c0*k0) + Rational(1, p0*b0*c0*k0)
    assert s == Rational(4, 409)

    # (p6) fixed-(c,k) regression (Thm 17.1(iii) scope): p=29, (c,k)=(1,2):
    # D=15 | 465, D=-1 mod 8 gives NON-coprime (a,b)=(2,4); identity still exact;
    # canonical re-decomposition lands at different (c,k)=(4,1).
    p0, c0, k0 = 29, 1, 2
    n0 = 4*p0*c0*k0*k0 + 1
    assert n0 == 465 and n0 % 15 == 0 and 15 % (4*c0*k0) == 4*c0*k0 - 1
    a0 = (15 + 1)//(4*c0*k0); b0 = (n0//15 + 1)//(4*c0*k0)
    assert (a0, b0) == (2, 4) and _gcd(a0, b0) == 2
    assert k0*p0 + a0 + b0 == 4*a0*b0*c0*k0
    s = Rational(1, a0*b0*c0) + Rational(1, p0*a0*c0*k0) + Rational(1, p0*b0*c0*k0)
    assert s == Rational(4, 29)
    # canonical decomposition of the induced witness: x=abc=8, q=(a+b)/k=3, d=a^2c=4
    x0, q0, d0 = a0*b0*c0, (a0 + b0)//k0, a0*a0*c0
    g0 = _gcd(d0, x0); aa = d0//g0; cc = g0//aa; bb = x0//(aa*cc); kk = (aa + bb)//q0
    assert (aa, bb, cc, kk) == (1, 2, 4, 1) and kk*p0 == 4*aa*bb*cc*kk - aa - bb

    # (p7) Thm 17.3(c): residue 1 never lies in R(M) = {-4D mod M}: no D | A^2 with M | 4D+1
    for A0 in range(1, 2001):
        M0 = 4*A0 - 1
        for D0 in divisors(A0*A0):
            assert (4*D0 + 1) % M0 != 0, (A0, D0)

    # (p8) Thm 17.3(d): Case-A moving-c families end-to-end (Type-I reconstruction)
    nA = 0
    for aa, bb, mm in ((1, 2, 3), (2, 3, 5 if False else 5), (1, 6, 7), (3, 4, 7), (2, 5, 7), (1, 10, 11)):
        if _gcd(aa, bb) != 1 or (aa + bb) % mm or mm % 4 != 3:
            continue
        M4 = 4*aa*bb
        tgt = (-pow(mm, -1, M4)) % M4
        for p1 in primerange(3, 30000):
            if p1 % M4 == tgt:
                cc = (p1*mm + 1)//M4; kk = (aa + bb)//mm
                assert (p1*mm + 1) % M4 == 0
                z0 = aa*bb*cc; d1 = aa*aa*cc
                assert d1 * (z0*z0 // d1) == z0*z0 and (d1 + z0) % mm == 0
                s = Rational(1, aa*cc*kk) + Rational(1, bb*cc*kk) + Rational(1, p1*aa*bb*cc)
                assert s == Rational(4, p1)
                nA += 1
                break
    assert nA >= 4, nA

    # (p9) sec-17.7 descent audit: shape algebra + the 4/9 example
    from sympy import symbols as _sy, expand as _ex
    p_, x_, y_, z1_, x1_, y1_, x2_, z_ = _sy('p_ x_ y_ z1_ x1_ y1_ x2_ z_', positive=True)
    # (1,0,0): z=p*z1, p coprime to x,y,z1: clearing gives 4xyz1 = p*xy + p^2*z1*(x+y)
    e1 = _ex(4*x_*y_*p_*z1_ - p_**2*(x_*y_ + x_*p_*z1_ + y_*p_*z1_))
    assert _ex(e1/p_) == _ex(4*x_*y_*z1_ - p_*x_*y_ - p_**2*z1_*(x_ + y_))
    # (1,1,0): x=p*x1, y=p*y1: e2/p^2 = 4x1y1z - p^2x1y1 - p*z*(x1+y1)
    e2 = _ex(4*p_*x1_*p_*y1_*z_ - p_**2*(p_*x1_*p_*y1_ + p_*y1_*z_ + p_*x1_*z_))
    assert _ex(e2/p_**2) == _ex(4*x1_*y1_*z_ - p_**2*x1_*y1_ - p_*z_*(x1_ + y1_))
    # (2,1,0): x=p^2 x2, y=p y1: e3/p^3 = 4x2y1z - p^2x2y1 - y1z - p*x2*z  (mod p: y1z(4x2-1))
    e3 = _ex(4*p_**2*x2_*p_*y1_*z_ - p_**2*(p_**2*x2_*p_*y1_ + p_*y1_*z_ + p_**2*x2_*z_))
    assert _ex(e3/p_**3) == _ex(4*x2_*y1_*z_ - p_**2*x2_*y1_ - y1_*z_ - p_*x2_*z_)
    # (2,0,0): x=p^2 x2, p coprime y,z: reduces to YZ(4X-1) = p^2 X(Y+Z) => p^2 | 4X-1
    e4 = _ex(4*p_**2*x2_*y_*z_ - p_**2*(p_**2*x2_*y_ + y_*z_ + p_**2*x2_*z_))
    assert _ex(e4/p_**2) == _ex(4*x2_*y_*z_ - p_**2*x2_*y_ - y_*z_ - p_**2*x2_*z_)
    assert _ex((4*x2_*y_*z_ - y_*z_) - y_*z_*(4*x2_ - 1)) == 0
    # (a,a,0) consistency for a=2,3: valuation bookkeeping v_p(X+Y) = a-2 (numeric spot):
    # a=2, p=5: X=2, Y=3 (X+Y=5, v=1? need v=a-2=0 -> pick X+Y coprime to 5: X=2,Y=4? gcd... just check equation shape)
    for a_, p0_, X_, Y_ in ((2, 5, 1, 3), (3, 5, 1, 4)):
        # numeric valuation spot-checks of the (a,a,0) constraint v_p(X+Y) = a-2
        from sympy import multiplicity as _mult
        assert _mult(p0_, X_ + Y_) == a_ - 2
    # the (2,1,0) witness at p=3 and the reviewer's 4/3 accident:
    # 4/9 = 1/9 + 1/12 + 1/4, v3-shape (2,1,0), 3 | 4*1-1; and 4/3 = 1/1 + 1/12 + 1/4
    assert Rational(1, 9) + Rational(1, 12) + Rational(1, 4) == Rational(4, 9)
    assert (4*1 - 1) % 3 == 0
    assert Rational(1, 1) + Rational(1, 12) + Rational(1, 4) == Rational(4, 3)

    print(f"sec-17 companions: identities symbolic OK; {nII} random Type-II tuples exact; "
          f"{ndec} witness decompositions; {npar} parity checks all +1; "
          f"Mahler means {[round(v, 5) for v in vals]}; entropy toy exact; 409 + p=29 "
          f"regressions OK; R(M) residue-1 escape verified M<=8000 (A<=2000); {nA} Case-A moving-c "
          f"families exact; 17.7 shape algebra + 4/9 example OK")


check_p()


# ---------------------------------------------------------------- (q)
def check_q():
    """Numerical companions for §18 (informational asymptotics, exact sets)."""
    print("\n== (q) full-harvest cubic supply and assembly budgets ==")

    # Independent (non-circular) check of Lemma 18.1: enumerate ALL ordered
    # factorizations uvw = A and the residues -u*v^{-1} mod M; compare with
    # {-4D mod M : D | A^2}.  Includes M = 231 = 77*3 = 33*7 = 21*11: the
    # class set is intrinsic to M, identical however M is split as k*ell.
    from sympy import divisors as _divs
    from math import gcd as _g
    for M0 in list(range(3, 400, 4)) + [231, 4*250 - 1, 4*333 - 1]:
        A0 = (M0 + 1) // 4
        lhs = set()
        for u0 in _divs(A0):
            for v0 in _divs(A0 // u0):
                # w = A0//(u0*v0) automatically a positive integer
                lhs.add((-u0 * pow(v0, -1, M0)) % M0)
        rhs = {(-4 * D0) % M0 for D0 in _divs(A0 * A0)}
        assert lhs == rhs, M0
    print("Lemma 18.1 independent enumeration: {-u v^-1} = {-4D} verified, "
          "M = 3..399 and 231/999/1331 (intrinsic across k*ell splits)")

    q_max = 100_000
    a_max = (q_max + 1) // 4

    # A small SPF table avoids making 25,000 separate factorint calls.  For
    # M=4A-1, the complete Lemma-16.1 class set is {-4D mod M:D|A^2}.
    spf = list(range(a_max + 1))
    for p0 in range(2, int(a_max**0.5) + 1):
        if spf[p0] == p0:
            for n0 in range(p0 * p0, a_max + 1, p0):
                if spf[n0] == n0:
                    spf[n0] = p0

    def square_divisors_spf(n0):
        factors = []
        while n0 > 1:
            p0, e0 = spf[n0], 0
            while n0 % p0 == 0:
                n0 //= p0
                e0 += 1
            factors.append((p0, e0))
        ds = [1]
        for p0, e0 in factors:
            ds = [d0 * p0**j for d0 in ds for j in range(2 * e0 + 1)]
        return ds

    cutoffs = (2_000, 5_000, 10_000, 25_000, 50_000, 100_000)
    supply = canonical = 0.0
    samples = []
    next_cut = 0
    for A0 in range(1, a_max + 1):
        M = 4 * A0 - 1
        ds = square_divisors_spf(A0)
        classes = {(-4 * d0) % M for d0 in ds}
        canonical_classes = {(-4 * d0) % M for d0 in ds if d0 < A0}
        assert len(canonical_classes) == (len(ds) - 1) // 2
        assert canonical_classes <= classes
        assert (len(ds) - 1) // 2 <= len(classes) <= len(ds)
        supply += len(classes) / M
        canonical += len(canonical_classes) / M
        while next_cut < len(cutoffs) and M + 4 > cutoffs[next_cut]:
            Q0 = cutoffs[next_cut]
            samples.append((Q0, supply, canonical))
            next_cut += 1

    # The finite range still has large lower-order terms; only broad guards are
    # appropriate.  The fitted exponent is evidence, not part of the proof.
    ratios = [s0 / log(Q0)**3 for Q0, s0, _ in samples]
    xs = [log(log(Q0)) for Q0, _, _ in samples]
    ys = [log(s0) for _, s0, _ in samples]
    xbar, ybar = sum(xs) / len(xs), sum(ys) / len(ys)
    fitted_B = (sum((x0 - xbar) * (y0 - ybar) for x0, y0 in zip(xs, ys))
                / sum((x0 - xbar)**2 for x0 in xs))
    assert all(0.005 < r0 < 0.2 for r0 in ratios)
    assert 2.0 < fitted_B < 3.5
    print("exact union mass S(Q)/log^3 Q:",
          {Q0: round(s0 / log(Q0)**3, 5) for Q0, s0, _ in samples},
          f"; informational fitted B={fitted_B:.3f}")

    # Cross-decomposition warning: the literal (k,ell)-double sum is not the
    # union over moduli.  M=231 has three admissible prime choices for ell,
    # but all three decompositions produce exactly the same identity classes.
    M = 3 * 7 * 11
    A0 = (M + 1) // 4
    full = {(-4 * d0) % M for d0 in square_divisors_spf(A0)}
    decompositions = [(M // ell0, ell0) for ell0 in (3, 7, 11)]
    assert all(k0 % 4 == 1 and k0 * ell0 == M
               for k0, ell0 in decompositions)
    class_sets = []
    for k0, ell0 in decompositions:
        Ak = (k0 * ell0 + 1) // 4
        class_sets.append({(-4 * d0) % (k0 * ell0)
                           for d0 in square_divisors_spf(Ak)})
    assert all(s0 == full for s0 in class_sets)
    print(f"cross-k dedup at M={M}: {len(decompositions)} decompositions, "
          f"{len(full)} union classes (not {len(decompositions)*len(full)})")

    # Explicit arithmetic for Assessment 18.4.  With polylogarithmic K,
    # r=log K=O(log L), mu=t^2 r and J~mu give t^3 r~L.  With r~t,
    # J(t+r)~t^4 and mu~t^3.  Constants are immaterial to the exponents.
    budget_rows = []
    for L0 in (10**6, 10**9, 10**12):
        r0 = 0.5 * log(L0)                 # K=L^(1/2)
        t0 = (L0 / r0)**(1 / 3)
        mu0 = t0 * t0 * r0
        norm = L0**(2 / 3) * log(L0)**(1 / 3)
        t3 = (L0 / 2)**0.25                # r=t, J(t+r)=2t^4=L
        mu3 = t3**3
        assert abs(t0**3 * r0 / L0 - 1) < 1e-12
        assert abs(2 * t3**4 / L0 - 1) < 1e-12
        budget_rows.append((L0, mu0 / norm, mu3 / L0**0.75))
    print("toy level balances (L, polylog-normalized, cubic-normalized):",
          [(L0, round(a0, 3), round(b0, 3))
           for L0, a0, b0 in budget_rows])


check_q()


# ---------------------------------------------------------------- (r)
def check_r():
    """Replay the finite checks supporting the section-19 frontier data."""
    import json
    from pathlib import Path
    from random import Random
    from sympy import expand

    data = json.loads(Path(__file__).with_name("recorddata.json").read_text())

    # The k=1/F1 dictionary, including exact criterion-B reconstruction.
    rng = Random(0x19)
    for _ in range(100):
        g0, u0, v0 = (rng.randint(1, 10_000), rng.randint(1, 1_000),
                      rng.randint(1, 1_000))
        p0 = 4 * g0 * u0 * v0 - u0 - v0
        q0, x0, d0 = u0 + v0, g0 * u0 * v0, u0 * u0 * g0
        assert p0 + q0 == 4 * x0
        assert x0 * x0 % d0 == 0 and (d0 + x0) % q0 == 0
        assert caseB_solution(p0, q0, d0, x0) == (
            g0 * u0 * v0, p0 * g0 * u0, p0 * g0 * v0)

    # Twenty stored witnesses replay the valuation decomposition
    # d=a^2*c, x=a*c*b and its four-parameter identity.
    stored = data["type_II_dictionary"]["replay_witnesses"]
    assert len(stored) == 20
    for p0, q0, d0, x0, a0, b0, c0, k0 in stored:
        g0 = gcd(d0, x0)
        assert a0 == d0 // g0 and g0 % a0 == 0
        assert c0 == g0 // a0 and b0 == x0 // (a0 * c0)
        assert gcd(a0, b0) == 1 and (a0 + b0) == q0 * k0
        assert d0 == a0 * a0 * c0 and x0 == a0 * b0 * c0
        assert k0 * p0 == 4 * a0 * b0 * c0 * k0 - a0 - b0

    a, b, c, k, p = symbols("a b c k p")
    polynomial = ((4 * a * c * k - 1) * (4 * b * c * k - 1)
                  - (4 * p * c * k**2 + 1))
    relation = k * p - (4 * a * b * c * k - a - b)
    assert expand(polynomial.subs(p, (4 * a * b * c * k - a - b) / k)) == 0
    assert expand(polynomial + 4 * c * k * relation) == 0

    def direct_hit(n0, w0):
        return any((d + n0) % w0 == 0 for d in divisors_of_square(n0))

    def direct_interleaved(p0):
        for w0 in range(3, 1000, 4):
            if (direct_hit((p0 + w0) // 4, w0)
                    or direct_hit((p0 * w0 + 1) // 4, w0)):
                return w0
        raise AssertionError("record replay guard exhausted")

    def direct_case_b(p0):
        q0 = (-p0) % 4
        if q0 == 0:
            q0 = 4
        for w0 in range(q0, 1000, 4):
            if direct_hit((p0 + w0) // 4, w0):
                return w0
        raise AssertionError("Case-B record replay guard exhausted")

    # Five original interleaved records plus the five newest Case-B records
    # make the ten entries from §19.1.
    inter = data["interleaved_records"]
    assert len(inter) == 5
    for row in inter:
        assert direct_interleaved(row["p"]) == row["w_star"]
    case_b = data["case_b_records"][-5:]
    for row in case_b:
        assert direct_case_b(row["p"]) == row["q_min"]

    # Section 19.4 addendum: independently recompute every extension record.
    extension = data["extension"]
    assert extension["max_p"] == 9_999_999_817
    assert extension["max_w_star"] == 71
    assert extension["records"][-1] == {"p": 2_927_257_369, "w_star": 71}
    for row in extension["new_records"]:
        assert factorint(row["p"]) == {row["p"]: 1}
        assert direct_interleaved(row["p"]) == row["w_star"]

    # Replay three stored F3 deficits.  Reduction modulo each generator's
    # order makes 0 <= e < ord exact: adding an order can only increase the
    # cap-excess cost.  This is a separate min-plus implementation from the
    # production script.
    replays = extension["f3_microscopy"]["deficit_replays"]
    assert len(replays) == 3
    for row in replays:
        p0, w0, half0 = row["p"], row["w"], row["half"]
        n0 = ((p0 + w0) // 4 if half0 == "B" else
              (p0 * w0 + 1) // 4)
        fac0 = factorint(n0)
        assert {str(q0): e0 for q0, e0 in sorted(fac0.items())} == row["factorization"]
        target0 = (-n0) % w0
        assert n0 == row["n"] and target0 == row["target"]

        capped = {1}
        for q0, e0 in fac0.items():
            powers0 = {pow(q0, j0, w0) for j0 in range(2 * e0 + 1)}
            capped = {a0 * b0 % w0 for a0 in capped for b0 in powers0}
        assert target0 not in capped

        costs = {1: 0}
        for q0, e0 in fac0.items():
            options0 = []
            power0, exponent0 = 1, 0
            while True:
                options0.append((power0, max(0, exponent0 - 2 * e0)))
                power0 = power0 * q0 % w0
                exponent0 += 1
                if power0 == 1:
                    break
                assert exponent0 <= w0
            next_costs = {}
            for a0, cost0 in costs.items():
                for power0, extra0 in options0:
                    residue0 = a0 * power0 % w0
                    next_costs[residue0] = min(
                        next_costs.get(residue0, 10**9), cost0 + extra0)
            costs = next_costs
        assert costs[target0] == row["deficit"] >= 1
        exponents0 = {int(q0): e0 for q0, e0 in
                      row["canonical_exponents"].items()}
        residue0 = prod(pow(q0, exponents0[q0], w0) for q0 in fac0) % w0
        deficit0 = sum(max(0, exponents0[q0] - 2 * e0)
                       for q0, e0 in fac0.items())
        assert residue0 == target0 and deficit0 == row["deficit"]

    print("section-19 replay: original tables, extension record w*=71, and "
          "three exact F3 deficits")


print("\n== (r) computational-frontier replay ==")
check_r()


# ---------------------------------------------------------------- (s)
def check_s():
    """Section 20: composition, affine transfers, and finite orbit replay."""
    from sympy import symbols, expand, simplify

    p, u, v, a, b, c, k, t = symbols(
        "p u v a b c k t", nonzero=True)
    h = 4 * c * k
    L = h * k
    Np = 1 + L * p

    # Lemma 20.1 and the explicit inherited-factor transfer (20.2)-(20.3).
    assert expand(1 + L * (u + v + L * u * v)
                  - (1 + L * u) * (1 + L * v)) == 0
    p_ab = 4 * a * b * c - (a + b) / k
    b_new = b + k * t * (h * b - 1)
    p_new = 4 * a * b_new * c - (a + b_new) / k
    assert simplify(p_new - (p_ab + t * (1 + L * p_ab))) == 0
    assert expand((h * a - 1) * (h * b - 1)
                  - (1 + L * p_ab)) == 0

    # All three coordinate translations and their simultaneous reduction.
    assert simplify((4 * a * b * (c + t) - (a + b) / k)
                    - (p_ab + 4 * a * b * t)) == 0
    assert simplify((4 * (a + k * t) * b * c
                     - (a + k * t + b) / k)
                    - (p_ab + t * (4 * b * c * k - 1))) == 0
    assert simplify((4 * a * (b + k * t) * c
                     - (a + b + k * t) / k)
                    - (p_ab + t * (4 * a * c * k - 1))) == 0
    a0, b0 = symbols("a0 b0", positive=True)
    p0 = 4 * a0 * b0 * c - (a0 + b0) / k
    D0, E0 = h * a0 - 1, h * b0 - 1
    reduced = 4 * (a0 + k * u) * (b0 + k * v) * c \
        - (a0 + k * u + b0 + k * v) / k
    assert simplify(reduced - (p0 + u * E0 + v * D0 + L * u * v)) == 0
    assert expand((D0 + L * u) * (E0 + L * v)
                  - (1 + L * reduced)) == 0

    # Ternary fixed-slice composition and binary cross-modulus forgetting.
    p1, p2, p3, w1, w2 = symbols("p1 p2 p3 w1 w2")
    ternary_p = ((1 + L * p1) * (1 + L * p2) * (1 + L * p3) - 1) / L
    assert expand(1 + L * ternary_p
                  - (1 + L * p1) * (1 + L * p2) * (1 + L * p3)) == 0
    cross_p = w1 * p1 + w2 * p2 + 4 * w1 * w2 * p1 * p2
    assert expand((1 + 4 * w1 * p1) * (1 + 4 * w2 * p2)
                  - (1 + 4 * cross_p)) == 0

    # Minimal corrected binary law (20.4a-c).  The divisibility by k follows
    # symbolically after imposing k | a_i+b_i; the polynomial identities are
    # checked here without that substitution.
    a1, a2, b1, b2 = symbols("a1 a2 b1 b2", positive=True)
    A = h * a1 * a2 - a1 - a2
    B = h * b1 * b2 - b1 - b2
    corrected_p = 4 * A * B * c - (A + B) / k
    assert expand(h * A - 1 - ((h * a1 - 1) * (h * a2 - 1) - 2)) == 0
    assert expand(h * B - 1 - ((h * b1 - 1) * (h * b2 - 1) - 2)) == 0
    assert expand((h * A - 1) * (h * B - 1)
                  - (1 + L * corrected_p)) == 0
    H, K, T = symbols("H K T", nonzero=True)
    C_rescaled, P_rescaled = H / (4 * K), T / K
    assert expand(1 + 4 * P_rescaled * C_rescaled * K**2
                  - (1 + H * T)) == 0

    # Euclidean reduction (20.11), diagonal identity (20.15), and the
    # signed/four-term near representations (20.16)-(20.17).
    R = 4 * a * c * k - 1
    assert expand(4 * a * c * (k * p + a)
                  - (p * R + p + 4 * a**2 * c)) == 0
    assert expand(a * Np - (p * k * R + a + p * k)) == 0
    n = symbols("n", positive=True)
    pp = 4 * n + 1
    assert simplify(1 / (n + 1) + 3 / (pp * (n + 1)) - 4 / pp) == 0
    assert simplify(1 / (n + 1) + 1 / (n * (n + 1))
                    - 1 / (n * pp) - 4 / pp) == 0

    def all_divisors(n0):
        ds = [1]
        for q0, e0 in factorint(n0).items():
            ds = [d0 * q0**j0 for d0 in ds for j0 in range(e0 + 1)]
        return sorted(ds)

    def fixed_status(p0, c0, k0):
        h0, L0 = 4 * c0 * k0, 4 * c0 * k0 * k0
        n0 = 1 + L0 * p0
        ds = all_divisors(n0)
        witness = any(d0 % h0 == h0 - 1 for d0 in ds)
        atom = not any(1 < d0 < n0 and d0 % L0 == 1 for d0 in ds)
        return witness, atom

    # Lemma 20.2's nonclosure example and the explicit witnessed atom.
    delta25 = {d0 % 12 for d0 in all_divisors(25)}
    delta49 = {d0 % 12 for d0 in all_divisors(49)}
    delta_product = {d0 % 12 for d0 in all_divisors(25 * 49)}
    assert 11 not in delta25 and 11 not in delta49 and 11 in delta_product
    assert factorint(4 * 313 + 1) == {7: 1, 179: 1}
    assert fixed_status(313, 1, 1) == (True, True)
    # Correcting the p=5 witness with itself gives (A,B,P)=(2,12,82),
    # and the affine shift B -> B+33 reaches the atom p=313.
    assert 4 * 2 * 12 - 2 - 12 == 82
    assert 4 * 2 * (12 + 33) - 2 - (12 + 33) == 313
    assert (4 * 2 - 1) * (4 * (12 + 33) - 1) == 4 * 313 + 1
    assert fixed_status(5, 1, 1)[0] and fixed_status(3, 1, 2)[0]
    assert (1 + 4 * 5) * (1 + 16 * 3) == 1 + 4 * 257
    assert fixed_status(257, 1, 1)[0]
    # Corrected cross-slice composition: p=3 at (1,2) and p=59 at
    # (1,1) give the hard prime 2617 at (1,1).
    assert (7 * 3 - 2) * (7 * 79 - 2) == 19 * 551 == 1 + 4 * 2617
    assert factorint(2617) == {2617: 1} and 2617 % 24 == 1
    assert fixed_status(2617, 1, 1)[0]
    # Common-modulus rescaling of p=3 at (1,2) and p=41 at (1,4).
    assert (7 * 15 - 2) * (7 * 175 - 2) == 103 * 1223 \
        == 1 + 16 * 7873
    assert factorint(7873) == {7873: 1} and 7873 % 24 == 1
    assert fixed_status(7873, 1, 2)[0]

    # Exact finite atom table in §20.1.
    hard = [p0 for p0 in primerange(2, 5000) if p0 % 24 == 1]
    assert len(hard) == 76
    expected = {
        (1, 1): Counter({(False, False): 16, (False, True): 24,
                         (True, False): 14, (True, True): 22}),
        (1, 2): Counter({(False, False): 4, (False, True): 46,
                         (True, False): 2, (True, True): 24}),
    }
    for ck0, wanted in expected.items():
        assert Counter(fixed_status(p0, *ck0) for p0 in hard) == wanted

    # Exhaust every smaller-prime absorption seed for c,k <= 3.  The cap
    # s<1000 is complete for targets P<5000 because P>(L+1)s>=5s.
    seeds = []
    for c0 in range(1, 4):
        for k0 in range(1, 4):
            L0 = 4 * c0 * k0 * k0
            for s0 in primerange(2, 1000):
                if fixed_status(s0, c0, k0)[0]:
                    seeds.append((s0, c0, k0, 1 + L0 * s0))
    reached = []
    for P0 in hard:
        if any(s0 < P0 and (P0 - s0) % Ns0 == 0
               for s0, _c0, _k0, Ns0 in seeds):
            reached.append(P0)
    assert reached == [433, 457, 1753, 2113, 2953, 3001, 3433, 3793,
                       4057, 4177, 4561, 4993]
    assert not ({409, 577, 1201, 2521} & set(reached))

    # reviewer-round supplements: general non-coprime divisor-set equality,
    # corrected-law parity, and the (20.14) synchronization equivalence
    from sympy import divisors as _dv
    from random import Random as _R
    from math import gcd as igcd
    _r = _R(20)
    for _ in range(200):
        n1 = _r.randint(2, 400); n2 = _r.randint(2, 400); h0 = _r.choice([4, 8, 12, 20])
        if igcd(n1 * n2, h0) != 1:
            continue
        s12 = {d % h0 for d in _dv(n1 * n2)}
        s1x2 = {(d1 * d2) % h0 for d1 in _dv(n1) for d2 in _dv(n2)}
        assert s12 == s1x2, (n1, n2, h0)
    # corrected same-slice law parity: odd inputs -> even canonical P (Lemma 20.2.1)
    for (a1, b1), (a2, b2), c0, k0 in (((1, 1), (1, 1), 1, 1), ((1, 13), (1, 1), 2, 2)):
        h0 = 4 * c0 * k0
        p1 = (4 * a1 * b1 * c0 * k0 - a1 - b1) // k0
        p2 = (4 * a2 * b2 * c0 * k0 - a2 - b2) // k0
        if p1 % 2 and p2 % 2:
            A0 = h0 * a1 * a2 - a1 - a2
            B0 = h0 * b1 * b2 - b1 - b2
            assert (A0 + B0) % k0 == 0
            P0 = 4 * A0 * B0 * c0 - (A0 + B0) // k0
            assert P0 % 2 == 0, (a1, b1, a2, b2, c0, k0, P0)
    # (20.14): r = 4kt-1: r = -1 mod 4ck  <=>  c | t
    for k0 in (1, 2, 3):
        for t0 in range(1, 30):
            r0 = 4 * k0 * t0 - 1
            for c0 in range(1, 12):
                assert ((r0 + 1) % (4 * c0 * k0) == 0) == (t0 % c0 == 0)

    print("sec-20 composition/correction algebra exact; fixed-slice atoms "
          "and 12/76 small transfer reachability replayed; non-coprime "
          "divisor-set equality, corrected-law parity, and (20.14) sync checked")


print("\n== (s) frontal-assault transfer algebra (§20) ==")
check_s()

# ---------------------------------------------------------------- (t)
def check_t():
    """Section 21: exact intrinsic avoidance and the quadratic escape."""
    import numpy as np

    def rzero(d0):
        ans = 1
        for p0, e0 in factorint(d0).items():
            ans *= p0**((e0 + 1) // 2)
        return ans

    # Lemma 21.1: D|A^2 iff R_0(D)|A, including the converse reorganization
    # through M|n+4D.  The bounded loops are exhaustive, not random.
    for A0 in range(1, 101):
        M0 = 4 * A0 - 1
        for D0 in range(1, A0 * A0 + 1):
            assert ((A0 * A0) % D0 == 0) == (A0 % rzero(D0) == 0)
        for D0 in divisors_of_square(A0):
            assert M0 % (4 * rzero(D0)) == 4 * rzero(D0) - 1
            for n0 in range(1, 3 * M0 + 1):
                assert ((n0 + 4 * D0) % M0 == 0) == ((-4 * D0) % M0 == n0 % M0)

    # Lemma 21.2: every intrinsic class has Jacobi symbol -1.  Consequently
    # no square (and, more generally, no unit with Jacobi symbol +1) is hit.
    sign_checks = square_checks = 0
    for M0 in range(3, 2000, 4):
        A0 = (M0 + 1) // 4
        for D0 in divisors_of_square(A0):
            r0 = (-4 * D0) % M0
            assert gcd(r0, M0) == 1
            assert jacobi_symbol(r0, M0) == -1
            sign_checks += 1
            for y0 in (1, 2, 7, 31):
                if gcd(y0, M0) == 1:
                    assert y0 * y0 % M0 != r0
                    square_checks += 1

    # Exact natural densities: the event is periodic modulo the lcm of the
    # moduli.  X=27 has period 4542615, still small enough to enumerate whole.
    expected = {
        3: (3, 2), 7: (21, 8), 11: (231, 64), 15: (1155, 256),
        19: (21945, 4096), 23: (504735, 57344),
        27: (4542615, 516096),
    }
    exact = {}
    for X0, (period0, survivors0) in expected.items():
        moduli0 = list(range(3, X0 + 1, 4))
        assert lcm(*moduli0) == period0
        alive = np.ones(period0, dtype=np.bool_)
        for M0 in moduli0:
            A0 = (M0 + 1) // 4
            residues0 = {(-4 * D0) % M0 for D0 in divisors_of_square(A0)}
            for r0 in residues0:
                alive[r0::M0] = False
        assert int(alive.sum()) == survivors0
        # The common residue 1 and every literal square provide independent
        # regression guards for the two proved escape constructions.
        assert alive[1 % period0]
        for y0 in range(1, min(200, period0)):
            assert alive[(y0 * y0) % period0]
        exact[X0] = f"{survivors0}/{period0}"

    print(f"R0 equivalence exhaustive through A=100; Jacobi -1 on "
          f"{sign_checks} classes ({square_checks} square checks)")
    print("exact full-period avoider densities:", exact)


print("\n== (t) intrinsic-system avoidance (§21) ==")
check_t()

# ---------------------------------------------------------------- (u)
def check_u():
    """Section 22: exact low-degree coefficient solves and new transfers."""
    from itertools import combinations_with_replacement
    from sympy import (Poly, divisors, expand, isprime, linear_eq_to_matrix,
                       linsolve, symbols)

    # The generic raw quadratic has 15 coefficients.  Requiring Q+1 to
    # vanish when either centered input slice is zero is exactly divisibility
    # by h1*h2.  Replay the complete linear solve (rank 11, dimension 4).
    X = symbols("D1 E1 D2 E2")
    z = symbols("u1 v1 u2 v2")
    raw_monomials = [1, *X] + [X[i] * X[j]
                                  for i in range(4) for j in range(i, 4)]
    coeffs = symbols(f"coef0:{len(raw_monomials)}")
    generic = sum(q0 * m0 for q0, m0 in zip(coeffs, raw_monomials))
    centered = expand(generic.subs(dict(zip(X, (zz - 1 for zz in z)))) + 1)
    equations = []
    for restriction, variables in (
            ({z[2]: 0, z[3]: 0}, z[:2]),
            ({z[0]: 0, z[1]: 0}, z[2:])):
        equations.extend(Poly(centered.subs(restriction), *variables).coeffs())
    matrix, rhs = linear_eq_to_matrix(equations, coeffs)
    solution = next(iter(linsolve((matrix, rhs), coeffs)))
    solved_centered = expand(centered.subs(dict(zip(coeffs, solution))))
    assert len(raw_monomials) == 15 and matrix.rank() == 11
    assert all(sum(mon[:2]) == sum(mon[2:]) == 1
               for mon, q0 in Poly(solved_centered, *z).terms() if q0 != 0)
    assert len(solved_centered.free_symbols & set(coeffs)) == 4

    # The support rule (22.5) replays every entry of (22.6).
    expected_counts = {
        (1, 0, 0): 14, (0, 1, 0): 9, (0, 0, 1): 9,
        (2, 0, 0): 10, (1, 1, 0): 7, (1, 0, 1): 7,
        (0, 2, 0): 3, (0, 1, 1): 4, (0, 0, 2): 3,
    }
    for (alpha, beta, gamma), wanted in expected_counts.items():
        qdegree = alpha + beta + gamma
        count = 0
        for degree in (1, 2):
            for indices in combinations_with_replacement(range(4), degree):
                d1 = sum(i < 2 for i in indices)
                d2 = degree - d1
                count += degree >= qdegree and d1 >= beta and d2 >= gamma
        assert count == wanted, ((alpha, beta, gamma), count, wanted)

    # The k1*k2 structure adds exactly three independent coefficient
    # equations: the four entries of R+S must be equal (22.10).
    tensor_coeffs = symbols("tensor0:4")
    tensor_matrix, tensor_rhs = linear_eq_to_matrix(
        [tensor_coeffs[i] - tensor_coeffs[0] for i in range(1, 4)],
        tensor_coeffs)
    tensor_solution = next(iter(linsolve((tensor_matrix, tensor_rhs),
                                         tensor_coeffs)))
    assert tensor_matrix.rank() == 3
    assert len(set(tensor_solution)) == 1

    # Generic tensor-partition identities and the strict lower bound.
    a1, b1, c1, k1, s1, a2, b2, c2, k2, s2 = symbols(
        "a1 b1 c1 k1 s1 a2 b2 c2 k2 s2", positive=True)
    tensor_terms = (a1 * a2, a1 * b2, b1 * a2, b1 * b2)
    for mask in range(1, 15):
        AA = sum(tensor_terms[i] for i in range(4) if mask >> i & 1)
        BB = sum(tensor_terms) - AA
        assert expand(AA + BB - (a1 + b1) * (a2 + b2)) == 0
        # non-tautological strict-lowering ingredient: AB >= a1 b1 a2 b2,
        # spot-checked exactly on a positive grid for every partition mask
        for vals in ((1, 1, 1, 1), (1, 2, 3, 4), (2, 1, 5, 3), (7, 4, 2, 9)):
            sub = dict(zip((a1, b1, a2, b2), vals))
            assert (AA * BB - a1 * b1 * a2 * b2).subs(sub) >= 0, (mask, vals)

    # The explicit 1+3 factor map has maximal output modulus h1*h2.
    D1, E1, D2, E2, h1, h2 = symbols("D1 E1 D2 E2 h1 h2")
    new_D = (D1 + 1) * (D2 + 1) - 1
    new_E = ((D1 + 1) * (E2 + 1) + (E1 + 1) * (D2 + 1)
             + (E1 + 1) * (E2 + 1) - 1)
    aa1, bb1, aa2, bb2 = symbols("aa1 bb1 aa2 bb2")
    factor_subs = {D1: h1 * aa1 - 1, E1: h1 * bb1 - 1,
                   D2: h2 * aa2 - 1, E2: h2 * bb2 - 1}
    assert expand((new_D + 1).subs(factor_subs)
                  - h1 * h2 * aa1 * aa2) == 0
    assert expand((new_E + 1).subs(factor_subs)
                  - h1 * h2 * (aa1 * bb2 + bb1 * aa2 + bb1 * bb2)) == 0

    def parameter_value(a0, b0, c0, k0):
        assert (a0 + b0) % k0 == 0
        return 4 * a0 * b0 * c0 - (a0 + b0) // k0

    def partition_output(left, right, mask):
        p1, a1, b1, c1, k1 = left
        p2, a2, b2, c2, k2 = right
        assert p1 == parameter_value(a1, b1, c1, k1)
        assert p2 == parameter_value(a2, b2, c2, k2)
        terms = (a1 * a2, a1 * b2, b1 * a2, b1 * b2)
        A0 = sum(terms[i] for i in range(4) if mask >> i & 1)
        B0 = sum(terms) - A0
        C0, K0 = 4 * c1 * c2, k1 * k2
        P0 = parameter_value(A0, B0, C0, K0)
        assert P0 > max(p1, p2)
        return P0, A0, B0, C0, K0

    assert partition_output((17, 1, 6, 1, 1), (7, 1, 1, 2, 2), 1) \
        == (409, 1, 13, 8, 2)
    assert partition_output((7, 1, 2, 1, 3), (1217, 17, 18, 1, 5), 1) \
        == (23929, 17, 88, 4, 15)
    # Opposite split: terms 00+11 versus 01+10.
    assert partition_output((73, 2, 5, 2, 1), (47, 1, 3, 4, 4), 9) \
        == (23929, 17, 11, 32, 4)

    # Complete parameter enumeration for a fixed target: AB <= p/2,
    # K | A+B, and C is then forced by (22.20).  This includes non-coprime
    # (A,B), unlike an enumeration of canonical criterion-B rows alone.
    hard_targets = (409, 577, 5569, 9601, 23929, 83449)

    def all_parameter_rows(P0):
        rows = []
        for A0 in range(1, P0 // 2 + 1):
            for B0 in range(1, P0 // (2 * A0) + 1):
                for K0 in divisors(A0 + B0):
                    numerator = K0 * P0 + A0 + B0
                    denominator = 4 * A0 * B0 * K0
                    if numerator % denominator == 0:
                        C0 = numerator // denominator
                        assert C0 >= 1
                        rows.append((A0, B0, C0, K0))
        return rows

    rows_by_target = {P0: all_parameter_rows(P0) for P0 in hard_targets}
    assert [len(rows_by_target[P0]) for P0 in hard_targets] \
        == [14, 14, 20, 14, 78, 30]
    assert [sum(C0 % 4 == 0 for _A0, _B0, C0, _K0
                in rows_by_target[P0]) for P0 in hard_targets] \
        == [2, 0, 0, 2, 22, 0]

    # Invert every primitive tensor partition through every target parameter
    # row.  Record both arbitrary positive sources and prime sources.
    reached_positive, reached_prime = set(), set()
    for P0, rows in rows_by_target.items():
        for A0, B0, C0, K0 in rows:
            if C0 % 4:
                continue
            target_s = (A0 + B0) // K0
            for kk1 in divisors(K0):
                kk2 = K0 // kk1
                for ss1 in divisors(target_s):
                    ss2 = target_s // ss1
                    for aaa1 in range(1, kk1 * ss1):
                        bbb1 = kk1 * ss1 - aaa1
                        for aaa2 in range(1, kk2 * ss2):
                            bbb2 = kk2 * ss2 - aaa2
                            terms = (aaa1 * aaa2, aaa1 * bbb2,
                                     bbb1 * aaa2, bbb1 * bbb2)
                            for mask in range(1, 15):
                                left_sum = sum(terms[i] for i in range(4)
                                               if mask >> i & 1)
                                if left_sum != A0 or sum(terms) - left_sum != B0:
                                    continue
                                for cc1 in divisors(C0 // 4):
                                    cc2 = C0 // (4 * cc1)
                                    source1 = 4 * aaa1 * bbb1 * cc1 - ss1
                                    source2 = 4 * aaa2 * bbb2 * cc2 - ss2
                                    if source1 > 0 and source2 > 0:
                                        assert max(source1, source2) < P0
                                        reached_positive.add(P0)
                                        if isprime(source1) and isprime(source2):
                                            reached_prime.add(P0)
    assert reached_positive == reached_prime == {409, 9601, 23929}

    # Complete one-pair cubic coefficient systems: terms below h^r vanish.
    DD, EE, uu, vv = symbols("DD EE uu vv")
    uni_monomials = [1, DD, EE, DD**2, DD * EE, EE**2,
                     DD**3, DD**2 * EE, DD * EE**2, EE**3]
    uni_coeffs = symbols("uni0:10")
    uni_centered = expand(sum(q0 * m0 for q0, m0 in
                              zip(uni_coeffs, uni_monomials)).subs(
                                  {DD: uu - 1, EE: vv - 1}) + 1)
    for power, expected_rank, expected_dimension in ((1, 1, 9), (2, 3, 7),
                                                      (3, 6, 4)):
        low_equations = [q0 for mon, q0 in Poly(uni_centered, uu, vv).terms()
                         if sum(mon) < power]
        uni_matrix, uni_rhs = linear_eq_to_matrix(low_equations, uni_coeffs)
        uni_solution = next(iter(linsolve((uni_matrix, uni_rhs), uni_coeffs)))
        solved = expand(uni_centered.subs(dict(zip(uni_coeffs, uni_solution))))
        assert uni_matrix.rank() == expected_rank
        assert len(solved.free_symbols & set(uni_coeffs)) == expected_dimension
        assert all(sum(mon) >= power
                   for mon, q0 in Poly(solved, uu, vv).terms() if q0 != 0)

    # Centered powers: identities and exact prime examples.
    for power, wanted in ((2, 59), (3, 503)):
        h0, a0, b0 = 4, 1, 2
        P0 = h0**power * (a0 * b0)**power - a0**power - b0**power
        D0, E0 = h0 * a0 - 1, h0 * b0 - 1
        assert ((D0 + 1)**power - 1) * ((E0 + 1)**power - 1) \
            == 1 + h0**power * P0
        assert P0 == wanted and isprime(P0)
    cubic_hard = 4**3 * (2 * 15)**3 - 2**3 - 15**3
    assert cubic_hard == 1_724_617 and cubic_hard % 24 == 1
    assert isprime(cubic_hard)

    print("sec-22 coefficient systems exact (degree 2 and univariate degree 3); "
          "new tensor maps and centered powers verified; exhaustive six-target "
          "inverse result = 3 reached, 3 blocked")


print("\n== (u) low-degree transfer-map classification (§22) ==")
check_u()

# ---------------------------------------------------------------- (v)
def check_v():
    """Section 23: flexible-(C,K) tensors and their exact inverse search."""
    import os
    from fractions import Fraction
    from functools import lru_cache
    from math import gcd
    from sympy import divisors, expand, isprime, primerange, symbols

    @lru_cache(None)
    def cached_divisors(n):
        return tuple(divisors(n))

    def parameter_value(a, b, c, k):
        assert (a + b) % k == 0
        return 4 * a * b * c - (a + b) // k

    def assert_valid_tuple(P, row):
        """Check the all-positive-integers Type-II identity directly."""
        a, b, c, k = row
        assert min(row) >= 1 and (a + b) % k == 0
        assert parameter_value(a, b, c, k) == P >= 2
        denominators = (a * b * c, P * a * c * k, P * b * c * k)
        assert sum(Fraction(1, d) for d in denominators) == Fraction(4, P)

    def source_record(source):
        P, (a, b, c, k) = source
        assert_valid_tuple(P, (a, b, c, k))
        return (a, b, c, k, (a + b) // k, P)

    def assert_forward_branch(P, target, source1, source2, mask,
                              require_descent=True):
        """Replay one displayed branch, including its exact tensor mask."""
        A, B, C, K = target
        p1, tuple1 = source1
        p2, tuple2 = source2
        left = source_record(source1)
        right = source_record(source2)
        a1, b1, c1, k1 = tuple1
        a2, b2, c2, k2 = tuple2
        terms = (a1 * a2, a1 * b2, b1 * a2, b1 * b2)
        assert 1 <= mask < 15
        assert sum(terms[i] for i in range(4) if mask >> i & 1) == A
        assert sum(terms[i] for i in range(4) if not mask >> i & 1) == B
        modulus_quarter = 4 * c1 * c2 * k1 * k2
        assert C * K == modulus_quarter
        assert (A + B) % K == 0 and modulus_quarter % K == 0
        assert (A, B, modulus_quarter // K, K) == target
        assert_valid_tuple(P, target)
        if require_descent:
            assert 2 <= p1 < P and 2 <= p2 < P
        else:
            assert p1 >= 2 and p2 >= 2
        return (target, left, right, mask)

    def v2(n):
        exponent = 0
        while n % 2 == 0:
            exponent += 1
            n //= 2
        return exponent

    def all_parameter_rows(P):
        """Complete by AB <= P/2 and equation (22.20)."""
        rows = []
        for A in range(1, P // 2 + 1):
            for B in range(1, P // (2 * A) + 1):
                for K in cached_divisors(A + B):
                    numerator = K * P + A + B
                    denominator = 4 * A * B * K
                    if numerator % denominator == 0:
                        rows.append((A, B, numerator // denominator, K))
        return rows

    # A branch is counted with ordered c-, k-, and s-splittings and with one
    # of the 14 ordered nonempty proper tensor subsets.  Source value 1 is
    # excluded, and flexible outputs are not presumed to descend.
    def inverse_branch_summary(P, rows, stop_at_first=False):
        count = 0
        first = None
        for A, B, C, K in rows:
            if C * K % 4:
                continue
            tensor_product = C * K // 4  # (c1*c2)*(k1*k2)
            for kappa in cached_divisors(tensor_product):
                if (A + B) % kappa:
                    continue
                gamma = tensor_product // kappa
                s_product = (A + B) // kappa
                for k1 in cached_divisors(kappa):
                    k2 = kappa // k1
                    for c1 in cached_divisors(gamma):
                        c2 = gamma // c1
                        for s1 in cached_divisors(s_product):
                            s2 = s_product // s1
                            n1, n2 = k1 * s1, k2 * s2
                            assert n1 * n2 == A + B
                            for a1 in range(1, n1):
                                b1 = n1 - a1
                                p1 = parameter_value(a1, b1, c1, k1)
                                if not 2 <= p1 < P:
                                    continue
                                for a2 in range(1, n2):
                                    b2 = n2 - a2
                                    p2 = parameter_value(a2, b2, c2, k2)
                                    if not 2 <= p2 < P:
                                        continue
                                    terms = (a1 * a2, a1 * b2,
                                             b1 * a2, b1 * b2)
                                    for mask in range(1, 15):
                                        left = sum(terms[i] for i in range(4)
                                                   if mask >> i & 1)
                                        if left != A or sum(terms) - left != B:
                                            continue
                                        branch = ((A, B, C, K),
                                                  (a1, b1, c1, k1, s1, p1),
                                                  (a2, b2, c2, k2, s2, p2),
                                                  mask)
                                        count += 1
                                        if first is None:
                                            first = branch
                                        if stop_at_first:
                                            return count, first
        return count, first

    # Fast sufficient inverse with the fixed source tuple (1,1,1,1) for 2.
    # The four monomials are (a,b,a,b), so subset equations reduce to nine
    # coefficient pairs instead of a loop over all a.
    masks_by_counts = {}
    for mask in range(1, 15):
        counts = (sum(bool(mask >> i & 1) for i in (0, 2)),
                  sum(bool(mask >> i & 1) for i in (1, 3)))
        masks_by_counts.setdefault(counts, mask)

    def fixed_two_inverse(P, row):
        A, B, C, K = row
        if C * K % 4 or (A + B) % 2:
            return None
        tensor_product = C * K // 4
        half_sum = (A + B) // 2
        for k2 in cached_divisors(gcd(tensor_product, half_sum)):
            c2, s2 = tensor_product // k2, half_sum // k2
            for (i, j), mask in masks_by_counts.items():
                if i == j:
                    if i != 1 or A != half_sum:
                        continue
                    candidates = range(1, half_sum)
                else:
                    numerator = A - j * half_sum
                    denominator = i - j
                    if numerator % denominator:
                        continue
                    candidates = (numerator // denominator,)
                for a2 in candidates:
                    if not 1 <= a2 < half_sum:
                        continue
                    b2 = half_sum - a2
                    p2 = parameter_value(a2, b2, c2, k2)
                    if 2 <= p2 < P:
                        return (row, (1, 1, 1, 1, 2, 2),
                                (a2, b2, c2, k2, s2, p2), mask)
        return None

    # Symbolic scaling identity and a concrete failure of automatic descent.
    AB, cc, kappa, Kp, ss = symbols("AB cc kappa Kp ss")
    flexible_P = 4 * AB * (4 * cc * kappa / Kp) - kappa * ss / Kp
    assert expand(flexible_P
                  - kappa / Kp * (16 * cc * AB - ss)) == 0
    assert_valid_tuple(2, (1, 1, 1, 1))
    assert_valid_tuple(3, (1, 1, 1, 2))
    # Sources 2 and 75, exact mask 0001, (A,B)=(1,9), C'K'=20:
    # the output 71 is smaller than the source 75.
    warning_branch = assert_forward_branch(
        71, (1, 9, 2, 10), (2, (1, 1, 1, 1)),
        (75, (1, 4, 5, 1)), 0b0001, require_descent=False)
    assert warning_branch[0] == (1, 9, 2, 10)
    assert warning_branch[1][-1] == 2 and warning_branch[2][-1] == 75
    assert 71 < 75

    hard_targets = (409, 577, 5569, 9601, 23929, 83449)
    expected_rows = (14, 14, 20, 14, 78, 30)
    expected_four_C = (2, 0, 0, 2, 22, 0)
    expected_four_CK = (4, 2, 10, 4, 42, 4)
    expected_branches = (272, 48, 1536, 144, 33768, 80)
    rows_by_target = {P: all_parameter_rows(P) for P in hard_targets}
    got_rows, got_four_C, got_four_CK, got_branches = [], [], [], []
    for P in hard_targets:
        rows = rows_by_target[P]
        got_rows.append(len(rows))
        got_four_C.append(sum(C % 4 == 0 for A, B, C, K in rows))
        got_four_CK.append(sum(C * K % 4 == 0 for A, B, C, K in rows))
        branch_count, first = inverse_branch_summary(P, rows)
        got_branches.append(branch_count)
        assert first is not None
    assert tuple(got_rows) == expected_rows
    assert tuple(got_four_C) == expected_four_C
    assert tuple(got_four_CK) == expected_four_CK
    assert tuple(got_branches) == expected_branches

    # Hard-coded replay of all six displayed branches (23.10).  The mask bits
    # index (a1*a2, a1*b2, b1*a2, b1*b2); every displayed split is 0001.
    displayed_2310 = (
        (409, (1, 13, 8, 2), (2, (1, 1, 1, 1)),
         (89, (1, 6, 4, 1)), 0b0001),
        (577, (1, 77, 2, 2), (2, (1, 1, 1, 1)),
         (113, (1, 38, 1, 1)), 0b0001),
        (5569, (1, 41, 34, 6), (2, (1, 1, 1, 1)),
         (4059, (1, 20, 51, 1)), 0b0001),
        (9601, (1, 173, 14, 2), (2, (1, 1, 1, 1)),
         (2321, (1, 86, 7, 1)), 0b0001),
        (23929, (1, 301, 20, 2), (2, (1, 1, 1, 1)),
         (5849, (1, 150, 10, 1)), 0b0001),
        (83449, (5, 39, 107, 4), (2, (1, 1, 1, 1)),
         (36358, (5, 17, 107, 1)), 0b0001),
    )
    fixed_branches = {}
    for P, target, source1, source2, mask in displayed_2310:
        assert target in rows_by_target[P]
        branch = assert_forward_branch(P, target, source1, source2, mask)
        assert fixed_two_inverse(P, target) == branch
        fixed_branches[P] = branch

    # The 577 row also replays all three exact identities in (23.11).
    assert fixed_branches[577] == (
        (1, 77, 2, 2), (1, 1, 1, 1, 2, 2),
        (1, 38, 1, 1, 39, 113), 0b0001)
    for p0, tuple0 in ((2, (1, 1, 1, 1)),
                       (113, (1, 38, 1, 1)),
                       (577, (1, 77, 2, 2))):
        assert_valid_tuple(p0, tuple0)

    # Hard-coded replay of all four exceptional displayed branches (23.13).
    displayed_2313 = (
        (601, (2, 19, 4, 3), (5, (1, 2, 1, 1)),
         (65, (1, 6, 3, 1)), 0b0100),
        (5881, (2, 37, 20, 1), (5, (1, 2, 1, 1)),
         (227, (1, 12, 5, 1)), 0b0100),
        (9049, (1, 566, 4, 81), (59, (1, 20, 1, 1)),
         (8397, (1, 26, 81, 1)), 0b0001),
        (20641, (17, 76, 4, 3), (5, (1, 2, 1, 1)),
         (2825, (14, 17, 3, 1)), 0b0010),
    )
    for branch_data in displayed_2313:
        P, target, source1, source2, mask = branch_data
        assert target in all_parameter_rows(P)
        assert_forward_branch(P, target, source1, source2, mask)

    # Lemma 23.8 needs odd output: at M=4, two source-2 tuples with the
    # singleton split (1,3) read as (4,12,1,1), whose even value is 176.
    assert_valid_tuple(2, (1, 1, 1, 1))
    even_target = (4, 12, 1, 1)
    assert 16 * 1 == 4 * even_target[0]
    assert 16 * 3 == 4 * even_target[1]
    assert_valid_tuple(176, even_target)
    assert even_target[2] * even_target[3] == 1

    # Lemma 23.9 regression: a non-product reading is genuinely active.
    # Two source-5 tuples have tensor sums (3,6), H=16 and factors (47,95).
    assert_valid_tuple(5, (1, 2, 1, 1))
    source_terms = (1, 2, 2, 4)
    tensor_mask = 0b0011
    tensor_A = sum(source_terms[i] for i in range(4)
                   if tensor_mask >> i & 1)
    tensor_B = sum(source_terms[i] for i in range(4)
                   if not tensor_mask >> i & 1)
    assert (tensor_A, tensor_B) == (3, 6)
    H = 16
    factors = (H * tensor_A - 1, H * tensor_B - 1)
    assert factors == (47, 95)
    M = 24
    assert H * gcd(tensor_A, tensor_B) % M == 0
    arbitrary_target = (H * tensor_A // M, H * tensor_B // M, 1, 6)
    assert arbitrary_target == (2, 4, 1, 6)
    assert M == 4 * arbitrary_target[2] * arbitrary_target[3]
    assert factors == (M * arbitrary_target[0] - 1,
                       M * arbitrary_target[1] - 1)
    assert_valid_tuple(31, arbitrary_target)
    assert arbitrary_target[3] == arbitrary_target[0] + arbitrary_target[1]
    assert arbitrary_target[2] * arbitrary_target[3] % 4 != 0
    assert H * gcd(tensor_A, tensor_B) == M * gcd(*arbitrary_target[:2])
    product_target = (tensor_A, tensor_B, 4, 1)
    assert_valid_tuple(279, product_target)
    assert factors == (16 * product_target[0] - 1,
                       16 * product_target[1] - 1)

    # Complete finite audit for Corollary 23.9.1.  The hard-coded row counts
    # prevent a vacuous pass; all rows come from the exhaustive (23.8) loop.
    expected_failures = [73, 193, 241, 673, 1129, 1153, 2473,
                         2521, 3169, 3361, 5281]
    expected_resister_row_counts = (6, 4, 8, 10, 10, 16, 18, 6, 12, 4, 22)
    for P, expected_count in zip(expected_failures,
                                 expected_resister_row_counts):
        rows = all_parameter_rows(P)
        assert len(rows) == expected_count
        for A, B, C, K in rows:
            assert_valid_tuple(P, (A, B, C, K))
            assert v2(C * K) <= 1
            assert gcd(A, B) % 2 == 1
            assert v2(4 * C * K) + v2(gcd(A, B)) <= 3

    # Exact reachability scan.  A failed fixed-2 attempt is passed to the
    # complete inverse enumerator; no-4|CK failures have exhausted all rows.
    def reachability_scan(prime_stop):
        scan_primes = tuple(p for p in primerange(2, prime_stop)
                            if p % 24 == 1)
        no_four_CK, no_inverse, extra_inverse = [], [], []
        fixed_certificates = []
        qualifying_count = inverse_count = 0
        for P in scan_primes:
            rows = all_parameter_rows(P)
            qualifying = [row for row in rows
                          if row[2] * row[3] % 4 == 0]
            if qualifying:
                qualifying_count += 1
            fixed = next((branch for row in qualifying
                          if (branch := fixed_two_inverse(P, row)) is not None),
                         None)
            if fixed is not None:
                fixed_certificates.append((P, fixed))
                inverse_count += 1
                continue
            if not qualifying:
                no_four_CK.append(P)
                no_inverse.append(P)
                continue
            count, branch = inverse_branch_summary(P, rows, stop_at_first=True)
            if count:
                extra_inverse.append(P)
                inverse_count += 1
            else:
                no_inverse.append(P)
        return {
            "primes": scan_primes,
            "qualifying_count": qualifying_count,
            "inverse_count": inverse_count,
            "fixed_certificates": fixed_certificates,
            "extra_inverse": extra_inverse,
            "no_four_CK": no_four_CK,
            "no_inverse": no_inverse,
        }

    scan_10k = reachability_scan(10_001)
    assert len(scan_10k["primes"]) == 143
    assert scan_10k["qualifying_count"] == scan_10k["inverse_count"] == 132
    assert len(scan_10k["fixed_certificates"]) == 129
    assert scan_10k["extra_inverse"] == [601, 5881, 9049]
    assert scan_10k["no_four_CK"] == scan_10k["no_inverse"] == expected_failures

    full_scan_ran = os.environ.get("ES_FULL_SCAN") == "1"
    if full_scan_ran:
        scan_100k = reachability_scan(100_000)
        assert len(scan_100k["primes"]) == 1181
        assert scan_100k["qualifying_count"] == 1170
        assert scan_100k["inverse_count"] == 1170
        assert len(scan_100k["fixed_certificates"]) == 1166
        assert scan_100k["extra_inverse"] == [601, 5881, 9049, 20641]
        assert (scan_100k["no_four_CK"] == scan_100k["no_inverse"]
                == expected_failures)

        other_sources = [(P, branch[2][-1])
                         for P, branch in scan_100k["fixed_certificates"]]
        prime_sources = sum(bool(isprime(source))
                            for P, source in other_sources)
        hard_prime_sources = sum(bool(isprime(source)) and source % 24 == 1
                                 for P, source in other_sources)
        composite_sources = len(other_sources) - prime_sources
        ratios = sorted(Fraction(source, P) for P, source in other_sources)
        median_ratio = (ratios[len(ratios) // 2 - 1]
                        + ratios[len(ratios) // 2]) / 2
        max_ratio = max(ratios)
        assert (prime_sources, hard_prime_sources, composite_sources) == (
            139, 20, 1027)
        assert round(float(median_ratio), 8) == 0.49098945
        assert max_ratio == Fraction(73868, 73897)
        print("ES_FULL_SCAN=1: P < 10^5 row = 1181/1170/1170/1166; "
              "source stats = 139 prime, 20 hard-prime, 1027 composite, "
              f"median {float(median_ratio):.8f}, max {max_ratio}")
    else:
        print("ES_FULL_SCAN=1 replays the P < 10^5 row and source statistics")

    print("flexible tensor validity exact; six targets 4|CK counts =",
          dict(zip(hard_targets, got_four_CK)))
    print("all six old blockers descend; ordered descending branch counts =",
          dict(zip(hard_targets, got_branches)), "; all displayed branches exact")
    print("hard primes <= 10^4: 143 total, 132 flexible-invertible "
          "(129 via source 2), 11 blocked by no tuple with 4|CK")


print("\n== (v) flexible tensor reinterpretation (§23) ==")
check_v()


# ---------------------------------------------------------------- (w)
def check_w():
    """Finite companions for the §24 avoidance bounds and assessments."""
    import numpy as np

    # Finite companion to Lemma 24.5: for the D=1 family, compare avoidance
    # with the local condition excluding prime divisors p == 3 (mod 4).
    d1_rows = []
    N0 = 100_000
    ns0 = np.arange(1, N0 + 1, dtype=np.int64)
    for X0 in (20, 40, 80):
        y0 = ns0 + 4
        local = np.ones(N0, dtype=bool)
        product_density = 1.0
        for p0 in primerange(3, X0 + 1):
            if p0 % 4 == 3:
                local &= y0 % p0 != 0
                product_density *= 1.0 - 1.0 / p0
        divisor_avoider = np.ones(N0, dtype=bool)
        for M0 in range(3, X0 + 1, 4):
            divisor_avoider &= y0 % M0 != 0
        assert np.array_equal(local, divisor_avoider)
        assert abs(local.mean() - product_density) < 3e-4
        d1_rows.append((X0, round(float(local.mean()), 6),
                        round(product_density, 6)))

    # Finite companion to Lemma 24.3: compute the full, honestly
    # deduplicated prime-class mass; this does not verify the asymptotic.
    prime_mass_rows = []
    for X0 in (1_000, 3_000, 10_000, 30_000):
        mass = 0.0
        for ell in primerange(3, X0 + 1):
            if ell % 4 != 3:
                continue
            A0 = (ell + 1) // 4
            f0 = len({(-4 * d0) % ell for d0 in divisors_of_square(A0)})
            mass += f0 / ell
        normalized = mass / log(X0) ** 2
        assert 0.10 < normalized < 0.16
        prime_mass_rows.append((X0, round(mass, 4), round(normalized, 4)))

    # Finite companion to Assessment 24.1: compare actual (R,s)-hit counts
    # with both the raw model and its stated eligibility filters.  The
    # filtered count uses squarefree products <= X, excludes 2, and excludes
    # primes dividing R (equivalently, products not coprime to 4R).
    rng = np.random.default_rng(240124)
    subset_rows = []
    for X0, samples in ((80, 4_000), (160, 3_000)):
        ns = rng.integers(10**11, 9 * 10**11, size=samples,
                          dtype=np.int64)
        actual = raw_model = filtered_model = harmonic = 0.0
        small_primes = tuple(primerange(2, X0 + 1))
        squarefree_products = tuple(
            m0 for m0 in range(1, X0 + 1)
            if m0 % 2 == 1 and all(e0 == 1 for e0 in factorint(m0).values())
        )
        event_count = 0
        for R0 in range(1, (X0 + 1) // 4 + 1):
            q0 = 4 * R0
            phi0 = q0
            for p0 in factorint(q0):
                phi0 -= phi0 // p0
            squarefree_divisors = [1]
            for p0 in factorint(R0):
                squarefree_divisors = (squarefree_divisors
                                       + [s0 * p0 for s0 in squarefree_divisors])
            eligible_products = tuple(
                m0 for m0 in squarefree_products if gcd(m0, R0) == 1
            )
            targets = tuple(range(q0 - 1, X0 + 1, q0))
            for s0 in squarefree_divisors:
                D0 = R0 * R0 // s0
                shifted = ns + 4 * D0
                hit = np.zeros(samples, dtype=bool)
                for M0 in targets:
                    hit |= shifted % M0 == 0
                omega = np.zeros(samples, dtype=np.int16)
                for p0 in small_primes:
                    omega += shifted % p0 == 0
                eligible_count = np.zeros(samples, dtype=np.int16)
                for m0 in eligible_products:
                    eligible_count += shifted % m0 == 0
                actual += float(hit.mean())
                raw_model += float(np.minimum(
                    1.0, np.exp2(omega.astype(float)) / phi0).mean())
                filtered_model += float(np.minimum(
                    1.0, eligible_count.astype(float) / phi0).mean())
                harmonic += sum(1.0 / M0 for M0 in targets)
                event_count += 1
        raw_ratio = raw_model / actual
        filtered_ratio = filtered_model / actual
        assert raw_model > filtered_model > actual
        assert 2.0 < filtered_ratio < 4.5
        assert actual < harmonic
        subset_rows.append((X0, event_count, round(actual, 3),
                            round(raw_model, 3), round(filtered_model, 3),
                            round(raw_ratio, 3), round(filtered_ratio, 3),
                            round(harmonic, 3)))

    # Finite replay of the seven §21.5 table rows; these assertions check the
    # displayed regression diagnostics, not their asymptotic interpretation.
    fit_X = np.array([50, 100, 200, 400, 800, 1600, 3200], dtype=float)
    fit_survivors = np.array(
        [633186, 211887, 54255, 11585, 1740, 201, 14], dtype=float
    )
    fit_y = -np.log(fit_survivors / 12_000_000)
    fit_L = np.log(fit_X)

    def affine_rmse(regressor):
        design = np.column_stack((np.ones(regressor.size), regressor))
        coefficients = np.linalg.lstsq(design, fit_y, rcond=None)[0]
        residual = fit_y - design @ coefficients
        return float(np.sqrt(np.mean(residual**2)))

    reg_loglog = fit_L**2 * np.log(fit_L)
    reg_subset = fit_L**(2 + log(2))
    rmse_loglog = affine_rmse(reg_loglog)
    rmse_subset = affine_rmse(reg_subset)
    reg_correlation = float(np.corrcoef(reg_loglog, reg_subset)[0, 1])
    assert abs(rmse_loglog - 0.0463) < 2e-3
    assert abs(rmse_subset - 0.0768) < 2e-3
    assert abs(reg_correlation - 0.99972) < 2e-3

    # Finite companion to Theorem 24.8: construct the local sets B_p and
    # check every surviving sample against every (R,D,M) event directly.
    X0, Y0, N0 = 100, 5, 100_000
    shifts = []
    for R0 in range(1, Y0 + 1):
        squarefree_divisors = [1]
        for p0 in factorint(R0):
            squarefree_divisors = (squarefree_divisors
                                   + [s0 * p0 for s0 in squarefree_divisors])
        shifts.extend((R0, R0 * R0 // s0) for s0 in squarefree_divisors)
    ns = np.arange(1, N0 + 1, dtype=np.int64)
    certified = np.ones(N0, dtype=bool)
    crt_density = 1.0
    for p0 in primerange(3, X0 + 1):
        if p0 % 4 != 3:
            continue
        bad = {(-4 * D0) % p0 for R0, D0 in shifts if R0 % p0 != 0}
        assert 0 not in bad and len(bad) < p0
        crt_density *= 1.0 - len(bad) / p0
        for b0 in bad:
            certified &= ns % p0 != b0
    for R0, D0 in shifts:
        shifted = ns + 4 * D0
        for M0 in range(4 * R0 - 1, X0 + 1, 4 * R0):
            assert not np.any(certified & (shifted % M0 == 0))
    measured_density = float(certified.mean())
    # N0 gives about 273 expected certified samples here (roughly 6% relative
    # standard error), so a 25% relative window is conservative but meaningful.
    assert N0 * crt_density > 250
    assert abs(measured_density / crt_density - 1.0) < 0.25

    print("D=1 exact local/product densities:", d1_rows)
    print("full prime mass (X, mass, mass/log^2 X):", prime_mass_rows)
    print("subset-product check (X, events, actual, raw, filtered, "
          "raw/actual, filtered/actual, harmonic):", subset_rows)
    print("§21.5 fits (RMSE L^2logL, RMSE subset, correlation): "
          "%.5f, %.5f, %.6f" %
          (rmse_loglog, rmse_subset, reg_correlation))
    print("truncated-fiber certificate: X=100, Y=5, shifts=%d, "
          "density=%.6f (CRT %.6f)" %
          (len(shifts), measured_density, crt_density))


print("\n== (w) H_PF lower-bound routes (§24) ==")
check_w()


# ---------------------------------------------------------------- (x)
def check_x():
    """Section 25: sub-maximal maps, resister anatomy, and the 10^6 census."""
    import os
    from functools import lru_cache
    from math import gcd, isqrt
    from sympy import divisors, factorint, primerange

    resisters = (73, 193, 241, 673, 1129, 1153, 2473, 2521,
                 3169, 3361, 5281)

    @lru_cache(None)
    def divs(n):
        return tuple(divisors(n))

    def v2(n):
        e = 0
        while n % 2 == 0:
            e += 1
            n //= 2
        return e

    def tuple_value(row):
        a, b, c, k = row
        assert min(row) >= 1 and (a + b) % k == 0
        return 4 * a * b * c - (a + b) // k

    def assert_tuple(P, row):
        assert tuple_value(row) == P >= 2

    # For fixed A,B, q=4ABC-P is positive and at most A+B.  Thus C is the
    # unique integer floor(P/(4AB))+1, and q | A+B is the exact tuple test.
    def row_at(P, A, B):
        if 2 * A * B > P:
            return None
        C = P // (4 * A * B) + 1
        q = 4 * A * B * C - P
        if (A + B) % q:
            return None
        return (A, B, C, (A + B) // q)

    def all_rows(P):
        rows = []
        for A in range(1, isqrt(P // 2) + 1):
            for B in range(A, P // (2 * A) + 1):
                row = row_at(P, A, B)
                if row is None:
                    continue
                rows.append(row)
                if A != B:
                    rows.append((B, A, row[2], row[3]))
        return sorted(rows)

    # Every displayed anatomy row and cell is a regression constant.  The last
    # Boolean says that notes.md prints “+ swap”; expansion below also swaps the
    # two hard-coded factor dictionaries.  These comparisons are deliberately
    # independent of factorint's reconstruction of its own output.
    # row, CK, v2(C), v2(A+B), gcd(A,B), factors(FA), factors(FB), add_swap
    anatomy_rows = {
        73: (
            ((1, 20, 1, 3), 3, 0, 0, 1, ((11, 1),), ((239, 1),), False),
            ((1, 21, 1, 2), 2, 0, 1, 1, ((7, 1),), ((167, 1),), False),
            ((2, 5, 2, 1), 2, 1, 0, 1, ((3, 1), (5, 1)), ((3, 1), (13, 1)), False),
            ((5, 2, 2, 1), 2, 1, 0, 1, ((3, 1), (13, 1)), ((3, 1), (5, 1)), False),
            ((20, 1, 1, 3), 3, 0, 0, 1, ((239, 1),), ((11, 1),), False),
            ((21, 1, 1, 2), 2, 0, 1, 1, ((167, 1),), ((7, 1),), False),
        ),
        193: (
            ((2, 5, 5, 1), 5, 0, 0, 1, ((3, 1), (13, 1)), ((3, 2), (11, 1)), False),
            ((2, 13, 2, 1), 2, 1, 0, 1, ((3, 1), (5, 1)), ((103, 1),), False),
            ((5, 2, 5, 1), 5, 0, 0, 1, ((3, 2), (11, 1)), ((3, 1), (13, 1)), False),
            ((13, 2, 2, 1), 2, 1, 0, 1, ((103, 1),), ((3, 1), (5, 1)), False),
        ),
        241: (
            ((1, 21, 3, 2), 6, 0, 1, 1, ((23, 1),), ((503, 1),), False),
            ((1, 22, 3, 1), 3, 0, 0, 1, ((11, 1),), ((263, 1),), False),
            ((1, 62, 1, 9), 9, 0, 0, 1, ((5, 1), (7, 1)), ((23, 1), (97, 1)), False),
            ((1, 69, 1, 2), 2, 0, 1, 1, ((7, 1),), ((19, 1), (29, 1)), False),
            ((21, 1, 3, 2), 6, 0, 1, 1, ((503, 1),), ((23, 1),), False),
            ((22, 1, 3, 1), 3, 0, 0, 1, ((263, 1),), ((11, 1),), False),
            ((62, 1, 1, 9), 9, 0, 0, 1, ((23, 1), (97, 1)), ((5, 1), (7, 1)), False),
            ((69, 1, 1, 2), 2, 0, 1, 1, ((19, 1), (29, 1)), ((7, 1),), False),
        ),
        673: (
            ((1, 34, 5, 5), 25, 0, 0, 1, ((3, 2), (11, 1)), ((3, 1), (11, 1), (103, 1)), True),
            ((2, 5, 17, 1), 17, 0, 0, 1, ((3, 3), (5, 1)), ((3, 1), (113, 1)), True),
            ((2, 43, 2, 3), 6, 1, 0, 1, ((47, 1),), ((1031, 1),), True),
            ((2, 45, 2, 1), 2, 1, 0, 1, ((3, 1), (5, 1)), ((359, 1),), True),
            ((3, 19, 3, 2), 6, 0, 1, 1, ((71, 1),), ((5, 1), (7, 1), (13, 1)), True),
        ),
        1129: (
            ((1, 285, 1, 26), 26, 0, 1, 1, ((103, 1),), ((107, 1), (277, 1)), True),
            ((1, 308, 1, 3), 3, 0, 0, 1, ((11, 1),), ((5, 1), (739, 1)), True),
            ((2, 13, 11, 1), 11, 0, 0, 1, ((3, 1), (29, 1)), ((571, 1),), True),
            ((2, 29, 5, 1), 5, 0, 0, 1, ((3, 1), (13, 1)), ((3, 1), (193, 1)), True),
            ((3, 19, 5, 2), 10, 0, 1, 1, ((7, 1), (17, 1)), ((3, 1), (11, 1), (23, 1)), True),
        ),
        1153: (
            ((1, 17, 17, 6), 102, 0, 1, 1, ((11, 1), (37, 1)), ((5, 1), (19, 1), (73, 1)), True),
            ((2, 5, 29, 1), 29, 0, 0, 1, ((3, 1), (7, 1), (11, 1)), ((3, 1), (193, 1)), True),
            ((2, 21, 7, 1), 7, 0, 0, 1, ((5, 1), (11, 1)), ((587, 1),), True),
            ((2, 73, 2, 5), 10, 1, 0, 1, ((79, 1),), ((3, 1), (7, 1), (139, 1)), True),
            ((2, 77, 2, 1), 2, 1, 0, 1, ((3, 1), (5, 1)), ((3, 1), (5, 1), (41, 1)), True),
            ((2, 145, 1, 21), 21, 0, 0, 1, ((167, 1),), ((19, 1), (641, 1)), True),
            ((2, 165, 1, 1), 1, 0, 0, 1, ((7, 1),), ((659, 1),), True),
            ((5, 58, 1, 9), 9, 0, 0, 1, ((179, 1),), ((2087, 1),), True),
        ),
        2473: (
            ((1, 20, 31, 3), 93, 0, 0, 1, ((7, 1), (53, 1)), ((43, 1), (173, 1)), True),
            ((1, 62, 10, 9), 90, 1, 0, 1, ((359, 1),), ((11, 1), (2029, 1)), True),
            ((1, 209, 3, 6), 18, 0, 1, 1, ((71, 1),), ((41, 1), (367, 1)), True),
            ((1, 212, 3, 3), 9, 0, 0, 1, ((5, 1), (7, 1)), ((13, 1), (587, 1)), True),
            ((2, 5, 62, 1), 62, 1, 0, 1, ((3, 2), (5, 1), (11, 1)), ((3, 1), (7, 1), (59, 1)), True),
            ((2, 45, 7, 1), 7, 0, 0, 1, ((5, 1), (11, 1)), ((1259, 1),), True),
            ((2, 165, 2, 1), 2, 1, 0, 1, ((3, 1), (5, 1)), ((1319, 1),), True),
            ((4, 31, 5, 5), 25, 0, 0, 1, ((3, 1), (7, 1), (19, 1)), ((3, 1), (1033, 1)), True),
            ((5, 42, 3, 1), 3, 0, 0, 1, ((59, 1),), ((503, 1),), True),
        ),
        2521: (
            ((2, 29, 11, 1), 11, 0, 0, 1, ((3, 1), (29, 1)), ((3, 1), (5, 2), (17, 1)), True),
            ((2, 159, 2, 7), 14, 1, 0, 1, ((3, 1), (37, 1)), ((29, 1), (307, 1)), True),
            ((4, 161, 1, 3), 3, 0, 0, 1, ((47, 1),), ((1931, 1),), True),
        ),
        3169: (
            ((1, 114, 7, 5), 35, 0, 0, 1, ((139, 1),), ((15959, 1),), True),
            ((1, 797, 1, 42), 42, 0, 1, 1, ((167, 1),), ((5, 1), (61, 1), (439, 1)), True),
            ((1, 834, 1, 5), 5, 0, 0, 1, ((19, 1),), ((13, 1), (1283, 1)), True),
            ((2, 21, 19, 1), 19, 0, 0, 1, ((151, 1),), ((5, 1), (11, 1), (29, 1)), True),
            ((2, 397, 1, 57), 57, 0, 0, 1, ((5, 1), (7, 1), (13, 1)), ((5, 1), (43, 1), (421, 1)), True),
            ((2, 453, 1, 1), 1, 0, 0, 1, ((7, 1),), ((1811, 1),), True),
        ),
        3361: (
            ((1, 29, 29, 10), 290, 0, 1, 1, ((19, 1), (61, 1)), ((3, 1), (11213, 1)), True),
            ((5, 34, 5, 1), 5, 0, 0, 1, ((3, 2), (11, 1)), ((7, 1), (97, 1)), True),
        ),
        5281: (
            ((1, 21, 63, 2), 126, 0, 1, 1, ((503, 1),), ((19, 1), (557, 1)), True),
            ((1, 38, 35, 1), 35, 0, 0, 1, ((139, 1),), ((3, 3), (197, 1)), True),
            ((1, 265, 5, 14), 70, 0, 1, 1, ((3, 2), (31, 1)), ((3, 1), (24733, 1)), True),
            ((1, 278, 5, 1), 5, 0, 0, 1, ((19, 1),), ((3, 1), (17, 1), (109, 1)), True),
            ((1, 1322, 1, 189), 189, 0, 0, 1, ((5, 1), (151, 1)), ((999431, 1),), True),
            ((1, 1329, 1, 38), 38, 0, 1, 1, ((151, 1),), ((13, 1), (41, 1), (379, 1)), True),
            ((1, 1358, 1, 9), 9, 0, 0, 1, ((5, 1), (7, 1)), ((19, 1), (31, 1), (83, 1)), True),
            ((1, 1509, 1, 2), 2, 0, 1, 1, ((7, 1),), ((12071, 1),), True),
            ((3, 63, 7, 6), 42, 0, 1, 3, ((503, 1),), ((19, 1), (557, 1)), True),
            ((6, 17, 13, 1), 13, 0, 0, 1, ((311, 1),), ((883, 1),), True),
            ((13, 102, 1, 5), 5, 0, 0, 1, ((7, 1), (37, 1)), ((2039, 1),), True),
        ),
    }
    expected_anatomy = {P: {} for P in resisters}
    for P, displayed_rows in anatomy_rows.items():
        for row, R, vC, vSum, coordinate_gcd, factors_A, factors_B, add_swap in displayed_rows:
            expected_anatomy[P][row] = (R, vC, vSum, coordinate_gcd, factors_A, factors_B)
            if add_swap:
                swapped = (row[1], row[0], row[2], row[3])
                expected_anatomy[P][swapped] = (
                    R, vC, vSum, coordinate_gcd, factors_B, factors_A,
                )

    expected_counts = (6, 4, 8, 10, 10, 16, 18, 6, 12, 4, 22)
    expected_distinct_CK = (2, 2, 4, 4, 5, 8, 9, 3, 6, 2, 10)
    rows_by_P = {}
    for P, expected_count, expected_CK_count in zip(
            resisters, expected_counts, expected_distinct_CK):
        rows = all_rows(P)
        rows_by_P[P] = rows
        assert len(rows) == expected_count
        assert set(rows) == set(expected_anatomy[P])
        assert len({C * K for A, B, C, K in rows}) == expected_CK_count
        for row in rows:
            A, B, C, K = row
            assert_tuple(P, row)
            R = C * K
            FA, FB = 4 * A * R - 1, 4 * B * R - 1
            expected_R, expected_vC, expected_vSum, expected_gcd, expected_FA, expected_FB = expected_anatomy[P][row]
            assert R == expected_R
            assert v2(C) == expected_vC
            assert v2(A + B) == expected_vSum
            assert gcd(A, B) == expected_gcd
            assert tuple(sorted(factorint(FA).items())) == expected_FA
            assert tuple(sorted(factorint(FB).items())) == expected_FB
            assert FA * FB == 4 * P * C * K * K + 1
            assert v2(C) + v2(A + B) <= 1
            assert gcd(A, B) % 2 == 1

    # Pointwise h1-expressivity is vacuous on this finite target set: for
    # every row, (1,1,CK,1) is a smaller source with the required ck-product.
    degenerate_rows = 0
    for P in resisters:
        for A, B, C, K in rows_by_P[P]:
            R = C * K
            source = (1, 1, R, 1)
            source_P = 4 * R - 2
            assert_tuple(source_P, source)
            assert source[2] * source[3] == R
            assert 2 <= source_P < P
            degenerate_rows += 1
    assert degenerate_rows == sum(expected_counts) == 116

    # Exact inverse for u1+n*u1*z2 and v1+m*v1*w2, n,m in {1,2,3},
    # with aligned or swapped second-source coordinates.  Divisors of A and
    # B make the search finite and complete for this stated coefficient box.
    def shifted_inverses(P, target):
        A, B, C, K = target
        R = C * K
        hits = []
        for a1 in divs(A):
            qA = A // a1
            for b1 in divs(B):
                qB = B // b1
                for k1 in divs(gcd(R, a1 + b1)):
                    c1 = R // k1
                    p1 = tuple_value((a1, b1, c1, k1))
                    if not 2 <= p1 < P:
                        continue
                    for n in (1, 2, 3):
                        if (qA - 1) % (4 * n):
                            continue
                        RA = (qA - 1) // (4 * n)
                        if RA <= 0:
                            continue
                        for m in (1, 2, 3):
                            if (qB - 1) % (4 * m):
                                continue
                            RB = (qB - 1) // (4 * m)
                            if RB <= 0:
                                continue
                            for c2k2 in divs(gcd(RA, RB)):
                                x, y = RA // c2k2, RB // c2k2
                                for swapped in (False, True):
                                    a2, b2 = ((y, x) if swapped else (x, y))
                                    for k2 in divs(gcd(c2k2, a2 + b2)):
                                        c2 = c2k2 // k2
                                        p2 = tuple_value((a2, b2, c2, k2))
                                        if not 2 <= p2 < P:
                                            continue
                                        z2, w2 = ((b2, a2) if swapped
                                                  else (a2, b2))
                                        assert A == a1 * (1 + n * 4 * c2 * k2 * z2)
                                        assert B == b1 * (1 + m * 4 * c2 * k2 * w2)
                                        hits.append((n, m, swapped,
                                                     (p1, (a1, b1, c1, k1)),
                                                     (p2, (a2, b2, c2, k2))))
        return hits

    expected_shifted_rows = (0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 2)
    expected_shifted_branches = (0, 0, 0, 0, 0, 8, 8, 0, 0, 8, 16)
    shifted_rows = []
    shifted_branches = []
    for P in resisters:
        hit_rows = 0
        branches = 0
        for row in rows_by_P[P]:
            hits = shifted_inverses(P, row)
            hit_rows += bool(hits)
            branches += len(hits)
        shifted_rows.append(hit_rows)
        shifted_branches.append(branches)
    assert tuple(shifted_rows) == expected_shifted_rows
    assert tuple(shifted_branches) == expected_shifted_branches
    # A negative cross coefficient gives 1-n*h2*z2 <= -3, so cannot produce
    # a positive target coordinate; this closes the requested minus variants.
    assert all(1 - n * 4 * z <= -3 for n in (1, 2, 3)
               for z in range(1, 5))

    displayed_shifted = (
        (1153, (5, 58, 1, 9), (69, (1, 2, 9, 1)),
         (20, (1, 7, 1, 1))),
        (2473, (5, 42, 3, 1), (21, (1, 2, 3, 1)),
         (14, (1, 5, 1, 1))),
        (3361, (5, 34, 5, 1), (37, (1, 2, 5, 1)),
         (11, (1, 4, 1, 1))),
        (5281, (13, 102, 1, 5), (113, (1, 6, 5, 1)),
         (41, (3, 4, 1, 1))),
    )
    for P, target, source1, source2 in displayed_shifted:
        p1, (a1, b1, c1, k1) = source1
        p2, (a2, b2, c2, k2) = source2
        assert_tuple(p1, source1[1])
        assert_tuple(p2, source2[1])
        assert 2 <= p1 < P and 2 <= p2 < P
        assert c1 * k1 == target[2] * target[3]
        output = (a1 * (1 + 4 * c2 * k2 * a2),
                  b1 * (1 + 4 * c2 * k2 * b2),
                  target[2], target[3])
        assert output == target and tuple_value(output) == P

    # Three fixed M=g maps are descending-surjective on every k=1 Type-II
    # tuple except (1,1,C,1).  The source construction checks those genuinely
    # coefficient-fixed maps end to end; no target-dependent coefficient enters.
    def additive_certificate(P, target):
        A, B, C, K = target
        if K != 1:
            return None
        R = C
        if A >= 2 and B >= 2:       # (-1+u1+u2, -1+v1+v2)
            map_name = "sum-sum"
            source1 = (1, 1, R, 1)
            source2 = (A - 1, B - 1, R, 1)
            output = (source1[0] + source2[0],
                      source1[1] + source2[1], C, K)
        elif A == 1 and B >= 2:     # (-1+u1, -1+v1+v2)
            map_name = "copy-sum"
            source1 = (1, 1, R, 1)
            source2 = (1, B - 1, R, 1)
            output = (source1[0], source1[1] + source2[1], C, K)
        elif B == 1 and A >= 2:     # (-1+u1+u2, -1+v1)
            map_name = "sum-copy"
            source1 = (1, 1, R, 1)
            source2 = (A - 1, 1, R, 1)
            output = (source1[0] + source2[0], source1[1], C, K)
        else:
            return None
        p1, p2 = tuple_value(source1), tuple_value(source2)
        assert output == target and tuple_value(output) == P
        assert 2 <= p1 < P and 2 <= p2 < P
        assert 4 * source1[2] * source1[3] == 4 * R
        assert 4 * source2[2] * source2[3] == 4 * R
        return map_name, (p1, source1), (p2, source2)

    displayed_additive = {
        73: ((2, 5, 2, 1), 6, 27),
        193: ((2, 5, 5, 1), 18, 75),
        241: ((1, 22, 3, 1), 10, 230),
        673: ((2, 5, 17, 1), 66, 267),
        1129: ((2, 13, 11, 1), 42, 515),
        1153: ((2, 5, 29, 1), 114, 459),
        2473: ((2, 5, 62, 1), 246, 987),
        2521: ((2, 29, 11, 1), 42, 1203),
        3169: ((2, 21, 19, 1), 74, 1499),
        3361: ((5, 34, 5, 1), 18, 2603),
        5281: ((6, 17, 13, 1), 50, 4139),
    }
    additive_resister_targets = {}
    for P, (target, expected_p1, expected_p2) in displayed_additive.items():
        assert target in rows_by_P[P]
        certificate = additive_certificate(P, target)
        assert certificate is not None
        _, (p1, _), (p2, _) = certificate
        assert (p1, p2) == (expected_p1, expected_p2)
        additive_resister_targets[P] = target

    # Fast fixed-source-2 inverse used in the census.
    count_pairs = ((0, 1), (0, 2), (1, 0), (1, 1),
                   (1, 2), (2, 0), (2, 1))

    def fixed_two_inverse(P, row):
        A, B, C, K = row
        if C * K % 4 or (A + B) % 2:
            return None
        tensor_product = C * K // 4
        half_sum = (A + B) // 2
        for k2 in divs(gcd(tensor_product, half_sum)):
            c2 = tensor_product // k2
            for i, j in count_pairs:
                if i == j:
                    if i != 1 or A != half_sum:
                        continue
                    candidates = range(1, half_sum)
                else:
                    numerator, denominator = A - j * half_sum, i - j
                    if numerator % denominator:
                        continue
                    candidates = (numerator // denominator,)
                for a2 in candidates:
                    if not 1 <= a2 < half_sum:
                        continue
                    b2 = half_sum - a2
                    p2 = tuple_value((a2, b2, c2, k2))
                    if 2 <= p2 < P:
                        return row, (a2, b2, c2, k2, p2)
        return None

    extra_branches = {
        601: ((2, 19, 4, 3), (5, (1, 2, 1, 1)),
              (65, (1, 6, 3, 1)), 0b0100),
        5881: ((2, 37, 20, 1), (5, (1, 2, 1, 1)),
               (227, (1, 12, 5, 1)), 0b0100),
        9049: ((1, 566, 4, 81), (59, (1, 20, 1, 1)),
               (8397, (1, 26, 81, 1)), 0b0001),
        20641: ((17, 76, 4, 3), (5, (1, 2, 1, 1)),
                (2825, (14, 17, 3, 1)), 0b0010),
    }

    def assert_extra_branch(P, data):
        target, source1, source2, mask = data
        p1, (a1, b1, c1, k1) = source1
        p2, (a2, b2, c2, k2) = source2
        assert_tuple(p1, source1[1])
        assert_tuple(p2, source2[1])
        terms = (a1 * a2, a1 * b2, b1 * a2, b1 * b2)
        A = sum(terms[i] for i in range(4) if mask >> i & 1)
        B = sum(terms) - A
        C, K = target[2:]
        assert C * K == 4 * c1 * c2 * k1 * k2
        assert (A, B) == target[:2]
        assert tuple_value(target) == P and 2 <= p1 < P and 2 <= p2 < P
        return target

    def reachability_census(stop, cap=3000):
        primes = tuple(p for p in primerange(2, stop) if p % 24 == 1)
        fixed, pending, target_by_P = [], [], {}
        for P in primes:
            certificate = None
            saw_qualifying = False
            for B in range(1, min(cap, P // 2) + 1):
                for A in (1, 2, 3):
                    row = row_at(P, A, B)
                    if row is None or row[2] * row[3] % 4:
                        continue
                    saw_qualifying = True
                    certificate = fixed_two_inverse(P, row)
                    if certificate is not None:
                        break
                if certificate is not None:
                    break
            if certificate is None:
                pending.append((P, saw_qualifying))
            else:
                fixed.append(P)
                target_by_P[P] = certificate[0]

        no_four_CK, extras = [], []
        qualifying_count = len(fixed)
        for P, _ in pending:
            rows = all_rows(P)
            qualifying = [row for row in rows if row[2] * row[3] % 4 == 0]
            if not qualifying:
                no_four_CK.append(P)
                target_by_P[P] = rows[0]
                continue
            qualifying_count += 1
            certificate = next((cert for row in qualifying
                                if (cert := fixed_two_inverse(P, row))
                                is not None), None)
            if certificate is not None:
                fixed.append(P)
                target_by_P[P] = certificate[0]
                continue
            assert P in extra_branches
            target = assert_extra_branch(P, extra_branches[P])
            assert target in qualifying
            extras.append(P)
            target_by_P[P] = target

        if stop == 1_000_001:
            assert len(pending) == 407

        # A pure descending certificate exists for every prime having a
        # qualifying row.  For the residual eleven,
        # the fixed additive maps cover a k=1 row.  This remains diagnostic
        # descent: selecting that target row has already supplied a witness.
        assert set(target_by_P) == set(primes)
        for P in no_four_CK:
            assert P in additive_resister_targets
            assert additive_certificate(P, additive_resister_targets[P])
        return (len(primes), qualifying_count, len(fixed) + len(extras),
                len(fixed), extras, no_four_CK)

    scan_20k = reachability_census(20_001)
    assert scan_20k == (267, 256, 256, 253,
                        [601, 5881, 9049], list(resisters))

    full_scan_ran = os.environ.get("ES_FULL_SCAN") == "1"
    if full_scan_ran:
        scan_1m = reachability_census(1_000_001)
        assert scan_1m == (9732, 9721, 9721, 9717,
                           [601, 5881, 9049, 20641], list(resisters))
        print("ES_FULL_SCAN=1: P <= 10^6 row = "
              "9732/9721/9721/9717; pure resisters unchanged (11); "
              "adding three fixed M=g maps covers all 9732 census primes")
    else:
        print("ES_FULL_SCAN=1 replays the complete P <= 10^6 census")

    # Exact witness-division law and its obstruction when t divides P but
    # not C: (6;1,1,2,1)/2 gives (3;1,1,1,2), while division by 3 cannot
    # preserve the factor pair 7*7 at any modulus satisfying C''K''^2=6.
    assert_tuple(6, (1, 1, 2, 1))
    assert_tuple(3, (1, 1, 1, 2))
    assert 2 % 2 == 0 and (1, 1, 2 // 2, 2 * 1) == (1, 1, 1, 2)
    old_factors = (7, 7)
    assert all(not (D % (4 * C2 * K2) == -1 % (4 * C2 * K2)
                        and E % (4 * C2 * K2) == -1 % (4 * C2 * K2))
               for C2 in divs(6) for K2 in range(1, isqrt(6) + 1)
               if C2 * K2 * K2 == 6 for D, E in (old_factors,))

    print("resister anatomy: all 116 ordered rows and displayed cells "
          "hard-coded; every row has a smaller ck-matched source")
    print("shifted h1 maps (cross coefficients ±1..±3): four targets fall "
          "{1153,2473,3361,5281}; seven resist this finite box")
    print("fixed additive M=g maps: all eleven old resisters fall; default "
          "pure-tensor census P <= 20000 leaves exactly the same eleven")


print("\n== (x) sub-maximal transfer maps and extended census (§25) ==")
check_x()

# ---------------------------------------------------------------- (y)
def check_y():
    """Section 26: Type-I divisor form, transfers, and combined payoff."""
    from functools import lru_cache
    from sympy import divisors, expand, symbols

    @lru_cache(None)
    def cached_divisors(n):
        return tuple(divisors(n))

    def type_i_value(row):
        a, b, c, k = row
        assert min(row) >= 1 and (a + b) % k == 0
        m = (a + b) // k
        numerator = 4 * a * b * c - 1
        assert numerator % m == 0
        return numerator // m

    def assert_type_i(P, row):
        a, b, c, k = row
        assert type_i_value(row) == P >= 2
        assert P * (a + b) == k * (4 * a * b * c - 1)
        denominators = (a * c * k, b * c * k, P * a * b * c)
        assert sum(Fraction(1, d) for d in denominators) == Fraction(4, P)
        m, z0, d0 = (a + b) // k, a * b * c, a * a * c
        assert z0 == (P * m + 1) // 4
        assert z0 * z0 % d0 == 0 and (z0 + d0) % m == 0
        assert ((z0 + d0) // m, (z0 + z0 * z0 // d0) // m,
                P * z0) == denominators

    def all_type_i_rows(P):
        """Complete Lemma-26.2 divisor enumeration; ordered in (a,b)."""
        rows = []
        for k in range(1, 2 * P // 3 + 1):
            for c in range(1, (2 * P + k) // (4 * k) + 1):
                if gcd(P, c * k) != 1:
                    continue
                h = 4 * c * k
                norm = P * P + 4 * c * k * k
                for D in cached_divisors(norm):
                    if (D + P) % h:
                        continue
                    E = norm // D
                    # Coprimality makes this automatic; retain it as an
                    # independent regression for the bookkeeping in Thm 26.1.
                    assert (E + P) % h == 0
                    a, b = (D + P) // h, (E + P) // h
                    row = (a, b, c, k)
                    assert min(row) >= 1 and type_i_value(row) == P
                    assert (h * a - P) * (h * b - P) == norm
                    rows.append(row)
        assert len(rows) == len(set(rows))
        return tuple(sorted(rows))

    # The factor identity itself, and the exact point at which cancellation
    # needs gcd(p,4ck)=1.
    a, b, c, k, p = symbols("a b c k p", integer=True)
    lhs = (4 * a * c * k - p) * (4 * b * c * k - p)
    relation_reduced = expand(lhs - (p * p + 4 * c * k * k))
    assert expand(relation_reduced - 4 * c * k * (
        k * (4 * a * b * c - 1) - p * (a + b))) == 0
    bad_p, bad_c, bad_k, bad_D = 3, 1, 3, 9
    bad_h = 4 * bad_c * bad_k
    bad_norm = bad_p * bad_p + 4 * bad_c * bad_k * bad_k
    assert bad_norm == 45 and bad_norm % bad_D == 0
    assert (bad_D + bad_p) % bad_h == 0
    assert (bad_norm // bad_D + bad_p) % bad_h != 0

    expected_7 = (
        (1, 1, 2, 2), (1, 2, 1, 3), (1, 8, 2, 1),
        (1, 9, 1, 2), (2, 1, 1, 3), (2, 15, 1, 1),
        (8, 1, 2, 1), (9, 1, 1, 2), (15, 2, 1, 1),
    )
    expected_17 = (
        (1, 6, 5, 1), (2, 5, 3, 1),
        (5, 2, 3, 1), (6, 1, 5, 1),
    )
    expected_73 = (
        (1, 5, 11, 2), (1, 11, 5, 4), (2, 21, 10, 1),
        (3, 20, 7, 1), (5, 1, 11, 2), (11, 1, 5, 4),
        (20, 3, 7, 1), (21, 2, 10, 1),
    )
    expected_193 = (
        (1, 5, 29, 2), (1, 13, 26, 2), (1, 29, 5, 10),
        (5, 1, 29, 2), (5, 138, 10, 1), (13, 1, 26, 2),
        (29, 1, 5, 10), (138, 5, 10, 1),
    )
    expected_241 = (
        (1, 22, 63, 1), (2, 21, 33, 1), (2, 69, 31, 1),
        (3, 66, 7, 3), (9, 14, 11, 1), (14, 9, 11, 1),
        (21, 2, 33, 1), (22, 1, 63, 1), (66, 3, 7, 3),
        (69, 2, 31, 1),
    )
    assert all_type_i_rows(7) == expected_7
    assert all_type_i_rows(17) == expected_17
    assert all_type_i_rows(73) == expected_73
    assert all_type_i_rows(193) == expected_193
    assert all_type_i_rows(241) == expected_241
    for P, row in ((7, (1, 1, 2, 2)),
                   (17, (2, 5, 3, 1)),
                   (73, (1, 5, 11, 2))):
        assert_type_i(P, row)

    resisters = (73, 193, 241, 673, 1129, 1153, 2473,
                 2521, 3169, 3361, 5281)
    expected_counts = (8, 8, 10, 26, 32, 30, 56, 12, 26, 26, 36)
    expected_primitive = (8, 8, 8, 24, 28, 28, 48, 12, 26, 26, 30)
    expected_m_counts = (2, 3, 2, 8, 7, 9, 12, 4, 9, 9, 11)
    expected_max_k = (4, 10, 3, 34, 26, 58, 124, 11, 38, 29, 78)
    expected_m_divides_k = (0, 0, 0, 0, 2, 0, 4, 0, 2, 0, 4)
    type_i_rows = {}
    for P, count, primitive_count, m_count, max_k, divisible_count in zip(
            resisters, expected_counts, expected_primitive,
            expected_m_counts, expected_max_k, expected_m_divides_k):
        rows = all_type_i_rows(P)
        type_i_rows[P] = rows
        assert len(rows) == count
        assert all(row[0] != row[1] for row in rows)
        assert len({(min(a0, b0), max(a0, b0), c0, k0)
                    for a0, b0, c0, k0 in rows}) == count // 2
        assert sum(gcd(row[0], row[1]) == 1 for row in rows) == primitive_count
        assert len({(a0 + b0) // k0 for a0, b0, c0, k0 in rows}) == m_count
        assert max(row[3] for row in rows) == max_k
        assert sum(k0 % ((a0 + b0) // k0) == 0
                   for a0, b0, c0, k0 in rows) == divisible_count
        for row in rows:
            assert_type_i(P, row)

    # Brahmagupta reaches the quadratic-form value for 73 but all four
    # balanced source-factor products have the wrong target residue.
    assert_type_i(5, (1, 2, 2, 1))
    assert_type_i(13, (2, 9, 2, 1))
    norm1, factors1 = 33, (3, 11)
    norm2, factors2 = 177, (3, 59)
    target_P, target_K, fixed_c = 73, 8, 2
    assert norm1 * norm2 == target_P**2 + 4 * fixed_c * target_K**2
    balanced = tuple((x * y) % 64 for x in factors1 for y in factors2)
    assert balanced == (9, 49, 33, 9)
    assert (-target_P) % 64 == 55 and 55 not in balanced
    assert not any(row[2:] == (fixed_c, target_K)
                   for row in type_i_rows[73])

    def corrected_type_i(source1, source2, t):
        p1, row1 = source1
        p2, row2 = source2
        assert_type_i(p1, row1)
        assert_type_i(p2, row2)
        a1, b1, c1, k1 = row1
        a2, b2, c2, k2 = row2
        m1, m2 = (a1 + b1) // k1, (a2 + b2) // k2
        assert m1 == m2
        m = m1
        A = a1 * a2
        B = (a1 + b1) * (a2 + b2) - A
        C = m * t - 4 * c1 * c2
        K = k1 * k2 * m
        assert C > 0 and (4 * A * B * C - 1) % m == 0
        P = (4 * A * B * C - 1) // m
        target = (A, B, C, K)
        assert_type_i(P, target)
        assert P > max(p1, p2)
        return P, target

    binary_examples = (
        ((5, (1, 2, 2, 1)), (29, (1, 11, 2, 4)), 23,
         2473, (1, 35, 53, 12)),
        ((17, (1, 6, 5, 1)), (17, (2, 5, 3, 1)), 17,
         3169, (2, 47, 59, 7)),
        ((5, (1, 2, 2, 1)), (13, (1, 5, 2, 2)), 83,
         5281, (1, 17, 233, 6)),
    )
    for source1, source2, t, P, target in binary_examples:
        assert corrected_type_i(source1, source2, t) == (P, target)
        assert target in type_i_rows[P]

    # Streaming replay of every step in the exact inverse (26.17).  It
    # enumerates n_i and a_i, then every c_i allowed by the source residue and
    # strict-descent bounds, and finally reconstructs the positive integer t.
    # It returns on the first branch for a target and never collects branches.
    def source_c_values(a0, b0, m0, target_P):
        coefficient = 4 * a0 * b0
        if gcd(coefficient, m0) != 1:
            return
        residue = pow(coefficient, -1, m0)
        first = residue if residue else m0
        for c0 in range(first, m0 * target_P // coefficient + 1, m0):
            numerator = coefficient * c0 - 1
            if numerator % m0:
                continue
            source_P = numerator // m0
            if 2 <= source_P < target_P:
                yield c0, source_P

    def binary_singleton_inverse(P, row):
        A, B, C, K = row
        total = A + B
        m = total // K
        if K % m:
            return None
        for singleton_index, singleton in enumerate((A, B)):
            for n1 in cached_divisors(total):
                n2 = total // n1
                if n1 % m or n2 % m:
                    continue
                k1, k2 = n1 // m, n2 // m
                for a1 in cached_divisors(singleton):
                    a2 = singleton // a1
                    if not (1 <= a1 < n1 and 1 <= a2 < n2):
                        continue
                    b1, b2 = n1 - a1, n2 - a2
                    for c1, p1 in source_c_values(a1, b1, m, P):
                        for c2, p2 in source_c_values(a2, b2, m, P):
                            if (C + 4 * c1 * c2) % m:
                                continue
                            t = (C + 4 * c1 * c2) // m
                            assert t >= 1
                            assert K == k1 * k2 * m
                            constructed = (singleton, total - singleton, C, K)
                            expected = row if singleton_index == 0 else (B, A, C, K)
                            assert constructed == expected
                            assert C == m * t - 4 * c1 * c2
                            assert_type_i(p1, (a1, b1, c1, k1))
                            assert_type_i(p2, (a2, b2, c2, k2))
                            assert_type_i(P, constructed)
                            return ((p1, (a1, b1, c1, k1)),
                                    (p2, (a2, b2, c2, k2)), t)
        return None

    m_divides_k = {
        P for P, rows in type_i_rows.items()
        if any(row[3] % ((row[0] + row[1]) // row[3]) == 0 for row in rows)
    }
    binary_inverse_branches = {}
    for P, rows in type_i_rows.items():
        branch = next((branch for row in rows
                       if (branch := binary_singleton_inverse(P, row))
                       is not None), None)
        if branch is not None:
            binary_inverse_branches[P] = branch
    binary_inverse_targets = set(binary_inverse_branches)
    assert m_divides_k == {1129, 2473, 3169, 5281}
    assert binary_inverse_targets == {2473, 3169, 5281}
    assert not (binary_inverse_targets & {73, 193, 241, 1129, 2521})

    def type_ii_value(row):
        a0, b0, c0, k0 = row
        assert min(row) >= 1 and (a0 + b0) % k0 == 0
        return 4 * a0 * b0 * c0 - (a0 + b0) // k0

    def assert_type_ii(P, row):
        a0, b0, c0, k0 = row
        assert type_ii_value(row) == P >= 2
        denominators = (a0 * b0 * c0,
                        P * a0 * c0 * k0, P * b0 * c0 * k0)
        assert sum(Fraction(1, d) for d in denominators) == Fraction(4, P)

    def all_type_ii_rows(P):
        """Complete (22.20) enumeration."""
        rows = []
        for A in range(1, P // 2 + 1):
            for B in range(1, P // (2 * A) + 1):
                for K in cached_divisors(A + B):
                    numerator = K * P + A + B
                    denominator = 4 * A * B * K
                    if numerator % denominator == 0:
                        rows.append((A, B, numerator // denominator, K))
        return tuple(rows)

    cross_expected = {
        673: (97, (1, 34, 5, 5)),
        1153: (385, (1, 17, 17, 6)),
        3361: (1121, (1, 29, 29, 10)),
        5281: (481, (1, 21, 63, 2)),
    }
    cross_targets = set()
    for Q in resisters:
        for row in all_type_ii_rows(Q):
            assert_type_ii(Q, row)
            m = (row[0] + row[1]) // row[3]
            if m > 1 and (Q - 1) % m == 0:
                source_p = 1 + (Q - 1) // m
                assert 2 <= source_p < Q
                assert_type_i(source_p, row)
                assert Q == m * (source_p - 1) + 1
                cross_targets.add(Q)
        if Q in cross_expected:
            source_p, row = cross_expected[Q]
            assert row in all_type_ii_rows(Q)
            assert_type_i(source_p, row)
            assert_type_ii(Q, row)
    assert cross_targets == set(cross_expected)

    # Block (v) independently replays §23's exhaustive base census and leaves
    # exactly these eleven.  Recompute the 143-prime universe here rather than
    # using 132 and 143 only as inherited arithmetic constants.
    hard_primes = tuple(P for P in primerange(2, 10_001) if P % 24 == 1)
    assert len(hard_primes) == 143 and set(resisters) < set(hard_primes)
    base_reached = len(hard_primes) - len(resisters)
    assert base_reached == 132
    newly_reached = binary_inverse_targets | cross_targets
    combined_blocked = set(resisters) - newly_reached
    assert newly_reached == {673, 1153, 2473, 3169, 3361, 5281}
    assert combined_blocked == {73, 193, 241, 1129, 2521}
    assert base_reached + len(newly_reached) == 138

    print("Type-I exact tuple counts (11 resisters):",
          dict(zip(resisters, expected_counts)))
    print("corrected Type-I tensor reaches", sorted(binary_inverse_targets),
          "; cross-type bridge reaches", sorted(cross_targets))
    print("combined hard-prime reachability <= 10^4: 138/143; blocked =",
          sorted(combined_blocked))


print("\n== (y) Type-I transfer theory (§26) ==")
check_y()

# ---------------------------------------------------------------- (z)
def check_z():
    """Finite companions and reproducibility checks for the §27 audit."""
    import csv
    import hashlib
    import os
    from pathlib import Path
    import shlex
    import subprocess
    import tempfile
    import numpy as np

    def fiber_shifts(Y0):
        shifts0 = []
        for R0 in range(1, Y0 + 1):
            squarefree0 = [1]
            for p0 in factorint(R0):
                squarefree0 += [s0 * p0 for s0 in squarefree0]
            shifts0.extend((R0, R0 * R0 // s0) for s0 in squarefree0)
        return shifts0

    # Exact conditioned-event classification from (27.5).  The full X=27
    # period is small enough to enumerate.  Small conditioned 3 mod 4 prime
    # factors make four of the fourteen remaining atoms impossible.
    X0, Y0 = 27, 2
    low_shifts = fiber_shifts(Y0)
    H0 = len(low_shifts)
    conditioned_primes = tuple(
        p0 for p0 in primerange(3, X0 + 1) if p0 % 4 == 3
    )
    allowed = {}
    for p0 in conditioned_primes:
        bad0 = {(-4 * D0) % p0 for R0, D0 in low_shifts if R0 % p0}
        allowed[p0] = ({0} if p0 <= 2 * H0
                       else set(range(p0)) - bad0)

    period0 = lcm(*range(3, X0 + 1, 4))
    ns0 = np.arange(period0, dtype=np.int64)
    certificate = np.ones(period0, dtype=bool)
    for p0 in conditioned_primes:
        certificate &= np.isin(ns0 % p0, tuple(allowed[p0]))
    certificate_count = int(certificate.sum())
    assert (period0, certificate_count) == (4_542_615, 460_800)

    no_remaining_hit = np.ones(period0, dtype=bool)
    atom_count = impossible_count = 0
    for R0 in range(Y0 + 1, (X0 + 1) // 4 + 1):
        for RR0, D0 in fiber_shifts(R0):
            if RR0 != R0:
                continue
            for M0 in range(4 * R0 - 1, X0 + 1, 4 * R0):
                atom_count += 1
                event = ns0 % M0 == (-4 * D0) % M0
                exact_count = int(np.count_nonzero(certificate & event))
                predicted = Fraction(1, 1)
                for p0, a0 in factorint(M0).items():
                    if p0 % 4 == 1:
                        predicted *= Fraction(1, p0**a0)
                    else:
                        residue0 = (-4 * D0) % p0
                        if residue0 not in allowed[p0]:
                            predicted = Fraction(0, 1)
                            break
                        predicted *= Fraction(
                            1, p0**(a0 - 1) * len(allowed[p0])
                        )
                assert Fraction(exact_count, certificate_count) == predicted
                impossible_count += predicted == 0
                no_remaining_hit &= ~event
    conditional_void = Fraction(
        int(np.count_nonzero(certificate & no_remaining_hit)),
        certificate_count,
    )
    assert (atom_count, impossible_count, conditional_void) == (
        14, 4, Fraction(147, 320)
    )

    # Construction-consistency smoke test for Theorem 27.1's hybrid.  It
    # checks indexing and threshold logic, not the Euler-product, Bonferroni,
    # Q_0, or finite-rounding estimates in the proof.
    X1, Y1 = 300, 8
    shifts1 = fiber_shifts(Y1)
    H1 = len(shifts1)
    local_sets = {}
    for p1 in primerange(3, X1 + 1):
        if p1 % 4 != 3 or p1 <= 4 * H1:
            continue
        low_bad1 = {(-4 * D1) % p1 for R1, D1 in shifts1 if R1 % p1}
        A1 = (p1 + 1) // 4
        prime_bad1 = {(-4 * d1) % p1 for d1 in divisors_of_square(A1)}
        G1 = low_bad1 | prime_bad1
        assert 0 not in G1 and len(G1) < 3 * p1 / 4
        local_sets[p1] = G1

    low_event_checks = 0
    for R1, D1 in shifts1:
        for M1 in range(4 * R1 - 1, X1 + 1, 4 * R1):
            certifying = next(
                p1 for p1, a1 in factorint(M1).items()
                if p1 % 4 == 3 and a1 % 2 == 1
            )
            assert gcd(M1, R1) == gcd(M1, D1) == 1
            if certifying > 4 * H1:
                assert (-4 * D1) % certifying in local_sets[certifying]
            else:
                assert (-4 * D1) % certifying != 0
            low_event_checks += 1
    prime_class_checks = 0
    for p1 in primerange(3, X1 + 1):
        if p1 % 4 != 3:
            continue
        for d1 in divisors_of_square((p1 + 1) // 4):
            if p1 > 4 * H1:
                assert (-4 * d1) % p1 in local_sets[p1]
            else:
                assert (-4 * d1) % p1 != 0
            prime_class_checks += 1

    # Primorial quarantine: a modulus sharing any pinned prime cannot hit,
    # because M == -1 (mod R) makes that prime coprime to D.
    quarantine_checks = 0
    for R1 in range(1, (X1 + 1) // 4 + 1):
        for RR1, D1 in fiber_shifts(R1):
            if RR1 != R1:
                continue
            for M1 in range(4 * R1 - 1, X1 + 1, 4 * R1):
                for p1 in factorint(M1):
                    if p1 <= 11:
                        assert D1 % p1 != 0 and (-4 * D1) % p1 != 0
                        quarantine_checks += 1

    # Reproducible sample provenance.  The default run compiles the checked-in
    # sampler, executes its direct-divisor-oracle self-test, hashes and parses
    # all 240 checked-in chunk rows, and derives the table totals.  The costly
    # (about six seconds on the recorded host) regeneration is opt-in.
    root = Path(__file__).resolve().parent
    sampler_source = root / "scripts" / "sample_avoidance.cpp"
    sample_data = root / "data" / "avoidance-sample-x6400.tsv"
    assert hashlib.sha256(sampler_source.read_bytes()).hexdigest() == (
        "90f4a8833595865040ddb2bfd2c343daf0c3cd68afa39ecbf8a536b531a74094"
    )
    assert hashlib.sha256(sample_data.read_bytes()).hexdigest() == (
        "1a0428e5d0e28043d172530498ac90c6e80625c3fd8b2a6ac788a89e19c7c896"
    )

    def read_sample_rows(path):
        with path.open(newline="") as handle:
            data_lines = [line for line in handle if not line.startswith("#")]
        return list(csv.DictReader(data_lines, delimiter="\t"))

    sample_rows = read_sample_rows(sample_data)
    survivor_fields = tuple(f"survive_{x}" for x in
                            (50, 100, 200, 400, 800, 1600, 3200, 6400))
    assert len(sample_rows) == 240
    assert {(int(row["stream"]), int(row["chunk"])) for row in sample_rows} == {
        (stream, chunk) for stream in range(24) for chunk in range(10)
    }
    mask64 = (1 << 64) - 1
    for row in sample_rows:
        stream, chunk = int(row["stream"]), int(row["chunk"])
        assert int(row["seed"]) == (
            27_006_400 + 0x9e3779b97f4a7c15 * stream
        ) & mask64
        assert int(row["start"]) == chunk * 10_000_000
        assert int(row["draws"]) == 10_000_000
        assert all(0 <= int(row[field]) <= 10_000_000
                   for field in survivor_fields)
        assert 0 <= int(row["sample_sum_mod_2^64"]) <= mask64
        assert 0 <= int(row["sample_mix_xor"]) <= mask64

    sample_count = sum(int(row["draws"]) for row in sample_rows)
    raw_survivors = np.array([
        sum(int(row[field]) for row in sample_rows)
        for field in survivor_fields
    ], dtype=np.int64)
    expected_survivors = np.array([
        126_504_179, 42_472_324, 10_805_883, 2_315_665,
        362_699, 42_008, 3_854, 274,
    ], dtype=np.int64)
    assert sample_count == 2_400_000_000
    assert np.array_equal(raw_survivors, expected_survivors)

    with tempfile.TemporaryDirectory(prefix="es-sampler-") as build_dir:
        executable = Path(build_dir) / "sample_avoidance"
        compile_command = (shlex.split(os.environ.get("CXX", "g++")) + [
            "-O3", "-DNDEBUG", "-std=c++20", "-pthread",
            "-o", str(executable), str(sampler_source),
        ])
        subprocess.run(compile_command, check=True, capture_output=True, text=True)
        self_test = subprocess.run(
            [str(executable), "--self-test"], check=True,
            capture_output=True, text=True,
        )
        assert "match direct oracle" in self_test.stdout
        if os.environ.get("ES_BIG_SAMPLE") == "1":
            regenerated = Path(build_dir) / "regenerated.tsv"
            subprocess.run(
                [str(executable), "--output", str(regenerated)],
                check=True,
            )
            assert read_sample_rows(regenerated) == sample_rows
            print("ES_BIG_SAMPLE=1: all 2.4 billion draws and 240 chunks "
                  "match the checked-in raw data")
        else:
            print("Set ES_BIG_SAMPLE=1 to regenerate all 2.4 billion sample draws")

    fit_X = np.array([50, 100, 200, 400, 800, 1600, 3200, 6400.])
    fit_survivors = raw_survivors.astype(float)
    fit_y = -np.log(fit_survivors / sample_count)
    fit_L = np.log(fit_X)

    def affine_rmse_z(regressor):
        design = np.column_stack((np.ones(regressor.size), regressor))
        coefficients = np.linalg.lstsq(design, fit_y, rcond=None)[0]
        return float(np.sqrt(np.mean((fit_y - design @ coefficients)**2)))

    regressors = (
        fit_L * np.log(fit_L), fit_L**1.5, fit_L**2,
        fit_L**2 * np.log(fit_L), fit_L**(2 + log(2)), fit_L**3,
    )
    rmses = tuple(affine_rmse_z(regressor) for regressor in regressors)
    expected_rmses = (0.43396, 0.36647, 0.13702, 0.05667, 0.16856, 0.29564)
    assert all(abs(got - wanted) < 2e-5
               for got, wanted in zip(rmses, expected_rmses))
    correlation = float(np.corrcoef(regressors[3], regressors[4])[0, 1])
    assert abs(correlation - 0.999651) < 2e-6

    # Wilson arithmetic for the new row and the exact raw-mass shell.
    z95 = 1.959963984540054
    phat = fit_survivors[-1] / sample_count
    denominator = 1 + z95**2 / sample_count
    center = (phat + z95**2 / (2 * sample_count)) / denominator
    half_width = z95 * np.sqrt(
        phat * (1 - phat) / sample_count
        + z95**2 / (4 * sample_count**2)
    ) / denominator
    assert abs((center - half_width) - 1.0142531e-7) < 1e-14
    assert abs((center + half_width) - 1.2850863e-7) < 1e-14

    intrinsic_mass = 0.0
    mass_3200 = None
    for M1 in range(3, 6401, 4):
        A1 = (M1 + 1) // 4
        intrinsic_mass += len({(-4 * d1) % M1
                               for d1 in divisors_of_square(A1)}) / M1
        if M1 == 3199:
            mass_3200 = intrinsic_mass
    assert abs(mass_3200 - 18.5283467617) < 1e-9
    assert abs(intrinsic_mass - 23.1850498655) < 1e-9

    toy_T = log(X0)**log(2)
    toy_weight = 0.0
    for R0 in range(Y0 + 1, (X0 + 1) // 4 + 1):
        phi0 = 4 * R0
        for p0 in factorint(4 * R0):
            phi0 = phi0 // p0 * (p0 - 1)
        toy_weight += 2**len(factorint(R0)) * min(1.0, toy_T / phi0)
    toy_ratio = -log(float(conditional_void)) / toy_weight
    assert abs(toy_ratio - 0.20419) < 2e-5

    print("conditioned X=27,Y=2: 14 atoms, 4 impossible, "
          "conditional void=147/320; (27.5) exact")
    print("Theorem 27.1 construction smoke test: %d low events and %d prime "
          "classes; primorial exclusions=%d" %
          (low_event_checks, prime_class_checks, quarantine_checks))
    print("§27 raw-data and table-arithmetic replay: X=6400 has "
          "274/2.4e9 survivors, Wilson [1.01425e-7,1.28509e-7]")
    print("§27 fits (L^2logL, subset RMSE, correlation): "
          "%.5f, %.5f, %.6f" % (rmses[3], rmses[4], correlation))


print("\n== (z) large-R conditioning and H_DC (§27) ==")
check_z()

# ---------------------------------------------------------------- (aa)
def check_aa():
    """Section 28: reconciled census, tuple atoms, and image conditions."""
    import os
    import random
    from functools import lru_cache
    from math import isqrt
    from sympy import divisors

    @lru_cache(None)
    def divs(n):
        return tuple(divisors(n))

    def type_ii_value(row):
        a, b, c, k = row
        assert min(row) >= 1 and (a + b) % k == 0
        return 4 * a * b * c - (a + b) // k

    def assert_type_ii(P, row):
        a, b, c, k = row
        assert type_ii_value(row) == P >= 2
        denominators = (a * b * c, P * a * c * k, P * b * c * k)
        assert sum(Fraction(1, d) for d in denominators) == Fraction(4, P)

    def row_at(P, A, B):
        if 2 * A * B > P:
            return None
        C = P // (4 * A * B) + 1
        q = 4 * A * B * C - P
        if (A + B) % q:
            return None
        return A, B, C, (A + B) // q

    def all_type_ii_rows(P):
        rows = []
        for A in range(1, isqrt(P // 2) + 1):
            for B in range(A, P // (2 * A) + 1):
                row = row_at(P, A, B)
                if row is None:
                    continue
                rows.append(row)
                if A != B:
                    rows.append((B, A, row[2], row[3]))
        return tuple(sorted(rows))

    # Reconcile the five rows omitted from §26.5.  Sources, target, descent,
    # fixed coordinate map, and all rational identities are checked directly.
    reconciliation = (
        (73, (2, 5, 2, 1), "++", (6, (1, 1, 2, 1)),
         (27, (1, 4, 2, 1))),
        (193, (2, 5, 5, 1), "++", (18, (1, 1, 5, 1)),
         (75, (1, 4, 5, 1))),
        (241, (1, 22, 3, 1), "1+", (10, (1, 1, 3, 1)),
         (230, (1, 21, 3, 1))),
        (1129, (2, 13, 11, 1), "++", (42, (1, 1, 11, 1)),
         (515, (1, 12, 11, 1))),
        (2521, (2, 29, 11, 1), "++", (42, (1, 1, 11, 1)),
         (1203, (1, 28, 11, 1))),
    )
    for P, target, map_name, source1, source2 in reconciliation:
        p1, row1 = source1
        p2, row2 = source2
        assert_type_ii(p1, row1)
        assert_type_ii(p2, row2)
        assert 2 <= p1 < P and 2 <= p2 < P
        assert 4 * row1[2] * row1[3] == 4 * target[2] * target[3]
        assert 4 * row2[2] * row2[3] == 4 * target[2] * target[3]
        if map_name == "++":
            output = (row1[0] + row2[0], row1[1] + row2[1],
                      target[2], target[3])
        else:
            output = (row1[0], row1[1] + row2[1],
                      target[2], target[3])
        assert output == target
        assert_type_ii(P, output)

    eleven_k1 = {
        73: (2, 5, 2, 1), 193: (2, 5, 5, 1),
        241: (1, 22, 3, 1), 673: (2, 5, 17, 1),
        1129: (2, 13, 11, 1), 1153: (2, 5, 29, 1),
        2473: (2, 5, 62, 1), 2521: (2, 29, 11, 1),
        3169: (2, 21, 19, 1), 3361: (5, 34, 5, 1),
        5281: (6, 17, 13, 1),
    }
    for P, row in eleven_k1.items():
        assert_type_ii(P, row)
        assert row in all_type_ii_rows(P)
    old_26_blocked = {73, 193, 241, 1129, 2521}
    assert old_26_blocked < set(eleven_k1)
    assert old_26_blocked - {P for P, *_ in reconciliation} == set()

    # Exact inverse of all three fixed additive maps at R=CK.  Monotonicity
    # in the ignored coordinate makes the least positive residue complete.
    def fixed_additive_inverse(P, row):
        A, B, C, K = row
        R = C * K
        if A >= 2 and B >= 2:
            for a1 in range(1, A):
                a2 = A - a1
                for b1 in range(1, B):
                    b2 = B - b1
                    for k1 in divs(gcd(R, a1 + b1)):
                        row1 = (a1, b1, R // k1, k1)
                        p1 = type_ii_value(row1)
                        if not 2 <= p1 < P:
                            continue
                        for k2 in divs(gcd(R, a2 + b2)):
                            row2 = (a2, b2, R // k2, k2)
                            p2 = type_ii_value(row2)
                            if 2 <= p2 < P:
                                return "++", (p1, row1), (p2, row2)
        if B >= 2:
            for b1 in range(1, B):
                b2 = B - b1
                for k1 in divs(gcd(R, A + b1)):
                    row1 = (A, b1, R // k1, k1)
                    p1 = type_ii_value(row1)
                    if not 2 <= p1 < P:
                        continue
                    for k2 in divs(R):
                        a2 = (-b2) % k2 or k2
                        row2 = (a2, b2, R // k2, k2)
                        p2 = type_ii_value(row2)
                        if 2 <= p2 < P:
                            return "1+", (p1, row1), (p2, row2)
        if A >= 2:
            for a1 in range(1, A):
                a2 = A - a1
                for k1 in divs(gcd(R, a1 + B)):
                    row1 = (a1, B, R // k1, k1)
                    p1 = type_ii_value(row1)
                    if not 2 <= p1 < P:
                        continue
                    for k2 in divs(R):
                        b2 = (-a2) % k2 or k2
                        row2 = (a2, b2, R // k2, k2)
                        p2 = type_ii_value(row2)
                        if 2 <= p2 < P:
                            return "+1", (p1, row1), (p2, row2)
        return None

    def assert_additive_branch(P, target, branch):
        map_name, source1, source2 = branch
        p1, row1 = source1
        p2, row2 = source2
        assert_type_ii(p1, row1)
        assert_type_ii(p2, row2)
        assert 2 <= p1 < P and 2 <= p2 < P
        if map_name == "++":
            output = (row1[0] + row2[0], row1[1] + row2[1],
                      target[2], target[3])
        elif map_name == "1+":
            output = (row1[0], row1[1] + row2[1],
                      target[2], target[3])
        else:
            output = (row1[0] + row2[0], row1[1],
                      target[2], target[3])
        assert output == target and type_ii_value(output) == P
        return True

    # Theorem 28.3, including interval existence and both descent inequalities,
    # is replayed on every applicable small target row.
    def interior_additive(P, row):
        A, B, C, K = row
        m = (A + B) // K
        if A < 2 or B < 2 or m < 2:
            return None
        if K == 1:
            row1, row2 = (1, 1, C, 1), (A - 1, B - 1, C, 1)
        else:
            lower = max(1, K - B + 1)
            upper = min(A - 1, K - 1)
            assert lower <= upper
            delta, delta2 = lower, K - lower
            row1 = (delta, delta2, C, K)
            row2 = (A - delta, B - delta2, C, K)
        p1, p2 = type_ii_value(row1), type_ii_value(row2)
        assert 2 <= p1 < P and 2 <= p2 < P
        assert (row1[0] + row2[0], row1[1] + row2[1], C, K) == row
        return (p1, row1), (p2, row2)

    def flexible_inverse(P, row):
        A, B, C, K = row
        if C * K % 4:
            return None
        tensor_product = C * K // 4
        for kappa in divs(tensor_product):
            if (A + B) % kappa:
                continue
            gamma = tensor_product // kappa
            s_product = (A + B) // kappa
            for k1 in divs(kappa):
                k2 = kappa // k1
                for c1 in divs(gamma):
                    c2 = gamma // c1
                    for s1 in divs(s_product):
                        s2 = s_product // s1
                        n1, n2 = k1 * s1, k2 * s2
                        for a1 in range(1, n1):
                            b1 = n1 - a1
                            p1 = type_ii_value((a1, b1, c1, k1))
                            if not 2 <= p1 < P:
                                continue
                            for a2 in range(1, n2):
                                b2 = n2 - a2
                                p2 = type_ii_value((a2, b2, c2, k2))
                                if not 2 <= p2 < P:
                                    continue
                                terms = (a1 * a2, a1 * b2,
                                         b1 * a2, b1 * b2)
                                for mask in range(1, 15):
                                    left = sum(terms[i] for i in range(4)
                                               if mask >> i & 1)
                                    if left == A and sum(terms) - left == B:
                                        return True
        return None

    # Fast complete inverse for branches having fixed source (1,1,1,1).
    # The tensor subset is determined, up to irrelevant duplicate masks, by
    # how many copies of the second source's two coordinates it selects.
    tensor_masks_by_counts = {}
    for mask in range(1, 15):
        counts = (sum(bool(mask >> i & 1) for i in (0, 2)),
                  sum(bool(mask >> i & 1) for i in (1, 3)))
        tensor_masks_by_counts.setdefault(counts, mask)

    def fixed_two_inverse(P, row):
        A, B, C, K = row
        if C * K % 4 or (A + B) % 2:
            return None
        tensor_product = C * K // 4
        half_sum = (A + B) // 2
        for k2 in divs(gcd(tensor_product, half_sum)):
            c2, s2 = tensor_product // k2, half_sum // k2
            for (i, j), mask in tensor_masks_by_counts.items():
                if i == j:
                    if i != 1 or A != half_sum:
                        continue
                    candidates = range(1, half_sum)
                else:
                    numerator = A - j * half_sum
                    denominator = i - j
                    if numerator % denominator:
                        continue
                    candidates = (numerator // denominator,)
                for a2 in candidates:
                    if not 1 <= a2 < half_sum:
                        continue
                    b2 = half_sum - a2
                    source = (a2, b2, c2, k2)
                    p2 = type_ii_value(source)
                    if 2 <= p2 < P:
                        return row, (2, (1, 1, 1, 1)), (p2, source), mask, s2
        return None

    def bridge_inverse(P, row):
        m = (row[0] + row[1]) // row[3]
        if m > 1 and (P - 1) % m == 0:
            source = 1 + (P - 1) // m
            assert 2 <= source < P
            return True
        return None

    def decomposes_type_ii(P, row):
        additive = fixed_additive_inverse(P, row)
        if additive is not None:
            assert_additive_branch(P, row, additive)
            return True
        return bool(bridge_inverse(P, row) or flexible_inverse(P, row))

    hard_3k = tuple(P for P in primerange(2, 3001) if P % 24 == 1)
    atoms = []
    tuple_count = 0
    for P in hard_3k:
        rows = all_type_ii_rows(P)
        assert rows
        assert any(decomposes_type_ii(P, row) for row in rows)
        for row in rows:
            tuple_count += 1
            if row[0] >= 2 and row[1] >= 2 and (row[0] + row[1]) // row[3] >= 2:
                assert interior_additive(P, row)
            if not decomposes_type_ii(P, row):
                atoms.append((P, row, (row[0] + row[1]) // row[3]))
    assert len(hard_3k) == 46 and tuple_count == 940
    expected_atoms_up_to_swap = (
        (241, (1, 62, 1, 9), 7), (409, (1, 104, 1, 15), 7),
        (577, (1, 146, 1, 21), 7), (601, (1, 153, 1, 14), 11),
        (937, (1, 118, 2, 17), 7), (1129, (1, 285, 1, 26), 11),
        (1249, (1, 314, 1, 45), 7), (1609, (1, 202, 2, 29), 7),
        (1657, (1, 417, 1, 38), 11), (1753, (1, 440, 1, 63), 7),
        (2089, (1, 524, 1, 75), 7), (2089, (1, 528, 1, 23), 23),
        (2281, (1, 286, 2, 41), 7), (2593, (1, 650, 1, 93), 7),
        (2617, (1, 328, 2, 47), 7), (2713, (1, 681, 1, 62), 11),
        (2953, (1, 370, 2, 53), 7),
    )
    normalized_atoms = sorted(
        (P, row if row[0] <= row[1] else (row[1], row[0], row[2], row[3]), m)
        for P, row, m in atoms
    )
    assert len(atoms) == 34 and len({P for P, row, m in atoms}) == 16
    assert sorted(set(normalized_atoms)) == sorted(expected_atoms_up_to_swap)
    assert all(min(row[:2]) == 1 and row[3] > 1 and row[2] * row[3] % 4
               and (P - 1) % m for P, row, m in atoms)

    # Reconcile §28's restricted-family atoms with §30's larger move system.
    # Each row has an immediate descending X^-1 or Y^-1 predecessor, and the
    # canonical §30 reverse path (relabel to K=1, then X/Y/Z subtraction)
    # reaches the sole global seed.  Relabelling may first raise the value.
    section30_predecessor_counts = {"X": 0, "Y": 0}
    for P, row, unused_m in atoms:
        A, B, C, K = row
        if A > K:
            predecessor = (A - K, B, C, K)
            section30_predecessor_counts["X"] += 1
        else:
            assert B > K
            predecessor = (A, B - K, C, K)
            section30_predecessor_counts["Y"] += 1
        assert 2 <= type_ii_value(predecessor) < P

        current = (A, B, C * K, 1)
        assert type_ii_value(current) == K * P
        while current[0] > 1:
            current = (current[0] - 1, current[1], current[2], 1)
        while current[1] > 1:
            current = (current[0], current[1] - 1, current[2], 1)
        while current[2] > 1:
            current = (current[0], current[1], current[2] - 1, 1)
        assert current == (1, 1, 1, 1)
    assert section30_predecessor_counts == {"X": 17, "Y": 17}

    # Deterministic sample beyond 3000: every tuple, not merely one per prime.
    sample_pool = [P for P in primerange(3001, 100_000) if P % 24 == 1]
    sample = tuple(sorted(random.Random(2809).sample(sample_pool, 30)))
    expected_sample = (
        4513, 6961, 7297, 12241, 14737, 15073, 17881, 20641,
        21601, 21673, 25609, 25801, 30937, 45697, 47569, 48049,
        48121, 48673, 48817, 51001, 61129, 61681, 62761, 63337,
        63697, 65257, 67057, 71569, 81649, 93601,
    )
    assert sample == expected_sample
    sample_atoms = []
    sample_tuple_count = 0
    for P in sample:
        prime_has_branch = False
        for row in all_type_ii_rows(P):
            sample_tuple_count += 1
            if decomposes_type_ii(P, row):
                prime_has_branch = True
            else:
                m = (row[0] + row[1]) // row[3]
                sample_atoms.append((P, row, m))
        assert prime_has_branch
    assert sample_tuple_count == 1952 and len(sample_atoms) == 58
    assert len({P for P, row, m in sample_atoms}) == 18
    assert all(min(row[:2]) == 1 and row[2] * row[3] % 4
               and (P - 1) % m for P, row, m in sample_atoms)

    # If “all tuples” includes Type I, the corrected law is very far from
    # complete.  This is a separate target domain from the Type-II atom scan.
    def type_i_value(row):
        a, b, c, k = row
        assert min(row) >= 1 and (a + b) % k == 0
        m = (a + b) // k
        numerator = 4 * a * b * c - 1
        assert numerator % m == 0
        return numerator // m

    def all_type_i_rows(P):
        rows = []
        for k in range(1, 2 * P // 3 + 1):
            for c in range(1, (2 * P + k) // (4 * k) + 1):
                if gcd(P, c * k) != 1:
                    continue
                h = 4 * c * k
                norm = P * P + 4 * c * k * k
                for D in divs(norm):
                    if (D + P) % h:
                        continue
                    E = norm // D
                    if (E + P) % h:
                        continue
                    row = ((D + P) // h, (E + P) // h, c, k)
                    assert type_i_value(row) == P
                    rows.append(row)
        return tuple(rows)

    def least_type_i_source(a, b, m, P):
        coefficient = 4 * a * b
        if gcd(coefficient, m) != 1:
            return None
        c = pow(coefficient, -1, m) or m
        source = (coefficient * c - 1) // m
        if source < 2:
            c += m
            source += coefficient
        return (c, source) if source < P else None

    def corrected_type_i_inverse(P, row):
        A, B, C, K = row
        m = (A + B) // K
        if K % m:
            return None
        total = A + B
        for singleton in (A, B):
            for n1 in divs(total):
                n2 = total // n1
                if n1 % m or n2 % m:
                    continue
                k1, k2 = n1 // m, n2 // m
                for a1 in divs(singleton):
                    a2 = singleton // a1
                    if not (1 <= a1 < n1 and 1 <= a2 < n2):
                        continue
                    b1, b2 = n1 - a1, n2 - a2
                    source1 = least_type_i_source(a1, b1, m, P)
                    source2 = least_type_i_source(a2, b2, m, P)
                    if source1 is None or source2 is None:
                        continue
                    c1, p1 = source1
                    c2, p2 = source2
                    if (C + 4 * c1 * c2) % m:
                        continue
                    assert 2 <= p1 < P and 2 <= p2 < P
                    return True
        return None

    type_i_count = type_i_gate_count = type_i_image_count = 0
    for P in hard_3k:
        for row in all_type_i_rows(P):
            type_i_count += 1
            m = (row[0] + row[1]) // row[3]
            type_i_gate_count += row[3] % m == 0
            type_i_image_count += bool(corrected_type_i_inverse(P, row))
    assert (type_i_count, type_i_gate_count, type_i_image_count) == (1830, 44, 40)

    # Exact k=1 test: B | P+A, cofactor == -1 (mod 4A), A<=sqrt(P/2).
    def k1_witness(P, require_interior=False):
        for A in range(1, isqrt(P // 2) + 1):
            for B in divs(P + A):
                if B < A:
                    continue
                D = (P + A) // B
                if (D + 1) % (4 * A):
                    continue
                C = (D + 1) // (4 * A)
                row = (A, B, C, 1)
                if type_ii_value(row) != P:
                    continue
                if not require_interior or A >= 2:
                    return row
        return None

    hard_100k = tuple(P for P in primerange(2, 100_000) if P % 24 == 1)
    no_k1_100k = [P for P in hard_100k if k1_witness(P) is None]
    assert len(hard_100k) == 1181
    assert no_k1_100k == [409, 577, 5569, 9601, 23929, 83449]
    k1_image = {P for P in hard_100k if k1_witness(P) is not None}
    k1_interior_count = sum(k1_witness(P, require_interior=True) is not None
                            for P in hard_100k)
    assert len(k1_image) == 1175 and k1_interior_count == 1165

    # Recompute, rather than pin, both tensor image rows in (28.10).  The fast
    # fixed-source inverse handles 1166 primes.  Only its residual is passed
    # to the complete flexible inverse, keeping the default audit inexpensive.
    fixed_source2_image = set()
    flexible_tensor_image = set()
    for P in hard_100k:
        rows = all_type_ii_rows(P)
        if any(fixed_two_inverse(P, row) is not None for row in rows):
            fixed_source2_image.add(P)
            flexible_tensor_image.add(P)
        elif any(flexible_inverse(P, row) for row in rows):
            flexible_tensor_image.add(P)
    assert len(fixed_source2_image) == 1166
    assert len(flexible_tensor_image) == 1170
    hard_10k = {P for P in hard_100k if P <= 10_000}
    assert len(hard_10k) == 143
    assert len(flexible_tensor_image & hard_10k) == 132
    assert hard_10k - flexible_tensor_image == set(eleven_k1)

    decade_rows = []
    for lower, upper, expected in (
            (10, 100, (2, 0)), (100, 1000, (12, 2)),
            (1000, 10_000, (129, 2)), (10_000, 100_000, (1038, 2))):
        decade_primes = [P for P in hard_100k if lower <= P < upper]
        decade_rows.append((lower, len(decade_primes),
                            sum(P in no_k1_100k for P in decade_primes)))
        assert (len(decade_primes), decade_rows[-1][2]) == expected

    if os.environ.get("ES_FULL_SCAN") == "1":
        hard_1m = tuple(P for P in primerange(2, 1_000_001) if P % 24 == 1)
        no_k1_1m = [P for P in hard_1m if k1_witness(P) is None]
        assert len(hard_1m) == 9732
        assert no_k1_1m == [409, 577, 5569, 9601, 23929, 83449,
                            102001, 329617, 712321]
        last_decade = [P for P in hard_1m if 100_000 <= P < 1_000_000]
        assert (len(last_decade), sum(P in no_k1_1m for P in last_decade)) == (
            8551, 3)
        decade_rows.append((100_000, 8551, 3))
        print("ES_FULL_SCAN=1: k=1-less hard primes through 10^6 =",
              no_k1_1m)
    else:
        print("ES_FULL_SCAN=1 extends the exact k=1-less census through 10^6")

    # Fast P-only bridge predicate: m | P-1 and ABC=(P+m)/4.
    def bridge_image(P):
        for m in divs(P - 1):
            if m <= 1 or (P + m) % 4:
                continue
            N = (P + m) // 4
            for A in divs(N):
                for B in divs(N // A):
                    if (A + B) % m == 0:
                        C, K = N // (A * B), (A + B) // m
                        assert type_ii_value((A, B, C, K)) == P
                        return True
        return False

    bridge_count = sum(bridge_image(P) for P in hard_100k)
    assert bridge_count == 771

    # Complete corrected-Type-I gate/image scan.  K=m*l gives A+B=m^2*l;
    # the quadratic bound skips the central A interval where C cannot exist.
    def corrected_type_i_density(X, hard_primes):
        hard_set = set(hard_primes)
        gate, image = set(), set()
        for m in range(3, X // 4 + 2, 4):
            l_max = (X * m + 5) // (4 * m * m)
            for ell in range(1, l_max + 1):
                total = m * m * ell
                N = (X * m + 1) // 4
                if total - 1 > N:
                    break
                discriminant = total * total - 4 * N
                A_max = total // 2
                if discriminant > 0:
                    root = (total - isqrt(discriminant)) // 2
                    while (root + 1) * (total - root - 1) <= N:
                        root += 1
                    while root * (total - root) > N:
                        root -= 1
                    A_max = min(A_max, root)
                for A in range(1, A_max + 1):
                    B = total - A
                    AB = A * B
                    if AB > N or gcd(4 * AB, m) != 1:
                        continue
                    C_max = N // AB
                    C0 = pow(4 * AB, -1, m) or m
                    for C in range(C0, C_max + 1, m):
                        P = (4 * AB * C - 1) // m
                        if P not in hard_set:
                            continue
                        gate.add(P)
                        if P not in image and corrected_type_i_inverse(
                                P, (A, B, C, m * ell)):
                            image.add(P)
        return gate, image

    corrected_gate, corrected_image = corrected_type_i_density(
        100_000, hard_100k)
    assert (len(corrected_gate), len(corrected_image)) == (697, 681)
    assert sorted(corrected_gate - corrected_image) == [
        1129, 6217, 20161, 25801, 26713, 28729, 38977, 49921,
        69481, 70393, 77569, 78553, 82561, 84913, 89689, 97609,
    ]

    # The six k=1 misses all have a broader fixed-additive branch.  Together
    # with the recomputed k=1 image this verifies the fixed-additive table row.
    fixed_additive_image = set(k1_image)
    for P in no_k1_100k:
        branch = next((fixed_additive_inverse(P, row)
                       for row in all_type_ii_rows(P)
                       if fixed_additive_inverse(P, row) is not None), None)
        assert branch is not None
        fixed_additive_image.add(P)
    assert len(fixed_additive_image) == len(hard_100k)
    image_density_counts = {
        "fixed additive": len(fixed_additive_image),
        "k=1 additive": len(k1_image),
        "flexible tensor": len(flexible_tensor_image),
        "fixed source 2": len(fixed_source2_image),
        "k=1 Phi++": k1_interior_count,
        "bridge": bridge_count,
        "Type-I gate": len(corrected_gate),
        "corrected Type-I": len(corrected_image),
    }
    assert image_density_counts == {
        "fixed additive": 1181, "k=1 additive": 1175,
        "flexible tensor": 1170, "fixed source 2": 1166,
        "k=1 Phi++": 1165, "bridge": 771,
        "Type-I gate": 697, "corrected Type-I": 681,
    }

    print("five §26 blockers replayed under the §23 descending standard; "
          "this block recomputes empty combined blocked sets through 10^4 "
          "and below 10^5 (the million-prime row belongs to full block (x))")
    print("Type-II restricted-family census P<=3000: 940 rows, 34 atoms at "
          "16 primes; all 34 have direct descending §30 X/Y predecessors and "
          "reduce to its seed; random beyond sample: 1952 rows, 58 atoms at "
          "18 primes")
    print("k=1-less default census:", no_k1_100k,
          "; decade rows (lower,total,missing) =", decade_rows)
    print("image-condition counts on 1181 hard primes <10^5:",
          image_density_counts)


print("\n== (aa) reconciled transfer census and tuple atoms (§28) ==")
check_aa()

# ---------------------------------------------------------------- (ab)
def check_ab():
    """Finite companions for the transfer-law mass audit in §29."""
    def positive_divisors(n):
        out = [1]
        for prime, exponent in factorint(n).items():
            out = [d * prime**j for d in out
                   for j in range(exponent + 1)]
        return sorted(out)

    # Lemma 29.1: every fixed-(c,k) Case-B prime class is intrinsic,
    # and every intrinsic class has such a description.  Keep both raw and
    # union counts so factorization multiplicity cannot masquerade as mass.
    prime_count = raw_b_count = intrinsic_b_count = overlap_b_count = 0
    for q0 in primerange(3, 3001):
        if q0 % 4 != 3:
            continue
        prime_count += 1
        A0 = (q0 + 1) // 4
        generated = []
        for k0 in positive_divisors(A0):
            for c0 in positive_divisors(A0 // k0):
                a0 = A0 // (c0 * k0)
                residue = (-pow(4 * c0 * k0 * k0, -1, q0)) % q0
                D0 = c0 * a0 * a0
                assert A0 * A0 % D0 == 0
                assert residue == (-a0 * pow(k0, -1, q0)) % q0
                assert residue == (-4 * D0) % q0
                generated.append(residue)
        intrinsic = {(-4 * D0) % q0 for D0 in divisors_of_square(A0)}
        generated_union = set(generated)
        assert generated_union == intrinsic
        raw_b_count += len(generated)
        intrinsic_b_count += len(intrinsic)
        overlap_b_count += len(generated_union & intrinsic)
    assert (prime_count, raw_b_count, intrinsic_b_count, overlap_b_count) == (
        218, 7193, 5114, 5114,
    )

    # Lemma 29.2 at finite scale.  Restrict to classes compatible with the
    # hard progression P=1 (mod 24), and deduplicate residues at each full
    # modulus before taking mass.  Every raw class is also reconstructed as
    # an exact Type-I parameter identity.
    def case_a_stats(X0):
        residue_sets = {}
        raw_mass = 0.0
        raw_classes = 0
        for q0 in primerange(3, X0 // 4 + 1):
            if q0 % 4 != 3:
                continue
            for n0 in range(1, X0 // (4 * q0) + 1):
                if gcd(q0, 2 * n0) != 1:
                    continue
                h0 = 4 * n0
                if (q0 + 1) % gcd(h0, 24) != 0:
                    continue
                for k0 in positive_divisors(n0):
                    c0 = n0 // k0
                    value = (-4 * c0 * k0 * k0) % q0
                    if pow(value, (q0 - 1) // 2, q0) != 1:
                        continue
                    root = pow(value, (q0 + 1) // 4, q0)
                    for r0 in {root, (-root) % q0}:
                        # q=3 shares a factor with the hard modulus 24.
                        if q0 == 3 and r0 != 1:
                            continue
                        t0 = ((r0 + q0) * pow(h0, -1, q0)) % q0
                        residue = (-q0 + h0 * t0) % (h0 * q0)
                        modulus = h0 * q0
                        assert residue % q0 == r0
                        assert (residue + q0) % h0 == 0
                        assert (residue - 1) % gcd(modulus, 24) == 0
                        assert (residue * residue + 4 * c0 * k0 * k0) % q0 == 0

                        # Use a positive representative to replay (26.2)--(26.4).
                        P0 = residue or modulus
                        a0 = (P0 + q0) // h0
                        norm0 = P0 * P0 + 4 * c0 * k0 * k0
                        assert norm0 % q0 == 0
                        cofactor = norm0 // q0
                        assert (cofactor + P0) % h0 == 0
                        b0 = (cofactor + P0) // h0
                        assert P0 * (a0 + b0) == k0 * (4 * a0 * b0 * c0 - 1)

                        residue_sets.setdefault(modulus, set()).add(residue)
                        raw_classes += 1
                        raw_mass += 1 / modulus
        distinct_mass = sum(len(residues) / modulus
                            for modulus, residues in residue_sets.items())
        return (distinct_mass, raw_mass, raw_classes,
                len(residue_sets), sum(map(len, residue_sets.values())))

    cutoffs = (500, 1000, 2000, 3000)
    expected = {
        500: (0.09249689000908083, 0.09487784239003325, 23, 14, 22),
        1000: (0.15946563337222747, 0.16572603963263366, 76, 36, 72),
        2000: (0.2383230628981856, 0.2532556867033714, 206, 81, 190),
        3000: (0.29711217554271874, 0.31965677026770084, 371, 136, 336),
    }
    stats = {}
    for X0 in cutoffs:
        got = case_a_stats(X0)
        wanted = expected[X0]
        assert abs(got[0] - wanted[0]) < 1e-14
        assert abs(got[1] - wanted[1]) < 1e-14
        assert got[2:] == wanted[2:]
        stats[X0] = got

    # The artificial envelope in (29.7) grants two roots to every triple.
    # It is an upper bound even before hard-compatibility and class dedup.
    envelope = {}
    for X0 in cutoffs:
        value = 0.0
        for q0 in primerange(3, X0 // 4 + 1):
            if q0 % 4 != 3:
                continue
            for n0 in range(1, X0 // (4 * q0) + 1):
                value += len(positive_divisors(n0)) / (2 * n0 * q0)
        assert stats[X0][1] <= value + 1e-15
        envelope[X0] = value

    # Scope the example precisely: one local projection is outside R(7), but
    # the other is subsumed, §4 already has the exact progression, and 673 is
    # itself intrinsic at modulus 15.  No new-target claim is being tested.
    q0, c0, k0, h0 = 7, 5, 1, 20
    roots = {1, 6}
    crt_classes = set()
    for r0 in roots:
        t0 = ((r0 + q0) * pow(h0, -1, q0)) % q0
        crt_classes.add((-q0 + h0 * t0) % (h0 * q0))
    intrinsic7 = {(-4 * D0) % 7 for D0 in divisors_of_square(2)}
    intrinsic35 = {(-4 * D0) % 35 for D0 in divisors_of_square(9)}
    intrinsic15 = {(-4 * D0) % 15 for D0 in divisors_of_square(4)}
    assert crt_classes == {13, 113}
    assert intrinsic7 == {3, 5, 6}
    assert 13 % 7 == 6 in intrinsic7 and 113 % 7 == 1 not in intrinsic7
    eligible_divisors = [M for M in positive_divisors(140) if M % 4 == 3]
    assert eligible_divisors == [7, 35]
    assert intrinsic35 == {23, 26, 31, 32, 34} and 113 % 35 == 8
    assert intrinsic15 == {7, 11, 13, 14}
    assert 673 % 140 == 113 and 673 % 24 == 1
    assert 673 % 15 == 13 in intrinsic15
    assert (673 * 673 + 4 * c0 * k0 * k0) % q0 == 0
    a0 = (673 + q0) // h0
    b0 = ((673 * 673 + 4 * c0 * k0 * k0) // q0 + 673) // h0
    assert 673 * (a0 + b0) == k0 * (4 * a0 * b0 * c0 - 1)

    ratios = []
    for X0 in cutoffs:
        distinct, raw = stats[X0][:2]
        L0 = log(X0)
        ratios.append((X0, round(distinct, 6), round(distinct / raw, 4),
                       round(distinct / (L0 * L0 * log(L0)), 6),
                       round(distinct / L0**3, 6)))

    print("Case-B q<=3000: %d primes, %d raw descriptions -> %d distinct; "
          "intrinsic overlap %d/%d" %
          (prime_count, raw_b_count, intrinsic_b_count,
           overlap_b_count, intrinsic_b_count))
    print("Case-A hard-compatible CRT (X, mass, union/raw, "
          "mass/(L^2logL), mass/L^3):", ratios)
    print("Case-A counts at X=3000: 371 raw -> 336 distinct classes at "
          "136 moduli; all exact reconstructions OK")
    print("(q,c,k)=(7,5,1): 13 mod 140 is intrinsic at 7; 113 has a "
          "projection absent at 7 (and no containing intrinsic progression), "
          "but already occurs in §4 and 673 is intrinsic at 15")


print("\n== (ab) transfer-law congruence supply (§29) ==")
check_ab()

# ---------------------------------------------------------------- (ac)
def check_ac():
    """Section 30: common-g moves and full Type-II orbit closure."""
    from functools import lru_cache
    from math import gcd, isqrt
    from sympy import divisors, primerange

    @lru_cache(None)
    def divs(n):
        return tuple(divisors(n))

    def tuple_value(row):
        A, B, C, K = row
        assert min(row) >= 1 and (A + B) % K == 0
        P = 4 * A * B * C - (A + B) // K
        assert P >= 2
        return P

    def assert_tuple(row, expected=None, check_fractions=False):
        P = tuple_value(row)
        if expected is not None:
            assert P == expected
        if check_fractions:
            A, B, C, K = row
            denominators = (A * B * C, P * A * C * K, P * B * C * K)
            assert sum(Fraction(1, d) for d in denominators) == Fraction(4, P)
        return P

    def relabel(row, K2):
        A, B, C, K = row
        R = C * K
        assert R % K2 == 0 and (A + B) % K2 == 0
        out = (A, B, R // K2, K2)
        assert K2 * assert_tuple(out) == K * assert_tuple(row)
        return out

    def common_add(left, right, kind, Kout):
        """The three fixed centered-factor maps (30.4)."""
        a1, b1, c1, k1 = left
        a2, b2, c2, k2 = right
        R = c1 * k1
        assert c2 * k2 == R
        g = 4 * R
        D1, E1 = g * a1 - 1, g * b1 - 1
        D2, E2 = g * a2 - 1, g * b2 - 1
        if kind == "++":
            A, B = a1 + a2, b1 + b2
            Dp, Ep = D1 + D2 + 1, E1 + E2 + 1
        elif kind == "1+":
            A, B = a1, b1 + b2
            Dp, Ep = D1, E1 + E2 + 1
        elif kind == "+1":
            A, B = a1 + a2, b1
            Dp, Ep = D1 + D2 + 1, E1
        else:
            raise AssertionError(kind)
        assert Dp == g * A - 1 and Ep == g * B - 1
        assert R % Kout == 0 and (A + B) % Kout == 0
        out = (A, B, R // Kout, Kout)
        pout = assert_tuple(out)
        T = g * A * B - A - B
        assert T == Kout * pout
        p1, p2 = assert_tuple(left), assert_tuple(right)
        if kind == "++":
            assert T == k1 * p1 + k2 * p2 + g * (a1 * b2 + a2 * b1)
        elif kind == "1+":
            assert T == k1 * p1 + b2 * (g * a1 - 1)
        else:
            assert T == k1 * p1 + a2 * (g * b1 - 1)
        assert Dp * Ep == 1 + g * Kout * pout
        return out

    def move_x(row):
        A, B, C, K = row
        old = assert_tuple(row)
        out = (A + K, B, C, K)
        assert assert_tuple(out) == old + (4 * B * C * K - 1)
        g = 4 * C * K
        assert g * (A + K) - 1 == (g * A - 1) + g * K
        return out

    def move_y(row):
        A, B, C, K = row
        old = assert_tuple(row)
        out = (A, B + K, C, K)
        assert assert_tuple(out) == old + (4 * A * C * K - 1)
        g = 4 * C * K
        assert g * (B + K) - 1 == (g * B - 1) + g * K
        return out

    def move_z(row):
        A, B, C, K = row
        old = assert_tuple(row)
        out = (A, B, C + 1, K)
        assert assert_tuple(out) == old + 4 * A * B
        return out

    # Exhaust the richer common-g law on independent readings of each source
    # and every output reading in a nontrivial positive box.
    additive_checks = 0
    for R in range(1, 9):
        sources = []
        for a in range(1, 5):
            for b in range(1, 5):
                for k in divs(gcd(R, a + b)):
                    sources.append((a, b, R // k, k))
        for left in sources:
            for right in sources:
                for kind in ("++", "1+", "+1"):
                    if kind == "++":
                        A, B = left[0] + right[0], left[1] + right[1]
                    elif kind == "1+":
                        A, B = left[0], left[1] + right[1]
                    else:
                        A, B = left[0] + right[0], left[1]
                    for kout in divs(gcd(R, A + B)):
                        common_add(left, right, kind, kout)
                        additive_checks += 1

    # What actually commutes is the reduced K=1 translation grid, not the
    # mixed seven-schema closure.  Binary input order and relabel/X order give
    # explicit noncommuting regressions.
    commute_base = (2, 3, 4, 1)
    assert move_x(move_y(commute_base)) == move_y(move_x(commute_base))
    assert move_x(move_z(commute_base)) == move_z(move_x(commute_base))
    assert move_y(move_z(commute_base)) == move_z(move_y(commute_base))
    binary_left = (1, 1, 1, 1)
    binary_right = (2, 1, 1, 1)
    assert common_add(binary_left, binary_right, "1+", 1) == (1, 2, 1, 1)
    assert common_add(binary_right, binary_left, "1+", 1) == (2, 2, 1, 1)
    noncommuting_sheet = (1, 1, 1, 2)
    assert move_x(relabel(noncommuting_sheet, 1)) == (2, 1, 2, 1)
    assert relabel(move_x(noncommuting_sheet), 1) == (3, 1, 2, 1)

    # A nontrivial binary branch can preserve value, contrary to the old
    # blanket fixed-value claim.  It still uses an auxiliary source and is not
    # a source-independent invertible fixed-fibre action.
    fixed_value_left = (2, 69, 4, 1)
    fixed_value_right = (1, 22, 4, 1)
    fixed_value_output = common_add(
        fixed_value_left, fixed_value_right, "++", 2)
    assert assert_tuple(fixed_value_left) == 2137
    assert assert_tuple(fixed_value_right) == 329
    assert fixed_value_output == (3, 91, 2, 2)
    assert assert_tuple(fixed_value_output) == 2137

    # Fixed-slice grid normal forms and all relabellings in a small box.  The
    # counter records valid input rows, not the larger number of move checks.
    grid_rows = 0
    for C in range(1, 5):
        for K in range(1, 7):
            for A in range(1, 13):
                for B in range(1, 13):
                    if (A + B) % K:
                        continue
                    row = (A, B, C, K)
                    P = assert_tuple(row)
                    move_x(row)
                    move_y(row)
                    move_z(row)
                    R = C * K
                    for K2 in divs(gcd(R, A + B)):
                        relabel(row, K2)

                    A0 = (A - 1) % K + 1
                    B0 = (B - 1) % K + 1
                    assert A0 + B0 in (K, 2 * K)
                    seed = (A0, B0, C, K)
                    u, v = (A - A0) // K, (B - B0) // K
                    current = seed
                    for unused in range(u):
                        current = move_x(current)
                    for unused in range(v):
                        current = move_y(current)
                    assert current == row
                    g = 4 * C * K
                    assert P == (assert_tuple(seed)
                                 + u * (g * B0 - 1)
                                 + v * (g * A0 - 1) + g * K * u * v)
                    grid_rows += 1

    # Construct every bounded decorated lattice node from the single seed.
    decorated_nodes = 0
    global_seed = (1, 1, 1, 1)
    assert_tuple(global_seed, 2, check_fractions=True)
    for R in range(1, 9):
        eR = global_seed
        for unused in range(R - 1):
            eR = move_z(eR)
        assert eR == (1, 1, R, 1)
        for A in range(1, 9):
            for B in range(1, 9):
                current = eR
                previous = assert_tuple(current)
                for unused in range(A - 1):
                    current = common_add(current, eR, "+1", 1)
                    assert assert_tuple(current) > previous
                    previous = assert_tuple(current)
                for unused in range(B - 1):
                    current = common_add(current, eR, "1+", 1)
                    assert assert_tuple(current) > previous
                    previous = assert_tuple(current)
                assert current == (A, B, R, 1)
                for K in divs(gcd(R, A + B)):
                    target = relabel(current, K)
                    assert target == (A, B, R // K, K)
                    assert assert_tuple(current) == K * assert_tuple(target)
                    decorated_nodes += 1

    # The canonical KP path need not minimize the peak: this P=73 path peaks
    # at the target itself.  Also check the unbounded-K family algebraically;
    # infinitude of prime values is the separate Dirichlet argument in §30.
    low_peak_path = [global_seed]
    for unused in range(2):
        low_peak_path.append(move_z(low_peak_path[-1]))
    low_peak_path.append(move_y(low_peak_path[-1]))
    low_peak_path.append(relabel(low_peak_path[-1], 3))
    for unused in range(6):
        low_peak_path.append(move_y(low_peak_path[-1]))
    assert low_peak_path[-1] == (1, 20, 1, 3)
    assert [assert_tuple(row) for row in low_peak_path] == [
        2, 6, 10, 21, 7, 18, 29, 40, 51, 62, 73,
    ]
    assert max(map(assert_tuple, low_peak_path)) == 73 < 3 * 73
    for n in range(20):
        K = 6 * n + 3
        row = (1, 7 * K - 1, 1, K)
        P = assert_tuple(row)
        assert P == 28 * K - 11 == 168 * n + 73
        assert P % 24 == 1
        assert assert_tuple(relabel(row, 1)) == K * P

    # Lemma 25.8 gives every ordered Type-II tuple of P with no search cutoff.
    def row_at(P, A, B):
        if 2 * A * B > P:
            return None
        C = P // (4 * A * B) + 1
        q = 4 * A * B * C - P
        if (A + B) % q:
            return None
        return (A, B, C, (A + B) // q)

    def all_rows(P):
        rows = []
        for A in range(1, isqrt(P // 2) + 1):
            for B in range(A, P // (2 * A) + 1):
                row = row_at(P, A, B)
                if row is None:
                    continue
                rows.append(row)
                if A != B:
                    rows.append((B, A, row[2], row[3]))
        return sorted(rows)

    hard_primes = [p for p in primerange(2, 5001) if p % 24 == 1]
    rows_by_prime = {}
    nonseed_endpoints = []
    for P in hard_primes:
        rows = all_rows(P)
        assert rows                         # finite value-fibre regression only
        rows_by_prime[P] = rows
        for row in rows:
            A, B, C, K = row
            assert_tuple(row, P, check_fractions=True)
            R = C * K
            current = relabel(row, 1)
            assert current == (A, B, R, 1)
            assert assert_tuple(current) == K * P  # canonical lift, not minimum
            while current[0] > 1:
                a, b, r, one = current
                nxt = (a - 1, b, r, one)
                assert assert_tuple(current) - assert_tuple(nxt) == 4 * r * b - 1
                current = nxt
            while current[1] > 1:
                a, b, r, one = current
                nxt = (a, b - 1, r, one)
                assert assert_tuple(current) - assert_tuple(nxt) == 4 * r * a - 1
                current = nxt
            while current[2] > 1:
                a, b, r, one = current
                nxt = (a, b, r - 1, one)
                assert assert_tuple(current) - assert_tuple(nxt) == 4 * a * b
                current = nxt
            if current != global_seed:
                nonseed_endpoints.append((P, row, current))
    assert not nonseed_endpoints

    expected_table = (
        (500, 9, 102, 41), (1000, 14, 182, 74),
        (2000, 30, 522, 197), (3000, 46, 940, 359),
        (4000, 61, 1402, 524), (5000, 76, 1938, 717),
    )
    table = []
    for bound, wanted_primes, wanted_rows, wanted_seeds in expected_table:
        ps = [P for P in hard_primes if P <= bound]
        row_count = sum(len(rows_by_prime[P]) for P in ps)
        seeds = {
            ((A - 1) % K + 1, (B - 1) % K + 1, C, K)
            for P in ps for A, B, C, K in rows_by_prime[P]
        }
        off_seed = sum(P <= bound for P, row, endpoint in nonseed_endpoints)
        table.append((bound, len(ps), row_count, len(seeds), off_seed))
        assert (len(ps), row_count, len(seeds)) == (
            wanted_primes, wanted_rows, wanted_seeds
        )

    print("common-g additive laws: %d admissible independent-reading branches; "
          "valid grid rows audited: %d; bounded decorated nodes constructed: "
          "%d" % (additive_checks, grid_rows, decorated_nodes))
    print("complete finite value-fibre canonical reductions through 5000 "
          "(bound, hard primes, ordered tuples, local fixed-slice seeds, "
          "endpoints off global seed):", table)


print("\n== (ac) full Type-II generation orbit (§30) ==")
check_ac()


# ---------------------------------------------------------------- (ad)
def check_ad():
    """Exact small-scale rough-event enumeration for §31."""

    def tau3(n):
        out = 1
        for e in factorint(n).values():
            out *= (e + 1) * (e + 2) // 2
        return out

    expected = {
        (80, 3): (13, 2.6377878615258217, 3.6115446632487553,
                  0.04715333385100241, 0.204479861037451,
                  0.05730010074882489),
        (120, 3): (20, 3.363912912202289, 5.484397404494572,
                   0.05490972332435533, 0.15887281668150682,
                   0.09339846903266923),
        (160, 5): (21, 3.2544024853701723, 4.131858245775285,
                   0.05087060224100122, 0.19332400027263097,
                   0.09144414035036377),
        (200, 5): (27, 3.7196502318836147, 4.7730977015384815,
                   0.05164884872205539, 0.2987014116162228,
                   0.09309693804572494),
    }
    table = []
    determinant_checks = class_checks = 0
    for (X, z), wanted in expected.items():
        L = log(X)
        kappa = 0.02
        rows = []
        rough_primes = set()
        for M in range(3, X + 1, 4):
            A0 = (M + 1) // 4
            residues = {(-4 * d) % M for d in divisors_of_square(A0)}
            F = len(residues)
            assert F <= tau3(A0)
            class_checks += 1
            factors = tuple(map(int, factorint(M)))
            if min(factors) <= z:
                continue
            rows.append((M, F, factors))
            rough_primes.update(factors)
            for q in factors:
                k = M // q
                r = k % 4
                assert r in (1, 3) and (q * r) % 4 == 3
                c = (q * r + 1) // 4
                t = (k - r) // 4
                assert 4 * c - q * r == 1
                assert q * t + c == A0
                determinant_checks += 1

        b = {q: L**3 / (q * log(z)) for q in rough_primes}
        charges = {q: kappa * b[q] for q in rough_primes}
        total0 = total = 0.0
        neighborhoods = {q: 0.0 for q in rough_primes}
        composite_neighborhoods = {q: 0.0 for q in rough_primes}
        for M, F, factors in rows:
            activity = (F / M) * exp(2 * sum(charges[q] for q in factors))
            total0 += F / M
            total += activity
            for q in factors:
                neighborhoods[q] += activity
                if M != q:                  # remove the prime-modulus diagonal
                    composite_neighborhoods[q] += activity

        got = (
            len(rows), total0, total, total / (L**3 / log(z)),
            max(neighborhoods[q] / b[q] for q in rough_primes),
            max(composite_neighborhoods[q] / b[q]
                for q in rough_primes),
        )
        assert got[0] == wanted[0]
        assert all(abs(x - y) < 1e-12 for x, y in zip(got[1:], wanted[1:]))
        table.append((X, z, got[0], round(got[1], 5), round(got[3], 5),
                      round(got[4], 5), round(got[4] / kappa, 5),
                      round(got[5], 5)))

    print("rough weighted events (X,z,count,S0,S_a/(L^3/log z),"
          "max Tq/bq,max Tq/aq,max composite Tq/bq):", table)
    print("divisor-majorant/algebra checks:", class_checks,
          "class bounds and", determinant_checks, "linear-form readings")


print("\n== (ad) weighted rough shifted-divisor estimates (§31) ==")
check_ad()

# ---------------------------------------------------------------- (ae)
def check_ae():
    """Section 32: k=1 certification, mass, and nine-prime anatomy."""
    from math import isqrt
    from time import monotonic
    from sympy import isprime
    started = monotonic()

    def divs(n):
        out = [1]
        for p, e in factorint(n).items():
            out = [d * p**j for d in out for j in range(e + 1)]
        return tuple(sorted(out))

    # Trace the floor/parity factorization of every small intrinsic D.
    cert = cert1 = certgt1 = pw = direct = 0
    for M in range(3, 300, 4):
        H = (M + 1) // 4
        lower = set()
        for D in divisors_of_square(H):
            u = w = 1
            for p, e in factorint(D).items():
                u *= p ** (e // 2)
                w *= p ** (e % 2)
            v = H // (u * w)
            r = (-4 * D) % M
            P = r + M
            while not isprime(P):
                P += M
            s = (P * v + u) // M
            g = gcd(u, v)
            a, b, c, k = s // g, u // g, g * g * w, v // g
            assert gcd(a, b) == 1
            assert k * P == 4 * a * b * c * k - a - b
            assert sum(Fraction(1, z) for z in
                       (a * b * c, P * a * c * k, P * b * c * k)) == Fraction(4, P)
            assert k == H // gcd(H, D)
            assert (k == 1) == (D % H == 0)
            cert += 1
            cert1 += k == 1
            certgt1 += k > 1
            if D < H:
                lower.add((-4 * D) % M)
        k1classes = {(-t) % M for t in divs(H)}
        assert len(k1classes) == len(divs(H))
        assert len(lower & k1classes) == (len(divs(H // 4)) if H % 4 == 0 else 0)
        for t in divs(H):
            for j in (1, 2, 5):
                P, A, B, C = j * M - t, j, t, H // t
                assert P == 4 * A * B * C - A - B
                assert (4 * A * C - 1) * (4 * B * C - 1) == 4 * P * C + 1
                direct += 1
        if isprime(M):
            for D in divisors_of_square(H):
                if D >= H:
                    continue
                T = prod(p ** (e % 2) for p, e in factorint(D).items())
                d1 = isqrt(D // T)
                d2 = H // (T * d1)
                h = gcd(d1, d2)
                u, v, w = d1 // h, d2 // h, T * h * h
                r = M - 4 * D
                P = r + M
                while not isprime(P):
                    P += M
                j = (P - r) // M
                s = v - u + j * v
                assert gcd(s, u) == 1 and v > 1
                assert v * P == 4 * s * u * w * v - s - u
                assert v == H // gcd(H, D)
                pw += 1
    assert cert1 and certgt1
    assert (409 * 2 + 1) // 7 == 117
    assert 2 * 409 == 4 * 117 * 2 - 117 - 1

    # Truncated all-modulus versus prime-modulus k=1 masses.
    tau = [0] * (100_000 // 4 + 2)
    for d in range(1, len(tau)):
        for n in range(d, len(tau), d):
            tau[n] += 1
    pset = set(primerange(3, 100_001))
    mass = []
    for X in (100, 1_000, 10_000, 100_000):
        whole = sum(tau[H] / (4 * H - 1)
                    for H in range(1, (X + 1) // 4 + 1) if 4 * H - 1 <= X)
        prime = sum(tau[(p + 1) // 4] / p for p in pset if p <= X and p % 4 == 3)
        mass.append((X, whole / log(X)**2, prime / log(X)))
    wanted_mass = ((.120350, .366879), (.119906, .422304),
                   (.120576, .458852), (.121154, .484461))
    for row, wanted in zip(mass, wanted_mass):
        assert abs(row[1] - wanted[0]) < 1e-6
        assert abs(row[2] - wanted[1]) < 1e-6

    nine = (409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321)
    # SPF-backed, memory-bounded independent denominator enumeration.
    limit = max(nine) + 1000
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p

    def fac(n):
        out = []
        while n > 1:
            p, e = spf[n], 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        return out

    def sqdivs(x, P):
        R, values = P * x, [1]
        for p, e in [(P, 2)] + [(p, 2 * e) for p, e in fac(x)]:
            new, power = [], 1
            append = new.append
            for unused in range(e + 1):
                for d in values:
                    value = d * power
                    if value <= R:
                        append(value)
                power *= p
            values = new
        return values

    def sqmult(c):
        return prod(e // 2 + 1 for p, e in fac(c))

    def type_i(P, stop=False):
        raw = primitive = 0
        moduli = set()
        for x in range(P // 4 + 1, 3 * P // 4 + 1):
            q, R = 4 * x - P, P * x
            for d in sqdivs(x, P):
                if (d + R) % q:
                    continue
                y = (R + d) // q
                if y < x or y % P == 0:
                    continue
                z = (R + R * R // d) // q
                if z < y or z % P:
                    continue
                assert 4 * x * y * z == P * (x * y + x * z + y * z)
                h = gcd(x, y)
                A, B = x // h, y // h
                assert (z * h * h) % (P * x * y) == 0
                C = z * h * h // (P * x * y)
                assert h % C == 0
                K = h // C
                assert gcd(A, B) == 1 and P * (A + B) == K * (4 * A * B * C - 1)
                if stop:
                    return True
                orientations = 1 if A == B else 2
                primitive += orientations
                raw += orientations * sqmult(C)
                moduli.add((A + B) // K)
        return False if stop else (raw, primitive, moduli)

    def fdivs(n):
        values = [1]
        for p, e in fac(n):
            values = [d * p**j for d in values for j in range(e + 1)]
        return values

    def k1(P):
        for A in range(1, isqrt(P // 2) + 1):
            for B in fdivs(P + A):
                if B >= A and ((P + A) // B + 1) % (4 * A) == 0:
                    C = (((P + A) // B) + 1) // (4 * A)
                    assert P == 4 * A * B * C - A - B
                    return A, B, C, 1
        return None

    # Same intrinsic class, opposite target-level k=1 outcomes.
    assert 17 % 7 == 409 % 7 == (-4) % 7
    assert k1(17) == (1, 6, 1, 1)
    assert k1(409) is None

    def type_ii(P):
        rows = []
        for A in range(1, isqrt(P // 2) + 1):
            for B in range(A, P // (2 * A) + 1):
                C = P // (4 * A * B) + 1
                q = 4 * A * B * C - P
                if (A + B) % q == 0:
                    K = (A + B) // q
                    assert K * P == 4 * A * B * C * K - A - B
                    rows.append((A, B, C, K))
        return rows

    minima = {
        409:(2,((1,13,8),(1,21,5),(1,117,1),(7,15,1))),
        577:(2,((1,5,29),(1,21,7),(1,77,2),(1,165,1))),
        5569:(2,((1,141,10),(1,237,6),(9,157,1))),
        9601:(2,((1,37,65),(1,173,14),(3,115,7),(3,835,1))),
        23929:(2,((1,21,285),(1,53,113),(1,301,20),(1,6837,1),(3,19,105),(7,15,57))),
        83449:(2,((3,211,33),(43,243,2))),
        102001:(3,((5,232,22),)),
        329617:(2,((1,5,16481),(1,213,387),(1,9285,9),(1,43949,2),(5,41,402))),
        712321:(2,((1,69,2581),(1,253,704),(1,1877,95),(1,61941,3),
                   (3,499,119),(3,571,104),(13,2745,5),(153,1165,1))),
    }
    idata = {
        409:(22,18,5,()), 577:(22,22,9,(7,39)),
        5569:(40,34,12,(39,47,143)), 9601:(40,34,11,()),
        23929:(196,128,36,(7,11,39,303)), 83449:(70,64,25,(39,191)),
        102001:(106,82,25,(47,111,115)),
        329617:(230,184,71,(3,107,167,21975)),
        712321:(150,122,49,(35,191)),
    }
    anatomy = []
    for P in nine:
        assert k1(P) is None
        rows = type_ii(P)
        mk = min(r[3] for r in rows)
        mts = tuple(r[:3] for r in rows if r[3] == mk)
        assert (mk, mts) == minima[P]
        qb = {(A + B) // K for A, B, C, K in rows}
        raw, primitive, qa = type_i(P)
        wr, wp, wm, common = idata[P]
        assert (raw, primitive, len(qa), tuple(sorted(qa & qb))) == (wr, wp, wm, common)
        assert qa - qb and qb - qa
        anatomy.append((P, mk, len(mts), raw, primitive, len(qa), len(qb), common))

    type_i_less = [P for P in primerange(3, 100_001) if not type_i(P, stop=True)]
    assert type_i_less == []
    elapsed = monotonic() - started
    print("certification (intrinsic,k=1,k>1,§15,direct) =", (cert,cert1,certgt1,pw,direct))
    print("k=1 masses (X,all/L^2,prime/L) =",
          [(X,round(a,6),round(b,6)) for X,a,b in mass])
    print("anatomy (P,min-k,#min,Type-I,primitive,#A-mod,#B-mod,common) =", anatomy)
    print("Type-I-less odd primes <=10^5:", type_i_less, "; block seconds %.2f" % elapsed)


print("\n== (ae) k=1 certification and nine-prime anatomy (§32) ==")
check_ae()

# ---------------------------------------------------------------- (af)
def check_af():
    """Section 33: exact windows and failure of prime-coordinate tensoring."""
    import numpy as np

    def exact_avoiders(X0):
        moduli0 = list(range(3, X0 + 1, 4))
        period0 = lcm(*moduli0)
        alive0 = np.ones(period0, dtype=np.bool_)
        for M0 in moduli0:
            A0 = (M0 + 1) // 4
            for D0 in divisors_of_square(A0):
                alive0[(-4 * D0) % M0::M0] = False
        return period0, alive0

    expected = {
        15: (1155, 256, {100: (18, 27), 1000: (217, 226)}),
        23: (504735, 57344,
             {100: (4, 21), 1000: (98, 128),
              10000: (1110, 1161), 100000: (11340, 11385)}),
    }
    rows = []
    saved15 = None
    for X0, (period_expected, survivors_expected, windows) in expected.items():
        period0, alive0 = exact_avoiders(X0)
        survivors0 = int(alive0.sum())
        assert (period0, survivors0) == (period_expected, survivors_expected)
        max_window = max(windows)
        extended = np.concatenate((alive0, alive0[:max_window]))
        prefix = np.empty(extended.size + 1, dtype=np.int64)
        prefix[0] = 0
        np.cumsum(extended, out=prefix[1:])
        for width, extrema in windows.items():
            counts = prefix[width:width + period0] - prefix[:period0]
            got = (int(counts.min()), int(counts.max()))
            assert got == extrema
            # Every survivor belongs to exactly width cyclic windows.
            assert int(counts.sum()) == width * survivors0
            rows.append((X0, width, got[0],
                         round(width * survivors0 / period0, 4), got[1]))
        if X0 == 15:
            saved15 = alive0

    # Three corners of a prime-coordinate rectangle survive, but the fourth
    # is the intrinsic class 13 mod 15 (D=8).  A tensor product cannot do this.
    rectangle = (231, 616, 693, 1078)
    assert [(n % 3, n % 5, n % 7, n % 11) for n in rectangle] == [
        (0, 1, 0, 0), (1, 1, 0, 0), (0, 3, 0, 0), (1, 3, 0, 0)]
    assert [bool(saved15[n]) for n in rectangle] == [True, True, True, False]
    assert 1078 % 15 == (-4 * 8) % 15 and 16 % 8 == 0

    print("exact cyclic windows (X,W,min,mean,max) =", rows)
    print("X=15 prime-coordinate rectangle: three survivors, crossed corner killed")


print("\n== (af) finite-window transfer obstructions (§33) ==")
check_af()


# ---------------------------------------------------------------------- (ag)
def check_ag():
    """§34: k-incidence moment, real CS loss, and composite completion."""
    from sympy import li as logarithmic_integral
    from time import monotonic

    started = monotonic()
    x, z, K, c, h0 = 30_000, 35, 25, 1, 3
    J = tuple(range(1, K + 1, 4))

    def phi(n):
        ans = n
        for p in factorint(n):
            ans = ans // p * (p - 1)
        return ans

    def incidence(u, v):
        return sum((u + c * v) % k == 0 and gcd(u * v, k) == 1 for k in J)

    pairs = [(u, v) for u in range(h0 + 1, z + 1)
             for v in range(h0 + 1, z + 1) if gcd(u, v) == 1]
    direct_m1 = sum(Fraction(incidence(u, v), u * v) for u, v in pairs)
    direct_m2 = sum(Fraction(incidence(u, v) ** 2, u * v) for u, v in pairs)
    expanded_m2 = sum(
        Fraction(1, u * v)
        for k in J for kp in J
        for u, v in pairs if (u + c * v) % lcm(k, kp) == 0
    )
    assert direct_m2 == expanded_m2       # exact expansion in Lemma 34.7
    threshold = 2
    bad_m1 = sum(Fraction(incidence(u, v), u * v) for u, v in pairs
                 if incidence(u, v) > threshold)
    assert bad_m1 <= direct_m2 / threshold

    rows = []
    for u, v in pairs:
        q = 4 * u * v
        for k in J:
            if gcd(u * v, k) == 1 and (u + c * v) % k == 0:
                rows.append((k, u, v, q, (-pow(k, -1, q)) % q))

    good_q_multiplicity = Counter()
    for k, u, v, q, a in rows:
        if incidence(u, v) <= threshold:
            good_q_multiplicity[q] += 1
    assert all(mult <= threshold * 2 ** len(factorint(q // 4))
               for q, mult in good_q_multiplicity.items())  # (34.21)

    # Actual E(x;q,a) on the occupied toy progressions and its exact CS bound.
    progression_multiplicity = Counter((q, a) for k, u, v, q, a in rows)
    primes = list(primerange(x + 1, 2 * x + 1))
    residue_counts = {
        q: Counter(p % q for p in primes)
        for q in {q for q, a in progression_multiplicity}
    }
    delta_li = float(logarithmic_integral(2 * x) - logarithmic_integral(x))
    errors = {
        (q, a): residue_counts[q][a] - delta_li / phi(q)
        for q, a in progression_multiplicity
    }
    actual_l1 = sum(mult * abs(errors[qa])
                    for qa, mult in progression_multiplicity.items())
    occupied_variance = sum(e * e for e in errors.values())
    multiplicity_square = sum(mult * mult for mult in progression_multiplicity.values())
    cs_bound = (occupied_variance * multiplicity_square) ** 0.5
    assert actual_l1 <= cs_bound * (1 + 1e-12)
    main = sum(mult * delta_li / phi(q)
               for (q, a), mult in progression_multiplicity.items())
    harmonic_k = sum(phi(k) / k ** 2 for k in J)
    scale_proxy = x ** (7 / 6) * (K * harmonic_k) ** 0.5
    target_proxy = x * log(x) * harmonic_k

    # Prime-power/CRT care: small q=4uv complete Kloosterman sums satisfy
    # the standard tau(q)*sqrt((r,h,q)q) envelope used in (34.11).
    q = 4 * 11 * 13
    tau_q = prod(e + 1 for e in factorint(q).values())
    kloosterman_ratios = []
    for r in (1, 2, 3, 5, 7):
        for h in (1, 2, 4, 6):
            complete = sum(
                cmath.exp(2j * cmath.pi * (r * a + h * pow(a, -1, q)) / q)
                for a in range(1, q) if gcd(a, q) == 1
            )
            envelope = tau_q * (gcd(r, h, q) * q) ** 0.5
            kloosterman_ratios.append(abs(complete) / envelope)
    assert max(kloosterman_ratios) < 1 + 1e-9
    floor_completion_loss = (4 * K ** 20) ** 0.5 / K
    assert floor_completion_loss == 2 * K ** 9

    elapsed = monotonic() - started
    print("toy incidence (triples,M1,M2,bad>M2/T,max good W) =",
          (len(rows), round(float(direct_m1), 6), round(float(direct_m2), 6),
           round(float(bad_m1), 6), max(good_q_multiplicity.values())))
    print("toy progression (|E|/main,CS/main,(34.7)-scale/main) =",
          tuple(round(v, 6) for v in
                (actual_l1 / main, cs_bound / main, scale_proxy / target_proxy)))
    print("completion (max Weil-envelope ratio,q^.5/K at floor,seconds) =",
          (round(max(kloosterman_ratios), 6), int(floor_completion_loss),
           round(elapsed, 3)))


print("\n== (ag) prime-slice k-aspect assault (§34) ==")
check_ag()


# ---------------------------------------------------------------- (ah)
def check_ah():
    """Unit W: bounded residues and the two a=1 special slices (§35)."""
    from time import monotonic

    started = monotonic()

    def divs(n):
        values = [1]
        for r, e in factorint(n).items():
            values = [d * r**j for d in values for j in range(e + 1)]
        return values

    def square_divs(n):
        values = [1]
        for r, e in factorint(n).items():
            values = [d * r**j for d in values for j in range(2 * e + 1)]
        return values

    hard10 = [p for p in primerange(5, 10_000_000) if p % 24 == 1]
    hard1 = [p for p in hard10 if p < 1_000_000]

    q3_count = qwindow_count = 0
    for p in hard1:
        x3 = (p + 3) // 4
        factor_q3 = any(r % 3 == 2 for r in factorint(x3))
        q3_count += factor_q3
        hit = False
        for q in range(3, 64, 4):
            x = (p + q) // 4
            literal_hit = any((d + x) % q == 0 for d in square_divs(x))
            if q == 3:
                assert literal_hit == factor_q3
            if literal_hit:
                hit = True
                break
        qwindow_count += hit
    assert (len(hard1), q3_count, qwindow_count) == (9732, 5192, 9732)

    def a1_type_ii(p, c0, c1):
        for c in range(c0, c1 + 1):
            modulus = 4 * c
            for D in divs(p + modulus):
                if D % modulus == modulus - 1:
                    k = (D + 1) // modulus
                    t = (p + modulus) // D
                    b = k * t - 1
                    assert b > 0 and k * p == 4 * b * c * k - b - 1
                    return c, D, k, b
        return None

    type_ii_first = {p: a1_type_ii(p, 1, 256) for p in hard1}
    caps = (1, 2, 4, 8, 16, 32, 64, 128)
    cap_counts = tuple(sum(got is not None and got[0] <= cap
                           for got in type_ii_first.values()) for cap in caps)
    assert cap_counts == (4850, 7824, 8962, 9525, 9680, 9719, 9726, 9727)
    type_ii_residual = [p for p, got in type_ii_first.items() if got is None]
    assert type_ii_residual == [193, 2521, 66529]
    for p in type_ii_residual:
        assert a1_type_ii(p, 257, (p + 2) // 4) is None

    rescue_tuples = {
        193: (2, 5, 5, 1),
        2521: (2, 159, 2, 7),
        66529: (5, 832, 4, 27),
    }
    for p, (a, b, c, k) in rescue_tuples.items():
        assert gcd(a, b) == 1
        assert k * p == 4 * a * b * c * k - a - b

    # Canonically reconstruct every q<=63 witness below 10^5 and replay the
    # maximum, over p, of the least |a-b| in that window.
    max_least_offset = None
    for p in (p for p in hard1 if p < 100_000):
        best = None
        for h in range(3, 64, 4):
            x = (p + h) // 4
            for d in square_divs(x):
                if (d + x) % h:
                    continue
                g0 = gcd(d, x)
                a = d // g0
                assert g0 % a == 0
                c = g0 // a
                b = x // g0
                assert (a + b) % h == 0
                k = (a + b) // h
                assert gcd(a, b) == 1
                assert k * p == 4 * a * b * c * k - a - b
                row = (abs(a - b), h, a, b, c, k)
                best = row if best is None else min(best, row)
        assert best is not None
        row = (best[0], p, best[1:])
        max_least_offset = row if max_least_offset is None else max(max_least_offset, row)
    assert max_least_offset == (535, 87049, (47, 38, 573, 1, 13))

    # The first 1000 c-values cover almost everything.  Scan the residual
    # in increasing c through the proved finite bound, caching 4c+1 divisors.
    rules = []
    for c in range(1, 1001):
        n = 4 * c + 1
        rules.extend((c, D) for D in divs(n) if D < n and D % 4 == 3)
    first, type_i_residual = {}, []
    for p in hard10:
        got = next(((c, D) for c, D in rules if (p + D) % (4 * c) == 0), None)
        if got is None:
            type_i_residual.append(p)
        else:
            first[p] = got

    cache = {}
    for p in type_i_residual:
        got = None
        for c in range(1001, (3 * p + 1) // 8 + 1):
            if c not in cache:
                n = 4 * c + 1
                cache[c] = [D for D in divs(n) if D < n and D % 4 == 3]
            for D in cache[c]:
                if (p + D) % (4 * c) == 0:
                    got = (c, D)
                    break
            if got is not None:
                break
        assert got is not None, p
        first[p] = got

    for p, (c, D) in first.items():
        E = (4 * c + 1) // D
        k = (p + D) // (4 * c)
        b = (p * E + 1) // (4 * c)
        assert b * D == p + k
        assert p * (1 + b) == k * (4 * b * c - 1)

    largest = max((c, p, D) for p, (c, D) in first.items())
    assert len(hard10) == 82887
    assert largest == (107588, 8604961, 2079)
    elapsed = monotonic() - started
    print("q=3/q<=63 counts =", (q3_count, qwindow_count),
          "; a=1 Type-II cap counts/residual =", (cap_counts, type_ii_residual))
    print("Type-II rescues/max least q<=63 offset =",
          (tuple(rescue_tuples.values()), max_least_offset))
    print("a=1 Type-I hard primes/max first c =", (len(hard10), largest),
          "; campaign-host calibration seconds %.2f" % elapsed)


print("\n== (ah) Unit W blind pointwise slices (§35) ==")
check_ah()

# ---------------------------------------------------------------- (ai)
def check_ai():
    """§36: exact Type-I character/quadric mass and slice obstructions."""
    from fractions import Fraction as Q
    from functools import lru_cache
    from math import isqrt
    import os

    ground = (
        73, 193, 241, 673, 1129, 1153, 2473, 2521, 3169, 3361, 5281,
        409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321,
    )
    expected_raw = (
        8, 8, 10, 26, 32, 30, 56, 12, 26, 26, 36,
        22, 22, 40, 40, 196, 70, 106, 230, 150,
    )
    expected_primitive = (
        8, 8, 8, 24, 28, 28, 48, 12, 26, 26, 30,
        18, 22, 34, 34, 128, 64, 82, 184, 122,
    )
    expected_k1 = (
        4, 2, 8, 6, 8, 8, 20, 0, 8, 16, 18,
        14, 14, 22, 16, 44, 24, 24, 72, 52,
    )

    # Independent §32.3 denominator enumerator.  For Type I, a divisor d of
    # (Px)^2 must be P-free: then P does not divide y and P divides z.  We
    # apply this exact p-adic filter while generating divisors, rather than
    # generating the irrelevant P-divisible parts of the divisor list.
    limit = max(ground) + 1
    spf = list(range(limit + 1))
    for r in range(2, isqrt(limit) + 1):
        if spf[r] == r:
            for n in range(r * r, limit + 1, r):
                if spf[n] == n:
                    spf[n] = r

    def fac(n):
        out = []
        while n > 1:
            r, e = spf[n], 0
            while n % r == 0:
                n //= r
                e += 1
            out.append((r, e))
        return out

    def square_divisors_to_R(x, R):
        values = [1]
        for r, e0 in fac(x):
            new, power = [], 1
            for unused in range(2 * e0 + 1):
                new.extend(d * power for d in values if d * power <= R)
                power *= r
            values = new
        return values

    def denominator_rows(P):
        """Canonical primitive rows A<=B, with the p-denominator last."""
        rows = []
        for x in range(P // 4 + 1, 3 * P // 4 + 1):
            q, R = 4 * x - P, P * x
            for d in square_divisors_to_R(x, R):
                if (d + R) % q:
                    continue
                y = (R + d) // q
                if y < x or y % P == 0:
                    continue
                z = (R + R * R // d) // q
                if z < y or z % P:
                    continue
                assert 4 * x * y * z == P * (x * y + x * z + y * z)
                h0 = gcd(x, y)
                A, B = x // h0, y // h0
                C = z * h0 * h0 // (P * x * y)
                K = h0 // C
                assert (A, B) == (x // h0, y // h0) and gcd(A, B) == 1
                assert min(A, B, C, K) > 0
                assert P * (A + B) == K * (4 * A * B * C - 1)
                rows.append((A, B, C, K))
        assert len(rows) == len(set(rows))
        return tuple(rows)

    def square_multiplier_count(C):
        return prod(e // 2 + 1 for r, e in fac(C))

    canonical = {}
    got_raw, got_primitive, got_c1, got_k1 = [], [], [], []
    for P in ground:
        rows = denominator_rows(P)
        canonical[P] = rows
        orientations = lambda row: 1 if row[0] == row[1] else 2
        got_raw.append(sum(orientations(row) * square_multiplier_count(row[2])
                           for row in rows))
        got_primitive.append(sum(orientations(row) for row in rows))
        # c=1 occurs in the unique dilation g^2|C exactly when C is a square.
        got_c1.append(sum(orientations(row) for row in rows
                          if isqrt(row[2]) ** 2 == row[2]))
        # A raw k=1 row is necessarily primitive, so K=1 in the canonical row.
        got_k1.append(sum(orientations(row) for row in rows if row[3] == 1))
    assert tuple(got_raw) == expected_raw
    assert tuple(got_primitive) == expected_primitive
    assert tuple(got_c1) == (0,) * len(ground)
    assert tuple(got_k1) == expected_k1

    def ordinary_divisors(n):
        values = [1]
        for r, e in factorint(n).items():
            values = [d * r**j for d in values for j in range(e + 1)]
        return values

    def divisor_rows(P):
        """Theorem 26.1 enumeration, used only in the stated small range."""
        rows = []
        for K in range(1, 2 * P // 3 + 1):
            for C in range(1, (2 * P + K) // (4 * K) + 1):
                if gcd(P, C * K) != 1:
                    continue
                h0, norm = 4 * C * K, P * P + 4 * C * K * K
                for D in ordinary_divisors(norm):
                    if (D + P) % h0:
                        continue
                    E = norm // D
                    assert (E + P) % h0 == 0
                    A, B = (D + P) // h0, (E + P) // h0
                    rows.append((A, B, C, K))
                    # The hyperbolic/quadric identities (36.6)-(36.8)
                    # on the divisor rows (forward direction).
                    s, t, r = A + B, A - B, C * K * (A - B)
                    assert C * K * (s * s - t * t) == P * s + K
                    assert r * r == C * K * (C * K * s * s - P * s - K)
                    trace = 4 * C * K * s - 2 * P
                    assert trace == D + E
                    assert trace * trace - 4 * norm == (D - E) ** 2
        assert len(rows) == len(set(rows))
        return tuple(rows)

    def expanded_rows(rows):
        out = []
        for A, B, C, K in rows:
            gs = [1]
            for r, e in fac(C):
                gs = [g * r**j for g in gs for j in range(e // 2 + 1)]
            for g in gs:
                row = (g * A, g * B, C // (g * g), g * K)
                out.append(row)
                if A != B:
                    out.append((row[1], row[0], row[2], row[3]))
        return tuple(out)

    exact_limit = 100 if os.environ.get("ES_FULL_SCAN") == "1" else 50
    for P in primerange(3, exact_limit):
        drows = divisor_rows(P)
        erows = expanded_rows(denominator_rows(P))
        assert set(drows) == set(erows) and len(drows) == len(erows)
        c1_divisor = sum(row[2] == 1 for row in drows)
        # Gaussian slice count (36.10), written through rational norms
        # (the Gaussian-divisor bijection is proved in Theorem 36.2).
        c1_gaussian = 0
        for K in range(1, 2 * P // 3 + 1):
            norm, modulus = P * P + 4 * K * K, 4 * K
            c1_gaussian += sum((D + P) % modulus == 0
                               for D in ordinary_divisors(norm))
        assert c1_divisor == c1_gaussian
        if P % 4 == 1:
            assert c1_gaussian == 0

    # The k=1 divisor formula (36.12), without factoring the moving
    # values Pa+1: f=4ac-P is generated directly in its proved range.
    def k1_divisor_count(P):
        half = 0
        for A in range(1, P // 2 + 1):
            for C in range(P // (4 * A) + 1, P // (2 * A) + 1):
                f = 4 * A * C - P
                half += (P * A + 1) % f == 0
        return 2 * half

    assert tuple(k1_divisor_count(P) for P in ground) == expected_k1
    k1_failures = [P for P in primerange(3, 10_000)
                   if P % 24 == 1 and k1_divisor_count(P) == 0]
    assert k1_failures == [2521]

    # --- Genuine Dirichlet-character evaluation of (36.3), and the
    # independent (s,r)-point enumeration of (36.6). ---
    from cmath import exp as cexp, pi as cpi

    def phi_of(m):
        out = 1
        for pf, e in fac(m):
            out *= pf ** (e - 1) * (pf - 1)
        return out

    @lru_cache(None)
    def unit_characters(m):
        """All phi(m) Dirichlet characters mod m as dicts on units."""
        comps = []
        for pf, e in fac(m):
            pe = pf ** e
            if pf == 2:
                gens = [] if e == 1 else ([(3, 2)] if e == 2 else
                                          [(pe - 1, 2), (5, 2 ** (e - 2))])
            else:
                gens = [(primitive_root(pe), pe - pe // pf)]
            # brute-force discrete logs on this cyclic/2-generator part
            logs = {}
            if not gens:
                logs[1 % pe] = ()
            elif len(gens) == 1:
                g, n = gens[0]
                x = 1
                for t in range(n):
                    logs[x] = (t,)
                    x = x * g % pe
            else:
                (g1, n1), (g2, n2) = gens
                x1 = 1
                for t1 in range(n1):
                    x2 = x1
                    for t2 in range(n2):
                        logs[x2] = (t1, t2)
                        x2 = x2 * g2 % pe
                    x1 = x1 * g1 % pe
            comps.append((pe, gens, logs))
        # characters = products of one character per component
        def build(idx, chi):
            if idx == len(comps):
                out = {0: 0j}
                for u in range(1, m):
                    if gcd(u, m) == 1:
                        val = 1 + 0j
                        for (pe, gens, logs), phase in zip(comps, chi):
                            ts = logs[u % pe]
                            for t, (j, n) in zip(ts, phase):
                                val *= cexp(2j * cpi * j * t / n)
                        out[u] = val
                    else:
                        out[u] = 0j
                yield out
                return
            pe, gens, logs = comps[idx]
            orders = [n for _, n in gens]
            def phases(os):
                if not os:
                    yield ()
                    return
                for j in range(os[0]):
                    for rest in phases(os[1:]):
                        yield ((j, os[0]),) + rest
            for ph in phases(orders):
                yield from build(idx + 1, chi + [ph])
        return tuple(build(0, []))

    def character_mass(P):
        """Formula (36.3) with all phi(h) characters, complex floats."""
        total = 0j
        for K in range(1, 2 * P // 3 + 1):
            for C in range(1, (2 * P + K) // (4 * K) + 1):
                if gcd(P, C * K) != 1:
                    continue
                h0, norm = 4 * C * K, P * P + 4 * C * K * K
                ds = ordinary_divisors(norm)
                for chi in unit_characters(h0):
                    inner = sum(chi[D % h0] for D in ds)
                    total += chi[(-P) % h0].conjugate() * inner / phi_of(h0)
        return total

    def quadric_points(P):
        """Literal (s,r)-point count of (36.6), independent of divisors."""
        count = 0
        for K in range(1, 2 * P // 3 + 1):
            for C in range(1, (2 * P + K) // (4 * K) + 1):
                if gcd(P, C * K) != 1:
                    continue
                ck, norm = C * K, P * P + 4 * C * K * K
                for s in range(2, (norm + 1 + 2 * P) // (4 * ck) + 1):
                    val = ck * (ck * s * s - P * s - K)
                    if val < 0:
                        continue
                    r = isqrt(val)
                    if r * r != val or r % ck:
                        continue
                    if r >= ck * s or (s - r // ck) % 2:
                        continue
                    count += 1 if r == 0 else 2
        return count

    char_limit = 30
    for P in primerange(3, char_limit):
        drows = len(divisor_rows(P))
        assert quadric_points(P) == drows
        assert abs(character_mass(P) - drows) < 1e-6
    # r=0 points exist only for P = 3 mod 4 (D1-repair check): T_I(3)=3 odd.
    assert quadric_points(3) == 3

    # Genuine character evaluation of the k=1 formula (36.13).
    def k1_character_mass(P):
        total = 0j
        for A in range(1, P // 2 + 1):
            m4 = 4 * A
            fs = [f for f in ordinary_divisors(P * A + 1) if f <= P]
            for chi in unit_characters(m4):
                inner = sum(chi[f % m4] for f in fs)
                total += chi[(-P) % m4].conjugate() * inner / phi_of(m4)
        return 2 * total

    for P in (73, 193):
        assert abs(k1_character_mass(P) - k1_divisor_count(P)) < 1e-6

    # Hurwitz H(N): reduced (possibly imprimitive) positive forms of
    # discriminant -N, generic weight 1, and exceptional weights 1/2,1/3.
    @lru_cache(None)
    def hurwitz(N):
        if N == 0:
            return Q(-1, 12)
        if N < 0 or N % 4 not in (0, 3):
            return Q(0)
        ans = Q(0)
        for A in range(1, isqrt(N // 3) + 2):
            for B in range(-A, A + 1):
                discr = B * B + N
                if discr % (4 * A):
                    continue
                C = discr // (4 * A)
                if A > C or ((abs(B) == A or A == C) and B < 0):
                    continue
                if A == C and B == 0:
                    ans += Q(1, 2)
                elif A == C and B == A:
                    ans += Q(1, 3)
                else:
                    ans += 1
        return ans

    def kronecker_mass(n):
        radius = isqrt(4 * n)
        return sum((hurwitz(4 * n - t * t)
                    for t in range(-radius, radius + 1) if t * t <= 4 * n), Q(0))

    for n in range(2, 41):
        if isqrt(n) ** 2 != n:
            assert kronecker_mass(n) == sum(max(d, n // d)
                                             for d in ordinary_divisors(n))
    # A disciplined failed projection test: the unprojected Hurwitz mass
    # does not split uniformly among the phi(4ck) ray classes.
    P, C, K = 73, 10, 1
    norm, modulus = P * P + 4 * C * K * K, 4 * C * K
    ds = ordinary_divisors(norm)
    target = sorted(D for D in ds if (D + P) % modulus == 0)
    full_mass = sum(max(D, norm // D) for D in ds)
    target_mass = sum(max(D, norm // D) for D in target)
    assert kronecker_mass(norm) == full_mass == 13280
    assert target == [7, 767] and target_mass == 1534
    assert full_mass // 16 == 830 and target_mass != Q(full_mass, 16)
    # The tempting single-discriminant formula happens twice, then fails.
    assert 2 * hurwitz(4 * 73) == 8
    assert 2 * hurwitz(4 * 193) == 8
    assert 2 * hurwitz(4 * 241) == 24 != expected_primitive[2]

    print("ground Type-I raw/primitive counts =", (tuple(got_raw), tuple(got_primitive)))
    print("c=1 ground counts/k=1 hard failures <10^4 =",
          (tuple(got_c1), k1_failures))
    print("quadric exact range/Hurwitz projection failure =",
          (exact_limit, (norm, full_mass, target_mass)))
    print("character-sum (36.3)/(36.13) and (s,r)-quadric checks: exact",
          "below", char_limit, "and at k=1 for 73, 193")


print("\n== (ai) Type-I character mass and class-number audit (§36) ==")
check_ai()

# ---------------------------------------------------------------- (aj)
def check_aj():
    """Unit Y: residue-set transfer and composite factorial moments (§37)."""
    from math import comb, factorial

    def is_prime(n):
        return n >= 2 and factorint(n) == {n: 1}

    def intrinsic_residues(M):
        A = (M + 1) // 4
        return {(-4 * D) % M for D in divisors_of_square(A)}

    def merge_classes(d, a, M, b):
        """Return the exact merged CRT class, or None if incompatible."""
        g0 = gcd(d, M)
        if (b - a) % g0:
            return None
        M0 = M // g0
        t = 0 if M0 == 1 else ((b - a) // g0 * pow(d // g0, -1, M0)) % M0
        modulus = d * M0
        return modulus, (a + d * t) % modulus

    def composite_moments(X, z, reduced, degree=4):
        small_primes = list(primerange(2, z + 1))
        prime_residues = {
            p: intrinsic_residues(p)
            for p in primerange(z + 1, X + 1) if p % 4 == 3
        }
        atoms = []
        for M in range(3, X + 1, 4):
            factors = factorint(M)
            if M <= z or any(p in factors for p in small_primes) or is_prime(M):
                continue
            for residue in intrinsic_residues(M):
                if reduced and any(
                    p in prime_residues and residue % p in prime_residues[p]
                    for p in factors
                ):
                    continue
                atoms.append((M, residue))

        # dp[j][(d,a)] is the number of compatible j-subsets merging to a mod d.
        dp = [{(1, 0): 1}] + [{} for _ in range(degree)]
        for M, residue in atoms:
            for j in range(degree - 1, -1, -1):
                for (d, a), multiplicity in list(dp[j].items()):
                    merged = merge_classes(d, a, M, residue)
                    if merged is not None:
                        dp[j + 1][merged] = dp[j + 1].get(merged, 0) + multiplicity

        mu = sum((Fraction(1, M) for M, _ in atoms), Fraction())
        moments = [
            sum((Fraction(mult, d) for (d, _), mult in dp[j].items()), Fraction())
            for j in range(1, degree + 1)
        ]
        compatible_counts = [sum(dp[j].values()) for j in range(1, degree + 1)]
        return len(atoms), mu, moments, compatible_counts

    expected = {
        (80, 2, False): (
            42, Fraction(4246558, 3828825),
            [Fraction(4246558, 3828825), Fraction(253492, 348075),
             Fraction(19991, 60775), Fraction(138374, 1276275)],
            [42, 472, 1959, 4278],
        ),
        (80, 2, True): (
            14, Fraction(6038, 15015),
            [Fraction(6038, 15015), Fraction(1678, 15015),
             Fraction(268, 15015), Fraction(16, 15015)],
            [14, 50, 44, 16],
        ),
        (120, 3, False): (
            64, Fraction(4097396, 5311735),
            [Fraction(4097396, 5311735), Fraction(9887193, 37182145),
             Fraction(1863034, 37182145), Fraction(191091, 37182145)],
            [64, 1007, 2528, 2429],
        ),
        (120, 3, True): (
            34, Fraction(51538, 124355),
            [Fraction(51538, 124355), Fraction(10532, 124355),
             Fraction(64, 6545), Fraction(64, 124355)],
            [34, 284, 352, 64],
        ),
        (200, 5, False): (
            55, Fraction(7313, 17017),
            [Fraction(7313, 17017), Fraction(960, 17017),
             Fraction(43, 17017), Fraction(3, 17017)],
            [55, 634, 43, 3],
        ),
        (200, 5, True): (
            28, Fraction(3620, 17017),
            [Fraction(3620, 17017), Fraction(192, 17017), Fraction(0), Fraction(0)],
            [28, 192, 0, 0],
        ),
    }

    rows = []
    for key, want in expected.items():
        got = composite_moments(*key)
        assert got == want
        K, mu, moments, _ = got
        ratios = tuple(
            round(float(factorial(j) * moments[j - 1] / mu ** j), 3)
            for j in range(1, 5)
        )
        rows.append((key[0], key[1], "reduced" if key[2] else "raw",
                     K, round(float(mu), 5), ratios))

    # Exact residue-set rounding ledger: the low prime tensor at 3 and 7 has
    # 2*4=8 allowed classes modulo 21, and every interval error is <= 8.
    allowed = {
        n for n in range(21)
        if n % 3 not in intrinsic_residues(3)
        and n % 7 not in intrinsic_residues(7)
    }
    assert len(allowed) == 8
    for H in (0, 1, 5, 20, 100, 1000):
        actual = sum(m % 21 in allowed for m in range(1, H + 1))
        assert abs(Fraction(actual) - Fraction(H * len(allowed), 21)) <= len(allowed)

    # Replay the pointwise odd-Bonferroni identity used in (37.13).
    for r in (1, 3, 5, 7):
        for h in range(1, 25):
            assert sum((-1) ** j * comb(h, j) for j in range(r + 1)) == -comb(h - 1, r)

    print("composite moments (X,z,family,K,mu,j!e_j/mu^j) =", rows)
    print("residue-set tensor rho/modulus =", (len(allowed), 21),
          "; odd Bonferroni identity exact")


print("\n== (aj) Unit Y two-level hypergraph minorant (§37) ==")
check_aj()


# ---------------------------------------------------------------- (ak)
def check_ak():
    """Section 38: fixed-value binary maps and the k=2 -> k=1 hunt."""
    import os
    from collections import defaultdict
    from functools import lru_cache
    from math import isqrt
    from sympy import expand, symbols

    V0 = 5000

    @lru_cache(None)
    def divs(n):
        values = [1]
        for r, e in factorint(n).items():
            values = [d * r**j for d in values for j in range(e + 1)]
        return tuple(sorted(values))

    def value(row):
        a, b, c, k = row
        assert min(row) >= 1 and (a + b) % k == 0
        p = 4 * a * b * c - (a + b) // k
        assert p >= 2
        return p

    # Enumerate the whole finite box by AB <= V0/2.  Source indices retain
    # only rows in the same box; no source-pair Cartesian product is formed.
    by_value = defaultdict(list)
    by_vr = defaultdict(list)
    aux_pair = defaultdict(list)
    for a in range(1, V0 // 2 + 1):
        for b in range(1, V0 // (2 * a) + 1):
            den = 4 * a * b
            for k in divs(a + b):
                q = (a + b) // k
                c0 = max(1, (q + 2 + den - 1) // den)
                c1 = (V0 + q) // den
                for c in range(c0, c1 + 1):
                    p = den * c - q
                    row = (a, b, c, k)
                    assert value(row) == p
                    R = c * k
                    by_value[p].append(row)
                    by_vr[(p, R)].append(row)
                    aux_pair[(R, a, b)].append((row, p))

    assert len(by_value) == 4927
    assert sum(map(len, by_value.values())) == 188374

    adj = defaultdict(set)
    adj_small = defaultdict(set)
    outgoing, participating = set(), set()
    outgoing_small, participating_small = set(), set()
    moving_values, moving_values_small = set(), set()
    directed, directed_small = set(), set()
    branch_counts = Counter()
    branch_counts_small = Counter()

    def add_branches(p, fixed, out, others, kind, law_check):
        if not others:
            return
        moving_values.add(p)
        outgoing.add(fixed)
        participating.update((fixed, out))
        if fixed != out:
            adj[(p, fixed)].add(out)
            adj[(p, out)].add(fixed)
            directed.add((p, fixed, out))
        branch_counts[kind] += len(others)
        small = []
        for other, other_p in others:
            assert value(other) == other_p
            law_check(other, other_p)
            if other_p < p:
                small.append((other, other_p))
        if small:
            moving_values_small.add(p)
            outgoing_small.add(fixed)
            participating_small.update((fixed, out))
            if fixed != out:
                adj_small[(p, fixed)].add(out)
                adj_small[(p, out)].add(fixed)
                directed_small.add((p, fixed, out))
            branch_counts_small[kind] += len(small)

    for (p, R), fibre in by_vr.items():
        g = 4 * R
        for fixed in fibre:
            a, b, c, k = fixed
            assert c * k == R
            # The copied-coordinate maps cannot preserve their first input:
            # D=ga-1 and E=gb-1 are coprime to kP and exceed every possible
            # positive difference of two readings of R.
            D, E = g * a - 1, g * b - 1
            assert D * E == 1 + g * k * p
            assert gcd(D, k * p) == gcd(E, k * p) == 1
            assert D > R and E > R

            for out in fibre:
                A, B, C, j = out
                assert C * j == R

                # Preserve the first input under Phi_{++}.  The other two
                # first-input equations have no solutions by the check above.
                if A > a and B > b:
                    others = aux_pair.get((R, A - a, B - b), ())

                    def check_pp(other, other_p, A=A, B=B, j=j):
                        u, v, cc, ell = other
                        assert (A, B) == (a + u, b + v)
                        assert (j - k) * p == (ell * other_p
                                               + g * (a * v + u * b))
                        assert value((A, B, R // j, j)) == p

                    add_branches(p, fixed, out, others, "++", check_pp)

                # Preserve the second input of a copied-coordinate map.  The
                # auxiliary first source is recovered exactly from the output.
                if B > b:
                    others = aux_pair.get((R, A, B - b), ())

                    def check_1p(other, other_p, A=A, B=B, j=j):
                        x, y, cc, h = other
                        assert (A, B) == (x, y + b)
                        assert j * p == h * other_p + b * (g * x - 1)

                    add_branches(p, fixed, out, others, "1+@2", check_1p)
                if A > a:
                    others = aux_pair.get((R, A - a, B), ())

                    def check_p1(other, other_p, A=A, B=B, j=j):
                        x, y, cc, h = other
                        assert (A, B) == (x + a, y)
                        assert j * p == h * other_p + a * (g * y - 1)

                    add_branches(p, fixed, out, others, "+1@2", check_p1)

    assert branch_counts == {
        "++": 3822, "1+@2": 100042, "+1@2": 100042,
    }
    assert branch_counts_small == {
        "++": 3076, "1+@2": 78067, "+1@2": 78067,
    }
    assert (len(moving_values), len(outgoing), len(participating)) == (
        4895, 83357, 85333)
    assert (len(moving_values_small), len(outgoing_small),
            len(participating_small)) == (4813, 65462, 68218)
    assert sum(len(v) for v in adj.values()) // 2 == 78601
    assert sum(len(v) for v in adj_small.values()) // 2 == 66773

    def component_sizes(p, graph):
        seen, sizes = set(), []
        for start in by_value[p]:
            if start in seen:
                continue
            stack, size = [start], 0
            seen.add(start)
            while stack:
                row = stack.pop()
                size += 1
                for nxt in graph.get((p, row), ()):
                    if nxt not in seen:
                        seen.add(nxt)
                        stack.append(nxt)
            sizes.append(size)
        return sorted(sizes, reverse=True)

    selected = {
        # P: (#rows, #R, #components, max, isolated; smaller-source analog)
        73: (6, 2, 2, 4, 0, 3, 4, 2),
        241: (8, 4, 4, 2, 0, 6, 2, 4),
        409: (14, 6, 7, 4, 2, 14, 1, 14),
        577: (14, 7, 9, 2, 4, 13, 2, 12),
        1753: (36, 15, 20, 6, 10, 21, 6, 12),
        1873: (18, 7, 11, 6, 8, 11, 6, 8),
        2137: (32, 13, 17, 6, 8, 18, 6, 10),
        2161: (26, 8, 10, 8, 4, 12, 8, 8),
        3049: (22, 9, 15, 4, 12, 16, 4, 14),
        4441: (50, 19, 32, 8, 26, 32, 8, 26),
        4993: (42, 18, 27, 6, 18, 27, 6, 18),
    }
    for p, wanted in selected.items():
        cs, css = component_sizes(p, adj), component_sizes(p, adj_small)
        got = (len(by_value[p]),
               len({c * k for a, b, c, k in by_value[p]}),
               len(cs), max(cs), cs.count(1),
               len(css), max(css), css.count(1))
        assert got == wanted

    hard = [p for p in primerange(2, V0 + 1) if p % 24 == 1]
    assert len(hard) == 76
    assert sum(len(by_value[p]) for p in hard) == 1938
    assert sum(p in moving_values for p in hard) == 76
    assert sum(p in moving_values_small for p in hard) == 75
    assert not any(len(component_sizes(p, adj)) == 1 for p in hard)
    assert (sum(row in outgoing for p in hard for row in by_value[p]),
            sum(row in participating for p in hard for row in by_value[p]),
            sum(row in outgoing_small for p in hard for row in by_value[p]),
            sum(row in participating_small for p in hard for row in by_value[p])) == (
                1146, 1176, 936, 974)

    # The 2137 branch and its lack of a direct reverse branch.
    x = (2, 69, 4, 1)
    y = (1, 22, 4, 1)
    z = (3, 91, 2, 2)
    assert (value(x), value(y), value(z)) == (2137, 329, 2137)
    assert (2137, x, z) in directed and (2137, z, x) not in directed

    # Inverses do occur: every unequal tuple has an auxiliary K=1 source
    # realizing coordinate swap, and the swapped construction reverses it.
    for fixed in by_value[2137]:
        u, v, c, k = fixed
        if u == v:
            continue
        R = c * k
        if u > v:
            other = (v, u - v, R, 1)
            swapped = (v, u, c, k)       # Phi_{1+}(other,fixed)
        else:
            other = (v - u, u, R, 1)
            swapped = (v, u, c, k)       # Phi_{+1}(other,fixed)
        assert value(other) >= 2 and value(swapped) == value(fixed)
    assert (len(directed),
            sum((p, z0, x0) in directed for p, x0, z0 in directed),
            len(directed_small),
            sum((p, z0, x0) in directed_small
                for p, x0, z0 in directed_small)) == (
                144796, 132390, 118768, 103990)

    # Coordinate-ring replay for the only sparse-rational maps surviving the
    # §38 search: identity and A<->B.
    A, B, C, K, P = symbols("A B C K P")
    relation = 4 * A * B * C * K - A - B - K * P
    assert expand(relation) == expand(
        4 * B * A * C * K - B - A - K * P)

    # Type-I's genuine partial fixed-value scaling preserves both the equation
    # and its divisor factors; it only changes a nonprimitive presentation.
    type_i = (1, 1, 4, 2)
    scaled = (2, 2, 1, 4)
    p_i = 15
    for a, b, c, k in (type_i, scaled):
        assert p_i * (a + b) == k * (4 * a * b * c - 1)
    assert tuple(4 * a * type_i[2] * type_i[3] - p_i
                 for a in type_i[:2]) == tuple(
        4 * a * scaled[2] * scaled[3] - p_i for a in scaled[:2])

    # k=2 -> k=1 feature hunt.  Default replays the first finite range;
    # ES_FULL_SCAN=1 reruns the exact P<10^5 research census.
    def rows_with_k(p, wanted_k):
        rows = []
        for a in range(1, isqrt(p // 2) + 1):
            for b in range(a, p // (2 * a) + 1):
                c = p // (4 * a * b) + 1
                q = 4 * a * b * c - p
                if (a + b) % q:
                    continue
                k = (a + b) // q
                if k == wanted_k:
                    rows.append((a, b, c, k))
                    if a != b:
                        rows.append((b, a, c, k))
        return rows

    full = os.environ.get("ES_FULL_SCAN") == "1"
    bound = 100_000 if full else 1_000
    cases = []
    k1_count = k2_count = both_count = 0
    for p in primerange(2, bound):
        if p % 24 != 1:
            continue
        k1_rows = rows_with_k(p, 1)
        k2_rows = rows_with_k(p, 2)
        k1_count += bool(k1_rows)
        k2_count += bool(k2_rows)
        both_count += bool(k1_rows and k2_rows)
        if k1_rows and k2_rows:
            cases.extend((p, row, tuple(k1_rows)) for row in k2_rows)

    expected = ((1175, 1120, 1114, 10624) if full
                else (12, 12, 10, 34))
    assert (k1_count, k2_count, both_count, len(cases)) == expected

    def features(row):
        a, b, c, k = row
        return (1, a, b, c, a * b, a * c, b * c, a * b * c)

    # Every affine/bilinear expression has one or two of these eight features,
    # each nonzero coefficient in [-3,3]: 48 + C(8,2)*36 = 1056.
    polynomials = []
    for i in range(8):
        polynomials.extend(((i, coefficient),)
                           for coefficient in range(-3, 4) if coefficient)
    for i in range(8):
        for j in range(i + 1, 8):
            for ci in range(-3, 4):
                if not ci:
                    continue
                for cj in range(-3, 4):
                    if cj:
                        polynomials.append(((i, ci), (j, cj)))
    assert len(polynomials) == 1056

    feature_rows = [features(row) for p, row, targets in cases]
    target_sets = [
        [{target[j] for target in targets} for p, row, targets in cases]
        for j in range(3)
    ]
    compatible = [0, 0, 0]
    for polynomial in polynomials:
        alive = [True, True, True]
        for n, feature_row in enumerate(feature_rows):
            output = sum(coefficient * feature_row[i]
                         for i, coefficient in polynomial)
            if output <= 0:
                alive = [False, False, False]
                break
            for j in range(3):
                if alive[j] and output not in target_sets[j][n]:
                    alive[j] = False
            if not any(alive):
                break
        for j in range(3):
            compatible[j] += alive[j]
    assert compatible == [0, 0, 0]

    print("fixed-value V<=5000: tuples/branches/smaller branches =",
          (188374, sum(branch_counts.values()),
           sum(branch_counts_small.values())),
          "; graph edges/components at P=2137 =",
          (78601, len(component_sizes(2137, adj))))
    print("hard fibres <=5000: moves/smaller-source moves/connected =",
          (76, 75, 0), "; reversible directed edges =",
          (132390, 103990))
    print("k=2->k=1 two-feature box: bound/counts/candidates =",
          (bound, expected, len(polynomials)), "; universal coordinate hits =",
          compatible)


print("\n== (ak) fixed-value actions and k=2 -> k=1 hunt (§38) ==")
check_ak()


# ---------------------------------------------------------------- (al)
def check_al():
    """Exact toy companion for the c-free multiplier-prime assembly (§39)."""
    # Parse first, before constructing even the small finite atom family.
    import ast
    import os
    from pathlib import Path

    ast.parse(Path(__file__).read_text())

    # The genuine kappa<1/240 and H=K^10 have no nontrivial small instance.
    # kappa_toy=1/4 and H_toy=1 preserve only the structural congruences.
    X = 1200 if os.environ.get("ES_FULL_SCAN") == "1" else 625
    kappa_toy = Fraction(1, 4)
    K = 1
    while (K + 1) ** kappa_toy.denominator <= X:
        K += 1
    H_toy = 1

    def integer_cuberoot(n):
        z = 0
        while (z + 1) ** 3 <= n:
            z += 1
        return z

    atoms = []
    lower = int(X ** 0.5)
    while (lower + 1) ** 2 <= X:
        lower += 1
    while lower ** 2 > X:
        lower -= 1
    for ell in primerange(lower + 1, X + 1):
        if ell % 4 != 3:
            continue
        z = integer_cuberoot(ell)
        for k in range(1, K + 1, 4):
            A = (k * ell + 1) // 4
            for u in range(H_toy + 1, z + 1):
                for v in range(H_toy + 1, z + 1):
                    if gcd(u, v) != 1 or gcd(u * v, k) != 1:
                        continue
                    if A % (u * v):
                        continue
                    modulus = k * ell
                    residue = (-u * pow(v, -1, modulus)) % modulus
                    atoms.append((k, ell, u, v, modulus, residue))

    assert K >= 5 and 0 < len(atoms) < (1000 if X == 625 else 3000)

    # I1: the atom's k-part implies the moving c-fibre coupling.
    toy_M0 = 24 * lcm(*(range(1, K + 1, 4)))
    for k, ell, u, v, modulus, residue in atoms:
        n = residue + 2 * modulus
        c = n % toy_M0
        assert (u + n * v) % k == 0
        assert c % k == n % k and (u + c * v) % k == 0

    # Honest deduplication at k*ell and distinct ell-projections.
    modulus_classes = [(k, ell, residue) for k, ell, u, v, modulus, residue in atoms]
    assert len(modulus_classes) == len(set(modulus_classes))
    by_ell = {}
    for atom in atoms:
        by_ell.setdefault(atom[1], []).append(atom)
    for ell, rows in by_ell.items():
        projections = [row[5] % ell for row in rows]
        assert len(projections) == len(set(projections))

    compatible_pairs = dependent_pairs = 0
    delta = Fraction(0)
    for i, left in enumerate(atoms):
        for right in atoms[i + 1:]:
            g = gcd(left[4], right[4])
            compatible = (left[5] - right[5]) % g == 0
            if compatible:
                compatible_pairs += 1
                assert left[1] != right[1]
                if gcd(left[0], right[0]) > 1:
                    dependent_pairs += 1
                    delta += Fraction(1, lcm(left[4], right[4]))

    # Exact e_j without a Cartesian subset materialization.  At X<=1200 the
    # toy multipliers are exactly 1 and 5.  Process one ell-coordinate at a
    # time; a state records the common residue mod 5, if one is imposed.
    assert set(row[0] for row in atoms) == {1, 5}
    max_j = 4
    dp = {(0, None): Fraction(1)}
    for ell in sorted(by_ell):
        old = dp
        new = dict(old)  # choose no atom at this ell
        for (j, residue5), weight in old.items():
            if j == max_j:
                continue
            for k, ell0, u, v, modulus, residue in by_ell[ell]:
                assert ell0 == ell
                if k == 1:
                    next_residue = residue5
                    factor = Fraction(1, ell)
                else:
                    atom_residue5 = residue % 5
                    if residue5 is not None and residue5 != atom_residue5:
                        continue
                    next_residue = atom_residue5
                    factor = Fraction(1, 5 * ell) if residue5 is None else Fraction(1, ell)
                key = (j + 1, next_residue)
                new[key] = new.get(key, Fraction(0)) + weight * factor
        dp = new

    e = [sum(weight for (degree, state), weight in dp.items() if degree == j)
         for j in range(max_j + 1)]
    mu = sum(Fraction(1, row[4]) for row in atoms)
    assert e[0] == 1 and e[1] == mu
    ratios = [float(e[j] * prod(range(1, j + 1)) / mu ** j)
              for j in range(1, max_j + 1)]

    print("toy parameters X/kappa/K/H and atoms/classes/ells =",
          (X, str(kappa_toy), K, H_toy),
          (len(atoms), len(set(modulus_classes)), len(by_ell)))
    print("compatible/dependent pairs; mu, Delta/mu, Delta/mu^2 =",
          (compatible_pairs, dependent_pairs),
          tuple(round(value, 6) for value in
                (float(mu), float(delta / mu), float(delta / (mu * mu)))))
    print("exact j! e_j / mu^j for j=1..4 =",
          tuple(round(value, 6) for value in ratios))


print("\n== (al) c-free critical-window assembly toy (§39) ==")
check_al()

# ---------------------------------------------------------------- (am)
def check_am():
    """Section 40: exact residue dispersion for toy reduced composite systems."""
    import ast
    from collections import defaultdict

    # Keep an explicit syntax check in the companion requested for this wave.
    with open(__file__, encoding="utf-8") as source:
        ast.parse(source.read(), filename=__file__)

    def is_prime(n):
        return n >= 2 and factorint(n) == {n: 1}

    def intrinsic_representatives(M):
        """Least divisor representative for every distinct intrinsic class."""
        representatives = {}
        for D in divisors_of_square((M + 1) // 4):
            key = (-4 * D) % M
            representatives[key] = min(representatives.get(key, D), D)
        return representatives

    def radical_root(D):
        return prod(p ** ((e + 1) // 2) for p, e in factorint(D).items())

    def toy_dispersion(X, z, Y):
        # As in (aj), keep only composite z-rough moduli and delete every atom
        # implied by a prime-modulus atom.  Y is the toy low-prime tensor cutoff.
        prime_residues = {
            p: set(intrinsic_representatives(p))
            for p in primerange(z + 1, X + 1) if p % 4 == 3
        }
        atoms = []
        for M in range(3, X + 1, 4):
            factors = factorint(M)
            if is_prime(M) or any(p <= z for p in factors):
                continue
            beta = Fraction(1)
            for p in factors:
                if p <= Y and p in prime_residues:
                    beta *= Fraction(p, p - len(prime_residues[p]))
            for residue, D in intrinsic_representatives(M).items():
                if any(
                    p in prime_residues and residue % p in prime_residues[p]
                    for p in factors
                ):
                    continue
                atoms.append((M, residue, D, beta / M, tuple(factors)))

        u = defaultdict(lambda: defaultdict(Fraction))
        u_endpoint = defaultdict(lambda: defaultdict(Fraction))
        u_regular = defaultdict(lambda: defaultdict(Fraction))
        for M, residue, D, weight, factors in atoms:
            R = radical_root(D)
            k = ((M + 1) // 4) // R
            assert 4 * R * k - 1 == M
            for p in factors:
                if p <= z:
                    continue
                a = residue % p
                assert k % p == pow(4 * R, -1, p)
                u[p][a] += weight
                if k < p:
                    q = M // p
                    assert M == p * q and q > z and q < 4 * R
                    u_endpoint[p][a] += weight
                else:
                    u_regular[p][a] += weight

        def dispersion(vectors):
            return sum((
                p * sum((mass * mass for mass in by_residue.values()), Fraction())
                for p, by_residue in vectors.items()
            ), Fraction())

        exact = dispersion(u)
        endpoint = dispersion(u_endpoint)
        regular = dispersion(u_regular)
        t = {p: sum(by_residue.values(), Fraction()) for p, by_residue in u.items()}
        cauchy = sum((p * mass * mass for p, mass in t.items()), Fraction())
        assert exact <= cauchy

        # Ordered-pair expansion of p sum_a u_{p,a}^2, checked as rationals.
        pair_expansion = Fraction()
        for M, residue, _, weight, factors in atoms:
            for M1, residue1, _, weight1, factors1 in atoms:
                pair_expansion += weight * weight1 * sum(
                    p for p in set(factors).intersection(factors1)
                    if p > z and (residue - residue1) % p == 0
                )
        assert pair_expansion == exact
        assert exact >= endpoint + regular  # the omitted term is twice a nonnegative cross term
        return atoms, u, exact, cauchy, endpoint, regular, t

    cases = ((80, 2, 11), (120, 3, 13), (200, 5, 17))
    expected = {
        (80, 2, 11): (14, Fraction(127263, 135200), Fraction(1361, 676),
                      Fraction(54609, 67600), Fraction(289, 27040)),
        (120, 3, 13): (34, Fraction(48478967, 83463200),
                       Fraction(26229391, 10432900), Fraction(2371407, 5216450),
                       Fraction(353863, 16692640)),
        (200, 5, 17): (28, Fraction(168865, 781456), Fraction(64248, 48841),
                       Fraction(150469, 781456), Fraction(4651, 781456)),
    }
    rows = []
    last_u = None
    for X, z, Y in cases:
        atoms, u, exact, cauchy, endpoint, regular, t = toy_dispersion(X, z, Y)
        assert (len(atoms), exact, cauchy, endpoint, regular) == expected[(X, z, Y)]
        Lambda = log(X) ** 3 / log(log(X))
        harmonic_loss = sum(Fraction(1, p) for p in primerange(z + 1, X + 1))
        rows.append((
            X, z, Y, len(atoms), round(float(exact / Lambda ** 2), 7),
            round(float(cauchy / Lambda ** 2), 7),
            round(float(cauchy / exact), 3), round(float(endpoint / exact), 3),
            round(float(harmonic_loss), 3),
            tuple((p, round(float(t[p]), 5)) for p in sorted(t)),
        ))
        if X == 200:
            last_u = u

    # Exact additive-character Parseval spot check in Q(zeta_7).  Elements are
    # coefficient vectors in the basis 1,zeta,...,zeta^5, with
    # zeta^6=-(1+zeta+...+zeta^5).
    p = 7
    vector = [last_u[p].get(a, Fraction()) for a in range(p)]

    def zeta_power(exponent):
        exponent %= p
        if exponent == p - 1:
            return tuple(Fraction(-1) for _ in range(p - 1))
        value = [Fraction() for _ in range(p - 1)]
        value[exponent] = Fraction(1)
        return tuple(value)

    def add(left, right):
        return tuple(a + b for a, b in zip(left, right))

    def scale(scalar, value):
        return tuple(scalar * coefficient for coefficient in value)

    def multiply(left, right):
        value = tuple(Fraction() for _ in range(p - 1))
        for i, x in enumerate(left):
            for j, y in enumerate(right):
                if x and y:
                    value = add(value, scale(x * y, zeta_power(i + j)))
        return value

    transforms = []
    for h in range(p):
        value = tuple(Fraction() for _ in range(p - 1))
        for a, mass in enumerate(vector):
            value = add(value, scale(mass, zeta_power(h * a)))
        transforms.append(value)
    parseval = tuple(Fraction() for _ in range(p - 1))
    for h in range(p):
        parseval = add(parseval, multiply(transforms[h], transforms[-h % p]))
    target = [Fraction() for _ in range(p - 1)]
    target[0] = p * sum((mass * mass for mass in vector), Fraction())
    assert parseval == tuple(target)

    print("dispersion (X,z,Y,K,S/Lambda^2,Cauchy/Lambda^2,C/S,endpoint/S,sum1/p,t_p) =",
          rows)
    print("ordered-pair and Q(zeta_7) additive-character Parseval identities exact")


print("\n== (am) residue-dispersion companions (§40) ==")
check_am()

# ---------------------------------------------------------------- (an)
def check_an():
    """Unit R: independent atom, CRT-moment, and residue-profile stress."""
    import ast
    import os
    from collections import defaultdict
    from pathlib import Path

    ast.parse(Path(__file__).read_text(encoding="utf-8"), filename=__file__)

    # This is intentionally a fresh enumerator, independent of (al).  The
    # literal mode uses the §39 dyadic x^(1/6) cutoff.  The enlarged mode uses
    # ell^(1/3), solely to make more residue classes visible at toy scale.
    def root_floor(n, degree):
        value = int(n ** (1 / degree))
        while (value + 1) ** degree <= n:
            value += 1
        while value ** degree > n:
            value -= 1
        return value

    def build_atoms(X, K, H_toy=1, enlarged=False):
        blocks = []
        if enlarged:
            blocks.append((X ** 0.5, X, None))
        else:
            left = X ** 0.5
            while left < X:
                right = min(2 * left, X)
                blocks.append((left, right, int(left ** (1 / 6))))
                left = right

        atoms = []
        for left, right, block_z in blocks:
            for ell in primerange(int(left) + 1, int(right) + 1):
                if not left < ell <= right or ell % 4 != 3:
                    continue
                z = root_floor(ell, 3) if enlarged else block_z
                for k in range(1, K + 1, 4):
                    quotient = (k * ell + 1) // 4
                    for u in range(H_toy + 1, z + 1):
                        for v in range(H_toy + 1, z + 1):
                            if gcd(u, v) != 1 or gcd(u * v, k) != 1:
                                continue
                            if len(factorint(u * v)) > 6:  # inactive toy omega cutoff
                                continue
                            if quotient % (u * v):
                                continue
                            modulus = k * ell
                            residue = (-u * pow(v, -1, modulus)) % modulus
                            atoms.append((k, ell, u, v, modulus, residue))
        return atoms

    def multiplier_crt(L, residue, k, atom_residue):
        common = gcd(L, k)
        if (residue - atom_residue) % common:
            return None
        quotient = k // common
        shift = 0 if quotient == 1 else (
            (atom_residue - residue) // common
            * pow(L // common, -1, quotient)
        ) % quotient
        new_L = L * quotient
        return new_L, (residue + L * shift) % new_L

    def exact_moments(atoms, max_degree=6):
        # Process one ell fibre at a time, choosing zero or one atom.  A state
        # records only the compatible multiplier CRT class; no atom Cartesian
        # products are materialized.
        fibres = defaultdict(Counter)
        for k, ell, u, v, modulus, residue in atoms:
            fibres[ell][(k, residue % k)] += 1
        states = {(0, 1, 0): Fraction(1)}
        for ell, options in sorted(fibres.items()):
            updated = dict(states)
            for (degree, L, residue), weight in states.items():
                if degree == max_degree:
                    continue
                for (k, atom_residue), multiplicity in options.items():
                    merged = multiplier_crt(L, residue, k, atom_residue)
                    if merged is None:
                        continue
                    new_L, new_residue = merged
                    key = (degree + 1, new_L, new_residue)
                    updated[key] = updated.get(key, Fraction()) + (
                        weight * Fraction(multiplicity, ell)
                    )
            states = updated
        values = [
            sum((weight / L for (degree, L, residue), weight in states.items()
                 if degree == j), Fraction())
            for j in range(max_degree + 1)
        ]
        direct_mu = sum((Fraction(1, atom[4]) for atom in atoms), Fraction())
        assert values[0] == 1 and values[1] == direct_mu
        return values

    def audit_family(atoms, K, check_pair_sum=False, scan_pairs=True):
        by_ell = defaultdict(list)
        fibre_modulus = 24 * lcm(*range(1, K + 1, 4))
        for atom in atoms:
            k, ell, u, v, modulus, residue = atom
            by_ell[ell].append(atom)
            # S1 coupling, plus the complete multiplier identity on one hit.
            n = residue + 2 * modulus
            c = n % fibre_modulus
            assert (u + n * v) % k == 0 and (u + c * v) % k == 0
            w = (k * ell + 1) // (4 * u * v)
            s = (n * v + u) // modulus
            assert Fraction(4, n) == (
                Fraction(1, s * u * w)
                + Fraction(1, n * s * v * w)
                + Fraction(1, n * u * v * w)
            )

        for ell, rows in by_ell.items():
            projections = [row[5] % ell for row in rows]
            assert len(projections) == len(set(projections))

        compatible_pairs = 0
        pair_sum = Fraction()
        if scan_pairs:
            for index, left in enumerate(atoms):
                for right in atoms[index + 1:]:
                    common = gcd(left[4], right[4])
                    if (left[5] - right[5]) % common == 0:
                        compatible_pairs += 1
                        assert left[1] != right[1]
                        if check_pair_sum:
                            pair_sum += Fraction(1, lcm(left[4], right[4]))
        return len(by_ell), compatible_pairs, pair_sum

    def integer_divisors(n):
        return [d for d in range(1, n + 1) if n % d == 0]

    def profile_summary(atoms):
        rows_by_k = defaultdict(list)
        for atom in atoms:
            rows_by_k[atom[0]].append(atom)
        normalized = []
        for k, rows in rows_by_k.items():
            W_k = sum((Fraction(1, row[4]) for row in rows), Fraction())
            for g in integer_divisors(k):
                if g == 1:
                    continue
                units = [a for a in range(g) if gcd(a, g) == 1]
                phi_g = len(units)
                masses = defaultdict(Fraction)
                for row in rows:
                    masses[row[5] % g] += Fraction(1, row[4])
                for a in units:
                    normalized.append(float(phi_g * masses[a] / W_k))
        if not normalized:
            return (0, 0.0, 0.0, 0.0, 0.0)
        ordered = sorted(normalized)
        return (
            len(normalized),
            round(ordered[0], 3),
            round(ordered[len(ordered) // 2], 3),
            round(ordered[-1], 3),
            round(sum(abs(value - 1) for value in ordered) / len(ordered), 3),
        )

    # Literal dyadic families at the largest cheap toy scales.  Exact counts
    # pin the endpoint convention and make future changes visible.
    literal_cases = ((3000, 5), (6000, 9), (10000, 13))
    expected = {(3000, 5): (138, 69), (6000, 9): (330, 147),
                (10000, 13): (966, 409)}
    literal = {}
    moment_rows = []
    profile_rows = []
    coupling_atoms = compatible_total = 0
    for X, K in literal_cases:
        atoms = build_atoms(X, K)
        literal[(X, K)] = atoms
        ell_count, compatible_pairs, pair_sum = audit_family(
            atoms, K, check_pair_sum=(X == 3000)
        )
        assert (len(atoms), ell_count) == expected[(X, K)]
        moments = exact_moments(atoms)
        if X == 3000:
            assert moments[2] == pair_sum
        mu = moments[1]
        ratios = tuple(round(float(prod(range(1, j + 1)) * moments[j] / mu ** j), 6)
                       for j in range(1, 7))
        moment_rows.append(("literal", X, K, len(atoms), ell_count,
                            round(float(mu), 6), ratios))
        profile_rows.append(("literal", X, K, len(atoms), *profile_summary(atoms)))
        coupling_atoms += len(atoms)
        compatible_total += compatible_pairs

    # The enlarged family supplies many (k,g,a), including k=9, while keeping
    # the same arithmetic events.  It is a finite sparsity stress, not an
    # approximation to the dyadic asymptotic.
    enlarged_cases = ((3000, 5), (6000, 9), (10000, 13))
    enlarged = {}
    for X, K in enlarged_cases:
        atoms = build_atoms(X, K, enlarged=True)
        enlarged[(X, K)] = atoms
        audit_family(atoms, K, scan_pairs=False)
        coupling_atoms += len(atoms)
        profile_rows.append(("enlarged", X, K, len(atoms), *profile_summary(atoms)))

    unequal_power_atoms = build_atoms(3000, 9, enlarged=True)
    ell_count, compatible_pairs, _ = audit_family(unequal_power_atoms, 9)
    moments = exact_moments(unequal_power_atoms)
    mu = moments[1]
    moment_rows.append((
        "enlarged", 3000, 9, len(unequal_power_atoms), ell_count,
        round(float(mu), 6),
        tuple(round(float(prod(range(1, j + 1)) * moments[j] / mu ** j), 6)
              for j in range(1, 7)),
    ))
    coupling_atoms += len(unequal_power_atoms)
    compatible_total += compatible_pairs

    # Independent overlap regression against (al)'s documented parameters.
    overlap = build_atoms(625, 5, enlarged=True)
    overlap_classes = {(row[0], row[1], row[5]) for row in overlap}
    overlap_ells = {row[1] for row in overlap}
    assert (len(overlap), len(overlap_classes), len(overlap_ells)) == (134, 134, 34)

    if os.environ.get("ES_FULL_SCAN") == "1":
        heavy = enlarged[(10000, 13)]
        values = exact_moments(heavy)
        mu = values[1]
        moment_rows.append((
            "enlarged-full", 10000, 13, len(heavy), len({row[1] for row in heavy}),
            round(float(mu), 6),
            tuple(round(float(prod(range(1, j + 1)) * values[j] / mu ** j), 6)
                  for j in range(1, 7)),
        ))

    print("independent atom/moment rows (mode,X,K,atoms,ells,mu,j!e_j/mu^j j=1..6) =",
          moment_rows)
    print("W profile stress (mode,X,K,atoms,cells,min,median,max,mean|.-1|), normalized by 1/phi(g) =",
          profile_rows)
    print("S1/fixed-ell atoms checked and compatible pairs exhaustively scanned; (al) overlap =",
          (coupling_atoms, compatible_total),
          (len(overlap), len(overlap_classes), len(overlap_ells)))


print("\n== (an) Unit R independent construction stress (§41) ==")
check_an()


# ---------------------------------------------------------------- (ao)
def check_ao():
    """Section 42: sparse endpoint normal forms and exact collision census."""
    import ast
    import os
    from collections import defaultdict

    with open(__file__, encoding="utf-8") as source:
        ast.parse(source.read(), filename=__file__)

    def ao_is_prime(n):
        return n >= 2 and factorint(n) == {n: 1}

    def ao_representatives(M):
        representatives = {}
        for D in divisors_of_square((M + 1) // 4):
            residue = (-4 * D) % M
            representatives[residue] = min(representatives.get(residue, D), D)
        return representatives

    def ao_radical_root(D):
        return prod(r ** ((e + 1) // 2) for r, e in factorint(D).items())

    def ao_radical_divisors(R):
        values = [1]
        for r in factorint(R):
            values += [r * value for value in values]
        return values

    def ao_endpoint_system(X, z, Y):
        """Build the reduced toy system, then derive endpoints in two ways."""
        prime_residues = {
            p: set(ao_representatives(p))
            for p in primerange(z + 1, X + 1) if p % 4 == 3
        }
        retained = {}
        for M in range(3, X + 1, 4):
            factors = factorint(M)
            if ao_is_prime(M) or any(r <= z for r in factors):
                continue
            kappa = Fraction(1)
            for r in factors:
                if r <= Y and r in prime_residues:
                    kappa *= Fraction(r, r - len(prime_residues[r]))
            kept = set()
            for residue, D in ao_representatives(M).items():
                if any(
                    r in prime_residues and residue % r in prime_residues[r]
                    for r in factors
                ):
                    continue
                kept.add(D)
            retained[M] = (tuple(factors), kappa, kept)

        # Route 1: start from each retained (M,D) and inspect its prime factors.
        direct = []
        for M, (factors, kappa, kept) in retained.items():
            A = (M + 1) // 4
            for D in kept:
                R = ao_radical_root(D)
                s = R * R // D
                assert s in ao_radical_divisors(R) and A % R == 0
                c = A // R
                for p in factors:
                    if p <= z or c >= p:
                        continue
                    q = M // p
                    assert q > z and q < 4 * R
                    residue = (-4 * D) % p
                    assert residue == (-pow(4 * c * c * s, -1, p)) % p
                    direct.append((p, M, D, R, s, c, q, residue,
                                   kappa / M))

        # Route 2: for each (p,R), use the unique q in (0,4R).
        sparse = []
        max_R = (X + 1) // 4
        for p in primerange(z + 1, X + 1):
            for R in range(1, max_R + 1):
                if 4 * R <= z or gcd(p, 4 * R) != 1:
                    continue
                q = (-pow(p, -1, 4 * R)) % (4 * R)
                assert 0 < q < 4 * R and (p * q + 1) % (4 * R) == 0
                M = p * q
                if q <= z or M > X or M not in retained:
                    continue
                c = (M + 1) // (4 * R)
                if not (1 <= c < p):
                    continue
                factors, kappa, kept = retained[M]
                for s in ao_radical_divisors(R):
                    D = R * R // s
                    if D not in kept:
                        continue
                    residue = (-4 * D) % p
                    sparse.append((p, M, D, R, s, c, q, residue,
                                   kappa / M))
        assert sorted(direct) == sorted(sparse)

        by_p = defaultdict(list)
        for incidence in direct:
            by_p[incidence[0]].append(incidence)

        census = []
        endpoint_energy = Fraction()
        endpoint_diagonal = Fraction()
        max_kappa = max((kappa for _, kappa, _ in retained.values()),
                        default=Fraction(1))
        for p in sorted(by_p):
            rows = by_p[p]
            K = len(rows)
            assert len({row[2] for row in rows}) == K  # equal-D off-diagonal is absent
            masses = defaultdict(Fraction)
            buckets = defaultdict(list)
            total_mass = Fraction()
            for row in rows:
                _, _, D, _, s, c, q, residue, weight = row
                assert (c * c * s * 4 * residue + 1) % p == 0
                masses[residue] += weight
                buckets[residue].append(row)
                total_mass += weight
            assert total_mass <= max_kappa * K * Fraction(1, p * z)
            collisions = sum(len(bucket) * (len(bucket) - 1) // 2
                             for bucket in buckets.values())
            for bucket in buckets.values():
                for i in range(len(bucket)):
                    for j in range(i):
                        left, right = bucket[i], bucket[j]
                        assert left[2] != right[2]
                        assert (left[2] - right[2]) % p == 0
                        assert (left[5] ** 2 * left[4]
                                - right[5] ** 2 * right[4]) % p == 0
            energy_p = p * sum((mass * mass for mass in masses.values()),
                               Fraction())
            diagonal_p = p * sum((row[-1] ** 2 for row in rows), Fraction())
            assert diagonal_p <= energy_p
            endpoint_energy += energy_p
            endpoint_diagonal += diagonal_p
            census.append((p, K, collisions, K * (K - 1) // 2))

        return direct, by_p, tuple(census), endpoint_energy, endpoint_diagonal

    cases = [(80, 2, 11), (120, 3, 13), (200, 5, 17)]
    if os.environ.get("ES_FULL_SCAN") == "1":
        # Streaming residue buckets avoid an incidence Cartesian product.
        cases += [(400, 7, 23), (800, 11, 31)]

    expected = {
        (80, 2, 11): (
            25, ((3, 5, 10, 10), (5, 8, 9, 28), (7, 2, 0, 1),
                 (11, 6, 0, 15), (13, 4, 0, 6)),
            Fraction(54609, 67600), Fraction(49211, 135200)),
        (120, 3, 13): (
            59, ((5, 14, 23, 91), (7, 13, 22, 78), (11, 6, 0, 15),
                 (17, 12, 4, 66), (19, 14, 0, 91)),
            Fraction(2371407, 5216450), Fraction(17395877, 83463200)),
        (200, 5, 17): (
            51, ((7, 11, 15, 55), (11, 14, 8, 91), (13, 14, 4, 91),
                 (17, 12, 4, 66)),
            Fraction(150469, 781456), Fraction(71765, 781456)),
    }
    summaries = []
    final_by_p = None
    for X, z, Y in cases:
        incidences, by_p, census, energy, diagonal = ao_endpoint_system(X, z, Y)
        result = (len(incidences), census, energy, diagonal)
        if (X, z, Y) in expected:
            assert result == expected[(X, z, Y)]
        summaries.append((X, z, *result))
        if (X, z, Y) == (200, 5, 17):
            final_by_p = by_p

    # Exact endpoint Parseval check in Q(zeta_7), independently of block (am).
    p = 7
    vector = [Fraction() for _ in range(p)]
    for row in final_by_p[p]:
        vector[row[7]] += row[-1]

    def ao_zeta_power(exponent):
        exponent %= p
        if exponent == p - 1:
            return tuple(Fraction(-1) for _ in range(p - 1))
        value = [Fraction() for _ in range(p - 1)]
        value[exponent] = Fraction(1)
        return tuple(value)

    def ao_add(left, right):
        return tuple(x + y for x, y in zip(left, right))

    def ao_scale(scalar, value):
        return tuple(scalar * x for x in value)

    def ao_multiply(left, right):
        value = tuple(Fraction() for _ in range(p - 1))
        for i, x in enumerate(left):
            for j, y in enumerate(right):
                if x and y:
                    value = ao_add(value, ao_scale(x * y,
                                                   ao_zeta_power(i + j)))
        return value

    transforms = []
    for h in range(p):
        value = tuple(Fraction() for _ in range(p - 1))
        for residue, mass in enumerate(vector):
            value = ao_add(value, ao_scale(mass,
                                           ao_zeta_power(h * residue)))
        transforms.append(value)
    parseval = tuple(Fraction() for _ in range(p - 1))
    for h in range(p):
        parseval = ao_add(parseval,
                          ao_multiply(transforms[h], transforms[-h % p]))
    target = [Fraction() for _ in range(p - 1)]
    target[0] = p * sum((mass * mass for mass in vector), Fraction())
    assert parseval == tuple(target)

    printable = [
        (X, z, K, census, str(energy), str(diagonal))
        for X, z, K, census, energy, diagonal in summaries
    ]
    print("endpoint (X,z,incidences,(p,K,collisions,all-pairs),energy,diagonal) =",
          printable)
    print("unique-q, complement c^2*s collision, and Q(zeta_7) Parseval checks exact")


print("\n== (ao) short-cofactor endpoint companions (§42) ==")
check_ao()

# ---------------------------------------------------------------- (ap)
def check_ap():
    """Exact finite companions for the general-numerator transfer in §43."""
    import os
    from collections import defaultdict
    from random import Random
    from sympy import symbols, simplify

    # Symbolic cancellation in Lemma 43.1.  Substituting
    # m=(k*ell+1)/(u*v*w) should make the identity identically zero.
    n_s, k_s, ell_s, u_s, v_s, w_s = symbols(
        "n k ell u v w", nonzero=True)
    s_s = (n_s * v_s + u_s) / (k_s * ell_s)
    m_s = (k_s * ell_s + 1) / (u_s * v_s * w_s)
    rhs = (1 / (s_s * u_s * w_s)
           + 1 / (n_s * s_s * v_s * w_s)
           + 1 / (n_s * u_s * v_s * w_s))
    assert simplify(rhs - m_s / n_s) == 0

    def ap_divisors(value):
        result = [1]
        for prime, exponent in factorint(value).items():
            result = [d * prime ** e for d in result
                      for e in range(exponent + 1)]
        return sorted(result)

    # Hundreds of exact rational instances, including deliberately sought
    # even and composite representatives of each congruence class.
    rng = Random(430015)
    numerators = (3, 5, 6, 7, 8, 12, 25)
    exact_checks = 0
    even_checks = 0
    composite_checks = 0
    shared_factor_checks = 0
    per_m = Counter()
    for m in numerators:
        for _ in range(52):
            while True:
                ell = rng.randrange(2, 120)
                if gcd(ell, m) == 1:
                    break
            k0 = (-pow(ell, -1, m)) % m
            if k0 == 0:
                k0 = m
            k = k0 + m * rng.randrange(0, 8)
            assert (k * ell + 1) % m == 0
            A = (k * ell + 1) // m
            assert A > 0 and gcd(A, k * ell) == 1
            u = rng.choice(ap_divisors(A))
            remaining = A // u
            v = rng.choice(ap_divisors(remaining))
            w = remaining // v
            modulus = k * ell
            assert gcd(v, modulus) == 1
            residue = (-u * pow(v, -1, modulus)) % modulus
            candidates = [residue + j * modulus for j in range(1, 12)]
            n = rng.choice(candidates)
            # On alternating samples prefer an even or visibly composite n.
            if exact_checks % 2 == 0:
                preferred = [q for q in candidates if q % 2 == 0]
                if preferred:
                    n = preferred[0]
            else:
                preferred = [q for q in candidates
                             if any(q % p == 0 and q != p
                                    for p in (2, 3, 5, 7, 11))]
                if preferred:
                    n = preferred[0]
            assert n > 0 and (n * v + u) % modulus == 0
            s = (n * v + u) // modulus
            assert s > 0
            value = (Fraction(1, s * u * w)
                     + Fraction(1, n * s * v * w)
                     + Fraction(1, n * u * v * w))
            assert value == Fraction(m, n)
            exact_checks += 1
            per_m[m] += 1
            even_checks += (n % 2 == 0)
            composite_checks += (n > 3 and not bool(list(primerange(n, n + 1))))
            shared_factor_checks += (gcd(m, n) > 1)

    assert exact_checks == 52 * len(numerators)
    assert even_checks and composite_checks and shared_factor_checks

    # Structural atom census for m=5.  The extra 5uv>K condition is the
    # finite analogue of mH^2>K in Lemma 43.6 and makes k unique.
    toy_m, toy_K = 5, 24
    atoms = []
    for ell in primerange(41, 401):
        z = int(round(ell ** (1 / 3)))
        while (z + 1) ** 3 <= ell:
            z += 1
        while z ** 3 > ell:
            z -= 1
        for k in range(1, toy_K + 1):
            if gcd(k, toy_m) != 1 or (k * ell + 1) % toy_m:
                continue
            A = (k * ell + 1) // toy_m
            for u in range(2, z + 1):
                for v in range(2, z + 1):
                    if gcd(u, v) != 1 or gcd(u * v, k * ell) != 1:
                        continue
                    if toy_m * u * v <= toy_K or A % (u * v):
                        continue
                    residue = (-u * pow(v, -1, k * ell)) % (k * ell)
                    atoms.append((k, ell, u, v, residue, k * ell))

    assert atoms
    by_ell_residue = {}
    by_modulus_class = {}
    coupling_checks = 0
    ramified_atoms = 0
    for atom in atoms:
        k, ell, u, v, residue, modulus = atom
        assert (k * ell + 1) % (toy_m * u * v) == 0
        assert (residue * v + u) % k == 0
        assert (residue * v + u) % ell == 0
        coupling_checks += 1
        ramified_atoms += (gcd(toy_m, u * v) > 1)
        ell_key = (ell, residue % ell)
        assert ell_key not in by_ell_residue, (ell_key, atom,
                                               by_ell_residue.get(ell_key))
        by_ell_residue[ell_key] = atom
        modulus_key = (modulus, residue)
        assert modulus_key not in by_modulus_class
        by_modulus_class[modulus_key] = atom

    # Exercise the genuinely product-modulus case where m and uv overlap.
    assert ramified_atoms

    # Distinct atoms sharing ell cannot be CRT-compatible, since their ell
    # projections are distinct.  Check this without forming an all-atom
    # Cartesian array.
    ell_buckets = defaultdict(list)
    for atom in atoms:
        ell_buckets[atom[1]].append(atom)
    same_ell_pairs = 0
    for ell, bucket in ell_buckets.items():
        residues = set()
        for atom in bucket:
            residue = atom[4] % ell
            assert residue not in residues
            residues.add(residue)
        same_ell_pairs += len(bucket) * (len(bucket) - 1) // 2

    # Informational finite-range approach to the exact multiplier local
    # factor eta_2(m)=prod_{p|m} p^2/(p^2+p-1).  Ratios use the full
    # harmonic proxy sum as their finite-range normalizer.
    local_limit = 200_000 if os.environ.get("ES_FULL_SCAN") == "1" else 30_000
    phi = list(range(local_limit + 1))
    for p in range(2, local_limit + 1):
        if phi[p] == p:
            for j in range(p, local_limit + 1, p):
                phi[j] -= phi[j] // p
    weights = [0.0] * (local_limit + 1)
    total = 0.0
    for k in range(1, local_limit + 1):
        weight = (phi[k] * phi[k]) / (k * k * k)
        weights[k] = weight
        total += weight

    local_rows = []
    for m in (3, 5, 6, 8, 12, 25):
        eta = Fraction(1)
        for p in factorint(m):
            eta *= Fraction(p * p, p * p + p - 1)
        coprime_ratio = sum(weights[k] for k in range(1, local_limit + 1)
                            if gcd(k, m) == 1) / total
        class_ratios = []
        for residue in range(1, m + 1):
            if gcd(residue, m) == 1:
                class_ratios.append(sum(weights[k]
                                         for k in range(residue,
                                                        local_limit + 1, m))
                                    / total)
        local_rows.append((m, round(coprime_ratio, 6), round(float(eta), 6),
                           tuple(round(value, 6) for value in class_ratios),
                           round(float(eta) / sum(1 for r in range(1, m + 1)
                                                  if gcd(r, m) == 1), 6)))

    print("general-m identity exact/symbolic:", exact_checks,
          "rational instances; even/composite/shared(m,n) =",
          (even_checks, composite_checks, shared_factor_checks),
          "; per m =", dict(per_m))
    print("m=5 toy atoms/dedup/coupling/same-ell pairs/ramified =",
          (len(atoms), len(by_ell_residue), coupling_checks,
           same_ell_pairs, ramified_atoms))
    print("INFORMATIONAL eta_2 finite ratios",
          "(m,coprime actual/predicted,class ratios,predicted each) =", local_rows)


print("\n== (ap) general-numerator multiplier transfer (§43) ==")
check_ap()


# ---------------------------------------------------------------- (aq)
def check_aq():
    """§44: exact slice-vanishing grades and small-box conspiracies."""
    from collections import defaultdict
    from sympy import kronecker_symbol

    hard = tuple(p for p in primerange(2, 30_000) if p % 24 == 1)
    slices = tuple((c, k) for k in range(1, 31)
                   for c in range(1, 30 // k + 1))
    assert len(hard) == 385 and len(slices) == 111

    def squarefree_core(n):
        return prod(q for q, e in factorint(n).items() if e % 2)

    def grade_data(P, C, K):
        """Factor-box coefficient and an independent literal divisor list."""
        h = 4 * C * K
        norm = P * P + 4 * C * K * K
        factors = factorint(norm)
        coefficients = {1: 1}
        literal_divisors = [1]
        for q, e in factors.items():
            updated = defaultdict(int)
            power = 1
            for _ in range(e + 1):
                for residue, multiplicity in coefficients.items():
                    updated[residue * power % h] += multiplicity
                power = power * q % h
            coefficients = dict(updated)
            literal_divisors = [d * q**j for d in literal_divisors
                                for j in range(e + 1)]
        target = (-P) % h
        target_divisors = tuple(sorted(d for d in literal_divisors
                                       if d % h == target))
        # The group-ring coefficient in (44.3) is exactly the literal grade.
        assert coefficients.get(target, 0) == len(target_divisors)
        assert len(literal_divisors) == prod(e + 1 for e in factors.values())

        # Every surviving grade gives the exact Type-I row, and complementing
        # a divisor preserves the grade because norm == P^2 (mod h).
        for D in target_divisors:
            E = norm // D
            assert E % h == target
            A, B = (D + P) // h, (E + P) // h
            assert min(A, B) > 0
            assert P * (A + B) == K * (4 * A * B * C - 1)
        assert len(target_divisors) % 2 == 0
        return factors, target_divisors

    patterns = {}
    forced_wrong_grade = 0
    for P in hard:
        vanished = set()
        for C, K in slices:
            factors, target_divisors = grade_data(P, C, K)
            if not target_divisors:
                vanished.add((C, K))

            # Theorem 44.2: the four negative-norm genus characters exclude
            # the target whenever sf(C) is 1, 2, 3, or 6.
            core = squarefree_core(C)
            if core in (1, 2, 3, 6):
                assert not target_divisors
                for q in factors:
                    assert gcd(q, 4 * core) == 1
                    assert kronecker_symbol(-core, q) == 1
        patterns[P] = frozenset(vanished)

    forced_wrong_grade = sum(squarefree_core(C) in (1, 2, 3, 6)
                             for C, K in slices)
    assert forced_wrong_grade == 80

    depth_histogram = Counter(len(vanished) for vanished in patterns.values())
    expected_histogram = {
        99: 2, 100: 3, 101: 10, 102: 4, 103: 18, 104: 43, 105: 40,
        106: 43, 107: 55, 108: 55, 109: 64, 110: 33, 111: 15,
    }
    assert dict(sorted(depth_histogram.items())) == expected_histogram
    maximizers = tuple(P for P in hard if len(patterns[P]) == len(slices))
    assert maximizers == (
        2521, 9601, 12289, 13729, 15289, 18481, 19009, 20089,
        21121, 21169, 21841, 27361, 27481, 28921, 29569,
    )
    assert tuple(P for P in hard if len(patterns[P]) == 99) == (5953, 11353)

    cutoff_table = []
    for cutoff in (4, 5, 10, 15, 20, 25, 30):
        box = tuple((C, K) for C, K in slices if C * K <= cutoff)
        all_zero = sum(all(s in patterns[P] for s in box) for P in hard)
        cutoff_table.append((cutoff, len(box), all_zero))
    assert tuple(cutoff_table) == (
        (4, 8, 385), (5, 10, 220), (10, 27, 161), (15, 45, 63),
        (20, 66, 41), (25, 87, 30), (30, 111, 15),
    )

    # Corollary 44.3: D=3 forces the (5,1) slice on p == 97 (mod 120).
    progression = tuple(P for P in hard if P % 120 == 97)
    assert len(progression) == 95
    for P in progression:
        assert (P * P + 20) % 3 == 0 and (P + 3) % 20 == 0
        assert (5, 1) not in patterns[P]

    # Lemma 44.4: joint vanishing is not determined by the natural product
    # of the two ray moduli.  The exact factorizations expose the moving D.
    assert 193 % 840 == 1033 % 840
    assert (5, 1) in patterns[193] and (7, 1) in patterns[193]
    assert (5, 1) not in patterns[1033] and (7, 1) in patterns[1033]
    assert factorint(193**2 + 20) == {3: 2, 41: 1, 101: 1}
    assert factorint(193**2 + 28) == {37277: 1}
    assert factorint(1033**2 + 20) == {3: 1, 67: 1, 5309: 1}
    assert 67 % 20 == (-1033) % 20

    # The unique k=1 zero below 10^4 from §36 is a complete ck<=30
    # conspiracy, not merely an isolated k=1 failure.
    assert len(patterns[2521]) == 111

    print("hard primes/slices/wrong-grade-forced slices =",
          (len(hard), len(slices), forced_wrong_grade))
    print("all-zero (ck cutoff, slice count, hard-prime count) =", cutoff_table)
    print("vanishing-depth histogram =", dict(sorted(depth_histogram.items())))
    print("depth-111 primes =", maximizers,
          "; 2521 vanishes on all 111 slices")


print("\n== (aq) slice-conspiracy characterizations (§44) ==")
check_aq()


# ---------------------------------------------------------------- (ar)
def check_ar():
    """Section 45: exact joint Kloosterman matrix and coefficient norms."""
    import ast
    import os
    from collections import defaultdict

    with open(__file__, encoding="utf-8") as source:
        ast.parse(source.read(), filename=__file__)

    def ar_is_prime(n):
        return n >= 2 and factorint(n) == {n: 1}

    def ar_representatives(M):
        representatives = {}
        for D in divisors_of_square((M + 1) // 4):
            residue = (-4 * D) % M
            representatives[residue] = min(representatives.get(residue, D), D)
        return representatives

    def ar_radical_root(D):
        return prod(r ** ((e + 1) // 2) for r, e in factorint(D).items())

    def ar_build(X, z, Y):
        """Rebuild retained atoms, then form G[m,p] without pair arrays."""
        prime_residues = {
            p: set(ar_representatives(p))
            for p in primerange(z + 1, X + 1) if p % 4 == 3
        }
        retained = {}
        for M in range(3, X + 1, 4):
            factors = factorint(M)
            if ar_is_prime(M) or any(r <= z for r in factors):
                continue
            kappa = Fraction(1)
            for r in factors:
                if r <= Y and r in prime_residues:
                    kappa *= Fraction(r, r - len(prime_residues[r]))
            kept = set()
            for residue, D in ar_representatives(M).items():
                if any(
                    r in prime_residues and residue % r in prime_residues[r]
                    for r in factors
                ):
                    continue
                kept.add(D)
            retained[M] = (tuple(factors), kappa, kept)

        coefficients = defaultdict(lambda: defaultdict(Fraction))
        residue_masses = defaultdict(lambda: defaultdict(Fraction))
        squarefree_index = {}
        edge_l2_squared = Fraction()
        incidences = 0
        for M, (factors, kappa, kept) in retained.items():
            A = (M + 1) // 4
            for D in kept:
                R = ar_radical_root(D)
                s = R * R // D
                assert all(e == 1 for e in factorint(s).values())
                assert A % R == 0
                c = A // R
                m = 4 * c * c * s
                previous = squarefree_index.setdefault(m, (c, s))
                assert previous == (c, s)  # uniqueness of m/4 = c^2 s
                for p in factors:
                    if p <= z or c >= p:
                        continue
                    q = M // p
                    assert q > z and q < 4 * R and M <= X
                    assert all(r > z for r in factorint(q))
                    assert gcd(m, M) == 1 and 4 <= m < p * (X + 1)
                    residue = (-pow(m, -1, p)) % p
                    assert residue == (-4 * D) % p
                    coefficient = kappa / q
                    coefficients[p][m] += coefficient
                    residue_masses[p][residue] += kappa / M
                    edge_l2_squared += coefficient * coefficient
                    incidences += 1

                    # Both exact orientations in (45.5), checked in Q/Z.
                    for h in (1, p - 1):
                        phase_p = Fraction(-h * pow(m, -1, p), p)
                        phase_M = Fraction(-h * q * pow(m, -1, M), M)
                        phase_recip = (Fraction(h * pow(p, -1, m), m)
                                       - Fraction(h, m * p))
                        assert (phase_p - phase_M).denominator == 1
                        assert (phase_p - phase_recip).denominator == 1

        direct_energy = sum(
            p * sum((mass * mass for mass in buckets.values()), Fraction())
            for p, buckets in residue_masses.items()
        )
        bilinear_energy = Fraction()
        l1 = Fraction()
        l2_squared = Fraction()
        weighted_frobenius = Fraction()
        cells = 0
        for p, row in coefficients.items():
            inverse_buckets = defaultdict(Fraction)
            for m, coefficient in row.items():
                inverse_buckets[(-pow(m, -1, p)) % p] += coefficient
                l1 += coefficient
                l2_squared += coefficient * coefficient
                weighted_frobenius += coefficient * coefficient / p
                cells += 1
            # Exact h-orthogonality in the bilinearized form (45.3).
            bilinear_energy += sum(
                (coefficient * coefficient / p
                 for coefficient in inverse_buckets.values()), Fraction()
            )
        assert bilinear_energy == direct_energy
        assert l2_squared >= edge_l2_squared
        return (incidences, cells, direct_energy, l1, l2_squared,
                edge_l2_squared, weighted_frobenius)

    cases = [(80, 2, 11), (120, 3, 13), (200, 5, 17)]
    if os.environ.get("ES_FULL_SCAN") == "1":
        cases += [(400, 7, 23), (800, 11, 31)]
    expected = {
        (80, 2, 11): (
            25, 23, Fraction(54609, 67600), Fraction(1897, 260),
            Fraction(378617, 135200), Fraction(352357, 135200),
            Fraction(55711, 135200)),
        (120, 3, 13): (
            59, 57, Fraction(2371407, 5216450), Fraction(17286, 1615),
            Fraction(201997063, 83463200), Fraction(194884603, 83463200),
            Fraction(18474697, 83463200)),
        (200, 5, 17): (
            51, 51, Fraction(150469, 781456), Fraction(6509, 884),
            Fraction(485259, 390728), Fraction(485259, 390728),
            Fraction(71765, 781456)),
    }

    rows = []
    for case in cases:
        values = ar_build(*case)
        if case in expected:
            assert values == expected[case]
        rows.append((*case, values[0], values[1],
                     *(str(value) for value in values[2:])))

    print("joint matrix (X,z,Y,incidences,cells,V,l1,l2^2,edge-l2^2,sum l2_p^2/p) =",
          rows)
    print("endpoint residue energy = exact Kloosterman-matrix Parseval energy; reciprocity exact")


print("\n== (ar) moving-s Kloosterman-matrix audit (§45) ==")
check_ar()

# ---------------------------------------------------------------- (as)
def check_as():
    """Section 46: exact endpoint-bulk corner decomposition."""
    import ast
    import os
    from collections import defaultdict

    with open(__file__, encoding="utf-8") as source:
        ast.parse(source.read(), filename=__file__)

    def as_is_prime(n):
        return n >= 2 and factorint(n) == {n: 1}

    def as_representatives(M):
        representatives = {}
        for D in divisors_of_square((M + 1) // 4):
            residue = (-4 * D) % M
            representatives[residue] = min(representatives.get(residue, D), D)
        return representatives

    def as_radical_root(D):
        return prod(r ** ((e + 1) // 2) for r, e in factorint(D).items())

    def as_block(m, cutoff):
        """j for cutoff*2^j < m <= cutoff*2^(j+1)."""
        assert m > cutoff
        return ((m - 1) // cutoff).bit_length() - 1

    def as_build(X, z, Y):
        """Build G[m,p], then split its residue energy without pair arrays."""
        prime_residues = {
            p: set(as_representatives(p))
            for p in primerange(z + 1, X + 1) if p % 4 == 3
        }
        retained = {}
        for M in range(3, X + 1, 4):
            factors = factorint(M)
            if as_is_prime(M) or any(r <= z for r in factors):
                continue
            kappa = Fraction(1)
            for r in factors:
                if r <= Y and r in prime_residues:
                    kappa *= Fraction(r, r - len(prime_residues[r]))
            kept = set()
            for residue, D in as_representatives(M).items():
                if any(
                    r in prime_residues and residue % r in prime_residues[r]
                    for r in factors
                ):
                    continue
                kept.add(D)
            retained[M] = (tuple(factors), kappa, kept)

        coefficients = defaultdict(lambda: defaultdict(Fraction))
        cell_parameters = {}
        for M, (factors, kappa, kept) in retained.items():
            A = (M + 1) // 4
            for D in kept:
                R = as_radical_root(D)
                s = R * R // D
                assert A % R == 0
                c = A // R
                m = 4 * c * c * s
                assert cell_parameters.setdefault(m, (c, s)) == (c, s)
                for p in factors:
                    if p <= z or c >= p:
                        continue
                    q = M // p
                    assert q > z and q < 4 * R and gcd(m, M) == 1
                    coefficients[p][m] += kappa / q

        # The finite analogue of W_1=z L^2/log L in (46.8).
        cutoff = max(4, int(z * log(X) ** 2 / log(log(X))))
        pieces = defaultdict(Fraction)
        open_cells = closed_cells = 0
        for p, row in coefficients.items():
            buckets = defaultdict(list)
            for m, coefficient in row.items():
                c, _ = cell_parameters[m]
                closed = m <= cutoff or (c >= z and m <= z * cutoff)
                buckets[(-pow(m, -1, p)) % p].append(
                    (m, coefficient, closed))
                if closed:
                    closed_cells += 1
                else:
                    open_cells += 1

            for cells in buckets.values():
                closed_sum = sum((g for _, g, closed in cells if closed),
                                 Fraction())
                open_rows = [(m, g) for m, g, closed in cells if not closed]
                open_sum = sum((g for _, g in open_rows), Fraction())
                open_diagonal = sum((g * g for _, g in open_rows), Fraction())
                block_sums = defaultdict(Fraction)
                block_squares = defaultdict(Fraction)
                for m, g in open_rows:
                    j = as_block(m, cutoff)
                    block_sums[j] += g
                    block_squares[j] += g * g
                local = sum((block_sums[j] ** 2 - block_squares[j]
                             for j in block_sums), Fraction())
                far = open_sum ** 2 - sum(
                    (value * value for value in block_sums.values()), Fraction())
                assert local >= 0 and far >= 0

                pieces["closed"] += closed_sum ** 2 / p
                pieces["mixed"] += 2 * closed_sum * open_sum / p
                pieces["open-diagonal"] += open_diagonal / p
                pieces["open-local"] += local / p
                pieces["open-far"] += far / p
                pieces["total"] += (closed_sum + open_sum) ** 2 / p

            # Arithmetic-progression occupancies used in Lemmas 46.3--46.4.
            prefix_counts = Counter(m % p for m in row if m <= cutoff)
            assert max(prefix_counts.values(), default=0) <= (cutoff + p - 1) // p
            block_counts = defaultdict(Counter)
            for m in row:
                if m > cutoff:
                    block_counts[as_block(m, cutoff)][m % p] += 1
            for j, counts in block_counts.items():
                width = cutoff * 2 ** j
                assert max(counts.values(), default=0) <= width // p + 1

        assert pieces["total"] == sum(
            (pieces[name] for name in
             ("closed", "mixed", "open-diagonal", "open-local", "open-far")),
            Fraction())
        assert (pieces["open-diagonal"] + pieces["open-local"]
                + pieces["open-far"] >= 0)
        return (cutoff, closed_cells, open_cells,
                *(pieces[name] for name in
                  ("closed", "mixed", "open-diagonal", "open-local",
                   "open-far", "total")))

    cases = [(80, 2, 11), (120, 3, 13), (200, 5, 17)]
    if os.environ.get("ES_FULL_SCAN") == "1":
        cases += [(400, 7, 23), (800, 11, 31)]

    expected = {
        (80, 2, 11): (
            25, 12, 11, Fraction(16681, 33800), Fraction(5277, 27040),
            Fraction(14419, 135200), Fraction(0), Fraction(1, 80),
            Fraction(54609, 67600)),
        (120, 3, 13): (
            43, 28, 29, Fraction(735841, 3338528),
            Fraction(1062997, 8346320), Fraction(6819677, 83463200),
            Fraction(0), Fraction(2759, 109820),
            Fraction(2371407, 5216450)),
        (200, 5, 17): (
            84, 30, 21, Fraction(7635, 91936), Fraction(95917, 1562912),
            Fraction(29501, 781456), Fraction(0), Fraction(3, 289),
            Fraction(150469, 781456)),
        (400, 7, 23): (
            140, 50, 34, Fraction(1149696311, 18401725888),
            Fraction(13756187, 445716544),
            Fraction(2612018711, 128812081216), Fraction(1, 832),
            Fraction(203263, 36428756),
            Fraction(1938623889, 16101510152)),
        (800, 11, 31): (
            258, 151, 150,
            Fraction(77161480892545741127118439,
                     2107339042676052674803557152),
            Fraction(198624380002352137829660547,
                     8429356170704210699214228608),
            Fraction(313024080491417457652016507,
                     16858712341408421398428457216),
            Fraction(17451321, 15854098624),
            Fraction(70610715947907451031165,
                     7855877139519301676807296),
            Fraction(1497652428663746795066282367,
                     16858712341408421398428457216)),
    }
    rows = []
    for case in cases:
        values = as_build(*case)
        if case in expected:
            assert values == expected[case]
        # Cross-check the total against the independently fixed §45 values.
        known_total = {
            (80, 2, 11): Fraction(54609, 67600),
            (120, 3, 13): Fraction(2371407, 5216450),
            (200, 5, 17): Fraction(150469, 781456),
        }
        if case in known_total:
            assert values[-1] == known_total[case]
        rows.append((*case, values[0], values[1], values[2],
                     *(str(value) for value in values[3:])))

    print("bulk corners (X,z,Y,W1,closed cells,open cells,"
          "closed,mixed,open diag,open local,open far,total) =", rows)
    print("five rational corners resum exactly; no incidence Cartesian arrays")


print("\n== (as) endpoint-bulk collision audit (§46) ==")
check_as()


# ---------------------------------------------------------------- (at)
def check_at():
    """Section 47: exact conditional codegrees and the divisor-cube wall."""
    import os
    from functools import lru_cache

    def is_prime(n):
        return n >= 2 and factorint(n) == {n: 1}

    def intrinsic_representatives(M):
        representatives = {}
        for D in divisors_of_square((M + 1) // 4):
            residue = (-4 * D) % M
            representatives[residue] = min(representatives.get(residue, D), D)
        return representatives

    def merge_classes(d, a, M, b):
        common = gcd(d, M)
        if (a - b) % common:
            return None
        quotient = M // common
        shift = 0 if quotient == 1 else (
            (b - a) // common * pow(d // common, -1, quotient)
        ) % quotient
        modulus = d * quotient
        return modulus, (a + d * shift) % modulus

    def build_complete_H(X, z, Y):
        prime_residues = {
            p: set(intrinsic_representatives(p))
            for p in primerange(z + 1, X + 1) if p % 4 == 3
        }
        low = {p: len(classes) for p, classes in prime_residues.items() if p <= Y}
        atoms = []

        # Prime atoms above the tensor cutoff are counted by H.
        for p, classes in prime_residues.items():
            if p > Y:
                for residue in classes:
                    atoms.append((p, residue, dict(factorint(p)), "prime"))

        # Composite atoms use exactly the §37/§40 prime-implied deletion.
        for M in range(3, X + 1, 4):
            factors = dict(factorint(M))
            if is_prime(M) or any(p <= z for p in factors):
                continue
            for residue in intrinsic_representatives(M):
                if any(
                    p in prime_residues
                    and residue % p in prime_residues[p]
                    for p in factors
                ):
                    continue
                atoms.append((M, residue, factors, "composite"))
        return atoms, low

    def hierarchy_audit(X, z, Y, degree):
        atoms, low = build_complete_H(X, z, Y)

        @lru_cache(None)
        def factors(n):
            return dict(factorint(n))

        @lru_cache(None)
        def conditional_probability(modulus):
            probability = Fraction(1, modulus)
            for p, forbidden in low.items():
                if modulus % p == 0:
                    probability *= Fraction(p, p - forbidden)
            return probability

        mu = sum((conditional_probability(M) for M, *_ in atoms), Fraction())
        states = [((), 1, 0)]
        state_counts = []
        maxima = []
        extension_counts = [0, 0, 0]
        maximum_ratio = Fraction()

        # Every compatible subset is generated once, with early CRT pruning.
        for depth in range(1, degree + 1):
            next_states = []
            for indices, modulus, residue in states:
                start = indices[-1] + 1 if indices else 0
                for index in range(start, len(atoms)):
                    merged = merge_classes(
                        modulus, residue, atoms[index][0], atoms[index][1]
                    )
                    if merged is not None:
                        next_states.append((indices + (index,), *merged))
            states = next_states
            state_counts.append(len(states))
            ell_values = []

            for indices, modulus, residue in states:
                old_factors = factors(modulus)
                selected = set(indices)
                split = [Fraction(), Fraction(), Fraction()]
                for index, (M, atom_residue, new_factors, _) in enumerate(atoms):
                    if index in selected:
                        continue
                    merged = merge_classes(modulus, residue, M, atom_residue)
                    if merged is None:
                        continue

                    shared = old_factors.keys() & new_factors.keys()
                    if not shared:
                        category = 0
                    elif any(new_factors[p] > old_factors[p] for p in shared):
                        category = 2
                    else:
                        category = 1

                    ratio = (conditional_probability(merged[0])
                             / conditional_probability(modulus))
                    local_ratio = Fraction(1)
                    for p, exponent in new_factors.items():
                        old_exponent = old_factors.get(p, 0)
                        if old_exponent:
                            local_ratio /= p ** max(exponent - old_exponent, 0)
                        elif p in low:
                            local_ratio /= p ** (exponent - 1) * (p - low[p])
                        else:
                            local_ratio /= p ** exponent
                    assert ratio == local_ratio       # (47.4)--(47.5)
                    split[category] += ratio
                    extension_counts[category] += 1

                ell = sum(split, Fraction())
                assert ell == split[0] + split[1] + split[2]  # (47.7)
                ell_values.append(ell)
                maximum_ratio = max(maximum_ratio, ell / mu)
            maxima.append(max(ell_values))

        return (len(atoms), mu, tuple(state_counts), tuple(maxima),
                maximum_ratio, tuple(extension_counts))

    # A complete toy H: every compatible S through degree four and every
    # possible extension B are checked, all in exact rational arithmetic.
    toy = hierarchy_audit(40, 2, 7, 4)
    expected_toy = (
        28,
        Fraction(27839083, 19372210),
        (28, 316, 1868, 6217),
        (Fraction(6342705, 3874442), Fraction(295533, 149017),
         Fraction(14316, 7843), Fraction(421, 253)),
        Fraction(38419290, 27839083),
        (73548, 14916, 0),
    )
    assert toy == expected_toy

    # Exact finite member of Theorem 47.2.  These are atoms of the complete
    # X=5655 system; only this extracted divisor cube is enumerated here.
    q, ps = 3, (5, 13, 29)
    top_modulus = q * prod(ps)
    cube = []
    for size in (1, 3):
        for chosen in combinations(ps, size):
            M = q * prod(chosen)
            residue = (-8) % M
            assert M % 8 == 7
            assert intrinsic_representatives(M)[residue] == 2
            assert residue % q not in intrinsic_representatives(q)
            cube.append((M, residue))
    assert len(cube) == 4 and top_modulus == 5655
    top = (top_modulus, (-8) % top_modulus)
    cube_extension = Fraction()
    for M, residue in cube:
        if M == top_modulus:
            continue
        merged = merge_classes(top[0], top[1], M, residue)
        assert merged == top
        cube_extension += Fraction(1)  # P(top intersect B) / P(top)
    assert cube_extension == 3

    # Both prime-power corners in §47.3 are retained in the actual system.
    prime_residues = {
        p: set(intrinsic_representatives(p)) for p in (7, 11, 31)
    }
    for M, D, residue in (
        (119, 3, 107), (539, 675, 534),
        (539, 27, 431), (1519, 76, 1215),
    ):
        assert (-4 * D) % M == residue
        for p in factorint(M):
            if p % 4 == 3:
                assert residue % p not in prime_residues[p]

    # Condition only at 7, where f(7)=3 and theta_7=4.
    assert len(prime_residues[7]) == 3

    def conditioned_at_7(modulus):
        probability = Fraction(1, modulus)
        if modulus % 7 == 0:
            probability *= Fraction(7, 4)
        return probability

    higher = merge_classes(119, 107, 539, 534)
    assert higher is not None and factorint(119)[7] < factorint(539)[7]
    assert conditioned_at_7(higher[0]) / conditioned_at_7(119) == Fraction(1, 77)
    assert conditioned_at_7(539) * 4 == Fraction(1, 77)

    equal_power = merge_classes(539, 431, 1519, 1215)
    assert equal_power is not None and gcd(539, 1519) == 49
    assert 431 % 49 == 1215 % 49 == 39
    assert conditioned_at_7(equal_power[0]) / conditioned_at_7(539) == Fraction(1, 31)
    assert conditioned_at_7(1519) * 28 == Fraction(1, 31)
    assert 28 == 49 * (7 - len(prime_residues[7])) // 7

    # The larger complete composite toy exhibits both <= and > categories;
    # keep its 99,362 compatible triples behind the requested full-scan gate.
    if os.environ.get("ES_FULL_SCAN") == "1":
        full = hierarchy_audit(550, 5, 550, 3)
        assert full == (
            136,
            Fraction(1327039027, 1697425912),
            (136, 5998, 99362),
            (Fraction(2021864469, 1697425912),
             Fraction(283588275, 130571224),
             Fraction(25140620, 7316491)),
            Fraction(5832623840, 1327039027),
            (1890096, 1001762, 32184),
        )

    print("complete hierarchy toy (K,mu,compatible counts,max ell,C_toy,categories) =",
          toy)
    print("Lambda_toy := mu; exact max ell <= C_toy Lambda_toy with C_toy =",
          toy[4], "; divisor-cube contribution =", cube_extension)
    print("higher/equal prime-power extension ratios =", Fraction(1, 77),
          Fraction(1, 31), "; all structure splits exact")


print("\n== (at) complete-system codegree hierarchy (§47) ==")
check_at()


# ---------------------------------------------------------------- (au)
def check_au():
    """§48: unforced-slice census, conspiracy depth, and fixed guarantees."""
    import os
    from collections import defaultdict
    from math import sqrt
    from sympy import kronecker_symbol

    scan_limit = 100_000 if os.environ.get("ES_FULL_SCAN") == "1" else 30_000
    hard_all = tuple(p for p in primerange(2, scan_limit) if p % 24 == 1)
    census_hard = tuple(p for p in hard_all if p < 30_000)
    assert len(census_hard) == 385
    if scan_limit == 100_000:
        assert len(hard_all) == 1181

    core_cache = {}

    def squarefree_core(n):
        if n not in core_cache:
            core_cache[n] = prod(q for q, e in factorint(n).items() if e % 2)
        return core_cache[n]

    forced_cores = {1, 2, 3, 6}
    box_slices = tuple((c, k) for k in range(1, 31)
                       for c in range(1, 30 // k + 1))
    unforced = tuple((c, k) for c, k in box_slices
                     if squarefree_core(c) not in forced_cores)
    assert len(box_slices) == 111 and len(unforced) == 31
    assert sum(squarefree_core(c) in forced_cores
               for c, k in box_slices) == 80

    hit_cache = {}

    def slice_hit(P, C, K):
        """Exact bounded exponent-box test, storing only residues modulo 4CK."""
        key = (P, C, K)
        if key in hit_cache:
            return hit_cache[key]
        h = 4 * C * K
        target = (-P) % h
        residues = {1}
        for q, e in factorint(P * P + 4 * C * K * K).items():
            powers = []
            power = 1
            for _ in range(e + 1):
                powers.append(power)
                power = power * q % h
            residues = {a * b % h for a in residues for b in powers}
        hit_cache[key] = target in residues
        return hit_cache[key]

    # Columns are (c,k,total zeros, genus-forced zeros, residual box zeros,
    # positives, least prime fixed divisor, one guaranteed residue, modulus).
    expected_rows = (
        (5, 1, 220, 185, 35, 165, 3, 97, 120),
        (7, 1, 330, 182, 148, 55, 11, 73, 1848),
        (10, 1, 313, 185, 128, 72, 7, 73, 840),
        (11, 1, 273, 181, 92, 112, 3, 217, 264),
        (13, 1, 334, 188, 146, 51, 7, 1657, 2184),
        (14, 1, 299, 182, 117, 86, 23, 1489, 3864),
        (15, 1, 348, 185, 163, 37, 23, 457, 2760),
        (17, 1, 303, 186, 117, 82, 3, 337, 408),
        (19, 1, 336, 181, 155, 49, 7, 601, 3192),
        (20, 1, 334, 185, 149, 51, 7, 313, 1680),
        (21, 1, 341, 182, 159, 44, 11, 409, 1848),
        (22, 1, 365, 181, 184, 20, 23, 1033, 6072),
        (23, 1, 346, 173, 173, 39, 3, 457, 552),
        (26, 1, 318, 188, 130, 67, 7, 97, 2184),
        (28, 1, 371, 182, 189, 14, 23, 3673, 7728),
        (29, 1, 325, 189, 136, 60, 3, 577, 696),
        (30, 1, 353, 185, 168, 32, 23, 337, 2760),
        (5, 2, 293, 185, 108, 92, 7, 313, 840),
        (7, 2, 358, 182, 176, 27, 23, 145, 3864),
        (10, 2, 340, 185, 155, 45, 7, 1273, 1680),
        (11, 2, 326, 181, 145, 59, 23, 769, 6072),
        (13, 2, 353, 188, 165, 32, 7, 409, 2184),
        (14, 2, 337, 182, 155, 48, 23, 3001, 7728),
        (15, 2, 363, 185, 178, 22, 23, 937, 2760),
        (5, 3, 348, 185, 163, 37, 23, 577, 2760),
        (7, 3, 348, 182, 166, 37, 11, 241, 1848),
        (10, 3, 348, 185, 163, 37, 23, 217, 2760),
        (5, 4, 321, 185, 136, 64, 7, 73, 1680),
        (7, 4, 368, 182, 186, 17, 23, 313, 7728),
        (5, 5, 325, 185, 140, 60, 3, 97, 600),
        (5, 6, 359, 185, 174, 26, 23, 1177, 2760),
    )
    assert tuple((row[0], row[1]) for row in expected_rows) == unforced

    observed_rows = []
    zero_sets = {}
    for C, K in unforced:
        zeros = frozenset(P for P in census_hard if not slice_hit(P, C, K))
        genus = frozenset(P for P in census_hard
                          if kronecker_symbol(-squarefree_core(C), P) == 1)
        assert genus <= zeros
        zero_sets[(C, K)] = zeros
        observed_rows.append((C, K, len(zeros), len(genus),
                              len(zeros - genus), len(census_hard) - len(zeros)))
    assert tuple(observed_rows) == tuple(row[:6] for row in expected_rows)

    # Reproduce §44's conventions and its aggregate counts without refactoring
    # or repeating the 80 deterministically zero factorizations.
    total_depth = Counter(80 + sum(P in zero_sets[s] for s in unforced)
                          for P in census_hard)
    assert dict(sorted(total_depth.items())) == {
        99: 2, 100: 3, 101: 10, 102: 4, 103: 18, 104: 43, 105: 40,
        106: 43, 107: 55, 108: 55, 109: 64, 110: 33, 111: 15,
    }
    cutoff_rows = []
    for cutoff in (4, 5, 10, 15, 20, 25, 30):
        slices = tuple((C, K) for C, K in box_slices if C * K <= cutoff)
        all_zero = sum(all(squarefree_core(C) in forced_cores
                           or P in zero_sets[(C, K)] for C, K in slices)
                       for P in census_hard)
        cutoff_rows.append((cutoff, len(slices), all_zero))
    assert tuple(cutoff_rows) == (
        (4, 8, 385), (5, 10, 220), (10, 27, 161), (15, 45, 63),
        (20, 66, 41), (25, 87, 30), (30, 111, 15),
    )

    def admissible(P, C, K):
        return (3 * K <= 2 * P and 4 * C * K <= 2 * P + K
                and gcd(P, C * K) == 1)

    # Find ck_min in product order.  Only unresolved primes continue, and each
    # factor box stores at most 4ck residues.
    unresolved = set(hard_all)
    ck_min = {}
    first_slice = {}
    for n in range(1, 129):
        pairs = tuple((C, n // C) for C in range(1, n + 1) if n % C == 0
                      and squarefree_core(C) not in forced_cores)
        for C, K in pairs:
            for P in tuple(unresolved):
                if admissible(P, C, K) and slice_hit(P, C, K):
                    ck_min[P] = n
                    first_slice[P] = (C, K)
                    unresolved.remove(P)
        if not unresolved:
            break
    assert not unresolved, ("ck_min guard exhausted", sorted(unresolved))
    depth = {P: ck_min[P] - 1 for P in hard_all}

    expected_depth_hist = {
        4: 165, 6: 29, 9: 30, 10: 66, 12: 13, 13: 19, 16: 18,
        18: 4, 20: 6, 21: 3, 22: 2, 25: 10, 27: 3, 28: 2, 30: 1,
        33: 2, 34: 1, 37: 3, 38: 1, 41: 2, 43: 1, 58: 2, 66: 1,
        76: 1,
    }
    assert dict(sorted(Counter(depth[P] for P in census_hard).items())) == expected_depth_hist

    depth_records = []
    running = -1
    for P in census_hard:
        if depth[P] > running:
            running = depth[P]
            depth_records.append((P, running))
    assert tuple(depth_records) == (
        (73, 6), (193, 9), (241, 10), (769, 12), (1321, 20),
        (2281, 25), (2521, 37), (9601, 66), (12289, 76),
    )

    dyadic = []
    for j in range(6, 15):
        bucket = tuple(P for P in census_hard
                       if 2**j <= P < min(2**(j + 1), 30_000))
        if bucket:
            maximum = max(depth[P] for P in bucket)
            dyadic.append((2**j, min(2**(j + 1), 30_000), len(bucket),
                           maximum, tuple(P for P in bucket if depth[P] == maximum)))
    assert tuple(dyadic) == (
        (64, 128, 2, 6, (73,)), (128, 256, 2, 10, (241,)),
        (256, 512, 5, 10, (409,)), (512, 1024, 6, 12, (769,)),
        (1024, 2048, 16, 20, (1321,)),
        (2048, 4096, 31, 37, (2521,)),
        (4096, 8192, 58, 27, (8161,)),
        (8192, 16384, 99, 76, (12289,)),
        (16384, 30_000, 166, 58, (29569,)),
    )

    def divisor_square_hit(n, modulus):
        target = (-n) % modulus
        residues = {1}
        for q, e in factorint(n).items():
            powers = []
            power = 1
            for _ in range(2 * e + 1):
                powers.append(power)
                power = power * q % modulus
            residues = {a * b % modulus for a in residues for b in powers}
        return target in residues

    def w_star(P):
        for w in range(3, 80, 4):
            x = (P + w) // 4
            if divisor_square_hit(x, w):
                return w
            z = (P * w + 1) // 4
            if divisor_square_hit(z, w):
                return w
        raise AssertionError(("w* guard exhausted", P))

    w_values = {P: w_star(P) for P in census_hard}
    assert dict(sorted(Counter(w_values.values()).items())) == {
        3: 304, 7: 62, 11: 14, 15: 2, 23: 2, 31: 1,
    }

    def pearson(xs, ys):
        mean_x = sum(xs) / len(xs)
        mean_y = sum(ys) / len(ys)
        numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
        denominator = sqrt(sum((x - mean_x)**2 for x in xs)
                           * sum((y - mean_y)**2 for y in ys))
        return numerator / denominator

    def tied_ranks(values):
        positions = defaultdict(list)
        for i, value in enumerate(values):
            positions[value].append(i)
        ans = [0.0] * len(values)
        first = 1
        for value in sorted(positions):
            indices = positions[value]
            rank = (first + first + len(indices) - 1) / 2
            for i in indices:
                ans[i] = rank
            first += len(indices)
        return ans

    D_values = [depth[P] for P in census_hard]
    W_values = [w_values[P] for P in census_hard]
    assert round(pearson(D_values, W_values), 6) == 0.525121
    assert round(pearson(tied_ranks(D_values), tied_ranks(W_values)), 6) == 0.568502
    grouped = []
    for w in sorted(set(W_values)):
        values = [depth[P] for P in census_hard if w_values[P] == w]
        grouped.append((w, len(values), round(sum(values) / len(values), 3), max(values)))
    assert tuple(grouped) == (
        (3, 304, 7.303, 37), (7, 62, 17.258, 66),
        (11, 14, 27.143, 76), (15, 2, 26.5, 37),
        (23, 2, 21.0, 30), (31, 1, 38.0, 38),
    )

    def fixed_prime_classes(C, K, q):
        """Hard CRT classes on which q is the target divisor."""
        if gcd(q, 2 * C * K) != 1 or factorint(q) != {q: 1}:
            return ()
        h = 4 * C * K
        modulus = lcm(24, h, q)
        return tuple((r, modulus) for r in range(1, modulus, 24)
                     if r % h == (-q) % h
                     and (r * r + 4 * C * K * K) % q == 0)

    # Least eligible prime q and one displayed class for every unforced slice.
    for C, K, zeros, genus, residual, positives, q, r, modulus in expected_rows:
        assert fixed_prime_classes(C, K, q)
        assert (r, modulus) in fixed_prime_classes(C, K, q)
        assert all(not fixed_prime_classes(C, K, smaller)
                   for smaller in primerange(3, q))
        scanned = 0
        for P in hard_all:
            if P % modulus != r:
                continue
            scanned += 1
            h = 4 * C * K
            norm = P * P + 4 * C * K * K
            assert norm % q == 0 and q % h == (-P) % h
            E = norm // q
            A, B = (P + q) // h, (P + E) // h
            assert A > 0 and B > 0
            assert P * (A + B) == K * (4 * A * B * C - 1)
            assert slice_hit(P, C, K)
        assert scanned > 0

    # Complete hard-compatible prime-divisor guarantees for q <= 7 and ck <= 30.
    small_guarantees = tuple(
        (C, K, q, r, modulus)
        for q in (3, 5, 7) for C, K in unforced
        for r, modulus in fixed_prime_classes(C, K, q)
    )
    assert all(not fixed_prime_classes(C, K, q)
               for q in (3, 5, 7) for C, K in box_slices
               if squarefree_core(C) in forced_cores)
    expected_small = (
        (5, 1, 3, 97, 120), (11, 1, 3, 217, 264),
        (17, 1, 3, 337, 408), (23, 1, 3, 457, 552),
        (29, 1, 3, 577, 696), (5, 5, 3, 97, 600),
        (5, 1, 7, 433, 840), (5, 1, 7, 673, 840),
        (10, 1, 7, 73, 840), (10, 1, 7, 193, 840),
        (13, 1, 7, 1657, 2184), (13, 1, 7, 1969, 2184),
        (17, 1, 7, 1081, 2856), (17, 1, 7, 2713, 2856),
        (19, 1, 7, 601, 3192), (19, 1, 7, 1513, 3192),
        (20, 1, 7, 313, 1680), (20, 1, 7, 793, 1680),
        (26, 1, 7, 97, 2184), (26, 1, 7, 1345, 2184),
        (5, 2, 7, 313, 840), (5, 2, 7, 793, 840),
        (10, 2, 7, 1273, 1680), (10, 2, 7, 1513, 1680),
        (13, 2, 7, 409, 2184), (13, 2, 7, 1033, 2184),
        (5, 4, 7, 73, 1680), (5, 4, 7, 1033, 1680),
        (5, 5, 7, 793, 4200), (5, 5, 7, 1993, 4200),
    )
    assert small_guarantees == expected_small
    for C, K, q, r, modulus in small_guarantees:
        matching = tuple(P for P in census_hard if P % modulus == r)
        assert matching
        for P in matching:
            h = 4 * C * K
            E = (P * P + 4 * C * K * K) // q
            A, B = (P + q) // h, (P + E) // h
            assert q % h == (-P) % h
            assert P * (A + B) == K * (4 * A * B * C - 1)
            assert slice_hit(P, C, K)

    if scan_limit == 100_000:
        full_records = []
        running = -1
        for P in hard_all:
            if depth[P] > running:
                running = depth[P]
                full_records.append((P, running))
        assert tuple(full_records[-2:]) == ((55_441, 82), (92_401, 102))
        assert max(depth.values()) == 102

    print("unforced slices / hard census =", (len(unforced), len(census_hard)))
    print("per-slice (c,k,zeros,genus,residual,positive) =",
          tuple(row[:6] for row in expected_rows))
    print("D histogram / records / max =",
          (expected_depth_hist, depth_records, max(depth[P] for P in census_hard)))
    print("D versus w*: Pearson/Spearman =", (0.525121, 0.568502))
    print("least-q guarantees / all q<=7 classes =",
          (len(expected_rows), len(small_guarantees)))
    if scan_limit == 100_000:
        print("ES_FULL_SCAN hard primes / max D =", (len(hard_all), max(depth.values())))


print("\n== (au) conspiracy depth and guaranteed slice positivity (§48) ==")
check_au()


# ---------------------------------------------------------------- (av)
def check_av():
    """§49: exact implication antichain and collective-closure obstruction."""
    import os
    from functools import lru_cache

    def is_prime(n):
        return n >= 2 and factorint(n) == {n: 1}

    @lru_cache(None)
    def integer_divisors(n):
        values = [1]
        for p, e in factorint(n).items():
            values = [d * p**j for d in values for j in range(e + 1)]
        return tuple(sorted(values))

    @lru_cache(None)
    def intrinsic_representatives(M):
        representatives = {}
        for D in divisors_of_square((M + 1) // 4):
            residue = (-4 * D) % M
            representatives[residue] = min(representatives.get(residue, D), D)
        return representatives

    def merge_classes(d, a, M, b):
        common = gcd(d, M)
        if (a - b) % common:
            return None
        quotient = M // common
        shift = 0 if quotient == 1 else (
            (b - a) // common * pow(d // common, -1, quotient)
        ) % quotient
        modulus = d * quotient
        return modulus, (a + d * shift) % modulus

    def build_complete_H(X, z, Y):
        prime_residues = {
            p: set(intrinsic_representatives(p))
            for p in primerange(z + 1, X + 1) if p % 4 == 3
        }
        low = {p: len(classes) for p, classes in prime_residues.items() if p <= Y}
        atoms = []

        for p, classes in prime_residues.items():
            if p > Y:
                for residue in classes:
                    atoms.append((p, residue,
                                  intrinsic_representatives(p)[residue], "prime"))

        for M in range(3, X + 1, 4):
            factors = factorint(M)
            if is_prime(M) or any(p <= z for p in factors):
                continue
            for residue, D in intrinsic_representatives(M).items():
                if any(
                    p in prime_residues
                    and residue % p in prime_residues[p]
                    for p in factors
                ):
                    continue
                atoms.append((M, residue, D, "composite"))
        return atoms, low

    def implication_reduce(atoms):
        atom_classes = {(M, residue) for M, residue, *_ in atoms}
        reduced = []
        deleted = []
        for atom in atoms:
            M, residue = atom[:2]
            containers = tuple(
                d for d in integer_divisors(M)
                if d < M and (d, residue % d) in atom_classes
            )
            if containers:
                deleted.append((atom, containers))
            else:
                reduced.append(atom)
        return reduced, deleted

    def conditional_weight(M, low):
        probability = Fraction(1, M)
        for p, forbidden in low.items():
            if M % p == 0:
                probability *= Fraction(p, p - forbidden)
        return probability

    # A nontrivial implication-reduction toy.  The full-space void identity
    # is certified symbolically: every deleted class is contained in a class
    # of the final antichain, so no lcm-sized residue array is formed.
    raw, low = build_complete_H(1000, 2, 1000)
    reduced, deleted = implication_reduce(raw)
    assert (len(raw), len(reduced), len(deleted)) == (1042, 970, 72)
    reduced_classes = {(M, residue) for M, residue, *_ in reduced}
    assert len(reduced_classes) == len(reduced)
    for M, residue, D, _ in raw:
        if (M, residue) in reduced_classes:
            continue
        containers = tuple(
            d for d in integer_divisors(M)
            if d < M and (d, residue % d) in reduced_classes
        )
        assert containers
        d = containers[0]
        D0 = intrinsic_representatives(d)[residue % d]
        assert D % d == D0 % d                 # (49.3), since 4 is a unit
    for M, residue, *_ in reduced:
        assert all(
            (d, residue % d) not in reduced_classes
            for d in integer_divisors(M) if d < M
        )

    raw_mu = sum((conditional_weight(M, low) for M, *_ in raw), Fraction())
    reduced_mu = sum(
        (conditional_weight(M, low) for M, *_ in reduced), Fraction()
    )
    mass_share = reduced_mu / raw_mu
    assert round(float(mass_share), 6) == 0.939936

    # Exact residue profiles W^dagger_{g,a}.  The largest normalized load is
    # phi(g) max_a W(g,a)/W(g), with every mass retained as a Fraction.
    profiles = {}
    for M, residue, *_ in reduced:
        weight = conditional_weight(M, low)
        for g in integer_divisors(M):
            if g == 1:
                continue
            if g not in profiles:
                profiles[g] = [Fraction(), {}]
            profiles[g][0] += weight
            bins = profiles[g][1]
            bins[residue % g] = bins.get(residue % g, Fraction()) + weight

    profile_rows = []
    for g, (total, bins) in profiles.items():
        phi_g = g
        for p in factorint(g):
            phi_g = phi_g // p * (p - 1)
        maximum = max(bins.values())
        profile_rows.append((Fraction(phi_g) * maximum / total,
                             g, maximum / total, len(bins)))
    profile_rows.sort(reverse=True)
    assert profile_rows[0] == (Fraction(220), 943, Fraction(1, 4), 4)

    # Exact small-S hierarchy for the implication-reduced complete H toy.
    def hierarchy_toy(X, z, Y, degree):
        atoms, low_coordinates = build_complete_H(X, z, Y)
        atoms, _ = implication_reduce(atoms)

        @lru_cache(None)
        def probability(modulus):
            return conditional_weight(modulus, low_coordinates)

        mu = sum((probability(M) for M, *_ in atoms), Fraction())
        states = [((), 1, 0)]
        counts, maxima = [], []
        for _ in range(degree):
            new_states = []
            for indices, modulus, residue in states:
                start = indices[-1] + 1 if indices else 0
                for index in range(start, len(atoms)):
                    merged = merge_classes(
                        modulus, residue, atoms[index][0], atoms[index][1]
                    )
                    if merged is not None:
                        new_states.append((indices + (index,), *merged))
            states = new_states
            counts.append(len(states))
            extension_loads = []
            for indices, modulus, residue in states:
                selected = set(indices)
                load = Fraction()
                for index, (M, atom_residue, *_rest) in enumerate(atoms):
                    if index in selected:
                        continue
                    merged = merge_classes(modulus, residue, M, atom_residue)
                    if merged is not None:
                        load += probability(merged[0]) / probability(modulus)
                extension_loads.append(load)
            maxima.append(max(extension_loads))
        return len(atoms), mu, tuple(counts), tuple(maxima)

    hierarchy = hierarchy_toy(40, 2, 7, 3)
    assert hierarchy == (
        28,
        Fraction(27839083, 19372210),
        (28, 316, 1868),
        (Fraction(6342705, 3874442), Fraction(295533, 149017),
         Fraction(14316, 7843)),
    )
    hierarchy_ratios = tuple(value / hierarchy[1] for value in hierarchy[3])
    assert hierarchy_ratios == (
        Fraction(31713525, 27839083),
        Fraction(38419290, 27839083),
        Fraction(35360520, 27839083),
    )

    # The minimal collective-implication square: diagonal semiprime atoms
    # imply both off-diagonal atoms although all four survive the antichain.
    grid_raw, grid_low = build_complete_H(143, 2, 143)
    grid, _ = implication_reduce(grid_raw)
    grid_classes = {(M, residue) for M, residue, *_ in grid}
    q_values, p_values = (3, 11), (5, 13)
    for q in q_values:
        for p in p_values:
            M = q * p
            assert (M, (-8) % M) in grid_classes
            assert intrinsic_representatives(M)[(-8) % M] == 2
    selected = ((15, (-8) % 15), (143, (-8) % 143))
    merged_selected = merge_classes(*selected[0], *selected[1])
    assert merged_selected == (2145, (-8) % 2145)
    collective_load = Fraction()
    for M in (39, 55):
        merged = merge_classes(*merged_selected, M, (-8) % M)
        assert merged == merged_selected
        collective_load += (
            conditional_weight(merged[0], grid_low)
            / conditional_weight(merged_selected[0], grid_low)
        )
    assert collective_load == 2

    if os.environ.get("ES_FULL_SCAN") == "1":
        full_raw, full_low = build_complete_H(5655, 5, 5655)
        full_reduced, full_deleted = implication_reduce(full_raw)
        assert (len(full_raw), len(full_reduced), len(full_deleted)) == (6210, 6140, 70)
        full_mu = sum(
            (conditional_weight(M, full_low) for M, *_ in full_raw), Fraction()
        )
        full_reduced_mu = sum(
            (conditional_weight(M, full_low) for M, *_ in full_reduced), Fraction()
        )
        assert round(float(full_reduced_mu / full_mu), 6) == 0.992549

    print("antichain toy (raw,dagger,deleted,count-share,mass-share) =",
          (len(raw), len(reduced), len(deleted),
           Fraction(len(reduced), len(raw)), mass_share))
    print("max residue concentration (phi(g)*share,g,share,bins) =",
          profile_rows[0])
    print("small-S (Lambda_dagger,counts,max ell/Lambda_dagger) =",
          (hierarchy[1], hierarchy[2], hierarchy_ratios))
    print("collective 2x2 semiprime-grid forced extension load =", collective_load)


print("\n== (av) implication-reduced antichain (§49) ==")
check_av()
# ---------------------------------------------------------------- (aw)
def check_aw():
    """§50: prime-factor slice reduction and its finite depth comparison."""
    import os
    from sympy import kronecker_symbol

    scan_limit = 100_000 if os.environ.get("ES_FULL_SCAN") == "1" else 30_000
    guard = 320 if scan_limit == 100_000 else 128
    hard_all = tuple(p for p in primerange(2, scan_limit) if p % 24 == 1)
    census_hard = tuple(p for p in hard_all if p < 30_000)
    assert len(census_hard) == 385
    if scan_limit == 100_000:
        assert len(hard_all) == 1181

    core_cache = {}

    def squarefree_core(n):
        if n not in core_cache:
            core_cache[n] = prod(q for q, e in factorint(n).items() if e % 2)
        return core_cache[n]

    def admissible(P, C, K):
        return (gcd(P, C * K) == 1 and 3 * K <= 2 * P
                and 4 * C * K <= 2 * P + K)

    def exponent_box_hit(P, C, K, factors):
        """Exact (44.4) test, retaining at most 4CK residue grades."""
        h = 4 * C * K
        residues = {1}
        for q, e in factors.items():
            powers = []
            power = 1
            for _ in range(e + 1):
                powers.append(power)
                power = power * q % h
            residues = {a * b % h for a in residues for b in powers}
            assert len(residues) <= h
        return (-P) % h in residues

    unresolved_prime = set(hard_all)
    unresolved_slice = set(hard_all)
    prime_min = {}
    slice_min = {}
    first_prime_slice = {}
    first_good_prime = {}
    implication_checks = 0

    # Both minima are found in product order.  Once both have been found for
    # P, no data for P are retained or recomputed at larger products.
    for n in range(1, guard + 1):
        pairs = tuple((C, n // C) for C in range(1, n + 1) if n % C == 0)
        for C, K in pairs:
            for P in tuple(unresolved_prime | unresolved_slice):
                if not admissible(P, C, K):
                    continue
                h = 4 * C * K
                norm = P * P + 4 * C * K * K
                factors = factorint(norm)
                hit = exponent_box_hit(P, C, K, factors)
                good_primes = tuple(q for q in factors
                                    if q % h == (-P) % h)

                # The universally forced cores have neither a target divisor
                # nor a good prime, independently checking the genus filter.
                core = squarefree_core(C)
                if core in (1, 2, 3, 6):
                    assert not hit and not good_primes

                # Check every one-prime event encountered before the two
                # minima resolve, not just the selected minimum witness.
                for q in good_primes:
                    assert factorint(q) == {q: 1}
                    assert gcd(q, h) == 1 and norm % q == 0
                    E = norm // q
                    assert q % h == E % h == (-P) % h
                    assert q % 4 == E % 4 == 3 and q < norm
                    A, B = (P + q) // h, (P + E) // h
                    assert min(A, B) > 0
                    assert P * (A + B) == K * (4 * A * B * C - 1)
                    assert (Fraction(1, A * C * K)
                            + Fraction(1, B * C * K)
                            + Fraction(1, P * A * B * C)
                            == Fraction(4, P))
                    assert kronecker_symbol(-core, P) == -1
                    assert hit
                    implication_checks += 1

                if P in unresolved_slice and hit:
                    slice_min[P] = n
                    unresolved_slice.remove(P)
                if P in unresolved_prime and good_primes:
                    prime_min[P] = n
                    first_prime_slice[P] = (C, K)
                    first_good_prime[P] = min(good_primes)
                    unresolved_prime.remove(P)
        if not unresolved_prime and not unresolved_slice:
            break

    assert not unresolved_prime, ("prime-factor guard exhausted",
                                  sorted(unresolved_prime))
    assert not unresolved_slice, ("slice guard exhausted",
                                  sorted(unresolved_slice))
    assert all(prime_min[P] >= slice_min[P] for P in hard_all)

    expected_prime_hist = {
        5: 156, 7: 30, 10: 36, 11: 35, 13: 13, 14: 15, 17: 16,
        19: 4, 21: 15, 22: 9, 23: 6, 26: 10, 28: 4, 29: 3, 31: 1,
        33: 2, 34: 3, 35: 1, 37: 1, 38: 4, 39: 2, 42: 5, 43: 1,
        46: 1, 55: 2, 62: 1, 66: 4, 67: 1, 69: 1, 70: 1, 77: 1,
        78: 1,
    }
    expected_slice_hist = {
        5: 165, 7: 29, 10: 30, 11: 66, 13: 13, 14: 19, 17: 18,
        19: 4, 21: 6, 22: 3, 23: 2, 26: 10, 28: 3, 29: 2, 31: 1,
        34: 2, 35: 1, 38: 3, 39: 1, 42: 2, 44: 1, 59: 2, 67: 1,
        77: 1,
    }
    observed_prime_hist = dict(sorted(Counter(prime_min[P]
                                               for P in census_hard).items()))
    observed_slice_hist = dict(sorted(Counter(slice_min[P]
                                               for P in census_hard).items()))
    assert observed_prime_hist == expected_prime_hist
    assert observed_slice_hist == expected_slice_hist

    def strict_records(values, primes):
        records = []
        running = -1
        for P in primes:
            if values[P] > running:
                running = values[P]
                records.append((P, running))
        return tuple(records)

    expected_records = (
        (73, 7), (193, 10), (241, 21), (1201, 34), (2521, 38),
        (4729, 66), (7489, 70), (9601, 78),
    )
    assert strict_records(prime_min, census_hard) == expected_records
    equal = sum(prime_min[P] == slice_min[P] for P in census_hard)
    gaps = {P: prime_min[P] - slice_min[P] for P in census_hard}
    assert equal == 311 and sum(gap > 0 for gap in gaps.values()) == 74
    assert max(gaps.values()) == 55 and gaps[23_689] == 55
    assert (slice_min[23_689], prime_min[23_689]) == (11, 66)
    assert first_prime_slice[23_689] == (33, 2)
    assert first_good_prime[23_689] == 77_951
    assert max(prime_min[P] for P in census_hard) == 78
    assert tuple(P for P in census_hard if prime_min[P] == 78) == (9601,)

    if scan_limit == 100_000:
        full_records = strict_records(prime_min, hard_all)
        assert full_records[-3:] == ((31_081, 110), (51_769, 249),
                                     (83_689, 282))
        assert max(prime_min.values()) == 282
        assert tuple(P for P in hard_all if prime_min[P] == 282) == (83_689,)
        assert max(slice_min.values()) == 103
        assert sum(prime_min[P] == slice_min[P] for P in hard_all) == 960
        assert max(prime_min[P] - slice_min[P] for P in hard_all) == 211

    print("prime-factor ck histogram =", expected_prime_hist)
    print("prime-factor records / exact implication instances =",
          (expected_records, implication_checks))
    print("ck_pr versus ck_min: equal/larger/max gap/maxima =",
          (equal, 74, 55, 78, 77))
    if scan_limit == 100_000:
        print("ES_FULL_SCAN hard primes / max ck_pr / max ck_min =",
              (len(hard_all), max(prime_min.values()), max(slice_min.values())))


print("\n== (aw) conditional slice prime-factor reduction (§50) ==")
check_aw()
# ---------------------------------------------------------------- (ax)
def check_ax():
    """§51: witness-modulus tails and truncated CRT bookkeeping."""

    def ordinary_divisors(n):
        values = [1]
        for q, e in factorint(n).items():
            values = [d * q**j for d in values for j in range(e + 1)]
        return values

    # Direct Lemma-16.1 harvest.  Taking k=1, ell=M shows that every
    # M=3 (mod 4) is a valid multiplier modulus; no primality is imposed.
    modulus_classes = {}
    for M in range(3, 3001, 4):
        A = (M + 1) // 4
        classes = set()
        for u in ordinary_divisors(A):
            for v in ordinary_divisors(A // u):
                w = A // (u * v)
                assert u * v * w == A and gcd(v, M) == 1
                classes.add((-u * pow(v, -1, M)) % M)
        # Independently replay Lemma 18.1's intrinsic divisor description.
        intrinsic = {(-4 * D) % M for D in divisors_of_square(A)}
        assert classes == intrinsic
        modulus_classes[M] = classes

    hard_primes = tuple(p for p in primerange(2, 300_000) if p % 24 == 1)
    assert len(hard_primes) == 3202
    witness_modulus = {p: None for p in hard_primes}
    for M, classes in modulus_classes.items():
        for p in hard_primes:
            if witness_modulus[p] is None and p % M in classes:
                witness_modulus[p] = M
    assert all(M is not None and M <= 3000 for M in witness_modulus.values())
    assert max(witness_modulus.values()) == 279

    thresholds = (25, 100, 400, 1600)
    tails = tuple(sum(M > T for M in witness_modulus.values())
                  for T in thresholds)
    assert tails == (226, 19, 0, 0)
    assert all(a >= b for a, b in zip(tails, tails[1:]))

    # Informational continuity-corrected log-linear fits.  Positivity of the
    # fitted decay constants is only a weak finite sanity check.
    def fitted_shape(feature):
        xs = [feature(log(T)) for T in thresholds]
        ys = [log((count + 0.5) / len(hard_primes)) for count in tails]
        xbar = sum(xs) / len(xs)
        ybar = sum(ys) / len(ys)
        slope = (sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
                 / sum((x - xbar) ** 2 for x in xs))
        intercept = ybar - slope * xbar
        assert slope < 0
        predictions = tuple(exp(intercept + slope * x) for x in xs)
        assert all(a > b for a, b in zip(predictions, predictions[1:]))
        return (intercept, -slope)

    fit_elementary = fitted_shape(lambda t: t * t * log(t))
    fit_cubic = fitted_shape(lambda t: t**3)

    # A structural toy with the same determinant and 4uv>K size guards.
    # Its genuine asymptotic floor H=K^10 would make every small instance
    # empty, so H is omitted exactly as in the earlier §39 toy companion.
    def toy_atoms(X, K, modulus_cap=200):
        atoms = []
        for ell in primerange(3, X + 1):
            if ell % 4 != 3:
                continue
            z = int(ell ** (1 / 3) + 1e-12)
            for k in range(1, K + 1, 4):
                M = k * ell
                if M > modulus_cap:
                    continue
                A = (M + 1) // 4
                for u in ordinary_divisors(A):
                    if u > z:
                        continue
                    for v in ordinary_divisors(A // u):
                        if (v > z or gcd(u, v) != 1 or gcd(u * v, k) != 1
                                or 4 * u * v <= K):
                            continue
                        residue = (-u * pow(v, -1, M)) % M
                        atoms.append((k, ell, u, v, M, residue))
        assert len(atoms) == len({(a[4], a[5]) for a in atoms})
        return tuple(atoms)

    atoms = toy_atoms(40, 5)
    assert len(atoms) == 10

    def merge_classes(left, right):
        a, m = left
        b, n = right
        g = gcd(m, n)
        if (b - a) % g:
            return None
        n1 = n // g
        step = ((b - a) // g * pow(m // g, -1, n1)) % n1
        modulus = m * n1
        return ((a + m * step) % modulus, modulus)

    # Every same-ell pair is incompatible, while compatible distinct atoms
    # have distinct ell, replaying the content used in (39.5).
    for A, B in combinations(atoms, 2):
        merged = merge_classes((A[5], A[4]), (B[5], B[4]))
        if A[1] == B[1]:
            assert merged is None
        elif merged is not None:
            assert A[1] != B[1]

    selected = tuple(A for A in atoms
                     if A[1] in (11, 23, 31) and A[4] in (55, 23, 31))
    assert len(selected) == 6
    inclusion_exclusion = Fraction()
    for j in range(len(selected) + 1):
        for subset in combinations(selected, j):
            merged = (0, 1)
            for A in subset:
                merged = merge_classes(merged, (A[5], A[4]))
                if merged is None:
                    break
            if merged is not None:
                inclusion_exclusion += Fraction((-1) ** j, merged[1])

    period = 1
    for A in selected:
        period = lcm(period, A[4])
    direct_void = sum(not any(n % A[4] == A[5] for A in selected)
                      for n in range(period))
    assert (period, direct_void) == (39_215, 32_277)
    assert inclusion_exclusion == Fraction(direct_void, period)

    # Finite checks of the exceptional-conductor deletion used in §51.3.
    # These are class counts, not evidence for the asymptotic 1/3 lemma.
    deletion_rows = []
    for X, K, expected in ((40, 5, (10, 8, 10, 10)),
                           (200, 13, (90, 54, 64, 90)),
                           (300, 13, (144, 82, 98, 144))):
        family = set()
        for A in toy_atoms(X, K, modulus_cap=3000):
            _, _, u, v, M, residue = A
            family.add((M, residue, 4 * u * v))
        retained = tuple(sum(q % r != 0 for _, _, q in family)
                         for r in (3, 5, 7))
        row = (len(family),) + retained
        assert row == expected
        assert all(10 * count >= 3 * len(family) for count in retained)
        deletion_rows.append(((X, K), row))

    print("W_II<=3000 hard-prime tails (T:count) =",
          dict(zip(thresholds, tails)))
    print("continuity-corrected fits (log C,c): elementary/cubic =",
          (tuple(round(x, 6) for x in fit_elementary),
           tuple(round(x, 6) for x in fit_cubic)))
    print("toy CRT void (atoms,period,count,probability) =",
          (len(selected), period, direct_void, inclusion_exclusion))
    print("exceptional-conductor deletion toys ((X,K):(all,r=3,5,7)) =",
          deletion_rows)


print("\n== (ax) witness-modulus tail and effectivity audit (§51) ==")
check_ax()


# ---------------------------------------------------------------- (ay)
def check_ay():
    """§52: per-slice sieve bookkeeping and finite residual census."""
    import os
    from sympy import kronecker_symbol, sqrt_mod, totient

    scan_limit = 100_000 if os.environ.get("ES_FULL_SCAN") == "1" else 30_000
    hard = tuple(p for p in primerange(2, scan_limit) if p % 24 == 1)
    assert len(hard) == (1181 if scan_limit == 100_000 else 385)

    def squarefree_core(n):
        return prod(q for q, e in factorint(n).items() if e % 2)

    def discriminant(s):
        return -s if (-s) % 4 == 1 else -4 * s

    def genus(s, n):
        return int(kronecker_symbol(discriminant(s), n))

    def admissible(P, C, K):
        return (gcd(P, C * K) == 1 and 3 * K <= 2 * P
                and 4 * C * K <= 2 * P + K)

    def exponent_box_hit(P, C, K, factors):
        h = 4 * C * K
        residues = {1}
        for q, e in factors.items():
            powers, power = [], 1
            for _ in range(e + 1):
                powers.append(power)
                power = power * q % h
            residues = {u * v % h for u in residues for v in powers}
            assert len(residues) <= h
        return (-P) % h in residues

    def divisors_from_factorization(factors):
        values = [1]
        for q, e in factors.items():
            values = [d * q**j for d in values for j in range(e + 1)]
        return values

    # Four fixed unforced classes.  Here the least compatible active class is
    # a=73 in every case, but it is derived rather than assumed.
    panel = ((5, 1), (7, 1), (10, 1), (13, 1))
    expected_panel = (
        ((105, 35), (297, 86)),
        ((66, 41), (204, 122)),
        ((105, 58), (297, 163)),
        ((31, 24), (98, 81)),
    )
    panel_rows = []
    reconstruction_samples = 0
    for index, (C, K) in enumerate(panel):
        s, h, Q = squarefree_core(C), 4 * C * K, lcm(24, 4 * C * K)
        compatible = tuple(a for a in range(Q)
                           if a % 24 == 1 and gcd(a, Q) == 1
                           and genus(s, a) == -1)
        assert compatible and compatible[0] == 73
        a = compatible[0]

        # The genus identity makes every q in the good ray class a split
        # prime.  Check all such q <= 10^4, including the exact two roots.
        for q in primerange(3, 10_001):
            if q % h != (-a) % h:
                continue
            assert gcd(q, 2 * C * K) == 1
            assert genus(s, q) == 1
            roots = tuple(sqrt_mod((-4 * C * K * K) % q, q,
                                   all_roots=True))
            assert len(roots) == 2 and roots[0] + roots[1] == q
            assert all((r * r + 4 * C * K * K) % q == 0 for r in roots)

        class_primes = vanishers = 0
        for P in hard:
            if P % Q != a:
                continue
            class_primes += 1
            norm = P * P + 4 * C * K * K
            factors = factorint(norm)
            hit = exponent_box_hit(P, C, K, factors)
            good_factors = tuple(q for q in factors if q % h == (-P) % h)
            if not hit:
                vanishers += 1
                assert not good_factors       # Theorem 50.1 contrapositive
            for q in good_factors:
                roots = tuple(sqrt_mod((-4 * C * K * K) % q, q,
                                       all_roots=True))
                assert len(roots) == 2 and P % q in roots
                if reconstruction_samples >= 50:
                    continue
                E = norm // q
                A, B = (P + q) // h, (P + E) // h
                assert min(A, B) > 0
                assert P * (A + B) == K * (4 * A * B * C - 1)
                assert (Fraction(1, A * C * K)
                        + Fraction(1, B * C * K)
                        + Fraction(1, P * A * B * C)
                        == Fraction(4, P))
                reconstruction_samples += 1
        observed = (class_primes, vanishers)
        assert observed == expected_panel[index][scan_limit == 100_000]

        q_count = sum(q % h == (-a) % h
                      for q in primerange(2, 30_001))
        expected_density = len(tuple(primerange(2, 30_001))) / int(totient(h))
        assert (q_count == (413, 268, 208, 141)[index]
                and 0.5 <= q_count / expected_density <= 2.0)
        panel_rows.append((C, K, h, Q, a, *observed, q_count))
    assert reconstruction_samples == 50

    # Recompute all 31 fluctuating slices in the ck<=30 box.  Counts are
    # (active genus sign -1, residual vanishing), in product order.
    forced_cores = {1, 2, 3, 6}
    slices = tuple((C, n // C) for n in range(1, 31)
                   for C in range(1, n + 1) if n % C == 0
                   and squarefree_core(C) not in forced_cores)
    assert len(slices) == 31
    expected_small = (
        (200, 35), (203, 148), (200, 108), (200, 128), (204, 92),
        (197, 146), (203, 176), (203, 117), (200, 163), (200, 163),
        (199, 117), (204, 155), (200, 136), (200, 155), (200, 149),
        (203, 166), (203, 159), (204, 145), (204, 184), (212, 173),
        (200, 140), (197, 165), (197, 130), (203, 186), (203, 155),
        (203, 189), (196, 136), (200, 174), (200, 163), (200, 178),
        (200, 168),
    )
    expected_full = (
        (603, 86), (612, 426), (603, 316), (603, 381), (611, 270),
        (608, 445), (612, 529), (612, 335), (603, 476), (603, 480),
        (598, 341), (608, 458), (603, 413), (603, 470), (603, 424),
        (612, 492), (612, 459), (611, 426), (611, 545), (607, 467),
        (603, 409), (608, 502), (608, 411), (612, 558), (612, 437),
        (612, 570), (595, 401), (603, 516), (603, 491), (603, 523),
        (603, 500),
    )
    slice_rows = []
    for C, K in slices:
        s = squarefree_core(C)
        active = residual = 0
        for P in hard:
            if genus(s, P) != -1:
                continue
            active += 1
            factors = factorint(P * P + 4 * C * K * K)
            residual += not exponent_box_hit(P, C, K, factors)
        phi_h = int(totient(4 * C * K))
        model = log(scan_limit)**(-2 / phi_h)
        slice_rows.append((C, K, active, residual,
                           residual / active, model))
    observed_counts = tuple(row[2:4] for row in slice_rows)
    assert observed_counts == (expected_full if scan_limit == 100_000
                               else expected_small)

    # Recompute ck_min and ck_pr in one streamed product-order pass.  The
    # selected target divisors below are then refactored one norm at a time.
    guard = 320 if scan_limit == 100_000 else 128
    unresolved_slice, unresolved_prime = set(hard), set(hard)
    slice_min, prime_min = {}, {}
    for n in range(1, guard + 1):
        for C in range(1, n + 1):
            if n % C:
                continue
            K = n // C
            for P in tuple(unresolved_slice | unresolved_prime):
                if not admissible(P, C, K):
                    continue
                factors = factorint(P * P + 4 * C * K * K)
                hit = exponent_box_hit(P, C, K, factors)
                good = any(q % (4 * n) == (-P) % (4 * n) for q in factors)
                if P in unresolved_slice and hit:
                    slice_min[P] = n
                    unresolved_slice.remove(P)
                if P in unresolved_prime and good:
                    prime_min[P] = n
                    unresolved_prime.remove(P)
        if not unresolved_slice and not unresolved_prime:
            break
    assert not unresolved_slice and not unresolved_prime
    gaps = tuple(P for P in hard if prime_min[P] > slice_min[P])
    assert len(gaps) == (221 if scan_limit == 100_000 else 74)

    event_shapes, witness_shapes = Counter(), Counter()
    for P in gaps:
        n = slice_min[P]
        shapes = set()
        for C in range(1, n + 1):
            if n % C:
                continue
            K, h = n // C, 4 * n
            if not admissible(P, C, K):
                continue
            norm = P * P + 4 * C * K * K
            factors = factorint(norm)
            for D in divisors_from_factorization(factors):
                if D * D >= norm or D % h != (-P) % h:
                    continue
                D_factors = factorint(D)
                assert all(q % h != (-P) % h for q in D_factors)
                omega = sum(D_factors.values())
                if len(D_factors) == 1:
                    shape = "prime-power"
                elif omega == 2:
                    shape = "semiprime"
                else:
                    shape = "multi-prime"
                shapes.add(shape)
                witness_shapes[shape] += 1
        assert shapes
        event_shapes[tuple(sorted(shapes))] += 1

    expected_event_small = {
        ("semiprime",): 49, ("multi-prime",): 13,
        ("multi-prime", "semiprime"): 6,
        ("prime-power", "semiprime"): 2, ("prime-power",): 2,
        ("multi-prime", "prime-power", "semiprime"): 1,
        ("multi-prime", "prime-power"): 1,
    }
    expected_event_full = {
        ("semiprime",): 136, ("multi-prime",): 44,
        ("multi-prime", "semiprime"): 25, ("prime-power",): 6,
        ("multi-prime", "prime-power"): 6,
        ("prime-power", "semiprime"): 3,
        ("multi-prime", "prime-power", "semiprime"): 1,
    }
    assert dict(event_shapes) == (expected_event_full if scan_limit == 100_000
                                  else expected_event_small)
    assert dict(witness_shapes) == (
        {"semiprime": 199, "multi-prime": 93, "prime-power": 16}
        if scan_limit == 100_000 else
        {"semiprime": 68, "multi-prime": 24, "prime-power": 6}
    )

    # Joint residual frequencies, always conditioned on both genus signs -1.
    correlation_pairs = (
        ((5, 1), (5, 2)), ((5, 1), (5, 3)),
        ((7, 1), (7, 2)), ((10, 1), (10, 2)),
        ((5, 1), (7, 1)), ((5, 1), (10, 1)),
        ((7, 1), (11, 1)), ((11, 1), (17, 1)),
    )
    expected_corr_small = (
        (200, 35, 108, 10), (200, 35, 163, 29),
        (203, 148, 176, 125), (200, 128, 155, 93),
        (101, 17, 70, 12), (200, 35, 128, 16),
        (99, 73, 43, 32), (101, 52, 64, 38),
    )
    expected_corr_full = (
        (603, 86, 316, 26), (603, 86, 476, 66),
        (612, 426, 529, 366), (603, 381, 470, 281),
        (307, 46, 214, 35), (603, 86, 381, 38),
        (313, 219, 141, 98), (305, 142, 180, 92),
    )
    correlation_rows = []
    for A, B in correlation_pairs:
        s_A, s_B = squarefree_core(A[0]), squarefree_core(B[0])
        population = van_A = van_B = joint = 0
        for P in hard:
            if genus(s_A, P) != -1 or genus(s_B, P) != -1:
                continue
            population += 1
            v_A = not exponent_box_hit(
                P, *A, factorint(P * P + 4 * A[0] * A[1] * A[1]))
            v_B = not exponent_box_hit(
                P, *B, factorint(P * P + 4 * B[0] * B[1] * B[1]))
            van_A += v_A
            van_B += v_B
            joint += v_A and v_B
        raw = (population, van_A, van_B, joint)
        correlation_rows.append((A, B, *raw,
                                 joint * population / (van_A * van_B)))
    assert tuple(row[2:6] for row in correlation_rows) == (
        expected_corr_full if scan_limit == 100_000 else expected_corr_small
    )

    print("panel (c,k,h,Q,a,class primes,vanishers,good q<=30000) =",
          tuple(panel_rows))
    print("INFO residual rows (c,k,active,vanish,freq,log-model) =",
          tuple(slice_rows))
    print("composite gap events / canonical witness shapes =",
          (len(gaps), dict(event_shapes), dict(witness_shapes)))
    print("INFO correlations (A,B,n,vA,vB,joint,joint/product) =",
          tuple(correlation_rows))


print("\n== (ay) per-slice sieve bookkeeping and residual census (§52) ==")
check_ay()


# ---------------------------------------------------------------- (az)
def check_az():
    """§53: corrected overlap mass, genus bits, and stacked-slice census."""
    import os
    from collections import defaultdict
    from fractions import Fraction
    from itertools import combinations
    from random import Random
    from statistics import median
    from sympy import kronecker_symbol, sqrt_mod, totient

    T = 30
    forced_cores = {1, 2, 3, 6}
    core_cache = {}

    def squarefree_core(n):
        if n not in core_cache:
            core_cache[n] = prod(q for q, e in factorint(n).items() if e % 2)
        return core_cache[n]

    def discriminant(s):
        return -s if (-s) % 4 == 1 else -4 * s

    def genus(s, n):
        return int(kronecker_symbol(discriminant(s), n))

    slices = tuple(
        (C, n // C, squarefree_core(C), n, C * (n // C)**2)
        for n in range(1, T + 1)
        for C in range(1, n + 1) if n % C == 0
    )
    unforced = tuple(row for row in slices if row[2] not in forced_cores)
    assert (len(slices), len(unforced)) == (111, 31)

    # At odd q the factor 4 is invertible, so the uniform threshold is T^2,
    # since CK^2=(CK)K<=T^2.  The requested interval (4T^3,10^5] is empty
    # at T=30, so check the stronger nonvacuous interval (T^2,10^5].
    # A common root is equivalent to equality of the two radicands modulo q.
    # (wave-19 review repair)
    radicands = tuple(sorted({row[4] for row in slices}))
    high_primes = tuple(primerange(T * T + 1, 100_001))
    assert len(high_primes) == 9438
    for q in high_primes:
        rooted = tuple(d for d in radicands
                       if pow((-4 * d) % q, (q - 1) // 2, q) == 1)
        residues = tuple((-4 * d) % q for d in rooted)
        assert len(residues) == len(set(residues))
        assert all(q > abs(d1 - d2)
                   for d1, d2 in combinations(rooted, 2))

    # A genuine below-threshold collision, and the permanent equal-radicand
    # collision which invalidates the uncorrected raw slice mass.
    q_small, first, second = 3, (5, 1), (5, 2)
    d_first, d_second = 5, 20
    roots_first = tuple(sqrt_mod(-4 * d_first, q_small, all_roots=True))
    roots_second = tuple(sqrt_mod(-4 * d_second, q_small, all_roots=True))
    assert roots_first == roots_second == (1, 2)
    assert q_small < T * T and (d_first - d_second) % q_small == 0
    duplicate_a, duplicate_b = (5, 2), (20, 1)
    assert duplicate_a[0] * duplicate_a[1]**2 == 20
    assert duplicate_b[0] * duplicate_b[1]**2 == 20

    L = 1
    for n in range(1, T + 1):
        L = lcm(L, n)
    Q = lcm(24, 4 * L)
    assert Q == 9_316_358_251_200

    def slice_masses(C):
        active = tuple(row for row in unforced if genus(row[2], C) == -1)
        raw = sum((Fraction(2, int(totient(4 * row[3]))) for row in active),
                  Fraction())

        # For one radicand d, several slice ray conditions remove the same
        # two roots.  Inclusion-exclusion over their h=4CK cylinders gives
        # the corrected root-union density.
        sharp = Fraction()
        for d in {row[4] for row in active}:
            moduli = tuple(sorted({4 * row[3] for row in active if row[4] == d}))
            union = Fraction()
            for size in range(1, len(moduli) + 1):
                for subset in combinations(moduli, size):
                    modulus = 1
                    for h in subset:
                        modulus = lcm(modulus, h)
                    union += (-1)**(size + 1) * Fraction(
                        1, int(totient(modulus)))
            sharp += 2 * union
        return raw, sharp, len(active), len({row[4] for row in active})

    # One direct escape class plus 256 seeded uniform reduced hard classes.
    rng = Random(530019)
    classes = [1]
    while len(classes) < 257:
        C = 1 + 24 * rng.randrange(Q // 24)
        if gcd(C, Q) == 1:
            classes.append(C)
    prime_cores = tuple(primerange(5, T + 1))
    raw_masses, sharp_masses, patterns = [], [], Counter()
    for C in classes:
        raw, sharp, active_count, radicand_count = slice_masses(C)
        assert 0 <= sharp <= raw
        assert radicand_count <= active_count
        raw_masses.append(raw)
        sharp_masses.append(sharp)
        patterns[tuple(genus(q, C) == -1 for q in prime_cores)] += 1

    assert all(genus(q, 1) == 1 for q in prime_cores)
    assert slice_masses(1) == (Fraction(), Fraction(), 0, 0)
    assert tuple(round(float(x), 9) for x in
                 (min(raw_masses), median(raw_masses), max(raw_masses))) == (
                     0.0, 1.338510101, 2.428391053)
    assert tuple(round(float(x), 9) for x in
                 (min(sharp_masses), median(sharp_masses), max(sharp_masses))) == (
                     0.0, 1.276010101, 2.324224387)

    # Remove the constructed escape before the empirical independence check.
    random_patterns = Counter()
    for C in classes[1:]:
        random_patterns[tuple(genus(q, C) == -1 for q in prime_cores)] += 1
    negative_marginals = tuple(
        sum(pattern[i] * count for pattern, count in random_patterns.items())
        for i in range(len(prime_cores))
    )
    pair_correlations = tuple(
        sum((1 if pattern[i] == pattern[j] else -1) * count
            for pattern, count in random_patterns.items())
        for i in range(len(prime_cores))
        for j in range(i + 1, len(prime_cores))
    )
    assert (len(random_patterns), max(random_patterns.values())) == (159, 5)
    assert negative_marginals == (138, 120, 132, 136, 128, 145, 128, 138)
    assert (min(pair_correlations), max(pair_correlations),
            sum(map(abs, pair_correlations))) == (-36, 30, 386)

    # Finite tie-back.  Stream one norm at a time and retain no factor table.
    scan_limit = 100_000 if os.environ.get("ES_FULL_SCAN") == "1" else 30_000
    z_data = scan_limit
    hard = tuple(p for p in primerange(2, scan_limit) if p % 24 == 1)
    assert len(hard) == (1181 if scan_limit == 100_000 else 385)
    least_histogram = Counter()
    bounded_good_count = 0
    mass_bands = defaultdict(lambda: [0, 0, Fraction()])
    for P in hard:
        raw_mass, _, _, _ = slice_masses(P)
        least_good = None
        bounded_good = False
        for C, K, s, n, _d in unforced:
            if genus(s, P) != -1:
                continue
            norm = P * P + 4 * C * K * K
            for q in factorint(norm):
                if q % (4 * n) != (-P) % (4 * n):
                    continue
                assert genus(s, P) == -1
                least_good = n if least_good is None else min(least_good, n)
                bounded_good |= q <= z_data
        least_histogram[least_good] += 1
        bounded_good_count += bounded_good

        value = float(raw_mass)
        band = (0 if value < 0.5 else 1 if value < 1.0 else
                2 if value < 1.5 else 3 if value < 2.0 else 4)
        mass_bands[band][0] += 1
        mass_bands[band][1] += not bounded_good
        mass_bands[band][2] += raw_mass

    expected_histogram_small = {
        5: 156, 7: 30, 10: 36, 11: 35, 13: 13, 14: 15, 17: 16,
        19: 4, 21: 15, 22: 9, 23: 6, 26: 10, 28: 4, 29: 3,
        None: 33,
    }
    expected_histogram_full = {
        5: 492, 7: 100, 10: 97, 11: 95, 13: 41, 14: 35, 17: 50,
        19: 19, 21: 50, 22: 19, 23: 17, 26: 34, 28: 7, 29: 9,
        None: 116,
    }
    assert dict(least_histogram) == (expected_histogram_full
                                     if scan_limit == 100_000
                                     else expected_histogram_small)
    assert sum(count for n, count in least_histogram.items() if n is not None) == (
        1065 if scan_limit == 100_000 else 352)
    assert bounded_good_count == (1040 if scan_limit == 100_000 else 345)

    band_rows = tuple(
        (band, count, no_good, round(float(total / count), 6))
        for band, (count, no_good, total) in sorted(mass_bands.items())
    )
    expected_bands_small = (
        (0, 76, 25, 0.324856), (1, 84, 14, 0.831566),
        (2, 62, 1, 1.281912), (3, 88, 0, 1.698663),
        (4, 75, 0, 2.198854),
    )
    expected_bands_full = (
        (0, 259, 103, 0.292388), (1, 244, 36, 0.83155),
        (2, 197, 2, 1.282395), (3, 225, 0, 1.684125),
        (4, 256, 0, 2.195519),
    )
    assert band_rows == (expected_bands_full if scan_limit == 100_000
                         else expected_bands_small)

    print("overlap check (uniform threshold,primes,small collision,duplicate) =",
          (T * T, len(high_primes),
           (q_small, first, second, roots_first), (duplicate_a, duplicate_b, 20)))
    print("Q_30 / sampled raw mass min,median,max / sharp =",
          (Q,
           tuple(round(float(x), 6) for x in
                 (min(raw_masses), median(raw_masses), max(raw_masses))),
           tuple(round(float(x), 6) for x in
                 (min(sharp_masses), median(sharp_masses), max(sharp_masses)))))
    print("INFO prime-core independence (patterns,marginals,corr range) =",
          (len(random_patterns), negative_marginals,
           (min(pair_correlations), max(pair_correlations))))
    print("ck_pr<=30 / good q<=z / INFO no-good mass bands =",
          (sum(v for key, v in least_histogram.items() if key is not None),
           bounded_good_count, band_rows))


print("\n== (az) stacked slice sieve structure and genus asymmetry (§53) ==")
check_az()


# ---------------------------------------------------------------- (ba)
def check_ba():
    """§54: logarithmic Type-II and Type-I residue-one escapes."""
    import os
    from sympy import isprime, kronecker_symbol

    def ordinary_divisors(n):
        values = [1]
        for q, e in factorint(n).items():
            values = [d * q**j for d in values for j in range(e + 1)]
        return values

    # Full Lemma-16.1 harvest for every eligible product modulus in the
    # required range.  The optional extension duplicates (ax)'s conventions
    # farther out without making the ordinary verification heavy.
    modulus_cap = 3000 if os.environ.get("ES_FULL_SCAN") == "1" else 300
    modulus_classes = {}
    datum_count = 0
    for M in range(3, modulus_cap + 1, 4):
        A = (M + 1) // 4
        classes = set()
        for u in ordinary_divisors(A):
            for v in ordinary_divisors(A // u):
                w = A // (u * v)
                assert u * v * w == A and gcd(v, M) == 1
                # This is the self-contained size contradiction in §54.1.
                assert 2 <= u + v <= u * v + 1 <= A + 1 < M
                classes.add((-u * pow(v, -1, M)) % M)
                datum_count += 1
        assert 1 not in classes
        modulus_classes[M] = classes
    assert len(modulus_classes) == (750 if modulus_cap == 3000 else 75)

    # A deliberately awkward datum exercises the freedoms most likely to be
    # lost in a product-modulus shorthand: composite ell, w > 1, and u = v.
    exotic = (1, 95, 2, 2, 6)
    k_ex, ell_ex, u_ex, v_ex, w_ex = exotic
    m_ex = k_ex * ell_ex
    assert not isprime(ell_ex) and u_ex == v_ex and w_ex > 1
    assert u_ex * v_ex * w_ex == (m_ex + 1) // 4
    assert (-u_ex * pow(v_ex, -1, m_ex)) % m_ex in modulus_classes[m_ex]
    assert (-u_ex * pow(v_ex, -1, m_ex)) % m_ex != 1

    # Construct M(T) literally, then find the least prime in its residue-one
    # class.  These regressions complement the product-class harvest above.
    expected_type_ii = ((3, 6, 7), (5, 60, 61),
                        (7, 420, 421), (11, 27720, 55441))
    type_ii_rows = []
    for T, expected_M, expected_P in expected_type_ii:
        M_T = 1
        for n in range(1, T + 1):
            M_T = lcm(M_T, n)
        P = 1 + M_T
        while not isprime(P):
            P += M_T
        assert (M_T, P) == (expected_M, expected_P)
        assert all(M_T % n == 0 for n in range(1, T + 1))
        eligible = tuple(M for M in modulus_classes if M <= T)
        assert all(P % M == 1 and P % M not in modulus_classes[M]
                   for M in eligible)
        type_ii_rows.append((T, M_T, P, eligible,
                             round(log(P) / log(M_T), 9)))

    def squarefree(n):
        return all(e == 1 for e in factorint(n).values())

    def discriminant(s):
        return -s if (-s) % 4 == 1 else -4 * s

    def admissible(P, C, K):
        return (gcd(P, C * K) == 1 and 3 * K <= 2 * P
                and 4 * C * K <= 2 * P + K)

    def direct_slice_mass(P, C, K):
        """Stream (44.2)'s grade counts for one norm."""
        h = 4 * C * K
        factors = factorint(P * P + 4 * C * K * K)
        grades = Counter({1: 1})
        for q, e in factors.items():
            powers = []
            power = 1
            for _ in range(e + 1):
                powers.append(power)
                power = power * q % h
            updated = Counter()
            for grade, count in grades.items():
                for q_power in powers:
                    updated[grade * q_power % h] += count
            grades = updated
        assert sum(grades.values()) == prod(e + 1 for e in factors.values())
        target = (-P) % h
        good_primes = tuple(q for q in factors if q % h == target)
        return grades[target], good_primes

    # Least primes in the three finite residue-one progressions, found by
    # direct search and retained as regression constants.
    expected = ((5, 120, 241), (7, 840, 2521), (11, 9240, 9241))
    rows = []
    for T, expected_R, expected_P in expected:
        R = 24
        for q in primerange(2, T + 1):
            R = lcm(R, q)
        P = 1 + R
        while not isprime(P):
            P += R
        assert (R, P) == (expected_R, expected_P)
        assert P % R == 1 and P % 24 == 1

        # Check the actual quadratic characters, not only congruences.
        for s in range(1, T + 1):
            if not squarefree(s):
                continue
            assert jacobi_symbol(s, P) == 1
            assert kronecker_symbol(discriminant(s), P) == 1

        checked_slices = 0
        for n in range(1, T + 1):
            for C in range(1, n + 1):
                if n % C:
                    continue
                K = n // C
                assert admissible(P, C, K)
                mass, good_primes = direct_slice_mass(P, C, K)
                assert mass == 0 and not good_primes
                checked_slices += 1
        rows.append((T, R, P, checked_slices,
                     round(log(P) / log(R), 9)))

    # The T=11 Type-I prime also misses the complete (ax)-style Type-II
    # harvest through modulus 11, as both residue-one conventions require.
    P11 = expected[-1][2]
    below_11 = tuple(M for M in modulus_classes if M <= 11)
    assert below_11 == (3, 7, 11)
    assert all(P11 % M == 1 and P11 % M not in modulus_classes[M]
               for M in below_11)

    print("residue-one Type-II escape (cap,moduli,data) =",
          (modulus_cap, len(modulus_classes), datum_count))
    print("Type-II least-prime regressions (T,M,p,eligible,log p/log M) =",
          type_ii_rows)
    print("Type-I least-prime regressions (T,R,p,slices,log p/log R) =", rows)
    print("INFO finite least-prime ratios versus effective Linnik L=5.2 =",
          tuple(row[-1] for row in rows))


print("\n== (ba) logarithmic lower tails (§54) ==")
check_ba()



# ---------------------------------------------------------------- (bb)
def check_bb():
    """§55: general-m witness tails, local thinning, and Page-case shadow."""

    def ordinary_divisors(n):
        values = [1]
        for q, e in factorint(n).items():
            values = [d * q**j for d in values for j in range(e + 1)]
        return values

    def factorization_classes(m, M):
        A = (M + 1) // m
        classes = set()
        for u in ordinary_divisors(A):
            for v in ordinary_divisors(A // u):
                w = A // (u * v)
                assert u * v * w == A and gcd(v, M) == 1
                classes.add((-u * pow(v, -1, M)) % M)
        return classes

    def harvest(m, cap=1500):
        family = {}
        for M in range(m - 1, cap + 1, m):
            A = (M + 1) // m
            classes = factorization_classes(m, M)
            intrinsic = {(-m * D) % M for D in divisors_of_square(A)}
            assert classes == intrinsic
            family[M] = classes
        return family

    families = {m: harvest(m) for m in (3, 4, 5, 6, 7)}

    # The m=4 specialization is exactly the factorization and intrinsic-class
    # harvest in (ax), now truncated at 1500.  Keep literal small-modulus
    # regressions so agreement is not only an equality of two formulas.
    ax_style = {
        M: factorization_classes(4, M) for M in range(3, 1501, 4)
    }
    assert families[4] == ax_style
    assert families[4][3] == {2}
    assert families[4][7] == {3, 5, 6}
    assert families[4][23] == {7, 10, 11, 15, 17, 19, 20, 21, 22}

    thresholds = (25, 100, 400)
    expected_tails = {
        3: (0, 0, 0),
        5: (875, 61, 5),
        6: (3136, 663, 77),
        7: (2222, 438, 35),
    }
    expected_unresolved = {3: 0, 5: 1, 6: 17, 7: 10}
    tail_rows, fit_rows = {}, {}
    for m in (3, 5, 6, 7):
        primes = tuple(p for p in primerange(2, 100_001) if gcd(p, m) == 1)
        witness = []
        for p in primes:
            witness.append(next((M for M, classes in families[m].items()
                                 if p % M in classes), None))
        tails = tuple(sum(M is None or M > T for M in witness)
                      for T in thresholds)
        assert tails == expected_tails[m]
        assert sum(M is None for M in witness) == expected_unresolved[m]
        assert all(a >= b for a, b in zip(tails, tails[1:]))
        tail_rows[m] = (len(primes), tails, expected_unresolved[m])

        eta2 = prod((Fraction(q * q, q * q + q - 1)
                     for q in factorint(m)), start=Fraction(1))
        eta1 = prod((Fraction(q, q + 1) for q in factorint(m)),
                    start=Fraction(1))
        phi_m = prod(q**(e - 1) * (q - 1)
                     for q, e in factorint(m).items())
        theta, lam = float(eta2 / phi_m), float(eta1 / phi_m)
        rates = tuple(-log((count + 0.5) / (len(primes) + 0.5))
                      for count in tails)
        cubic = tuple(rate / (theta * log(T)**3)
                      for rate, T in zip(rates, thresholds))
        layer1 = tuple(rate / (lam * log(T)**2 * log(2 + log(T)))
                       for rate, T in zip(rates, thresholds))
        fit_rows[m] = (tuple(round(x, 5) for x in layer1),
                       tuple(round(x, 5) for x in cubic))

    # Exact Euler-factor computation behind (43.4), including repeated-prime
    # denominators (only the support of m matters).
    expected_eta2 = {
        3: Fraction(9, 11),
        5: Fraction(25, 29),
        6: Fraction(36, 55),
        7: Fraction(49, 55),
    }
    eta_rows = {}
    for m in (3, 5, 6, 7):
        product_formula = prod(
            (Fraction(q * q, q * q + q - 1) for q in factorint(m)),
            start=Fraction(1))
        direct_local = Fraction(1)
        for q in factorint(m):
            harmonic_factor = Fraction(q * q + q - 1, q * q)
            direct_local *= 1 / harmonic_factor
        assert product_formula == direct_local == expected_eta2[m]
        eta_rows[m] = product_formula

    # The residue-side repair is a weighted multiplier-mass statement, not
    # merely existence of both signs.  Check its finite shadow for r=5|m=5
    # and for the concrete r=3|m=6 review case.  The asymptotic proof is the
    # dyadic progression argument (55.17), not this bounded computation.
    def euler_phi(n):
        value = n
        for q in factorint(n):
            value = value // q * (q - 1)
        return value

    sign_balance = {}
    for m, r in ((5, 5), (6, 3)):
        signs = {
            int(jacobi_symbol((-pow(b, -1, r)) % r, r))
            for b in range(1, m + 1) if gcd(b, m) == 1
        }
        assert signs == {-1, 1}
        total = sum((Fraction(euler_phi(k), k * k)
                     for k in range(1, 1501) if gcd(k, m) == 1),
                    start=Fraction(0))
        favorable_mass = sum(
            (Fraction(euler_phi(k), k * k)
             for k in range(1, 1501) if gcd(k, m) == 1
             and jacobi_symbol((-pow(k, -1, r)) % r, r) == -1),
            start=Fraction(0))
        ratio = favorable_mass / total
        assert Fraction(1, 3) < ratio < Fraction(3, 4)
        sign_balance[(m, r)] = round(float(ratio), 6)

    # If the Page conductor r=5 divides m=5, the BV modulus is q=muv, not uv.
    # Hence deletion is not vacuous: every such q is a multiple of 5.  The
    # effective repair instead keeps multipliers with chi_5(-k^{-1})=-1,
    # for which the exceptional explicit-formula term has the helpful sign.
    page_data = []
    favorable = unfavorable = 0
    for M in range(4, 1501, 5):
        A = (M + 1) // 5
        for k in ordinary_divisors(M):
            ell = M // k
            ell_fac = factorint(ell)
            if len(ell_fac) != 1 or next(iter(ell_fac.values())) != 1:
                continue
            for u in ordinary_divisors(A):
                for v in ordinary_divisors(A // u):
                    q_bv = 5 * u * v
                    assert q_bv % 5 == 0
                    sign = jacobi_symbol((-pow(k, -1, 5)) % 5, 5)
                    favorable += sign == -1
                    unfavorable += sign == 1
                    if len(page_data) < 8:
                        page_data.append((M, k, ell, u, v, q_bv, int(sign)))
    assert favorable > 0 and unfavorable > 0

    print("general-m W_m<=1500 tails (m:(prime count,tails,unresolved)) =",
          tail_rows)
    print("eta_2 exact values =", eta_rows)
    print("INFO fitted c by m (Layer-1,cubic) =", fit_rows)
    print("finite favorable harmonic-mass ratios (m,r) =", sign_balance)
    print("r=5|m Page shadow (favorable,unfavorable,sample q=muv data) =",
          (favorable, unfavorable, tuple(page_data)))


print("\n== (bb) general-numerator tails and effectivity (§55) ==")
check_bb()


# Shared exact Lemma-16.1/Lemma-18.1 harvest.  Blocks (bc) and (bd) call
# this with the same cap, so (bd) reuses the cached object rather than
# silently rebuilding a second class system.
_complete_multiplier_harvest_cache = {}


def complete_multiplier_harvest(modulus_cap):
    if modulus_cap not in _complete_multiplier_harvest_cache:
        rows = []
        for M in range(3, modulus_cap + 1, 4):
            A = (M + 1) // 4
            classes = frozenset(
                (-4 * D) % M for D in divisors_of_square(A)
            )
            rows.append((M, classes))
        _complete_multiplier_harvest_cache[modulus_cap] = tuple(rows)
    return _complete_multiplier_harvest_cache[modulus_cap]


# ---------------------------------------------------------------- (bc)
def check_bc():
    """§56: congruence ceilings and streamed extremal censuses."""
    import os

    full_scan = os.environ.get("ES_FULL_SCAN") == "1"

    def hard_primes_below(limit, chunk_size=100_000):
        """Stream hard primes through bounded sieve intervals."""
        for low in range(2, limit, chunk_size):
            high = min(limit, low + chunk_size)
            for P in primerange(low, high):
                if P % 24 == 1:
                    yield P

    def strict_records(values, ordered_primes):
        records, running = [], -1
        for P in ordered_primes:
            if values[P] > running:
                running = values[P]
                records.append((P, running))
        return tuple(records)

    def normalized_maxima(values, ordered_primes):
        rows = []
        for mode in range(3):
            best = (-1.0, -1, -1)
            for P in ordered_primes:
                log_P = log(P)
                denominator = (log_P, log_P * log(log_P), log_P * log_P)[mode]
                candidate = (values[P] / denominator, P, values[P])
                if candidate[0] > best[0]:
                    best = candidate
            rows.append(best)
        return tuple(rows)

    # Full Lemma-16.1/Lemma-18.1 harvest through the fixed modulus cap.
    # The classes are small; primes are streamed and stop at their first hit.
    modulus_cap = 3000
    modulus_classes = complete_multiplier_harvest(modulus_cap)
    for M, classes in modulus_classes:
        A = (M + 1) // 4
        # D=1 is the class used in Theorem 56.1.  Its explicit dictionary is
        # (u,v,w)=(1,A,1), not merely an appeal to the intrinsic formula.
        assert A == 1 * A * 1 and gcd(A, M) == 1
        assert (-pow(A, -1, M)) % M == (-4) % M in classes
    assert len(modulus_classes) == 750

    W_limit = 10_000_000 if full_scan else 1_000_000
    W_records, W_running, W_count = [], -1, 0
    W_maxima = [(-1.0, -1, -1) for _ in range(3)]
    for P in hard_primes_below(W_limit):
        W_count += 1
        witness = next((M for M, classes in modulus_classes
                        if P % M in classes), None)
        assert witness is not None, ("W cap exhausted", P, modulus_cap)
        if witness > W_running:
            W_running = witness
            W_records.append((P, witness))
        log_P = log(P)
        for mode, denominator in enumerate(
                (log_P, log_P * log(log_P), log_P * log_P)):
            candidate = (witness / denominator, P, witness)
            if candidate[0] > W_maxima[mode][0]:
                W_maxima[mode] = candidate

    expected_W_default = (
        (73, 7), (193, 15), (1201, 31), (2521, 47), (3361, 99),
        (33_289, 155), (90_841, 167), (144_169, 191), (167_521, 259),
        (225_289, 279), (361_321, 287), (915_961, 303), (954_409, 335),
    )
    expected_W_full = expected_W_default + (
        (1_853_329, 383), (2_031_121, 2495),
    )
    assert W_count == (82_887 if full_scan else 9_732)
    assert tuple(W_records) == (expected_W_full if full_scan
                                else expected_W_default)
    expected_W_maxima = (
        ((171.783468, 2_031_121, 2495),
         (64.198698, 2_031_121, 2495),
         (11.827479, 2_031_121, 2495))
        if full_scan else
        ((24.330286, 954_409, 335),
         (9.277839, 954_409, 335),
         (1.836625, 225_289, 279))
    )
    assert tuple((round(value, 6), P, W)
                 for value, P, W in W_maxima) == expected_W_maxima

    # Joint ck_pr and unrestricted-slice scan.  Product order and unresolved
    # sets avoid recomputation.  Genus-forced pairs are skipped before
    # factorization; every surviving norm is factored and discarded at once.
    slice_limit = 1_000_000 if full_scan else 300_000
    hard = tuple(hard_primes_below(slice_limit))
    assert len(hard) == (9_732 if full_scan else 3_202)
    unresolved_prime, unresolved_slice = set(hard), set(hard)
    prime_min, slice_min = {}, {}
    core_cache = {}

    def squarefree_core(n):
        if n not in core_cache:
            core_cache[n] = prod(q for q, e in factorint(n).items() if e % 2)
        return core_cache[n]

    def exponent_box_hit(P, C, K, factors):
        h = 4 * C * K
        residues = {1}
        for q, e in factors.items():
            powers, power = [], 1
            for _ in range(e + 1):
                powers.append(power)
                power = power * q % h
            residues = {a * b % h for a in residues for b in powers}
            assert len(residues) <= h
        return (-P) % h in residues

    guard = 1000 if full_scan else 500
    factorizations = 0
    for n in range(1, guard + 1):
        for C in range(1, n + 1):
            if n % C:
                continue
            K = n // C
            core = squarefree_core(C)
            if core in (1, 2, 3, 6):
                continue
            for P in tuple(unresolved_prime | unresolved_slice):
                if (gcd(P, n) != 1 or 3 * K > 2 * P
                        or 4 * n > 2 * P + K):
                    continue
                # On hard primes chi_core(P)=(core/P).  A +1 sign is the
                # exact genus-forced zero and cannot resolve either minimum.
                if pow(core, (P - 1) // 2, P) != P - 1:
                    continue
                norm = P * P + 4 * C * K * K
                factors = factorint(norm)
                factorizations += 1

                if P in unresolved_slice and exponent_box_hit(
                        P, C, K, factors):
                    slice_min[P] = n
                    unresolved_slice.remove(P)

                if P in unresolved_prime:
                    good_primes = tuple(q for q in factors
                                        if q % (4 * n) == (-P) % (4 * n))
                    if good_primes:
                        q = min(good_primes)
                        E = norm // q
                        A, B = (P + q) // (4 * n), (P + E) // (4 * n)
                        assert min(A, B) > 0
                        assert q % (4 * n) == E % (4 * n) == (-P) % (4 * n)
                        assert P * (A + B) == K * (4 * A * B * C - 1)
                        assert (Fraction(1, A * C * K)
                                + Fraction(1, B * C * K)
                                + Fraction(1, P * A * B * C)
                                == Fraction(4, P))
                        prime_min[P] = n
                        unresolved_prime.remove(P)
        if not unresolved_prime and not unresolved_slice:
            break
    assert not unresolved_prime, ("ck_pr guard exhausted", sorted(unresolved_prime))
    assert not unresolved_slice, ("ck_min guard exhausted", sorted(unresolved_slice))
    assert n == (898 if full_scan else 461)
    assert factorizations == (47_100 if full_scan else 14_143)
    assert all(prime_min[P] >= slice_min[P] for P in hard)

    prime_records_default = (
        (73, 7), (193, 10), (241, 21), (1201, 34), (2521, 38),
        (4729, 66), (7489, 70), (9601, 78), (31_081, 110),
        (51_769, 249), (83_689, 282), (113_161, 378), (171_481, 461),
    )
    prime_records_full = prime_records_default + (
        (319_489, 878), (538_561, 898),
    )
    slice_records_default = (
        (73, 7), (193, 10), (241, 11), (769, 13), (1321, 21),
        (2281, 26), (2521, 38), (9601, 67), (12_289, 77),
        (55_441, 83), (92_401, 103),
    )
    slice_records_full = slice_records_default + ((414_241, 218),)
    assert strict_records(prime_min, hard) == (
        prime_records_full if full_scan else prime_records_default)
    assert strict_records(slice_min, hard) == (
        slice_records_full if full_scan else slice_records_default)

    D_values = {P: slice_min[P] - 1 for P in hard}
    prime_maxima = normalized_maxima(prime_min, hard)
    D_maxima = normalized_maxima(D_values, hard)
    expected_prime_maxima = (
        ((69.273069, 319_489, 878),
         (27.277261, 319_489, 878),
         (5.465556, 319_489, 878))
        if full_scan else
        ((38.250190, 171_481, 461),
         (15.366153, 171_481, 461),
         (3.173703, 171_481, 461))
    )
    expected_D_maxima = (
        ((16.777222, 414_241, 217),
         (6.553922, 414_241, 217),
         (1.297121, 414_241, 217))
        if full_scan else
        ((8.920846, 92_401, 102),
         (3.661213, 92_401, 102),
         (0.857113, 12_289, 76))
    )
    assert tuple((round(value, 6), P, depth)
                 for value, P, depth in prime_maxima) == expected_prime_maxima
    assert tuple((round(value, 6), P, depth)
                 for value, P, depth in D_maxima) == expected_D_maxima

    print("W census (limit,count,cap,max,records) =",
          (W_limit, W_count, modulus_cap, W_running, tuple(W_records)))
    print("INFO W normalized maxima (ratio,p,W) =", tuple(W_maxima))
    print("ck_pr/D census (limit,count,max ck_pr,max D,factorizations) =",
          (slice_limit, len(hard), max(prime_min.values()),
           max(D_values.values()), factorizations))
    print("ck_pr records / D records =",
          (strict_records(prime_min, hard), strict_records(D_values, hard)))
    print("INFO ck_pr / D normalized maxima =", (prime_maxima, D_maxima))


print("\n== (bc) congruence-certificate ceilings and extremal census (§56) ==")
check_bc()


# ---------------------------------------------------------------- (bd)
def check_bd():
    """§57: crossing arithmetic, exact harvested tails, and toy lcm growth."""
    import os
    from time import perf_counter

    started = perf_counter()

    # Exact displayed logarithms from (57.4)--(57.5), followed by the
    # fixed-margin asymptotic ratios used only for the printed calibration.
    def cubic_log_rhs(L, theta, b=1.0, c=1.0, C=1.0):
        return log(C) + L - c * b**3 * L ** (3 * theta)

    def square_log_rhs(L, theta, b=1.0, c=1.0, C=1.0):
        t = b * L**theta
        return log(C) + L - c * t * t * log(2 + t)

    L_grid = (10**3, 10**4, 10**5, 10**6)
    displayed_cubic = {
        theta: tuple(cubic_log_rhs(L, theta) for L in L_grid)
        for theta in (0.25, 0.40)
    }
    displayed_square = {
        theta: tuple(square_log_rhs(L, theta) for L in L_grid)
        for theta in (0.40, 0.50)
    }
    assert all(value > 0 for value in displayed_cubic[0.25])
    assert all(value < 0 for value in displayed_cubic[0.40])
    assert displayed_square[0.40][-1] > 0
    assert all(value < 0 for value in displayed_square[0.50])
    endpoint_L = 10**4
    assert cubic_log_rhs(endpoint_L, 1 / 3, C=0.5) < 0
    assert abs(cubic_log_rhs(endpoint_L, 1 / 3, C=1.0)) < 1e-10
    assert cubic_log_rhs(endpoint_L, 1 / 3, C=2.0) > 0

    # Write t=log T=L^theta and compare the dominant saving with 2L.
    # The factor 2 is a display normalization, not the exact threshold.
    cubic_thetas = (0.25, 0.36, 0.40)
    cubic_ratios = {
        theta: tuple(L ** (3 * theta) / (2 * L) for L in L_grid)
        for theta in cubic_thetas
    }
    assert all(ratio < 1 for ratio in cubic_ratios[0.25])
    assert cubic_ratios[0.36][0] < 1 < cubic_ratios[0.36][-1]
    assert all(ratio > 1 for ratio in cubic_ratios[0.40])
    cubic_crossings = {
        theta: 2 ** (1 / (3 * theta - 1))
        for theta in cubic_thetas if theta > 1 / 3
    }
    assert abs(cubic_crossings[0.40] - 32) < 1e-10

    square_thetas = (0.40, 0.50, 0.55)
    square_ratios = {
        theta: tuple(
            (L ** (2 * theta)) * log(L ** theta) / (2 * L)
            for L in L_grid
        )
        for theta in square_thetas
    }
    assert all(ratio < 1 for ratio in square_ratios[0.40])
    assert all(ratio > 1 for ratio in square_ratios[0.50])
    assert all(ratio > 1 for ratio in square_ratios[0.55])
    # At theta=1/2 the equation t^2 log(t)=2L is log L=4.
    square_half_crossing = exp(4)
    assert square_half_crossing < L_grid[0]

    print("displayed log bounds (57.4), cubic =", displayed_cubic)
    print("displayed log bounds (57.5), square-log =", displayed_square)
    print("threshold ratios saving/(2 log N), cubic =", cubic_ratios)
    print("threshold ratios saving/(2 log N), square-log =", square_ratios)
    print("threshold crossing log N (c=1) =",
          (cubic_crossings, (0.50, square_half_crossing)))

    # Exact complete Lemma-16.1 harvest.  Fraction arithmetic computes
    # m(T)=sum omega(M)/M without floating-point loss.  The interval scan is
    # chunked, and each chunk retains only one byte per integer.
    thresholds = (100, 300, 1000, 3000)
    modulus_classes = complete_multiplier_harvest(thresholds[-1])
    assert modulus_classes is complete_multiplier_harvest(thresholds[-1])

    masses = tuple(
        sum((Fraction(len(classes), M)
             for M, classes in modulus_classes if M <= T), Fraction())
        for T in thresholds
    )
    expected_mass_decimals = (
        4.248031290751, 7.349236274282, 12.171587320339, 18.126592298585,
    )
    assert tuple(round(float(mass), 12) for mass in masses) == (
        expected_mass_decimals
    )

    full_scan = os.environ.get("ES_FULL_SCAN") == "1"
    scan_limit = 10_000_000 if full_scan else 300_000
    chunk_size = 100_000
    integer_tails = [0] * len(thresholds)
    prime_tails = [0] * len(thresholds)
    total_primes = 0

    for low in range(1, scan_limit + 1, chunk_size):
        high = min(scan_limit + 1, low + chunk_size)
        size = high - low
        covered = bytearray(size)
        chunk_primes = tuple(primerange(max(2, low), high))
        total_primes += len(chunk_primes)
        modulus_index = 0

        for threshold_index, T in enumerate(thresholds):
            while (modulus_index < len(modulus_classes)
                   and modulus_classes[modulus_index][0] <= T):
                M, classes = modulus_classes[modulus_index]
                for residue in classes:
                    first = low + (residue - low) % M
                    offset = first - low
                    if offset < size:
                        count = (size - 1 - offset) // M + 1
                        covered[offset::M] = b"\1" * count
                modulus_index += 1
            integer_tails[threshold_index] += size - sum(covered)
            prime_tails[threshold_index] += sum(
                not covered[P - low] for P in chunk_primes
            )

        # At the final threshold, replay §58's square escape inside this
        # exact finite box rather than treating the integer plateau as noise.
        first_square = isqrt(low - 1) + 1
        last_square = isqrt(high - 1)
        assert all(not covered[s * s - low]
                   for s in range(first_square, last_square + 1))

    square_survivors = isqrt(scan_limit)
    assert all(tail >= square_survivors for tail in integer_tails)
    if not full_scan:
        assert square_survivors == 547
        assert total_primes == 25_997
        assert tuple(integer_tails) == (5516, 1064, 569, 550)
        assert tuple(prime_tails) == (76, 5, 0, 0)
        assert (integer_tails[2] - square_survivors,
                integer_tails[3] - square_survivors) == (22, 3)

    calibration = []
    for T, mass, integer_tail, prime_tail in zip(
            thresholds, masses, integer_tails, prime_tails):
        fair_density = exp(-float(mass))
        calibration.append((
            T,
            round(float(mass), 12),
            integer_tail,
            prime_tail,
            (integer_tail / scan_limit) / fair_density,
            (prime_tail / total_primes) / fair_density,
        ))
    print("exact-harvest calibration (T,m(T),integer tail,prime tail) =",
          tuple(row[:4] for row in calibration))
    print("INFO observed-density / exp(-m(T)) (T,integer,prime) =",
          tuple((row[0], row[4], row[5]) for row in calibration))

    # A finite structural toy for the degree/modulus transition.  At cap X,
    # use every distinct harvested atom through X, take N_toy=X^2=e^(2t),
    # and count compatible degree-m sets with lcm>N_toy exactly.
    toy_rows = []
    for cap in (15, 23, 31):
        atoms = []
        for M, classes in modulus_classes:
            if M > cap:
                break
            atoms.extend((M, residue) for residue in classes)
        for degree in (2, 3, 4):
            compatible_count = exceeding_count = 0
            for atom_set in combinations(atoms, degree):
                compatible = all(
                    (left[1] - right[1]) % gcd(left[0], right[0]) == 0
                    for left, right in combinations(atom_set, 2)
                )
                if not compatible:
                    continue
                compatible_count += 1
                atom_lcm = lcm(*(atom[0] for atom in atom_set))
                exceeding_count += atom_lcm > cap * cap
            toy_rows.append((cap, degree, len(atoms),
                             compatible_count, exceeding_count))
    expected_toy_rows = (
        (15, 2, 11, 41, 0), (15, 3, 11, 57, 45),
        (15, 4, 11, 18, 18), (23, 2, 23, 200, 0),
        (23, 3, 23, 846, 765), (23, 4, 23, 1809, 1809),
        (31, 2, 31, 393, 0), (31, 3, 31, 2653, 2418),
        (31, 4, 31, 10389, 10371),
    )
    assert tuple(toy_rows) == expected_toy_rows
    print("toy atom-lcm table (X,degree,atoms,compatible,lcm>X^2) =",
          tuple(toy_rows))
    print("verify (bd) runtime seconds =", round(perf_counter() - started, 3))


print("\n== (bd) supercritical-window arithmetic and calibration (§57) ==")
check_bd()
def check_be():
    """§58: moving inverse censuses, shifted classes, and square escape."""
    import os

    full_scan = os.environ.get("ES_FULL_SCAN") == "1"
    # The structural replay always reaches 3000.  ES_FULL_SCAN gates only the
    # additional inverse thresholds, not correctness coverage of square escape.
    modulus_cap = 3000
    grid = [3, 7, 15, 31, 63, 100, 200, 335, 382, 500, 750,
            1000, 1250, 1500, 1750, 2000]
    if full_scan:
        grid += [2200, 2400, 2494]

    def primes_below_chunked(limit, chunk_size=100_000):
        """Generate primes in bounded-memory intervals [low, high)."""
        for low in range(2, limit, chunk_size):
            high = min(limit, low + chunk_size)
            yield from primerange(low, high)

    # Complete Lemma-18.1 harvest, independently compared with every original
    # (u,v,w) class.  Taking k=1, ell=M covers the original k*ell quantifier.
    from sympy import divisors as _divisors
    modulus_classes = []
    class_by_modulus = {}
    divisor_data_count = distinct_class_count = 0
    for M in range(3, modulus_cap + 1, 4):
        A = (M + 1) // 4
        square_divs = divisors_of_square(A)
        classes = {(-4 * D) % M for D in square_divs}
        original_classes = {
            (-u * pow(v, -1, M)) % M
            for u in _divisors(A) for v in _divisors(A // u)
        }
        assert original_classes == classes, (M, original_classes ^ classes)
        divisor_data_count += len(square_divs)
        distinct_class_count += len(classes)
        modulus_classes.append((M, classes, square_divs))
        class_by_modulus[M] = classes
    assert len(modulus_classes) == 750
    assert divisor_data_count == 15_754
    assert distinct_class_count == 14_745
    assert modulus_cap >= max(grid)

    def W_through_cap(n):
        return next((M for M, classes, _ in modulus_classes
                     if n % M in classes), None)

    # The tiny values explain why the moving convention n,p>T is used.
    assert W_through_cap(1) is None
    assert W_through_cap(2) == 3
    assert W_through_cap(3) == 7
    assert W_through_cap(4) is None

    # Stream once and resolve all integer thresholds as soon as both strict
    # inequalities n>T and W(n)>T hold.
    unresolved = set(grid)
    L_int = {}
    for n in range(1, (int(max(grid) ** 0.5) + 2) ** 2 + 1):
        witness = W_through_cap(n)
        for T in tuple(unresolved):
            if n > T and (witness is None or witness > T):
                L_int[T] = n
                unresolved.remove(T)
        if not unresolved:
            break
    assert not unresolved

    # Prime and hard-prime inverses are streamed together.  The endpoint is
    # the last §56 record needed by every default/full threshold here.
    unresolved_p, unresolved_h = set(grid), set(grid)
    L_p, L_h = {}, {}
    for P in primes_below_chunked(2_031_122):
        witness = W_through_cap(P)
        for T in tuple(unresolved_p):
            if P > T and (witness is None or witness > T):
                L_p[T] = (P, witness)
                unresolved_p.remove(T)
        if P % 24 == 1:
            for T in tuple(unresolved_h):
                if P > T and (witness is None or witness > T):
                    L_h[T] = (P, witness)
                    unresolved_h.remove(T)
        if not unresolved_p and not unresolved_h:
            break
    assert not unresolved_p and not unresolved_h

    expected_default = (
        (3, 4, 7, 11, 73, 7),
        (7, 9, 37, 15, 193, 15),
        (15, 16, 79, 23, 1201, 31),
        (31, 36, 211, 43, 2521, 47),
        (63, 64, 1381, 83, 3361, 99),
        (100, 121, 10_399, 103, 33_289, 155),
        (200, 225, 22_621, 419, 167_521, 259),
        (335, 336, 22_621, 419, 1_853_329, 383),
        (382, 400, 22_621, 419, 1_853_329, 383),
        (500, 529, 206_299, 695, 2_031_121, 2495),
        (750, 784, 2_031_121, 2495, 2_031_121, 2495),
        (1000, 1024, 2_031_121, 2495, 2_031_121, 2495),
        (1250, 1296, 2_031_121, 2495, 2_031_121, 2495),
        (1500, 1521, 2_031_121, 2495, 2_031_121, 2495),
        (1750, 1764, 2_031_121, 2495, 2_031_121, 2495),
        (2000, 2025, 2_031_121, 2495, 2_031_121, 2495),
    )
    expected_full_tail = (
        (2200, 2209, 2_031_121, 2495, 2_031_121, 2495),
        (2400, 2401, 2_031_121, 2495, 2_031_121, 2495),
        (2494, 2500, 2_031_121, 2495, 2_031_121, 2495),
    )
    actual = tuple((T, L_int[T], L_p[T][0], L_p[T][1],
                    L_h[T][0], L_h[T][1]) for T in grid)
    assert actual == expected_default + (expected_full_tail if full_scan else ())

    # Replay the definition, including every nonsurvivor before each reported
    # minimum.  In particular L_int(2000)=2025 checks all 2001..2024 rather
    # than inferring the answer merely because 2025 is the next square.
    for T in grid:
        for n in range(int(T) + 1, L_int[T]):
            witness = W_through_cap(n)
            assert witness is not None and witness <= T, (T, n, witness)
        witness = W_through_cap(L_int[T])
        assert witness is None or witness > T
    assert all(W_through_cap(n) is not None and W_through_cap(n) <= 2000
               for n in range(2001, 2025))

    # Exact consistency with the two hard-prime records in §56.
    assert W_through_cap(954_409) == 335
    assert W_through_cap(1_853_329) == 383
    assert W_through_cap(2_031_121) == 2495
    for T in range(335, 383):
        # There is no new hard prime to rescan: strict record order makes the
        # endpoint 1,853,329 the inverse throughout this entire interval.
        assert 335 <= T < 383
        assert W_through_cap(954_409) <= T < W_through_cap(1_853_329)

    # D=2 is eligible at a prime ell≡3 (mod 4) exactly for ell≡7 (mod 8).
    primes_3 = tuple(P for P in primerange(3, 3001) if P % 4 == 3)
    for ell in primes_3:
        A = (ell + 1) // 4
        assert ((A * A) % 2 == 0) == (ell % 8 == 7)

    # Exhaust every harvested divisor and every square m^2<=10^6 at every
    # eligible M<=3000.  Set membership against the complete class set checks
    # all 15,754,000 (M,D,m) incidences without materializing that product.
    square_membership_checks = 0
    for M, classes, divs in modulus_classes:
        A = (M + 1) // 4
        assert gcd(A, M) == 1
        for D in divs:
            assert gcd(D, M) == 1
            assert jacobi_symbol(D, M) == 1
            assert jacobi_symbol(-4 * D, M) == -1
        for m in range(1, 1001):
            assert (m * m) % M not in classes, (M, m)
            square_membership_checks += 1
    assert square_membership_checks == 750_000
    assert divisor_data_count * 1000 == 15_754_000

    # Explicit D=1 and D=2 shifted classes, including actual least-W replay.
    for ell in primes_3:
        if ell > modulus_cap:
            continue
        assert (-4) % ell in class_by_modulus[ell]
        for multiplier in (2, 3):
            n = multiplier * ell - 4
            assert n > 0 and W_through_cap(n) <= ell
        if ell % 8 == 7:
            assert (-8) % ell in class_by_modulus[ell]
            for multiplier in (2, 3):
                n = multiplier * ell - 8
                assert n > 0 and W_through_cap(n) <= ell

    # Necessary shifted conditions replayed against every inverse row and a
    # bounded population census at a representative threshold.
    census_values = set(L_int.values())
    census_values.update(P for P, witness in L_p.values())
    census_values.update(P for P, witness in L_h.values())
    for T in grid:
        for n in (L_int[T], L_p[T][0], L_h[T][0]):
            witness = W_through_cap(n)
            assert n > T and (witness is None or witness > T)
            assert all((n + 4) % ell for ell in primes_3 if ell <= T)
            assert all((n + 8) % ell for ell in primes_3
                       if ell <= T and ell % 8 == 7)
    spot_T = 335
    for n in range(spot_T + 1, 10_001):
        witness = W_through_cap(n)
        if witness is None or witness > spot_T:
            assert all((n + 4) % ell for ell in primes_3 if ell <= spot_T)
            assert all((n + 8) % ell for ell in primes_3
                       if ell <= spot_T and ell % 8 == 7)

    # Both constructive integer upper bounds, and comparison with the true
    # moving inverse on the complete finite grid.
    for T in grid:
        square_bound = (int(T ** 0.5) + 1) ** 2
        assert T < L_int[T] <= square_bound <= T + 2 * T ** 0.5 + 1 + 1e-12
    for T in (3, 7, 15, 31, 63):
        MT = 1
        for m in range(1, T + 1):
            MT = lcm(MT, m)
        witness = W_through_cap(MT + 1)
        assert witness is None or witness > T

    expected_ratios = {
        31: ((1.044, .11560), (1.558, .17264), (2.281, .25266)),
        100: ((1.041, .04796), (2.008, .09249), (2.261, .10413)),
        335: ((1.001, .01736), (1.725, .02993), (2.482, .04308)),
        382: ((1.008, .01568), (1.686, .02625), (2.427, .03778)),
        500: ((1.009, .01254), (1.969, .02447), (2.337, .02905)),
        1000: ((1.003, .00693), (2.103, .01452), (2.103, .01452)),
        2000: ((1.002, .00381), (1.911, .00726), (1.911, .00726)),
    }
    for T, expected in expected_ratios.items():
        values = (L_int[T], L_p[T][0], L_h[T][0])
        got = tuple((round(log(value) / log(T), 3),
                     round(log(value) / T, 5)) for value in values)
        assert got == expected

    print("moving inverse census (T,L_int,L_p,Wp,L_h,Wh) =", actual)
    print("square/full-system replay (moduli,divisor data,distinct classes,"
          "square checks,incidences) =",
          (len(modulus_classes), divisor_data_count, distinct_class_count,
           square_membership_checks, divisor_data_count * 1000))
    print("D=1/D=2 shifted conditions and hard-record interval checked")


print("\n== (be) inverse census and Jacobsthal integer/prime split (§58) ==")
check_be()


# ---------------------------------------------------------------- (bf)
def check_bf():
    """§59: polynomial escape obstructions and nonsquare tail candidates."""
    import os

    full_scan = os.environ.get("ES_FULL_SCAN") == "1"

    def squarefree_kernel(n):
        assert n > 0
        return prod(p for p, e in factorint(n).items() if e % 2)

    def negative_quadratic_discriminant(n):
        """Fundamental discriminant of Q(sqrt(-n)), n>0."""
        radicand = -squarefree_kernel(n)
        return radicand if radicand % 4 == 1 else 4 * radicand

    # Lemma 59.1 on a bounded complete local system.  Every square polynomial
    # avoids every harvested class.  The two nonsquares pass D=1 but are hit
    # by the displayed later shifts.
    local_rows = complete_multiplier_harvest(3000)
    for M, classes in local_rows:
        if M > 199:
            break
        assert all((x * x) % M not in classes for x in range(M))
        assert all(((2 * x + 1) ** 2) % M not in classes for x in range(M))
    assert (2**4 - 3 + 4 * 2) % 7 == 0
    assert 2 in divisors_of_square((7 + 1) // 4)

    # Several nonsquare quadratics whose f+4 discriminant is a negative
    # square pass the complete D=1 prime layer but are hit by another D.
    d1_pass_samples = (
        # (a,b,c, M,D,x)
        (2, 2, -3, 11, 3, 3),
        (1, -4, 1, 7, 2, 5),
        (1, -6, 30, 11, 3, 3),
    )
    for a, b, c0, M, D, x in d1_pass_samples:
        delta_1 = b * b - 4 * a * (c0 + 4)
        assert delta_1 < 0 and isqrt(-delta_1) ** 2 == -delta_1
        assert b * b != 4 * a * c0
        for p in primerange(3, 2000):
            if p % 4 == 3:
                assert not any((a * y * y + b * y + c0 + 4) % p == 0
                               for y in range(p))
        assert D != 1 and D in divisors_of_square((M + 1) // 4)
        assert (a * x * x + b * x + c0 + 4 * D) % M == 0

    # Finite discriminant-character replay of the D=1 dichotomy.  In this
    # box, exactly the negative-square discriminants have no QR value at a
    # tested prime 3 mod 4 (away from the finite bad primes).
    character_primes = tuple(p for p in primerange(3, 20_000) if p % 4 == 3)
    discriminant_rows = 0
    for delta in range(-200, 201):
        if delta == 0:
            continue
        symbols = tuple(jacobi_symbol(delta, p) for p in character_primes
                        if delta % p)
        negative_square = delta < 0 and isqrt(-delta) ** 2 == -delta
        if negative_square:
            assert symbols and all(symbol == -1 for symbol in symbols)
        else:
            assert 1 in symbols, delta
        discriminant_rows += 1
    assert discriminant_rows == 400

    # Replay the coefficient-dependent q construction in (59.14).  If
    # B=r^2-16a is nonzero, q occurs once in S_D but not in 4R(D), so the
    # quadratic field conductor has a cyclotomic coordinate omitted by Q_D.
    construction_rows = 0
    for a in range(1, 21):
        for r in range(1, 21):
            B = r * r - 16 * a
            if B == 0:
                continue
            q = next(p for p in primerange(3, 200) if (2 * a * B) % p)
            q2 = q * q
            double_root_lift = (-B * pow(16 * a, -1, q2)) % q2
            D = (double_root_lift + q) % q2
            assert D > 0 and D % q
            S_D = 16 * a * D + B
            assert S_D > 0 and S_D % q == 0 and S_D % q2
            R_D = prod(p ** ((e + 1) // 2)
                       for p, e in factorint(D).items())
            Q_D = 4 * R_D
            field_conductor = abs(negative_quadratic_discriminant(S_D))
            assert field_conductor % q == 0 and Q_D % q
            construction_rows += 1
    assert construction_rows == 396

    # In the square case S_D=16d^2D, the quadratic field conductor is always
    # already present in 4R(D), as required by the local obstruction.
    for d in range(1, 21):
        for D in range(1, 101):
            conductor = abs(negative_quadratic_discriminant(16 * d * d * D))
            R_D = prod(p ** ((e + 1) // 2)
                       for p, e in factorint(D).items())
            assert (4 * R_D) % conductor == 0

    # Complete, memory-bounded nonsquare survivor census.  The bytearray is
    # the only population-sized state; classes are added in threshold order.
    population_limit = 1_000_000 if full_scan else 300_000
    thresholds = (100, 300, 1000, 3000)
    covered = bytearray(population_limit + 1)
    modulus_index = 0
    nonsquare_counts = []
    final_nonsquares = []
    for T in thresholds:
        while (modulus_index < len(local_rows)
               and local_rows[modulus_index][0] <= T):
            M, classes = local_rows[modulus_index]
            for residue in classes:
                first = residue if residue else M
                if first <= population_limit:
                    count = (population_limit - first) // M + 1
                    covered[first::M] = b"\1" * count
            modulus_index += 1
        survivors = [n for n in range(1, population_limit + 1)
                     if not covered[n] and isqrt(n) ** 2 != n]
        nonsquare_counts.append(len(survivors))
        if T == thresholds[-1]:
            final_nonsquares = survivors

    expected_counts = ((17_007, 1841, 77, 4) if full_scan
                       else (4969, 517, 22, 3))
    expected_final = ([288, 336, 4545, 643_245] if full_scan
                      else [288, 336, 4545])
    assert tuple(nonsquare_counts) == expected_counts
    assert final_nonsquares == expected_final

    # Exact twisted-square reduction (Lemma 59.7) on a bounded complete
    # system.  The Jacobi and forbidden-D filters discard no hit.  Scaling a
    # square factor out of both n and D gives exactly the auxiliary datum.
    twisted_rows = ((288, 2, 12), (336, 21, 4), (4545, 505, 3))
    scaling_divisors = {
        m: tuple(t for t in range(1, m + 1) if m % t == 0)
        for _n, _s, m in twisted_rows
    }
    reduction_checks = 0
    for M, _classes in local_rows:
        A = (M + 1) // 4
        for D in divisors_of_square(A):
            for n, s, m in twisted_rows:
                hit = (n + 4 * D) % M == 0
                permitted = (gcd(M, n) == 1
                             and jacobi_symbol(s, M) == -1
                             and D % s != 0)
                assert not hit or permitted
                for t in scaling_divisors[m]:
                    if D % (t * t):
                        continue
                    auxiliary = s * (m // t) ** 2 + 4 * (D // (t * t))
                    assert hit == (auxiliary % M == 0)
                reduction_checks += 1

            if D % 2 == 0:
                E = D // 2
                assert 288 + 4 * D == 2 * (144 + 4 * E)
                assert (288 + 4 * D) % M
            if D % 8 == 0:
                E = D // 8
                assert 288 + 4 * D == 8 * (36 + 4 * E)
            if D % 21 == 0:
                E = D // 21
                assert 336 + 4 * D == 21 * (16 + 4 * E)
                assert (336 + 4 * D) % M
            if D % 505 == 0:
                E = D // 505
                assert 4545 + 4 * D == 505 * (9 + 4 * E)
                assert (4545 + 4 * D) % M

    for M in range(3, 3001, 4):
        if gcd(M, 21) == 1:
            assert jacobi_symbol(21, M) == jacobi_symbol(M, 21)
        if gcd(M, 505) == 1:
            assert jacobi_symbol(505, M) == jacobi_symbol(M, 505)
        if jacobi_symbol(2, M) == -1:
            assert M % 8 == 3

    # Pin every least W in the first sixty members of each twisted-square
    # family.  None means that the complete M<=3000 harvest has no hit; the
    # targeted scan below strengthens exactly those three entries.
    expected_family_W = {
        2: (3, 3, 11, 3, 3, 19, 3, 3, 11, 3, 3, None, 3, 3, 11,
            3, 3, 11, 3, 3, 59, 3, 3, 11, 3, 3, 19, 3, 3, 11,
            3, 3, 59, 3, 3, 11, 3, 3, 35, 3, 3, 11, 3, 3, 131,
            3, 3, 11, 3, 3, 11, 3, 3, 19, 3, 3, 11, 3, 3, 19),
        21: (11, 11, 19, None, 11, 11, 23, 19, 11, 11, 19, 11, 11,
             23, 23, 11, 11, 23, 71, 11, 11, 19, 11, 11, 19, 31, 11,
             11, 23, 19, 11, 11, 23, 11, 11, 23, 23, 11, 11, 23, 19,
             11, 11, 19, 11, 11, 23, 23, 11, 11, 19, 23, 11, 11, 23,
             11, 11, 23, 23, 11),
        505: (11, 11, None, 23, 11, 11, 23, 47, 11, 11, 23, 11, 11,
              23, 107, 11, 11, 23, 23, 11, 11, 23, 11, 11, 23, 87, 11,
              11, 23, 23, 11, 11, 23, 11, 11, 23, 23, 11, 11, 23, 23,
              11, 11, 23, 11, 11, 23, 23, 11, 11, 23, 23, 11, 11, 23,
              11, 11, 23, 23, 11),
    }
    family_W = {}
    for s in (2, 21, 505):
        values = []
        for m in range(1, 61):
            n = s * m * m
            values.append(next((M for M, classes in local_rows
                                if n % M in classes), None))
        family_W[s] = tuple(values)
    assert family_W == expected_family_W

    # The fourth full-population survivor has the exact small witness stated
    # in the text.  The three live candidates need a much deeper scan.
    resolved = {}
    if 643_245 in final_nonsquares:
        for M in range(3003, 4000, 4):
            A = (M + 1) // 4
            if any((643_245 + 4 * D) % M == 0
                   for D in divisors_of_square(A)):
                resolved[643_245] = M
                break
        assert resolved == {643_245: 3119}

    # Independent smallest-prime-factor scan.  The SPF entries are storage
    # only: every factor and every divisor product is explicitly converted to
    # a Python int, avoiding the fixed-width overflow that invalidated an
    # earlier external quick probe.  ES_FULL_SCAN reproduces the deep frontier.
    def targeted_python_int_scan(cap):
        from array import array

        a_max = (cap + 1) // 4
        spf = array("I", [0]) * (a_max + 1)
        for p in range(2, isqrt(a_max) + 1):
            if spf[p] == 0:
                spf[p] = p
                for multiple in range(p * p, a_max + 1, p):
                    if spf[multiple] == 0:
                        spf[multiple] = p

        targets = (288, 336, 4545)
        open_targets = set(targets)
        divisor_values = 0

        def legendre_at_prime(value, p):
            residue = value % p
            if residue == 0:
                return 0
            return 1 if pow(residue, (p - 1) // 2, p) == 1 else -1

        for A in range(1, a_max + 1):
            M = 4 * A - 1
            active = []
            if 288 in open_targets and M % 8 == 3:
                active.append(288)
            if (336 in open_targets
                    and legendre_at_prime(M, 3)
                    * legendre_at_prime(M, 7) == -1):
                active.append(336)
            if (4545 in open_targets
                    and legendre_at_prime(M, 5)
                    * legendre_at_prime(M, 101) == -1):
                active.append(4545)
            if not active:
                continue

            z = A
            factors = []
            while z > 1:
                p = int(spf[z]) or int(z)
                exponent = 0
                while z % p == 0:
                    z //= p
                    exponent += 1
                factors.append((p, 2 * exponent))

            divisors = [1]
            for p, exponent in factors:
                base = divisors
                extra = []
                power = 1
                for _ in range(exponent):
                    power = int(power * p)
                    extra.extend(int(D * power) for D in base)
                divisors = base + extra
            divisor_values += len(divisors)

            for n in active:
                target = int((-n * A) % M)  # A == 4^{-1} (mod M)
                if any(int(D) % M == target for D in divisors):
                    open_targets.remove(n)
        return open_targets, divisor_values

    resolution_cap = 150_000_000 if full_scan else 3_000_000
    unresolved, targeted_divisor_values = targeted_python_int_scan(
        resolution_cap
    )
    assert unresolved == {288, 336, 4545}
    assert targeted_divisor_values == (
        2_878_826_874 if full_scan else 36_611_608
    )

    # Exact floor count and the one-half exponent crossing in Proposition
    # 59.5; these are arithmetic regressions, not a tail theorem.
    for N, T in ((10_000, 100), (300_000, 3000), (1_000_000, 100_000)):
        assert sum(T < m * m <= N for m in range(1, isqrt(N) + 1)) == (
            isqrt(N) - isqrt(T)
        )
    c = Fraction(3, 5)
    crossing_cube = Fraction(1, 2) / c
    assert c * crossing_cube == Fraction(1, 2)

    print("polynomial local/discriminant/conductor checks =",
          (discriminant_rows, construction_rows))
    print("nonsquare tail census (N, T-grid, counts, final survivors) =",
          (population_limit, thresholds, tuple(nonsquare_counts),
           tuple(final_nonsquares)))
    family_histograms = {
        s: dict(sorted(Counter(values).items(),
                       key=lambda item: (-1 if item[0] is None else item[0])))
        for s, values in family_W.items()
    }
    print("twisted-square reduction/family W checks =",
          (reduction_checks, family_histograms))
    print("targeted Python-int resolution (cap,divisor values,resolved,unresolved) =",
          (resolution_cap, targeted_divisor_values,
           tuple(sorted(resolved.items())), tuple(sorted(unresolved))))


print("\n== (bf) polynomial escape classification and nonsquare census (§59) ==")
check_bf()


# ---------------------------------------------------------------- (bg)
def check_bg():
    """§60: exact witness duality, finite normal form, and survivors."""

    def is_eligible(M, D):
        return M >= 3 and M % 4 == 3 and ((M + 1) // 4) ** 2 % D == 0

    # Replay every divisor datum in the complete §56/(bc) modulus range, for
    # every represented positive n <= 2000.  Forward dualization and the
    # canonical (g,u,v,d) normal form are both inverted exactly.
    replay_limit = 2000
    replay_rows = 0
    correction_rows = 0
    swap_rows = 0
    fixed_swap_rows = 0
    for M in range(3, 3001, 4):
        A = (M + 1) // 4
        for D in divisors_of_square(A):
            residue = (-4 * D) % M
            first = residue or M
            for n in range(first, replay_limit + 1, M):
                a = (n + 4 * D) // M
                assert a * M == n + 4 * D
                assert (n + a) % 4 == 0
                h = (n + a) // 4
                assert a * A == D + h
                assert h * h % D == 0
                assert (D + h) % a == 0

                # Exact cancellation ledger.  The dual divisor condition
                # certifies only the part of D left after a^2 is removed.
                reduced_D = D // gcd(D, a * a)
                assert (h * h % D == 0) == (A * A % reduced_D == 0)
                assert A * A % D == 0
                assert gcd(a, D) == 1 or n % gcd(a, D) == 0
                correction_rows += gcd(a, D) > 1

                # Test Lemma 60.2 on the whole harvested sample, not only
                # on its three displayed examples.
                swap_condition = (
                    a >= 3 and a % 4 == 3
                    and ((a + 1) // 4) ** 2 % D == 0
                )
                assert swap_condition == is_eligible(a, D)
                if swap_condition:
                    assert n % 4 == 1 and a * M == n + 4 * D
                    swap_rows += 1
                    fixed_swap_rows += a == M

                g = gcd(A, h)
                u, v = A // g, h // g
                assert gcd(u, v) == 1 and D % g == 0
                d = D // g
                assert g % d == 0
                assert a == 4 * g * v - n
                assert a * u == d + v
                assert M == 4 * g * u - 1
                replay_rows += 1

    assert (replay_rows, correction_rows, swap_rows, fixed_swap_rows) == (
        33_882, 11_451, 1_196, 54
    )

    # Direct finite a-enumeration and an arithmetically independent canonical
    # enumeration.  The successive columns count D|h^2, integral A, the
    # survivor-specific Jacobi/forbidden-layer filters, and exact eligibility.
    targets = (288, 336, 4545)
    expected_near_misses = {
        288: (756, 43, 4, 0),
        336: (912, 65, 37, 0),
        4545: (22_995, 188, 62, 0),
    }
    expected_normal = {
        288: (96, 66, 209, 0),
        336: (112, 78, 262, 0),
        4545: (1515, 1152, 5405, 0),
    }
    near_misses = {}
    normal_counts = {}
    uniform_models = {}

    for n in targets:
        B = (n + 1) // 3
        divisor_rows = integral_rows = filtered_rows = eligible_rows = 0
        model_sum = Fraction(0, 1)
        for a in range(1, 2 * B + 1):
            if (n + a) % 4:
                continue
            h = (n + a) // 4
            h_divisors = divisors_of_square(h)
            model_sum += Fraction(len(h_divisors), a)
            for D in h_divisors:
                divisor_rows += 1
                if (D + h) % a:
                    continue
                integral_rows += 1
                A = (D + h) // a
                M = 4 * A - 1
                if n == 288:
                    filtered = (D % 2 == 1 and M % 8 == 3
                                and gcd(M, 288) == 1)
                elif n == 336:
                    filtered = (gcd(M, 336) == 1
                                and jacobi_symbol(21, M) == -1
                                and D % 21 != 0)
                else:
                    filtered = (gcd(M, 4545) == 1
                                and jacobi_symbol(505, M) == -1
                                and D % 505 != 0)
                if not filtered:
                    continue
                filtered_rows += 1
                if A * A % D:
                    # Every surviving near miss is exactly a forbidden
                    # cancellation: no coprime case can fail eligibility.
                    assert gcd(a, D) > 1 and n % gcd(a, D) == 0
                    if n == 288:
                        assert gcd(a, D) == 9
                        three_part, z = 1, D
                        while z % 3 == 0:
                            three_part *= 3
                            z //= 3
                        assert (A * A) % three_part != 0
                    continue
                eligible_rows += 1
                assert a * M == n + 4 * D
        near_misses[n] = (divisor_rows, integral_rows,
                          filtered_rows, eligible_rows)
        uniform_models[n] = round(float(model_sum), 6)

        pair_rows = divisor_tests = normal_hits = 0
        for g in range(1, B + 1):
            divisors_g = tuple(d for d in range(1, g + 1) if g % d == 0)
            v_min = max(1, (n + 4 * g) // (4 * g))
            for v in range(v_min, B + 1):
                a = 4 * g * v - n
                if a < 1 or a > g + v:
                    continue
                pair_rows += 1
                for d in divisors_g:
                    divisor_tests += 1
                    if (d + v) % a:
                        continue
                    u = (d + v) // a
                    if gcd(u, v) != 1:
                        continue
                    M, D = 4 * g * u - 1, g * d
                    assert is_eligible(M, D)
                    assert a * M == n + 4 * D
                    normal_hits += 1
        normal_counts[n] = (B, pair_rows, divisor_tests, normal_hits)

    assert near_misses == expected_near_misses
    assert normal_counts == expected_normal
    assert uniform_models == {288: 13.266827, 336: 15.617351,
                              4545: 49.909726}

    # The raw equation is symmetric, but eligibility is not.  These pin a
    # bi-eligible pair, a fixed point, and a failure of universal swapping.
    involution_rows = ((7, 1, 3, 17), (3, 1, 7, 17))
    for M, D, a, n in involution_rows:
        assert is_eligible(M, D) and is_eligible(a, D)
        assert a * M == n + 4 * D
    assert is_eligible(7, 1) and 7 * 7 == 45 + 4
    assert is_eligible(23, 36) and 7 * 23 == 17 + 4 * 36
    assert not is_eligible(7, 36)

    # Toy-box coverage identity.  Brute-force all data through M=10^5 and
    # compare the exact union M<=100 or a<=30 with an independent a-scan.
    toy_n = (2, 17, 45, 288, 336, 4545)
    brute_rows = set()
    divisor_values = 0
    for M in range(3, 100_001, 4):
        A = (M + 1) // 4
        for D in divisors_of_square(A):
            divisor_values += 1
            for n in toy_n:
                total = n + 4 * D
                if total % M == 0:
                    brute_rows.add((n, M, D, total // M))

    a_rows = set()
    for n in toy_n:
        for a in range(1, 31):
            if (n + a) % 4:
                continue
            h = (n + a) // 4
            for D in divisors_of_square(h):
                if (D + h) % a:
                    continue
                A = (D + h) // a
                M = 4 * A - 1
                if M <= 100_000 and is_eligible(M, D):
                    a_rows.add((n, M, D, a))
    m_rows = {row for row in brute_rows if row[1] <= 100}
    claimed_region = {row for row in brute_rows
                      if row[1] <= 100 or row[3] <= 30}
    assert m_rows | a_rows == claimed_region
    assert (divisor_values, len(brute_rows), len(m_rows), len(a_rows),
            len(m_rows & a_rows), len(claimed_region)) == (
                1_070_466, 9, 8, 9, 8, 9)

    print("duality replay (n cap,rows,gcd-correction,swap,fixed rows) =",
          (replay_limit, replay_rows, correction_rows,
           swap_rows, fixed_swap_rows))
    print("survivor dual near misses / canonical exhaustions / uniform models =",
          (near_misses, normal_counts, uniform_models))
    print("toy union coverage (M box,divisors,all,M-side,a-side,overlap) =",
          (100_000, divisor_values, len(brute_rows), len(m_rows),
           len(a_rows), len(m_rows & a_rows)))


print("\n== (bg) witness duality and resolved survivor frontier (§60) ==")
check_bg()


# ---------------------------------------------------------------- (bh)
def check_bh():
    """§61: complete bounded W-infinity census and prime dual criterion."""
    import os
    from hashlib import sha256

    full_scan = os.environ.get("ES_FULL_SCAN") == "1"
    census_limit = 1_000_000 if full_scan else 200_000
    # The auxiliary 300000 range cross-validates every hard prime in the
    # default §56 (bc) range.  Census counters below still count exactly the
    # displayed X-range, not this larger audit range.
    prime_cross_limit = 300_000
    work_limit = max(census_limit, prime_cross_limit)
    B_limit = (census_limit + 1) // 3
    work_B_limit = (work_limit + 1) // 3

    # Forward-sieve the canonical normal form (60.7).  The inequality
    # 4gv-g-v <= X is necessary for n=4gv-(d+v)/u <= X because d<=g.
    # Conversely every retained tuple is a witness datum.  Lists contain
    # ordinary Python ints; no fixed-width divisor products occur here.
    divisor_bound = work_B_limit + 1
    small_divisors = [[] for _ in range(divisor_bound + 1)]
    for d in range(1, divisor_bound + 1):
        for multiple in range(d, divisor_bound + 1, d):
            small_divisors[multiple].append(d)

    least_W = [0] * (work_limit + 1)
    pair_rows = divisor_tests = 0
    for g in range(1, work_B_limit + 1):
        census_v_max = ((census_limit + g) // (4 * g - 1)
                        if g <= B_limit else 0)
        work_v_max = (work_limit + g) // (4 * g - 1)
        for v in range(1, work_v_max + 1):
            in_census_box = v <= census_v_max
            if in_census_box:
                pair_rows += 1
            for d in small_divisors[g]:
                q = d + v
                assert q <= divisor_bound
                for u in small_divisors[q]:
                    if in_census_box:
                        divisor_tests += 1
                    if gcd(u, v) != 1:
                        continue
                    a = q // u
                    n = 4 * g * v - a
                    assert n >= 1
                    if n > work_limit:
                        continue
                    M = 4 * g * u - 1
                    if least_W[n] == 0 or M < least_W[n]:
                        least_W[n] = M

    infinities = tuple(n for n in range(1, census_limit + 1)
                       if least_W[n] == 0)
    nonsquare_infinities = tuple(
        n for n in infinities if isqrt(n) ** 2 != n
    )
    assert nonsquare_infinities == (288, 336, 4545)
    assert len(infinities) == isqrt(census_limit) + 3
    assert (pair_rows, divisor_tests) == (
        (3_400_244, 173_713_414) if full_scan
        else (599_581, 24_246_108)
    )

    # Compare exact forward-duality minima with the independent original-side
    # harvest used by (bc), for every hard prime through its 300000 range.
    # Then map each minimum back to an explicit (a,D) row of (61.12)-(61.15).
    hard_cross = tuple(int(p) for p in primerange(2, prime_cross_limit + 1)
                       if p % 24 == 1)
    modulus_classes = complete_multiplier_harvest(3000)
    original_prime_W = {
        p: next((M for M, classes in modulus_classes if p % M in classes),
                None)
        for p in hard_cross
    }
    assert len(hard_cross) == 3202
    assert all(original_prime_W[p] is not None for p in hard_cross)
    assert all(least_W[p] == original_prime_W[p] for p in hard_cross)
    assert (max(original_prime_W.values()), sum(original_prime_W.values())) == (
        279, 44_426
    )
    prime_cross_even_D = 0
    for p, M in original_prime_W.items():
        A = (M + 1) // 4
        D = next(int(D) for D in divisors_of_square(A)
                 if (p + 4 * int(D)) % M == 0)
        prime_cross_even_D += D % 2 == 0
        a = (p + 4 * D) // M
        h = (p + a) // 4
        assert 1 <= a <= 2 * ((p + 1) // 3) and a % 4 == 3
        assert h * h % D == 0 and (D + h) % a == 0
        assert gcd(a, D) == 1 and (D + h) // a == A
        assert A * A % D == 0 and a * M == p + 4 * D
    assert prime_cross_even_D == 1941

    # Arithmetically independent M-side overlap.  M=100351 is the larger
    # exact global ceiling for 288 and 336.  Every other nonsquare <=3000
    # has already acquired an explicit datum; squares are excluded by
    # Theorem 58.1.  Divisor products are explicitly converted to Python int.
    overlap_limit = 3000
    direct_cap = 100_351
    direct_W = [0] * (overlap_limit + 1)
    direct_divisors = direct_incidences = 0
    for M in range(3, direct_cap + 1, 4):
        A = (M + 1) // 4
        for divisor in divisors_of_square(A):
            D = int(divisor)
            direct_divisors += 1
            residue = int((-4 * D) % M)
            first = residue or M
            for n in range(first, overlap_limit + 1, M):
                direct_incidences += 1
                if direct_W[n] == 0:
                    direct_W[n] = M
    direct_infinities = tuple(n for n in range(1, overlap_limit + 1)
                              if direct_W[n] == 0)
    assert (direct_divisors, direct_incidences) == (1_074_878, 73_105)
    assert tuple(n for n in direct_infinities if isqrt(n) ** 2 != n) == (
        288, 336
    )
    assert direct_infinities == tuple(
        n for n in range(1, overlap_limit + 1) if least_W[n] == 0
    )
    assert all(direct_W[n] == least_W[n]
               for n in range(1, overlap_limit + 1) if direct_W[n])

    # Pin the complete gcd distributions behind the supports in (61.6).
    # These are the character-filtered near misses of (60.21), before the
    # final uncancelled eligibility check.
    near_miss_gcds = {}
    for n in (288, 336, 4545):
        B = (n + 1) // 3
        distribution = Counter()
        for a in range(1, 2 * B + 1):
            if (n + a) % 4:
                continue
            h = (n + a) // 4
            for divisor in divisors_of_square(h):
                D = int(divisor)
                if (D + h) % a:
                    continue
                A = (D + h) // a
                M = 4 * A - 1
                if n == 288:
                    filtered = (D % 2 == 1 and M % 8 == 3
                                and gcd(M, n) == 1)
                elif n == 336:
                    filtered = (gcd(M, n) == 1
                                and jacobi_symbol(21, M) == -1
                                and D % 21 != 0)
                else:
                    filtered = (gcd(M, n) == 1
                                and jacobi_symbol(505, M) == -1
                                and D % 505 != 0)
                if filtered:
                    assert A * A % D != 0
                    distribution[gcd(a, D)] += 1
        near_miss_gcds[n] = distribution
    assert near_miss_gcds == {
        288: Counter({9: 4}),
        336: Counter({48: 11, 3: 6, 112: 5, 7: 4, 6: 3,
                      8: 2, 4: 2, 14: 1, 24: 1, 16: 1, 28: 1}),
        4545: Counter({15: 19, 45: 16, 9: 11, 5: 9, 303: 5,
                       101: 1, 909: 1}),
    }

    # Full s<=200 squarefree, m<=30 table.  The digest pins every displayed
    # finite W, while the histogram and per-s vanishing rows keep failures
    # inspectable.  The largest argument is 180000, inside the default census.
    squarefree_s = tuple(
        s for s in range(2, 201)
        if all(s % (q * q) for q in range(2, isqrt(s) + 1))
    )
    twisted_rows = tuple(
        tuple(least_W[s * m * m] for m in range(1, 31))
        for s in squarefree_s
    )
    encoding = ";".join(
        f"{s}:" + ",".join(map(str, row))
        for s, row in zip(squarefree_s, twisted_rows)
    )
    assert len(squarefree_s) == 121
    assert sha256(encoding.encode()).hexdigest() == (
        "3c6c31f96adce8ea9180cc86e93da841e49d71f7a25a8d094e58c05fd5047007"
    )

    # Parse the grouped codebook printed in §61, so the digest cannot hide a
    # transcription error in the human-readable table.
    from pathlib import Path
    notes_text = Path(__file__).with_name("notes.md").read_text()
    table_text = notes_text.split(
        "Block (bh) pins all entries by a SHA-256 digest", 1
    )[1].split("```text\n", 1)[1].split("\n```", 1)[0]
    displayed_rows = {}
    for line in table_text.splitlines():
        s_text, values_text = line.split(" : ")
        values = tuple(0 if value == "I" else int(value)
                       for value in values_text.split(","))
        assert len(values) == 30
        for s in map(int, s_text.split(",")):
            assert s not in displayed_rows
            displayed_rows[s] = values
    assert displayed_rows == dict(zip(squarefree_s, twisted_rows))

    twisted_vanishing = {
        s: tuple(m for m, W in enumerate(row, 1) if W == 0)
        for s, row in zip(squarefree_s, twisted_rows) if 0 in row
    }
    assert twisted_vanishing == {2: (12,), 21: (4,)}
    assert Counter(W or None for row in twisted_rows for W in row) == {
        3: 940, 7: 1064, 11: 449, 15: 154, 19: 177, 23: 334,
        31: 86, 35: 31, 39: 51, 43: 30, 47: 104, 55: 24,
        59: 37, 67: 6, 71: 44, 79: 13, 83: 5, 87: 3, 95: 11,
        99: 1, 103: 6, 107: 5, 119: 14, 127: 7, 139: 1,
        143: 3, 151: 2, 163: 1, 167: 7, 179: 2, 199: 2,
        215: 2, 223: 2, 227: 1, 239: 3, 271: 1, 335: 1,
        419: 1, 479: 1, 499: 1, 727: 1, None: 2,
    }

    # The third sporadic kernel lies outside the s<=200 box.  Replay its
    # first thirty values from the small M-side harvest, using the complete
    # normal-form census to distinguish the one true infinity from a cutoff.
    row_505 = []
    for m in range(1, 31):
        n = 505 * m * m
        if n == 4545:
            assert least_W[n] == 0
            row_505.append(None)
            continue
        witness = next(
            (M for M in range(3, 3001, 4)
             if any((n + 4 * int(D)) % M == 0
                    for D in divisors_of_square((M + 1) // 4))),
            None,
        )
        row_505.append(witness)
    assert tuple(row_505) == (
        11, 11, None, 23, 11, 11, 23, 47, 11, 11,
        23, 11, 11, 23, 107, 11, 11, 23, 23, 11,
        11, 23, 11, 11, 23, 87, 11, 11, 23, 23,
    )

    # Independently enumerate the exact prime criterion (60.25), all the way
    # through a<=2B, for three late hard-prime record holders.  SPF storage is
    # bounded below 10^6; generated divisors and products remain Python ints.
    prime_targets = (954_409, 1_853_329, 2_031_121)
    h_cap = max((5 * p + 3) // 12 + 2 for p in prime_targets)
    spf = list(range(h_cap + 1))
    for q in range(2, isqrt(h_cap) + 1):
        if spf[q] == q:
            for multiple in range(q * q, h_cap + 1, q):
                if spf[multiple] == multiple:
                    spf[multiple] = q

    def square_divisors_from_spf(value):
        factors = []
        z = value
        while z > 1:
            q = int(spf[z])
            exponent = 0
            while z % q == 0:
                z //= q
                exponent += 1
            factors.append((q, exponent))
        divisors = [1]
        for q, exponent in factors:
            base = tuple(divisors)
            power = 1
            for _ in range(2 * exponent):
                power = int(power * q)
                divisors.extend(int(D * power) for D in base)
        return divisors

    prime_rows = {}
    for p in prime_targets:
        B = (p + 1) // 3
        raw_trials = congruence_rows = 0
        uniform_mass = 0.0
        best = None
        for a in range(3, 2 * B + 1, 4):
            h = (p + a) // 4
            divisors = square_divisors_from_spf(h)
            raw_trials += len(divisors)
            uniform_mass += len(divisors) / a
            for D in divisors:
                if (D + h) % a:
                    continue
                congruence_rows += 1
                A = (D + h) // a
                M = 4 * A - 1
                assert gcd(a, D) == 1
                assert D > 0 and D <= h * h and h * h % D == 0
                assert A * A % D == 0 and M % 4 == 3
                assert a * M == p + 4 * D
                candidate = (M, a, D, h)
                if best is None or candidate < best:
                    best = candidate
        prime_rows[p] = (raw_trials, round(uniform_mass, 6),
                         congruence_rows, best)
    assert prime_rows == {
        954_409: (11_465_930, 192.502348, 62,
                  (335, 2855, 504, 239316)),
        1_853_329: (24_242_528, 247.180398, 112,
                    (383, 4839, 2, 464542)),
        2_031_121: (26_874_324, 222.590291, 36,
                    (2495, 815, 576, 507984)),
    }

    print("decidable W-infinity census (limit,infinities,nonsquares,pairs,tests) =",
          (census_limit, len(infinities), nonsquare_infinities,
           pair_rows, divisor_tests))
    print("hard-prime original/duality cross-check "
          "(limit,count,max W,sum W,even-D minima) =",
          (prime_cross_limit, len(hard_cross), max(original_prime_W.values()),
           sum(original_prime_W.values()), prime_cross_even_D))
    print("independent direct overlap (n cap,M cap,divisors,incidences,tail) =",
          (overlap_limit, direct_cap, direct_divisors, direct_incidences,
           tuple(n for n in direct_infinities if isqrt(n) ** 2 != n)))
    print("twisted-square box (s count,m cap,vanishing,W histogram,digest) =",
          (len(squarefree_s), 30, twisted_vanishing,
           Counter(W or None for row in twisted_rows for W in row),
           sha256(encoding.encode()).hexdigest()))
    print("hard-prime dual criterion (p:(raw,uniform mass,rows,(W,a,D,h))) =",
          prime_rows)


print("\n== (bh) decidable census, twisted squares, and prime criterion (§61) ==")
check_bh()


# ---------------------------------------------------------------- (bi)
def check_bi():
    """§62: ratio spectra, exact small-a laws, and twisted-square stress."""
    import os
    from hashlib import sha256
    from random import Random

    # One bounded smallest-prime-factor table serves the exhaustive h<=10^5
    # laws.  Every generated divisor is an ordinary Python int.
    h_limit = 100_000
    spf = list(range(h_limit + 1))
    for q in range(2, isqrt(h_limit) + 1):
        if spf[q] == q:
            for multiple in range(q * q, h_limit + 1, q):
                if spf[multiple] == multiple:
                    spf[multiple] = q

    def factors_from_spf(value):
        factors = []
        z = value
        while z > 1:
            q = int(spf[z])
            exponent = 0
            while z % q == 0:
                z //= q
                exponent += 1
            factors.append((q, exponent))
        return tuple(factors)

    def divisors_from_factors(factors):
        divisors = [1]
        for q, exponent in factors:
            base = tuple(divisors)
            power = 1
            for _ in range(2 * exponent):
                power = int(power * q)
                divisors.extend(int(D * power) for D in base)
        return divisors

    def product_spectrum(factors, a):
        residues = {1}
        for q, exponent in factors:
            powers = {pow(q, f, a) for f in range(-exponent, exponent + 1)}
            residues = {int(x * y % a) for x in residues for y in powers}
        return residues

    def divisor_ratio_spectrum(factors, h, a):
        inverse_h = pow(h, -1, a)
        return {int(D * inverse_h % a)
                for D in divisors_from_factors(factors)}

    # The spectrum identity and self-pairing are checked directly on random
    # unit pairs, independently generating the two sides.
    rng = Random(620026)
    random_identity_rows = 0
    while random_identity_rows < 500:
        h = rng.randrange(1, h_limit + 1)
        a = rng.randrange(3, 400, 2)
        if gcd(h, a) != 1:
            continue
        factors = factors_from_spf(h)
        direct = divisor_ratio_spectrum(factors, h, a)
        bounded = product_spectrum(factors, a)
        assert direct == bounded
        divisors = divisors_from_factors(factors)
        hits = {D for D in divisors if D % a == (-h) % a}
        assert hits == {h * h // D for D in hits}
        random_identity_rows += 1

    # Primitive roots and inverse-paired residue classes in Theorem 62.2.
    prime_tables = {
        3: ((2,),),
        7: ((3, 5), (2, 4), (6,)),
        11: ((2, 6), (3, 4), (7, 8), (5, 9), (10,)),
        19: ((2, 10), (4, 5), (8, 12), (6, 16), (3, 13),
             (7, 11), (14, 15), (9, 17), (18,)),
        23: ((5, 14), (2, 12), (7, 10), (4, 6), (15, 20),
             (3, 8), (17, 19), (13, 16), (11, 21), (9, 18),
             (22,)),
    }

    def prime_budgets(factors, ell):
        classes = prime_tables[ell]
        lookup = {residue: r for r, pair in enumerate(classes, 1)
                  for residue in pair}
        budgets = [0] * len(classes)
        for q, exponent in factors:
            residue = q % ell
            if residue != 1:
                budgets[lookup[residue] - 1] += exponent
        return tuple(budgets)

    def prime_budget_hit(budgets):
        modulus = 2 * len(budgets)
        target = len(budgets)
        residues = {0}
        for r, budget in enumerate(budgets, 1):
            residues = {(x + r * j) % modulus for x in residues
                        for j in range(-budget, budget + 1)}
        return target in residues

    eleven_patterns = (
        (0, 0, 1, 2), (0, 0, 3, 1), (0, 0, 5, 0),
        (0, 1, 1, 0), (1, 0, 0, 1), (1, 0, 2, 0),
        (1, 2, 0, 0), (2, 0, 1, 0), (3, 1, 0, 0),
        (5, 0, 0, 0),
    )

    def fifteen_budgets(factors):
        values = {2: 0, 7: 0, 4: 0, 11: 0, 14: 0}
        for q, exponent in factors:
            residue = q % 15
            if residue in (2, 8):
                values[2] += exponent
            elif residue in (7, 13):
                values[7] += exponent
            elif residue in (4, 11, 14):
                values[residue] = 1
            elif residue != 1:
                raise AssertionError((q, residue))
        return tuple(values[k] for k in (2, 7, 4, 11, 14))

    def fifteen_law(budgets):
        v2, v7, i4, i11, i14 = budgets
        patterns = ((0, 0, 1, 1), (0, 2, 0, 1),
                    (1, 1, 0, 0), (2, 0, 0, 1))
        return bool(i14 or any(
            all(x >= y for x, y in zip((v2, v7, i4, i11), pattern))
            for pattern in patterns
        ))

    checked_counts = Counter()
    failure_counts = Counter()
    for h in range(1, h_limit + 1):
        factors = factors_from_spf(h)
        divisors = divisors_from_factors(factors)
        for a in (3, 7, 11, 15, 19, 23):
            if gcd(h, a) != 1:
                continue
            inverse_h = pow(h, -1, a)
            brute_hit = any(D * inverse_h % a == a - 1 for D in divisors)
            checked_counts[a] += 1
            failure_counts[a] += not brute_hit
            if a == 15:
                law_hit = fifteen_law(fifteen_budgets(factors))
            else:
                budgets = prime_budgets(factors, a)
                law_hit = prime_budget_hit(budgets)
                if a == 3:
                    assert law_hit == (budgets[0] >= 1)
                elif a == 7:
                    assert law_hit == (
                        budgets[2] >= 1
                        or (budgets[0] >= 1 and budgets[1] >= 1)
                        or budgets[0] >= 3
                    )
                elif a == 11:
                    assert law_hit == (
                        budgets[4] >= 1
                        or any(all(x >= y for x, y in zip(
                            budgets[:4], pattern))
                               for pattern in eleven_patterns)
                    )
            assert brute_hit == law_hit, (h, a, factors)

    assert checked_counts == Counter({
        3: 66_667, 7: 85_715, 11: 90_910,
        15: 53_333, 19: 94_737, 23: 95_653,
    }), checked_counts
    assert failure_counts == Counter({
        3: 8_814, 7: 25_359, 11: 34_046,
        15: 26_423, 19: 46_679, 23: 54_165,
    }), failure_counts

    # Multiplicity cannot be replaced by subgroup generation: 3 mod 7 is a
    # generator, but h=17 supplies it only once and cannot reach -1.
    surprise_factors = factors_from_spf(17)
    assert product_spectrum(surprise_factors, 7) == {1, 3, 5}
    assert pow(3, 3, 7) == 6 and 6 not in product_spectrum(
        surprise_factors, 7
    )

    # Recompute every hard-prime minimum through 10^5 in bounded prime chunks.
    # The independent (bc)/(bh) harvest supplies only an exact comparison cap.
    # For each a and every M<=that cap, D=a(M+1)/4-h is the sole possible
    # divisor; testing D|h^2 is exactly the ratio-spectrum condition.
    modulus_rows = complete_multiplier_harvest(3000)
    prime_W = {}
    ratio_candidate_tests = 0
    ratio_hits = 0
    for low in range(2, 100_001, 20_000):
        high = min(100_001, low + 20_000)
        for p0 in primerange(low, high):
            p = int(p0)
            if p % 24 != 1:
                continue
            reference = next(M for M, classes in modulus_rows
                             if p % M in classes)
            best = None
            B = (p + 1) // 3
            for a in range(3, 2 * B + 1, 4):
                h = (p + a) // 4
                for A in range(h // a + 1, (reference + 1) // 4 + 1):
                    ratio_candidate_tests += 1
                    D = int(a * A - h)
                    if (h * h) % D:
                        continue
                    ratio_hits += 1
                    assert D * pow(h, -1, a) % a == a - 1
                    z = D
                    normalized = 1
                    for q, exponent in factors_from_spf(h):
                        d_exponent = 0
                        while z % q == 0:
                            z //= q
                            d_exponent += 1
                        f = d_exponent - exponent
                        assert -exponent <= f <= exponent
                        normalized = normalized * pow(q, f, a) % a
                    assert z == 1 and normalized == a - 1
                    M = 4 * A - 1
                    if best is None or M < best:
                        best = M
            assert best == reference
            prime_W[p] = best

    encoding = ";".join(f"{p}:{prime_W[p]}" for p in prime_W)
    assert (len(prime_W), max(prime_W.values()), sum(prime_W.values()),
            ratio_candidate_tests) == (1181, 167, 15_779, 27_107_184)
    assert sha256(encoding.encode()).hexdigest() == (
        "2acabc3ad120e2f6b02c86f42677bc1b49c89152175bcfd59de0070cdde3a6ea"
    )

    # Both meanings of "early": first witnessing a and the a attached to the
    # least M.  Small-a entries are None on failure and (M,D) on success.
    anatomy_expected = {
        225_289: ((279, 811, 245, 56_525),
                  (31, 7_335, 524, 56_330),
                  (None, None, None, None, None, None)),
        954_409: ((335, 2_855, 504, 239_316),
                  (3, 318_495, 269, 238_603),
                  ((318_495, 269), None, None, None, None, None)),
        1_853_329: ((383, 4_839, 2, 464_542),
                    (3, 617_815, 29, 463_333),
                    ((617_815, 29), (264_783, 38),
                     (168_503, 51), None, None, None)),
        2_031_121: ((2_495, 815, 576, 507_984),
                    (11, 185_279, 1_737, 507_783),
                    (None, None, (185_279, 1_737), None,
                     (107_255, 1_681), None)),
    }
    anatomy = {}
    for p, (minimum_row, _, _) in anatomy_expected.items():
        reference = next(M for M, classes in modulus_rows
                         if p % M in classes)
        W, best_a, best_D, best_h = minimum_row
        assert reference == W and best_h == (p + best_a) // 4
        assert best_h * best_h % best_D == 0
        assert (best_D + best_h) % best_a == 0
        assert 4 * ((best_D + best_h) // best_a) - 1 == W

        first = None
        small = []
        for a in range(3, 32, 4):
            h = (p + a) // 4
            candidates = sorted(
                (4 * ((D + h) // a) - 1, int(D))
                for D in divisors_of_square(h) if (D + h) % a == 0
            )
            if a in (3, 7, 11, 15, 19, 23):
                small.append(candidates[0] if candidates else None)
            if first is None and candidates:
                first = (a, candidates[0][0], candidates[0][1], h)
        assert first is not None
        anatomy[p] = (minimum_row, first, tuple(small))
    assert anatomy == anatomy_expected

    # Pin the displayed failure-budget ledger, not only its P/F outcomes.
    failure_budgets_expected = {
        (225_289, 3): (0,),
        (225_289, 7): (0, 3, 0),
        (225_289, 11): (0, 2, 0, 2, 0),
        (225_289, 15): (2, 0, 0, 0, 0),
        (225_289, 19): (0, 1, 1, 0, 1, 0, 0, 0, 0),
        (225_289, 23): (0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0),
        (954_409, 7): (0, 3, 0),
        (954_409, 11): (0, 1, 0, 1, 0),
        (954_409, 15): (2, 0, 0, 0, 0),
        (954_409, 19): (0, 1, 2, 0, 0, 0, 0, 0, 0),
        (954_409, 23): (0, 4, 0, 0, 0, 2, 0, 0, 0, 0, 0),
        (1_853_329, 15): (4, 0, 0, 0, 0),
        (1_853_329, 19): (0, 0, 0, 0, 0, 1, 1, 0, 0),
        (1_853_329, 23): (0, 1, 0, 1, 0, 2, 0, 0, 0, 0, 0),
        (2_031_121, 3): (0,),
        (2_031_121, 7): (0, 3, 0),
        (2_031_121, 15): (4, 0, 0, 0, 0),
        (2_031_121, 23): (1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0),
    }
    failure_budgets = {}
    for (p, a), expected in failure_budgets_expected.items():
        factors = tuple((int(q), int(exponent)) for q, exponent in
                        factorint((p + a) // 4).items())
        failure_budgets[p, a] = (
            fifteen_budgets(factors) if a == 15
            else prime_budgets(factors, a)
        )
    assert failure_budgets == failure_budgets_expected

    # For the three composite sporadics the unit normalization can fail.
    # Every raw quotient row lies in such a nonunit branch and all are killed
    # by the uncancelled D|A^2 eligibility check.
    sporadic_rows = {}
    for n in (288, 336, 4545):
        B = (n + 1) // 3
        admissible = gcd_n = gcd_h = quotient = eligible = unit_quotient = 0
        for a in range(1, 2 * B + 1):
            if (n + a) % 4:
                continue
            admissible += 1
            h = (n + a) // 4
            gcd_n += gcd(a, n) > 1
            gcd_h += gcd(a, h) > 1
            for D0 in divisors_of_square(h):
                D = int(D0)
                if (D + h) % a:
                    continue
                quotient += 1
                unit_quotient += gcd(a, h) == 1
                A = (D + h) // a
                eligible += A * A % D == 0
        sporadic_rows[n] = (
            admissible, gcd_n, gcd_h, quotient, eligible, unit_quotient
        )
    assert sporadic_rows == {
        288: (48, 48, 32, 43, 0, 0),
        336: (56, 56, 40, 65, 0, 0),
        4545: (757, 357, 357, 188, 0, 0),
    }

    # Staged C_SQ' stress.  The default is a pinned slice; ES_FULL_SCAN=1
    # replays the full research box.  Rows are streamed and only survivors
    # are retained.  Stage 2 and the terminating dual decision are live code,
    # but the pinned run has no stage-1 survivor to pass to them.
    full_scan = os.environ.get("ES_FULL_SCAN") == "1"
    s_cap, m_cap = ((1000, 300) if full_scan else (200, 150))
    stage1_rows = complete_multiplier_harvest(10_000)
    squarefree_values = tuple(
        s for s in range(2, s_cap + 1)
        if all(exponent == 1 for exponent in factorint(s).values())
    )
    population = 0
    stage1_survivors = []
    maximum = (0, None)
    for s in squarefree_values:
        for m in range(1, m_cap + 1):
            n = int(s * m * m)
            if not 1_000_000 < n <= 100_000_000:
                continue
            population += 1
            W = next((M for M, classes in stage1_rows if n % M in classes),
                     None)
            if W is None:
                stage1_survivors.append((n, s, m))
            elif W > maximum[0]:
                maximum = (W, (n, s, m))

    stage2_survivors = list(stage1_survivors)
    if stage2_survivors:
        active = {n: (s, m) for n, s, m in stage2_survivors}
        for M in range(10_003, 1_000_001, 4):
            A = (M + 1) // 4
            classes = {int((-4 * D) % M) for D in divisors_of_square(A)}
            for n in tuple(active):
                if n % M in classes:
                    del active[n]
            if not active:
                break
        stage2_survivors = [(n, *active[n]) for n in sorted(active)]

    def complete_dual_decision(n):
        B = (n + 1) // 3
        best = None
        for a in range(1, 2 * B + 1):
            if (n + a) % 4:
                continue
            h = (n + a) // 4
            for D0 in divisors_of_square(h):
                D = int(D0)
                if (D + h) % a:
                    continue
                A = (D + h) // a
                if A * A % D:
                    continue
                M = 4 * A - 1
                if best is None or M < best:
                    best = M
        return best

    final_infinities = tuple(
        n for n, _, _ in stage2_survivors
        if complete_dual_decision(n) is None
    )
    hunt_summary = (
        len(squarefree_values), population, len(stage1_survivors),
        len(stage2_survivors), final_infinities, maximum
    )
    assert hunt_summary == (
        (607, 146_016, 0, 0, (), (3359, (9_028_800, 627, 120)))
        if full_scan else
        (121, 5_105, 0, 0, (), (659, (1_666_170, 170, 99)))
    )
    if full_scan:
        maximum_M, (maximum_n, _, _) = maximum
        maximum_D, maximum_a = 48, 2_688
        assert maximum_D in divisors_of_square((maximum_M + 1) // 4)
        assert maximum_n + 4 * maximum_D == maximum_a * maximum_M

    print("ratio-spectrum identity / small-law exhaustive counts =",
          (random_identity_rows, dict(checked_counts), dict(failure_counts)))
    print("hard-prime spectrum replay (count,candidates,hits,max,sum,digest) =",
          (len(prime_W), ratio_candidate_tests, ratio_hits,
           max(prime_W.values()), sum(prime_W.values()),
           sha256(encoding.encode()).hexdigest()))
    print("late-prime spectrum anatomy =", anatomy)
    print("sporadic nonunit anatomy =", sporadic_rows)
    print("twisted-square staged hunt (s,population,stage1,stage2,infinity,max) =",
          hunt_summary)


print("\n== (bi) divisor-ratio spectra and finite conspiracy (§62) ==")
check_bi()


# ---------------------------------------------------------------- (bj)
def check_bj():
    """§63: witness taxonomy, universal a-law, sqrt regime, and a_1."""
    import os
    from random import Random

    def factors_py(value):
        return tuple((int(q), int(e)) for q, e in factorint(value).items())

    def divisors_with_multiplier(factors, exponent_multiplier):
        divisors = [1]
        for q, exponent in factors:
            base = tuple(divisors)
            power = 1
            for _ in range(exponent_multiplier * exponent):
                power = int(power * q)
                divisors.extend(int(D * power) for D in base)
        return divisors

    def divisors_square_factors(factors):
        return divisors_with_multiplier(factors, 2)

    def ratio_success(h, a, factors=None):
        """Direct bounded-product form of the universal a-law."""
        factors = factors_py(h) if factors is None else factors
        residues = {1}
        for q, exponent in factors:
            powers = {pow(q, f, a)
                      for f in range(-exponent, exponent + 1)}
            residues = {int(x * y % a)
                        for x in residues for y in powers}
            # Later factors retain every old residue through exponent zero.
            if a - 1 in residues:
                return True
        return a - 1 in residues

    def check_prime_witness(p, a, D):
        """Replay Theorem 61.4 and the original Lemma-16.1 class."""
        p, a, D = int(p), int(a), int(D)
        B = (p + 1) // 3
        assert 1 <= a <= 2 * B and a % 4 == 3
        assert (p + a) % 4 == 0
        h = (p + a) // 4
        assert h * h % D == 0 and (D + h) % a == 0
        A = (D + h) // a
        M = 4 * A - 1
        assert M % 4 == 3 and a * M == p + 4 * D
        assert A * A % D == 0
        assert p % M == (-4 * D) % M
        return M, A, h

    # S1--S3 on a seeded random sample.  A 3 mod 4 prime factor q of p+4
    # supplies two 3 mod 4 factors; taking the larger as a simultaneously
    # exercises DIV (with e=h), both D1 divisors, and the sqrt construction.
    hard_pool = [int(p) for p in primerange(2, 2_000_001)
                 if int(p) % 24 == 1]
    rng = Random(630027)
    rng.shuffle(hard_pool)
    family_rows = []
    for p in hard_pool:
        shifted = p + 4
        factors = factors_py(shifted)
        q = next((q for q, _ in factors if q % 4 == 3), None)
        if q is None:
            continue
        cofactor = shifted // q
        assert q % 4 == 3 and cofactor % 4 == 3
        a, expected_M = max(q, cofactor), min(q, cofactor)

        # S1: e=h is a divisor of h and is -1 modulo a, so D=h/e=1.
        h = (p + a) // 4
        e = h
        assert h % e == 0 and e % a == a - 1
        D_div = h // e
        M, _, _ = check_prime_witness(p, a, D_div)
        assert M == expected_M

        # S2: the equivalence and both D=1 and D=h^2 witnesses.
        assert (h % a == a - 1) == ((p + 4) % a == 0)
        M_one, _, _ = check_prime_witness(p, a, 1)
        check_prime_witness(p, a, h * h)

        # S3: the selected factorization and all exact range constraints.
        B = (p + 1) // 3
        assert isqrt(shifted) <= a
        assert a <= shifted // 3 <= 2 * B
        assert M_one == expected_M and M_one * M_one <= shifted
        family_rows.append((p, a, M_one))
        if len(family_rows) == 512:
            break
    assert len(family_rows) == 512

    # Exercise the actual DIV family away from its D=1 endpoint: e is a
    # proper divisor of h, so D=h/e is generally neither 1 nor h^2.
    proper_div_rows = []
    for p in hard_pool:
        B = (p + 1) // 3
        for a in range(3, min(2 * B, 199) + 1, 4):
            h = (p + a) // 4
            e = next((e for e in divisors_with_multiplier(factors_py(h), 1)
                      if e != h and e % a == a - 1), None)
            if e is None:
                continue
            D = h // e
            check_prime_witness(p, a, D)
            proper_div_rows.append((p, a, h, e, D))
            if len(proper_div_rows) == 256:
                break
        if len(proper_div_rows) == 256:
            break
    assert len(proper_div_rows) == 256

    # The equivalence in S2 is also checked away from successful rows.
    for p, _, _ in family_rows:
        B = (p + 1) // 3
        for a in range(3, min(2 * B, 199) + 1, 4):
            h = (p + a) // 4
            assert (h % a == a - 1) == ((p + 4) % a == 0)

    # Fixed-D laws.  Direct eligibility is compared with the asserted class
    # for every divisor M of the shifted value in this seeded sample.
    class_modulus = {1: (4, 3), 2: (8, 7),
                     3: (12, 11), 4: (8, 7)}
    fixed_D_rows = 0
    for p, _, _ in family_rows:
        for D in range(1, 5):
            shifted = p + 4 * D
            # Generate all ordinary divisors independently of eligibility.
            ordinary = [1]
            for q, exponent in factors_py(shifted):
                ordinary = [int(d * q**j) for d in ordinary
                            for j in range(exponent + 1)]
            modulus, residue = class_modulus[D]
            for M in ordinary:
                if M % 4 != 3:
                    continue
                A = (M + 1) // 4
                direct = A * A % D == 0
                law = M % modulus == residue
                assert direct == law
                if direct:
                    a = shifted // M
                    check_prime_witness(p, a, D)
                fixed_D_rows += 1
    assert fixed_D_rows == 7_146

    # General squarefree eligibility, including even squarefree D.
    for D in range(1, 31):
        if any(e > 1 for _, e in factors_py(D)):
            continue
        for M in range(3, 1_000, 4):
            A = (M + 1) // 4
            assert (A * A % D == 0) == (M % (4 * D) == 4 * D - 1)

    # Universal CRT/log-vector law.  The same bounded coefficient is applied
    # to every prime-power component, then compared with a direct divisor
    # spectrum.  For fixed small components, logarithms are tabulated exactly.
    def crt_log_feasible(h, a, factors):
        components = []
        log_tables = []
        for ell, exponent in factors_py(a):
            modulus = int(ell**exponent)
            phi = int((ell - 1) * ell**(exponent - 1))
            generator = int(primitive_root(modulus))
            table = {}
            value = 1
            for j in range(phi):
                table[value] = j
                value = int(value * generator % modulus)
            assert len(table) == phi and table[modulus - 1] == phi // 2
            components.append((modulus, phi))
            log_tables.append(table)

        zero = tuple(0 for _ in components)
        reachable = {zero}
        for q, exponent in factors:
            vector = tuple(log_tables[i][q % modulus]
                           for i, (modulus, _) in enumerate(components))
            updated = set()
            for old in reachable:
                for f in range(-exponent, exponent + 1):
                    updated.add(tuple(
                        int((old[i] + f * vector[i]) % components[i][1])
                        for i in range(len(components))
                    ))
            reachable = updated
        target = tuple(phi // 2 for _, phi in components)
        return target in reachable

    # Coupling is material, not cosmetic.  For (a,h)=(15,4), the exponent
    # of 2 could reach -1 separately modulo 3 and modulo 5, but no one
    # f in [-2,2] reaches both targets.  Also exercise a prime that is 1 in
    # one component (7 mod 3) but has order 4 in the other (7 mod 5).
    assert not crt_log_feasible(4, 15, factors_py(4))
    assert all(any(pow(2, f, component) == component - 1
                   for f in range(-2, 3))
               for component in (3, 5))
    assert crt_log_feasible(7, 15, factors_py(7)) == ratio_success(7, 15)
    assert 7 % 3 == 1 and {pow(7, f, 5) for f in range(4)} == {1, 2, 3, 4}

    composite_a = (15, 27, 35, 39, 51, 63, 75, 99, 105)
    lattice_rows = 0
    while lattice_rows < 360:
        a = composite_a[rng.randrange(len(composite_a))]
        h = rng.randrange(1, 50_001)
        if gcd(h, a) != 1:
            continue
        factors = factors_py(h)
        inverse_h = pow(h, -1, a)
        direct = {
            int(D * inverse_h % a)
            for D in divisors_square_factors(factors)
        }
        assert crt_log_feasible(h, a, factors) == (a - 1 in direct)
        assert ratio_success(h, a, factors) == (a - 1 in direct)
        lattice_rows += 1
    assert lattice_rows == 360

    # Build an M-ascending table retaining every Python-int D, rather than
    # only the class sets cached by (bc).  It serves both the sqrt replay and
    # the a_1/W census.
    modulus_data = []
    for M in range(3, 3_001, 4):
        A = (M + 1) // 4
        by_class = {}
        for D in divisors_square_factors(factors_py(A)):
            by_class.setdefault(int((-4 * D) % M), []).append(int(D))
        modulus_data.append((M, {
            residue: tuple(sorted(values))
            for residue, values in by_class.items()
        }))

    def first_modulus_row(p):
        for M, by_class in modulus_data:
            values = by_class.get(p % M)
            if values:
                candidates = []
                for D in values:
                    assert (p + 4 * D) % M == 0
                    a = (p + 4 * D) // M
                    if a > 0:
                        candidates.append((int(a), int(D)))
                if candidates:
                    a, D = min(candidates)
                    check_prime_witness(p, a, D)
                    return M, a, D
        raise AssertionError(("modulus cap exhausted", p))

    sqrt_total = sqrt_factored = sqrt_late = 0
    sqrt_late_rows = []
    for low in range(2, 300_001, 50_000):
        high = min(300_001, low + 50_000)
        for p0 in primerange(low, high):
            p = int(p0)
            if p % 24 != 1:
                continue
            sqrt_total += 1
            W, _, _ = first_modulus_row(p)
            shifted_factors = factors_py(p + 4)
            has_three = any(q % 4 == 3 for q, _ in shifted_factors)
            if has_three:
                sqrt_factored += 1
                assert W * W <= p + 4
            if W * W > p + 4:
                sqrt_late += 1
                assert all(q % 4 == 1 for q, _ in shifted_factors)
                sqrt_late_rows.append((p, W, shifted_factors))
    assert (sqrt_total, sqrt_factored, sqrt_late) == (3202, 1517, 2)
    assert sqrt_late_rows == [
        (193, 15, ((197, 1),)),
        (3_361, 99, ((5, 1), (673, 1))),
    ]

    # The four late/record values all miss D=1 globally, not just below W.
    gap_expected = {
        225_289: {37: 1, 6_089: 1},
        954_409: {181: 1, 5_273: 1},
        1_853_329: {1_853_333: 1},
        2_031_121: {5: 3, 16_249: 1},
    }
    assert {p: {int(q): int(e) for q, e in factorint(p + 4).items()}
            for p in gap_expected} == gap_expected
    assert all(q % 4 == 1 for factors in gap_expected.values()
               for q in factors)

    def first_a(p):
        B = (p + 1) // 3
        for a in range(3, 2 * B + 1, 4):
            h = (p + a) // 4
            if ratio_success(h, a):
                return a
        return None

    # The default census is complete through 10^6; the research replay to
    # 10^7 is intentionally gated.  Prime generation is chunked and every
    # factor/divisor value remains a Python int.
    full_scan = os.environ.get("ES_FULL_SCAN") == "1"
    census_limit = 10_000_000 if full_scan else 1_000_000
    census = {}
    for low in range(2, census_limit + 1, 250_000):
        high = min(census_limit + 1, low + 250_000)
        for p0 in primerange(low, high):
            p = int(p0)
            if p % 24 != 1:
                continue
            a1 = first_a(p)
            assert a1 is not None
            W, a_W, D_W = first_modulus_row(p)
            census[p] = (a1, W, a_W, D_W)

    histogram = Counter(row[0] for row in census.values())
    expected_histogram = (
        {3: 47_137, 7: 28_606, 11: 4_419, 15: 961, 19: 766,
         23: 637, 27: 63, 31: 183, 35: 27, 39: 44, 43: 7, 47: 23,
         51: 2, 55: 4, 59: 4, 63: 1, 71: 2, 107: 1}
        if full_scan else
        {3: 5_192, 7: 3_551, 11: 584, 15: 131, 19: 113, 23: 96,
         27: 8, 31: 33, 35: 4, 39: 9, 43: 1, 47: 3, 51: 2,
         55: 2, 59: 2, 63: 1}
    )
    assert dict(sorted(histogram.items())) == expected_histogram
    assert len(census) == (82_887 if full_scan else 9_732)

    maximum_a1 = max((row[0], p) for p, row in census.items())
    maximum_W = max((row[1], p) for p, row in census.items())
    assert maximum_a1 == ((107, 8_803_369) if full_scan
                          else (63, 87_481))
    assert maximum_W == ((2_495, 2_031_121) if full_scan
                         else (335, 954_409))

    xs = [row[0] for row in census.values()]
    ys = [row[1] for row in census.values()]
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    pearson = (
        sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
        / (sum((x - mean_x)**2 for x in xs)
           * sum((y - mean_y)**2 for y in ys))**0.5
    )
    assert round(pearson, 6) == (0.271029 if full_scan else 0.354836)

    separation = Counter(
        "equal" if row[2] == row[0] else
        "a_W_larger" if row[2] > row[0] else "a_W_smaller"
        for row in census.values()
    )
    assert separation == Counter({"a_W_larger": len(census)})
    max_ratio = max((Fraction(row[2], row[0]), p, row)
                    for p, row in census.items())
    max_difference = max((row[2] - row[0], p, row)
                         for p, row in census.items())
    assert max_ratio == (
        (Fraction(1_428_563, 3), 9_999_937,
         (3, 7, 1_428_563, 1))
        if full_scan else
        (Fraction(142_791, 3), 999_529, (3, 7, 142_791, 2))
    )
    assert max_difference == (
        (1_428_560, 9_999_937, (3, 7, 1_428_563, 1))
        if full_scan else
        (142_788, 999_529, (3, 7, 142_791, 2))
    )

    anatomy_pins = {
        p: (first_a(p),) + first_modulus_row(p)
        for p in gap_expected
    }
    assert anatomy_pins == {
        225_289: (31, 279, 811, 245),
        954_409: (3, 335, 2_855, 504),
        1_853_329: (3, 383, 4_839, 2),
        2_031_121: (11, 2_495, 815, 576),
    }
    research_maximum_pin = (
        first_a(8_803_369),
        *first_modulus_row(8_803_369),
    )
    assert research_maximum_pin == (107, 139, 63_335, 49)

    print("taxonomy (D1,proper-DIV) / fixed-D / CRT feasibility rows =",
          ((len(family_rows), len(proper_div_rows)), fixed_D_rows, lattice_rows))
    print("sqrt replay (hard,3mod4-shift-factor,W>sqrt) =",
          (sqrt_total, sqrt_factored, sqrt_late))
    print("a1 census (limit,count,hist,max a1,max W,Pearson) =",
          (census_limit, len(census), dict(sorted(histogram.items())),
           maximum_a1, maximum_W, round(pearson, 6)))
    print("a1/a_W separation (directions,max ratio,max difference) =",
          (dict(separation), max_ratio, max_difference))
    print("late-prime a1/W/a_W/D pins =", anatomy_pins)
    print("research maximum-a1 pin =", research_maximum_pin)


print("\n== (bj) algebraic taxonomy, sqrt regime, and first-a index (§63) ==")
check_bj()


# ---------------------------------------------------------------- (bk)
def check_bk():
    """§64: cancellation cover, shifted sieves, and wider twisted hunt."""
    import os
    from random import Random

    full_scan = os.environ.get("ES_FULL_SCAN") == "1"

    # All products and divisors in this block are ordinary Python ints.
    def square_divisors_int(value):
        divisors = [1]
        for q0, exponent0 in factorint(value).items():
            q, exponent = int(q0), int(exponent0)
            base = tuple(divisors)
            power = 1
            for _ in range(2 * exponent):
                power = int(power * q)
                divisors.extend(int(D * power) for D in base)
        return divisors

    def harvested_class_rows(cap):
        rows = []
        for M in range(3, cap + 1, 4):
            A = (M + 1) // 4
            classes = {int((-4 * D) % M)
                       for D in square_divisors_int(A)}
            rows.append((M, classes))
        return rows

    stage1_rows = harvested_class_rows(10_000)
    assert (len(stage1_rows), sum(len(classes) for _, classes in stage1_rows),
            max(len(classes) for _, classes in stage1_rows)) == (
                2500, 64_978, 243
            )

    def valuation(value, q):
        exponent = 0
        while value % q == 0:
            value //= q
            exponent += 1
        return exponent

    def dual_rows(n):
        B = (n + 1) // 3
        for a in range(1, 2 * B + 1):
            if (n + a) % 4:
                continue
            h = (n + a) // 4
            for D in square_divisors_int(h):
                if (D + h) % a:
                    continue
                A = (D + h) // a
                yield a, h, D, A

    # Exact small replay of the finite normal form.  The global bound for
    # n<=80 is below 10^4, so this compares complete minima, including the
    # empty square rows, with the independent M-side class harvest.
    small_dual_W = {}
    for n in range(1, 81):
        dual_values = [4 * A - 1 for a, h, D, A in dual_rows(n)
                       if A * A % D == 0]
        dual_minimum = min(dual_values, default=None)
        class_minimum = next(
            (M for M, classes in stage1_rows if n % M in classes), None
        )
        assert dual_minimum == class_minimum
        small_dual_W[n] = dual_minimum
    assert (sum(W is None for W in small_dual_W.values()),
            max(W for W in small_dual_W.values() if W is not None),
            sum(W for W in small_dual_W.values() if W is not None)) == (
                8, 47, 692
            )

    # The cancellation-cover criterion is checked on complete finite row
    # sets for seeded n.  A failed eligibility prime must occur in a and D,
    # divide n, and satisfy the exact valuation window (64.3).
    rng = Random(640027)
    cancellation_rows = cancellation_failures = 0
    cancellation_targets = tuple(rng.sample(range(81, 1001), 64))
    for n in cancellation_targets:
        for a, h, D, A in dual_rows(n):
            cancellation_rows += 1
            assert (a * A - D) == h and h * h % D == 0
            assert (a * a * A * A) % D == 0
            bad = []
            for q0 in factorint(D):
                q = int(q0)
                d = valuation(D, q)
                alpha = valuation(a, q)
                beta = valuation(A, q)
                if d > 2 * beta:
                    bad.append(q)
                    assert alpha > 0 and n % q == 0
                    assert 2 * beta < d <= 2 * alpha + 2 * beta
            assert bool(bad) == (A * A % D != 0)
            cancellation_failures += bool(bad)

    assert (cancellation_rows, cancellation_failures) == (3523, 2347)

    # D=1 and D=2 are cancellation-immune original-coordinate layers.  The
    # direct factorizations below check the exact support descriptions.
    def odd_prime_factors(value):
        return tuple(int(q) for q in factorint(value)
                     if int(q) != 2)

    def shifted_four_passes(n):
        return all(q % 4 == 1 for q in odd_prime_factors(n + 4))

    def shifted_eight_passes(n):
        residues = {q % 8 for q in odd_prime_factors(n + 8)}
        return 7 not in residues and not ({3, 5} <= residues)

    shifted_four_count = shifted_both_count = 0
    for n in range(1, 5001):
        pass_four = shifted_four_passes(n)
        pass_eight = shifted_eight_passes(n)
        shifted_four_count += pass_four
        shifted_both_count += pass_four and pass_eight
        q3 = tuple(q for q in odd_prime_factors(n + 4) if q % 4 == 3)
        assert pass_four == (not q3)
        if q3:
            M = min(q3)
            assert n % M in stage1_rows[(M - 3) // 4][1]
            assert 1 in square_divisors_int((M + 1) // 4)
        factors8 = odd_prime_factors(n + 8)
        q7 = tuple(q for q in factors8 if q % 8 == 7)
        q3s = tuple(q for q in factors8 if q % 8 == 3)
        q5s = tuple(q for q in factors8 if q % 8 == 5)
        divisor7 = (q7[0] if q7 else q3s[0] * q5s[0]
                    if q3s and q5s else None)
        assert pass_eight == (divisor7 is None)
        if divisor7 is not None:
            M = int(divisor7)
            assert M % 8 == 7 and (n + 8) % M == 0
            A = (M + 1) // 4
            assert A % 2 == 0 and A * A % 2 == 0
    assert (shifted_four_count, shifted_both_count) == (1170, 521)
    assert {
        n: (factorint(n + 4), factorint(n + 8))
        for n in (288, 336, 4545)
    } == {
        288: ({2: 2, 73: 1}, {2: 3, 37: 1}),
        336: ({2: 2, 5: 1, 17: 1}, {2: 3, 43: 1}),
        4545: ({4549: 1}, {29: 1, 157: 1}),
    }

    # Every dyadic class in (64.7) carries the displayed D=1 or D=2 datum.
    dyadic_rows = 0
    for exponent in range(11):
        for k in range(21):
            n1 = (1 << exponent) * (4 * k + 3) - 4
            if n1 > 0:
                M = 4 * k + 3
                assert M % 4 == 3 and (n1 + 4) % M == 0
                dyadic_rows += 1
            n2 = (1 << exponent) * (8 * k + 7) - 8
            if n2 > 0:
                M = 8 * k + 7
                A = (M + 1) // 4
                assert M % 8 == 7 and (n2 + 8) % M == 0
                assert A * A % 2 == 0
                dyadic_rows += 1

    # Twisted-square D=1 residue exclusions: for q=3 mod 4 the congruence
    # sm^2=-4 mod q has roots exactly when (s/q)=-1.
    twisted_residue_rows = 0
    for q0 in primerange(3, 200):
        q = int(q0)
        if q % 4 != 3:
            continue
        for s in range(2, 51):
            if q == s or any(e != 1 for e in factorint(s).values()):
                continue
            if s % q == 0 or jacobi_symbol(s, q) != -1:
                continue
            roots = tuple(r for r in range(q) if (s * r * r + 4) % q == 0)
            assert len(roots) == 2
            m = int(roots[0] + q * rng.randrange(1, 8))
            n = int(s * m * m)
            assert (n + 4) % q == 0
            assert n % q in stage1_rows[(q - 3) // 4][1]
            twisted_residue_rows += 1

    # The ratio law needs primality only to force a unit branch.  On any odd
    # composite unit branch it gives the same exact witness criterion.
    unit_ratio_rows = unit_ratio_hits = unit_composite_rows = 0
    for _ in range(300):
        n = rng.randrange(3, 3000, 2)
        B = (n + 1) // 3
        choices = [a for a in range(1, 2 * B + 1)
                   if (n + a) % 4 == 0 and gcd(a, n) == 1]
        if not choices:
            continue
        a = int(rng.choice(choices))
        h = (n + a) // 4
        assert gcd(a, h) == 1
        divisors = square_divisors_int(h)
        inverse_h = pow(h, -1, a)
        ratio_hit = (a - 1) in {
            int(D * inverse_h % a) for D in divisors
        }
        quotient = [D for D in divisors if (D + h) % a == 0]
        assert ratio_hit == bool(quotient)
        for D in quotient:
            A = (D + h) // a
            assert gcd(a, D) == 1 and A * A % D == 0
        unit_ratio_rows += 1
        unit_ratio_hits += ratio_hit
        n_factorization = factorint(n)
        unit_composite_rows += (
            len(n_factorization) != 1
            or int(next(iter(n_factorization.values()))) != 1
        )

    assert (dyadic_rows, twisted_residue_rows,
            unit_ratio_rows, unit_ratio_hits, unit_composite_rows) == (
                460, 359, 300, 9, 226
            )

    # Full unfiltered quotient ledgers for the three sporadics.  These extend
    # (60.21)/(62.24): every failure-prime set lies in the support of n.
    gcd_ledgers = {}
    failure_ledgers = {}
    for n in (288, 336, 4545):
        gcd_counts = Counter()
        failure_counts = Counter()
        for a, h, D, A in dual_rows(n):
            G = gcd(a, D)
            failures = tuple(
                int(q) for q in factorint(D)
                if valuation(D, int(q)) > 2 * valuation(A, int(q))
            )
            assert failures and all(n % q == 0 for q in failures)
            gcd_counts[G] += 1
            failure_counts[failures] += 1
        gcd_ledgers[n] = gcd_counts
        failure_ledgers[n] = failure_counts
    assert gcd_ledgers == {
        288: Counter({96: 12, 9: 6, 3: 5, 6: 4, 12: 3,
                      16: 3, 18: 3, 36: 3, 4: 2, 24: 2}),
        336: Counter({48: 14, 112: 10, 6: 8, 3: 6, 21: 6,
                      7: 4, 42: 4, 8: 3, 2: 2, 4: 2, 14: 2,
                      24: 2, 16: 1, 28: 1}),
        4545: Counter({15: 73, 45: 35, 303: 20, 9: 18, 3: 15,
                       5: 13, 1515: 8, 101: 3, 909: 3}),
    }
    assert failure_ledgers == {
        288: Counter({(2, 3): 18, (3,): 17, (2,): 8}),
        336: Counter({(2, 3): 15, (2,): 12, (3,): 11,
                      (2, 7): 10, (7,): 10, (3, 7): 5,
                      (2, 3, 7): 2}),
        4545: Counter({(3, 5): 73, (3,): 46, (5,): 35,
                       (3, 101): 18, (101,): 8,
                       (3, 5, 101): 6, (5, 101): 2}),
    }

    # Exact support tests used to reduce the hunt before the general class
    # walk.  Trial division is complete through sqrt(max n+8), and values are
    # streamed one at a time.
    def shifted_support_tests(candidates):
        four = both = 0
        for n, _, _ in candidates:
            pass_four = shifted_four_passes(n)
            four += pass_four
            both += pass_four and shifted_eight_passes(n)
        return four, both

    def squarefree_values(cap):
        return tuple(s for s in range(2, cap + 1)
                     if all(int(e) == 1 for e in factorint(s).values()))

    def make_candidates(s_cap, m_cap, low, high, exclude_old):
        kernels = squarefree_values(s_cap)
        candidates = []
        for s in kernels:
            for m in range(1, m_cap + 1):
                if exclude_old and s <= 1000 and m <= 300:
                    continue
                n = int(s * m * m)
                if low < n <= high:
                    candidates.append((n, s, m))
        assert len({n for n, _, _ in candidates}) == len(candidates)
        return kernels, candidates

    def complete_dual_decision(n):
        best = None
        for a, h, D, A in dual_rows(n):
            if A * A % D:
                continue
            M = 4 * A - 1
            if best is None or M < best:
                best = M
        return best

    def staged_hunt(candidates):
        # Walk moduli, not a candidate/modulus Cartesian array.  Resolved
        # values are deleted immediately, so memory and work shrink at every
        # stage; the first hit is the exact least W.
        active = {n: (s, m) for n, s, m in candidates}
        least = {}
        for M, classes in stage1_rows:
            for n in tuple(active):
                if n % M in classes:
                    least[n] = M
                    del active[n]
            if not active:
                break
        stage1_survivors = tuple(
            (n, *active[n]) for n in sorted(active)
        )

        if active:
            for M in range(10_003, 1_000_001, 4):
                A = (M + 1) // 4
                classes = {int((-4 * D) % M)
                           for D in square_divisors_int(A)}
                for n in tuple(active):
                    if n % M in classes:
                        least[n] = M
                        del active[n]
                if not active:
                    break
        stage2_survivors = tuple(
            (n, *active[n]) for n in sorted(active)
        )
        final_infinities = tuple(
            n for n in sorted(active) if complete_dual_decision(n) is None
        )
        maximum_W = max(least.values(), default=0)
        maximum_rows = tuple(sorted(
            (n, s, m) for n, s, m in candidates
            if least.get(n) == maximum_W
        ))
        return (stage1_survivors, stage2_survivors, final_infinities,
                maximum_W, maximum_rows)

    if full_scan:
        s_cap, m_cap = 2000, 600
    else:
        s_cap, m_cap = 400, 350
    kernels, candidates = make_candidates(
        s_cap, m_cap, 1_000_000, 100_000_000, True
    )
    shifted_counts = shifted_support_tests(candidates)
    staged = staged_hunt(candidates)
    hunt_summary = (
        len(kernels), len(candidates), *shifted_counts,
        len(staged[0]), len(staged[1]), staged[2],
        (staged[3], staged[4]),
    )
    assert hunt_summary == (
        (1214, 242_837, 50_633, 18_943, 0, 0, (),
         (5303, ((3_201_660, 15, 462),)))
        if full_scan else
        (242, 11_833, 2_406, 872, 0, 0, (),
         (2147, ((1_359_015, 15, 301),)))
    )
    if full_scan:
        assert len(candidates) + 146_016 == 388_853
        maximum_pin = (3_201_660, 5303, 338, 604)
    else:
        maximum_pin = (1_359_015, 2147, 9, 633)
    n, M, D, a = maximum_pin
    assert D in square_divisors_int((M + 1) // 4)
    assert n + 4 * D == a * M

    thin_summary = None
    if full_scan:
        thin_kernels, thin_candidates = make_candidates(
            50, 2000, 100_000_000, 1_000_000_000, False
        )
        thin_shifted = shifted_support_tests(thin_candidates)
        thin_staged = staged_hunt(thin_candidates)
        thin_summary = (
            len(thin_kernels), len(thin_candidates), *thin_shifted,
            len(thin_staged[0]), len(thin_staged[1]), thin_staged[2],
            (thin_staged[3], thin_staged[4]),
        )
        assert thin_summary == (
            30, 4_992, 904, 314, 0, 0, (),
            (599, ((108_868_200, 42, 1610),)),
        )
        n, M, D, a = (108_868_200, 599, 7500, 181_800)
        assert D in square_divisors_int((M + 1) // 4)
        assert n + 4 * D == a * M

    # Uniform-independent comparison only; exact class sizes are pinned, but
    # this product has no theorem status.
    model_probability = 1.0
    for M, classes in stage1_rows:
        model_probability *= 1.0 - len(classes) / M
    assert f"{model_probability:.12e}" == "1.033524640428e-12"

    print("cancellation cover / shifted layers / unit branches =",
          (cancellation_rows, cancellation_failures,
           shifted_four_count, shifted_both_count, dyadic_rows,
           twisted_residue_rows, unit_ratio_rows, unit_ratio_hits,
           unit_composite_rows))
    print("full sporadic gcd and failure-prime ledgers =",
          (gcd_ledgers, failure_ledgers))
    print("wider twisted-square hunt "
          "(s,pop,D1-pass,D1+D2-pass,stage1,stage2,infinity,max) =",
          hunt_summary)
    if thin_summary is not None:
        print("thin >10^8 twisted-square hunt =", thin_summary)
    print("uniform-independent no-hit product through M=10^4 =",
          model_probability)


print("\n== (bk) gcd mechanism, shifted constraints, and wider hunt (§64) ==")
check_bk()


# ---------------------------------------------------------------- (bl)
def check_bl():
    """§65: bounded W-record and anatomy replay (not a full prime rescan)."""
    import os
    from random import Random
    from sympy import divisors as sympy_divisors
    from time import perf_counter

    started = perf_counter()
    full_scan = os.environ.get("ES_FULL_SCAN") == "1"
    modulus_cap = 30_000 if full_scan else 3_000

    # Rebuild both class systems locally.  The first expands factorint(A) to
    # the divisors of A^2; the second calls SymPy's direct divisors(A*A).
    # All divisor products and residues are explicitly ordinary Python ints.
    def factor_square_divisors(A):
        values = [1]
        for q0, exponent0 in factorint(int(A)).items():
            q, exponent = int(q0), int(exponent0)
            values = [int(D * q**e) for D in values
                      for e in range(2 * exponent + 1)]
        return values

    factor_rows = []
    direct_rows = []
    for M in range(3, modulus_cap + 1, 4):
        A = (M + 1) // 4
        factor_classes = frozenset(
            int((-4 * D) % M) for D in factor_square_divisors(A)
        )
        direct_classes = frozenset(
            int((-4 * int(D)) % M)
            for D in sympy_divisors(int(A * A))
        )
        assert factor_classes == direct_classes
        factor_rows.append((M, factor_classes))
        direct_rows.append((M, direct_classes))
    factor_rows, direct_rows = tuple(factor_rows), tuple(direct_rows)
    assert len(factor_rows) == (modulus_cap + 1) // 4

    def row_W(P, rows):
        return next((M for M, classes in rows if P % M in classes), None)

    records = (
        (73, 7), (193, 15), (1201, 31), (2521, 47), (3361, 99),
        (33_289, 155), (90_841, 167), (144_169, 191), (167_521, 259),
        (225_289, 279), (361_321, 287), (915_961, 303), (954_409, 335),
        (1_853_329, 383), (2_031_121, 2495),
    )
    default_records = tuple(row for row in records if row[0] <= 1_000_000)
    replay_records = records if full_scan else default_records
    for P, expected in replay_records:
        assert row_W(P, factor_rows) == expected
        assert row_W(P, direct_rows) == expected

    # The four §62.22 rows are always replayed, including their exact (a,D)
    # anatomy and a Lemma-16.1 fraction reconstruction.
    late_rows = {
        225_289: (279, 811, 245),
        954_409: (335, 2855, 504),
        1_853_329: (383, 4839, 2),
        2_031_121: (2495, 815, 576),
    }

    def fraction_reconstruction(P, M, D):
        A = (M + 1) // 4
        D_factors = {int(q): int(e) for q, e in factorint(D).items()}
        u = v = w = 1
        for q0, exponent0 in factorint(A).items():
            q, exponent = int(q0), int(exponent0)
            d_exponent = D_factors.get(q, 0)
            u_exponent = d_exponent // 2
            w_exponent = d_exponent - 2 * u_exponent
            v_exponent = exponent - u_exponent - w_exponent
            assert v_exponent >= 0
            u *= q**u_exponent
            v *= q**v_exponent
            w *= q**w_exponent
        assert u * v * w == A and u * u * w == D
        assert (P * v + u) % M == 0
        s = (P * v + u) // M
        x, y, z = s * u * w, P * s * v * w, P * u * v * w
        assert (Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
                == Fraction(4, P))

    for P, (M, expected_a, expected_D) in late_rows.items():
        assert row_W(P, factor_rows) == M
        assert row_W(P, direct_rows) == M
        A = (M + 1) // 4
        firing = tuple(D for D in factor_square_divisors(A)
                       if (P + 4 * D) % M == 0)
        D = min(firing)
        assert D == firing[0]
        a = (P + 4 * D) // M
        assert (a, D) == (expected_a, expected_D)
        assert D in {int(d) for d in sympy_divisors(int(A * A))}
        assert P % M == (-4 * D) % M and a * M == P + 4 * D
        fraction_reconstruction(P, M, D)

    # At least 1000 seeded random hard primes get independent-path minima.
    hard_spot = tuple(int(P) for P in primerange(2, 100_000)
                      if P % 24 == 1)
    assert len(hard_spot) == 1181
    rng = Random(650027)
    spot = tuple(hard_spot[i]
                 for i in rng.sample(range(len(hard_spot)), 1000))
    for P in spot:
        first = row_W(P, factor_rows)
        second = row_W(P, direct_rows)
        assert first is not None and first == second

    # Recompute the selected minimum D for the complete small exact prefix.
    # The §61.3 convention is the least firing D (equivalently least (a,D)
    # at fixed M).  Pin that it also equals the first expansion-order hit in
    # this prefix; expansion order is an observed coincidence, not the rule.
    parity = Counter()
    for P in hard_spot:
        M = row_W(P, factor_rows)
        A = (M + 1) // 4
        firing = tuple(D for D in factor_square_divisors(A)
                       if (P + 4 * D) % M == 0)
        D = min(firing)
        assert D == firing[0]
        parity["even" if D % 2 == 0 else "odd"] += 1
    assert parity == Counter({"even": 706, "odd": 475})

    # Check the wave-27 p+4 prediction exactly on the requested default
    # record prefix.  The full mode extends this only to the displayed full
    # table; neither mode rescans all primes through the census endpoint.
    structural_records = records if full_scan else default_records
    antecedent = []
    for P, M in structural_records:
        if M > isqrt(P + 4):
            antecedent.append(P)
            assert all(int(q) % 4 != 3 for q in factorint(P + 4))
    assert tuple(antecedent) == (
        (193, 3361, 2_031_121) if full_scan else (193, 3361)
    )

    print("W-record bounded replay "
          "(cap,records,late rows,seeded spots,small parity,seconds) =",
          (modulus_cap, len(replay_records), len(late_rows), len(spot),
           dict(parity), perf_counter() - started))
    if full_scan:
        print("ES_FULL_SCAN §65 scope: all 15 claimed record primes below "
              "10^8; this is intentionally not a rescan of all 719781 primes")


print("\n== (bl) W-record census and anatomy (§65) ==")
check_bl()


# ---------------------------------------------------------------- (bn)
def check_bn():
    """§67: extremal anatomy, residue-one examples, and spacing inputs."""
    import importlib.util
    import os
    from random import Random
    from time import perf_counter
    from sympy import isprime, primepi

    started = perf_counter()

    # Every divisor product below is an ordinary Python int.  Keep no
    # factorization table: one shifted integer is live at a time.
    def divisors_int(n):
        values = [1]
        for q0, e0 in factorint(int(n)).items():
            q, e = int(q0), int(e0)
            values = [int(D * q**j) for D in values for j in range(e + 1)]
        return tuple(values)

    def square_divisors_int_local(n):
        values = [1]
        for q0, e0 in factorint(int(n)).items():
            q, e = int(q0), int(e0)
            values = [int(D * q**j) for D in values
                      for j in range(2 * e + 1)]
        return tuple(values)

    def factor_string(n):
        return "*".join(
            str(int(q)) if int(e) == 1 else f"{int(q)}^{int(e)}"
            for q, e in sorted(factorint(int(n)).items())
        )

    def succeeds_a(P, a):
        h = (P + a) // 4
        assert 4 * h == P + a and gcd(a, h) == 1
        target = (-h) % a
        return any(D % a == target for D in square_divisors_int_local(h))

    def first_a(P):
        a = 3
        while not succeeds_a(P, a):
            a += 4
        return a

    def purity_first(P, cap=100):
        for D in range(1, cap + 1):
            firing = []
            for M in divisors_int(P + 4 * D):
                if M % 4 != 3 or M <= 4 * D:
                    continue
                A = (M + 1) // 4
                if (A * A) % D == 0:
                    firing.append(M)
            if firing:
                return D - 1, D, min(firing)
        raise AssertionError((P, cap))

    top = (
        (2_031_121, 2495, 11,
         (11, 19, 39, 55, 59, 95, 111, 139, 167, 179),
         28, 29, 52_083,
         ("5^3*16249", "3^3*75227", "13*156241", "2031137")),
        (88_808_281, 1007, 3,
         (3, 15, 19, 23, 35, 43, 59, 127, 131, 135, 159),
         7, 8, 2783,
         ("5*349*50893", "3*17*1741339", "7*331*38329", "88808297")),
        (39_203_761, 923, 7,
         (7, 11, 27, 47, 71, 107, 127, 143, 159, 167),
         10, 11, 94_467,
         ("5*401*19553", "3*11*1187993", "7^2*800077", "67*585131")),
        (43_371_241, 923, 7,
         (7, 35, 43, 71, 103, 179, 187, 199),
         1, 2, 1223,
         ("5*8674249", "3*1223*11821", "43371253", "43371257")),
        (21_475_609, 911, 7,
         (7, 27, 35, 51, 71, 103, 107, 111, 119, 151, 183, 191),
         9, 10, 15_439,
         ("21475613", "3*7158539", "21475621", "5^4*34361")),
        (23_836_201, 911, 11,
         (11, 19, 27, 31, 35, 47, 55, 59, 63, 71, 87, 111, 131, 135, 183),
         1, 2, 1759,
         ("5*4767241", "3*1759*4517", "23836213", "433*55049")),
        (62_850_769, 911, 3,
         (3, 23, 43, 47, 51, 55, 67, 71, 75, 83, 95, 99, 103, 111, 119, 131, 151),
         6, 7, 1987,
         ("62850773", "3*11*601*3169", "7^2*211*6079", "5*17*101*7321")),
        (22_706_161, 783, 11,
         (11, 19, 47, 55, 59, 79, 131, 143),
         13, 14, 783,
         ("5*4541233", "3*17*41*10859", "7*3243739", "13*1746629")),
        (5_214_049, 747, 3,
         (3, 7, 11, 15, 39, 47, 71, 83, 95, 131, 191),
         14, 15, 27_299,
         ("13*17*23593", "3*1738019", "5214061", "5*89*11717")),
        (5_309_329, 719, 7,
         (7, 11, 23, 31, 39, 63, 107, 111, 131, 171),
         1, 2, 1047,
         ("5309333", "3*11*349*461", "19*103*2713", "5*1061869")),
    )

    # One ascending class system gives every displayed W and the spacing
    # masses.  Its largest row is the observed record itself.
    class_rows = []
    for M in range(3, 2496, 4):
        A = (M + 1) // 4
        classes = frozenset(int((-4 * D) % M)
                            for D in square_divisors_int_local(A))
        class_rows.append((M, classes))
    class_rows = tuple(class_rows)

    def row_W(P):
        return next((M for M, classes in class_rows
                     if P % M in classes), None)

    profiles = []
    for P, expected_W, expected_a1, expected_success, expected_tau, expected_D, expected_M, expected_factors in top:
        assert row_W(P) == expected_W
        success = tuple(a for a in range(3, 201, 4) if succeeds_a(P, a))
        assert success == expected_success
        assert 50 - len(success) in (33, 35, 38, 39, 40, 42)
        assert first_a(P) == expected_a1
        assert purity_first(P) == (expected_tau, expected_D, expected_M)
        observed_factors = tuple(factor_string(P + 4 * D) for D in range(1, 5))
        assert observed_factors == expected_factors
        assert all(int(q) % 4 == 1 for q in factorint(P + 4))
        profiles.append((P, expected_W, expected_a1, expected_tau))
    assert tuple(50 - len(row[3]) for row in top) == (
        40, 39, 40, 42, 38, 35, 33, 42, 39, 40,
    )
    # Explicitly pin the requested independently recomputed top-three rows.
    assert tuple((first_a(P),) + purity_first(P)
                 for P, *_ in top[:3]) == (
        (11, 28, 29, 52_083),
        (3, 7, 8, 2783),
        (7, 10, 11, 94_467),
    )

    # §54.1 uses the full lcm(1,...,T).  Exhaust k in order, then replay W
    # and a_1 from the same direct definitions as above.
    residue_rows = (
        (15, 360_360, 12, 4_324_321, 23, 8, 3, 0.229656),
        (19, 232_792_560, 1, 232_792_561, 183, 164, 27, 0.192308),
        (23, 5_354_228_880, 2, 10_708_457_761, 47, 24, 7, 0.198258),
        (27, 80_313_433_200, 5, 401_567_166_001, 71, 44, 7, 0.204634),
    )
    for T, expected_L, expected_k, expected_p, expected_W, excess, expected_a1, linnik_ratio in residue_rows:
        L = 1
        for n in range(1, T + 1):
            L = lcm(L, n)
        assert L == expected_L and L % 24 == 0
        k = 1
        while not isprime(1 + k * L):
            k += 1
        P = 1 + k * L
        assert (k, P) == (expected_k, expected_p)
        observed_W = row_W(P)
        assert observed_W == expected_W and observed_W > T
        assert observed_W - T == excess
        assert first_a(P) == expected_a1
        assert round(log(P) / (5.2 * log(L)), 6) == linnik_ratio
    # The task specifically requires default least-prime/W replays at 15,19.
    assert tuple((row[0], row[3], row[4]) for row in residue_rows[:2]) == (
        (15, 4_324_321, 23), (19, 232_792_561, 183),
    )

    records = (
        (73, 7, 1.336115), (193, 15, 1.630725),
        (1201, 31, 1.753095), (2521, 47, 1.870574),
        (3361, 99, 2.194077), (33_289, 155, 2.152501),
        (90_841, 167, 2.101766), (144_169, 191, 2.122345),
        (167_521, 259, 2.234072), (225_289, 279, 2.242045),
        (361_321, 287, 2.220056), (915_961, 303, 2.181299),
        (954_409, 335, 2.217096), (1_853_329, 383, 2.228161),
        (2_031_121, 2495, 2.923244),
    )
    for P, W, expected in records:
        assert round(log(W) / log(log(P)), 6) == expected

    # Rebuild the independent-hit product conditional on the hard residue.
    raw = 1.0
    raw_at = {}
    thresholds = {255, 383, 511, 639, 767, 2495}
    for M, classes in class_rows:
        g = gcd(M, 24)
        allowed = tuple(r for r in range(M)
                        if r % g == 1 % g and gcd(r, M) == 1)
        hits = sum(r in classes for r in allowed)
        raw *= 1.0 - hits / len(allowed)
        if M in thresholds:
            raw_at[M] = raw
    assert round(-log(raw), 6) == 20.522039
    assert f"{raw:.6e}" == "1.222902e-09"
    calibration_counts = {255: 421, 383: 109, 511: 45, 639: 16, 767: 8}
    expected_betas = {
        255: 0.871712, 383: 0.863214, 511: 0.844367,
        639: 0.852878, 767: 0.846176,
    }
    for T, count in calibration_counts.items():
        beta = log(count / 719_781) / log(raw_at[T])
        assert round(beta, 6) == expected_betas[T]

    six_failure_product = prod((
        8814 / 66_667, 25_359 / 85_715, 34_046 / 90_910,
        26_423 / 53_333, 46_679 / 94_737, 54_165 / 95_653,
    ))
    assert round(six_failure_product, 6) == 0.002025
    assert sum((63, 183, 27, 44, 7, 23, 2, 4, 4, 1, 2, 1)) == 361
    assert round(361 / 82_887, 6) == 0.004355

    calibrated = raw**0.85
    assert f"{calibrated:.5e}" == "2.65633e-08"
    expected_now = calibrated * 636_894
    assert (int(primepi(10**8)), int(primepi(10**9))) == (
        5_761_455, 50_847_534,
    )
    future_population = (int(primepi(10**9)) - int(primepi(10**8))) / 8
    expected_future = calibrated * future_population
    assert round(expected_now, 4) == 0.0169
    assert round(expected_future, 4) == 0.1497
    assert f"{future_population:.3e}" == "5.636e+06"
    now_band = (raw**0.90 * 636_894, raw**0.80 * 636_894)
    future_band = (raw**0.90 * future_population,
                   raw**0.80 * future_population)
    assert tuple(round(x, 4) for x in now_band) == (0.0061, 0.0472)
    assert tuple(round(x, 4) for x in future_band) == (0.0537, 0.4177)
    assert round(exp(-expected_now), 4) == 0.9832

    # Seeded links between the class and dual-a coordinates.  This is not a
    # census: it independently reconstructs one firing divisor on each row.
    hard_spot = tuple(int(P) for P in primerange(73, 100_000)
                      if P % 24 == 1)
    rng = Random(670028)
    for P in (hard_spot[i]
              for i in rng.sample(range(len(hard_spot)), 128)):
        M = row_W(P)
        assert M is not None
        A = (M + 1) // 4
        firing = tuple(D for D in square_divisors_int_local(A)
                       if P % M == (-4 * D) % M)
        assert firing
        D = min(firing)
        a = (P + 4 * D) // M
        h = (P + a) // 4
        assert a % 4 == 3 and h * h % D == 0
        assert D % a == (-h) % a and succeeds_a(P, a)

    full_scan = os.environ.get("ES_FULL_SCAN") == "1"
    if full_scan:
        # Reuse only the durable independent scanner, not verify.py helpers.
        spec = importlib.util.spec_from_file_location(
            "review65_for_bn", "scripts/review65_independent.py"
        )
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        full_rows, _ = module.build_rows(2495)
        hard = module.hard_primes_below(100_000_000)
        full_W, last_M = module.scan_minima(hard, full_rows, 2495)
        assert last_M == 2495 and len(hard) == 719_781
        ranked = tuple(sorted(
            ((int(P), int(W)) for P, W in zip(hard, full_W)),
            key=lambda row: (-row[1], row[0]),
        )[:10])
        assert ranked == tuple((row[0], row[1]) for row in top)
        assert int((full_W >= 400).sum()) == 98
        assert int(((hard >= 10_000_000) & (hard < 100_000_000)).sum()) == 636_894
        for T, count in calibration_counts.items():
            assert int((full_W > T).sum()) == count
        assert int(((hard >= 10_000_000) & (full_W > 2495)).sum()) == 0

    print("record-stall anatomy (top rows,residue rows,A rows,spots,full,seconds) =",
          (len(top), len(residue_rows), len(records), 128, full_scan,
           perf_counter() - started))


print("\n== (bn) record-stall anatomy and honest A-window (§67) ==")
check_bn()


print("\nall checks passed")
