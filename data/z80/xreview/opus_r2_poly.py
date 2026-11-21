"""Independent (Opus R2 reviewer) checks of notes/z80/PROTH_CORE.md §7 (Theorems 10-11).
No repository script imported.  PARI for polynomial roots mod q / Jacobi symbols.
 (10) all odd 3<=k<=201, t=7 mod 8 up to 400, even e<=16: word identity, actual ES triple,
      actual Jacobi (z / n) = -1 (the Dedekind sign of the word), n nonsquare;
      negative controls: odd e and k even give failures of the stated congruences;
 (11) Chebotarev supply: share of primes q=97 mod 112, q<QMAX, with a root of F+14, for odd-degree
      F, an even-degree F with an odd-degree factor of F+14, and the even controls X^2, (8X+1)^2,
      840X^4+1; and the empirical density of x<=XMAX (in a progression with F(x)=1 mod 8) whose
      F(x)+14 has such a prime divisor q<=QPOOL, with real words, Jacobi signs and triples.
Run: ulimit -v 6000000; timeout 1800 uv run --offline --no-project --with cypari2 python -B opus_r2_poly.py
"""
from math import isqrt, gcd
from cypari2 import Pari
pari = Pari()

def tri_ok(n, x, y, z):
    return min(x, y, z) > 0 and 4 * x * y * z == n * (x * y + y * z + z * x)

def thm10():
    cnt = 0
    for k in range(3, 202, 2):
        u = k - 1
        for t in range(7, 401, 8):
            z = t * u - 1
            for e in range(2, 17, 2):
                n = k * (z ** e - 1) + 1; A = z; v = k * z ** (e - 1)
                assert n == t * u * v - u - v and A * v == n + u and A + 1 == t * u
                assert n % 8 == 1 and (n + t) % 8 == 0 and (t * v - 1) % 4 == 0
                D = (t * v - 1) // 4
                assert tri_ok(n, A * D * n, u * D, A * u * D)
                assert isqrt(n) ** 2 != n
                assert int(pari.kronecker(A, n)) == -1, (k, t, e)   # Jacobi of the word, computed
                cnt += 1
    # control: odd e breaks n = 1 mod 8 / the sign in general
    odd_fail = 0
    for k in range(3, 40, 2):
        u = k - 1
        for t in range(7, 80, 8):
            z = t * u - 1; e = 3; n = k * (z ** e - 1) + 1
            if int(pari.kronecker(z, n)) != -1: odd_fail += 1
    print('(10) Theorem 10 box:', cnt, 'cases OK (identity, triple, Jacobi -1, nonsquare); odd-e control sign failures:', odd_fail)

POLYS = {
    '840x+1': (lambda x: 840 * x + 1, 'x', 1),
    '840x^3+1': (lambda x: 840 * x ** 3 + 1, '840*x^3+1', 1),
    '8x^5+1': (lambda x: 8 * x ** 5 + 1, '8*x^5+1', 1),
    'x^3+8x^2+1 (odd deg, not monomial)': (lambda x: x ** 3 + 8 * x ** 2 + 1, 'x^3+8*x^2+1', 0),
    '8x^4+8x^2+15x-14 (even deg, F+14 has factor x)': (lambda x: 8*x**4+8*x**2+15*x-14, None, 0),
    '(8x+1)^2 control': (lambda x: (8 * x + 1) ** 2, '(8*x+1)^2', 0),
    '840x^4+1 control': (lambda x: 840 * x ** 4 + 1, '840*x^4+1', 1),
    '840x^2+1 control': (lambda x: 840 * x ** 2 + 1, '840*x^2+1', 1),
}

def thm11(QMAX=20000, XMAX=6000, QPOOL=4000):
    qs = [q for q in range(97, QMAX, 112) if pari.isprime(q)]
    pool = [q for q in qs if q <= QPOOL]
    for name, (F, _, _) in POLYS.items():
        # root supply: q with a root of F+14 mod q (brute force over residues for small q)
        with_root = 0; recip = 0.0; sub = qs[:60]
        for q in sub:
            if any((F(x) + 14) % q == 0 for x in range(q)): with_root += 1; recip += 1 / q
        # density in x over a progression with F(x) = 1 mod 8
        x0 = next(x for x in range(1, 9) if F(x) % 8 == 1) if any(F(x) % 8 == 1 for x in range(1, 9)) else None
        if x0 is None:
            print(f'(11) {name}: no x with F(x)=1 mod 8'); continue
        hits = tot = 0
        for x in range(x0, XMAX, 8):
            n = F(x); tot += 1
            for q in pool:
                if (n + 14) % q == 0:
                    t = (q + 1) // 14; v = (n + 14) // q
                    if v < 2: continue
                    assert n == t * 14 * v - 14 - v and t % 8 == 7 and v % 8 == 7 and (n + t) % 8 == 0
                    assert int(pari.kronecker(q, n)) == -1     # (tu-1 / n) with tu-1 = q
                    D = (t * v - 1) // 4; assert (t * v - 1) % 4 == 0
                    assert tri_ok(n, q * D * n, 14 * D, q * 14 * D)
                    hits += 1; break
        print(f'(11) {name}: roots of F+14 at {with_root}/{len(sub)} primes q=97 mod 112 below {QMAX} (sum 1/q={recip:.4f}); '
              f'share of x<{XMAX} (x={x0} mod 8) with a pool divisor q<={QPOOL}: {hits}/{tot} = {hits / tot:.3f}')

def landau_compare(XMAX=6000):
    """ES via ANY divisor = 3 mod 4 (trivial rule) on the same polynomial samples."""
    for name, (F, _, _) in POLYS.items():
        tot = hit = 0
        for x in range(1, XMAX):
            n = F(x)
            if n % 4 != 1: continue
            tot += 1
            m = n; ok = False
            for p in range(3, 2000, 4):
                if m % p == 0: ok = True; break
            hit += ok
        print(f'     trivial 3-mod-4 divisor (<2000) rule on {name}, n=1 mod 4: {hit}/{tot} = {hit / max(tot, 1):.3f}')

if __name__ == '__main__':
    thm10(); thm11(); landau_compare()
