"""NL7 Theorem NL+ illustration on the quartic curve p = t^4 + 1, t ≡ 0 (mod M0):
there (a,b) = (1,t^2), (c,d) = (t^2-1,t) [p = c^2+2d^2], (e,f) = (t^2+1,t) [p = e^2-2f^2], Pell (T,S) = (t^2,1).
Rule J (E(0) != 0): letters dividing c = t^2-1, e = t^2+1, |c±d| = t^2±t-1, e±f = t^2±t+1.
Reports the primes where NO U7 word has a letter dividing one of these expressions.
For y = L with L*p+1 too large to factor quickly we enumerate min(x,z) <= sqrt(p/L)+2 directly.
usage: quartic.py RULE M0 J0 J1 out
"""
import sys
sys.path.insert(0, 'scripts')
from z69_nl7_lib import *
from sympy import divisors, isprime
from math import isqrt

RULES4 = {
 'c': lambda t: [t*t - 1],
 'J': lambda t: [t*t - 1, t*t + 1, t*t + t - 1, t*t - t - 1, t*t + t + 1, t*t - t + 1],
}

def y_words_enum(n, L):
    out = []
    for x in range(1, isqrt(n // L) + 3):
        d = x * L - 1
        if d > 0 and (n + x) % d == 0:
            z = (n + x) // d
            if (x * L) % 8 == 0 or (z * L) % 8 == 0:
                out.append((x, L, z))
    return out

def has_letter(n, L):
    d1 = divisors(n + L)
    if words_with_x(n, L, d1) or words_with_z(n, L, d1):
        return True
    if L * n + 1 < 10**23:
        return bool(words_with_y(n, L))
    return bool(y_words_enum(n, L))

def main(rule, M0, J0, J1, out):
    E = RULES4[rule]
    nprime = nfail = 0
    fh = open(out, 'w')
    fh.write(f"# quartic curve p = t^4+1, t = {M0}*j, j in [{J0},{J1}); rule {rule}\n# FAIL t p #letters\n")
    for j in range(J0, J1):
        t = M0 * j
        p = t**4 + 1
        if not isprime(p):
            continue
        nprime += 1
        letters = set()
        for e in E(t):
            letters |= {d for d in divisors(e) if d <= p + 2}
        ok = False
        for L in sorted(letters):
            if has_letter(p, L):
                ok = True; break
        if not ok:
            nfail += 1
            fh.write(f"FAIL {t} {p} {len(letters)}\n"); fh.flush()
    fh.write(f"# primes {nprime} failures {nfail}\n")
    fh.close()
    print(f"quartic rule {rule} M0={M0} j in [{J0},{J1}): primes {nprime}, failures {nfail}")

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])
