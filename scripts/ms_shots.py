"""O197: the three 'modulus-m shots' through the cube point (1,1,1) (FIXED_MODULUS_SHOTS §1, 4 -> m):
p+1, p+m, m*p+1 'fire' iff they have a divisor h = -1 (mod m), h > 1 (h = m*k - 1 with the free cube coordinate k).
For m = 4 this is 'a prime factor = 3 mod 4'.  Count primes p <= N (p !| m) where all three fail.
usage: ms_shots.py m N"""
import sys
from sympy import primerange, divisors

def fires(N, m):
    return any(h > 1 and (h + 1) % m == 0 for h in divisors(N))

if __name__ == '__main__':
    m, N = int(sys.argv[1]), int(sys.argv[2])
    bad = [p for p in primerange(3, N + 1) if m % p and not (fires(p + 1, m) or fires(p + m, m) or fires(m * p + 1, m))]
    print(f"m={m}: primes <= {N} where p+1, p+{m}, {m}p+1 all fail: {len(bad)}; first: {bad[:12]}; "
          f"131 {'fails' if 131 in bad else 'fires'}, 241 {'fails' if 241 in bad else 'fires'}")
