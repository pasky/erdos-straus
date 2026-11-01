# z53 HCSHIFTS: Proposition W3 check (CERTIFIED instances).
# Q_X = prod_{ell <= X+1} ell^{a_ell}, a_ell = floor(log_ell(X+1)) + 1 (and 8 | Q_X).  For primes p = 1 (mod Q_X):
#   (i)  the (X+1)-smooth part of p + x and of x p + 1 equals x + 1, for every 1 <= x <= X;
#   (ii) every certificate (d | N, d = -1 mod x) with x in C ∩ [4, X] is private-type w.r.t. y = X + 1
#        (gcd(d, r) not in {1, r}, r the (X+1)-rough part of N).
# The script verifies (i) and (ii) by full factorisation at the first K such primes, and reports HC(p) and the number
# of prime factors of the rough parts.  Exit status 1 if any claim fails.
import sys
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)

def Q_of(X):
    Q = 1
    for l in pari.primes(pari.primepi(X + 1)):
        l = int(l); a = 1
        while l ** a <= X + 1: a += 1
        Q *= l ** a
    return Q

def inC(x): return x % 4 == 0 or x % 8 == 7

def certs(N, x):
    return [int(d) for d in pari.divisors(N) if int(d) % x == x - 1]

def rough(N, y):
    f = pari.factor(N); r = 1
    for i in range(len(f[0])):
        l, e = int(f[0][i]), int(f[1][i])
        if l > y: r *= l ** e
    return r

def main():
    bad = 0
    for X, K in [(16, 3), (20, 3), (24, 2), (32, 2)]:
        Q = Q_of(X); y = X + 1
        print(f"== X={X}: log Q_X = {float(pari.log(Q)):.2f}, Q_X/X-ratio log(Q)/X = {float(pari.log(Q))/X:.3f}")
        p = Q + 1; found = 0
        while found < K:
            if pari.isprime(p):
                found += 1
                hc = None; minomega = 99; ncert = 0
                for x in range(4, 400):
                    if not inC(x): continue
                    fired = False
                    for N in (p + x, x * p + 1):
                        cs = certs(N, x)
                        if x <= X:
                            r = rough(N, y)
                            if N // r != x + 1: print("  FAIL smooth part", p, x, N // r); bad += 1
                            om = len(pari.factor(r)[0]); minomega = min(minomega, om)
                            for d in cs:
                                g = pari.gcd(d, r)
                                if g == 1 or g == r: print("  FAIL congruence-type cert", p, x, d); bad += 1
                            ncert += len(cs)
                        if cs: fired = True
                    if fired and hc is None: hc = x
                    if hc is not None and x > X: break
                print(f"  p = {p}  (log p = {float(pari.log(p)):.1f}, X/log p = {X/float(pari.log(p)):.3f})  HC = {hc}; "
                      f"certificates with coordinate <= X: {ncert}, all private; min omega(rough part) over lines <= X: {minomega}")
            p += Q
    sys.exit(1 if bad else 0)

main()
