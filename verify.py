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
from math import gcd, lcm, log, exp, ceil, prod
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


# ---------------------------------------------------------------- (z)
def check_z():
    """Finite companions for the §27 large-R conditioning audit."""
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

    # Exact finite replay of Theorem 27.1's hybrid certificate.  Every
    # low-fiber event has a certifying 3 mod 4 prime coordinate, and every
    # prime-modulus intrinsic class is explicitly in G_p.
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

    # Arithmetic replay of the 2.4-billion-sample table.  The raw sampling
    # run is intentionally not repeated by the default verifier.
    fit_X = np.array([50, 100, 200, 400, 800, 1600, 3200, 6400.])
    fit_survivors = np.array([
        126_504_179, 42_472_324, 10_805_883, 2_315_665,
        362_699, 42_008, 3_854, 274,
    ], dtype=float)
    sample_count = 2_400_000_000
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
    print("Theorem 27.1 finite certificate: %d low events and %d prime "
          "classes; primorial exclusions=%d" %
          (low_event_checks, prime_class_checks, quarantine_checks))
    print("§27 sample replay: X=6400 has 274/2.4e9 survivors, Wilson "
          "[1.01425e-7,1.28509e-7]")
    print("§27 fits (L^2logL, subset RMSE, correlation): "
          "%.5f, %.5f, %.6f" % (rmses[3], rmses[4], correlation))


print("\n== (z) large-R conditioning and H_DC (§27) ==")
check_z()

print("\nall checks passed")
