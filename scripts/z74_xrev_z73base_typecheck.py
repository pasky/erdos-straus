"""z74 cross-review (Opus) of Z73_PID_SQUARE.md section 4: independent brute-force check.

For n = t^2 (t odd, 3 <= t <= TMAX) enumerate ALL solutions 4/n = 1/x + 1/y + 1/z (x<=y<=z) and classify each
as strict Type I (n divides exactly one denominator, coprime to the other two), strict Type II (n divides two,
coprime to the third), or other.  Elsholtz-Tao Prop. 1.6 predicts zero strict Type I/II solutions; the total
count shows the strictness hypothesis is not vacuous.  As a control, the same classifier is run on odd
non-squares, where strict Type I/II solutions should usually exist.
"""
import sys
from math import gcd


def solutions(n):
    out = []
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        a, b = 4 * x - n, n * x          # 4/n - 1/x = a/b
        if a <= 0:
            continue
        g = gcd(a, b); a //= g; b //= g
        ylo = max(x, -(-b // a))
        yhi = (2 * b) // a
        for y in range(ylo, yhi + 1):
            num, den = b * y, a * y - b   # z = b*y/(a*y-b)
            if den > 0 and num % den == 0:
                z = num // den
                if z >= y:
                    out.append((x, y, z))
    return out


def classify(n, s):
    div = [d % n == 0 for d in s]
    cop = [gcd(d, n) == 1 for d in s]
    k = sum(div)
    strict = all(dv or cp for dv, cp in zip(div, cop))
    if strict and k == 1:
        return "I"
    if strict and k == 2:
        return "II"
    return "other"


def main():
    tmax = int(sys.argv[1]) if len(sys.argv) > 1 else 41
    bad = 0
    for t in range(3, tmax + 1, 2):
        n = t * t
        sols = solutions(n)
        for s in sols:
            assert 4 * s[0] * s[1] * s[2] == n * (s[0] * s[1] + s[1] * s[2] + s[0] * s[2])
        cl = [classify(n, s) for s in sols]
        nI, nII = cl.count("I"), cl.count("II")
        bad += nI + nII
        print(f"n={n:5d}=t^2 t={t:3d}: total={len(sols):5d} strictI={nI} strictII={nII}")
    ctrl = [15, 21, 33, 35, 39, 45, 51, 55, 57, 63, 65, 69, 75, 77, 85, 87, 91, 93, 95, 99, 105, 111, 115, 117, 119]
    for n in ctrl:
        cl = [classify(n, s) for s in solutions(n)]
        print(f"control n={n}: strictI={cl.count('I')} strictII={cl.count('II')} other={cl.count('other')}")
    print("STRICT TYPE I/II AT ODD SQUARES:", bad)
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
