"""R135 from-scratch checks: Lemma 1.2 (genus, incl. l = 2), Lemma 1.3 identities, Prop 1.4 (Kneser criterion)
by brute force in (Z/e)*, and the e = 3, 7 explicit instances of §5.  No author code reused."""
import random
from math import gcd
from fractions import Fraction
from sympy import factorint, primerange


def legendre(a, l):  # Euler, l odd prime
    a %= l
    if a == 0: return 0
    return 1 if pow(a, (l - 1) // 2, l) == 1 else -1


def kron_minus_e(e, n):
    """Kronecker symbol (-e / n) computed from the DEFINITION (multiplicative in n over prime factors)."""
    D = -e
    r = 1
    for l, v in factorint(n).items():
        if l == 2:
            s = 1 if D % 8 in (1, 7) else (-1 if D % 8 in (3, 5) else 0)
        else:
            s = legendre(D, l)
        r *= s ** v
    return r


def lemma12():
    bad = 0; tests = 0
    for e in range(3, 400, 4):
        # chi_{-e} is a character mod e with chi(-1) = -1 : periodicity check
        for n in range(1, 3 * e):
            if gcd(n, e) == 1 and kron_minus_e(e, n) != kron_minus_e(e, n + e): bad += 1
        if kron_minus_e(e, e - 1) != -1: bad += 1
    for p in primerange(5, 4000):
        if p % 4 != 1: continue
        for e in range(3, 300, 4):
            if e % p == 0: continue
            for T, N in (("I", (p * e + 1) // 4), ("II", (p + e) // 4)):
                for l in factorint(N):
                    tests += 1
                    lp = legendre(l, p)
                    if kron_minus_e(e, l) != lp: bad += 1; print("L1.2(i) fail", p, e, T, l)
                chiN = kron_minus_e(e, N % e if N % e else e)  # character value of N mod e
                want = 1 if T == "I" else legendre(e, p)
                if chiN != want: bad += 1; print("L1.2(ii) fail", p, e, T)
    print("Lemma 1.2: prime-factor tests", tests, "failures", bad)


def lemma13():
    bad = 0
    for p in primerange(5, 300):
        for e in range(1, 60):
            if (p + e) % 4 == 0 and e % p:
                N = (p + e) // 4
                for a in range(1, N + 1):
                    if N % a: continue
                    for b in range(1, a):
                        if (N // a) % b == 0 and (a - b) % e == 0:
                            c = (a - b) // e; d = N // (a * b)
                            if Fraction(1, a*b*d) - Fraction(1, a*c*d*p) + Fraction(1, b*c*d*p) != Fraction(4, p): bad += 1
            if (p * e + 1) % 4 == 0:
                N = (p * e + 1) // 4
                for a in [x for x in range(1, min(N, 3000) + 1) if N % x == 0]:
                    for b in range(1, a):
                        if (N // a) % b == 0 and (a - b) % e == 0:
                            c = (a - b) // e; d = N // (a * b)
                            if Fraction(1, a*b*d*p) - Fraction(1, a*c*d) + Fraction(1, b*c*d) != Fraction(4, p): bad += 1
    print("Lemma 1.3 identity failures:", bad)


def units(e): return [g for g in range(1, e) if gcd(g, e) == 1]


def subgroups(e):
    U = units(e)
    def close(S):
        S = set(S) | {1}
        while True:
            T = {x * y % e for x in S for y in S}
            if T <= S: return frozenset(S)
            S |= T
    found = {close([1])}; frontier = list(found)
    while frontier:
        new = []
        for H in frontier:
            for g in U:
                if g not in H:
                    K = close(H | {g})
                    if K not in found: found.add(K); new.append(K)
        frontier = new
    return found


def order_mod_H(g, H, e):
    k, x = 1, g % e
    while x not in H: x = x * g % e; k += 1
    return k


def prop14(trials=4000, seed=1):
    rnd = random.Random(seed); viol = 0; sharp_hits = 0
    for e in list(range(3, 64)):
        if e % 2 == 0 and e != 2: pass
        U = units(e)
        if len(U) < 2: continue
        subs = [H for H in subgroups(e) if (e - 1) not in H]
        for _ in range(trials // 20):
            k = rnd.randint(1, 5)
            gs = [rnd.choice(U) for _ in range(k)]; vs = [rnd.randint(1, 3) for _ in range(k)]
            S = {1}
            for g, v in zip(gs, vs):
                A = {pow(g, t, e) if t >= 0 else pow(pow(g, -1, e), -t, e) for t in range(-v, v + 1)}
                S = {s * a % e for s in S for a in A}
            crit = all(sum(min(2*v+1, order_mod_H(g, H, e)) - 1 for g, v in zip(gs, vs)) >= len(U)//len(H) - 1 for H in subs)
            if crit and (e - 1) not in S: viol += 1; print("Prop1.4 VIOLATION", e, gs, vs)
            if (e - 1) in S and not crit: sharp_hits += 1
    print("Prop 1.4 violations:", viol, "(cases covered but criterion silent:", sharp_hits, ")")


def instances():
    bad = 0
    for p in primerange(5, 200000):
        if p % 4 != 1: continue
        N3 = (p + 3) // 4; f3 = factorint(N3)
        if any(l % 3 == 2 for l in f3):
            if not any((a + b) % 3 == 0 for a in [1] for b in [1]) and False: pass
            S = {1}
            for l, v in f3.items():
                S = {s * pow(l, t, 3) % 3 for s in S for t in range(0, 2*v+1)}  # l^{-1} = l mod 3
            if 2 not in S: bad += 1
        N7 = (p + 7) // 4; f7 = factorint(N7)
        if any(l % 7 in (3, 5, 6) for l in f7) and sum(1 for l in f7 if l % 7 not in (1, 6)) >= 3:
            S = {1}
            for l, v in f7.items():
                A = {pow(l, t, 7) for t in range(0, v + 1)} | {pow(pow(l, -1, 7), t, 7) for t in range(0, v + 1)}
                S = {s * a % 7 for s in S for a in A}
            if 6 not in S: bad += 1; print("e=7 instance fails", p)
    print("explicit instance failures:", bad)


if __name__ == "__main__":
    lemma12(); lemma13(); prop14(); instances()
