"""Blind-audit sanity checks for paper/es-threequarter-note.tex (task a1).

Every check here tests an exactly checkable identity or inequality from the
note on toy parameters.  None of them tests the asymptotic regime
(H = K^10, z = x^{1/6}, X huge), which is far beyond computation; they are
sanity checks of the algebra/probability, not evidence for the theorem.

Run:  PYTHONPATH=scripts uv run python scripts/es34_blind_audit_checks.py
"""
from __future__ import annotations

import itertools
import math
import random
from fractions import Fraction
from math import comb, gcd

from sympy import factorint, primerange, totient, isprime

OK = True


def check(cond: bool, msg: str) -> None:
    global OK
    print(("PASS " if cond else "FAIL ") + msg)
    OK &= bool(cond)


def omega(n: int) -> int:
    return len(factorint(n))


def lcm(*a: int) -> int:
    r = 1
    for x in a:
        r = r * x // gcd(r, x)
    return r


# 1. Lemma 8.1 (even Bonferroni majorant)
def bonferroni() -> None:
    bad = 0
    for r in range(0, 31, 2):
        for h in range(0, 120):
            Q = sum((-1) ** j * comb(h, j) for j in range(r + 1))
            want = 1 if h == 0 else comb(h - 1, r)
            if Q != want or not ((1 if h == 0 else 0) <= Q <= (1 if h == 0 else 0) + comb(h, r + 1)):
                bad += 1
    check(bad == 0, "Lemma 8.1: Q_r(h)=C(h-1,r), 1_{h=0}<=Q_r<=1_{h=0}+C(h,r+1) (r<=30 even, h<120)")


# 2. Factorial moments of independent Bernoulli sums: E(H)_m = m! e_m(p) <= (sum p)^m,
#    and P(H=0)=prod(1-p) <= exp(-sum p).
def bernoulli_moments() -> None:
    rng = random.Random(1)
    worst = 0.0
    for _ in range(200):
        n = rng.randint(1, 12)
        p = [Fraction(rng.randint(0, 50), 100) for _ in range(n)]
        # exact distribution of H
        dist = [Fraction(1)]
        for pi in p:
            new = [Fraction(0)] * (len(dist) + 1)
            for h, w in enumerate(dist):
                new[h] += w * (1 - pi)
                new[h + 1] += w * pi
            dist = new
        mu = sum(p)
        for m in range(1, n + 2):
            fm = sum(w * math.perm(h, m) for h, w in enumerate(dist))
            em = sum(math.prod(c) for c in itertools.combinations(p, m)) if m <= n else 0
            assert fm == math.factorial(m) * em
            if mu > 0:
                worst = max(worst, float(fm / mu**m))
        assert float(dist[0]) <= math.exp(-float(mu)) + 1e-15
    check(worst <= 1.0, f"Thm 6.3 (cond.-indep. proof): E(H)_m = m! e_m <= mu^m (max ratio {worst:.3f})")


# 3. Toy atom family: distinctness mod ell, and exact CRT (H)_1,(H)_2 vs fibre formula,
#    plus Monte Carlo for P(H=0) vs averaged product formula.
def toy_family():
    # toy parameters: multipliers k = 1 mod 4, k <= K; primes ell in (x0, x1];
    # u,v in (Hs, z] with z^2 < ell (distinctness), 4 Hs^2 > K (k-uniqueness).
    K = 13
    Ks = [k for k in range(1, K + 1) if k % 4 == 1]
    LK = lcm(*Ks)
    Hs, z = 1, 12          # 4*Hs^2=4 is NOT > K: we enforce k-uniqueness check separately
    Hs = 2                 # 4*Hs^2 = 16 > 13
    ells = [p for p in primerange(200, 420)]
    atoms = []
    for k in Ks:
        for l in ells:
            if (k * l + 1) % 4:
                continue
            A = (k * l + 1) // 4
            for u in range(Hs + 1, z + 1):
                for v in range(Hs + 1, z + 1):
                    if gcd(u, v) != 1 or gcd(u * v, k) != 1:
                        continue
                    if (k * l + 1) % (4 * u * v):
                        continue
                    res = (-u * pow(v, -1, k * l)) % (k * l)
                    atoms.append((k, l, u, v, res))
    # distinctness of projections mod ell
    by_l = {}
    for (k, l, u, v, res) in atoms:
        by_l.setdefault(l, []).append(res % l)
    dup = sum(len(r) - len(set(r)) for r in by_l.values())
    check(dup == 0 and len(atoms) > 50,
          f"Lemma 2.2 distinctness: {len(atoms)} toy atoms, {len(by_l)} primes, 0 coincident projections mod ell")
    # identity check (Lemma 2.1) on each atom: smallest positive n in class is representable
    badid = 0
    for (k, l, u, v, res) in atoms[:400]:
        n = res if res > 0 else k * l
        s, rem = divmod(n * v + u, k * l)
        w = (k * l + 1) // (4 * u * v)
        if rem or Fraction(4, n) != Fraction(1, s * u * w) + Fraction(1, n * s * v * w) + Fraction(1, n * u * v * w):
            badid += 1
    check(badid == 0, "Lemma 2.1 identity holds on toy atoms")

    # exact E(H) and E(H)_2 by pair enumeration with CRT probabilities
    EH = sum(Fraction(1, k * l) for (k, l, u, v, r) in atoms)
    EH2 = Fraction(0)
    for a, b in itertools.permutations(atoms, 2):
        k1, l1, _, _, r1 = a
        k2, l2, _, _, r2 = b
        if l1 == l2:
            continue  # same ell, distinct atoms: incompatible (distinct residues mod ell)
        g = gcd(k1, k2)
        if r1 % g != r2 % g:
            continue
        EH2 += Fraction(1, lcm(k1, k2) * l1 * l2)
    # fibre formula: average over c mod LK
    fsum1 = Fraction(0)
    fsum2 = Fraction(0)
    fvoid = 0.0
    act = {}
    for (k, l, u, v, r) in atoms:
        act.setdefault((k, r % k), {}).setdefault(l, 0)
        act[(k, r % k)][l] += 1
    for c in range(LK):
        f = {}
        for k in Ks:
            d = act.get((k, c % k))
            if d:
                for l, m in d.items():
                    f[l] = f.get(l, 0) + m
        mus = [Fraction(m, l) for l, m in f.items()]
        s1 = sum(mus)
        s2 = s1 * s1 - sum(x * x for x in mus)
        fsum1 += s1
        fsum2 += s2
        fvoid += math.prod(1 - float(x) for x in mus)
    fsum1 /= LK
    fsum2 /= LK
    fvoid /= LK
    check(fsum1 == EH, f"CRT: E(H) exact = fibre average ({float(EH):.5f})")
    check(fsum2 == EH2, f"CRT: E(H)_2 exact pair sum = fibre average of sum_{{l!=l'}} ({float(EH2):.5f})")
    # Monte Carlo on n mod M
    rng = random.Random(7)
    M_ells = sorted(set(l for (_, l, _, _, _) in atoms))
    trials = 20000
    zero = 0
    for _ in range(trials):
        c = rng.randrange(LK)
        resl = {l: rng.randrange(l) for l in M_ells}
        h = 0
        for (k, l, u, v, r) in atoms:
            if c % k == r % k and resl[l] == r % l:
                h += 1
        zero += (h == 0)
    pz = zero / trials
    se = math.sqrt(pz * (1 - pz) / trials)
    check(abs(pz - fvoid) < 4 * se,
          f"CRT void: MC P(H=0)={pz:.4f} vs fibre product formula {fvoid:.4f} (4 s.e.={4*se:.4f})")


# 4. Lemma 3.2: h(K(K)) - (2/pi^2) log K bounded
def lemma_h():
    import numpy as np
    Kmax = 2_000_000
    phi = np.arange(Kmax + 1, dtype=np.float64)
    for p in primerange(2, Kmax + 1):
        phi[p::p] *= (1 - 1 / p)
    ks = np.arange(1, Kmax + 1, 4)
    terms = phi[ks] / ks.astype(np.float64) ** 2
    cs = np.cumsum(terms)
    devs = []
    for K in [10, 100, 1000, 10**4, 10**5, 10**6, 2 * 10**6]:
        idx = (K - 1) // 4
        devs.append(cs[idx] - 2 / math.pi**2 * math.log(K))
    check(max(abs(d) for d in devs) < 2 and abs(devs[-1] - devs[-2]) < 0.01,
          "Lemma 3.2: h(K(K)) - (2/pi^2)log K = " + ", ".join(f"{d:.4f}" for d in devs))
    # (3.11)/(hremove)
    worst = 0
    for p in [3, 5, 7, 11, 101]:
        K = 10**5
        s = sum(float(phi[k]) / k**2 for k in range(p, K + 1, p))
        worst = max(worst, s / ((1 + math.log(K)) / p))
    check(worst <= 1, f"(16) sum_{{p|k<=K}} phi(k)/k^2 <= (1+log K)/p: max ratio {worst:.3f}")


# 5. phi(4uv) >= 2 phi(u) phi(v), coprime u,v
def phi_ineq():
    bad = 0
    for u in range(1, 200):
        for v in range(1, 200):
            if gcd(u, v) == 1 and totient(4 * u * v) < 2 * totient(u) * totient(v):
                bad += 1
    check(bad == 0, "phi(4uv) >= 2 phi(u)phi(v) for coprime u,v < 200")


# 6. Prime-power relative-probability table (34): brute force on Z/p^E with unit selector
def pp_table():
    bad = 0
    for p in [2, 3, 5]:
        for e in range(1, 4):
            for f in range(0, 4):
                for small in [True, False]:  # p <= y (selector conditions n to be a unit mod p) or not
                    E = max(e, f) + 1
                    mod = p**E
                    space = [n for n in range(mod) if (not small or n % p)]
                    a = 1  # a unit residue
                    cond = [n for n in space if n % p**f == a % p**f]
                    hit = [n for n in cond if n % p**e == a % p**e]
                    prob = Fraction(len(hit), len(cond))
                    # formula: q_y local * p^{-e} * b_y local of g=p^{min(e,f)}
                    g = min(e, f)
                    q = Fraction(p, p - 1) if small else Fraction(1)
                    b = (p**g - p ** (g - 1) if g > 0 else 1) if small else p**g
                    form = q * Fraction(1, p**e) * b
                    if prob != form:
                        bad += 1
    check(bad == 0, "(34) prime-power relative probability table q_y(k)b_y(g)/k (p=2,3,5; e,f<=3)")


# 7. Lemma 6.2 Euler factor ratio (1+1/p)/(1+(p-1)/p^2) = 1+O(p^-2)
def euler_factor():
    worst = 0
    for p in primerange(3, 10**5):
        r = (1 + 1 / p) / (1 + (p - 1) / p**2)
        worst = max(worst, (r - 1) * p * p)
        # nonconstant part: sum_e (1-1/p)^2/p^e = (p-1)/p^2
        assert abs((1 - 1 / p) ** 2 / (p - 1) - (p - 1) / p**2) < 1e-15
    check(worst < 1.01, f"Lemma 6.2 local ratio = 1+O(p^-2): max p^2(ratio-1) = {worst:.4f}")


# 8. Residue class count in Lemma 6.1: units (u,v) mod q0 with -u/v = a mod g: phi(q0)^2/phi(g)
def class_count():
    bad = 0
    for q0 in range(2, 60):
        for g in [d for d in range(1, q0 + 1) if q0 % d == 0]:
            units = [x for x in range(q0) if gcd(x, q0) == 1]
            for a in [x for x in range(g) if gcd(x, g) == 1][:3]:
                cnt = sum(1 for u in units for v in units if (-u * pow(v, -1, q0) - a) % g == 0)
                if cnt * totient(g) != totient(q0) ** 2:
                    bad += 1
    check(bad == 0, "Lemma 6.1 unit-pair count phi(q0)^2/phi(g) (q0<60)")


# 9. Section 10: identity classes mod M are exactly -4D, D | A^2 (toy M)
def identity_classes():
    bad = 0
    for M in range(3, 3000, 4):
        A = (M + 1) // 4
        cls = set()
        for u in [d for d in range(1, A + 1) if A % d == 0]:
            for v in [d for d in range(1, A // u + 1) if (A // u) % d == 0]:
                cls.add((-u * pow(v, -1, M)) % M)
        D = set((-4 * d) % M for d in range(1, A * A + 1) if (A * A) % d == 0) if A < 200 else None
        if D is not None and cls != D:
            bad += 1
        tau = 1
        for e in factorint(A).values():
            tau *= 2 * e + 1
        if not ((tau - 1) / 2 <= len(cls) <= tau):
            bad += 1
    check(bad == 0, "Sec 10: identity classes = {-4D: D|A^2}, (tau(A^2)-1)/2 <= F(M) <= tau(A^2)")


# 10. Lemma 5.1 sum over pairs: sum_{k,k'<=K} phi([k,k'])/[k,k']^2 / (1+log K)^3 stays bounded
def pair_sum():
    out = []
    for K in [10, 50, 200, 800]:
        s = 0.0
        ph = [0] + [int(totient(n)) for n in range(1, K * K + 1)] if K <= 200 else None
        for k in range(1, K + 1):
            for kk in range(1, K + 1):
                d = k * kk // gcd(k, kk)
                s += (ph[d] if ph else float(totient(d))) / d**2 if K <= 200 else 1 / d  # upper bound for big K
        out.append(s / (1 + math.log(K)) ** 3)
    check(max(out) < 1.0, "Lemma 4.1/5.1 pair sum / (1+log K)^3: " + ", ".join(f"{x:.3f}" for x in out))


# 11. final optimisation: exponent bookkeeping (symbolic check of 3/4)
def optimisation():
    # log T_abs <= C_L t^4 must be <= L/2; saving c t^3. t = alpha L^{1/4}.
    import sympy as sp
    L, a, CL, c = sp.symbols("L alpha C_L c", positive=True)
    t = a * L ** sp.Rational(1, 4)
    cost = sp.simplify(CL * t**4 / L)
    saving = sp.simplify(c * t**3)
    check(cost == CL * a**4 and sp.simplify(saving / L ** sp.Rational(3, 4)) == c * a**3,
          "Optimisation: t=alpha L^{1/4} gives cost C_L alpha^4 L (<= L/2 for alpha small), saving c alpha^3 L^{3/4}")


if __name__ == "__main__":
    bonferroni()
    bernoulli_moments()
    toy_family()
    lemma_h()
    phi_ineq()
    pp_table()
    euler_factor()
    class_count()
    identity_classes()
    pair_sum()
    optimisation()
    print("ALL PASS" if OK else "SOME FAILURES")
