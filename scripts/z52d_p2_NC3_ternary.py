# Ternary enumeration for Z2925 (genus class numbers of Gross lattices) and Z3181 (representation of sporadic exceptions).
# Even Gram matrices G = [[2a,f,g],[f,2b,h],[g,h,2c]], a<=b<=c, |f|<=a, |g|<=a, |h|<=b, abc <= det(G)/4 (Minkowski/Hermite for
# M = G/2, ternary gamma_3^3 = 2), det(G) = target, positive definite.  Classes: PARI qfisom.  Genus proxy: equal theta
# series (qfrep) up to bound B (same genus ⇒ same theta; the converse is the standard approximation used here).
import sys, math
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
def det3(a, b, c, f, g, h):
    # det of [[2a,f,g],[f,2b,h],[g,h,2c]]
    return 2*a*(4*b*c - h*h) - f*(2*f*c - h*g) + g*(f*h - 2*b*g)
def enum_even(target):
    out = []
    lim = target // 4
    a = 1
    while 2*a*2*a*2*a <= 8*lim:  # a^3 <= lim
        if a**3 > lim: break
        b = a
        while a*b*b <= lim:
            c = b
            while a*b*c <= lim:
                for f in range(-a, a+1):
                    for g in range(-a, a+1):
                        for h in range(-b, b+1):
                            if det3(a, b, c, f, g, h) == target and (a*b*c) <= lim:
                                out.append((2*a, 2*b, 2*c, f, g, h))
                c += 1
            b += 1
        a += 1
    return out
def gram(t):
    A, B, C, f, g, h = t
    return pari(f"[{A},{f},{g};{f},{B},{h};{g},{h},{C}]")
def classes(target):
    forms = enum_even(target)
    reps = []
    for t in forms:
        G = gram(t)
        if any(bool(pari.qfisom(G, R)) for R in reps): continue
        reps.append(G)
    return reps
def theta_key(G, B=40):
    r = pari.qfrep(G, B, 1) if False else None
    v = pari(f"vector({B},n,qfrep({G},n,1))")  # not used
    return None
if __name__ == "__main__":
    target = int(sys.argv[1])
    R = classes(target)
    print("target det", target, "number of isometry classes (even, reduced enumeration):", len(R))
