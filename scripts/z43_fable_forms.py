"""z43 (FABLE): sanity check of the two certificate forms I derived from scratch.

Type I  (exactly one denominator divisible by p):
    exists s,u>=1 and e | 4su^2+1 with p*e == -1 (mod 4su).
Type II (two denominators divisible by p):
    exists k,m>=1 and a divisor of 4km^2 p + 1 that is == -1 (mod 4km).
Compare with brute force over 4/p = 1/x+1/y+1/z, x<=y<=z.
"""
import sys
from sympy import primerange, divisors

def brute(p):
    # returns (hasI, hasII) by direct enumeration
    hasI = hasII = False
    # x in (p/4, 3p/4]
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        num = 4 * x - p          # 4/p - 1/x = num/(p x)
        den = p * x
        # 1/y + 1/z = num/den, y <= z, y in (den/num, 2den/num]
        for y in range(den // num + 1, 2 * den // num + 1):
            n2 = num * y - den
            if n2 <= 0:
                continue
            if (den * y) % n2 == 0:
                z = den * y // n2
                cnt = sum(1 for w in (x, y, z) if w % p == 0)
                if cnt == 1:
                    hasI = True
                elif cnt == 2:
                    hasII = True
                else:
                    raise RuntimeError((p, x, y, z, cnt))
    return hasI, hasII

def typeI(p, B):
    for s in range(1, B):
        for u in range(1, B):
            M = 4 * s * u
            if M > 4 * B * B:
                break
            N = 4 * s * u * u + 1
            for e in divisors(N):
                if (p * e + 1) % M == 0:
                    return (s, u, e)
    return None

def typeII(p, B):
    for k in range(1, B):
        for m in range(1, B):
            M = 4 * k * m
            N = 4 * k * m * m * p + 1
            for e in divisors(N):
                if e % M == M - 1:
                    return (k, m, e)
    return None

if __name__ == "__main__":
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    B = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    bad = 0
    for p in primerange(5, P):
        bI, bII = brute(p)
        cI = typeI(p, B) is not None
        cII = typeII(p, B) is not None
        # criterion with bounded search can only miss (false negative)
        if (cI and not bI) or (cII and not bII):
            print("FALSE POSITIVE", p, bI, bII, cI, cII); bad += 1
        if (bI and not cI) or (bII and not cII):
            print("missed (bounded search)", p, bI, bII, cI, cII)
    print("done, false positives:", bad)
