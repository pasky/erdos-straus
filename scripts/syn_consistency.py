"""O171 §5 cross-document consistency audit.
(a) GI Prop 4.1 count W(n) (Type I a=1 divisor form) == DK a0(n) (interior words, 4 | A) + DK boundary words
    (v = 1, 4 | A), for n = 1 (4).
(b) GI census (class +1, class -1) of D*(n) at p = 10009, 10177 (GI §4 lists (19,13), (26,14)).
(c) INV2 Lemma 5.1 vs DK Thm 4.5: for p = 1 (8) and (t,u,v) with tuv-u-v=p, 4 | tu-1, the odd parts of A=tu-1,
    B=tv-1 and uv all have Jacobi symbol -1 mod p.
Usage: syn_consistency.py NMAX
"""
import sys
from sympy import divisors, jacobi_symbol, isprime


def odd(x):
    while x % 2 == 0:
        x //= 2
    return x


def gi_sets(n):
    plus = minus = 0
    t = 3
    while t <= n + 2:
        N = t * n + 1
        for m2 in divisors(N):
            if m2 == 1:
                continue
            m = N // m2
            if m % 4:
                continue
            r = m2 % t
            if r == 1 % t:
                plus += 1
            elif r == t - 1:
                minus += 1
        t += 4
    return plus, minus


def dk_counts(n):
    """interior words t,u,v>=2 with 4|tu-1, and boundary words with u,v,t>=1 and some letter 1, 4|tu-1."""
    inter = bnd = 0
    t = 1
    while t <= n + 2:
        N = t * n + 1
        for A in divisors(N):
            B = N // A
            if (A + 1) % t or (B + 1) % t:
                continue
            u, v = (A + 1) // t, (B + 1) // t
            if u < 1 or v < 1 or A % 4:
                continue
            if t >= 2 and u >= 2 and v >= 2:
                inter += 1
            else:
                bnd += 1
        t += 1
    return inter, bnd


def main():
    NM = int(sys.argv[1])
    bad_a = cnt = 0
    for n in range(5, NM + 1, 4):
        W = gi_sets(n)[1]
        i, b = dk_counts(n)
        cnt += 1
        if W != i + b:
            bad_a += 1
            if bad_a < 5:
                print("mismatch (a)", n, W, i, b)
    print(f"(a) n=1(4) <= {NM}: {cnt} values, mismatches W != a0+boundary: {bad_a}")
    for p in (10009, 10177):
        print("(b)", p, gi_sets(p))
    bad_c = tot = 0
    for p in range(17, NM + 1, 8):
        if not isprime(p):
            continue
        t = 1
        while t <= p + 2:
            N = t * p + 1
            for A in divisors(N):
                B = N // A
                if (A + 1) % t or (B + 1) % t or A % 4:
                    continue
                u, v = (A + 1) // t, (B + 1) // t
                if u < 1 or v < 1:
                    continue
                tot += 1
                s = (jacobi_symbol(odd(A), p), jacobi_symbol(odd(B), p), jacobi_symbol(odd(u * v), p))
                if s != (-1, -1, -1):
                    bad_c += 1
                    if bad_c < 5:
                        print("violation (c)", p, t, u, v, s)
            t += 1
    print(f"(c) primes p=1(8) <= {NM}: {tot} E(p)-points, violations of Lemma 5.1: {bad_c}")


if __name__ == "__main__":
    main()
