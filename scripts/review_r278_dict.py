"""R278 from-scratch checks of QUESTION_R Props 1.1, 1.2, Cor 1.3, Prop 1.4.
Usage: uv run python scripts/review_r278_dict.py NMAX
"""
import sys
from math import gcd

def jac(a, n):
    assert n > 0 and n % 2
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

def words(NMAX):
    """all (t,u,v)>=2 with t*u*v-u-v = n <= NMAX, by direct triple loop (independent of author's loop)."""
    out = []
    for t in range(2, NMAX + 1):
        if 4 * t - 4 > NMAX: break
        for u in range(2, NMAX + 1):
            if 2 * t * u - u - 2 > NMAX: break
            for v in range(2, NMAX + 1):
                n = t * u * v - u - v
                if n > NMAX: break
                out.append((t, u, v, n))
    return out

def matrices(NMAX):
    """Prop 1.1 target set enumerated from the matrix side: b=n<=NMAX, c>=2, a,d = -1 mod c, a,d >= 2c-1, ad-bc=1."""
    S = set()
    for c in range(2, NMAX + 1):
        if 4 * c - 4 > NMAX: break
        a = 2 * c - 1
        while True:
            # need d >= 2c-1 with a*d - 1 = c*b, b<=NMAX  -> d <= (c*NMAX+1)/a
            if a * (2 * c - 1) - 1 > c * NMAX: break
            d = 2 * c - 1
            while a * d - 1 <= c * NMAX:
                if (a * d - 1) % c == 0:
                    S.add((a, (a * d - 1) // c, c, d))
                d += c
            a += c
    return S

def main():
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    W = words(NMAX)
    Wm = {(t * u - 1, n, t, t * v - 1) for t, u, v, n in W}
    M = matrices(NMAX)
    print(f"Prop1.1: words n<={NMAX}: {len(W)}, distinct images {len(Wm)}, matrix-side set {len(M)}, equal: {Wm == M}")
    bad12 = 0; cells = {}; c13 = [0, 0, 0]; ex = []
    n1 = 0
    for t, u, v, n in W:
        if n % 4 != 1: continue
        n1 += 1
        A = t * u - 1
        chi = jac(A, n)
        e, Ao = 0, A
        while Ao % 2 == 0: Ao //= 2; e += 1
        pred = jac(2, n) ** e * jac(-t, Ao)
        bad12 += (pred != chi)
        cells.setdefault((t % 8, A % 8, n % 8), set()).add(chi)
        if t % 4 == 3:
            c13[0] += 1
            if A % 2 == 0: c13[1] += 1
            if chi == 1:
                c13[2] += 1
                if len(ex) < 5: ex.append((t, u, v, n, A, chi))
    amb = sum(len(s) > 1 for s in cells.values())
    print(f"Prop1.2: words n=1(4): {n1}; formula failures {bad12}; (t,A,n) mod 8 cells {len(cells)}, ambiguous {amb}")
    print(f"Cor1.3 (t=3 mod 4): words {c13[0]}, with A even {c13[1]}, with chi=+1 {c13[2]}; examples {ex}")
    # prime example
    def isprime(m): return m > 1 and all(m % q for q in range(2, int(m ** .5) + 1))
    pex = [(t, u, v, n) for t, u, v, n in W if t % 4 == 3 and n % 4 == 1 and isprime(n) and jac(t * u - 1, n) == 1][:5]
    print("   prime examples:", pex)
    # Prop 1.4 on (A)3 words t,u,v<200 (4|t, n=1 mod 4)
    cnt = bad = 0
    for t in range(4, 200, 4):
        for u in range(2, 200):
            A = t * u - 1
            for v in range(2, 200):
                n = t * u * v - u - v
                if n % 4 != 1: continue
                As = t * v - 1
                cnt += 1
                if jac(t, As) != 1 or jac(A, n) != -1 or jac(A, n) != -jac(t, As): bad += 1
    print(f"Prop1.4: (A)3 words t,u,v<200 with n=1(4): {cnt}; failures {bad}")
    # general Prop 1.4 sign law (a/b) = -(c/d) on random a=d=3 mod 4 coset matrices (not self-levelled)
    import random
    random.seed(4); cnt2 = bad2 = 0
    while cnt2 < 20000:
        c = 4 * random.randint(1, 300); d = random.randrange(3, 4000, 4)
        if gcd(c, d) != 1: continue
        # a*d - b*c = 1, a = 3 mod 4, b = 1 mod 4 (b>0)
        a0 = pow(d, -1, c)
        for k in range(0, 40):
            a = a0 + k * c
            if a % 4 == 3 and (a * d - 1) % c == 0:
                b = (a * d - 1) // c
                if b > 0 and b % 4 == 1:
                    cnt2 += 1
                    if jac(a, b) != -jac(c, d): bad2 += 1
                    break
    print(f"Prop1.4 general law on {cnt2} random matrices: failures {bad2}")

if __name__ == "__main__":
    main()
