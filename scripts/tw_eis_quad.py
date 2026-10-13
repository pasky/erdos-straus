"""O182: quadratic part alpha_{-1} of the BL class on TES solutions: tame invariants at all odd places
(incl. lambda); inv_2 = sum by reciprocity. usage: tw_eis_quad.py B (runs a fixed list of primes)"""
import sys
from collections import Counter
import tw_eis as E, tw_eis_solve as S
t = (9, 0); cs = [(0, 1), (-1, -1), (2, 0)]
B = int(sys.argv[1])
for pi in [(-1, -18), (23, 18), (-9, -28), (-1, -28), (-3, -32), (41, 26), (-35, 6)]:
    sols, st = S.run(t, cs, pi, 1, B, verbose=False)
    pin = E.normalise(pi)
    c = Counter()
    for xs in sols:
        a = (E.neg(E.mul(xs[0], cs[2])), E.mul(cs[0], xs[2]))
        b = (E.neg(E.mul(xs[1], cs[2])), E.mul(cs[1], xs[2]))
        ps = set()
        for z in list(xs) + list(cs):
            ps |= set(E.factor(z)[1])
        ps.add(E.normalise(E.LAM)); ps.discard((2, 0))
        inv = {p: E.tame_symbol2(a, b, p) for p in ps}
        c[(inv.get(pin, 0), inv[E.normalise(E.LAM)], sum(inv.values()) % 2)] += 1
    print(pi, E.norm(pi), 'chi_pi(-1),(2)', E.quad_class((-1, 0), pi), E.quad_class((2, 0), pi),
          '(inv_pi, inv_lam, inv_2) counts:', dict(c), flush=True)
