# z51 dbreak: controls for the 4Z-line prime family.
# For each control n (n ≡ 1 mod 8 unless noted), list all events (l, e): l prime, l ≡ -1 (mod 4e), l | n + 4e,
# computed independently of sieve4.c via the e-view (factor n + 4e for e <= (n+3)/8; Lemma 1.1(d) gives l <= (n+4e)/3).
# Cross-check: the t-view (l | t n + 1, l ≡ -1 mod 4t) must give the same set (Lemma 1.1(a),(c)).
# Reports R(n) = #events, R_top(n) = #events with l > sqrt(2n), min event prime.
import math, sys, json
import numpy as np

def spf_sieve(M):
    spf = np.zeros(M + 1, dtype=np.int64)
    spf[1] = 1
    for i in range(2, int(M ** 0.5) + 1):
        if spf[i] == 0:
            spf[i] = i
            blk = spf[i * i::i]
            blk[blk == 0] = i
            spf[i * i::i] = blk
    z = np.nonzero(spf == 0)[0]
    spf[z] = z
    return spf

def factor(x, spf):
    fs = set()
    while x > 1:
        p = int(spf[x]); fs.add(p)
        while x % p == 0:
            x //= p
    return fs

def events_eview(n, spf):
    ev = set()
    for e in range(1, (n + 3) // 8 + 1):
        for l in factor(n + 4 * e, spf):
            if (l + 1) % (4 * e) == 0:
                ev.add((l, e))
    return ev

def is_prime(x):
    if x < 2: return False
    if x % 2 == 0: return x == 2
    r = int(math.isqrt(x))
    f = 3
    while f <= r:
        if x % f == 0: return False
        f += 2
    return True

def events_tview(n):
    # l | t n + 1 with l ≡ -1 (mod 4t): l > t, l <= (n+4e)/3 bounds t <= (n+3)/8 as well (t = (l+1)/(4e) <= (l+1)/4)
    ev = set()
    # enumerate via divisors: for each t, the l are prime factors of t n + 1 that are ≡ -1 mod 4t; t ranges up to (l+1)/4 <= (n+3)/8... use bound t <= n
    # cheap version for small n only
    for t in range(1, n // 2 + 2):
        x = t * n + 1
        y = x; p = 2
        fs = set()
        while p * p <= y:
            if y % p == 0:
                fs.add(p)
                while y % p == 0: y //= p
            p += 1 if p == 2 else 2
        if y > 1: fs.add(y)
        for l in fs:
            if (l + 1) % (4 * t) == 0 and l <= (n + 4 * ((l + 1) // (4 * t))):
                ev.add((l, (l + 1) // (4 * t)))
    return ev

hard = [193, 409, 577, 2521, 3361, 5569, 9601, 66529, 8813281]
rzeros = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281]
num8 = [17, 241]
squares = [x * x for x in (3, 5, 7, 9, 11, 101, 999)]
nonsq_U_fail = [105, 2961, 3985, 25305, 111969, 978145]
ctrl = sorted(set(hard + rzeros + num8 + squares + nonsq_U_fail))
M = 2 * max(ctrl) + 10
spf = spf_sieve(M)
out = {}
for n in ctrl:
    ev = events_eview(n, spf)
    top = [l for (l, e) in ev if l * l > 2 * n]
    rec = {"n": n, "mod8": n % 8, "square": int(math.isqrt(n)) ** 2 == n, "R": len(ev), "R_top": len(top),
           "min_l": min((l for l, e in ev), default=None), "in_A": len(ev) == 0}
    if n < 3000:
        evt = events_tview(n)
        rec["tview_agrees"] = (evt == ev)
    out[n] = rec
    print(rec)
json.dump(out, open("data/z51_dbreak/controls.json", "w"), indent=1)
