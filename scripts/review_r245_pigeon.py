"""R245 from-scratch: (1) s6_divisor_pigeonhole numerics (least prime forced window, odd K) for p = 1 (4) < P;
(2) Cauchy-Davenport signed-subset-sum bound min(u, 2N+1) (N = multiplicity of NONZERO images) on random cases, u prime."""
import sys, random
from sympy import primerange, factorint, isprime, jacobi_symbol, primitive_root
P = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
tot = fire = cap0 = bad = 0
for p in primerange(5, P):
    if p % 4 != 1: continue
    q = next(q for q in primerange(3, 10**7) if q != p and q % 8 == (4 - p) % 8 and jacobi_symbol(q, p) == -1)
    K = (p + q) // 4; assert K % 2 == 1
    f = factorint(K)
    S = {1}
    for s, b in f.items():
        S = {x * pow(s, e, q) % q for x in S for e in range(b + 1)}
    tot += 1
    crit = len(S) > (q - 1) // 2
    c0 = any((-x) % q in S for x in S)  # d1 = -d2 (mod q) <=> -1 in Sigma_q(K)
    fire += crit; cap0 += c0; bad += crit and not c0
print(f'p<{P}: {tot} primes, criterion fires {fire}, cap0 {cap0}, criterion&!cap0 {bad}')
# Cauchy-Davenport check
random.seed(1)
viol = 0
for trial in range(3000):
    u = random.choice([3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
    imgs = [random.randrange(u) for _ in range(random.randint(1, 6))]
    mult = [random.randint(1, 3) for _ in imgs]
    sums = {0}
    for l, b in zip(imgs, mult):
        sums = {(x + d * l) % u for x in sums for d in range(-b, b + 1)}
    N = sum(b for l, b in zip(imgs, mult) if l % u)
    if len(sums) < min(u, 2 * N + 1): viol += 1
print('CD violations:', viol)
# q = 7, K = 3*29^N: -1 never in Sigma_7(K)
for N in range(1, 6):
    K = 3 * 29**N; S = {1}
    for s, b in factorint(K).items():
        S = {x * pow(s, e, 7) % 7 for x in S for e in range(b + 1)}
    print('q=7 K=3*29^%d' % N, 'cap0' if any((-x) % 7 in S for x in S) else 'no cap0')
