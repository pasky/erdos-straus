"""Finite EVIDENCE for §7 (Q2); does not test PA or assert no minimum."""
from collections import Counter
from itertools import combinations_with_replacement
from math import prod
from random import Random

from z82_bcm_matching import prime


def main():
    a = 512
    primes = [p for p in range(a + 1, 2 * a) if prime(p)]
    if len(primes) % 2:
        primes.pop()
    h = prod(primes)
    planted = []
    for j in range(1, 5):
        band = [p for p in primes if 2*a < (p-a)*2**(j+1) < 3*a]
        planted.append(tuple(band[:2]))
    used = {p for pair in planted for p in pair}
    assert len(used) == 2 * len(planted)
    rest = [p for p in primes if p not in used]
    Random(82).shuffle(rest)
    matching = planted + list(zip(rest[::2], rest[1::2], strict=True))
    lifts = {}
    choices = Counter()
    for left, right in matching:
        for p, q in ((left, right), (right, left)):
            target = -(h // (p*q))**2 % (p*p)
            digit = target % p
            partner_lifts = {-(h // (p*r))**2 % (p*p) for r in primes if r != p}
            assert len(partner_lifts) == len(primes)-1
            matching_lifts = {v for v in partner_lifts if v % p == digit}
            assert digit and target in matching_lifts and len(matching_lifts) <= 2
            choices[len(matching_lifts)] += 1
            lifts[p] = target if p in used else next(
                v for v in range(digit, p*p, p) if v not in matching_lifts)
    m = h*h
    y = sum((m//(p*p))*pow(m//(p*p), -1, p*p)*v for p, v in lifts.items()) % m
    assert all(y % (p*p) == v for p, v in lifts.items())
    # A hit must divide h². In this band only total multiplicity 4 is
    # possible: (2a)^3 < a^4 and a^5 > 16a^4. Include multiplicities 1,
    # not just squared pairs, so we check the unit-digit exclusion too.
    tested = 0
    hits = []
    for p, q, r, s in combinations_with_replacement(primes, 4):
        if p == r or q == s:  # exponent > 2, not a divisor of h²
            continue
        t = p*q*r*s
        tested += 1
        if (m + t*y) % (t*t) == 0:
            hits.append(t)
    assert (m + a**4*y) % a**8 != 0
    assert sorted(hits) == [(p*q)**2 for p, q in reversed(planted)]
    print(f'A={a}, retained={len(primes)}, planted={planted}')
    print(f'first-digit partner counts: one={choices[1]}, two={choices[2]}')
    print(f'interval divisors checked={tested}, hits={sorted(hits)}, endpoint hit=False')


if __name__ == '__main__':
    main()
