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

print("\nall checks passed")
