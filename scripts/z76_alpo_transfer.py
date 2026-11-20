"""Exact small F1--F4 transfer checks. Standard library, no prime tables."""
from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt


@lru_cache(None)
def factors(n):
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            v = 0
            while n % d == 0:
                n //= d
                v += 1
            out.append((d, v))
        d += 1
    return tuple(out + ([(n, 1)] if n > 1 else []))


def divisors(n):
    ds = [1]
    for l, v in factors(n):
        ds = [a*l**j for a in ds for j in range(v+1)]
    return ds


def jac(a, n):
    s = 1
    for l, v in factors(n):
        if a % l == 0:
            return 0
        if v % 2 and pow(a % l, (l-1)//2, l) != 1:
            s = -s
    return s


def screen(n):
    r = r8 = nb = ng = forced = 0
    bm = gen = Fraction(0)
    for u in range(1, (n+1)//3+1):
        for b in range(1, (n+u)//(4*u-1)+1):
            q = 4*u*b
            a = -u-b
            r += (n-a) % q == 0
            r8 += (n-a) % (2*q) == 0
            if gcd(a, q) != 1 or gcd(n, q) != 1:
                continue
            phi, index = q, 1
            inside = True
            for l, v in factors(q):
                phi -= phi//l
                if l == 2:
                    index *= 2**min(v-1, 2)
                    inside &= (n-a) % (2**min(3,v)) == 0
                else:
                    index *= 2
                    inside &= pow(n*a % l, (l-1)//2, l) == 1
            if jac(-q, n) == -1:
                nb += 1
                bm += Fraction(2, phi)
                assert phi > 2
            if inside:
                ng += 1
                gen += Fraction(index, phi)
                forced += phi == index
    # Independent divisor search over C <= (n+2)/4 (minimum at u=b=1).
    ds = [(c, d) for c in range(1, (n+2)//4+1)
          for d in divisors(4*c*n+1) if (d+1) % (4*c) == 0]
    assert (r,r8) == (len(ds), sum(c%2 == 0 for c,_ in ds))
    U = isqrt(isqrt(n))
    edges = [(u,b) for u in range(U+1,2*U+1) for b in range(u+1,2*U+1)
             if (n+u+b) % (u*b) == 0]
    assert len(set(x for e in edges for x in e)) == 2*len(edges)
    return r,r8,nb,ng,forced,len(edges),float(bm),float(gen)


def all_es(m,n):
    hits = []
    for x in range(n//m+1, 3*n//m+1):
        h = Fraction(m,n) - Fraction(1,x)
        for y in range(max(x, h.denominator//h.numerator+1), 2*h.denominator//h.numerator+1):
            hz = h - Fraction(1,y)
            if hz.numerator == 1 and hz.denominator >= y:
                hits.append((x,y,hz.denominator))
    return hits


def main():
    print('n R R_even BM_active genus_active genus_singletons N2(floor(n^1/4)) M_BM M_gen')
    for n in (9,25,49,81,121,193,409,2521,3361,4545,131,241):
        r,e,b,g,f,h,mb,mg = screen(n)
        print(n,r,e,b,g,f,h,f'{mb:.6f}',f'{mg:.6f}')
    for n in (131,241):
        print(f'sorted 8/{n} solutions:',all_es(8,n))


if __name__ == '__main__':
    main()
