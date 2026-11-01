"""z53_hyp2cycle_controls.py — FRONTIER §4 item-14 test primes, odd squares, near-squares.
For each n: all 'balanced' forest edges {u<B} with B < 2u (i.e. u,B in a common window (U,2U]), uB | n+u+B,
k=(n+u+B)/(uB); report counts by layer: all (N2-type), 4|k ((★)), five-slice, and the balanced-block counts at
U = floor(n^(1/4)).  Enumeration: for each B, u runs over divisors of n+B in (B/2, B) (sympy divisors).
usage: uv run --with sympy python scripts/z53_hyp2cycle_controls.py"""
from sympy import divisors, isprime, integer_nthroot
import json, sys

def edges(n):
    out = []
    for B in range(2, n + 3):
        for u in divisors(n + B):
            if 2 * u > B and u < B and (n + u + B) % (u * B) == 0:
                out.append((u, B, (n + u + B) // (u * B)))
    return out

def five(u, B, k):
    return k % 4 == 0 or u % 4 == 0 or B % 4 == 0 or (k * u - 1) % 4 == 0 or (k * B - 1) % 4 == 0

def row(n):
    E = edges(n)
    U = integer_nthroot(n, 4)[0]
    bal = [(u, B, k) for (u, B, k) in E if U < u and B <= 2 * U]
    return dict(n=n, prime=isprime(n), n_mod_4=n % 4, edges=len(E), star=sum(k % 4 == 0 for *_, k in E),
                five=sum(five(*e) for e in E), U=U, N2=len(bal), N4=sum(k % 4 == 0 for *_, k in bal),
                N5=sum(five(*e) for e in bal))

if __name__ == "__main__":
    test = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 193, 2521, 66529, 3361]
    sq = [m * m for m in (21, 45, 101, 315, 1001, 3003)]
    near = [n for m in (100, 301, 1000) for n in (m * m - 4, m * m - 2, m * m + 2, m * m + 4, m * m + 6) if n % 2]
    res = {"test": [row(n) for n in test], "squares": [row(n) for n in sq], "near": [row(n) for n in near]}
    for kname, rows in res.items():
        for r in rows: print(kname, r)
    json.dump(res, open(sys.argv[1] if len(sys.argv) > 1 else "/dev/null", "w"), indent=1)
