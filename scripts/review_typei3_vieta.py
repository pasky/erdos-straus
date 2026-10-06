"""R72 from-scratch brute force for Lemma 5.1, Cor 5.2, Prop 5.3.
(1) Lemma 5.1 generalised to any integer B>=1 in place of 4c: F e = 1 + B K^2, e - F = B K delta  =>  F = 1 mod B delta.
(2) Cor 5.2: certificates at x̂_w for SOME w = 9 mod 16 with t <= 4 or alpha+2gamma <= 4, v_7(c) odd, ck <= HMAX.
(3) Prop 5.3: levels 5,6, all divisor pairs F<e of N with 16 n | e-F: F = 1 mod c_o (odd part of c), delta odd needed
    only for certificates, so it is not imposed here."""
import sys
from sympy import divisors


def val(p, n):
    e = 0
    while n % p == 0:
        n //= p; e += 1
    return e


def lemma51(Bmax, Kmax):
    tested = bad = 0
    for B in range(1, Bmax + 1):
        for K in range(1, Kmax + 1):
            N = 1 + B * K * K
            for F in divisors(N):
                e = N // F
                if e <= F or (e - F) % (B * K):
                    continue
                d = (e - F) // (B * K)
                tested += 1
                if (F - 1) % (B * d) or (e - 1) % (B * d):
                    bad += 1
    print(f'(1) Lemma 5.1 (B<= {Bmax}, K<= {Kmax}): {tested} pairs, failures {bad}')


def cor52(HMAX):
    found = 0; tested = 0
    for c in range(7, HMAX + 1, 7):
        if val(7, c) % 2 == 0:
            continue
        for k in range(1, HMAX // c + 1):
            al, ga = val(2, c), val(2, k)
            t = 2 + al + ga
            if not (t <= 4 or al + 2 * ga <= 4):
                continue
            h = 4 * c * k
            v = val(7, c * k)
            mp = (h >> t) // 7 ** v
            N = 1 + 4 * c * k * k
            for F in divisors(N):
                tested += 1
                if (F + 1) % mp or (F - 1) % 7 ** v:
                    continue
                # exists w = 9 mod 16 with F = -w mod 2^t  <=>  F = 7 mod 2^min(t,4)
                if F % 2 ** min(t, 4) == 7 % 2 ** min(t, 4):
                    found += 1
                    print('  Cor5.2 counterexample?', c, k, F, file=sys.stderr)
    print(f'(2) Cor 5.2 (ck <= {HMAX}): divisors tested {tested}, certificates at some w=9(16): {found}')


def prop53(CO):
    tested = bad = 0
    odd = range(1, CO, 2)
    for level in (5, 6):
        for ga in range(level // 2 + 1):
            al = level - 2 * ga
            for co in odd:
                for ko in odd:
                    c, k = 2 ** al * co, 2 ** ga * ko
                    n = co * ko
                    N = 1 + 4 * c * k * k
                    for F in divisors(N):
                        e = N // F
                        if e <= F or (e - F) % (16 * n):
                            continue
                        tested += 1
                        if (F - 1) % co:
                            bad += 1
    print(f'(3) Prop 5.3 (odd parts < {CO}): {tested} pairs with 16n | e-F, failures of F=1 mod c_o: {bad}')


if __name__ == '__main__':
    lemma51(60, 150)
    cor52(int(sys.argv[1]) if len(sys.argv) > 1 else 20000)
    prop53(int(sys.argv[2]) if len(sys.argv) > 2 else 60)
