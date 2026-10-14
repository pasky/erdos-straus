"""O211 §8 (R206 D3): ordinary reductions as bridges.  E: y^2 = x^3 + x + 1 (E(Q) = Z, trivial torsion).
For primes 5 <= h < H with h = 3 mod 4: N = #E(F_h) = h + 1 - a_h, the maximal size of a homomorphic image of
E(F_h) in F_h^* is at most g = gcd(N_exp-ish, h - 1) <= gcd(N, h - 1) (upper bound reported), and the part of E(F_h)
of order dividing m := (h+1)-part can only map to {+-1}: gcd(gcd(N, h+1), h-1) <= 2 is checked.
Reports: share of h with gcd(N, h-1) >= sqrt(h) (large image possible), #h with a_h = 0, and violations (must be 0).
Usage: PYTHONPATH=scripts uv run python scripts/y3_ordinary.py H"""
import sys, math
from sympy import primerange

def count(h):
    sq = [0]*h
    for y in range(h): sq[y*y % h] += 1
    return 1 + sum(sq[(x*x*x + x + 1) % h] for x in range(h))

if __name__ == "__main__":
    H = int(sys.argv[1]); n = big = ss = bad = 0
    for h in primerange(5, H):
        if h % 4 != 3 or (4 + 27) % h == 0: continue
        N = count(h); n += 1
        if N == h + 1: ss += 1
        if math.gcd(N, h - 1) >= math.isqrt(h): big += 1
        if math.gcd(math.gcd(N, h + 1), h - 1) > 2: bad += 1
    print(f"H={H}: h=3 mod 4 primes={n}; supersingular (a_h=0)={ss}; gcd(#E, h-1) >= sqrt h: {big}; (h+1)-part reaching F_h^* beyond +-1: {bad}")
