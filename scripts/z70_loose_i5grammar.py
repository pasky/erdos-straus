# z70 LOOSE I5 round 2: grammar search over priority gluings of partial involutions (Z70_LOOSE.md §3.3, pre-registered).
import sys, itertools
sys.path.insert(0, 'scripts')
from z70_loose_i5 import words, cert, swap, tau_xy, tau_yz, rho

def mu(w, n):
    x, y, z = w
    if y == 1 and x >= 2 and z >= 2: return (1, x, z - 1)
    if x == 1 and y >= 2: return (y, 1, z + 1)
    return None

def parts(n):
    rC, rL, rR = rho('C', n), rho('L', n), rho('R', n)
    return {'txy': lambda w: tau_xy(w, n), 'tyz': lambda w: tau_yz(w, n), 'mu': lambda w: mu(w, n),
            'mus': lambda w: (lambda t: swap(t) if t else None)(mu(swap(w), n)),
            'rL': rL, 'rR': rR, 'rC': rC, 'srC': lambda w: swap(rC(w))}

def build(seq, P):
    def f(w):
        for nm in seq:
            t = P[nm](w)
            if t is not None: return t
        return swap(w)
    return f

def evaluate(seq, n, cache):
    if n not in cache:
        T = words(n); cache[n] = (T, set(T), parts(n))
    T, S, P = cache[n]
    f = build(seq, P)
    img = {}
    for w in T:
        v = f(w)
        if v not in S: return 'notinT', None
        img[w] = v
    if any(img[img[w]] != w for w in T): return 'notinv', None
    if all(img[w] == swap(w) for w in T): return 'isswap', None
    fix = [w for w in T if img[w] == w]
    bad = [w for w in fix if not cert(w)]
    return ('ok' if not bad else 'badfix'), (len(fix), bad[:3])

if __name__ == '__main__':
    names = ['txy', 'tyz', 'mu', 'mus', 'rL', 'rR', 'rC', 'srC']
    cache = {}; tally = {}; surv1 = []
    seqs = [s for k in (1, 2, 3) for s in itertools.permutations(names, k)]
    for seq in seqs:
        r73 = evaluate(seq, 73, cache); r409 = evaluate(seq, 409, cache)
        key = (r73[0], r409[0]); tally[key] = tally.get(key, 0) + 1
        if r73[0] == 'ok' and r409[0] == 'ok': surv1.append(seq)
    print('maps tested:', len(seqs))
    for k, v in sorted(tally.items(), key=lambda t: -t[1]): print('  (73, 409) outcome', k, ':', v)
    print('stage-1 survivors:', surv1)
    from sympy import primerange
    for seq in surv1:
        fails = [p for p in primerange(5, 2000) if p % 4 == 1 and evaluate(seq, p, cache)[0] != 'ok']
        sq = [evaluate(seq, m, cache)[0] for m in (9, 105)]
        print('  stage 2', seq, 'prime failures (<2000):', len(fails), fails[:10], ' at 9, 105:', sq)
