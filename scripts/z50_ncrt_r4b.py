"""z50 ncrt Round 4 (2'): for a progression C, max over n in C (dyadic ranges) of the EXACT cheapest grouping
modulus of a U-word (pair modulus uv, or endpoint modulus tv-1 / tu-1), by direct enumeration of moduli <= B.
Bounded growth suggests a finite covering; growth with n suggests cl(C) meets A_inf (EVIDENCE only).
Usage: python3 z50_ncrt_r4b.py a M NMAX BMAX"""
import sys
a, M, NMAX, BMAX = map(int, sys.argv[1:5])
def isU(n, t, u, v):
    return t >= 1 and u >= 1 and v >= 1 and t*u-1 > 1 and t*v-1 > 1 and t*u*v-u-v == n and \
        any(e % 4 == 0 or (e + n) % 8 == 0 for e in (u, v))
def cheapest(n):
    for g in range(2, BMAX + 1):
        # pair classes with uv = g
        for u in range(1, g + 1):
            if g % u: continue
            v = g // u
            if (n + u + v) % g == 0 and isU(n, (n + u + v) // g, u, v): return g
        # endpoint classes with A = g: v | g+1, g | n+v
        A = g
        for v in range(1, A + 2):
            if (A + 1) % v == 0 and (n + v) % A == 0:
                t = (A + 1) // v; u = (n + v) // A
                if isU(n, t, u, v): return g
    return None
lo = 1000
while lo < NMAX:
    hi = min(2 * lo, NMAX); mx = 0; argmx = None; cnt = 0; none = 0
    for n in range(a + ((lo - a) // M + 1) * M, hi, M):
        g = cheapest(n); cnt += 1
        if g is None: none += 1; continue
        if g > mx: mx, argmx = g, n
    print("C=%d mod %d  n in [%d,%d): %d values, max cheapest modulus %d (n=%s), none<=BMAX: %d" % (a, M, lo, hi, cnt, mx, argmx, none))
    lo = hi
