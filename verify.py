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

print("\nall checks passed")
