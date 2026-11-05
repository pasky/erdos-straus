# z59 MSPLUS: structured candidate generator for (MS+) counterexamples beyond the census: non-square n in Mordell
# classes (n mod 840 in M), n < 2^62, in families designed to minimise the local mean (dead moduli at q >= 11) and/or
# to be near-squares.  Output lines "n tag".  Families (FAM argument):
#   sm2   : n = s*m^2, s non-square, s mod 840 in M, s <= SMAX, m coprime to 210, m in a log-spaced set up to n < NMAX
#   deadsq: n = s*(P*k)^2, P = prod of primes 11..y (y = 13..43), s non-square in M (s <= 3000), k coprime to 210
#   dead  : n = P*k with P = prod of primes 11..y, n in M, k random; half of them also pseudo-square: n QR mod all primes
#           in (y, Y] with Y as large as the CRT modulus allows (NMAX/1000), n non-square
#   msq   : n = m^2 + 840 t, 1 <= t <= T (near-squares in M), m coprime to 210, random m up to sqrt(NMAX)
#   semi  : n = p*q, p, q primes with p*q in M, p ~ q (balanced), random sizes up to NMAX
# Usage: python z59_msplus_gen.py FAM COUNT SEED [NMAX]
import sys, random, math
from sympy import isprime, primerange, nextprime

M = {1, 121, 169, 289, 361, 529}
def inM(n): return n % 840 in M
def issq(n): r = math.isqrt(n); return r * r == n
def legendre(a, p): return pow(a % p, (p - 1) // 2, p)  # 1, p-1 or 0

def main():
    fam, count, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    NMAX = int(float(sys.argv[4])) if len(sys.argv) > 4 else 4 * 10**18
    rnd = random.Random(seed)
    out = 0
    S = [s for s in range(2, 20001) if not issq(s) and inM(s)]
    if fam == 'sm2':
        while out < count:
            s = rnd.choice(S[:200])
            mmax = math.isqrt(NMAX // s)
            m = int(math.exp(rnd.uniform(math.log(1000), math.log(mmax))))
            if math.gcd(m, 210) != 1: continue
            n = s * m * m
            if n >= NMAX or n <= 10**11: continue
            print(n, f"sm2:s={s}:m={m}"); out += 1
    elif fam == 'deadsq':
        while out < count:
            y = rnd.choice([13, 17, 19, 23, 29, 31, 37, 41, 43])
            P = math.prod(primerange(11, y + 1))
            s = rnd.choice([x for x in S if x <= 3000])
            kmax = math.isqrt(NMAX // s) // P
            if kmax < 1: continue
            k = rnd.randrange(1, kmax + 1)
            if math.gcd(k, 210) != 1: continue
            n = s * (P * k) ** 2
            if n >= NMAX or n <= 10**11: continue
            print(n, f"deadsq:s={s}:y={y}:k={k}"); out += 1
    elif fam == 'dead':
        while out < count:
            y = rnd.choice([13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
            psq = rnd.choice([0, 1])  # 1: n is also a nonzero square mod every prime > y as long as the modulus fits
            P = math.prod(primerange(11, y + 1))
            # CRT: n = 0 mod P, n = random M-class mod 840, n = random nonzero square mod consecutive primes q > y
            mods = [(P, 0), (840, rnd.choice(sorted(M)))]
            cur, q, Y = P * 840, y, y
            while psq:
                q = nextprime(q)
                if cur * q > NMAX // 1000: break
                mods.append((q, pow(rnd.randrange(1, q), 2, q))); cur *= q; Y = q
            mod, res = 1, 0
            for mq, rq in mods:
                # combine res mod mod with rq mod mq (coprime moduli)
                t = ((rq - res) * pow(mod, -1, mq)) % mq
                res += mod * t; mod *= mq
            if mod >= NMAX // 10: continue
            lo = max(10**11, mod)
            kk = rnd.randrange(lo // mod, NMAX // mod)
            n = res + kk * mod
            if n <= 10**11 or n >= NMAX or issq(n): continue
            assert n % 4 == 1 and inM(n) and n % P == 0
            print(n, f"dead:y={y}:Y={Y}"); out += 1
    elif fam == 'msq':
        while out < count:
            m = rnd.randrange(math.isqrt(10**11) + 1, math.isqrt(NMAX))
            if math.gcd(m, 210) != 1: continue
            t = rnd.randrange(1, 50)
            n = m * m + 840 * t
            if issq(n): continue
            print(n, f"msq:t={t}"); out += 1
    elif fam == 'semi':
        while out < count:
            e = rnd.uniform(11, math.log10(NMAX) - 0.01)
            r = rnd.uniform(0.0, 0.3)  # log10 imbalance
            p = nextprime(int(10 ** (e / 2 - r))); q = nextprime(int(10 ** (e / 2 + r)))
            n = p * q
            if p == q or n >= NMAX or n % 4 != 1 or not inM(n): continue
            print(n, f"semi"); out += 1
    else:
        sys.exit("unknown family")

if __name__ == '__main__':
    main()
