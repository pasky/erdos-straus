"""R94 review A (from scratch): Lemma 1.1 identity, Lemma 1.3 distinctness, Lemma 2.1 numerics.
Usage: PYTHONPATH=scripts uv run python scripts/review_emnA_lemmas.py [Kmax]
Exit code 1 on any failure."""
import sys, random, math
from fractions import Fraction
from math import gcd

fails = 0

# ---- Lemma 1.1: exhaustive small search over (m,k,l,u,v,n), l arbitrary (not only prime)
cnt = 0
for m in range(4, 25):
    for k in range(1, 30):
        if gcd(k, m) != 1:
            continue
        for l in range(1, 60):
            N = k * l + 1
            if N % m:
                continue
            A = N // m
            for u in range(1, A + 1):
                if A % u:
                    continue
                for v in range(1, A // u + 1):
                    if (A // u) % v:
                        continue
                    w = A // (u * v)
                    kl = k * l
                    if gcd(v, kl) != 1:
                        continue
                    # first few n in class -u v^{-1} mod kl
                    n0 = (-u * pow(v, -1, kl)) % kl if kl > 1 else 0
                    for n in [n0 + j * kl for j in range(4)]:
                        if n < 1:
                            continue
                        s, r = divmod(n * v + u, kl)
                        assert r == 0
                        lhs = Fraction(m, n)
                        rhs = Fraction(1, s * u * w) + Fraction(1, n * s * v * w) + Fraction(1, n * u * v * w)
                        cnt += 1
                        if lhs != rhs:
                            fails += 1
print(f"Lemma1.1 identity: {cnt} instances, fails so far {fails}")

# ---- Lemma 1.3 distinct projections at fixed prime l (u,v <= z with z^2 < l, muv > K)
def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** .5) + 1):
        if s[i]:
            s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]

coll = 0; atoms = 0
for m in (4, 5, 6, 8, 9, 12, 30):
    K = 7
    for l in primes_upto(5000)[-120:]:
        z = int(math.isqrt(l - 1))
        while z * z >= l: z -= 1
        seen = {}
        for k in range(1, K + 1):
            if gcd(k, m) != 1: continue
            N = k * l + 1
            if N % m: continue
            A = N // m
            for u in range(2, z + 1):
                if A % u: continue
                for v in range(2, z + 1):
                    if (A // u) % v or gcd(u, v) != 1 or gcd(u * v, k) != 1 or m * u * v <= K:
                        continue
                    proj = (-u * pow(v, -1, l)) % l
                    atoms += 1
                    if proj in seen and seen[proj] != (k, u, v):
                        coll += 1
                    seen[proj] = (k, u, v)
fails += coll
print(f"Lemma1.3 distinct projections: {atoms} atoms, {coll} collisions")

# ---- Lemma 2.1 numerics
Kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
def phi(n):
    r, p, x = n, 2, n
    while p * p <= x:
        if x % p == 0:
            while x % p == 0: x //= p
            r -= r // p
        p += 1
    if x > 1: r -= r // x
    return r
# phi sieve
ph = list(range(Kmax + 1))
for p in range(2, Kmax + 1):
    if ph[p] == p:
        for j in range(p, Kmax + 1, p):
            ph[j] -= ph[j] // p
ms = list(range(4, 41)) + [60, 210, 2310, 30030]
ratio_lo, ratio_hi, hS_lo = 9, 0, 9
for m in ms:
    pm = phi(m)
    S = 0.0; h = 0.0
    chk = sorted(set([m * m, Kmax] + [x for x in (10**3, 10**4, 10**5) if x >= m * m]))
    chk = [x for x in chk if x <= Kmax]
    Sp = {p: 0.0 for p in (2, 3, 5, 7, 11, 13, 101)}
    for j in range(1, Kmax + 1):
        if gcd(j, m) == 1:
            S += 1 / j; h += ph[j] / j / j
            for p in Sp:
                if j % p == 0: Sp[p] += ph[j] / j / j
        if j in chk:
            if S < pm / m * math.log(j) - 1e-12:
                fails += 1; print("2.1(a) FAIL", m, j)
            if h < 0.54 * S:
                fails += 1; print("2.1(b) FAIL", m, j)
            for p, v in Sp.items():
                if m % p and v > S / p + 1e-12:
                    fails += 1; print("2.1(c) FAIL", m, j, p)
    if Kmax >= m * m:
        r = S / (pm / m * math.log(Kmax))
        ratio_lo = min(ratio_lo, r); ratio_hi = max(ratio_hi, r); hS_lo = min(hS_lo, h / S)
print(f"Lemma2.1 at K={Kmax}: S_m/((phi/m)logK) in [{ratio_lo:.3f},{ratio_hi:.3f}], min h_m/S_m={hS_lo:.3f}")
# (a) just below m^2: is the hypothesis x>=m^2 needed? report smallest x where (a) fails for primorial m
for m in (210, 2310, 30030):
    pm = phi(m); S = 0.0; worst = None
    for j in range(1, min(Kmax, m * m) + 1):
        if gcd(j, m) == 1: S += 1 / j
        if j >= 2 and S < pm / m * math.log(j): worst = j
    print(f"  (a) for m={m}: largest x<=min(K,m^2) violating S_m(x)>=(phi/m)log x: {worst}")
print("TOTAL FAILS", fails)
sys.exit(1 if fails else 0)
