"""Opus review: own exhaustive fibre check 4abcd=a+b+nc at n=c^2+r, even c.
Enumerate e=(a+b)/c (e = -n mod 4), a<=b, a*c*e<=n; d=(n+e)/(4ab)."""
import sys
def pts(n, c):
    out = []
    e = (-n) % 4 or 4
    while e*c <= n:
        for a in range(1, min(c*e//2, n//(c*e)) + 1):
            b = c*e - a
            if (n + e) % (4*a*b) == 0:
                d = (n + e)//(4*a*b); assert 4*a*b*c*d == a + b + n*c
                out.append((a, b, d))
        e += 4
    return out
CMAX = int(sys.argv[1])
for r in (1, 3, 5, 9, 13, 17, 21):
    hit = [c for c in range(2, CMAX + 1, 2) if pts(c*c + r, c)]
    print('r', r, 'even c<=', CMAX, 'with points:', len(hit), hit[:12])
