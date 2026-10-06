"""R60 from-scratch check: note atoms are POINTWISE_HAAR events E_{M,D},
atoms at a fixed prime l have distinct unit projections, and the unit-Haar
fibre product formula P(H=0|c) = prod(1 - f_c(l)/(l-1)) (exact enumeration
on a toy family). Small parameters only (not the note's asymptotic regime)."""
from math import gcd
from itertools import product
from fractions import Fraction
from sympy import primerange, divisors


def check_event_identity(Mmax=3000):
    bad = 0; n = 0
    for M in range(3, Mmax, 4):
        A = (M + 1) // 4
        for u in divisors(A):
            for v in divisors(A // u):
                w = A // (u * v)
                r = (-u * pow(v, -1, M)) % M
                D = u * u * w
                assert (A * A) % D == 0
                n += 1
                if r != (-4 * D) % M:
                    bad += 1
    return n, bad


def toy_family(Ks, ells, H, z):
    """atoms (k,l,u,v): k in Ks (k=1 mod 4), l prime, H<u,v<=z, (u,v)=(uv,k)=1, 4uv | kl+1"""
    atoms = []
    for k in Ks:
        for l in ells:
            for u in range(H + 1, z + 1):
                for v in range(H + 1, z + 1):
                    if gcd(u, v) == 1 and gcd(u * v, k) == 1 and (k * l + 1) % (4 * u * v) == 0:
                        atoms.append((k, l, u, v))
    return atoms


def check_fibre_product():
    Ks = [1, 5, 9]
    L = 45
    ells = [p for p in primerange(200, 400) if p % 4 == 3]
    H, z = 1, 6  # z^2 < l
    atoms = toy_family(Ks, ells, H, z)
    # distinct projections at fixed l
    for l in ells:
        res = [(-u * pow(v, -1, l)) % l for (k, ll, u, v) in atoms if ll == l]
        assert len(res) == len(set(res)), l
        assert all(r % l != 0 for r in res)
    # exact unit-Haar void per unit c mod L, enumerate a few ells only
    sub = ells[:2]
    for c in range(L):
        if gcd(c, L) != 1:
            continue
        act = {l: set() for l in sub}
        for (k, l, u, v) in atoms:
            if l in sub and (u + c * v) % k == 0:
                act[l].add((-u * pow(v, -1, l)) % l)
        tot = 0; void = 0
        for xs in product(*[range(1, l) for l in sub]):
            tot += 1
            if all(xs[i] not in act[l] for i, l in enumerate(sub)):
                void += 1
        pred = Fraction(1)
        for l in sub:
            pred *= Fraction(l - 1 - len(act[l]), l - 1)
        assert Fraction(void, tot) == pred
    return len(atoms)


if __name__ == "__main__":
    n, bad = check_event_identity()
    print(f"atom->event identity: {n} (M,u,v) triples, mismatches={bad}")
    print(f"toy family atoms={check_fibre_product()}: distinct projections + exact fibre product OK")
