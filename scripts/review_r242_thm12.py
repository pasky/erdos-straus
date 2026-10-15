"""R242: independent check of CAP_DOWN Thm 1.2 / Prop 1.3 / Prop 4.1(a) and the §1 statistics.
Usage: review_r242_thm12.py N QMAX mode scope
  mode = primes | all (non-square n = 1 (4), all prime factors = 1 (4));  scope = least | allq
  least: only at the least forced window q_new(n) (plus q_old = least q with K odd, for statistics);
  allq : every prime q = 3 (4), q <= QMAX, q not | n, (q/n) = -1.
For each tested (n, q): classify (E); if (E): verify -K' is a square of an element of H = <odd primes of K> mod q
(Thm 1.2 shape), build the Prop 1.3 witness d = K s^{o/2} (min cap over admissible s), check Def 1.1 exactly,
4e <= q-3, and compute the exhaustive least Lemma-1.1 cap at q (must be <= the Prop 1.3 cap).
If excluded: record whether ANY Lemma-1.1 divisor (any cap) exists ('fires') or not ('dead').
"""
import sys
from math import isqrt
from fractions import Fraction
from review_r242_common import spf_sieve, factor, jacobi, order, vp, check_def11

N, QMAX, MODE, SCOPE = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
spf = spf_sieve(N + QMAX + 4)
QP = [q for q in range(3, QMAX + 1, 4) if spf[q] == q]


def closure(gens, q):
    H = {1}
    frontier = [1]
    while frontier:
        nf = []
        for h in frontier:
            for g in gens:
                x = h * g % q
                if x not in H:
                    H.add(x)
                    nf.append(x)
        frontier = nf
    return H


def reach(fk, q, e):
    """residues of Lemma-1.1 divisors at cap e (e = None: any cap)."""
    R = {1}
    for s, b in fk.items():
        if s == 2:
            cs = range(0, 2 * b + 1)
        else:
            top = 2 * b + 2 * e if e is not None else 2 * b + 2 * q
            cs = set(range(0, 2 * b + 1)) | set(range(0, top + 1, 2))
        P = {pow(s, c, q) for c in cs}
        R = {r * p % q for r in R for p in P}
    return R


def test(n, q, stats):
    K = (n + q) // 4
    fk = factor(K, spf)
    t = fk.get(2, 0)
    Kp = K >> t
    assert all(n % s for s in fk) and K % q
    assert jacobi(K, q) == -1
    E = (q % 8 == 7) or (t % 2 == 0)
    excl_stmt = (n % 8 == 5 and q % 8 == 3 and t % 2 == 1)
    assert E == (not excl_stmt)
    if not E:
        fires = (-K) % q in reach(fk, q, None)
        stats['excl_fires' if fires else 'excl_dead'] += 1
        return None
    stats['E'] += 1
    assert jacobi(Kp, q) == -1
    H = closure([s for s in fk if s != 2], q)
    assert (-Kp) % q in {h * h % q for h in H}, 'Thm 1.2 shape fails'
    best = None
    for s, b in fk.items():
        if s == 2 or b % 2 == 0 or jacobi(s, q) != -1:
            continue
        o = order(s, q)
        assert o % 4 == 2 and pow(s, o // 2, q) == q - 1
        e = max(0, (o // 2 - b) // 2)
        if best is None or e < best[0]:
            best = (e, s, o)
    assert best is not None
    e, s, o = best
    d = K * s ** (o // 2)
    assert (K + d) % q == 0
    A = (K + d) // q
    cap = check_def11(n, K, n * A, Fraction(n * K * A, d), e, list(fk))
    assert cap == e and 4 * e <= q - 3
    ex = 0
    while (-K) % q not in reach(fk, q, ex):
        ex += 1
    assert ex <= e
    return e, ex


def relevant(n):
    if isqrt(n) ** 2 == n:
        return False
    f = factor(n, spf)
    if MODE == 'primes':
        return f == {n: 1}
    return all(p % 4 == 1 for p in f)


stats = {'E': 0, 'excl_fires': 0, 'excl_dead': 0, 'n': 0}
cls = {1: {'cnt': 0, 'sold': 0, 'snew': 0, 'firstexcl': 0, 'max_new': (0, 0), 'max_old': (0, 0),
           'max_prop': (0, 0), 'max_best': (0, 0)}}
cls[5] = {k: (v if not isinstance(v, tuple) else (0, 0)) for k, v in cls[1].items()}
dead_examples = []
for n in range(5, N + 1, 4):
    if not relevant(n):
        continue
    stats['n'] += 1
    qs = [q for q in QP if n % q and jacobi(q, n) == -1]
    if SCOPE == 'allq':
        for q in qs:
            before = stats['excl_dead']
            test(n, q, stats)
            if stats['excl_dead'] > before and len(dead_examples) < 5:
                dead_examples.append((n, q))
        continue
    qnew = next(q for q in qs if q % 8 == 7 or vp(n + q, 2) % 2 == 0)
    qold = next(q for q in qs if (n + q) % 8 == 4)
    e, ex = test(n, qnew, stats)
    c = cls[n % 8]
    c['cnt'] += 1
    c['sold'] += qold
    c['snew'] += qnew
    c['firstexcl'] += (qs[0] != qnew)
    c['max_new'] = max(c['max_new'], (qnew, n))
    c['max_old'] = max(c['max_old'], (qold, n))
    c['max_prop'] = max(c['max_prop'], (e, n))
    c['max_best'] = max(c['max_best'], (ex, n))
print('N', N, 'QMAX', QMAX, MODE, SCOPE, stats)
if SCOPE == 'allq':
    print('dead excluded examples (n, q):', dead_examples)
else:
    for r in (1, 5):
        c = cls[r]
        print('n = %d (8):' % r, c, 'mean qold %.2f qnew %.2f' % (c['sold'] / c['cnt'], c['snew'] / c['cnt']))
