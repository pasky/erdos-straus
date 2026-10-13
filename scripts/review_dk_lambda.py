"""R169 from-scratch: Cor 4.6, §4.2, §4.4 vanishing list, §9.1 / CONJECTURE SQ5, §10.1 t_min records.
lambda(n) = min HJ length of A in (0,n), gcd 1, Jacobi (A/n) = -1.
Usage: PYTHONPATH=scripts uv run python scripts/review_dk_lambda.py N [NSMALL]
"""
import sys
from math import gcd, isqrt
from review_dk_core import jacobi, hj
from review_dk_cells import five


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    NS = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
    INF = 10 ** 9
    int3 = bytearray(N + 1)      # interior length-3 word with Jacobi -1
    sl5 = bytearray(N + 1)       # interior word in one of the five slices (no Jacobi used)
    a0 = bytearray(N + 1); aT = bytearray(N + 1)
    tmin = [INF] * (N + 1)
    for t in range(2, N):
        if 4 * t - 4 > N: break
        for u in range(2, N):
            if 2 * t * u - u - 2 > N: break
            for v in range(2, N):
                n = t * u * v - u - v
                if n > N: break
                if n % 4 != 1: continue
                A = t * u - 1
                if jacobi(A, n) == -1:
                    int3[n] = 1
                    if t < tmin[n]: tmin[n] = t
                if five(t, u, v): sl5[n] = 1
                if A % 4 == 0: a0[n] = 1
                if t % 4 == 0: aT[n] = 1
    # length 2: n = b1*b2 - 1, A = b2, b1,b2 >= 2
    l2 = bytearray(N + 1)
    for b2 in range(2, N):
        if 2 * b2 - 1 > N: break
        for b1 in range(2, N):
            n = b1 * b2 - 1
            if n > N: break
            if n % 4 == 1 and jacobi(b2, n) == -1: l2[n] = 1
    # boundary 4.2 (v = 1): u(t-1) = n+1, t,u >= 2, tu = 1 mod 4  -- and factor criterion
    def bnd(n):
        m = n + 1
        for u in range(2, isqrt(m) + 1):
            if m % u == 0:
                for uu in (u, m // u):
                    t = m // uu + 1
                    if (t * uu) % 4 == 1: return True
        return False

    def crit(n):
        m = (n + 1) // 2; q = 2
        while q * q <= m:
            while m % q == 0:
                if q % 4 == 3: return True
                m //= q
            q += 1
        return m > 1 and m % 4 == 3
    bad = 0
    issq = lambda n: isqrt(n) ** 2 == n
    fails = []
    for n in range(5, N + 1, 4):
        b = bnd(n)
        if b != crit(n) or b != bool(l2[n]):
            bad += 1; print("boundary mismatch", n, b, crit(n), l2[n])
        if int3[n] != sl5[n]:
            bad += 1; print("Thm4.5 mismatch", n)
        lam3 = int3[n] or l2[n]
        if issq(n):
            if lam3 or sl5[n] or b: bad += 1; print("square with hit", n)
        elif not lam3:
            fails.append(n)
    print("N=%d bad=%d  non-square n=1(4) with lambda>3: %s" % (N, bad, fails))
    # direct lambda by HJ CF of every A, small n
    bad2 = 0
    for n in range(5, NS + 1, 4):
        lam = min((len(hj(n, A)) for A in range(1, n) if gcd(A, n) == 1 and jacobi(A, n) == -1), default=INF)
        if (lam <= 3) != bool(int3[n] or l2[n]) or (lam == 2) != bool(l2[n]):
            bad2 += 1; print("lambda direct mismatch", n, lam)
        if n == 105: print("lambda(105) direct =", lam)
    print("direct-lambda cross-check n<=%d bad=%d" % (NS, bad2))
    # 4.4 vanishing lists
    v0 = [n for n in range(5, N + 1, 4) if not issq(n) and not a0[n]]
    v0T = [n for n in range(5, N + 1, 4) if not issq(n) and not a0[n] and not aT[n]]
    print("a0=0 non-squares: %d, max %s" % (len(v0), max(v0) if v0 else None))
    print("a0=aT=0 non-squares (%d):" % len(v0T), v0T)
    # Cor 4.6 evidence + t_min records, primes p = 1 mod 8
    sieve = bytearray([1]) * (N + 1); sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(N) + 1):
        if sieve[i]: sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    P = [p for p in range(17, N + 1, 8) if sieve[p]]
    c2 = sum(1 for p in P if p <= 20000 and l2[p]); c3 = sum(1 for p in P if p <= 20000 and not l2[p] and int3[p])
    print("primes p=1(8)<=2e4: %d, lambda=2: %d, lambda=3: %d" % (sum(1 for p in P if p <= 20000), c2, c3))
    print("primes p=1(8)<=N: %d, with interior -1 word: %d" % (len(P), sum(int3[p] for p in P)))
    rec = []; best = 0
    for p in P:
        if tmin[p] > best:
            best = tmin[p]; rec.append((p, best))
    print("t_min records:", rec)


if __name__ == "__main__":
    main()
