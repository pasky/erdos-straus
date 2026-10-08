"""O94 toy check (EVIDENCE only, toy parameters, no H floor): the fibre mass
mu_c(m) = sum_{x<l<=2x} f_c(l)/l, f_c(l) = #{(k,u,v): k<=K,(k,m)=1, u,v<=z, (u,v)=(uv,k)=1,
m*u*v | k*l+1, k | u+c*v}, should scale like 1/m (Cor. 3.2: mu_c ~ t^2 h(J_c)/phi(m),
h ~ (phi(m)/m) log K).  Prints m*mu_c averaged over a few reduced c."""
import sys, math, random
import numpy as np
from sympy import primerange
x = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**6
K = int(sys.argv[2]) if len(sys.argv) > 2 else 30
z = int(sys.argv[3]) if len(sys.argv) > 3 else 40
P = np.array(list(primerange(x + 1, 2 * x + 1)), dtype=np.int64)
inv = 1.0 / P
random.seed(1)
cs = []
while len(cs) < 4:
    c = random.randrange(1, 10**9)
    if all(c % p for p in primerange(2, K + 1)): cs.append(c)
ms = list(range(4, 31)) + [60, 105, 210]
print(f"x={x} K={K} z={z} #primes={len(P)}")
for m in ms:
    tot = 0.0; pred = 0.0
    for c in cs:
        for k in range(1, K + 1):
            if math.gcd(k, m) != 1: continue
            for v in range(1, z + 1):
                if math.gcd(v, k) != 1: continue
                u0 = (-c * v) % k or k
                for u in range(u0, z + 1, k):
                    if math.gcd(u, v) != 1: continue
                    q = m * u * v
                    r = (-pow(k, -1, q)) % q
                    tot += inv[P % q == r].sum()
                    pred += math.log(2) / math.log(1.5 * x) / (q * np.prod([1 - 1/p for p in primerange(2, q+1) if q % p == 0]))
    tot /= len(cs); pred /= len(cs)
    print(f"m={m:4d} mu={tot:.4f} m*mu={m*tot:.3f} pred(BV main)={pred:.4f} m*pred={m*pred:.3f}")
