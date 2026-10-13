"""O182 TWISTED_T1 §3: twisted Egyptian fractions over Z[w]:  t/n = c1/x1 + c2/x2 + c3/x3,
x_i in Z[w] with x_i = 1 mod 2 (normalisation at the inert prime 2).  Finds all solutions having some
denominator X (any position) with norm(X - c_i n/t) <= B, via (E y - cj N)(E z - cl N) = cj cl N^2, N = n X, E = t X - ci n.
For each solution: shape (pi-adic valuations of u_i = x_i/c_i), the tame invariants of
alpha = (-u1/u3, -u2/u3)_w at every prime != lambda (Z/3), their sum (= -inv_lambda by reciprocity).
usage: tw_eis_solve.py t c1 c2 c3 n_a n_b e B      (n = (n_a + n_b w)^e; c_i given as a:b)
"""
import sys
from collections import Counter
import tw_eis as E


def parse(s):
    a, b = s.split(':')
    return (int(a), int(b))


def _merge(*facs):
    out = {}
    for f, k in facs:
        for p, v in f.items():
            out[p] = out.get(p, 0) + k * v
    return out


def run(t, cs, pi, e, B, norm2=True, verbose=True, wide=0):
    n = E.power(pi, e)
    pin = E.normalise(pi)
    L = E.normalise(E.LAM)
    sols = set()
    R = int(B ** 0.5) + 1
    for i in range(3):
        j, l = [k for k in range(3) if k != i]
        # centre the box at c_i n / t so that E = t X - c_i n is small (the ES regime)
        num = E.mul(E.mul(cs[i], n), E.conj(t)); nt = E.norm(t)
        cx, cy = round(num[0] / nt), round(num[1] / nt)
        box = [(cx + a, cy + b) for a in range(-R, R + 1) for b in range(-R, R + 1)
               if E.norm((a, b)) <= B and (cx + a, cy + b) != E.ZERO]
        if wide:  # also all X with N(X) <= wide (large-E regime)
            Rw = int((4 * wide / 3) ** 0.5) + 1
            box = list(set(box) | {(a, b) for a in range(-Rw, Rw + 1) for b in range(-Rw, Rw + 1)
                                   if 0 < E.norm((a, b)) <= wide})
        for X in box:
            if norm2 and (X[0] % 2, X[1] % 2) != (1, 0):
                continue
            Ee = E.sub(E.mul(t, X), E.mul(cs[i], n))
            if Ee == E.ZERO:
                continue
            N = E.mul(n, X)
            M = E.mul(E.mul(cs[j], cs[l]), E.mul(N, N))
            fac = _merge((E.factor(cs[j])[1], 1), (E.factor(cs[l])[1], 1), (E.factor(pi)[1], 2 * e),
                         (E.factor(X)[1], 2))
            for d in E.divisors(fac):
                for u in E.UNITS:
                    U = E.mul(u, d)
                    y = E.divexact(E.add(U, E.mul(cs[j], N)), Ee)
                    if y is None or y == E.ZERO:
                        continue
                    V = E.divexact(M, U)
                    z = E.divexact(E.add(V, E.mul(cs[l], N)), Ee)
                    if z is None or z == E.ZERO:
                        continue
                    xs = [None] * 3
                    xs[i], xs[j], xs[l] = X, y, z
                    if norm2 and any((x[0] % 2, x[1] % 2) != (1, 0) for x in xs):
                        continue
                    sols.add(tuple(xs))
    stats = Counter()
    for xs in sols:
        # verify t/n = sum c_i/x_i  <=>  t * x1 x2 x3 = n * sum c_i * prod_{k != i} x_k
        lhs = E.mul(t, E.mul(xs[0], E.mul(xs[1], xs[2])))
        rhs = E.ZERO
        for i in range(3):
            pr = cs[i]
            for k in range(3):
                if k != i:
                    pr = E.mul(pr, xs[k])
            rhs = E.add(rhs, pr)
        assert lhs == E.mul(n, rhs), xs
        vals = tuple(E.valuation(x, pin)[0] - E.valuation(c, pin)[0] for x, c in zip(xs, cs))
        # Type I: one u with v >= e, the others 0;  Type II: one 0, two >= e
        z0 = sum(1 for v in vals if v == 0)
        big = sum(1 for v in vals if v >= e)
        if z0 == 2 and big == 1:
            shape = 'I'
        elif z0 == 1 and big == 2:
            shape = 'II'
        else:
            shape = 'other'
        a = (E.neg(E.mul(xs[0], cs[2])), E.mul(cs[0], xs[2]))
        b = (E.neg(E.mul(xs[1], cs[2])), E.mul(cs[1], xs[2]))
        ps = set()
        for z in list(xs) + list(cs):
            ps |= set(E.factor(z)[1])
        ps.add((2, 0))
        ps.discard(L)
        inv = {p: E.tame_symbol(a, b, p) for p in ps}
        tot = sum(inv.values()) % 3
        inv2 = inv[(2, 0)]
        invpi = inv.get(pin, 0)
        other = sum(1 for p in ps if p not in ((2, 0), pin) and inv[p])
        stats[(shape, inv2, invpi, tot, other)] += 1
    if verbose:
        print(f"t={t} c={cs} n=pi^{e}, pi={pi} N(pi)={E.norm(pi)} B={B}: {len(sols)} sols")
        for k, v in sorted(stats.items(), key=str):
            print("   (shape, inv_2, inv_pi, sum_tame, #other tame places != 0) =", k, ":", v)
    return sols, stats


if __name__ == '__main__':
    t = parse(sys.argv[1]); cs = [parse(s) for s in sys.argv[2:5]]
    pi = (int(sys.argv[5]), int(sys.argv[6])); e = int(sys.argv[7]); B = int(sys.argv[8])
    run(t, cs, pi, e, B)
