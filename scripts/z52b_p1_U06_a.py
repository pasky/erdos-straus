#!/usr/bin/env python3
"""z52b pass1 U06 — cheap first steps for items Z0769, Z2001, Z2944, Z3009.

Definitions (repo FRONTIER.md §2.1, divisor form):
  cert(C, p) := exists divisor d > 1 of 4Cp+1 with d = -1 (mod 4C).
  R(p) >= 1 whenever cert(C, p) for some C (Type II / (*) line).
Outputs go to data/z52b/pass1/U06/.
"""
import json, math, os, random, sys

OUT = "data/z52b/pass1/U06"
os.makedirs(OUT, exist_ok=True)

def sieve(N):
    s = bytearray([1]) * (N + 1)
    s[0] = s[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i * i :: i] = bytearray(len(s[i * i :: i]))
    return [i for i in range(N + 1) if s[i]]

SMALL = sieve(10 ** 4)

def factor(n):
    f = {}
    for p in SMALL:
        if p * p > n:
            break
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def divisors(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds

def cert(C, p):
    N = 4 * C * p + 1
    m = 4 * C
    return any(d > 1 and d % m == m - 1 for d in divisors(factor(N)))

def hard_primes(lo, hi):
    M = {1, 121, 169, 289, 361, 529}
    return [q for q in sieve(hi) if q >= lo and q % 840 in M]

# ---------- Z0769: t=1, t=2 word counts (exact identities) ----------
def words(n, t):
    """#{(u,v): u,v >= 2, t*u*v - u - v = n}"""
    c = 0
    for u in range(2, n + 3):
        # solve for v: v (t u - 1) = n + u
        den = t * u - 1
        if (n + u) % den == 0:
            v = (n + u) // den
            if v >= 2:
                c += 1
    return c

def tau(n):
    return len(divisors(factor(n)))

z0769_bad = []
for n in range(1, 400):
    if words(n, 1) != tau(n + 1):
        z0769_bad.append(("t=1", n, words(n, 1), tau(n + 1)))
    # t=2: (2u-1)(2v-1)=2n+1 with u,v>=2 => odd divisors a,b>=3 ; count ordered pairs
    m = 2 * n + 1
    cnt = sum(1 for a in divisors(factor(m)) if a >= 3 and m % a == 0 and (m // a) >= 3)
    if words(n, 2) != cnt:
        z0769_bad.append(("t=2", n, words(n, 2), cnt))
print("Z0769 mismatches (n<400):", len(z0769_bad), z0769_bad[:5])

# ---------- Z2001: greedy menu cover of primes in [X, 2X], menu items (u,C) ----------
def menu_items(p, Umax):
    """all (u,C), u<=Umax, with (4uC-1) | (p+u)"""
    out = []
    for u in range(1, Umax + 1):
        N = p + u
        if N < 3:
            continue
        for m in divisors(factor(N)):
            if m % (4 * u) == (4 * u - 1) % (4 * u) and m >= 4 * u - 1:
                C = (m + 1) // (4 * u)
                if C >= 1:
                    out.append((u, C))
    return out

def greedy_menu(X, Umax):
    primes = [q for q in sieve(2 * X) if q >= X and q % 24 == 1]
    cover = {}
    for p in primes:
        for it in set(menu_items(p, Umax)):
            cover.setdefault(it, set()).add(p)
    left = set(primes)
    menu = []
    while left:
        best = max(cover.items(), key=lambda kv: len(kv[1] & left))
        g = best[1] & left
        if not g:
            break
        menu.append((best[0], len(g)))
        left -= g
    return len(primes), menu, len(left)

z2001 = {}
for k in (3, 4, 5):
    X = 10 ** k
    npr, menu, unc = greedy_menu(X, Umax=400)
    z2001[k] = {"n_primes": npr, "menu_size": len(menu), "uncovered": unc,
                "first_items": menu[:8]}
    print("Z2001 k=%d primes=%d greedy menu=%d uncovered=%d" % (k, npr, len(menu), unc), menu[:6])

# ---------- Z2944: single-prime certificate count S1(p) ----------
def S1(p, qs):
    """#{q prime, q=3 mod 4, q != p: c=-(4p)^{-1} mod q, 4c | q+1, c>=1}"""
    cnt, least = 0, None
    for q in qs:
        if q == p or q % 4 != 3:
            continue
        c = (-pow(4 * p, -1, q)) % q
        if c >= 1 and (q + 1) % (4 * c) == 0:
            cnt += 1
            if least is None:
                least = q
    return cnt, least

QMAX = 200000
qs = [q for q in sieve(QMAX) if q > 3]
hp = hard_primes(5, 100000)
s1 = []
for p in hp:
    c, lq = S1(p, qs)
    s1.append((p, c, lq))
zeros = [p for p, c, _ in s1 if c == 0]
mean = sum(c for _, c, _ in s1) / len(s1)
print("Z2944 hard primes <=1e5:", len(s1), "S1=0 for", len(zeros), "mean S1", round(mean, 2),
      "max", max(c for _, c, _ in s1), "min", min(c for _, c, _ in s1))
json.dump({"QMAX": QMAX, "rows": s1}, open(f"{OUT}/s1_hard_1e5_Q2e5.json", "w"))

# ---------- Z3009: EGZ-style composite certificates ----------
random.seed(1)
P = [p for p in sieve(100000) if p % 4 == 1]
CS = list(range(1, 13))
cert_tab = {}
for p in P:
    if p % 840 not in {1, 121, 169, 289, 361, 529}:
        continue
    for C in set(CS) | {a * b for a in CS for b in CS}:
        cert_tab[(C, p)] = cert(C, p)
hp_count = len({p for (_, p) in cert_tab})
rows = []
for C1 in CS:
    for C2 in CS:
        if C2 < C1:
            continue
        C12 = C1 * C2
        n_both = n_both_c = n_c = n = 0
        for p in {p for (_, p) in cert_tab}:
            a, b = cert_tab[(C1, p)], cert_tab[(C2, p)]
            c12 = cert_tab[(C12, p)]
            n += 1
            n_c += c12
            if a and b:
                n_both += 1
                n_both_c += c12
        if n_both:
            rows.append({"C1": C1, "C2": C2, "P_c12": n_c / n, "P_c12_given_both": n_both_c / n_both,
                         "n_both": n_both})
print("Z3009 primes (hard, <=1e5):", hp_count)
for r in rows[:12]:
    print(" C1=%d C2=%d  P(cert C1C2)=%.3f  P(.|both)=%.3f  n_both=%d" %
          (r["C1"], r["C2"], r["P_c12"], r["P_c12_given_both"], r["n_both"]))
json.dump({"rows": rows, "n_primes": hp_count}, open(f"{OUT}/egz_composite_1e5.json", "w"), indent=0)
