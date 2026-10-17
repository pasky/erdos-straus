"""R267 from-scratch spot check of NONCONG_LIFTS Computation 3.2 (matched sources; det / visible / all).

Witness of prime n (k=4): (θ, a, b, c, d), e = (a+b)/c, N_II = n + e, N_I = n e + 1, N = k a b d, H = k a b.
Enumeration: for each e, N = N_θ(n) with k | N, all factorisations N/k = a*b*d (ordered (a, b)), all c with c*e = a+b.
Bounds: II: e <= (n+k)/(k-1);  I: e <= a+b <= ab+1 <= (ne+1)/k + 1 is no bound, so we use the solution-side bound:
  Type I denominators (abdn, acd, bcd): the smallest is >= n/k... we instead bound e by x = acd >= ... (see note)
We avoid the issue by generating Type I witnesses from the complete solution list (x<=y<=z) of k/n instead.
"""
import sys
from math import gcd, isqrt
from sympy import isprime, factorint, divisors

K = 4


def solutions(n, k=K):
    """all (x<=y<=z) with k/n = 1/x+1/y+1/z, brute via divisor criterion."""
    out = []
    for x in range(n // k + 1, 3 * n // k + 1):
        A, B = k * x - n, n * x
        g = gcd(A, B); A //= g; B //= g
        if A <= 0:
            continue
        for u in divisors(B * B):
            if u > B:
                continue
            if (u + B) % A == 0:
                y = (u + B) // A
                if y < x:
                    continue
                z = (B * B // u + B) // A
                out.append((x, y, z))
    return out


def witnesses(n, k=K):
    """ET representations: for a solution, Type II if n divides exactly two denominators (x = abd, y = acdn, z = bcdn),
    Type I if exactly one (x = abdn, y = acd, z = bcd). For prime n ∤ k every solution is one of these.
    Recover (a, b, c, d): for Type II with free denominator X and the two n-multiples Y=n*y', Z=n*z':
    c*d = gcd(y', z') * t ... we enumerate all (a,b,c,d) with abd = X, acd = y', bcd = z' directly."""
    W = set()
    for sol in solutions(n, k):
        mult = [s for s in sol if s % n == 0]
        free = [s for s in sol if s % n]
        if len(mult) == 2:
            th, X, (Y, Z) = "II", free[0], (mult[0] // n, mult[1] // n)
        elif len(mult) == 1:
            th, X, (Y, Z) = "I", mult[0] // n, tuple(free)
        else:
            raise AssertionError(sol)
        # X = abd, Y = acd, Z = bcd (both orders of (Y, Z) give (a,b) swapped)
        for (y1, z1) in {(Y, Z), (Z, Y)}:
            gyz = gcd(y1, z1)
            for cd in divisors(gyz):
                a, b = y1 // cd, z1 // cd
                if X % (a * b) == 0 or True:
                    for d in divisors(cd):
                        c = cd // d
                        if a * b * d == X:
                            e, r = divmod(a + b, c)
                            assert r == 0
                            N = n + e if th == "II" else n * e + 1
                            assert N == k * a * b * d
                            W.add((th, a, b, c, d))
    return W


def is_square_mod(r, m):
    r %= m
    return any((s * s - r) % m == 0 for s in range(m)) if m < 200000 else None


def sq_mod(r, m):
    for pr, ex in factorint(m).items():
        pe = pr ** ex
        if not any((s * s - r) % pe == 0 for s in range(pe)):
            return False
    return True


def legendre(a, l):
    a %= l
    return 0 if a == 0 else (1 if pow(a, (l - 1) // 2, l) == 1 else -1)


def matched_sources(p, W):
    for q in range(max(3, p - W), p + W + 1):
        if q == p or not isprime(q) or (q - p) % 8:
            continue
        if all(legendre(q, l) == legendre(p, l) for l in (3, 5, 7)):
            yield q


def run(p, W=600):
    Hp = sorted({K * a * b for (_, a, b, _, _) in witnesses(p)})
    res = []
    for q in matched_sources(p, W):
        Wq = witnesses(q)
        allw = len(Wq)
        vis = det = 0
        for (_, a, b, _, _) in Wq:
            H = K * a * b
            v = not sq_mod(p, H)
            dt = any(H % h == 0 for h in Hp)
            assert not (dt and not v), (p, q, a, b)
            vis += v; det += dt
        res.append(f"{q}({p - q:+d}):{det}/{vis}/{allw}")
    return res


if __name__ == "__main__":
    for p in map(int, sys.argv[1:]):
        print(p, " ".join(run(p)))


def aggregate(Pmax, W=1000):
    from sympy import primerange
    M = {1, 121, 169, 289, 361, 529}
    ps = [p for p in primerange(3, Pmax + 1) if p % 840 in M]
    agg = dict(primes=len(ps), src=0, w=0, vis=0, det=0, srctot=0, srcvissuff=0)
    return ps, agg


def full_aggregate(Pmax, W=1000):
    ps, agg = aggregate(Pmax, W)
    for p in ps:
        Hp = {K * a * b for (_, a, b, _, _) in witnesses(p)}
        for q in matched_sources(p, W):
            agg["src"] += 1
            Wq = {(a, b) if a <= b else (b, a): None for (_, a, b, _, _) in []}
            ws = {(th, min(a, b), max(a, b), c, d) for (th, a, b, c, d) in witnesses(q)}
            nv = nd = nvd = 0
            for (_, a, b, _, _) in ws:
                H = K * a * b
                v = not sq_mod(p, H); dt = any(H % h == 0 for h in Hp)
                nv += v; nd += dt; nvd += v and dt
            agg["w"] += len(ws); agg["vis"] += nv; agg["det"] += nd
            agg["srctot"] += nd == len(ws); agg["srcvissuff"] += nvd == nv
    return agg
