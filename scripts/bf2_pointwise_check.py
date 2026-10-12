"""O163 Lemma 8.3 brute force: pointwise descent statements for n = lam^2 w^2.

For every positive solution of 4/n = 1/x+1/y+1/z (all orderings) check
 (a) n|x, lam||y, lam||z, gcd(w,yz)=1  =>  ( -(x/n)(y/lam)(z/lam) / lam ) = -1
 (b) n|y, n|z, lam||x, gcd(w,x)=1      =>  ( (1-4y/n) / lam ) = -1
 (c) n|x, lam^2|y, lam^2|z, gcd(w,yz)=1 never happens
 (d) n|y, n|z, lam^2|x, gcd(w,x)=1     never happens
 (e) Type I / Type II for n itself never happens (ET Prop 1.6)
and count how often the hypotheses of (a), (b) occur (non-vacuity), plus how often the
hypotheses hold but the *symbol condition* is dropped (it never can be +1).
"""
from math import gcd
import sys
from bf2_square_patterns import solutions


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def vlam(t, lam):
    k = 0
    while t % lam == 0:
        t //= lam
        k += 1
    return k


def check(lam, w):
    n = lam * lam * w * w
    cnt = dict(a=0, b=0, c=0, d=0, e=0, viol=0)
    sols = solutions(n)
    for s in sols:
        for i in range(3):
            x = s[i]
            y, z = [s[j] for j in range(3) if j != i]
            for (y, z) in ((y, z), (z, y)):
                # (a)
                if x % n == 0 and vlam(y, lam) == 1 and vlam(z, lam) == 1 and gcd(w, y * z) == 1:
                    cnt['a'] += 1
                    num = -(x // n) * (y // lam) * (z // lam)
                    if legendre(num, lam) != -1:
                        cnt['viol'] += 1
                        print("VIOLATION (a)", lam, w, x, y, z)
                # (b)
                if y % n == 0 and z % n == 0 and vlam(x, lam) == 1 and gcd(w, x) == 1:
                    cnt['b'] += 1
                    if legendre(1 - 4 * (y // n), lam) != -1:
                        cnt['viol'] += 1
                        print("VIOLATION (b)", lam, w, x, y, z)
                # (c)
                if x % n == 0 and y % (lam * lam) == 0 and z % (lam * lam) == 0 and gcd(w, y * z) == 1:
                    cnt['c'] += 1
                    cnt['viol'] += 1
                    print("VIOLATION (c)", lam, w, x, y, z)
                # (d)
                if y % n == 0 and z % n == 0 and x % (lam * lam) == 0 and gcd(w, x) == 1:
                    cnt['d'] += 1
                    cnt['viol'] += 1
                    print("VIOLATION (d)", lam, w, x, y, z)
                # (e)
                if (x % n == 0 and gcd(n, y * z) == 1) or (y % n == 0 and z % n == 0 and gcd(n, x) == 1):
                    cnt['e'] += 1
                    cnt['viol'] += 1
                    print("VIOLATION (e)", lam, w, x, y, z)
    return len(sols), cnt


if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 2500
    tot = dict(a=0, b=0, viol=0)
    for lam in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
        for w in range(1, 200, 2):
            if lam * lam * w * w > nmax:
                break
            ns, c = check(lam, w)
            print(f"lam={lam} w={w} n={lam*lam*w*w}: {ns} solutions; hyp(a) {c['a']}, hyp(b) {c['b']}, violations {c['viol']}")
            sys.stdout.flush()
            for k in tot:
                tot[k] += c[k]
    print("TOTAL", tot)
