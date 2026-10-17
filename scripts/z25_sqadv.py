"""Thm 3.2 check: a source witness w' is invisible to p (no determined lift can work) if p is congruent to an
odd square modulo alpha*H'(w').  Verify on fixtures: (i) every adversarial-tuple lcm found by z25_joint_run
indeed has p ≡ odd square; (ii) per source, does some witness have p ≡ odd square mod alpha*H'?"""
from sympy import isprime, sqrt_mod
from z25_gate import Hset
from math import lcm
def odd_square_mod(p, L):
    r = sqrt_mod(p % L, L, all_roots=True) if L > 1 else [1]
    return any(x % 2 == 1 or L % 2 == 1 for x in r)
for p in [97, 193, 313, 3361, 5209]:
    _, rp = Hset(p)
    Hp = {r[5] for r in rp}
    # consistency: no ET modulus H of p has p ≡ odd square mod H
    assert not any(odd_square_mod(p, H) for H in Hp), p
    out = []
    for g in (1, 2, 3, 4, 6, 8, 12):
        for j in range(-12, 13):
            n = (p + j) // g
            if (p + j) % g or n == p or n <= 3 or not isprime(n):
                continue
            _, rs = Hset(n)
            mods = {}
            for r in rs:
                mods.setdefault(r[6], set()).add(g * r[5])
            inv = sum(1 for v in mods.values() if odd_square_mod(p, lcm(*v)))
            out.append(f"{n}(x{g}):{inv}/{len(mods)}")
    print(p, 'invisible source witnesses:', ' '.join(out), flush=True)
