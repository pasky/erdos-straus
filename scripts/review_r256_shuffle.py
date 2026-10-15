"""R256 from-scratch conditional permutation test for m0(p) (s7_window_lottery 'independence test').

For primes p = 1 (4) <= N and windows m = 3 (4), m <= MW: K_m = (p+m)/4 = S*R (S: primes <= B).  Groups: (block of BS
consecutive primes, m, R mod m, bit length of R).  Permute the R's (with their factorisations) inside groups; recompute
m0' = least firing window.  Report tails #(m0 > M) actual vs shuffled, and a cruder 'm-only' shuffle (groups (block, m)
only, breaking R mod m) as a sensitivity control.
usage: review_r256_shuffle.py N B reps seed
"""
import random, sys
from collections import defaultdict
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from review_r256_m0 import spf_sieve, factor, primes_upto

N, B, reps, seed = map(int, sys.argv[1:5])
MW, BS = 51, 2000
TAILS = [3, 7, 11, 19, 27, 35, 47]
spf = spf_sieve(N//4 + MW + 10)
ps = [p for p in primes_upto(N) if p % 4 == 1]
WINS = list(range(3, MW + 1, 4))


def resset(fac, m):
    res = {1 % m}
    for q, e in fac:
        pw = [pow(q, j, m) for j in range(2*e + 1)]
        res = {(x*w) % m for x in res for w in pw}
    return res


S_res, R_fac, Kmod, keys = {}, {}, {}, {}
for i, p in enumerate(ps):
    for m in WINS:
        K = (p + m)//4
        f = factor(K, spf)
        S = tuple((q, e) for q, e in f.items() if q <= B)
        Rf = tuple((q, e) for q, e in f.items() if q > B)
        R = 1
        for q, e in Rf:
            R *= q**e
        S_res[i, m] = resset(S, m)
        R_fac[i, m] = Rf
        Kmod[i, m] = (-K) % m
        keys[i, m] = (i//BS, m, R % m, R.bit_length())


def m0_of(i, Rf_of):
    for m in WINS:
        t = Kmod[i, m]
        rs = resset(Rf_of(i, m), m)
        if any((s*r) % m == t for s in S_res[i, m] for r in rs):
            return m
    return 10**9


def tails(vals):
    return [sum(1 for v in vals if v > M) for M in TAILS]


actual = [m0_of(i, lambda i, m: R_fac[i, m]) for i in range(len(ps))]
print('N', N, 'B', B, 'primes', len(ps), 'tails M=', TAILS)
print('actual  ', tails(actual))
rng = random.Random(seed)
for mode in (('full', 'm-only') if reps < 10 else ('full',)):
    for rep in range(reps):
        groups = defaultdict(list)
        for (i, m), k in keys.items():
            groups[k if mode == 'full' else k[:2]].append(i)
        perm = {}
        for k, members in groups.items():
            sh = members[:]
            rng.shuffle(sh)
            for a, b in zip(members, sh):
                perm[a, k[1]] = b
        sv = [m0_of(i, lambda i, m: R_fac[perm[i, m], m]) for i in range(len(ps))]
        print(f'{mode:7s} rep{rep}', tails(sv))
