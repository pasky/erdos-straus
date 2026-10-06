"""MN3 numerics (EVIDENCE): forbidden fractions of the first stage-A steps after the
class-of-one prefix r = 1 mod Q(q0).

Stage A reveals prime powers q in P (primes not dividing m) in increasing order.  At step
q = l^(a+1) the completed atoms are M = q*M1, M1 | L(q) (MN2 Lemma 1.2).  With r = 1 mod Q(q0) and
(for the steps checked here) no earlier stage-A digits, an atom is consistent iff
gcd(M/l, Q0-part) ... i.e. all digits of M other than the new one are those of 1:
-mD = 1 mod M/l  (all of M/l is revealed and equals 1 there, as r = 1 on every revealed digit
when the earlier stage-A steps also chose 1 -- we force r = 1 on them, i.e. this measures the
class-of-one process continued deterministically, the worst case for SI).
Forbidden classes at the step: {-mD mod q} over consistent completed atoms, among the N lifts of 1 mod l^a.

usage: uv run python mn3_first.py m q0 nsteps
"""
import sys
from math import gcd
from sympy import factorint, divisors, primerange, isprime


def ppowers(m, lo, hi):
    out = []
    for p in primerange(2, hi + 1):
        if m % p == 0:
            continue
        pk = p
        while pk <= hi:
            if pk > lo:
                out.append((pk, p))
            pk *= p
    return sorted(out)


def main():
    m, q0, nsteps = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    # revealed modulus: lcm of P-prime powers <= current
    rev = {}
    for (pk, p) in ppowers(m, 1, q0):
        rev[p] = pk
    steps = ppowers(m, q0, 10 ** 6)[:nsteps]
    for (q, l) in steps:
        Lq = 1
        for p, pk in rev.items():
            if p != l:
                Lq *= pk
        la = rev.get(l, 1)          # l^a already revealed
        Nlifts = (l - 1) if la == 1 else l
        forb = set()
        ncons = 0
        for M1 in divisors(Lq):
            M = q * M1
            if M % m != m - 1 or M < 3:
                continue
            A = (M + 1) // m
            Mminus = M // l
            for D in divisors(A * A):
                if (m * D + 1) % Mminus == 0:   # -mD = 1 mod M/l
                    ncons += 1
                    forb.add((-m * D) % q)
        f = len(forb) / Nlifts
        print("q0=%d step q=%d (l=%d): consistent completed atoms Y=%d, forbidden fraction f=%.3f"
              % (q0, q, l, ncons, f))
        sys.stdout.flush()
        rev[l] = q


if __name__ == "__main__":
    main()
