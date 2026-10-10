"""O132 §3.1 (EVIDENCE): how is the Type II solution set of one prime p spread over dyadic parameter blocks?

Type II, a <= b: 4abd = p + e, a + b = ce. Row II{a,d} of Lemma 2.1: f = 4acd - 1 divides p + 4a^2 d with
f = -1 mod 4ad. With a <= b, a^2 d <= p/4 + a/2, so the loop over (a,d) is finite (~0.4 p pairs).
Blocks: (floor log2 a, floor log2 c, floor log2 d). Output: total count, number of nonempty blocks, the max per
block, and the share of the largest block; plus the count carried by a,c,d all <= 2^k (small boxes).
Usage: rt2_blocks.py p1 p2 ...   (p prime)
"""
import sys
from collections import Counter
from sympy import divisors, isprime


def typeII(p):
    sols = []
    a = 1
    while 4*a*a <= p + 2*a:
        d = 1
        while 4*a*a*d <= p + 2*a:
            N = p + 4*a*a*d
            q = 4*a*d
            for f in divisors(N):
                if (f + 1) % q == 0:
                    c = (f + 1)//q
                    e = N//f
                    b = c*e - a
                    if b >= a:
                        assert 4*a*b*d == p + e
                        sols.append((a, b, c, d, e))
            d += 1
        a += 1
    return sols


def main():
    for p in map(int, sys.argv[1:]):
        assert isprime(p)
        S = typeII(p)
        blk = Counter((a.bit_length()-1, c.bit_length()-1, d.bit_length()-1) for a, b, c, d, e in S)
        mx = max(blk.values()) if blk else 0
        small = {k: sum(1 for a, b, c, d, e in S if max(a, c, d) < 2**k) for k in (2, 4, 6)}
        print(f"p={p} p%840={p % 840} f_II(a<=b)={len(S)} nonempty blocks={len(blk)} "
              f"max/block={mx} top3={blk.most_common(3)} small boxes max(a,c,d)<2^k: {small}")


if __name__ == "__main__":
    main()
