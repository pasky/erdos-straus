"""z65 LOGIC2 kill test K1: the landing/coprimality lemma of Theorem T (Lemma 3.4 of Z65_LOGIC2.md).

Given D (even), a target (a1, a2) mod D with a1 + i a2 = w0^2, N(w0) a unit mod D, and Y in Z[b1, b2] not divisible by
n = b1^2 + b2^2, the lemma's recipe picks t = t0 (mod D) with G(t^2) != 0, where G(T) = Y(-2T, -2iT) in Z[i][T],
collects the primes P of D and of the norm N(G(t^2)), chooses s by CRT (s = s0 mod D, s = 1 mod r if r | t,
s = 0 mod r otherwise, for r in P not dividing D; s = 1 mod the other primes of t), and lands at
b = (s^2 - t^2, 2st), ell = s^2 + t^2.  Claims checked: b = (a1, a2) mod D, ell odd, gcd(s, t) = 1, gcd(Y(b), ell) = 1.
Usage: uv run --with sympy python scripts/z65_logic2_landing.py [TRIALS] [SEED]
"""
import random
import sys
from math import gcd

from sympy import factorint
from sympy.ntheory.modular import crt

TRIALS = int(sys.argv[1]) if len(sys.argv) > 1 else 300
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 6565
rng = random.Random(SEED)

YS = {
    "b1": {(1, 0): 1},
    "b1+b2": {(1, 0): 1, (0, 1): 1},
    "n+b1": {(2, 0): 1, (0, 2): 1, (1, 0): 1},
    "(b1+1)n+5": {(3, 0): 1, (1, 2): 1, (2, 0): 1, (0, 2): 1, (0, 0): 5},
    "b1^2-b2^2+7b1b2-3": {(2, 0): 1, (0, 2): -1, (1, 1): 7, (0, 0): -3},
    "n^2+n+1": {(4, 0): 1, (2, 2): 2, (0, 4): 1, (2, 0): 1, (0, 2): 1, (0, 0): 1},
    "b1*b2": {(1, 1): 1},
}


def ev(Y, x, y):
    return sum(c * x ** i * y ** j for (i, j), c in Y.items())


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gpow(a, k):
    r = (1, 0)
    for _ in range(k):
        r = gmul(r, a)
    return r


def G_at(Y, T):
    """Y(-2T, -2iT) as a Gaussian integer."""
    tot = (0, 0)
    for (i, j), c in Y.items():
        term = gmul(gpow((-2 * T, 0), i), gpow((0, -2 * T), j))
        tot = (tot[0] + c * term[0], tot[1] + c * term[1])
    return tot


def trial(Y, D):
    while True:
        s0, t0 = rng.randrange(D), rng.randrange(D)
        if gcd(s0 * s0 + t0 * t0, D) == 1:
            break
    a1, a2 = (s0 * s0 - t0 * t0) % D, (2 * s0 * t0) % D
    t = t0 + D * rng.randrange(1, 50)
    g = G_at(Y, t * t)
    N = g[0] ** 2 + g[1] ** 2
    if N == 0:
        return None
    P = set(factorint(N)) | set(factorint(D))
    mods, res = [D], [s0]
    for r in sorted(P | set(factorint(t))):
        if D % r == 0:
            continue
        mods.append(r)
        res.append(1 if (t % r == 0 or r not in P) else 0)
    s = int(crt(mods, res)[0]) + rng.randrange(0, 5) * (eval("*".join(map(str, mods))))
    ell = s * s + t * t
    b1, b2 = s * s - t * t, 2 * s * t
    ok_res = (b1 - a1) % D == 0 and (b2 - a2) % D == 0
    return ok_res, ell % 2 == 1, gcd(s, t) == 1, gcd(ev(Y, b1, b2), ell) == 1


def main():
    Ds = [8 * 3 * 5 * 7, 8 * 9 * 5 * 13, 16 * 3 * 17, 8 * 105 * 11]
    print(f"# trials per (Y, D) = {TRIALS}, seed {SEED}")
    allok = True
    for name, Y in YS.items():
        for D in Ds:
            cnt = [0, 0, 0, 0]
            done = 0
            for _ in range(TRIALS):
                r = trial(Y, D)
                if r is None:
                    continue
                done += 1
                for k in range(4):
                    cnt[k] += r[k]
            good = all(c == done for c in cnt)
            allok &= good
            print(f"{name:20s} D={D:6d} trials={done:4d} residue_ok={cnt[0]} ell_odd={cnt[1]} "
                  f"gcd(s,t)=1:{cnt[2]} gcd(Y(b),ell)=1:{cnt[3]} {'PASS' if good else 'FAIL'}")
    print("ALL PASS" if allok else "SOME FAIL")


if __name__ == "__main__":
    main()
