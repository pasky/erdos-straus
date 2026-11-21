"""Small exact controls for the primorial moment and the 4/8 split (stdlib)."""
from fractions import Fraction
from itertools import combinations_with_replacement, product
from math import gcd, isqrt, lcm, prod


def divisors(n):
    lo = [d for d in range(1, isqrt(n) + 1) if n % d == 0]
    return lo + [n // d for d in reversed(lo) if d != n // d]


def phi(n):
    return sum(gcd(i, n) == 1 for i in range(1, n + 1))


def solutions(n, m):
    """x<=y<=z: (Ay-H)(Az-H)=H^2 for m/n-1/x=A/H."""
    for x in range(n // m + 1, 3 * n // m + 1):
        h = Fraction(m, n) - Fraction(1, x)
        A, H = h.numerator, h.denominator
        for t in divisors(H * H):
            if t > H:
                break
            if (t + H) % A or (H * H // t + H) % A:
                continue
            y, z = (H + t) // A, (H + H * H // t) // A
            if x <= y:
                assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(m, n)
                yield x, y, z


def star(n):
    # smaller outer letter, C>=1, implies 4a^2-2a<=n.
    for a in range(1, (1 + isqrt(1 + 4 * n)) // 4 + 1):
        for f in divisors(n + a):
            if (f + 1) % (4 * a) == 0 and (n + a) // f >= a:
                yield a, (n + a) // f, (f + 1) // (4 * a)


def first7(n):
    # r|f+1, r<f implies r<=(f+1)/2; f<=n+r implies f<=2n+1.
    for f in range(7, 2 * n + 2, 8):
        a = -n % f
        if a and (f + 1) % a == 0:
            return f, a, (f + 1) // a, (n + a) // f
    return None


def candidate(a, c, d):
    f = 4*a*c*d - 1
    return f, -a * pow(c, -1, f) % f


def crt_checks():
    # Compare the telescoping multiplier with the exact conditional CRT probability
    # times f, correcting only for unconstrained primes dividing f.
    checks = 0
    for q, e in [(3, 3), (5, 2), (7, 1)]:
        m = q ** e
        for r, a, c, d in product(range(1, m), range(1, 9), range(1, 7), range(1, 12)):
            if r % q == 0 or gcd(a, c) != 1:
                continue
            f, x = candidate(a, c, d)
            g = gcd(m, f)
            val = val_phi = 1
            for j in range(1, e + 1):
                h = q**j
                if f % h == 0:
                    val += h * ((x-r) % h == 0) - (h//q) * ((x-r) % (h//q) == 0)
                    val_phi += phi(h) * ((x-r) % h == 0) - phi(h//q) * ((x-r) % (h//q) == 0)
            assert val == g * ((x-r) % g == 0)
            assert val_phi == phi(g) * ((x-r) % g == 0)
            checks += 1
    print('local signed expansions:', checks)
    base = 24
    atoms = [candidate(a, c, d) for a,c,d in product(range(1,5),range(1,4),range(1,4))
             if gcd(a,c)==1 and 4*a*c*d-1 in (3,7,11,15,23,35)]
    M = lcm(base, *(f for f,x in atoms))
    units = [t for t in range(1,M,base) if gcd(t,M)==1]
    hits = [sum((t-x)%f==0 for f,x in atoms) for t in units]
    moments = [Fraction(sum(h**j for h in hits),len(hits)) for j in (1,2)]
    from functools import lru_cache
    ph = lru_cache(None)(phi)
    def prob(system):
        if any((a-b)%gcd(f,g) for (f,a),(g,b) in combinations_with_replacement(system,2)):
            return Fraction()
        return Fraction(ph(base),ph(lcm(*(f for f,r in system))))
    assert moments == [sum(prob(((base,1),)+v) for v in product(atoms,repeat=j)) for j in (1,2)]
    print('small CRT fibre:', base, M, len(atoms), len(units), *moments)
    beta = {f: prod(Fraction(q-1,q) for q in (5,7,11,23) if f%q==0) for f,x in atoms}
    weighted = [sum(beta[f] for f,x in atoms if (t-x)%f==0) for t in units]
    for j in (1,2):
        direct = sum(h**j for h in weighted)/len(units)
        model = sum(prod(beta[f] for f,x in v)*prob(((base,1),)+v) for v in product(atoms,repeat=j))
        assert direct == model
        print('weighted moment',j,model)


if __name__ == '__main__':
    crt_checks()
    for n in (131,241):
        four, eight = list(solutions(n,4)), list(solutions(n,8))
        print('4 vs 8', n, 'sorted triples',len(four),len(eight), 'even-only',sum(not any(v%2 for v in t) for t in four))
        for j in (1,2):
            sub = [t for t in four if sum(v%n==0 for v in t)==j]
            print('  type',j,'odd denominator histogram', [sum(sum(v%2 for v in t)==s for t in sub) for s in range(4)], 'first',sub[:1])
        print('  star',list(star(n)))
        assert not eight and all(any(v%2 for v in t) for t in four)
    zeros = (409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281,17401609)
    for n in zeros:
        assert not list(star(n))
        w = first7(n)
        assert w and n == w[1]*w[2]*w[3]-w[1]-w[3]
        print('star zero',n,'first U7 (f,x,y,z)',w)
    for n in (9,25,49,81,105,1465,3865,4545,10305,12145,39361,67425):
        assert not list(star(n)) and first7(n) is None
    n = 1590284203561
    for a,b,C in [(15,26984,982239),(24,834911,19841),(24,1904735,8697)]:
        assert n == 4*a*b*C-a-b and C%2
    print('R8 record: 3 inherited odd-C examples replayed, not a new exhaustive count')
