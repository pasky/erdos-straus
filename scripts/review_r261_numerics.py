"""R261: from-scratch spot checks of CAP_BOUNDED §5.
mode 'four': the 4 primes needing > 10 forced windows: caps at first 20 forced windows, least cap-0 window (any m).
mode 'sample NS SEED': random sample of Mordell-hard p <= 1e7 (p mod 840 in {1,121,169,289,361,529}):
   cap-0 / cap<=1 rates at the first 10 forced prime windows q = 3 (4) <= 1000 vs all unforced ones, per 100-bin;
   cap at least forced window; explicit-witness min (Prop 1.3 one-prime + Prop 2.3 odd-order) over first 10 forced.
mode 'witness p...': explicit witness for given primes.
"""
import sys, random
from collections import Counter
from sympy import primerange, jacobi_symbol, factorint, isprime
from sympy.ntheory import n_order
from review_r261_windows import least_cap, rebuild, check_def11

HARD = {1, 121, 169, 289, 361, 529}
QS = [q for q in primerange(3, 1000) if q % 4 == 3]


def forced(p):
    return [q for q in QS if p % q and jacobi_symbol(q, p) == -1]


def cap(p, q, E):
    r = least_cap(p, q, E)
    return None if r is None else r[0]


def explicit_witness(p, q):
    K = (p + q) // 4
    fac = factorint(K)
    best = None
    for s, b in fac.items():  # Prop 1.3
        if s == 2 or b % 2 == 0 or jacobi_symbol(s, q) != -1:
            continue
        o = n_order(s, q)
        c = max(0, (o // 2 - b) // 2)
        best = c if best is None else min(best, c)
    if K % 2 == 1:  # Prop 2.3
        o = n_order(p * pow(4, -1, q) % q, q)
        while o % 2 == 0:
            o //= 2
        c = (o - 1) // 2 * max(fac.values())
        best = c if best is None else min(best, c)
    return best


mode = sys.argv[1]
if mode == 'four':
    for p in [3361, 2782921, 7071121, 8925841]:
        F = forced(p)[:20]
        caps = [cap(p, q, 3) for q in F]
        i0 = next((i for i, c in enumerate(caps) if c == 0), None)
        m0 = next(m for m in range(3, 10**4, 4) if p % m and least_cap(p, m, 0))
        print(p, p % 840, 'first-10 caps', caps[:10], 'first cap-0 forced', None if i0 is None else (F[i0], i0 + 1),
              'least cap-0 window any m', m0)
elif mode == 'witness':
    for p in map(int, sys.argv[2:]):
        F = forced(p)[:10]
        print(p, [(q, explicit_witness(p, q)) for q in F], 'min', min(explicit_witness(p, q) for q in F))
else:
    NS, SEED = int(sys.argv[2]), int(sys.argv[3])
    hard = [p for p in primerange(5, 10**7) if p % 840 in HARD]
    print('hard primes <= 1e7:', len(hard))
    random.seed(SEED)
    S = random.sample(hard, NS)
    st = Counter(); least = Counter(); W = Counter()
    for p in S:
        F = forced(p)
        F10 = F[:10]
        for q in QS:
            if p % q == 0:
                continue
            if q in F10:
                kind = 'F'
            elif q in F:
                continue
            else:
                kind = 'U'
            c = cap(p, q, 1)
            b = q // 100 if q < 300 else 'hi'
            for key in [(kind, 'all'), (kind, b)]:
                st[key + ('n',)] += 1
                st[key + ('c0',)] += c == 0
                st[key + ('c1',)] += c is not None
        c = cap(p, F[0], 3)
        least[4 if c is None else c] += 1
        W[min(explicit_witness(p, q) for q in F10)] += 1
    for kind in 'FU':
        for b in ['all', 0, 1, 2]:
            n = st[(kind, b, 'n')]
            print(kind, b, 'n', n, 'cap0 %.3f' % (st[(kind, b, 'c0')] / n), 'cap<=1 %.3f' % (st[(kind, b, 'c1')] / n))
    print('cap at least forced window', sorted(least.items()))
    print('explicit witness min', sorted(W.items()))
