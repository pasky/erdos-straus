"""O211 (b): Salie-angle dictionary for Type II at a prime modulus h.
For each prime p < P and each Type II certificate (c,d,h) with h prime (h = 4cdj-1, h | p + 4c^2 d):
 (i) y0 = 2cd is a root of y^2 = -pd (mod h) and 2*y0*j = h+1, so the root angle y0/h = 1/(2j) + 1/(2jh);
 (ii) the Salie sum S(1,-pd;h) = sum_x (x/h) e((x - pd/x)/h) equals eps_h sqrt(h) (-pd/h) * 2cos(2pi*2*y0/h)
      (Salie's closed form; eps_h = i for h = 3 mod 4), i.e. |S|/(2 sqrt h) = |cos(2pi(1/j + 1/(jh)))|.
Odd squares n (T1 control): count certificates (must be 0).
Usage: PYTHONPATH=scripts uv run python scripts/y3_salie.py [P]"""
import sys, cmath, math
from sympy import isprime, primerange

def certs(p):
    out = []
    c = 1
    while 3*c <= p + 1:
        d = 1
        while 4*c*d - 1 <= p + c:
            m = 4*c*d; t = p//m + 1
            while t*(m - 1) <= p + c:
                den = m*t - p
                if den > 0 and (c + t) % den == 0:
                    j = (c + t)//den; out.append((c, d, j, m*j - 1))
                t += 1
            d += 1
        c += 1
    return out

def leg(a, h): a %= h; return 0 if a == 0 else (1 if pow(a, (h-1)//2, h) == 1 else -1)

def salie(a, b, h):
    s = 0
    for x in range(1, h):
        s += leg(x, h) * cmath.exp(2j*math.pi*((a*x + b*pow(x, -1, h)) % h)/h)
    return s

if __name__ == "__main__":
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    bad = n = ns = 0
    for p in primerange(5, P):
        for (c, d, j, h) in certs(p):
            if not isprime(h): continue
            y0 = 2*c*d
            if (y0*y0 + p*d) % h or 2*y0*j != h + 1: bad += 1
            if h < 3000 and n < 300:
                S = salie(1, -p*d, h)
                pred = 1j*math.sqrt(h)*leg(-p*d, h)*2*math.cos(2*math.pi*2*y0/h)
                if abs(S - pred) > 1e-6*h: bad += 1
                n += 1
    sq = sum(len(certs(m*m)) for m in range(3, int(P**.5) + 1, 2))
    print(f"P={P}: dictionary failures={bad}, Salie closed-form checks={n}; odd-square certificates={sq}")
