"""Input lists for the z53 HYPKLOOST falsifiers (F1, F3). Writes p12/p10/sq12/sq10/ns12/rn12/rn10 .txt into argv[1].
p12/p10: 3000 consecutive primes after 1e12 / 1e10; sq12/sq10: 600 odd squares m^2, m = 10^6+1, 10^6+3, ... (resp. 10^5+1, ...);
ns12: 600 primes m^2+k, m = 10^6+1, 10^6+2, ..., first k in (1,4,8,12,16,20,24,28,36,40) with m^2+k = 1 mod 4 prime (one per m, m skipped if none);
rn12/rn10: 1500 random n = 10^12 + 4r + 1, r < 10^8 (resp. 10^10 + 4r + 1, r < 10^6), Python random.seed(53), rn12 drawn first.
The n actually used are also preserved as column 1 of data/z53/hypkloost/c_<set>.tsv.gz.
Usage: uv run --with sympy python scripts/z53_hypkloost_inputs.py /tmp/hk
"""
import sys, random
from sympy import nextprime, isprime
out = sys.argv[1]
random.seed(53)
def primes_from(x, k):
    res = []; p = x
    while len(res) < k:
        p = nextprime(p); res.append(p)
    return res
def w(name, xs):
    open(f"{out}/{name}.txt", "w").write("\n".join(map(str, xs)) + "\n")
w("p12", primes_from(10**12, 3000)); w("p10", primes_from(10**10, 3000))
w("sq12", [m * m for m in range(10**6 + 1, 10**6 + 1 + 2 * 600, 2)])
w("sq10", [m * m for m in range(10**5 + 1, 10**5 + 1 + 2 * 600, 2)])
ns = []; m = 10**6
while len(ns) < 600:
    m += 1
    for k in (1, 4, 8, 12, 16, 20, 24, 28, 36, 40):
        p = m * m + k
        if p % 4 == 1 and isprime(p):
            ns.append(p); break
w("ns12", ns)
w("rn12", [10**12 + 4 * random.randrange(0, 10**8) + 1 for _ in range(1500)])
w("rn10", [10**10 + 4 * random.randrange(0, 10**6) + 1 for _ in range(1500)])
