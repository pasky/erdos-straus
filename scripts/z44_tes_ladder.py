"""O276 memo z44_tes_ladder: the k-ladder for the order-3 variant TES over Z[w] (SYNTHESIS_SPARKS2 §3).
TES_(k)(n): 9/n = w/x + w^2/y + 2D/Z, D = Q^k (Q odd rational integer prime to 6N(n)), via ONE FIXED shot prime g ≡ 10+w (18).
For k = 1, 2, 3: over 2-primary split primes pi with N(pi) <= X and their cubes pi^3: does the fixed g fire
(g | n + 18 Q^k for some admissible Q)? If yes, build the Prop 3.1 solution, verify exactly, check Type II shape at pi.
usage: PYTHONPATH=scripts uv run python scripts/z44_tes_ladder.py X
"""
import sys
from math import gcd as igcd
import tw_eis as E
import syn2_tes_shots as S


def shot(n, D, g):
    A = E.add(n, E.mul(S.rat(18), D))
    Ee = E.divexact(A, g)
    if Ee is None:
        return None
    x = E.divexact(E.add(E.mul(S.W, n), Ee), S.rat(9))
    a = E.divexact(E.add(g, S.W2), S.rat(9))
    y = E.mul(n, a)
    Z = E.mul(E.mul(n, x), a)
    lhs = E.add(E.add(E.mul(E.mul(E.mul(S.W, n), y), Z), E.mul(E.mul(E.mul(S.W2, n), x), Z)),
                E.mul(E.mul(E.mul(E.mul(S.rat(2), D), n), x), y))
    assert lhs == E.mul(E.mul(E.mul(S.rat(9), x), y), Z)
    return x, y, Z


def main():
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    l, g = min(S.class_primes(3000))
    print(f"fixed shot prime g = {g}, N(g) = {l}")
    res = {}
    for p in S.rational_primes(X):
        if p % 3 != 1 or p < 7 or p == l:
            continue
        for pi0 in E.split_prime(p):
            pi = next(E.mul(u, pi0) for u in E.UNITS if S.two_primary(E.mul(u, pi0)))
            for tag, n in (("prime", pi), ("cube", E.power(pi, 3))):
                for k in (1, 2, 3):
                    hit = None
                    for Q in range(1, 12 * l, 2):
                        if igcd(Q, 6 * p) != 1:
                            continue
                        out = shot(n, S.rat(Q ** k), g)
                        if out:
                            hit = (Q, out)
                            break
                    key = (tag, k)
                    t = res.setdefault(key, [0, 0, 0])
                    t[0] += 1
                    if hit:
                        x, y, Z = hit[1]
                        e = 3 if tag == "cube" else 1
                        vx, vy, vZ = (E.valuation(v, pi)[0] for v in (x, y, Z))
                        t[1] += 1
                        t[2] += (vx == 0 and vy >= e and vZ >= e)
    for (tag, k), (tot, hit, t2) in sorted(res.items()):
        print(f"{tag:5s} k={k}: fixed g fires for {hit}/{tot}; Type II shape at pi in {t2}")


if __name__ == "__main__":
    main()
