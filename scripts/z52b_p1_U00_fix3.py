# z52b pass1 U00 fix (3): batch of small precise checks (see BRAINSTORM/z52b_pass1_U00.md for the list).
import sys, json, math, random
sys.path.insert(0, 'scripts')
from z52b_p1_U00_solver import solutions
from sympy import primerange, factorint, isprime, legendre_symbol, totient
import numpy as np
out = {}
# Z0351: e-slice success at p (p ≡ 1 mod 4, e ≡ 3 mod 4): N_e=(p+e)/4, M=p·N_e; success iff e/M = 1/y+1/z solvable,
# i.e. ∃ d | M², d ≡ −M (mod e), M²/d ≡ −M (mod e). (Because 4/p = 1/N_e + e/(p N_e).)
from cypari2 import Pari
pari = Pari(); pari.allocatemem(10**9)
def divs_sq(M):
    f = pari.factor(M); ds = [1]
    for i in range(len(f[0])):
        q, e = int(f[0][i]), int(f[1][i]); ds = [d * q ** k for d in ds for k in range(2 * e + 1)]
    return ds
def eslice_ok(p, e):
    M = p * ((p + e) // 4)
    for d in divs_sq(M):
        if (d + M) % e == 0 and ((M * M // d) + M) % e == 0: return True
    return False
ES = [3, 7, 11, 15, 19]
P = [q for q in primerange(5, 200000) if q % 4 == 1]
fail = {e: [] for e in ES}
for p in P:
    for e in ES:
        if not eslice_ok(p, e): fail[e].append(p)
nP = len(P)
dens = {e: len(fail[e]) / nP for e in ES}
joint = {}
for i, e in enumerate(ES):
    for f in ES[i + 1:]:
        sf = set(fail[e]); sg = set(fail[f])
        pe, pf = dens[e], dens[f]; pj = len(sf & sg) / nP
        joint[f'{e},{f}'] = round(pj / (pe * pf), 3) if pe * pf > 0 else None
out['Z0351'] = {'n_primes': nP, 'fail_density': {e: round(dens[e], 4) for e in ES}, 'joint_ratio_P(both fail)/(P P)': joint,
                'fail_all_five': sum(1 for p in P if all(p in set(fail[e]) for e in ES)),
                'note': 'p ≡ 2 mod 3 has 3 | 4p+1 (trivial e=3 witness); joint ratios >1 indicate shared failures'}
# Z0709: greedy failure: x0 = ceil(n/4); greedy FAILS at n if 4/n - 1/x0 has no 2-term representation with denominators >= x0.
def two_term(num, den, lo):
    # any y,z ≥ lo with 1/y+1/z = num/den ?
    if num <= 0: return False
    b = den; a = num
    f = pari.factor(b * b); ds = [1]
    for i in range(len(f[0])):
        q, e = int(f[0][i]), int(f[1][i]); ds = [d * q ** k for d in ds for k in range(e + 1)]
    for d in ds:
        if (d + b) % a: continue
        dp = b * b // d
        if (dp + b) % a: continue
        y = (b + d) // a; z = (b + dp) // a
        if min(y, z) >= lo: return True
    return False
fails = []
for n in range(5, 100001, 4):
    x0 = (n + 3) // 4
    num = 4 * x0 - n; den = n * x0
    if num <= 0: continue
    if not two_term(num, den, x0): fails.append(n)
comp = [n for n in fails if not isprime(n) and int(round(n ** .5)) ** 2 != n]
closed = 0; tested = 0; examples = []
fs = set(fails)
for n in comp:
    fac = factorint(n); ps = list(fac)
    if len(ps) == 2 and fac[ps[0]] == 1 and fac[ps[1]] == 1:
        tested += 1
        if ps[0] in fs and ps[1] in fs: closed += 1
        elif len(examples) < 10: examples.append((n, ps))
out['Z0709'] = {'n_range': '5..1e5 (n ≡ 1 mod 4)', 'greedy_fail_count': len(fails), 'fails_first': fails[:25],
                'nonsquare_composite_fails': len(comp), 'squarefree_semiprime_fails_with_both_factors_failing': f'{closed}/{tested}',
                'semiprime_fail_examples_nonclosed': examples}
json.dump(out, open('data/z52b/pass1/U00/fix3.json', 'w'), indent=1, default=str)
print(json.dumps(out, default=str)[:3000])
