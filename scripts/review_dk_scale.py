"""R169 from-scratch: §8.2 rotation cell census, §8.3 scaling law, §9.2 lemma and coverage.
Usage: PYTHONPATH=scripts uv run python scripts/review_dk_scale.py [N_cov]
"""
import sys
from math import gcd, isqrt
from review_dk_core import jacobi


def K3(a, b, c):
    return a * b * c - a - c


def main():
    Ncov = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    # 8.2 rotation census over mod-8 cells: word (v,t,u) -> (t,u,v): new (t',u',v') = (u,v,t)
    from review_dk_cells import PLUS
    sg = lambda t, u, v: 1 if (t % 4, u % 4, v % 4) in PLUS else -1
    cm = cp = cbad = 0
    for t in range(8):
        for u in range(8):
            for v in range(8):
                n = t * u * v - u - v; n2 = t * u * v - t - v
                if n % 4 == 1 and n2 % 4 == 1:
                    s1, s2 = sg(t, u, v), sg(u, v, t)
                    if s1 != s2: cbad += 1
                    elif s1 == -1: cm += 1
                    else: cp += 1
    print("rotation mod-8 cells: -1->-1 %d, +1->+1 %d, sign changes %d" % (cm, cp, cbad))
    # 8.3 scaling: K(a v', t, a u') = a K(v', a t, u'); (A/n) = (-1/a)(A/m)
    bad = cnt = 0
    for a in range(3, 40, 2):
        for t in range(2, 12):
            for u1 in range(1, 12):
                for v1 in range(1, 12):
                    m = K3(v1, a * t, u1); n = K3(a * v1, t, a * u1)
                    if n != a * m: bad += 1; continue
                    if m % 2 == 0 or m <= 1: continue
                    A = a * t * u1 - 1
                    cnt += 1
                    if jacobi(A, n) != jacobi(-1, a) * jacobi(A, m): bad += 1
    print("scaling law: cases %d bad %d" % (cnt, bad))
    # 9.2 lemma: n = a m = 1 mod 4, a = 3 mod 4; A | m+1, A = -1 mod a, A >= 2a-1, (2/m)^{v2(A)} = 1
    bad = cnt = 0
    for a in range(3, 80, 4):
        for m in range(3, 4000, 4):
            n = a * m
            for A in range(2 * a - 1, m + 2):
                if (m + 1) % A or (A + 1) % a: continue
                k = (A & -A).bit_length() - 1
                if jacobi(2, m) ** k != 1: continue
                cnt += 1
                v, t, u = a * (m + 1) // A, (A + 1) // a, a
                if K3(v, t, u) != n or t * u - 1 != A or jacobi(A, n) != -1 or min(v, t, u) < 2:
                    bad += 1; print("9.2 fail", a, m, A)
    print("9.2 lemma: cases %d bad %d" % (cnt, bad))
    # 9.2 coverage: composite non-square n = 1 mod 4 <= Ncov with a divisor = 3 mod 4;
    # 'inherited' = some -1 word with a | u, a | v for some a = 3 mod 4 (then a | n)
    inh = bytearray(Ncov + 1)
    for t in range(2, Ncov):
        if 4 * t - 4 > Ncov: break
        for u in range(2, Ncov):
            if 2 * t * u - u - 2 > Ncov: break
            for v in range(2, Ncov):
                n = t * u * v - u - v
                if n > Ncov: break
                if n % 4 != 1 or inh[n]: continue
                g = gcd(u, v)
                if g < 3: continue
                ok = any(g % d == 0 for d in range(3, g + 1, 4))
                if ok and jacobi(t * u - 1, n) == -1: inh[n] = 1
    sieve = bytearray([1]) * (Ncov + 1); sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(Ncov) + 1):
        if sieve[i]: sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    tot = hit = 0
    for n in range(5, Ncov + 1, 4):
        if sieve[n] or isqrt(n) ** 2 == n: continue
        has3 = False; m = n; q = 3
        while q * q <= m:
            while m % q == 0:
                if q % 4 == 3: has3 = True
                m //= q
            q += 2
        if m > 1 and m % 4 == 3: has3 = True
        if has3:
            tot += 1; hit += inh[n]
    print("coverage: composite non-square n=1(4)<=%d with a factor 3(4): %d, inherited: %d (%.1f%%)" % (Ncov, tot, hit, 100.0 * hit / tot))


if __name__ == "__main__":
    main()
