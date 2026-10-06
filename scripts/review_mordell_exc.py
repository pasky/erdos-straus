"""R80: ES numerically for every prime p <= N in the 6 exceptional classes mod 720720.
Search: x = ceil(p/4)+k, m = 4x-p, N = p x; 1/y+1/z = m/N  <=>  (m y - N)(m z - N) = N^2,
need divisor d | N^2, d <= N, d = -N mod m.  Exact verification with Fractions."""
import sys
from fractions import Fraction as Fr
from sympy import factorint, primerange, divisors

EXC = [112561, 352801, 380881, 418321, 473761, 483841]
L = 720720

def solve(p, kmax=10**5):
    x0 = (p+3)//4
    for x in range(x0, x0+kmax):
        m = 4*x - p; Nn = p*x
        f = factorint(x); f[p] = f.get(p, 0)+1
        f2 = {q: 2*e for q, e in f.items()}
        # enumerate divisors of N^2 up to N
        ds = [1]
        for q, e in f2.items():
            ds = [d*q**i for d in ds for i in range(e+1) if d*q**i <= Nn]
        for d in sorted(ds):
            if (d + Nn) % m == 0:
                y = (d+Nn)//m; z = (Nn*Nn//d + Nn)//m
                if (Nn*Nn//d + Nn) % m == 0:
                    assert Fr(4, p) == Fr(1, x)+Fr(1, y)+Fr(1, z)
                    return x, y, z
    return None

if __name__ == '__main__':
    N = int(float(sys.argv[1])); cnt = 0; fail = []
    from sympy import isprime
    for t in EXC:
        for p in range(t, N+1, L):
            if isprime(p):
                cnt += 1
                if solve(p) is None: fail.append(p)
    print('primes checked:', cnt, 'failures:', fail)
