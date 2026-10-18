"""s9_sign.py (O271): the Jacobi sign of a word.  For w = (t,u,v) in W(n): X = tu - 1, Y = tv - 1, XY = tn + 1 == 1 (mod n),
so sigma(w) := (X/n) = (Y/n) (Jacobi), and sigma == +1 at odd squares.  Checks: does every word with a coordinate == 0 (mod 4)
have sigma = -1 (primes p == 1 (4))?  Tabulates W+ / W- / U at primes and odd squares.  usage: python s9_sign.py PMAX"""
import sys
from math import isqrt
sys.argv, PMAX = sys.argv[:1] + ["1", "1"], int(sys.argv[1])
exec(open(__file__.replace("s9_sign.py", "s9_words.py")).read().split("def main")[0])

def jacobi(a, n):
    a %= n; t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: t = -t
        a %= n
    return t if n == 1 else 0

def isprime(n):
    return n > 1 and all(n % q for q in range(2, isqrt(n) + 1))

def stats(n):
    W = words(n); Wp = Wm = U = Ubad = 0; t4 = v4 = 0; t4m = v4m = 0
    for t, u, v in W:
        s = jacobi(t * u - 1, n)
        if s == 1: Wp += 1
        else: Wm += 1
        if t % 4 == 0 or u % 4 == 0 or v % 4 == 0:
            U += 1
            if s != -1: Ubad += 1
    return len(W), Wp, Wm, U, Ubad

agg = {"prime1": [0]*5, "prime3": [0]*5, "square": [0]*5}
for n in range(5, PMAX, 2):
    if isprime(n):
        key = "prime1" if n % 4 == 1 else "prime3"
    elif isqrt(n) ** 2 == n:
        key = "square"
    else:
        continue
    s = stats(n)
    agg[key] = [a + b for a, b in zip(agg[key], s)]
for k, (W, Wp, Wm, U, Ub) in agg.items():
    print(f"{k}: words {W}, sigma=+1: {Wp}, sigma=-1: {Wm}, with coord==0(4): {U}, of which sigma=+1: {Ub}, U/W- = {U/max(Wm,1):.3f}")
