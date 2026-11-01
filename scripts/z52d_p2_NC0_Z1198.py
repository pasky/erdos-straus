#!/usr/bin/env python3
"""Z1198: meet-in-the-middle divisor selection, with valuation/gcd strata for non-units.

Problem: given N = prod q^a, modulus m, target t: count divisors d | N with d = t (mod m).
MITM: split the prime powers of N into two groups; A = divisors of group 1, B = divisors of
group 2 (every divisor of N is uniquely a*b). Need a*b = t (mod m).
For each b, g = gcd(b, m): solvable iff g | t, and then a = (t/g) * (b/g)^{-1} (mod m/g),
where gcd(b/g, m/g) = 1 so the inverse exists. Non-units b are handled by keying A on residues
mod m/g (one table per distinct g), i.e. the valuation-style stratum of b.
Checked against direct enumeration of all divisors (exact counts), and on the ES instance
  N = M^2, M = p x, m = r = 4x - p, t = -M (mod r) (counts = number of solutions e).
"""
import sys, time, json, random, math
from functools import reduce

def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def pp_list(N):
    return [(q, a) for q, a in factor(N).items()]

def divisors_from_pp(pps):
    ds = [1]
    for q, a in pps:
        ds = [d * q ** i for d in ds for i in range(a + 1)]
    return ds

def direct_count(N, m, t):
    return sum(1 for d in divisors_from_pp(pp_list(N)) if (d - t) % m == 0)

def mitm_count(N, m, t):
    pps = pp_list(N)
    # balance: greedy split by divisor count
    pps_sorted = sorted(pps, key=lambda qa: -(qa[1] + 1))
    g1, g2, c1, c2 = [], [], 1, 1
    for qa in pps_sorted:
        if c1 <= c2:
            g1.append(qa); c1 *= qa[1] + 1
        else:
            g2.append(qa); c2 *= qa[1] + 1
    A = [d % m for d in divisors_from_pp(g1)]
    B = divisors_from_pp(g2)
    tables = {}          # modulus m/g -> histogram of a mod (m/g)
    work = len(A) + len(B)
    total = 0
    for b in B:
        bm = b % m
        g = math.gcd(bm, m)          # g = gcd(b, m); gcd(0, m) = m
        if t % g != 0:
            continue                 # a*b = t (mod m) forces g | t
        mod = m // g
        if mod not in tables:
            tab = {}
            for a in A:
                tab[a % mod] = tab.get(a % mod, 0) + 1
            tables[mod] = tab
            work += len(A)
        # gcd(bm/g, m/g) = 1, so the inverse exists:  a = (t/g) * (bm/g)^{-1}  (mod m/g)
        if mod == 1:
            a0 = 0
        else:
            a0 = ((t // g) % mod) * pow((bm // g) % mod, -1, mod) % mod
        total += tables[mod].get(a0, 0)
    return total, work, len(tables), len(A), len(B)

def test_random(trials=300, Nmax=10 ** 6, mmax=1000, seed=1):
    rnd = random.Random(seed)
    bad = 0
    for _ in range(trials):
        N = rnd.randint(2, Nmax); m = rnd.randint(2, mmax); t = rnd.randint(0, m - 1)
        c_d = direct_count(N, m, t)
        c_m, *_ = mitm_count(N, m, t)
        if c_d != c_m:
            bad += 1
    return trials, bad

def es_instances(pmax=1000, K=6):
    out = []
    ps = [p for p in range(5, pmax) if p % 4 == 1 and all(p % d for d in range(2, int(p ** 0.5) + 1))]
    rows = []
    for p in ps:
        x0 = -(-p // 4)
        for x in range(x0, x0 + K):
            r = 4 * x - p; M = p * x; N = M * M
            t = (-M) % r
            c_d = direct_count(N, r, t)
            c_m, work, ntab, la, lb = mitm_count(N, r, t)
            tau = 1
            for q, a in pp_list(N):
                tau *= 2 * a + 1
            rows.append((p, x, r, c_d, c_m, tau, work, la, lb))
    return rows

if __name__ == "__main__":
    t0 = time.time()
    trials, bad = test_random()
    print(f"random N<=1e6, m<=1000: trials={trials} mismatches={bad}")
    rows = es_instances(int(sys.argv[1]) if len(sys.argv) > 1 else 1000, 6)
    mism = sum(1 for r in rows if r[3] != r[4])
    print(f"ES instances (p<=1000, 6 windows): n={len(rows)} count mismatches={mism}")
    print("sum tau(M^2)=", sum(r[5] for r in rows), " sum MITM work=", sum(r[6] for r in rows),
          " max tau=", max(r[5] for r in rows), " max MITM work=", max(r[6] for r in rows))
    print("max |A|,|B| =", max(max(r[7], r[8]) for r in rows), "seconds", round(time.time() - t0, 2))
    solvable = sum(1 for r in rows if r[3] > 0)
    print("windows with >=1 divisor solution:", solvable)
    json.dump({"random_trials": trials, "random_mismatches": bad, "n_es": len(rows), "es_mismatch": mism,
               "rows": rows}, open("data/z52b/pass2/NC0/sub/Z1198_mitm.json", "w"))
