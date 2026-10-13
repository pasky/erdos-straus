"""O203 §5: does multiplication in Z[sqrt(-n)] (which sees ALL mu at once) map V_n points to V_n points more
often than chance?  A pair (A, B) (A even, B odd, coprime, gcd(B, n) = 1) is a V_n point (some mu) iff nA^2 + B^2
has a divisor g = -1 (mod 2AB) (GROWING_MUTE Prop 1.1(c)).  Take all V_n points with A, B <= X, form products
beta1*beta2 and beta1*conj(beta2) (beta = B + A sqrt(-n)), normalise, and test; baseline = random admissible (A, B)
with the same (A, B) magnitudes.  Also test triple products.  Usage: cp_cross.py n X ntrip"""
import sys
import random
from math import gcd
from sympy import divisors


def is_vn(n, A, B):
    A, B = abs(A), abs(B)
    if A == 0 or A % 2 or B % 2 == 0 or gcd(A, B) != 1 or gcd(B, n) != 1:
        return None  # not admissible
    M = 2 * A * B
    return any(g % M == M - 1 for g in divisors(n * A * A + B * B))


def main():
    n, X, ntrip = map(int, sys.argv[1:4])
    random.seed(2)
    P = [(A, B) for A in range(2, X + 1, 2) for B in range(1, X + 1, 2) if is_vn(n, A, B)]
    print("n", n, "V_n points with A,B <=", X, ":", len(P))
    stats = {"pair": [0, 0], "base": [0, 0], "trip": [0, 0], "base3": [0, 0]}

    def rec(key, A, B):
        r = is_vn(n, A, B)
        if r is not None:
            stats[key][0] += 1
            stats[key][1] += int(r)

    def mul(b1, b2):  # (B1 + A1 s)(B2 + A2 s), s^2 = -n
        (A1, B1), (A2, B2) = b1, b2
        return (A1 * B2 + A2 * B1, B1 * B2 - n * A1 * A2)

    for i, b1 in enumerate(P):
        for b2 in P[i:]:
            for c in (b2, (-b2[0], b2[1])):
                A, B = mul(b1, c)
                rec("pair", A, B)
                # baseline with comparable size: random admissible point of same |A|,|B| scale
                As, Bs = abs(A), abs(B)
                Ar = random.randrange(max(2, As // 2), As * 2 + 3) // 2 * 2 or 2
                Br = random.randrange(max(1, Bs // 2), Bs * 2 + 3) | 1
                rec("base", Ar, Br)
    for _ in range(ntrip):
        b1, b2, b3 = random.choice(P), random.choice(P), random.choice(P)
        A, B = mul(mul(b1, b2), (random.choice((1, -1)) * b3[0], b3[1]))
        rec("trip", A, B)
        As, Bs = abs(A), abs(B)
        Ar = random.randrange(max(2, As // 2), As * 2 + 3) // 2 * 2 or 2
        Br = random.randrange(max(1, Bs // 2), Bs * 2 + 3) | 1
        rec("base3", Ar, Br)
    for k, (a, h) in stats.items():
        print(k, "admissible", a, "V_n", h, "rate %.4f" % (h / a if a else 0))


if __name__ == "__main__":
    main()
