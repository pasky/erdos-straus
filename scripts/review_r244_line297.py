"""R244 from-scratch replay of EXP_NEAR_SQUARE §2 'line coverage': the 3-line X_{3,3} of 4^s + 297
(mu_l' = 3 exactly for l' != 3, mu_3 in Z_3 free) is covered by classes with v_3(L_M) <= 2.
Uses only prime moduli q (D_q and II2 with f = q), q <= QMAX; each witness re-verified by an exact solution of an
actual member 4^s + 297 (s chosen by CRT on the line). usage: review_r244_line297.py QMAX
"""
import sys
from fractions import Fraction
import sympy as sp

K = 297


def main():
    QMAX = int(sys.argv[1])
    need = set(range(9))  # residues c = mu_3 mod 9
    wit = {}
    for q in sp.primerange(5, QMAX):
        if K % q == 0:
            continue
        o = int(sp.n_order(4, q))
        v = sp.multiplicity(3, o)
        if v > 2:
            continue
        o1 = o // 3 ** v
        vals = set()
        if q % 4 == 3:
            m = (q + 1) // 4
            for a in sp.divisors(m):
                for d in sp.divisors(m // a):
                    vals.add(((-4 * a * a * d) % q, ('II2', a, d, q)))
        vals.add((0, ('D', q)))
        for c in range(3 ** v):
            mu = int(sp.ntheory.modular.crt([o1, 3 ** v], [3 % o1, c])[0]) if v else 3 % o1
            n = (pow(4, mu, q) + K) % q
            for r, tag in vals:
                if r == n:
                    for cc in range(c, 9, 3 ** v):
                        if cc in need:
                            need.discard(cc); wit[cc] = (tag, o, v)
                    break
        if not need:
            break
    print('uncovered residues mod 9:', sorted(need))
    for cc, (tag, o, v) in sorted(wit.items()):
        q = tag[-1] if tag[0] == 'II2' else tag[1]
        # actual exponent on the line: s ≡ 3 mod (o/3^v), s ≡ cc mod 9, s large
        o1 = o // 3 ** v
        s = int(sp.ntheory.modular.crt([o1, 9], [3 % o1, cc])[0]) + 9 * o1 * 3
        n = 4 ** s + K
        if tag[0] == 'D':
            assert n % q == 0
            # ES(q) by brute force
            sol = next((x, y, (Fraction(4, q) - Fraction(1, x) - Fraction(1, y)).denominator)
                       for x in range(q // 4 + 1, q + 1) for y in range(x, 4 * q * q)
                       if (lambda r: r > 0 and r.numerator == 1)(Fraction(4, q) - Fraction(1, x) - Fraction(1, y)))
            X, Y, Z = (u * (n // q) for u in sol)
        else:
            _, a, d, f = tag
            c = (f + 1) // (4 * a * d); e = (n + 4 * a * a * d) // f; assert (n + 4 * a * a * d) % f == 0
            b = c * e - a
            X, Y, Z = a * b * d, a * c * d * n, b * c * d * n
        assert min(X, Y, Z) > 0 and Fraction(4, n) == Fraction(1, X) + Fraction(1, Y) + Fraction(1, Z)
        print(f'  mu_3 ≡ {cc} (9): {tag}, ord_q(4) = {o} (v3 = {v}); verified at s = {s}')


if __name__ == '__main__':
    main()


def check_ii1(a, b, e, cc=6):
    """composite-modulus witness found by /tmp search (II1 family) for mu_3 ≡ cc (9): verify on an actual member."""
    M = 4 * a * b; m = M
    while m % 2 == 0:
        m //= 2
    L = 1
    for q, ex in sp.factorint(m).items():
        L = sp.ilcm(L, sp.n_order(4, q ** ex))
    L = int(L); v = sp.multiplicity(3, L); L1 = L // 3 ** v
    assert v <= 2 and (a + b) % e == 0 and sp.gcd(e, M) == 1
    s = int(sp.ntheory.modular.crt([L1, 9], [3 % L1, cc])[0]) + 9 * L1 * 2
    n = 4 ** s + K
    assert (n + e) % M == 0
    t = (n + e) // M; mm = (a + b) // e
    X, Y, Z = a * b * t, n * mm * b * t, n * mm * a * t
    assert Fraction(4, n) == Fraction(1, X) + Fraction(1, Y) + Fraction(1, Z)
    print(f'  mu_3 ≡ {cc} (9): II1 {(a, b, e)}, M = {M}, L = {L} = {sp.factorint(L)}; verified at s = {s}')


if __name__ == '__main__' and len(sys.argv) > 2:
    check_ii1(11, 6702, 959)
