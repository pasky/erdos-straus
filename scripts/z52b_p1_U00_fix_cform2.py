# z52b pass1 U00 fix (second part): (a) Z0852 conditioned on p mod 24 (is the witness-correlation a class effect?);
# (b) Z1627 comparison: obs/exp for R-zero primes 409, 577, 5569, 9601 vs typical primes; (c) Z1715: Gross–Zagier inertness
# of prime factors of H_{-4p}(0), and whether those factors are themselves C-form witnesses for 4Cp+1 (q ≡ -1 mod 4C, q | 4Cp+1).
import cypari2, json
import numpy as np
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
def divisors_of(N):
    f = pari.factor(N)
    ds = [1]
    for i in range(len(f[0])):
        p_, e = int(f[0][i]), int(f[1][i])
        ds = [d * p_ ** k for d in ds for k in range(e + 1)]
    return ds
def phi(m): return int(pari.eulerphi(m))
def obs_exp(p, Cmax):
    o = 0; e = 0.0
    for C in range(1, Cmax + 1):
        N = 4 * C * p + 1; ds = divisors_of(N)
        o += sum(1 for a in ds if 1 < a < N and a % (4 * C) == 4 * C - 1); e += (len(ds) - 2) / phi(4 * C)
    return o, round(e, 2)
out = {}
# (b)
out['Z1627_compare_Cmax6000'] = {str(p): obs_exp(p, 6000) for p in [409, 577, 5569, 9601, 401, 433, 1009, 10009, 10037, 100013]}
# (a) Z0852 class effect: fraction of levels C ≤ 50 witnessed, grouped by p mod 24 (and independence check within class)
primes = [int(q) for q in pari('primes([5,20000])') if int(q) % 4 == 1]
W = {}
for p in primes:
    W[p] = [any(a % (4 * C) == 4 * C - 1 for a in divisors_of(4 * C * p + 1) if 1 < a < 4 * C * p + 1) for C in range(1, 51)]
res = {}
for r in [1, 5, 13, 17]:
    ps = [p for p in primes if p % 24 == r] if False else [p for p in primes if p % 24 == r]
    if not ps: continue
    M = np.array([W[p] for p in ps])
    q = 1 - M.mean(axis=0)
    cf = np.array([next((C for C in range(1, 51) if M[i, C - 1]), 99) for i in range(len(ps))])
    row = []
    for c in [2, 5, 10, 20]:
        emp = float((cf > c).mean()); prod = float(np.prod(q[:c]))
        row.append({'c': c, 'emp': round(emp, 4), 'prod': round(prod, 4), 'ratio': round(emp / prod, 3) if prod > 0 else None})
    res[str(r)] = {'n_primes': len(ps), 'table': row}
out['Z0852_by_p_mod24'] = res
# Z0852 whole sample for reference is in fix_cform.json
# (c) Gross–Zagier inertness and C-form witness status of the factors of H_{-4p}(0)
rows = []
for p in [q for q in primes if q <= 300]:
    D = -4 * p
    H = int(pari('subst(polclass(%d),x,0)' % D))
    if H == 0: continue
    f = pari.factor(abs(H))
    fs = [int(f[0][i]) for i in range(len(f[0]))]
    info = []
    for q in fs:
        k4p = int(pari('kronecker(%d,%d)' % (D, q))); k3 = int(pari('kronecker(-3,%d)' % q))
        wit = None
        if q % 4 == 3:  # q is itself a C-form witness at level C = (q+1)/4 / d for C with 4C | q+1 and q | 4Cp+1
            Cs = [C for C in range(1, (q + 1) // 4 + 1) if (q + 1) % (4 * C) == 0 and (4 * C * p + 1) % q == 0]
            wit = Cs[:3]
        info.append({'q': q, 'kron(-4p/q)': k4p, 'kron(-3/q)': k3, 'q_is_Cform_witness_C': wit})
    rows.append({'p': p, 'factors': info})
inert_both = sum(1 for r in rows for i in r['factors'] if i['q'] not in (2, 3, r['p']) and i['kron(-4p/q)'] == -1 and i['kron(-3/q)'] == -1)
other = [(r['p'], i['q'], i['kron(-4p/q)'], i['kron(-3/q)']) for r in rows for i in r['factors'] if i['q'] not in (2, 3, r['p']) and not (i['kron(-4p/q)'] == -1 and i['kron(-3/q)'] == -1)]
wit_cnt = sum(1 for r in rows for i in r['factors'] if i['q_is_Cform_witness_C'])
tot = sum(1 for r in rows for i in r['factors'] if i['q'] % 4 == 3)
out['Z1715'] = {'n_p': len(rows), 'factors_not_2_3_p_inert_both': inert_both, 'exceptions_first': other[:10],
                'q≡3(4)_factors': tot, 'of_which_are_Cform_witnesses_for_their_p': wit_cnt, 'examples': rows[:5]}
json.dump(out, open('data/z52b/pass1/U00/fix_cform2.json', 'w'), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)[:4000])
