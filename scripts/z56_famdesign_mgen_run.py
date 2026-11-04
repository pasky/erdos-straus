# driver: exact M_gen split (G / corner K) and densities at test primes + seeded random primes p = 1 (4); writes
# data/z56/famdesign/mgen_split.tsv and prints per-scale summaries of M_G/M0_G, M_K/M0_K, M_G/L^2, M_gen/M0.
import random, subprocess, sys, statistics as st, sympy
random.seed(56)
test = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281]
def rp(lo, hi, k):
    out = set()
    while len(out) < k:
        n = random.randrange(lo, hi) | 1
        n = sympy.nextprime(n)
        while n % 4 != 1: n = sympy.nextprime(n)
        out.add(n)
    return sorted(out)
scales = {'1e6': rp(10**6, 2 * 10**6, 40), '1e7': rp(10**7, 2 * 10**7, 40), '1e8': rp(10**8, 2 * 10**8, 20),
          '1e9': rp(10**9, 2 * 10**9, int(sys.argv[1]) if len(sys.argv) > 1 else 3)}
ps = test + [p for v in scales.values() for p in v]
res = subprocess.run(['/tmp/z56mgen'], input='\n'.join(map(str, ps)), capture_output=True, text=True).stdout
rows = {int(l.split()[0]): list(map(float, l.split()[1:])) for l in res.strip().split('\n')}
with open('data/z56/famdesign/mgen_split.tsv', 'w') as f:
    f.write('p\tL2\tM0\tM0_G\tMgen\tM_G\tM_K\tM_G1/15\tM0_G1/15\tset\n')
    for p in ps:
        tag = 'test' if p in test else [k for k, v in scales.items() if p in v][0]
        f.write('\t'.join([str(p)] + ['%.5f' % x for x in rows[p]] + [tag]) + '\n')
def summ(name, pl):
    r = [rows[p] for p in pl]
    gG = [x[4] / x[2] for x in r]; gK = [x[5] / (x[1] - x[2]) for x in r]; gL = [x[4] / x[0] for x in r]; gt = [x[3] / x[1] for x in r]
    def s(v): return '%.3f±%.3f [%.3f,%.3f]' % (st.mean(v), st.pstdev(v), min(v), max(v))
    print(f'{name:5s} n={len(r):3d}  M_G/M0_G {s(gG)}  M_K/M0_K {s(gK)}  M_G/L2 {s(gL)}  Mgen/M0 {s(gt)}')
summ('test', test)
for k, v in scales.items(): summ(k, v)
