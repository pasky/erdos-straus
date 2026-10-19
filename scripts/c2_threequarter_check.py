#!/usr/bin/env python3
"""O278 / C2: from-scratch numerical sanity checks for paper/es-threequarter-note.tex.

Run:  PYTHONPATH=scripts timeout 600 uv run python scripts/c2_threequarter_check.py

Everything here is algebra / exact finite-probability checks on TOY parameters.
None of it is evidence in the asymptotic regime of the note (H=K^10, z=x^{1/6},
K=X^kappa), which is computationally unreachable.  Memory is capped at 2 GB.
"""
import math
import random
import resource
import sys
from fractions import Fraction
from itertools import combinations

import numpy as np
from sympy import factorint, isprime, primerange, totient, divisors

resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
random.seed(278)
FAIL = []


def check(name, ok, info=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {info}")
    if not ok:
        FAIL.append(name)


def omega(n):
    return len(factorint(n))


def phi(n):
    return int(totient(n))


# ---------------------------------------------------------------- A. identity
def check_identity(trials=400):
    ok = True
    for _ in range(trials):
        k = 4 * random.randint(0, 50) + 1
        while True:
            ell = random.choice(list(primerange(3, 5000)))
            if (k * ell) % 4 == 3:
                break
        A = (k * ell + 1) // 4
        ds = divisors(A)
        u = random.choice(ds)
        v = random.choice(divisors(A // u))
        w = A // (u * v)
        M = k * ell
        r = (-u * pow(v, -1, M)) % M
        for n in (r if r else M, r + M, r + 7 * M):
            if n <= 0:
                continue
            s = (n * v + u) // M
            if (n * v + u) % M or s <= 0:
                ok = False
                continue
            if Fraction(4, n) != Fraction(1, s * u * w) + Fraction(1, n * s * v * w) + Fraction(1, n * u * v * w):
                ok = False
    check("A identity 4/n = 1/(suw)+1/(nsvw)+1/(nuvw)", ok, f"({trials} random atoms)")


# ------------------------------------------------- B. distinctness at fixed ell
def toy_atoms(Klist, H, ell_lo, ell_hi, z_of):
    """atoms (k, ell, u, v, residue mod k*ell) with the note's conditions (no omega cutoff)."""
    atoms = []
    for ell in primerange(ell_lo, ell_hi + 1):
        z = z_of(ell)
        for k in Klist:
            if (k * ell) % 4 != 3:
                continue
            A = (k * ell + 1) // 4
            for u in divisors(A):
                if not (H < u <= z):
                    continue
                for v in divisors(A // u):
                    if not (H < v <= z) or math.gcd(u, v) != 1 or math.gcd(u * v, k) != 1:
                        continue
                    M = k * ell
                    atoms.append((k, ell, u, v, (-u * pow(v, -1, M)) % M))
    return atoms


def check_distinct():
    K = 13
    Klist = [k for k in range(1, K + 1) if k % 4 == 1]
    H = 2  # 4H^2 = 16 > K
    # block (x,2x] with z^2 < ell: take z = floor(sqrt(x))
    bad = 0
    total = 0
    for x in (400, 1000, 3000):
        atoms = toy_atoms(Klist, H, x + 1, 2 * x, lambda ell, x=x: math.isqrt(x))
        byell = {}
        for (k, ell, u, v, r) in atoms:
            byell.setdefault(ell, []).append(r % ell)
        for ell, rs in byell.items():
            total += len(rs)
            bad += len(rs) - len(set(rs))
    check("B same-ell projections distinct across all multipliers", bad == 0 and total > 0,
          f"({total} atoms, {bad} collisions)")
    # negative control: drop 4H^2 > K (H=0 allows u=1 or v=1) -> collisions expected to appear
    atoms = toy_atoms(list(range(1, 200, 4)), 0, 1001, 2000, lambda ell: math.isqrt(1000))
    byell = {}
    for (k, ell, u, v, r) in atoms:
        byell.setdefault(ell, []).append(r % ell)
    coll = sum(len(rs) - len(set(rs)) for rs in byell.values())
    check("B' control: without 4H^2>K collisions do occur", coll > 0, f"({coll} collisions)")


# ------------------------------------- C. exact CRT model: void & factorial moments
def check_crt_model():
    Klist = [1, 5, 9]
    L = 45
    y_primes = [2, 3]  # selector P_y = 6
    H = 1
    ells = [p for p in primerange(60, 140) if p % 4 == 3]
    atoms = toy_atoms(Klist, H, 60, 140, lambda ell: 7)  # z=7, z^2=49<ell
    # keep three primes with the most atoms (moderate modulus)
    cnt = {}
    for a in atoms:
        cnt[a[1]] = cnt.get(a[1], 0) + 1
    chosen = sorted(sorted(cnt, key=lambda e: -cnt[e])[:3])
    atoms = [a for a in atoms if a[1] in chosen]
    Msmall = 90  # lcm(L, P_y)
    M = Msmall * math.prod(chosen)
    n = np.arange(M, dtype=np.int64)
    Hn = np.zeros(M, dtype=np.int16)
    for (k, ell, u, v, r) in atoms:
        Hn += (n % (k * ell) == r)
    S = (np.gcd(n, 6) == 1)
    c = n % L
    ok_void = ok_mom = True
    maxdev = 0.0
    for cc in range(L):
        mask = S & (c == cc)
        if not mask.any():
            continue
        h = Hn[mask].astype(np.int64)
        # fibre probabilities
        p = []
        for ell in chosen:
            f = len({r % ell for (k, e, u, v, r) in atoms if e == ell and (u + cc * v) % k == 0})
            p.append(f / ell)
        void_exact = np.mean(h == 0)
        void_formula = math.prod(1 - q for q in p)
        maxdev = max(maxdev, abs(void_exact - void_formula))
        if abs(void_exact - void_formula) > 1e-12:
            ok_void = False
        for m in range(1, 5):
            ff = np.ones_like(h)
            for i in range(m):
                ff = ff * (h - i)
            em = sum(math.prod(s) for s in combinations(p, m)) if m <= len(p) else 0.0
            if abs(ff.mean() - math.factorial(m) * em) > 1e-9 or ff.mean() > sum(p) ** m + 1e-12:
                ok_mom = False
    check("C fibre void P(H=0|c,S)=prod(1-f_c/ell)", ok_void, f"(|A|={len(atoms)}, M={M}, maxdev={maxdev:.1e})")
    check("C fibre factorial moments = m! e_m(p) <= mu_c^m", ok_mom, "(m<=4)")
    return atoms, chosen, Hn, S, n


# --------------------------------------------- D. Bonferroni even majorant
def check_bonferroni():
    ok = True
    for r in range(0, 31, 2):
        for h in range(0, 120):
            Q = sum((-1) ** j * math.comb(h, j) for j in range(r + 1))
            if h == 0:
                ok &= Q == 1
            else:
                ok &= Q == math.comb(h - 1, r) and Q >= 0
            ok &= (1 if h == 0 else 0) <= Q <= (1 if h == 0 else 0) + math.comb(h, r + 1)
    check("D even Bonferroni: Q_r(h)=C(h-1,r), 1_{h=0}<=Q_r<=1_{h=0}+C(h,r+1)", ok)


# ------------------------------------- E. exact integer transfer with ledger
def count_class(N, a, q):
    """#{1<=n<=N : n = a (mod q)} computed independently of N/q."""
    a %= q
    first = a if a else q
    return 0 if first > N else (N - first) // q + 1

def check_transfer(atoms, chosen):
    r = 2
    y_primes = [2, 3]
    # direct sum over n <= N, and expansion N*E + error
    for N in (10**4, 123457):
        nn = np.arange(1, N + 1, dtype=np.int64)
        Hn = np.zeros(N, dtype=np.int64)
        for (k, ell, u, v, res) in atoms:
            Hn += (nn % (k * ell) == res)
        Q = sum((-1) ** j * np.vectorize(lambda h, j=j: math.comb(int(h), j))(Hn) for j in range(r + 1))
        S = (np.gcd(nn, 6) == 1)
        direct = int((S * Q).sum())
        # expansion: sum over d|6, subsets B of size <= r; exact count floor and expectation
        exp_sum = Fraction(0)
        cnt_sum = 0
        Tabs = 0
        for d in (1, 2, 3, 6):
            mu = (-1) ** len(factorint(d))
            for j in range(r + 1):
                for B in combinations(atoms, j):
                    Tabs += 1
                    # CRT combine
                    mod, res, okc = d, 0, True
                    for (k, ell, u, v, rr) in B:
                        m2 = k * ell
                        g = math.gcd(mod, m2)
                        if (rr - res) % g:
                            okc = False
                            break
                        # solve x = res (mod), x = rr (m2)
                        l = mod // g * m2
                        t = ((rr - res) // g * pow(mod // g, -1, m2 // g)) % (m2 // g) if m2 // g > 1 else 0
                        res = (res + mod * t) % l
                        mod = l
                    if not okc:
                        continue
                    coef = (-1) ** j * mu
                    exp_sum += Fraction(coef, mod)
                    cnt_sum += coef * count_class(N, res, mod)
        # count of 1<=n<=N with n = res mod q: handled above
        err = cnt_sum - N * exp_sum
        check(f"E exact expansion count == direct sum (N={N})", cnt_sum == direct, f"({direct})")
        check(f"E |sum - N E nu| <= T_abs (N={N})", abs(err) <= Tabs, f"(err={float(err):.2f}, T_abs={Tabs})")


# ------------------------------------- F. lattice sums (toy H, z)
def check_lattice():
    H, z = 30, 2500
    Lam = math.log(z / H)
    lo_ratio, up_ratio = [], []
    us = np.arange(H + 1, z + 1, dtype=np.int64)
    phis = np.array([phi(int(u)) for u in us], dtype=np.float64)
    for k in (1, 5, 9, 21, 45, 77):
        for c in [cc for cc in range(k) if math.gcd(cc, k) == 1][:3] if k > 1 else [0]:
            s1 = s2 = 0.0
            for i, v in enumerate(us):
                v = int(v)
                if math.gcd(v, k) != 1:
                    continue
                sel = ((us + c * v) % k == 0) & (np.gcd(us, v) == 1)
                s1 += (1.0 / us[sel]).sum() / v
                s2 += (1.0 / phis[sel]).sum() / phis[i]
            base = phi(k) / k**2 * Lam**2
            lo_ratio.append(s1 / base)
            up_ratio.append(s2 / base)
    check("F lattice lower ratio >= 1/4 (toy H=30,z=2500)", min(lo_ratio) >= 0.25,
          f"(min {min(lo_ratio):.3f}, max {max(lo_ratio):.3f})")
    check("F lattice upper ratio bounded (toy)", max(up_ratio) < 10, f"(max {max(up_ratio):.3f})")


# ------------------------------------- G. h(K), removal bound, pair-lcm sum
def check_h():
    Kmax = 20000
    ph = [0] * (Kmax + 1)
    for k in range(1, Kmax + 1):
        ph[k] = k
    for p in primerange(2, Kmax + 1):
        for m in range(p, Kmax + 1, p):
            ph[m] -= ph[m] // p
    diffs = []
    s = 0.0
    for k in range(1, Kmax + 1):
        if k % 4 == 1:
            s += ph[k] / k**2
        if k in (100, 1000, 5000, 20000):
            diffs.append(s - 2 / math.pi**2 * math.log(k))
    check("G h(K)-(2/pi^2)log K bounded", max(map(abs, diffs)) < 2, f"({[round(d, 4) for d in diffs]})")
    K = 5000
    ok = True
    for p in (2, 3, 5, 7, 31, 101, 997):
        lhs = sum(ph[k] / k**2 for k in range(p, K + 1, p))
        ok &= lhs <= (1 + math.log(K)) / p
    check("G removal bound sum_{p|k} phi(k)/k^2 <= (1+log K)/p", ok)
    rat = []
    for K in (50, 200, 800):
        tot = 0.0
        for k1 in range(1, K + 1):
            for k2 in range(1, K + 1):
                g = math.gcd(k1, k2)
                l = k1 * k2 // g
                # phi([a,b]) = phi(a)phi(b)/phi((a,b)); complete sum, no truncation
                tot += ph[k1] * ph[k2] / ph[g] / l**2
        rat.append(tot / (1 + math.log(K)) ** 3)
    check("G sum phi([k,k'])/[k,k']^2 / (1+log K)^3 bounded", max(rat) < 1, f"({[round(r, 4) for r in rat]})")


# ------------------------------------- K/L. local factors and phi(4uv)
def check_local():
    lo, hi = 10.0, 0.0
    for d in range(1, 30001):
        f = factorint(d)
        a = math.exp(-sum(2 / (p - 1) for p in f))
        b = (phi(d) / d) ** 2
        lo, hi = min(lo, a / b), max(hi, a / b)
    check("K exp(-sum 2/(p-1)) ≍ (phi(d)/d)^2", 0.1 < lo and hi <= 1.0 + 1e-12, f"(ratio in [{lo:.3f},{hi:.3f}])")
    ok = True
    for _ in range(5000):
        u, v = random.randint(1, 10**5), random.randint(1, 10**5)
        if math.gcd(u, v) == 1:
            ok &= phi(4 * u * v) >= 2 * phi(u) * phi(v)
    check("L phi(4uv) >= 2 phi(u)phi(v) for coprime u,v", ok)


# ------------------------------------- M. identity-class supply R(M)
def check_supply():
    ok = True
    for M in range(3, 1600, 4):
        A = (M + 1) // 4
        cls = set()
        for u in divisors(A):
            for v in divisors(A // u):
                cls.add((-u * pow(v, -1, M)) % M if math.gcd(v, M) == 1 else None)
        cls.discard(None)
        R = {(-4 * D) % M for D in divisors(A * A)}
        t = len(divisors(A * A))
        ok &= cls == R and (t - 1) / 2 <= len(R) <= t
    check("M identity classes mod M = {-4D : D | A^2}, (tau-1)/2<=F<=tau", ok, "(M<1600)")


# ------------------------------------- N. weighted second moment (toy)
def sieve_phi_omega(n):
    ph = list(range(n + 1))
    om = [0] * (n + 1)
    for p in range(2, n + 1):
        if ph[p] == p:
            for m in range(p, n + 1, p):
                ph[m] -= ph[m] // p
                om[m] += 1
    return ph, om


def check_wsecond():
    ph, om = sieve_phi_omega(1000)
    rat = []
    for (K, H, z) in ((9, 3, 400), (21, 5, 700), (45, 7, 900)):
        J = [k for k in range(1, K + 1) if k % 4 == 1]
        L = math.lcm(*J)
        c = 2 if math.gcd(2, L) == 1 else 1
        tot = 0.0
        for u in range(H + 1, z + 1):
            for v in range(H + 1, z + 1):
                if math.gcd(u, v) != 1:
                    continue
                rr = sum(1 for k in J if (u + c * v) % k == 0)
                if rr:
                    # coprime u,v: omega(uv)=omega(u)+omega(v); phi(4uv)=phi(4)phi(u)phi(v) unless 2|uv
                    p4 = 2 * ph[u] * ph[v] * (2 if (u * v) % 2 == 0 else 1)
                    tot += 2 ** (om[u] + om[v]) * rr * rr / p4
        rat.append(tot / (math.log(z) ** 4 * (1 + math.log(K)) ** 3))
    check("N weighted 2nd moment / (log z)^4(1+log K)^3 bounded (toy)", max(rat) < 1, f"({[round(r, 4) for r in rat]})")


if __name__ == "__main__":
    check_identity()
    check_distinct()
    atoms, chosen, *_ = check_crt_model()
    check_bonferroni()
    check_transfer(atoms[:12], chosen)
    check_lattice()
    check_h()
    check_local()
    check_supply()
    check_wsecond()
    print("ALL PASS" if not FAIL else f"FAILURES: {FAIL}")
    sys.exit(1 if FAIL else 0)
