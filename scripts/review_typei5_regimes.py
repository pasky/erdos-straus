# R92 from-scratch: (1) complete enumeration of regime (ii) of TYPEI5 Prop 3.3 with u = 7^b, via the
# quadratic  x^2 + (6Tj - uK)x + (4K1 j^3 + uE) = 0  (x = -Delta > 0, K1 = 8W|lam|, K = T^2 - K1 j, E = 2K1 T j^2),
# for every (a, lam<0, j) with 8W|lam|j < T^2 and every b up to a rigorous bound;
# (2) exact verification of regime-(iii) candidates printed by review_typei5_reg3.c;
# (3) every candidate (u,a,lam,j,Delta) is pushed through the full TYPEI4 Cor 3.2 conditions.
import sys
from math import isqrt, log
from fractions import Fraction as Fr

def full_check(L, u, W, lam, j, Delta):
    """Return list of certificates (c',g,delta,P1,X) for case-B data, or [] ; also a reason string."""
    T = 2 ** (L - 4)
    if Delta == 0: return [], "Delta=0"
    rho = Fr(2 * lam * (T * u + 2 * j), Delta)
    if rho.denominator != 1 or rho <= 0: return [], "rho"
    rho = int(rho); m = rho * j - lam * u; y = T * u // 2 - j
    if m <= 0 or m % 2 == 0 or y <= 0: return [], "m/y"
    num = y * y - 2 * W * m * u * j
    if num <= 0 or num % m: return [], "P1"
    P1 = num // m; z = T * u // 2 + j
    if rho * P1 != z or P1 % 7 == 0: return [], "z"
    certs = []
    for dl in range(1, isqrt(m) + 1, 2):
        if m % (dl * dl): continue
        cp = m // (dl * dl)
        if cp % 7 == 0 or y % (cp * dl): continue
        g = y // (cp * dl)
        if P1 != cp * g * g - 2 * W * u * j: continue
        Xn = 1 + W * u * rho
        if Xn % (4 * cp * g): continue
        X = Xn // (4 * cp * g)
        if X % 2 and X % 7:
            certs.append((cp, g, dl, P1, X))
    return certs, "shape" if not certs else "CERT"

def is7pow(n):
    if n < 1: return False
    while n % 7 == 0: n //= 7
    return n == 1

def regime2(L):
    T = 2 ** (L - 4); found = []; ncase = 0
    W = 7
    while 8 * W < T * T:
        l = 1
        while 8 * W * l < T * T:
            for j in range(1, T * T, 2):
                if 8 * W * l * j >= T * T: break
                ncase += 1
                K1 = 8 * W * l; K = T * T - K1 * j; E = 2 * K1 * T * j * j
                C = E * E + 6 * T * j * E * K + 4 * K1 * j ** 3 * K * K
                xmax = (C + E) // K
                Nmax = xmax * xmax + 6 * T * j * xmax + 4 * K1 * j ** 3
                bmax = int(log(Nmax) / log(7)) + 2
                for b in range(0, bmax + 1):
                    u = 7 ** b
                    B = 6 * T * j - u * K; Cc = 4 * K1 * j ** 3 + u * E
                    D = B * B - 4 * Cc
                    if D < 0: continue
                    r = isqrt(D)
                    if r * r != D: continue
                    for x2 in (-B + r, -B - r):
                        if x2 > 0 and x2 % 2 == 0:
                            x = x2 // 2
                            if K * x - E > 0:
                                found.append((u, W, -l, j, -x))
            l += 1
        W *= 49
    return ncase, found

if __name__ == "__main__":
    L = int(sys.argv[1]); T = 2 ** (L - 4)
    ncase, found = regime2(L)
    print(f"L={L} regime (ii): {ncase} (a,lam,j) cases, {len(found)} 7-power solutions of (Lin)")
    for (u, W, lam, j, D) in found:
        c, why = full_check(L, u, W, lam, j, D)
        print("   (ii) u=%d W=%d lam=%d j=%d Delta=%d -> %s %s" % (u, W, lam, j, D, why, c))
    if len(sys.argv) > 2:
        for line in open(sys.argv[2]):
            if not line.strip(): continue
            L2, a, lam, s, j = map(int, line.split()); W = 7 ** a; kap = 8 * W * lam
            g = 2 * T ** 3 - s * kap; e = g * j - s * T * T
            N = 4 * kap * j ** 3 + (2 * T * j - s) * (4 * T * j + s)
            if N % e or not is7pow(N // e):
                print("   (iii) a=%d lam=%d s=%d j=%d: false positive" % (a, lam, s, j)); continue
            u = N // e; Delta = 2 * T * j - s
            c, why = full_check(L, u, W, lam, j, Delta)
            print("   (iii) u=%d a=%d lam=%d s=%d j=%d Delta=%d -> %s %s" % (u, a, lam, s, j, Delta, why, c))
