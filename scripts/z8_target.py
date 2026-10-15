# z8_target.py — targeted exponent covering for n_s = c0*4^s + k: general ET search (ec_cover) with moduli <= Mmax,
# then the residual exponents s mod L are attacked with classes of LARGE admissible prime modulus q (ord_q 4 | L,
# q <= QMAX): divisor classes D_q, II2 (a, d, f = q) [n = -4a^2 d mod q, 4ad | q+1], and II2 with f = q*g, I1 with
# 4ad = 4*q*a' (a' small admissible), all evaluated on the residual exponents only.
# Usage: PYTHONPATH=scripts uv run python scripts/z8_target.py c0 k L Mmax QMAX [out.json]
import sys, json, functools
import mordell_lib as ML
import ec_cover as EC
from ec_screen import primes_upto, admissible_prime_powers
ML.residue_table = functools.lru_cache(maxsize=20000)(ML.residue_table)

c0, k, L, Mmax, QMAX = map(int, sys.argv[1:6])
base = 10 * L + 64
rep = lambda m: base + ((m - base) % L)
nval = lambda m, M: (c0 * pow(4, rep(m), M) + k) % M

# 1. general sets (same as ec_cover.search)
sets = []
for q, Q in admissible_prime_powers(4, L, QMAX=Mmax):
    if q == 2: continue
    s = {m for m in range(L) if nval(m, q) == 0}
    if s: sets.append((q, ('D', (q,)), s))
for M in EC.candidate_moduli(c0, 4, k, L, Mmax):
    if M % 4 and M % 4 != 3: continue
    W = ML.residue_table(M)
    cov = {}
    for m in range(L):
        r = nval(m, M)
        if r in W: cov.setdefault(W[r], set()).add(m)
    for cls, s in cov.items(): sets.append((M, cls, s))
allcov = set().union(*[s for _, _, s in sets])
U = sorted(set(range(L)) - allcov)
print('general search: %d sets, residual %d exponents: %s' % (len(sets), len(U), U[:20]), flush=True)

# 2. large admissible primes
small = [q for q, Q in admissible_prime_powers(4, L, QMAX=200) if q > 2]
big = [q for q in primes_upto(QMAX) if q > 2 and pow(4, L, q) == 1 and q > 200]
print('large admissible primes:', len(big), big[:15], flush=True)
from mordell_lib import divisors
extra = []
for q in big:
    res = {m: nval(m, q) for m in U}
    s = {m for m in U if res[m] == 0}
    if s: extra.append((q, ('D', (q,)), s))
    if q % 4 == 3:
        A = (q + 1) // 4
        for a in divisors(A):
            for d in divisors(A // a):
                r = (-4 * a * a * d) % q
                s = {m for m in U if res[m] == r}
                if s: extra.append((q, ('II2', (a, d, q)), s))
    # I1 with a*d = q * t, t small admissible product (incl. powers of 2), f | 4a^2 d + 1
    for t in [1, 2, 4, 8] + small + [2 * x for x in small] + [4 * x for x in small]:
        Mq = 4 * q * t
        for a in divisors(q * t):
            d = q * t // a
            N = 4 * a * a * d + 1
            if N > 10 ** 14: continue
            for f in divisors(N):
                r = (-f) % Mq
                s = {m for m in U if nval(m, Mq) == r}
                if s: extra.append((Mq, ('I1', (a, d, f)), s))
cov2 = set().union(*[s for _, _, s in extra]) if extra else set()
U2 = sorted(set(U) - cov2)
print('after large primes: residual %d: %s' % (len(U2), U2[:20]), flush=True)
if not U2:
    unc, chosen = set(range(L)), []
    allsets = sets + extra
    while unc:
        M, cls, s = max(allsets, key=lambda t: (len(unc & t[2]), -t[0]))
        chosen.append((M, cls, sorted(s))); unc -= s
    print('COVERING with %d classes' % len(chosen))
    for M, cls, s in chosen: print('  M=%d %s %s m mod %d in %s' % (M, cls[0], cls[1], L, s[:10]))
    if len(sys.argv) > 6:
        json.dump(EC.certificate(c0, L, chosen, 4, k), open(sys.argv[6], 'w'))
