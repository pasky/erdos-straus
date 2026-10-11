"""O135 §3.3: limiting (p -> infinity) expected number of e-slices passing the NECESSARY size condition
3*tau(L_e^2) >= phi(e)/2 for a transparent full-coset certificate (Theorem 2.2, theta = 0), per type.

Model (exact limit of the census as p -> oo over a random residue class): for primes l < e, l does not divide e,
the events l^j | N_e are independent with P(v_l >= j) = l^-j (CRT over p).  Including l | e (which never divide N)
only enlarges tau, so we include all l < e: an UPPER bound for the model probability.
DP over the log of tau(L^2) = prod(2v+1) on a grid; primes added incrementally as e grows.
Output: partial sums of sum_{e = 3 mod 4} P_e by decade (one type; double for I+II).
Usage: lsa_model_limit.py EMAX
"""
import sys, math
import numpy as np
from sympy import primerange, totient

EMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10**5
H = 0.01                      # log-grid step
NB = int(60 / H)              # log tau(L^2) up to e^60
dist = np.zeros(NB); dist[0] = 1.0
primes = list(primerange(2, EMAX + 1))
pi = 0
total = 0.0
dec = {}
for e in range(3, EMAX + 1, 4):
    while pi < len(primes) and primes[pi] < e:
        l = primes[pi]; pi += 1
        new = dist * (1 - 1 / l)               # v = 0
        for v in range(1, 80):
            pv = l ** (-v) * (1 - 1 / l)
            if pv < 1e-18:
                break
            sh = int(round(math.log(2 * v + 1) / H))
            new[sh:] += dist[:NB - sh] * pv
        dist = new
    thr = math.log(totient(e) / 6.0)
    k = max(0, int(math.ceil(thr / H - 1e-9)))
    pe = float(dist[k:].sum()) if k < NB else 0.0
    total += pe
    d = int(math.log10(e))
    dec[d] = dec.get(d, 0.0) + pe
for d in sorted(dec):
    print(f"e in [1e{d},1e{d+1}): sum P = {dec[d]:.4f}")
print(f"total over e <= {EMAX} (one type): {total:.4f}")
