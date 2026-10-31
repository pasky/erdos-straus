"""Pass-1 U04 quick checks (Z0866, Z0785, Z0721). Reads repo data only; memory-bounded."""
import json, math
from sympy import primerange, factorint, isprime
ulimit_note = "run under ulimit -v 4000000"
V = json.load(open('data/z52b/variants.json'))
H = json.load(open('data/z52b/hard_profile.json'))
out = {}
# Z0866: primitive-solution failure primes (repo list, p<=1e5)
prim = V['primitive gcd=1']
fails = prim['fail_primes_head'] + prim['fail_primes_tail']  # head/tail only
allfail = V['primitive gcd=1'].get('fail_primes', None)
out['Z0866_n_fail_listed'] = prim['n_fail_primes']
out['Z0866_head_tail_mod12'] = {r: sum(1 for p in fails if p % 12 == r) for r in (1, 5, 7, 11)}
out['Z0866_head_tail_mod_4'] = {r: sum(1 for p in fails if p % 4 == r) for r in (1, 3)}
out['Z0866_head_tail_all_1mod12'] = all(p % 12 == 1 for p in fails)
# Z0785 Neumann-Setzer: p = u^2 + 64 (u odd) among hard primes vs all p = 1 mod 4 primes
hard = [int(k) for k in H.keys()]
def is_nsq(p):
    m = p - 64
    return m > 0 and math.isqrt(m) ** 2 == m
hits = [p for p in hard if is_nsq(p)]
out['Z0785_hard_n'] = len(hard)
out['Z0785_hard_hits'] = hits
base = [p for p in primerange(101, 100001) if p % 4 == 1]
bh = [p for p in base if is_nsq(p)]
out['Z0785_base_n'] = len(base)
out['Z0785_base_hits'] = len(bh)
out['Z0785_base_rate'] = len(bh) / len(base)
out['Z0785_hard_rate'] = len(hits) / len(hard)
# Z0721: p-1 factorisation of hard primes (claim: 2^4*3*5^2 or 2^4*3*5*7 type)
out['Z0721_p_minus_1'] = {p: factorint(p - 1) for p in [2521, 1201, 3361, 20521, 21841, 4201, 14401, 9601]}
out['Z0721_v2_of_p_minus_1'] = {p: factorint(p - 1).get(2, 0) for p in [2521, 1201, 3361, 20521, 21841, 4201, 14401, 9601]}
print(json.dumps(out, indent=1, default=str))
json.dump(out, open('data/z52b/pass1/U04/quick_checks.json', 'w'), indent=1, default=str)
