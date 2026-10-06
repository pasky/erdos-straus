"""OMEGA16 §6 (N3): adversarial unit-class sieve systems vs LS (EVIDENCE).

min(kappa, l-2) unit classes are removed mod each prime 3 <= l <= z (at least one unit class kept). The adversary picks the
classes greedily to delay the least surviving prime p > z ("Jacobsthal for primes"):
for each l (in a given order) it removes the classes of the smallest surviving primes.
Reports least survivor p_min, log(1/delta) and the LS ratio log p_min / (log z + log(1/delta)).

Usage: PYTHONPATH=scripts uv run python scripts/omega16_adversary.py Y
"""
import sys, math, json
import numpy as np
from sympy import primerange


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i :: i] = False
    return np.nonzero(s)[0].astype(np.int64)


def run(P, z, kappa, order, rng=None):
    ells = [l for l in primerange(3, z + 1)]
    if order == 'down':
        ells = ells[::-1]
    elif order == 'random':
        rng.shuffle(ells)
    alive = P[P > z]
    logd = sum(math.log(1 - min(kappa, l - 2) / (l - 1)) for l in ells)
    for l in ells:
        r = min(kappa, l - 2)
        removed = set()
        i = 0
        while len(removed) < r and i < len(alive):
            c = int(alive[i] % l)
            removed.add(c)
            i += 1
        if removed:
            res = alive % l
            mask = np.ones(len(alive), dtype=bool)
            for c in removed:
                mask &= res != c
            alive = alive[mask]
        if len(alive) == 0:
            return None, -logd
    return int(alive[0]), -logd


def main():
    Y = int(float(sys.argv[1]))
    P = primes_upto(Y)
    rng = np.random.default_rng(1)
    out = []
    print("z    kappa  order   p_min        log(1/delta)  LS-ratio log p/(log z+log 1/delta)")
    for z in [30, 100, 300, 1000]:
        for kappa in [1, 2, 3, 4, 6, 8]:
            if kappa > z // 4:
                continue
            for order in ['up', 'down', 'random']:
                p, L = run(P, z, kappa, order, rng)
                ratio = math.log(p if p else Y) / (math.log(z) + L)
                ps = str(p) if p else f'>{Y:.0e}'
                rs = f'{ratio:6.2f}' if p else f'>{ratio:5.2f}'
                print(f"{z:5d} {kappa:3d}  {order:6s}  {ps:>12s}  {L:10.2f}   {rs}")
                out.append({'z': z, 'kappa': kappa, 'order': order, 'p_min': p, 'log_inv_delta': L})
    print(json.dumps({'Y': Y, 'rows': out}), file=sys.stderr)


if __name__ == '__main__':
    main()
