"""R199: Cor 3.3 recount.  For primes p = 1 (mod 8): (a) direct check for p < 2e5: exists a word (1,u,v), i.e. a divisor
d = u-1 of p+1, with (-d/p) = -1  <=>  p+1 has a prime factor = 3 (mod 4); (b) count p < 1e6, p = 1 (8), with no such
prime factor.  Also checks the p = 5 (8) and p = 3 (4) remarks for p < 2e5 (word (1,3,(p+1)/2+1) resp. (1,2,p+2))."""
N = 10 ** 6
spf = list(range(N + 2))
for i in range(2, int((N + 1) ** 0.5) + 1):
    if spf[i] == i:
        for k in range(i * i, N + 2, i):
            if spf[k] == k:
                spf[k] = i


def factors(n):
    f = set()
    while n > 1:
        f.add(spf[n]); n //= spf[n]
    return f


def divisors(n):
    ds = [1]
    m = n
    while m > 1:
        q = spf[m]; e = 0
        while m % q == 0:
            m //= q; e += 1
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds


isprime = lambda n: n > 1 and spf[n] == n
leg = lambda a, p: 1 if pow(a % p, (p - 1) // 2, p) == 1 else -1
mism = tot = 0
for p in range(3, 200000):
    if not isprime(p):
        continue
    direct = any(leg(-d, p) == -1 for d in divisors(p + 1))
    if p % 8 == 1:
        tot += 1
        crit = any(q % 4 == 3 for q in factors(p + 1))
        mism += direct != crit
    else:
        mism += not direct  # p = 3,5,7 (mod 8): always a spine certificate
print('p=1(8) < 2e5:', tot, 'mismatches (all residues):', mism)
cnt = none = 0
for p in range(3, N):
    if p % 8 == 1 and isprime(p):
        cnt += 1
        none += not any(q % 4 == 3 for q in factors(p + 1))
print('p=1(8) < 1e6:', cnt, 'with no prime factor 3 mod 4 in p+1:', none)
