import sys
from sympy import isprime
from z25_gate import joint_fixture
for p in [97, 193, 313, 3361, 5209]:
    srcs = []
    for g in (1, 2, 3, 4, 6, 8, 12):
        for j in range(-12, 13):
            if (p + j) % g == 0 and (p + j) // g not in (p,) and isprime((p + j) // g) and (p + j) // g > 3:
                srcs.append(((p + j) // g, g))
    t = joint_fixture(p, srcs)
    print(p, len(srcs), 'sources;', 'some source has no failing witness (joint law total)' if t is None else f'adversarial tuple exists (law not total): lcm-moduli {t}', flush=True)
