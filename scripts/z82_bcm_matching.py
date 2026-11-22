"""Finite sign/CRT check for (Q), not a leastness or ES experiment."""
from math import isqrt, prod


def prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def main():
    A = 512
    S = [p for p in range(A + 1, 2 * A) if prime(p)]
    h = prod(S)
    marks = {}
    pairs = []
    for j in range(1, 5):
        # The toy old-polynomial exceptions are the residues 0 and 1.
        band = [p for p in S if 2 * A < (p - A) * 2 ** (j + 1) < 3 * A]
        p, q, u, v = next((p, q, u, v) for p in band for q in band if p < q
                          for u in [-(h // (p * q)) % p]
                          for v in [-(h // (p * q)) % q] if min(u, v) > 1)
        marks.update({p: u, q: v})
        pairs.append((p, q))
    for p in S:
        if p not in marks:
            forbidden = {0, 1} | {-(h // (p * q)) % p for q in S if p != q}
            marks[p] = next(r for r in range(p) if r not in forbidden)
    Y = sum((h // p) * pow(h // p, -1, p) * marks[p] for p in S) % h
    hits = [t for t in range(A*A+1, 4*A*A) if (h + t*Y) % (t*t) == 0]
    assert hits == [p*q for p, q in reversed(pairs)]
    print(f'A={A}, {len(S)} primes, planted={pairs}, exhaustive hits={hits}')


if __name__ == '__main__':
    main()
