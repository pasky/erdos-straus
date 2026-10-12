"""O145 (b) Lemma 3.1(a) check: at t ≡ 0 mod 64*47#, p = t^2+1 prime, small polynomial values are residues."""
from sympy import isprime, jacobi_symbol as J, primorial
L = 64 * primorial(15); cnt = 0
for t in range(L, 3000 * L, L):
    p = t * t + 1
    if not isprime(p): continue
    lin = [J((t + a) % p, p) for a in range(-7, 8) if a]
    big = [J((t + a) % p, p) for a in range(-60, 61) if a]
    quad = [J((t*t + b*t + c) % p, p) for b in range(-3, 4) for c in range(-3, 4) if (t*t + b*t + c) % p]
    print("|a|<=7 NR:", lin.count(-1), " |a|<=60 NR:", big.count(-1), "/120  quad NR:", quad.count(-1), "/", len(quad))
    cnt += 1
    if cnt >= 6: break
