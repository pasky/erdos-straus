"""Bounded, exact Lucas/ES intersection experiment (no large Lucas integers).
Run: ulimit -v 8000000; timeout 180 uv run python scripts/z45_recent_pointwise_tools_scan.py
All factorizations here are small; each is reconstructed and its primes checked.
"""
import json
from math import gcd, isqrt
from pathlib import Path
from sympy import factorint, isprime, primerange, divisors, totient

OUT = Path('data/z45_recent_pointwise_tools')

def factors(n):
    fs = {int(q): int(e) for q, e in factorint(n).items()}
    product = 1
    for q, e in fs.items():
        assert isprime(q)
        product *= q ** e
    assert product == n
    return fs

def umod(t, P, Q, ell):
    # O(t) time, O(1) space, t <= 256 in trace experiments.
    a, b = 0, 1
    for _ in range(t):
        a, b = b, (P * b - Q * a) % ell
    return a

def rank_exact(t, P, Q, ell):
    if (Q * (P * P - 4 * Q)) % ell == 0:
        return False
    return umod(t, P, Q, ell) == 0 and all(
        umod(t // q, P, Q, ell) != 0 for q in factorint(t)
    )

def scan(p, cap=64):
    out = {'p': p, 'cap': cap, 'divisor_levels': 0, 'prime_levels': 0,
           'trace1_levels': 0, 'trace15_levels': 0, 'trace15_bhv_levels': 0, 'examples': []}
    for C in range(1, min(cap, (p + 2) // 4) + 1):
        t, N = 4 * C, 4 * C * p + 1
        fs = factors(N)
        ds = [int(d) for d in divisors(N) if d % t == t - 1]
        ps = [ell for ell in fs if ell % t == t - 1]
        out['divisor_levels'] += bool(ds)
        out['prime_levels'] += bool(ps)
        hits = []
        for P in range(1, 16, 2):
            Q = (P * P - p) // 4
            if gcd(P, Q) != 1 or Q == 0:
                continue
            for ell in ps:
                assert pow(p % ell, (ell - 1) // 2, ell) == ell - 1
                if rank_exact(t, P, Q, ell):
                    hits.append([C, ell, P, Q])
        out['trace1_levels'] += any(h[2] == 1 for h in hits)
        out['trace15_levels'] += bool(hits)
        out['trace15_bhv_levels'] += bool(hits) and t > 30
        if hits and len(out['examples']) < 3:
            out['examples'].append(hits[0])
    return out

small = [scan(int(p)) for p in primerange(5, 1001) if p % 4 == 1]
selected = [scan(p) for p in [193, 409, 577, 2521, 3361, 5569, 9601, 23929,
                            66529, 83449, 102001, 329617, 712321, 5101441, 8813281]]
# Full (star) census only below 1001; the C bound is proved in the memo.
full_fail = []
for row in small:
    p = row['p']
    if not any(any(int(d) % (4*C) == 4*C-1 for d in divisors(4*C*p+1))
               for C in range(1, (p+2)//4+1)):
        full_fail.append(p)
# Enumerate every trace residue for selected small certificate factors.
toy = []
for p in [5, 13, 17, 41, 73, 97, 193]:
    for C in range(1, 9):
        t = 4*C
        for ell in factors(t*p+1):
            if ell % t != t-1 or ell > 2000:
                continue
            # Q modulo ell from (P^2-p)/4; lift trace to an odd integer.
            good = []
            for residue in range(ell):
                P = residue if residue % 2 else residue + ell
                Q = (P*P-p)//4
                if rank_exact(t, P, Q, ell):
                    good.append(residue)
            # Independent engine: enumerate primitive elements of the norm-one
            # torus in F_ell[s]/(s^2-p), rather than Lucas recurrence.
            def mul(x, y):
                return ((x[0]*y[0]+p*x[1]*y[1]) % ell,
                        (x[0]*y[1]+x[1]*y[0]) % ell)
            torus_good = []
            for residue in range(ell):
                inv = pow((residue*residue-p) % ell, -1, ell)
                z = ((residue*residue+p)*inv % ell, 2*residue*inv % ell)
                power, order = (1, 0), None
                for j in range(1, t+1):
                    power = mul(power, z)
                    if power == (1, 0):
                        order = j
                        break
                if order == t:
                    torus_good.append(residue)
            assert good == torus_good
            assert len(good) == int(totient(t)), (p, C, ell, good)
            toy.append({'p': p, 'C': C, 'ell': ell, 'count': len(good),
                        'phi_t': int(totient(t)), 'first_traces': good[:8]})
# Direct Pasten embedding and numerator-8 controls: no class -1 divisors.
pasten = []
for p in [5, 13, 97, 193, 409]:
    for k in [1, 2, 3]:
        C = p*k*k
        N = 4*C*p+1
        fs = factors(N)
        assert all(ell % 4 == 1 for ell in fs)
        pasten.append([p, k, C, N, fs])
controls = []
for n in [9, 25, 49, 81, 121, 169, 289, 529]:
    hits = sum(any(int(d) % (4*C) == 4*C-1 for d in divisors(4*C*n+1))
               for C in range(1, (n+2)//4+1))
    assert hits == 0
    controls.append([4, n, hits])
for n in [11, 17, 131, 241]:
    hits = sum(any(int(d) % (8*C) == 8*C-1 for d in divisors(8*C*n+1))
               for C in range(1, (n+2)//8+1))
    assert hits == 0
    controls.append([8, n, hits])
# Identify near-square and Mordell-hard subset outcomes, not asymptotics.
summary = {'sample_size': len(small), 'complete_star_failures_below_1001': full_fail}
for key in ['divisor_levels', 'prime_levels', 'trace1_levels', 'trace15_levels']:
    summary[key] = {'primes_with_hit': sum(r[key] > 0 for r in small),
                    'total_levels': sum(r[key] for r in small)}
summary['trace15_bhv_primes'] = sum(r['trace15_bhv_levels'] > 0 for r in small)
summary['hard_sample'] = [scan(int(p)) for p in primerange(1001, 20001)
                          if p % 840 in [1,121,169,289,361,529]][:30]
summary['near_square_sample'] = [dict(scan(int(p)), signed_gap=int(p)-m*m)
    for p in primerange(1001, 20001) if p % 4 == 1
    for m in [isqrt(p), isqrt(p)+1] if 0 < abs(p-m*m) <= 4]
summary['toy_cases'] = len(toy)
summary['toy_traces_tested'] = sum(r['ell'] for r in toy)
summary['selected'] = selected
summary['mordell_hard_small'] = [r for r in small if r['p'] % 840 in [1,121,169,289,361,529]]
summary['near_square_small'] = [dict(r, gap=r['p']-isqrt(r['p'])**2)
                                for r in small if r['p']-isqrt(r['p'])**2 <= 4]
OUT.mkdir(exist_ok=True)
(OUT/'scan.json').write_text(json.dumps({'summary': summary, 'small': small,
    'toy': toy, 'pasten': pasten, 'controls': controls}, indent=2)+'\n')
print(json.dumps(summary, indent=2))
