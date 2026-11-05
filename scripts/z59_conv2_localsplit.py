"""z59 CONV2 Prop 2.2: which (★)-zeros (screens) are rescued by a complete modulus 7 or 15 of the union U
(Jacobi (n/f) = -1 with gcd(n, f) = 1), and the small-factor profile of the rest."""
from math import gcd
def jac(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0
rd = lambda fn: [int(l) for l in open(fn) if l.strip() and not l.startswith('#')]
primes = rd('data/z58/screens/star_prime_zeros.txt'); comps = rd('data/z58/screens/composite_zeros_le8e6.txt')
M = {1, 121, 169, 289, 361, 529}
loc = lambda n: any(gcd(n, f) == 1 and jac(n, f) == -1 for f in (3, 7, 15))
for name, L in (("(★)-zero primes", primes), ("(★)-zero composites", comps)):
    print(name, len(L), "| locally rescued (f = 3, 7, 15):", sum(map(loc, L)), "| in 𝔐:", sum(n % 840 in M for n in L))
print("locally rescued primes:", [n for n in primes if loc(n)], " all outside 𝔐:", all(n % 840 not in M for n in primes if loc(n)))
rest = [n for n in comps if not loc(n)]
print("composites not locally rescued:", len(rest), "| 3|n:", sum(n % 3 == 0 for n in rest), "| 5|n:", sum(n % 5 == 0 for n in rest),
      "| 7|n:", sum(n % 7 == 0 for n in rest), "| coprime to 105:", [n for n in rest if gcd(n, 105) == 1])
