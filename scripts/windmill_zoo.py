"""Zoo of ES-flavoured finite sets S(p): report the fraction of primes
p = 1 (mod 24) for which |S(p)| is odd (WINDMILL.md §3.5).  A set that is odd
for every p would be a candidate for a windmill argument.

uv run python windmill_zoo.py 20000
"""
import sys
from math import isqrt, gcd
from sympy import primerange, divisors


def zoo(p):
    t = (p - 1) // 4
    S = {}
    r = isqrt(p)
    # Z: Zagier set x^2+4yz=p (control, provably odd)
    S['Zagier x^2+4yz=p'] = sum(len(divisors((p - x * x) // 4)) for x in range(1, r + 1, 2))
    # forms [U,4a,W], UW-4a^2=p, U = eps mod 4a, U>=4a-1 ; a <= A
    for A_name, A in (('sqrt', r), ('t/4', t // 4)):
        for eps in (-1, 1):
            c = 0
            for a in range(1, A + 1):
                N = p + 4 * a * a
                for U in divisors(N):
                    if U >= 4 * a - 1 and (U - eps) % (4 * a) == 0:
                        c += 1
            S[f'UW-4a^2=p, U={eps:+d} mod 4a, a<={A_name}'] = c
    # reduced forms of disc -4p with b = 0 mod 4 and U = 3 mod 4 / U = -1 mod b
    red = []
    a = 1
    while 3 * a * a <= 4 * p:
        for b in range(-a + 1, a + 1):
            if (b * b + 4 * p) % (4 * a) == 0:
                cc = (b * b + 4 * p) // (4 * a)
                if cc >= a and not (cc == a and b < 0) and b % 2 == 0:
                    red.append((a, b, cc))
        a += 1
    S['reduced forms -4p'] = len(red)
    S['reduced, a=3 mod 4'] = sum(1 for f in red if f[0] % 4 == 3)
    S['reduced, b=0 mod 4'] = sum(1 for f in red if f[1] % 4 == 0)
    S['reduced, b>0, a=-1 mod b'] = sum(1 for f in red if f[1] > 0 and (f[0] + 1) % f[1] == 0)
    # window divisor sets
    for L in (1, 2, 3, 5, 8, 13):
        cp = cm = 0
        for x in range(t + 1, t + 1 + L):
            q = 4 * x - p
            for D in divisors(x * x):
                if (D + x) % q == 0: cp += 1
                if (D - x) % q == 0: cm += 1
        S[f'window L={L}: D|x^2, D=-x (q)'] = cp
        S[f'window L={L}: D|x^2, D=+x (q)'] = cm
        S[f'window L={L}: D|x^2, D=+-x (q)'] = cp + cm
    # Type I chart box a in [1-t,t], |h|<=H (signed Type I incidences), via e | x^2
    for H in (1, 2, 5):
        c = 0
        for a in range(1 - t, t + 1):
            x = t + a
            if x == 0 or x % p == 0: continue
            for h in range(-H, H + 1):
                e = (4 * a - 1) * h - a
                if e and (x * x) % e == 0 and p * h - t != 0:
                    c += 1
        S[f'TypeI chart |h|<={H}'] = c
    # 1/x+1/y+2/z = 4/p, z odd, ordered (x,y)  (odd by swap argument)
    return S


def main():
    hi = int(sys.argv[1])
    ps = [p for p in primerange(25, hi) if p % 24 == 1]
    tot = None
    for p in ps:
        S = zoo(p)
        if tot is None: tot = {k: 0 for k in S}
        for k, v in S.items(): tot[k] += v % 2
    for k, v in tot.items():
        flag = '  <== ALWAYS ODD' if v == len(ps) else ('  <== always even' if v == 0 else '')
        print(f'{k:45s} odd {v}/{len(ps)}{flag}')


if __name__ == '__main__':
    main()
