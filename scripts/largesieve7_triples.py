"""LS7 Lemma 1.1/1.2 check: D | A^2 <-> coprime (u,v), uv | A; class identities; residue pinning."""
import sys
from math import gcd
from sympy import divisors, primefactors

def check(Mmax):
    n = 0
    for M in range(3, Mmax, 4):
        A = (M + 1) // 4
        Ds = set(divisors(A * A))
        trip = set()
        for u in divisors(A):
            for v in divisors(A // u):
                if gcd(u, v) == 1:
                    t = A // (u * v)
                    D = u * u * t
                    assert D == A * u // v and A * u % v == 0
                    assert D in Ds and A * A // D == v * v * t
                    c = (-4 * D) % M
                    assert (c * v + u) % M == 0                    # -u/v
                    assert (c - (-4 * u * u * t)) % M == 0          # -4u^2 t
                    assert (c * 4 * v * v * t + 1) % M == 0         # -1/(4v^2t)
                    for p in primefactors(M):
                        a = c % p
                        assert a and (4 * u * v * t) % p == 1
                        assert (u + a * v) % p == 0
                        assert (4 * a * v * v * t + 1) % p == 0
                        assert (4 * u * u * t + a) % p == 0
                    trip.add(D); n += 1
        assert trip == Ds, M
    return n

if __name__ == "__main__":
    Mmax = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    print("triples checked:", check(Mmax), "for all M = 3 mod 4 below", Mmax)
