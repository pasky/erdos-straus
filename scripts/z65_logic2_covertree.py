"""z65 LOGIC2: refinement-tree version of the ET Prop 1.9 covering probe (Theorem D / question Q_U).

Start from the target set K at level Q0 = 9240 (n = 1 mod 840, n a non-residue mod 11) and multiply the level by the
primes in PRIMES one at a time.  At each level Q, the residues mod Q of K that are not covered by any ET Prop 1.9
family class with modulus dividing Q are kept ("open nodes"); their refinements are tested at the next level.
A node covered at level Q stays covered for all refinements, so the open-node count at level Q is exactly the number of
residue classes of K mod Q that are uncovered at level Q.  If it reaches 0, K is a finite union of polynomially
solvable classes (IOpen proves ES on K for large n).  If it keeps growing, that is EVIDENCE for K meeting the closed
uncovered set U (Z65_LOGIC2.md Theorem D).  Families exactly as in scripts/z65_logic2_cover.py.
Usage: uv run --with sympy python scripts/z65_logic2_covertree.py [p1 p2 ...]   (default 13 17 19 23 29)
"""
import sys
from collections import defaultdict
from math import gcd

from sympy import divisors, factorint
from sympy.ntheory.residue_ntheory import sqrt_mod


def is_qr(x, p):
    return pow(x % p, (p - 1) // 2, p) == 1


def family_sets(Q):
    """dict modulus -> set of residues, for all ET Prop 1.9 family classes with modulus dividing Q."""
    S = defaultdict(set)
    divs = divisors(Q)
    divset = set(divs)
    four = [m for m in divs if m % 4 == 0]
    for m in four:
        P = m // 4
        for a in divisors(P):
            d = P // a
            for f in divisors(4 * a * a * d + 1):            # T1a
                S[m].add((-f) % m)
            b = d
            for e in divisors(a + b):                        # T2a, T1d
                if gcd(e, 4 * a * b) == 1:
                    S[m].add((-e) % m)
                    S[m].add((-pow(e, -1, m)) % m)
            for f in divs:                                   # T1b, T1c (CRT-combined modulus m*f)
                if f == 1 or gcd(f, m) != 1 or (m * f) not in divset:
                    continue
                M = m * f
                inv = pow(m, -1, f)
                c1 = (-f) % m
                tgt = []
                if gcd(a, f) == 1:                           # T1b with (a, c) = (a, d)
                    tgt.append((-d * pow(a, -1, f)) % f)
                rhs = (-4 * a * a * d) % f                    # T1c with (c, d) = (a, d)
                tgt += [x for x in (sqrt_mod(rhs, f, all_roots=True) or []) if gcd(x, f) == 1]
                for c2 in tgt:
                    S[M].add((c1 + m * (((c2 - c1) * inv) % f)) % M)
        for e in divisors(P):                                # T2c: modulus 4ade = m
            ad = P // e
            if gcd(4 * ad, e) != 1:
                continue
            for a in divisors(ad):
                d = ad // a
                S[m].add((-4 * a * a * d - e) % m)
    for f in divs:                                           # T2b
        if (f + 1) % 4:
            continue
        P = (f + 1) // 4
        for a in divisors(P):
            if gcd(a, f) != 1:
                continue
            for d in divisors(P // a):
                S[f].add((-4 * a * a * d) % f)
    return S


def covered(x, S):
    return any((x % m) in R for m, R in S.items())


def main():
    primes = [int(p) for p in sys.argv[1:]] or [13, 17, 19, 23, 29]
    Q = 9240
    nonres11 = [x for x in range(1, 11) if not is_qr(x, 11)]
    nodes = [x for x in range(Q) if gcd(x, Q) == 1 and x % 840 == 1 and x % 11 in nonres11]
    print(f"# target K: n = 1 mod 840, n non-residue mod 11; refinement primes {primes}")
    for step in range(len(primes) + 1):
        S = family_sets(Q)
        nmem = sum(len(v) for v in S.values())
        open_nodes = [x for x in nodes if not covered(x, S)]
        tot = len(nodes)
        print(f"level Q={Q} ({dict(factorint(Q))}): tested={tot} uncovered={len(open_nodes)} "
              f"(family residues={nmem}, moduli={len(S)})", flush=True)
        if step == len(primes) or not open_nodes:
            break
        p = primes[step]
        newQ = Q * p
        nodes = [x + Q * k for x in open_nodes for k in range(p) if (x + Q * k) % p != 0]
        Q = newQ
    if open_nodes:
        print("# sample uncovered residues at final level:", open_nodes[:5])


if __name__ == "__main__":
    main()
