"""O136 §5.2 (EVIDENCE): a spinor-exceptional (Brauer-Manin) factor vanishing on squares.
For n <= N coprime to 6 with n = 1 (mod 3) [the n = 1 mod 3 class meets every class mod 72 that
3x^2+4y^2+9z^2 represents generically], list n NOT represented by 3x^2+4y^2+9z^2 and factor them."""
import sys, math
from sympy import factorint
N = int(sys.argv[1]) if len(sys.argv) > 1 else 50000
a, b, c = 3, 4, 9
rep = bytearray(N + 1)
for z in range(math.isqrt(N // c) + 1):
    for y in range(math.isqrt((N - c*z*z) // b) + 1):
        s = c*z*z + b*y*y
        for x in range(math.isqrt((N - s) // a) + 1):
            rep[s + a*x*x] = 1
# classes mod 72 (n coprime to 6) and their represented fraction on [N/2, N]
cls = {}
for n in range(N // 2, N + 1):
    if math.gcd(n, 6) == 1:
        t = cls.setdefault(n % 72, [0, 0]); t[0] += 1; t[1] += rep[n]
good = sorted(r for r, (t, k) in cls.items() if k > 0.5 * t)
print("classes mod 72 generically represented:", good)
miss = [n for n in range(1, N + 1) if math.gcd(n, 6) == 1 and n % 72 in good and not rep[n]]
print("exceptions in those classes up to", N, ":", len(miss))
ok = True
for n in miss:
    m = math.isqrt(n)
    f = factorint(n)
    sq = (m*m == n) and all(q % 3 == 1 for q in factorint(m))
    ok &= sq
    print(n, f, "m^2 with all primes of m = 1 mod 3" if sq else "OTHER")
print("all exceptions are m^2 with primes(m) = 1 mod 3:", ok)
sq_ok = [m for m in range(1, math.isqrt(N)+1) if math.gcd(m,6)==1 and all(q%3==1 for q in factorint(m)) and (m*m)%72 in good]
print("such squares in range:", len(sq_ok), " of which non-represented:", sum(1 for m in sq_ok if not rep[m*m]))
