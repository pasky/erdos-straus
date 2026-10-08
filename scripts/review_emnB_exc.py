"""R94 review B, from scratch: brute-force m-exceptional n (m/n != 1/x+1/y+1/z, positive
integers, repetitions allowed) for n <= N0, m in a range; compare with PW Table 1.
Two-unit-fraction criterion: a/b (reduced) = 1/y+1/z  iff  exist coprime y',z' with
y'z' | b and a | y'+z'   (then g = b(y'+z')/(a y' z'), y = g y', z = g z').
Usage: uv run python scripts/review_emnB_exc.py N0 mlo mhi
"""
import sys
from math import gcd

def spf_sieve(n):
    s = list(range(n + 1))
    for p in range(2, int(n ** 0.5) + 1):
        if s[p] == p:
            for k in range(p * p, n + 1, p):
                if s[k] == k: s[k] = p
    return s

def factor(n, spf):
    f = {}
    while n > 1:
        p = spf[n]; f[p] = f.get(p, 0) + 1; n //= p
    return f

def merge(f1, f2):
    f = dict(f1)
    for p, e in f2.items(): f[p] = f.get(p, 0) + e
    return f

def two_unit(a, fb):
    """a/b with b given by factorization fb (gcd(a,b)=1 assumed)."""
    if a == 0: return False
    ps = list(fb.items())
    # y' z' coprime, y'z' | b: each prime power p^e of b goes to y' (exp 1..e), z' (1..e) or neither
    # enumerate via DFS over primes, tracking (y' mod a, z' mod a)
    states = {(1 % a, 1 % a)}
    for p, e in ps:
        new = set(states)
        pw = [pow(p, i, a) for i in range(1, e + 1)]
        for (ya, za) in states:
            for q in pw:
                new.add((ya * q % a, za)); new.add((ya, za * q % a))
        states = new
    return any((ya + za) % a == 0 for ya, za in states)

def representable(m, n, spf):
    if m * 1 > 3 * n: return False  # m/n > 3
    fn = factor(n, spf)
    xlo = n // m + 1
    for x in range(xlo, 3 * n // m + 1):
        a = m * x - n; b = n * x
        if a <= 0: continue
        g = gcd(a, b); a //= g
        fb = merge(fn, factor(x, spf))
        # divide out g from fb
        gg = g
        for p in list(fb):
            while gg % p == 0:
                gg //= p; fb[p] -= 1
            if fb[p] == 0: del fb[p]
        if two_unit(a, fb): return True
    return False

PW = {4: [1], 5: [1], 6: [1], 7: [1, 2], 8: [1, 2, 3, 11, 17, 131, 241], 9: [1, 2, 5, 11, 19],
      10: [1, 2, 3, 7, 11, 43, 61, 67, 181], 11: [1, 2, 3, 4, 37],
      12: [1, 2, 3, 5, 7, 13, 25, 29, 31, 37, 73, 97, 193, 433, 577, 1129, 1657, 1873, 2521, 2593, 3433, 10369, 12049, 12241],
      13: [1, 2, 3, 4, 5, 7, 14, 53, 61, 67, 79, 211, 281], 14: [1, 2, 3, 4, 5, 17, 19, 29, 59, 257, 353, 841],
      15: [1, 2, 3, 4, 8, 16, 17, 19, 23, 31, 34, 47, 53, 61, 79, 113, 122, 137, 151, 197, 226, 233, 271, 541, 1103, 1171, 1367, 4201, 6301, 12601, 16831, 20521]}

if __name__ == "__main__":
    N0, mlo, mhi = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    spf = spf_sieve(3 * N0 + 10)
    bad = 0
    for m in range(mlo, mhi + 1):
        exc = []
        for n in range(1, N0 + 1):
            # divisor closure shortcut: if some proper divisor is representable, n is representable
            if not representable(m, n, spf): exc.append(n)
        ref = [n for n in PW.get(m, []) if n <= N0]
        ok = (exc == ref) if m in PW else None
        if ok is False: bad += 1
        print(f"m={m}: exceptional n<={N0}: {exc}  PW-match={ok}", flush=True)
    sys.exit(1 if bad else 0)
