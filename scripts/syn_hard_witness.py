"""O171 §4: what certifies locally-square primes (n_p > Y)?  For such p (p = 1 mod 8) and for control primes
p = 1 (8) of the same size, scan Type II slices e = 3 (4) upward, find the first e with -1 in Sigma_e((p+e)/4),
and classify it: 'bigmod' (e has a prime factor > Y) or 'split' (e Y-smooth; by Thm 2.3 the witness then splits
the Y-rough part).  Usage: syn_hard_witness.py LOG10P Y COUNT SEED
"""
import sys, random
from sympy import factorint, isprime, legendre_symbol, primerange

def divs(fac):
    ds = [1]
    for q, k in fac.items():
        ds = [d * q**i for d in ds for i in range(k + 1)]
    return ds

def witness(N, e):
    fac = factorint(N)
    ds = divs(fac)
    res = {}
    for d in ds:
        res.setdefault(d % e, []).append(d)
    for a in ds:
        for b in res.get((-a) % e, []):
            if (N // a) % b == 0:
                return a, b, fac
    return None

def first(p, Y):
    e = 3
    while True:
        w = witness((p + e) // 4, e)
        if w:
            a, b, fac = w
            big = max(factorint(e)) > Y
            return e, ("bigmod" if big else "split")
        e += 4

def main():
    L, Y, C, seed = float(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    rng = random.Random(seed)
    odd = list(primerange(3, Y + 1))
    lo = int(10**L)
    hard, ctrl = [], []
    while len(hard) < C:
        p = lo + 8 * rng.randrange(lo // 8) + 1
        p -= (p - 1) % 8
        loc = all(legendre_symbol(p % q, q) == 1 for q in odd)
        if not loc and len(ctrl) >= C:
            continue
        if not isprime(p):
            continue
        (hard if loc else ctrl).append(p)
    for name, ps in (("n_p>Y", hard), ("control", ctrl[:C])):
        es, kinds = [], {}
        for p in ps:
            e, k = first(p, Y)
            es.append(e)
            kinds[k] = kinds.get(k, 0) + 1
        es.sort()
        print(f"{name}: p~1e{L}, Y={Y}, {len(ps)} primes; first-witness slice e: median {es[len(es)//2]}, "
              f"90% {es[int(.9*len(es))]}, max {es[-1]}; kinds {kinds}")

if __name__ == "__main__":
    main()
