"""z67 K11: targeted falsifier for the candidate witness pi0 = (2 at 11, 2 at 13, 1 elsewhere), family II-2.

By Lemma M, pi0 lies in the II-2 class (a, c, d) (f = 4acd - 1) iff N := {11,13}-part of f is > 1,
N | a + 2c and f/N | a + c.  Then f | (a+c)(a+2c), and modulo f = 4adc - 1 this gives
f | (4a^2 d + 1)(4a^2 d + 2).  So for each (a, d) every candidate c comes from a divisor delta = 4adc - 1 of
(4a^2 d + 1)(4a^2 d + 2) with delta = -1 mod 4ad.  We scan all a*d <= X exhaustively (complete for those (a, d),
all c) and report any catching triple.  Also reports the same count for the control profile (1 at 11, 1 at 13),
which is a square and must give 0.
Usage: uv run --with cypari2 python scripts/z67_k11_pi0_ii2.py X
"""
import sys

import cypari2

pari = cypari2.Pari()


def s143(x):
    n = 1
    for p in (11, 13):
        while x % p == 0:
            x //= p
            n *= p
    return n


def main():
    X = int(sys.argv[1])
    hits, ctrl, tested, pos = [], 0, 0, []
    for a in range(1, X + 1):
        for d in range(1, X // a + 1):
            A = 4 * a * a * d
            q = 4 * a * d
            divs = set()
            for x in pari.divisors(A + 1):
                for y in pari.divisors(A + 2):
                    t = int(x) * int(y)
                    if t % q == q - 1:
                        divs.add(t)
            for delta in divs:
                c = (delta + 1) // q
                tested += 1
                N = s143(delta)
                if N == 1:
                    continue
                fp = delta // N
                if (a + 2 * c) % N == 0 and (a + c) % fp == 0:
                    hits.append((a, c, d, delta, N))
                if (a + c) % N == 0 and (a + c) % fp == 0:   # control: gamma = (1, 1) (square)
                    ctrl += 1
                n11 = 1
                t = N
                while t % 11 == 0:
                    t //= 11
                    n11 *= 11
                if (a + 2 * c) % n11 == 0 and (a + c) % (N // n11) == 0 and (a + c) % fp == 0:
                    pos.append((a, c, d, delta, N))      # positive control: gamma = (2 at 11, 1 at 13)
    print(f"# II-2 scan a*d <= {X}: {tested} (a,c,d) candidates; pi0 catches: {len(hits)}; square-control catches: {ctrl}")
    print(f"# positive control gamma=(2,1): {len(pos)} catches, first {pos[:3]}")
    for h in hits[:20]:
        print("  a=%d c=%d d=%d f=%d N=%d" % h)


if __name__ == "__main__":
    main()
