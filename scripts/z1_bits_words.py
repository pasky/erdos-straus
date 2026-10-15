"""z1: actual words vs the depth law. For primes p = 1 mod 4 in [P0,P1): chi=-1 words (mod reversal), share in S_8,
and the independent-bit prediction of P(S_8(p) empty) = prod (1/2 per one-iso word, 1/4 per two-iso word)."""
import sys, math
from sympy import primerange
from cf_lib import words_fast
P0, P1 = int(sys.argv[1]), int(sys.argv[2])
W4 = W8 = 0; pred = 0.0; obs = 0; rows = []
for p in primerange(P0, P1):
    if p % 4 != 1: continue
    seen = set(); lp = 0.0; any8 = False
    for (t, u, v) in words_fast(p):
        key = (t, min(u, v), max(u, v))
        if key in seen: continue
        seen.add(key)
        P = (t, u, v, t*u-1, t*v-1)
        c4 = sum(x % 4 == 0 for x in P)
        if c4 == 0: continue
        W4 += 1
        if any(x % 8 == 0 for x in P): W8 += 1; any8 = True
        lp += math.log(0.5 if c4 == 1 else 0.25)
    pe = math.exp(lp); pred += pe
    if not any8: obs += 1; rows.append((p, round(pe, 4)))
print('primes p=1 mod 4 in [%d,%d): chi=-1 words (mod reversal) %d, share in S_8 %.4f (cell law 7/12 = %.4f)' % (P0, P1, W4, W8 / W4, 7/12))
print('S_8(p) empty: observed %d, independent-bit prediction %.2f' % (obs, pred))
print('observed empties (p, predicted prob):', rows[:40])
