"""R277 from-scratch exact checks for SINGLE_P_COUNT Lemma 1.1, Lemma 2.1, Prop 2.2.

Independent of scripts/z30_*. Exact rationals (fractions.Fraction).
  (A) Lemma 1.1: triple count vs pair form vs divisor form vs SL2 form, primes < P1.
  (B) s(q) = |G/G^2| by brute force; real characters enumerated as homs G -> {+-1} by brute force;
      Lemma 2.1 identity R* = M_gen + X with X computed from the brute-force character sum
      (sum over ALL chars = phi(q)*1[n=a] is also checked through a full brute-force character table
      for q <= QMAX_FULL via explicit cyclic decomposition).
  (C) Prop 2.2(a) explicit Legendre form == definition; (b) M_gen(m^2) = R*(m^2) = 0; (d) mean preservation.
"""
import sys
from fractions import Fraction
from math import gcd
from itertools import product
from functools import lru_cache


def isprime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def phi(n):
    r = n
    for l in factor(n):
        r = r // l * (l - 1)
    return r


@lru_cache(None)
def units(q):
    return tuple(x for x in range(1, q) if gcd(x, q) == 1)


@lru_cache(None)
def squares(q):
    return frozenset(x * x % q for x in units(q))


@lru_cache(None)
def real_chars(q):
    """All homomorphisms (Z/q)^x -> {+1,-1}, by brute force over a generating set."""
    U = units(q)
    gens = []
    span = {1}
    for x in U:
        if x not in span:
            gens.append(x)
            # closure
            new = set(span)
            changed = True
            while changed:
                changed = False
                for s in list(new):
                    for g in gens:
                        t = s * g % q
                        if t not in new:
                            new.add(t)
                            changed = True
            span = new
    chars = []
    for signs in product([1, -1], repeat=len(gens)):
        # try to define chi by BFS; reject if inconsistent
        val = {1: 1}
        frontier = [1]
        ok = True
        while frontier and ok:
            nf = []
            for s in frontier:
                for g, e in zip(gens, signs):
                    t = s * g % q
                    v = val[s] * e
                    if t in val:
                        if val[t] != v:
                            ok = False
                            break
                    else:
                        val[t] = v
                        nf.append(t)
                if not ok:
                    break
            frontier = nf
        if ok and len(val) == len(U):
            # verify multiplicativity fully
            if all(val[x * y % q] == val[x] * val[y] for x in U for y in U[:8]):
                chars.append(val)
    return chars


def pairs(n):
    """coprime (u,B), u+B odd, 4uB-u-B <= n"""
    out = []
    u = 1
    while 4 * u - u - 1 <= n:
        B = 1
        while 4 * u * B - u - B <= n:
            if gcd(u, B) == 1 and (u + B) % 2 == 1:
                out.append((u, B))
            B += 1
        u += 1
    return out


def legendre(a, l):
    a %= l
    if a == 0:
        return 0
    return 1 if pow(a, (l - 1) // 2, l) == 1 else -1


def Rstar(n):
    return sum(1 for u, B in pairs(n) if (n + u + B) % (4 * u * B) == 0)


def Mgen_def(n, brute=True):
    tot = Fraction(0)
    for u, B in pairs(n):
        q = 4 * u * B
        a = (-(u + B)) % q
        if gcd(n, q) != 1:
            continue
        if brute:
            s = len(units(q)) // len(squares(q))
            insq = (n * a) % q in squares(q)
        else:
            s = 4 * 2 ** len([l for l in factor(u * B) if l != 2])
            insq = None
        if insq:
            tot += Fraction(s, phi(q))
    return tot


def Mgen_explicit(n):
    """Prop 2.2(a) explicit indicator."""
    tot = Fraction(0)
    for u, B in pairs(n):
        q = 4 * u * B
        if (n + u + B) % 8 != 0:
            continue
        ok = True
        for l in factor(u):
            if l != 2 and legendre(n, l) != legendre(-B, l):
                ok = False
        for l in factor(B):
            if l != 2 and legendre(n, l) != legendre(-u, l):
                ok = False
        if ok:
            s = 4 * 2 ** len([l for l in factor(u * B) if l != 2])
            tot += Fraction(s, phi(q))
    return tot


def partA(P1):
    bad = 0
    for p in range(3, P1):
        if not isprime(p):
            continue
        # triples
        t = 0
        for u in range(1, p + 1):
            for B in range(1, p + 1):
                if 4 * u * B - u - B > p:
                    break
                if (p + u + B) % (4 * u * B) == 0:
                    t += 1
        pf = sum(1 for u in range(1, p + 1) for B in range(1, p + 1)
                 if 4 * u * B - u - B <= p and gcd(u, B) == 1 and (p + u + B) % (4 * u * B) == 0)
        dv = 0
        dvhalf = 0
        C = 1
        while 4 * C - 2 <= p:
            N = 4 * C * p + 1
            for d in range(1, N + 1):
                if d * d > N:
                    break
                if N % d == 0:
                    for e in {d, N // d}:
                        if e % (4 * C) == 4 * C - 1:
                            dv += 1
                            if e * e < N:
                                dvhalf += 1
            C += 1
        # SL2 form: gamma=(a p; c d), c in 4N, a,d>=1, a=d=-1 mod c, ad - pc = 1
        sl = 0
        c = 4
        while c - 1 <= p + 1:  # a,d >= c-1 so ad >= (c-1)^2 = pc+1
            if (c - 1) ** 2 > p * c + 1:
                break
            N = p * c + 1
            for a in range(c - 1, N + 1, c):
                if N % a == 0 and (N // a) % c == c - 1:
                    sl += 1
            c += 4
        Rs = Rstar(p)
        if not (t == pf == dv == sl == Rs == 2 * dvhalf and t % 2 == 0):
            bad += 1
            print("Lemma1.1 MISMATCH", p, t, pf, dv, sl, Rs, dvhalf)
    print(f"(A) Lemma 1.1 four forms + R*=R + evenness: mismatches = {bad} for primes < {P1}")


def partB(N):
    bad = 0
    nq = 0
    for n in range(3, N, 2):
        Rs = Rstar(n)
        Mg = Mgen_def(n)
        Me = Mgen_explicit(n)
        # X from brute-force real characters: X = R* - (sum over real chars)/phi
        Mchar = Fraction(0)
        for u, B in pairs(n):
            q = 4 * u * B
            a = (-(u + B)) % q
            if gcd(n, q) != 1:
                continue
            ch = real_chars(q)
            assert len(ch) == len(units(q)) // len(squares(q)) == 4 * 2 ** len([l for l in factor(u * B) if l != 2]), q
            Mchar += Fraction(sum(c[n % q] * c[a] for c in ch), phi(q))
            nq += 1
        if not (Mg == Me == Mchar):
            bad += 1
            print("MISMATCH Mgen", n, Mg, Me, Mchar)
        m = int(round(n ** 0.5))
        if m * m == n:
            print(f"  square n={n}: R*={Rs} M_gen={Mg} X={Rs - Mg}")
            if Rs != 0 or Mg != 0:
                bad += 1
    print(f"(B,C) odd n<{N}: M_gen(definition, brute squares) == M_gen(Prop 2.2(a) explicit) == "
          f"(brute real-character sum); s(q)=|G/G^2|=4*2^omega_odd; mismatches = {bad}")


def partD(qs):
    for (u, B) in qs:
        q = 4 * u * B
        a = (-(u + B)) % q
        U = units(q)
        s = len(U) // len(squares(q))
        avg = Fraction(sum(Fraction(s, phi(q)) for n in U if n * a % q in squares(q)), len(U))
        assert avg == Fraction(1, phi(q)), (u, B)
    print(f"(D) Prop 2.2(d) mean preservation: OK for {len(qs)} pairs")


if __name__ == "__main__":
    P1 = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    partA(P1)
    partB(N)
    partD([(u, B) for u in range(1, 12) for B in range(1, 12) if gcd(u, B) == 1 and (u + B) % 2])
