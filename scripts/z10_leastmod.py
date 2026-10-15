"""O234 EVIDENCE: least PRIME certifying modulus ℓ (ℓ ≡ 3 mod 4) of the 𝒟_e family, for all primes 5 ≤ p ≤ N,
by cap e (Prop 5.1; e = 99 ~ ∞), plus odd-square T1 control (n = m² must never be hit).  For each prime ℓ ≤ L:
classes −4D mod ℓ, D ∈ 𝒟_e(ℓ), 4D < ℓ; only n > ℓ counted.  Prints #p with no certificate at ℓ ≤ L, mean/max least ℓ.
usage: z10_leastmod.py N L"""
import sys, math
import numpy as np
from sympy import primerange, factorint
N, L = int(sys.argv[1]), int(sys.argv[2])
P = np.zeros(N + 1, bool); P[2:] = True
for i in range(2, math.isqrt(N) + 1):
    if P[i]: P[i*i::i] = False
ps = np.nonzero(P)[0]; ps = ps[ps >= 5]
sqs = np.array([m * m for m in range(3, math.isqrt(N) + 1, 2)])
for e in (0, 1, 2, 4, 99):
    least = np.zeros(N + 1, np.int64)
    for l in primerange(7, L + 1):
        if l % 4 != 3: continue
        A = (l + 1) // 4; fA = factorint(A)
        Ds = [1]
        for s, sg in fA.items():
            Ds = [d * s ** t for d in Ds for t in range(0, 2 * sg + 2 * e + 1)
                  if (t <= 2 * sg or (s != 2 and t % 2 == 0)) and d * s ** t * 4 < l]
        for D in Ds:
            c = (-4 * D) % l
            idx = np.arange(c + l * ((l - c) // l + 1), N + 1, l)
            sel = idx[least[idx] == 0]; least[sel] = l
    lp = least[ps]; none = int((lp == 0).sum()); got = lp[lp > 0]
    sqhit = int((least[sqs] > 0).sum())
    print(f"e={e}: primes 5..{N}: {len(ps)}; no prime-modulus certificate with ℓ ≤ {L}: {none}; "
          f"mean least ℓ {got.mean():.2f}, max {got.max()}; odd squares hit: {sqhit}")
