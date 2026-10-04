#!/usr/bin/env python3
"""Independent check of EXCEPTIONAL_TWIN4 Lemma 2.3 (reviewer's code; shares nothing
with scripts/twin4_rough_bt.py).

Lemma 2.3: for s>=1, w>=2, q>=1, (b,q)=1, x >= q*2^(s+1), Y=x/q, Z=Y^(1/(s+1)),
H = sum_{w<p<=Z} 1/(p-1):
  sum_{x<R<=2x, R=b (q), Omega(R)<=s, P^-(R)>w} 1/R <= 3(s+1) sum_{i<s} H^i / (phi(q) log Y).

Different algorithms: Omega by adding 1 at every multiple of every prime power;
least prime factor by writing primes in decreasing order; phi by trial division.
Stress regime: x at the threshold q*2^(s+1) (smallest Y, where log Y is smallest),
q with many small primes (phi(q)/q small), small w, s up to 5, all units b
(or 300 random ones). Also reports, per s, the worst ratio at the threshold
and the worst ratio of lhs against the *s-free* quantity 1/(phi(q) log Y)
(to see how much the constant 3(s+1)ΣH^i is needed).

Usage: uv run --with numpy python reviews/exceptional-twin4-check-lemma23.py [N] [seed]
"""
import sys, math, random
import numpy as np

N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 4_000_000
seed = int(sys.argv[2]) if len(sys.argv) > 2 else 7
random.seed(seed)

isp = np.ones(N + 1, dtype=bool); isp[:2] = False
for p in range(2, int(N ** 0.5) + 1):
    if isp[p]:
        isp[p * p::p] = False
primes = np.nonzero(isp)[0]

Om = np.zeros(N + 1, dtype=np.int16)
for p in primes:
    pe = int(p)
    while pe <= N:
        Om[pe::pe] += 1
        pe *= int(p)
lpf = np.zeros(N + 1, dtype=np.int64)
for p in primes[::-1]:
    lpf[int(p)::int(p)] = p


def phi(n):
    r, m, d = n, n, 2
    while d * d <= m:
        if m % d == 0:
            r -= r // d
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        r -= r // m
    return r


pr_list = [int(p) for p in primes[:20000]]
inv_pm1 = np.array([1.0 / (p - 1) for p in pr_list])
pr_arr = np.array(pr_list)


def Hsum(w, Z):
    m = (pr_arr > w) & (pr_arr <= Z)
    return float(inv_pm1[m].sum())


qs = [1, 2, 3, 4, 6, 12, 30, 60, 210, 420, 2310, 4620, 30030, 7, 101, 997, 9973, 65537]
qs += random.sample(range(5, 100000), 12)
ws = [2, 3, 7, 50, 300, 2000]
worst = {}
worst_thr = {}
cases = 0
for s in range(1, 6):
    for w in ws:
        ok = (lpf > w) & (Om >= 1) & (Om <= s)
        for q in qs:
            x0 = q * 2 ** (s + 1)
            if 2 * x0 > N:
                continue
            xs = sorted(set([x0, x0 + 1, int(x0 * 1.5)] +
                            [int(x0 * 4 ** k) for k in range(1, 12) if 2 * x0 * 4 ** k <= N]))
            xs = [x for x in xs if 2 * x <= N]
            ph = phi(q)
            units = [b for b in range(q) if math.gcd(b, q) == 1]
            if len(units) > 300:
                units = random.sample(units, 300)
            for x in xs:
                Y = x / q
                Z = Y ** (1.0 / (s + 1))
                H = Hsum(w, Z)
                bound = 3 * (s + 1) * sum(H ** i for i in range(s)) / (ph * math.log(Y))
                for b in units:
                    first = x + 1 + ((b - (x + 1)) % q)
                    R = np.arange(first, 2 * x + 1, q, dtype=np.int64)
                    R = R[ok[R]]
                    lhs = float((1.0 / R).sum()) if R.size else 0.0
                    rat = lhs / bound
                    cases += 1
                    key = s
                    if rat > worst.get(key, (0,))[0]:
                        worst[key] = (rat, w, q, x, b, lhs * ph * math.log(Y))
                    if x == x0 and rat > worst_thr.get(key, (0,))[0]:
                        worst_thr[key] = (rat, w, q, x, b)
    print(f"s={s}: worst ratio {worst.get(s)}  at threshold {worst_thr.get(s)}  (cases so far {cases})", flush=True)

W = max(v[0] for v in worst.values())
print(f"TOTAL cases {cases}; worst lhs/bound = {W:.4f}  (Lemma 2.3 claims <= 1)")
