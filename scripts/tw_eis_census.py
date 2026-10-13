"""O182 §3 census: all 2-primary split primes pi (both conjugates) with 100 < N(pi) <= maxnorm, plus inert p:
count Type I/II solutions of TES(pi) in the search window B; report primes with none. usage: tw_eis_census.py B maxnorm"""
import sys
from collections import Counter
import tw_eis as E, tw_eis_solve as S
B, maxnorm = int(sys.argv[1]), int(sys.argv[2])
t = (9, 0); cs = [(0, 1), (-1, -1), (2, 0)]


def isprime(p): return p > 1 and all(p % d for d in range(2, int(p ** 0.5) + 1))


def assoc1(pi):
    return [E.mul(u, pi) for u in E.UNITS if (E.mul(u, pi)[0] % 2, E.mul(u, pi)[1] % 2) == (1, 0)][0]


ps = []
for p in range(101, maxnorm + 1):
    if isprime(p) and p % 3 == 1:
        ps += [assoc1(x) for x in E.split_prime(p)]
    if isprime(p) and p % 3 == 2 and p * p <= maxnorm and p > 2:
        ps.append((p, 0))
tot = Counter(); none = []; invs = Counter()
for pi in ps:
    sols, st = S.run(t, cs, pi, 1, B, verbose=False)
    c = Counter()
    for k, v in st.items():
        c[k[0]] += v; invs[k[1:]] += v
    tot['I'] += c['I']; tot['II'] += c['II']
    if c['I'] + c['II'] == 0:
        none.append((pi, E.norm(pi)))
print('primes', len(ps), 'TypeI', tot['I'], 'TypeII', tot['II'], 'invariant tuples', dict(invs))
print('no Type I/II in window:', len(none), none[:40])
