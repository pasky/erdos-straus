#!/usr/bin/env python3
"""z51 linnik §3 checks.
(1) For S a set of s primes and r >= 1 let b_{n0} := #ordered r-tuples from S whose product has squarefree kernel n0.
    Check: sum_n0 b_n0 chi(n0) = (sum_q chi(q))^r for quadratic chi = (./p), p not in S;  ||b||^2 = E_eps sigma^{2r}
    <= (2r-1)!! s^r.
(2) Empirical quadratic large sieve: sum_{p <= Q, p == 1 mod 4} |sum b_n (n/p)|^2  vs  (Q + N) ||b||^2, N = max n0.
(3) Bias counts: #{p <= Q : |sum_{q in S} (q/p)| >= 2 eta s} for a block S, against the Theorem 3.1 bound
    (Q+N)||b||^2 / (2 eta s)^{2r} (implied constant 1, heuristic sanity only).
"""
import itertools, math, random, sys
from collections import Counter

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]

def leg(a, p):
    r = pow(a % p, (p - 1) // 2, p)
    return 0 if r == 0 else (1 if r == 1 else -1)

def kernel_weights(S, r):
    b = Counter()
    for tup in itertools.product(S, repeat=r):
        c = Counter(tup)
        n0 = 1
        for q, e in c.items():
            if e % 2: n0 *= q
        b[n0] += 1
    return b

def main():
    rnd = random.Random(5)
    S = [q for q in primes_upto(60) if q > 30]          # 31..59: 7 primes
    s = len(S)
    for r in (2, 3, 4):
        b = kernel_weights(S, r)
        nb2 = sum(v * v for v in b.values())
        dfact = math.prod(range(2 * r - 1, 0, -2))
        # E sigma^{2r} exactly over all sign vectors
        Es = sum(sum(e) ** (2 * r) for e in itertools.product((-1, 1), repeat=s)) / 2 ** s
        assert abs(nb2 - Es) < 1e-6, (nb2, Es)
        assert nb2 <= dfact * s ** r
        for p in primes_upto(3000)[20:60]:
            if p in S: continue
            lhs = sum(v * leg(n0, p) for n0, v in b.items())
            assert lhs == sum(leg(q, p) for q in S) ** r
        N = max(b)
        for Q in (10 ** 4, 10 ** 5):
            tot = sum(sum(v * leg(n0, p) for n0, v in b.items()) ** 2
                      for p in primes_upto(Q) if p % 4 == 1 and p > 60)
            print("r=%d s=%d ||b||^2=%d (bound (2r-1)!!s^r=%d)  Q=%d: sum_p|.|^2=%d  (Q+N)||b||^2=%d  ratio=%.3f"
                  % (r, s, nb2, dfact * s ** r, Q, tot, (Q + N) * nb2, tot / ((Q + N) * nb2)))
    print("identities (1) verified")

if __name__ == "__main__":
    main()
