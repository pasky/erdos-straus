"""s9_level_bm.py (O271): the BM layer of Theorem K (O269) in level coordinates.
For 4 | t and N = t n + 1: every d | N with d == -1 (mod t) has chi_{-t}(d) = -1 (chi_{-t} odd).  Level-BM relaxation:
  BM_t(n): N has a prime factor l with (-t/l) = -1.
Claim (Prop 2.2): for odd n, BM_t(n) holds for some 4 | t  <=>  n is not a square; witness: least prime l with (n/l) = -1,
t == 0 (mod 4), t == -n^{-1} (mod l), t <= 4l.
Checks all odd n <= NMAX: witness valid at every non-square; no level t <= TMAX works at odd squares (all prime factors of
t m^2 + 1 split in Q(sqrt(-t))).  Also: how often the BM-witness level already carries an ES (★) hit.
usage: python s9_level_bm.py NMAX TMAX"""
import sys
from math import isqrt

def jacobi(a, n):
    a %= n; t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: t = -t
        a %= n
    return t if n == 1 else 0

def kron(D, l):   # Kronecker (D/l) for odd prime l
    return jacobi(D, l)

def primes_upto(m):
    s = bytearray([1]) * (m + 1); s[0] = s[1] = 0
    for i in range(2, isqrt(m) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(m + 1) if s[i]]

def factor(N):
    f = []; d = 2
    while d * d <= N:
        if N % d == 0:
            f.append(d)
            while N % d == 0: N //= d
        d += 1 if d == 2 else 2
    if N > 1: f.append(N)
    return f

def main():
    NMAX, TMAX = int(sys.argv[1]), int(sys.argv[2])
    P = primes_upto(10000)
    bad = 0; hit = 0; nonsq = 0; maxl = 0; sqbad = 0; nsq = 0
    for n in range(3, NMAX + 1, 2):
        r = isqrt(n)
        if r * r == n:
            nsq += 1
            for t in range(4, TMAX + 1, 4):
                if any(kron(-t, l) == -1 for l in factor(t * n + 1) if l > 2):
                    sqbad += 1; break
            continue
        nonsq += 1
        l = next(q for q in P[1:] if n % q and jacobi(n, q) == -1)
        maxl = max(maxl, l)
        ninv = pow(n, -1, l)
        t = next(t for t in range(4, 4 * l + 1, 4) if (t + ninv) % l == 0)
        N = t * n + 1
        if N % l or kron(-t, l) != -1:
            bad += 1
        # does the witness level carry a (★) word (divisor d == -1 mod t, d >= t-1, N/d >= t-1)?
        if any(N % d == 0 and d >= t - 1 and N // d >= t - 1 for d in range(t - 1, isqrt(N) + 1, t)):
            hit += 1
    print(f"odd n <= {NMAX}: {nonsq} non-squares, BM-witness failures {bad}, max least non-residue prime {maxl}; "
          f"witness level also an ES (★) level at {hit} ({hit/nonsq:.3f})")
    print(f"odd squares <= {NMAX}: {nsq}; squares with some 4 | t <= {TMAX} having an inert prime factor: {sqbad}")

if __name__ == "__main__":
    main()
