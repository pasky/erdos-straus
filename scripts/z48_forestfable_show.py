#!/usr/bin/env python3
"""z48 forestfable — print the forest F_p of one prime with colours, classes and components."""
import sys
from math import isqrt
from sympy import factorint, legendre_symbol, isprime


def edges(p):
    out = []
    for u in range(1, isqrt(p + 1) + 3):
        n = p + u
        r = (-p) % u
        f = factorint(n)
        divs = [1]
        for q, e in f.items():
            divs = [d * q ** k for d in divs for k in range(e + 1)]
        for v in sorted(divs):
            if v > u and v % u == r and (p + u + v) % (u * v) == 0:
                out.append((u, v))
    return out


def main():
    p = int(sys.argv[1])
    assert isprime(p) and p % 4 == 1
    E = edges(p)
    chi = lambda x: int(legendre_symbol(x % p, p))
    comp = {}
    par = {}

    def find(x):
        while par.get(x, x) != x:
            x = par[x]
        return x

    for u, v in E:
        par.setdefault(u, u); par.setdefault(v, v)
        a, b = find(u), find(v)
        if a != b:
            par[max(a, b)] = min(a, b)
    print(f"p = {p} ≡ {p%24} (mod 24), least QNR r = {next(x for x in range(2, p) if chi(x) == -1)}, {len(E)} edges")
    print(" u     v     t    A=(p+u)/v  A*=(p+v)/u  chi(u) chi(v)  bi  slots              root")
    for u, v in E:
        t = (p + u + v) // (u * v)
        A, As = (p + u) // v, (p + v) // u
        bi = chi(u) * chi(v) == -1
        slots = [name for name, val in (("t", t), ("u", u), ("v", v), ("tu-1", t * u - 1), ("tv-1", t * v - 1)) if val % 4 == 0]
        mark = "*" if bi else " "
        pa = "p" if isprime(A) else " "
        pas = "p" if isprime(As) else " "
        print(f"{u:5d} {v:6d} {t:5d} {A:8d}{pa} {As:9d}{pas}   {chi(u):+d}    {chi(v):+d}    {mark}  {','.join(slots):16s}  {find(u)}")
    roots = sorted(set(find(x) for x in par))
    print("components (root: size, bichromatic?):")
    for rt in roots:
        members = [x for x in par if find(x) == rt]
        cols = set(chi(x) for x in members)
        print(f"  {rt}: size {len(members)}, colours {sorted(cols)}, members {sorted(members)[:12]}{'...' if len(members)>12 else ''}")


if __name__ == "__main__":
    main()
