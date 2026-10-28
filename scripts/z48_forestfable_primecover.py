#!/usr/bin/env python3
"""z48 forestfable — the prime-numerator sub-covering.
ES5(p) ⟸ ∃ prime ℓ with p mod ℓ ∈ G_ℓ = {−d mod ℓ : d | ℓ+1, d < ℓ, (−d/ℓ) = −1}  (p ≡ 1 mod 8).
For distinct primes the residues p mod ℓ are independent in the CRT model, so the model survival
probability for ℓ ≤ X is exactly  Π_{5≤ℓ≤X} (1 − |G_ℓ|/(ℓ−1))  (conditioned on p ≡ 1 mod 24: ℓ = 2, 3 never hit).
Prints the sieve sum S(X) = Σ |G_ℓ|/(ℓ−1), −log Π, local slopes d(−log Π)/d(log X), and the
average of |G_ℓ|/(τ(ℓ+1)−1) by ℓ mod 8."""
import sys, math
from sympy import primerange, divisors, jacobi_symbol
X = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
cps = [10**k for k in range(2, int(math.log10(X)) + 1)]
S = 0.0; logP = 0.0; i = 0
ratio = {1: [0, 0], 3: [0, 0], 5: [0, 0], 7: [0, 0]}
prev = None
print("X  S(X)=sum|G|/(l-1)  -log prod  slope_since_prev  (log X)")
def report(x):
    global prev
    slope = (logP - prev[1]) / (math.log(x) - prev[0]) if prev else float('nan')
    print(f"{x:8d}  {S:8.4f}  {logP:8.4f}  {slope:6.3f}  {math.log(x):.2f}")
    prev = (math.log(x), logP)
for l in primerange(5, X + 1):
    while cps and l > cps[0]:   # report each checkpoint before including the first prime above it
        report(cps.pop(0))
    g = 0
    for d in divisors(l + 1):
        if d < l and jacobi_symbol((-d) % l, l) == -1:
            g += 1
    S += g / (l - 1)
    logP += -math.log(1 - g / (l - 1))
    r = ratio[l % 8]; r[0] += g; r[1] += len(divisors(l + 1)) - 1
while cps:
    report(cps.pop(0))
print("mean |G_l|/(tau(l+1)-1) by l mod 8:", {k: round(v[0] / v[1], 3) for k, v in ratio.items()})
