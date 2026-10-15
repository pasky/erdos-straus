"""s7_cap_density: forced-witness cap bound (q1-3)/4 vs exact window cap at q1, on Mordell-hard primes.
q1(p) = least prime q ≡ 3 (4) with (q/p) = -1. Exact cap at window m (CAP_DOWN Lemma 1.1): least e such that
-K ≡ prod s^{c_s} (mod m), c_2 <= 2 b_2, odd s: c_s <= 2b_s or (c_s even and c_s <= 2b_s + 2e).
Usage: python s7_cap_density.py N
"""
import sys, collections, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from s7_window_excess import spf_sieve, factor, legendre

def window_cap(K, m, spf, emax=12):
    fac = factor(K, spf); target = (-K) % m
    for e in range(emax + 1):
        S = {1 % m}
        for s, b in fac.items():
            r = s % m
            if s == 2:
                ex = range(0, 2 * b + 1)
            else:
                ex = list(range(0, 2 * b + 1)) + [c for c in range(2 * b + 1, 2 * b + 2 * e + 1) if c % 2 == 0]
            pw = {pow(r, c, m) for c in ex}
            S = {u * v % m for u in S for v in pw}
        if target in S:
            return e
    return None

if __name__ == "__main__":
    N = int(sys.argv[1])
    spf = spf_sieve(N // 4 + 2000)
    isp = bytearray([1]) * (N + 1); isp[0] = isp[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if isp[i]:
            isp[i * i::i] = bytearray(len(isp[i * i::i]))
    MH = {1, 121, 169, 289, 361, 529}
    tab = collections.Counter(); viol = 0; n = 0
    for p in range(5, N + 1, 4):
        if not isp[p] or p % 840 not in MH:
            continue
        n += 1
        q1 = next(q for q in range(3, p, 4) if isp[q] and legendre(q, p) == -1)
        bound = (q1 - 3) // 4
        c = window_cap((p + q1) // 4, q1, spf)
        if c is None or c > bound:
            viol += 1
        tab[(q1 if q1 < 60 else '>=60', bound if q1 < 60 else '-', c)] += 1
    print("Mordell-hard primes <=", N, ":", n, "; exact cap at q1 exceeding (q1-3)/4:", viol)
    for k in sorted(tab, key=str):
        print("  (q1, forced bound, exact cap at q1)", k, tab[k])
