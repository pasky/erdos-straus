# z50 ajopus: squarefree-kernel distribution of chain survivors (section 7.3).
# Usage: DUMP files produced by `chain N mode seed Lmax` with env DUMP=<file>; run with
#   uv run --with sympy python3 scripts/z50_ajopus_cores.py N survU.txt survR.txt
import sys, random
from sympy import factorint
def core(n):
    c = 1
    for p, e in factorint(n).items():
        if e % 2: c *= p
    return c
N = int(sys.argv[1]); Ks = [1, 100, 10**4, 10**6]
def report(name, xs):
    random.seed(1); s = random.sample(xs, min(len(xs), 20000)); cs = [core(n) for n in s]
    print(name, len(xs), ' '.join('K=%d:%.4f' % (K, sum(c <= K for c in cs)/len(cs)) for K in Ks))
for f in sys.argv[2:]:
    report(f, [int(x) for x in open(f)])
random.seed(2); report('baseline', [8*random.randrange(N//8)+1 for _ in range(20000)])
