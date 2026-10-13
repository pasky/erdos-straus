"""O182 §3: TES at primes in the 'cube classes' n = +-1 mod 9 (where Type I/II identities cannot reach, by T1_3).
usage: tw_eis_hard.py B maxnorm count"""
import sys, time
from collections import Counter
import tw_eis as E, tw_eis_solve as S
B, maxnorm, count = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
t = (9, 0); cs = [(0, 1), (-1, -1), (2, 0)]


def isprime(p): return p > 1 and all(p % d for d in range(2, int(p ** 0.5) + 1))


def assoc1(pi):
    return [E.mul(u, pi) for u in E.UNITS if (E.mul(u, pi)[0] % 2, E.mul(u, pi)[1] % 2) == (1, 0)]


hard, easy = [], []
for p in range(7, maxnorm):
    if not (isprime(p) and p % 3 == 1):
        continue
    for pi0 in E.split_prime(p):
        for pi in assoc1(pi0)[:1]:
            m9 = (pi[0] % 9, pi[1] % 9)
            (hard if m9 in ((1, 0), (8, 0)) else easy).append(pi)
print('hard primes found', len(hard), 'easy', len(easy))
for label, lst in (('hard', hard[:count]), ('easy', easy[:count])):
    agg = Counter(); zero = 0
    for pi in lst:
        sols, st = S.run(t, cs, pi, 1, B, verbose=False)
        c = Counter()
        for k, v in st.items():
            c[k[0]] += v; agg[k] += v
        if c['I'] + c['II'] == 0:
            zero += 1
        print(label, pi, E.norm(pi), dict(c), flush=True)
    print(label, 'primes with no Type I/II found:', zero, '/', len(lst), dict(agg))
