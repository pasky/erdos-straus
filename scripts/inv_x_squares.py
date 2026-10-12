"""O158: checks on the O152 odd set X(n) = {(t,u,v) >= 1 : t*u*v - u - v = n}.

For odd n <= N (and odd squares m^2 <= S) verify:
 (a) |X(n)| = #{(t,u): u*(t*u-2) = n}  (mod 2)              [swap u<->v; diagonal u=v]
 (b) ES-part {4 | t*u-1} of X(m^2) is empty for odd m          [Lemma 2.2]
 (c) parity of |X(m^2)| (odd for every odd prime m)              [Prop 2.3]
usage: inv_x_squares.py N S
"""
import sys
from sympy import divisors, isprime

def X(n):
    out = []
    for t in range(1, n + 3):
        N = t * n + 1
        for A in divisors(N):
            B = N // A
            if (A + 1) % t == 0 and (B + 1) % t == 0:
                out.append((t, (A + 1) // t, (B + 1) // t, A, B))
    return out

def diag(n):
    return sum(1 for u in divisors(n) if (n // u + 2) % u == 0)

def main():
    N, S = int(sys.argv[1]), int(sys.argv[2])
    bad = 0
    for n in range(1, N + 1, 2):
        xs = X(n)
        if (len(xs) - diag(n)) % 2:
            bad += 1
    print(f"(a) parity identity |X(n)| = #diag(n) mod 2 fails for {bad} odd n <= {N}")
    es_bad = 0; odd_sq = 0; prime_even = 0; cnt = 0
    for m in range(3, int(S ** 0.5) + 1, 2):
        xs = X(m * m)
        cnt += 1
        if any(A % 4 == 0 for (_, _, _, A, _) in xs):
            es_bad += 1
        if len(xs) % 2:
            odd_sq += 1
        elif isprime(m):
            prime_even += 1
    print(f"(b) odd m in [3,{int(S**0.5)}]: {cnt}; X(m^2) has an ES element (4|A) for {es_bad}")
    print(f"(c) |X(m^2)| odd for {odd_sq}/{cnt}; odd prime m with |X(m^2)| even: {prime_even}")

if __name__ == '__main__':
    main()
