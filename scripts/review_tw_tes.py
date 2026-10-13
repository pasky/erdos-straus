"""R182 from-scratch solver for twisted Eisenstein targets  t/n = c1/x1 + c2/x2 + c3/x3  over Z[w],
x_i = 1 mod 2 (2-primary).  Window: all solutions with SOME denominator X_i satisfying
N(t X_i - c_i n) <= N(t) * B   (i.e. N(X_i - c_i n/t) <= B, exact, not rounded).
For each solution: exact verification, pi-shape, tame cubic invariants at every tame place, and an
independent brute-force lambda-adic test (norm groups) of inv_lambda = 0, plus the reciprocity cross-check.
usage: review_tw_tes.py MODE ...   (see __main__)"""
import sys, time
from collections import Counter
from itertools import product
from math import isqrt
import review_tw_zw as Z
from review_tw_zw import mul, add, sub, neg, norm, pw, divexact, conj, ONE, W, Z0


def divisors(fac):
    items = list(fac.items())
    for exps in product(*[range(k + 1) for _, k in items]):
        d = ONE
        for (p, _), e in zip(items, exps):
            d = mul(d, pw(p, e))
        yield d


def merge(*fs):
    out = {}
    for f in fs:
        for p, k in f.items(): out[p] = out.get(p, 0) + k
    return out


def solve(t, cs, n, B, wide=0):
    sols = set()
    Nt = norm(t)
    for i in range(3):
        j, k = [r for r in range(3) if r != i]
        cen = divexact(mul(cs[i], n), ONE)  # c_i n
        # X approx c_i n / t
        q = mul(cen, conj(t)); cx, cy = q[0] / Nt, q[1] / Nt
        R = isqrt(4 * B // 3 + 1) + 3
        cands = set()
        for a in range(int(cx) - R, int(cx) + R + 2):
            for b in range(int(cy) - R, int(cy) + R + 2):
                X = (a, b)
                if norm(sub(mul(t, X), cen)) <= Nt * B: cands.add(X)
        if wide:
            Rw = isqrt(4 * wide // 3) + 2
            for a in range(-Rw, Rw + 1):
                for b in range(-Rw, Rw + 1):
                    if 0 < norm((a, b)) <= wide: cands.add((a, b))
        fcj, _ = Z.factor(cs[j]); fck, _ = Z.factor(cs[k]); fn, _ = Z.factor(n)
        for X in cands:
            if not Z.is_2primary(X): continue
            E = sub(mul(t, X), cen)
            if E == Z0: continue
            M = mul(n, X)
            fX, _ = Z.factor(X)
            fac = merge(fcj, fck, {p: 2 * e for p, e in fn.items()}, {p: 2 * e for p, e in fX.items()})
            CC = mul(mul(cs[j], cs[k]), mul(M, M))
            cjM, ckM = mul(cs[j], M), mul(cs[k], M)
            for d0 in divisors(fac):
                for u in Z.UNITS:
                    d = mul(u, d0)
                    Y = divexact(add(cjM, d), E)
                    if Y is None or Y == Z0 or not Z.is_2primary(Y): continue
                    Zz = divexact(add(ckM, divexact(CC, d)), E)
                    if Zz is None or Zz == Z0 or not Z.is_2primary(Zz): continue
                    xs = [None] * 3; xs[i], xs[j], xs[k] = X, Y, Zz
                    sols.add(tuple(xs))
    return sols


def verify(t, cs, n, xs):
    # t x1 x2 x3 == n (c1 x2 x3 + c2 x1 x3 + c3 x1 x2)
    lhs = mul(t, mul(xs[0], mul(xs[1], xs[2])))
    rhs = Z0
    for i in range(3):
        p = cs[i]
        for k in range(3):
            if k != i: p = mul(p, xs[k])
        rhs = add(rhs, p)
    return lhs == mul(n, rhs)


def analyse(t, cs, pi, e, xs):
    n = pw(pi, e)
    assert verify(t, cs, n, xs)
    v = [Z.val(x, pi)[0] - Z.val(c, pi)[0] for x, c in zip(xs, cs)]
    zeros = sum(1 for a in v if a == 0); big = sum(1 for a in v if a >= e)
    shape = 'I' if (zeros == 2 and big == 1) else ('II' if (zeros == 1 and big == 2) else 'other')
    a = (neg(mul(xs[0], cs[2])), mul(cs[0], xs[2]))
    b = (neg(mul(xs[1], cs[2])), mul(cs[1], xs[2]))
    ps = Z.tame_places(a[0], a[1], b[0], b[1], n) | {(2, 0)}
    inv = {p: Z.tame3_frac(a, b, p) for p in ps}
    inv2 = inv[(2, 0)]
    pis = {p for p in ps if Z.val(n, p)[0] > 0}
    invn = sum(inv[p] for p in pis) % 3
    other = sum(1 for p in ps if p != (2, 0) and p not in pis and inv[p])
    tot = sum(inv.values()) % 3
    lt = Z.lam_trivial_frac(a, b)
    assert (tot == 0) == lt, ("reciprocity mismatch", xs)
    return (shape, inv2, invn, 0 if lt else 'nz', other)


def twoprim(pi):
    for u in Z.UNITS:
        x = mul(u, pi)
        if Z.is_2primary(x): return x


def isprime(p): return p > 1 and all(p % d for d in range(2, isqrt(p) + 1))


def run(t, cs, pi, e, B, wide=0):
    n = pw(pi, e)
    sols = solve(t, cs, n, B, wide)
    return Counter(analyse(t, cs, pi, e, xs) for xs in sols), sols


if __name__ == '__main__':
    mode = sys.argv[1]
    P = lambda s: tuple(int(x) for x in s.split(':'))
    if mode == 'table':  # table t c1 c2 c3 B
        t = P(sys.argv[2]); cs = [P(s) for s in sys.argv[3:6]]; B = int(sys.argv[6])
        split = [p for p in range(7, 2600) if isprime(p) and p % 3 == 1]
        cubes = [(twoprim(Z.split_prime(p)), 3) for p in split[:5]]
        primes = [(twoprim(Z.split_prime(p)), 1) for p in split if 300 < p < 2600][::12][:8]
        for label, lst in (('prime', primes), ('cube', cubes)):
            tot = Counter()
            for pi, e in lst:
                st, _ = run(t, cs, pi, e, B)
                tot += st
                print(label, pi, norm(pi), dict(Counter(k[0] for k in st.elements())), flush=True)
            for k, v in sorted(tot.items(), key=str): print('   ', label, k, v)
    elif mode == 'one':  # one t c1 c2 c3 pa pb e B [wide]
        t = P(sys.argv[2]); cs = [P(s) for s in sys.argv[3:6]]
        pi = twoprim((int(sys.argv[6]), int(sys.argv[7]))); e = int(sys.argv[8]); B = int(sys.argv[9])
        wide = int(sys.argv[10]) if len(sys.argv) > 10 else 0
        t0 = time.time(); st, sols = run(t, cs, pi, e, B, wide)
        print(pi, 'e=', e, 'N(pi)=', norm(pi), 'B=', B, 'wide=', wide, len(sols), 'sols', dict(st), f'{time.time()-t0:.0f}s')
    elif mode == 'inert':  # inert t c1 c2 c3 p e B
        t = P(sys.argv[2]); cs = [P(s) for s in sys.argv[3:6]]
        p = int(sys.argv[6]); e = int(sys.argv[7]); B = int(sys.argv[8])
        st, sols = run(t, cs, (p, 0), e, B)
        print('inert', p, 'e=', e, len(sols), dict(st))
    elif mode == 'census':  # census B pmax inertmax
        t, cs = (9, 0), [(0, 1), (-1, -1), (2, 0)]
        B, pmax, imax = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
        lst = []
        for p in range(102, pmax + 1):
            if isprime(p) and p % 3 == 1:
                pi = Z.split_prime(p); lst += [twoprim(pi), twoprim(conj(pi))]
        lst += [(p, 0) for p in range(5, imax + 1) if isprime(p) and p % 3 == 2]
        tot = Counter(); fails = []
        for pi in lst:
            st, _ = run(t, cs, pi, 1, B)
            tot += st
            if not any(k[0] in ('I', 'II') for k in st): fails.append((pi, norm(pi)))
        print('primes', len(lst), dict(tot))
        print('no Type I/II in window:', len(fails), fails)
