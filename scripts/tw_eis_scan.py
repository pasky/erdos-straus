"""O182 §3 scan: primes vs cubes for a twisted Eisenstein target. usage: tw_eis_scan.py t c1 c2 c3 B [norm2 0/1]"""
import sys, time
from collections import Counter
import tw_eis as E, tw_eis_solve as S

t = S.parse(sys.argv[1]); cs = [S.parse(s) for s in sys.argv[2:5]]; B = int(sys.argv[5])
norm2 = len(sys.argv) <= 6 or sys.argv[6] == '1'


def assoc1(pi):  # associate = 1 mod 2
    for u in E.UNITS:
        x = E.mul(u, pi)
        if (x[0] % 2, x[1] % 2) == (1, 0):
            return x


def isprime(p): return p > 1 and all(p % d for d in range(2, int(p ** 0.5) + 1))


split = [p for p in range(7, 2600) if isprime(p) and p % 3 == 1]
cubes = [assoc1(E.split_prime(p)[0]) for p in split[:5]]
primes = [assoc1(E.split_prime(p)[0]) for p in split if 300 < p < 2600][::12][:8]
for label, lst, e in (('prime', primes, 1), ('cube', cubes, 3)):
    tot = Counter()
    for pi in lst:
        t0 = time.time()
        sols, st = S.run(t, cs, pi, e, B, norm2=norm2, verbose=False)
        shp = Counter()
        for k, v in st.items():
            shp[k[0]] += v
            tot[k] += v
        print(label, pi, 'N(n)=', E.norm(E.power(pi, e)), dict(shp), f'{time.time()-t0:.0f}s', flush=True)
    for k, v in sorted(tot.items(), key=str):
        print('  ', label, '(shape, inv_2, inv_pi, sum_tame, #other!=0)', k, v)
