"""Marginal cheap-shot densities, all residue classes (NOT a model for zero rate)."""
from fractions import Fraction
from math import gcd

print('# offset design shots blocked E_hits root_multiplicity_at_u_eq_offset')
for c in [0, 1, 4, 16, 36, 64, 100]:
    mean, shots, blocked, diagonals = Fraction(), 0, 0, 0
    for f in range(7, 1001, 8):
        # Uniform m mod f with m²+c a unit, or uniform p mod f in baseline.
        counts = [0] * f
        for t in range(f):
            p = (t*t+c) % f if c else t
            if gcd(p, f) == 1:
                counts[(-p) % f] += 1
        den = sum(counts)
        for u in range(1, (f+1)//8+1):
            if ((f+1)//8) % u == 0:
                shots += 1
                blocked += counts[u] == 0
                mean += Fraction(counts[u], den)
                if c == u:
                    diagonals += counts[u]
    assert diagonals == 0
    print(c, 'shift' if c else 'uniform-units', shots, blocked,
          f'{float(mean):.6f}', diagonals)
