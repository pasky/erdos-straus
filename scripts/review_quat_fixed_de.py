"""R130: re-verify QUATERNION_ES §3.4 / Prop 5.1 from scratch.
(1) the named opposite-status pairs with the same (d,e);
(2) the 40/93 (Type I) and 120/450 (Type II) counts under the stated filter
    p = 1 mod 24, p < 1500, d <= 12, e < 60.
Type I(d,e,p): 4d | pe+1, m=(pe+1)/4d has a divisor a with e | a + m/a.
Type II(d,e,p): 4d | p+e, m=(p+e)/4d has a divisor a with e | a + m/a.
"""
from sympy import primerange, divisors, jacobi_symbol as J, factorint


def es(m, e):
    return [a for a in divisors(m) if a <= m // a and (a + m // a) % e == 0]


def typeI(d, e, p):
    if (p * e + 1) % (4 * d):
        return None
    return es((p * e + 1) // (4 * d), e)


def typeII(d, e, p):
    if (p + e) % (4 * d):
        return None
    return es((p + e) // (4 * d), e)


def main():
    for (d, e, ps) in [(5, 23, (313, 73)), (10, 7, (457, 97))]:
        for p in ps:
            m = (p * e + 1) // (4 * d)
            print(f"TypeI d={d} e={e} p={p} m={m} (-d/p)={J(-d, p)} genus(-d/l) l|e:",
                  {l: J(-d, l) for l in factorint(e)}, "m mod e", m % e, "ES divisors a:", typeI(d, e, p))
    for (d, e, ps) in [(1, 7, (73, 97)), (1, 11, (73, 193))]:
        for p in ps:
            print(f"TypeII d={d} e={e} p={p} m={(p+e)//(4*d)} ES divisors a:", typeII(d, e, p),
                  "genus (-p/l):", {l: J(-p % l, l) for l in factorint(e)})
    nI = gI = nII = gII = 0
    for p in primerange(3, 1500):
        if p % 24 != 1:
            continue
        for d in range(1, 13):
            for e in range(1, 60):
                if (p * e + 1) % (4 * d) == 0 and J(-d, p) == -1:
                    if any(  # 4 r^2 d = -1 mod e solvable
                           (4 * r * r * d + 1) % e == 0 for r in range(e)):
                        nI += 1; gI += bool(typeI(d, e, p))
                if (p + e) % (4 * d) == 0 and any((4 * r * r * d + p) % e == 0 for r in range(e)):
                    nII += 1; gII += bool(typeII(d, e, p))
    print(f"filtered TypeI: {gI}/{nI}   TypeII: {gII}/{nII}")


if __name__ == "__main__":
    main()
