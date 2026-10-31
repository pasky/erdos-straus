# z52b pass1 U00: exact enumerator of all solutions of 4/n = 1/x + 1/y + 1/z with x ≤ y ≤ z (positive integers), via
# x ∈ (n/4, 3n/4] and the 2-term step (a y − b)(a z − b) = b², a = 4x − n, b = n x (divisors of b²). cypari2 factorisation.
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2 * 10 ** 9)
def _divs_sq(b):
    f = pari.factor(b)
    ps = [(int(f[0][i]), int(f[1][i])) for i in range(len(f[0]))]
    ds = [1]
    for q, e in ps:
        ds = [d * q ** k for d in ds for k in range(2 * e + 1)]
    return ds
def solutions(n):
    out = set()
    for x in range((n + 3) // 4, (3 * n) // 4 + 1):
        a = 4 * x - n
        if a <= 0 or x * n == 0: continue
        b = n * x
        if (b * b) % 1 or a == 0: continue
        for d in _divs_sq(b):
            if (d + b) % a: continue
            dp = b * b // d
            if (dp + b) % a: continue
            y = (b + d) // a; z = (b + dp) // a
            if y < 1 or z < 1: continue
            t = tuple(sorted((x, y, z)))
            out.add(t)
    return sorted(out)
if __name__ == '__main__':
    import sys
    for n in map(int, sys.argv[1:]):
        s = solutions(n); print(n, len(s), s[:6])
