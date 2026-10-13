"""R175 from-scratch W(n) = #{(c,f,g) in N^3 : cfg - c - f = n, fg = 1 mod 4} (GI §0 definition; for n = 1 mod 4
equivalently #{(t, m'') : t = 3 (4), m'' | tn+1, m'' = -1 (t), 4 | (tn+1)/m''}).  numpy strided adds."""
import sys, numpy as np
from math import isqrt
X = int(sys.argv[1])
W = np.zeros(X + 1, dtype=np.int32)
for f in range(1, X + 2):
    g = 1
    while True:
        M = f * g - 1
        if M - f > X:
            break
        if M >= 1 and (f * g) % 4 == 1:
            c0 = max(1, -(-(1 + f) // M))
            s = c0 * M - f
            if s <= X:
                W[s::M] += 1
        g += 1
n = np.arange(X + 1)
sq = np.array([isqrt(int(k)) ** 2 == k for k in range(X + 1)])
odd_sq_nonzero = [int(k) for k in range(1, X + 1, 2) if sq[k] and W[k] != 0]
zeros = [int(k) for k in range(1, X + 1, 4) if W[k] == 0 and not sq[k]]
print("X", X, "odd squares with W != 0:", odd_sq_nonzero[:10])
print("non-square zeros n = 1 mod 4:", len(zeros), zeros)
sieve = np.ones(X + 1, bool); sieve[:2] = False
for i in range(2, isqrt(X) + 1):
    if sieve[i]: sieve[i*i::i] = False
pz = [int(k) for k in zeros if sieve[k]]
print("prime zeros:", pz, " #primes = 1 mod 4 with W=0:", int(np.sum((W == 0) & sieve & (n % 4 == 1))))
print("zeros = 9 mod 24:", sum(1 for z in zeros if z % 24 == 9), "of", len(zeros))
for r in zeros[:8]:
    print("r", r, "W(r k^2) k=3,5,7,11,13:", [int(W[r * k * k]) if r * k * k <= X else None for k in (3, 5, 7, 11, 13)])
np.save(sys.argv[2] if len(sys.argv) > 2 else "/tmp/W.npy", W)
