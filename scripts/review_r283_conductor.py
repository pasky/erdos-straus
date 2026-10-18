"""R283: conductor of the Hecke character alpha -> (q/alpha)_3 on Z[w]: check it is trivial on primes alpha = 1 (mod 3q)
(so conductor | 3q, sharper than O272's 'divides 9t'), and nontrivial on some alpha = 1 (mod q) (ramified at 3)."""
from sympy import isprime
for q in (7, 13, 19, 31):
    triv = tot = 0; nontriv_modq = 0; tot_q = 0
    for a in range(-400, 401):
        for b in range(-400, 401):
            N = a * a - a * b + b * b
            if N < 5 or not isprime(N) or N % 3 != 1 or N == q:
                continue
            r = (-a * pow(b, -1, N)) % N if b % N else None
            if r is None:
                continue
            v = pow(q, (N - 1) // 3, N)  # (q/alpha)_3 as element of F_N
            if (a - 1) % (3 * q) == 0 and b % (3 * q) == 0:
                tot += 1; triv += (v == 1)
            elif (a - 1) % q == 0 and b % q == 0:
                tot_q += 1; nontriv_modq += (v != 1)
    print(f"q={q}: alpha=1 mod 3q: {triv}/{tot} trivial; alpha=1 mod q only: {nontriv_modq}/{tot_q} nontrivial")
