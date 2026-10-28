#!/usr/bin/env python3
"""Independent check of Lemma 2's encoding on actual primes p ≡ 1 (mod 840):
forest-on-[1,H] edges (brute: uv | p+u+v) == congruence events E_(a,v) that p hits;
avoidance of C_(A,d) (A<=H) <=> no G_A hit for A<=H is implied; count survivors."""
import json, sys
from math import gcd
from sympy import isprime, jacobi_symbol
H = int(sys.argv[1]); N = int(sys.argv[2])
mism = 0; tested = 0; surv = []; cov_imp_fail = 0
for p in range(841, N, 840):
    if not isprime(p): continue
    tested += 1
    edges = {(u, v) for v in range(2, H+1) for u in range(1, v) if (p+u+v) % (u*v) == 0}
    events = {(a, v) for v in range(2, H+1) for a in range(1, v) if gcd(a, v) == 1 and (p + a + v) % (a*v) == 0}
    if edges != events: mism += 1
    covhit = [(A, d) for A in range(2, H+1) for d in range(1, A) if (A+1) % d == 0 and (p + d) % A == 0 and (A, d) not in ((2,1),(3,2))]
    Ghit = []
    for A in range(2, H+1):
        Ao = A
        while Ao % 2 == 0: Ao //= 2
        for d in range(1, A):
            if (A+1) % d == 0 and (p+d) % A == 0 and Ao > 1 and jacobi_symbol(-d % Ao, Ao) == -1:
                Ghit.append((A, d))
    if not covhit and Ghit: cov_imp_fail += 1
    if edges == {(1,2),(2,3)} and not covhit: surv.append(p)
print(json.dumps({'H': H, 'N': N, 'primes': tested, 'edge_event_mismatch': mism, 'cover_implication_fail': cov_imp_fail, 'joint_survivors': len(surv), 'first': surv[:5]}))
