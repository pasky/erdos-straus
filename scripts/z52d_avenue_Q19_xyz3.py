# z52d avenue Q19 (Z1982): exceptions of n = xyz - x - y - z (x,y,z >= 2) up to N.
# Identity: (xy-1)(xz-1) = x(n+x) + 1, so n is represented iff for some x >= 2,
# x^2 + n x + 1 has a factorisation d*e with d ≡ e ≡ -1 (mod x), d, e >= 2x-1.
import sys
from collections import Counter
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
rep = bytearray(N + 1)
x = 2
while 8 - 6 <= N and x * x * x - 3 * x <= N:
    y = x
    while x * y * y - x - 2 * y <= N:
        z = y
        while True:
            n = x * y * z - x - y - z
            if n > N: break
            if n >= 0: rep[n] = 1
            z += 1
        y += 1
    x += 1
exc = [n for n in range(1, N + 1) if not rep[n]]
def isprime(m):
    if m < 2: return False
    i = 2
    while i * i <= m:
        if m % i == 0: return False
        i += 1
    return True
big = [n for n in exc if n > 1000]
print("exceptions <=", N, ":", len(exc), " >1000:", len(big))
print("mod 12:", sorted(Counter(n % 12 for n in big).items()))
print("2n+5 prime:", sum(isprime(2 * n + 5) for n in big), "/", len(big))
print("3n+10 all factors 1 mod 3 or prime:", sum(isprime(3 * n + 10) for n in big), "(prime count)")
print("both 2n+5 and 3n+10 prime:", sum(isprime(2*n+5) and isprime(3*n+10) for n in big))
print("2n+5, 3n+10, 4n+17 prime:", sum(isprime(2*n+5) and isprime(3*n+10) and isprime(4*n+17) for n in big))
print("sample:", big[:15])
