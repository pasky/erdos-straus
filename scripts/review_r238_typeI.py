"""R238 from-scratch check of CAP_POINTWISE Prop 4.1 (Type I windows).

usage: review_r238_typeI.py P K Y
p = 1 (4) prime <= P, k' = 3 (4) prime <= K, a = (pk'+1)/4.
(a) (s/k') = (s/p) for odd primes s | a; (a/p) = 1.
(b) predicted-empty windows (all odd s | a residues mod p, and a odd or k' = 7 (8)): search ALL y <= Y (not only
    a | y) with x = pa, 1/z = k'/a - 1/y > 0, test Def 1.1 (cap infinity) exactly. Report hits with a | y (would
    refute Prop 4.1) and hits with a not dividing y (outside Prop 4.1's scope; relevant to the 'Dichotomy' reading).
"""
import sys
from fractions import Fraction
from review_r238_core import factor, is_prime, jacobi, def11_cap


def main():
    P, Kp, Y = map(int, sys.argv[1:4])
    nid = nviol = nempty = 0
    hit_in = hit_out = 0
    ex_out = []
    for p in range(5, P + 1, 4):
        if not is_prime(p):
            continue
        for k in range(3, Kp + 1, 4):
            if not is_prime(k) or k == p:
                continue
            a = (p * k + 1) // 4
            fa = factor(a)
            if jacobi(a % p, p) != 1:
                nviol += 1
            for s in fa:
                if s > 2:
                    nid += 1
                    if jacobi(s, k) != jacobi(s, p):
                        nviol += 1
            empty = all(jacobi(s, p) == 1 for s in fa if s > 2) and (a % 2 == 1 or k % 8 == 7)
            if not empty:
                continue
            nempty += 1
            for y in range(a // k + 1, Y + 1):
                zi = Fraction(k, a) - Fraction(1, y)
                if zi <= 0:
                    continue
                e = def11_cap(p, p * a, y, 1 / zi)
                if e is not None:
                    if y % a == 0:
                        hit_in += 1
                        print("REFUTES Prop 4.1:", p, k, a, y)
                    else:
                        hit_out += 1
                        if len(ex_out) < 5:
                            ex_out.append((p, k, a, y, e))
    print(f"P={P} K={Kp} Y={Y}: symbol identities {nid}, violations {nviol}; predicted-empty windows {nempty}")
    print(f"  Def1.1 solutions there with a|y: {hit_in}; with a not | y (outside Prop 4.1 scope): {hit_out} e.g. {ex_out}")


if __name__ == "__main__":
    main()
