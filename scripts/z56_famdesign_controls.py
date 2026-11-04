# control inputs for z56scan '-' mode: FRONTIER §4 item-14 test primes, odd squares, prime near-squares p = m^2 + k
import sympy
test = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281,
        193, 2521, 66529, 3361, 5101441]
sq = [m * m for m in (10001, 10003, 31623, 31625, 99999, 100001, 316227, 316229, 999999, 1000001)]
near = []
for m0 in (10**4, 31623, 10**5):
    for m in range(m0, m0 + 400):
        for k in range(1, 17):
            n = m * m + k
            if n % 4 == 1 and sympy.isprime(n): near.append((n, k))
print('\n'.join(map(str, test + sq + [n for n, k in near])))
