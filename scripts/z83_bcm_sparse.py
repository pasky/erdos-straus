"""Finite checks of the sparse-prime root/gcd lemma (not a nonstandard proof)."""
from itertools import product
from math import gcd, isqrt, prod


def crt(residues, moduli):
    a, m = 0, 1
    for r, q in zip(residues, moduli, strict=True):
        a += m * (((r-a) * pow(m, -1, q)) % q)
        m *= q
    return a, m


def run(primes):
    h = prod(primes)
    for i, p in enumerate(primes):
        assert p >= 3 and all(p % k for k in range(2, isqrt(p)+1))
        assert p > prod(primes[:i])**2
    for flags in product((0, 1), repeat=len(primes)):
        residues = []
        for p, rooted in zip(primes, flags, strict=True):
            # A nontrivial unit square when possible, else a nonsquare.
            residues.append(4 % p if rooted else next(a for a in range(2, p) if pow(a,(p-1)//2,p) == p-1))
        P, _ = crt(residues, primes)
        # t(t²-P)²=0 mod p² iff t=0 mod p² or t²=P mod p.
        branches = [[(0, p*p)] + [(r,p) for r in range(1,p) if (r*r-P)%p == 0] for p in primes]
        best = h*h
        for conjunction in product(*branches):
            a, modulus = crt(*zip(*conjunction, strict=True))
            best = min(best, a or modulus)
        if len(primes) <= 2:
            brute = next(t for t in range(1,h*h+1) if (t*(t*t-P)**2) % (h*h) == 0)
            assert brute == best
        assert best*(best*best-P)**2 % (h*h) == 0
        omitted = h*h // gcd(best, h*h)
        top = max((p for p in primes if omitted%p == 0), default=1)
        assert top == max((p for p,b in zip(primes,flags,strict=True) if b), default=1)
        print(''.join(map(str,flags)), 'least', best, 'greatest-root', top)


if __name__ == '__main__':
    for group in [(3, 11), (3, 11, 1091)]:
        print('primes', *group)
        run(group)
