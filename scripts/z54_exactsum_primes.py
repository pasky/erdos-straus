# z54 EXACTSUM: random primes p = 1 (mod 24) in [10^k, 2*10^k], seeded. Usage: python ... k count seed
import sys, random
import cypari2
pari = cypari2.Pari()
k, cnt, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = random.Random(seed); out = set()
while len(out) < cnt:
    x = rng.randrange(10**k, 2 * 10**k); x -= x % 24; x += 1
    if pari.isprime(x): out.add(x)
print('\n'.join(map(str, sorted(out))))
