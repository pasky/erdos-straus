"""Check mixed-radical lifting and the disc coefficient bound in small standard examples."""
from math import comb, gcd
from itertools import product


def lift(h, a, b):
    def F(x):
        return x + b*(x**3 - 7*x + 11)
    d, x, nsteps = 1, 0, 0
    while d != h:
        assert h % d == 0 and 0 <= x < d and (F(x)-a) % d == 0
        e = h//d
        g = gcd(b, e)
        if g == 1:
            return False, e, nsteps
        x += d*((-((F(x)-a)//d)) % g)
        d *= g
        nsteps += 1
    assert (F(x)-a) % h == 0 and 0 <= x < h
    return True, x, nsteps


def main():
    yes = no = depth = 0
    for h in range(1, 100):
        for b in range(-12, 13):
            success = all(gcd(d, b) > 1 for d in range(2, h+1) if h % d == 0)
            for a in range(h):
                ok, r, n = lift(h,a,b)
                assert ok == success
                depth = max(n, depth)
                if ok:
                    yes += 1
                else:
                    assert r > 1 and h % r == 0 and gcd(r,b) == 1
                    no += 1
    print(f'Mixed cubic: {yes} lifts, {no} coprime divisor escapes; maximum {depth} enlargements.')
    nchecked = 0
    for p, k in product((2,3,5), range(1,4)):
        d = p**k
        for co in product((-3,0,2,5), repeat=4):
            if not any(v % p for v in co):
                continue
            for z in (-2,0,1,9):
                vals = [d**i*sum(co[j]*comb(j,i)*z**(j-i) for j in range(i,4)) for i in range(4)]
                assert any(v % (p*d**3) for v in vals)
                nchecked += 1
    print(f'Disc minimum ≤ degree·v(d) for {nchecked} translations of primitive coefficient lists.')


if __name__ == '__main__':
    main()
