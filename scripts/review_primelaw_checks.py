"""Independent checks for the hostile review of EXCEPTIONAL_PRIMELAW.md.

(a) Lemma 4.1 projection: for unit b mod d and unit n mod L, the average of
    1[n' = b (d)] over units n' = n (mod L) (n' mod lcm(d,L)) equals
    phi(L)/phi(lcm) * 1[n = b (gcd(d,L))], and the E*-mean is preserved.
(b) Lemma 1.3: E*-mass of b mod l^v inside (Z/l^E)^x.
(c) R-term identity: K2 R-term - log(Q0/phi(Q0)) = (pi(W)+1) log 2.
"""
import math
import random
from sympy import totient as phi, primerange


def check_a(trials=300, seed=1):
    rnd = random.Random(seed)
    bad = 0
    for _ in range(trials):
        L = rnd.choice([12, 30, 60, 84, 90, 120, 210, 36, 72])
        d = rnd.randint(2, 200)
        D = L * d // math.gcd(L, d)
        units_d = [b for b in range(d) if math.gcd(b, d) == 1]
        b = rnd.choice(units_d)
        g = math.gcd(d, L)
        kappa = phi(L) / phi(D)
        for n in range(L):
            if math.gcd(n, L) != 1:
                continue
            lifts = [m for m in range(n, D, L) if math.gcd(m, D) == 1]
            assert len(lifts) == phi(D) // phi(L)
            avg = sum(1 for m in lifts if m % d == b) / len(lifts)
            pred = kappa if n % g == b % g else 0.0
            if abs(avg - pred) > 1e-12:
                bad += 1
        # mean preservation: E*[1[n=b (d)]] = 1/phi(d) vs kappa/phi(g)
        if abs(1 / phi(d) - kappa / phi(g)) > 1e-12:
            bad += 1
    print(f"(a) Lemma 4.1 projection: {trials} random (L,d,b): mismatches = {bad}")


def check_b():
    bad = 0
    for l in [3, 5, 7, 11]:
        for E in range(1, 4):
            q = l ** E
            units = [n for n in range(q) if n % l]
            for v in range(1, E + 1):
                for b in range(l ** v):
                    mass = sum(1 for n in units if n % l ** v == b) / len(units)
                    pred = 0.0 if b % l == 0 else (l / (l - 1)) * l ** (-v)
                    if abs(mass - pred) > 1e-12:
                        bad += 1
    print(f"(b) Lemma 1.3 unit masses (l<=11, E<=3): mismatches = {bad}")


def check_c():
    for W in [5, 13, 31, 101, 1009]:
        ps = list(primerange(3, W + 1))
        k2 = 3 * math.log(2) + sum(math.log(2 * p / (p - 1)) for p in ps)
        q0_over_phi = math.log(2) + sum(math.log(p / (p - 1)) for p in ps)
        pi_w = len(ps) + 1
        print(f"(c) W={W}: K2 R-term - log(Q0/phi(Q0)) = {k2 - q0_over_phi:.6f}; "
              f"(pi(W)+1)log2 = {(pi_w + 1) * math.log(2):.6f}; "
              f"log(P_W/phi(P_W)) = {q0_over_phi:.4f}")


if __name__ == "__main__":
    check_a()
    check_b()
    check_c()
