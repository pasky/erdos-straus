"""R223 (hostile review #2 of STERILE_EXPLICIT.md): from-scratch brute force of P-data and Q-data for small N,
checking Lemmas 1.1, 1.2 (P), the Q identities / f <= F+2 / <= 2 points per (a,d) / f-route congruences (§3.2),
the parity and non-residue statements imported from M17 Lemma 1.3 / 5.1 for general odd prime r, and the
in-cell restrictions r ∤ ab (P), r ∤ abcde (Q).  Written independently of scripts/se_*.
Usage: PYTHONPATH=scripts uv run python scripts/review_se2_identities.py"""
import sys
from math import gcd, isqrt

def legendre(x, r):
    x %= r
    if x == 0: return 0
    return 1 if pow(x, (r - 1) // 2, r) == 1 else -1

def P_data(N):
    """all (a,b,c,d,e) positive with 4abd = N+e, a+b = ce, a <= b (no r-condition)."""
    out = []
    a = 1
    while 4 * a * a - 2 * a <= N + 2 * a:          # 4ab <= N + e <= N + 2b  and b >= a
        b = a
        while 4 * a * b - 2 * b <= N:               # 4abd >= 4ab, N + e <= N + 2b
            m = 4 * a * b
            e = (-N) % m
            if e == 0: e = m
            if e <= a + b and (a + b) % e == 0:
                d = (N + e) // m
                c = (a + b) // e
                out.append((a, b, c, d, e))
            b += 1
        a += 1
    return out

def Q_data(F):
    """all N-points (a,b,c,d) of Sigma^I_F: 4abcd = F(a+b)+c, with a <= b; returns (a,b,c,d,e,f)."""
    out = []
    # f = 4acd - F > 0 and f <= F + 2 (to be re-checked, not assumed): enumerate acd <= F (generous)
    for a in range(1, F + 1):
        for c in range(1, F // a + 1):
            for d in range(1, F // (a * c) + 1):
                f = 4 * a * c * d - F
                if f <= 0: continue
                if (a * F + c) % f: continue
                b = (a * F + c) // f
                if b < a: continue
                assert 4 * a * b * c * d == F * (a + b) + c
                if (a + b) % c: continue
                out.append((a, b, c, d, (a + b) // c, f))
    return out

def Q_data_wide(F, lim):
    """sanity: the same with acd up to lim*F, to test that no point has acd > F (i.e. f > 3F)."""
    n = 0
    for a in range(1, lim * F + 1):
        for c in range(1, lim * F // a + 1):
            for d in range(1, lim * F // (a * c) + 1):
                f = 4 * a * c * d - F
                if f > 0 and (a * F + c) % f == 0 and (a * F + c) // f >= a and ((a + (a * F + c) // f) % c == 0):
                    n += 1
    return n

def check_P(r, K):
    N = r ** K
    D = P_data(N)
    nin = 0
    for (a, b, c, d, e) in D:
        f, f2 = 4 * a * c * d - 1, 4 * b * c * d - 1
        assert e * f == N + 4 * a * a * d and e * f2 == N + 4 * b * b * d          # 1.1(i)
        assert b * f == N * c + a and a * f2 == N * c + b                          # 1.1(ii)
        assert f * f2 == 4 * c * c * d * N + 1                                     # 1.1(iii)
        assert 4 * a * a * d <= 2 * N and 2 * a * a * d <= N and a * c * d <= N      # 1.2 / caps
        assert e <= N // (a * c * d) + 1 and b <= N / (2 * a * d)
        if c % r and d % r:
            if a % r == 0 or b % r == 0:
                assert a % r == 0 and b % r == 0, "r|b without r|a"                # M17 §5: r|b => r|a
                assert (-f) % r == 1 and (-f2) % r == 1                            # box ≡ 1: not in a cell
            else:
                nin += 1
                assert gcd(e, a * b * d) == 1 and e % 2 == 1                       # 1.1(iv)
                assert K % 2 == 1, ("even K with a primitive datum", r, K)          # M17 Lemma 1.3 (P)
                h = (K + 1) // 2
                box = (-f) % r ** h
                assert box == (-a * pow(b, -1, r ** K)) % r ** h                    # M17 Lemma 5.1(ii)
        if c % r == 0 or d % r == 0:
            pass
    # parity for ALL data with r ∤ cd (not only primitive): (N/f) = -1 forces K odd
    for (a, b, c, d, e) in D:
        if c % r and d % r: assert K % 2 == 1
    return len(D), nin

def check_Q(r, k):
    F = r ** k
    D = Q_data(F)
    per_ad = {}
    nin = 0
    for (a, b, c, d, e, f) in D:
        assert e * f == 4 * a * a * d + 1 and 4 * a * b * d == e * F + 1 and f * b == a * F + c
        assert f * (4 * b * c * d - F) == F * F + 4 * c * c * d
        assert 1 <= f <= F + 2
        per_ad[(a, d)] = per_ad.get((a, d), 0) + 1
        if e % r == 0: continue                               # not a Q-datum
        assert a % r and b % r and d % r                      # forced
        box = (-4 * a * a * d) % F
        if c % r == 0:
            assert legendre(box, r) == 1                      # residue cell
            continue
        nin += 1
        assert k % 2 == 1 and legendre(box, r) == -1          # M17 Lemma 1.3
        assert box == (-a * pow(b, -1, F)) % F                # M17 Lemma 5.1(i)
        assert gcd(f, F) == 1
        # f-route congruences (§3.2): c ≡ -aF, d ≡ -(4a^2)^{-1}, a ≡ -c F^{-1} (mod f)
        assert (c + a * F) % f == 0 and (4 * a * a * d + 1) % f == 0 and (a * F + c) % f == 0
        assert (f + F) % (4 * a) == 0 and (f + F) % (4 * c) == 0 and (f + F) % (4 * d) == 0
    assert max(per_ad.values(), default=0) <= 2              # M17C Lemma 2.1(iv)
    return len(D), nin, max(per_ad.values(), default=0)

if __name__ == '__main__':
    for r in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        for K in range(1, 16):
            if r ** K > 2 * 10 ** 6: break
            n, nin = check_P(r, K)
            print(f"P r={r} K={K}: data {n}, primitive {nin}: ok")
        for k in range(1, 6):
            if r ** k > 6000: break
            n, nin, mx = check_Q(r, k)
            print(f"Q r={r} k={k}: points {n}, in-cell Q-data {nin}, max per (a,d) {mx}: ok")
    print("wide Q enumeration (acd <= 3F) at F=343, 289:", Q_data_wide(343, 3), len(Q_data(343)), Q_data_wide(289, 3), len(Q_data(289)))
    for K in (3, 5):
        print(f"D_P(17^{K}) with 17 ∤ cd =", sum(1 for t in P_data(17 ** K) if t[2] % 17 and t[3] % 17), "(M17: 32, 121)")
    print("D_Q(17^3) with 17 ∤ e =", sum(1 for t in Q_data(17 ** 3) if t[4] % 17), "(M17: 73)")
