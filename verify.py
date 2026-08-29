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


print("\nall checks passed")
