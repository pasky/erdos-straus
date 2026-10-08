"""O92 (POINTWISE_TYPEI5.md Prop 3.3): complete enumeration of the finite regimes (ii) lambda<0 and
(iii) lambda>0, Delta<2Tj, of case B (j = Tu/2 - y > 0) at level L, for ALL b (u = 7^b).
mode 'cert': u must be a power of 7 (fibre certificates);  mode 'relax': u any odd integer (regression vs typei5_relax).
Usage: typei5_regimes.py L mode"""
import sys
from sympy import divisors, factorint

def divs_from(fac):
    ds = [1]
    for p, e in fac.items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds

def is7pow(u):
    while u % 7 == 0: u //= 7
    return u == 1

def verify(L, u, a, j, m, relax):
    """full TYPEI4 Cor 3.2 conditions given (u, a, j, m); returns list of (c',g,delta,P1,X)"""
    T = 2 ** (L - 4); y = T * u // 2 - j; out = []
    if y <= 0 or y % 2 == 0 or m <= 0: return out
    for dl in divisors(m):
        if (m // dl) % dl: continue
        cp = m // (dl * dl)
        if cp % 7 == 0 or y % (cp * dl): continue
        g = y // (cp * dl); z = T * u - y
        P1 = cp * g * g + 7 ** a * u * (2 * y - T * u)
        if P1 < 1 or z % P1 or P1 % 7 == 0: continue
        num = 1 + 7 ** a * u * (z // P1)
        if num % (4 * cp * g): continue
        X = num // (4 * cp * g)
        if X % 2 == 0 or (not relax and X % 7 == 0): continue
        out.append((cp, g, dl, P1, X))
    return out

def run(L, relax):
    T = 2 ** (L - 4); ok7 = (lambda u: u % 2 == 1) if relax else is7pow
    sols = []; ncase = 0
    a = 1
    while 7 ** a < T ** 3 / 4 or 8 * 7 ** a < T * T:
        A7 = 7 ** a
        # regime (iii): lambda>0, s = 2Tj - Delta >= 1, 7^a*lambda*s < T^3/4
        lam = 1
        while A7 * lam < T ** 3 / 4:
            kap = 8 * A7 * lam; s = 1
            while A7 * lam * s < T ** 3 / 4:
                g = 2 * T ** 3 - s * kap; Rc = factorint(kap); 
                for p, e in factorint(s).items(): Rc[p] = Rc.get(p, 0) + 3 * e
                for p, e in factorint(4 * T ** 3 - s * kap).items(): Rc[p] = Rc.get(p, 0) + 2 * e
                for Dp in divs_from(Rc):
                    ncase += 1
                    if (Dp + s * T * T) % g: continue
                    j = (Dp + s * T * T) // g
                    if j < 1 or j % 2 == 0 or s >= 2 * T * j: continue
                    N = 4 * kap * j ** 3 + (2 * T * j - s) * (4 * T * j + s)
                    if N % Dp: continue
                    u = N // Dp
                    if not ok7(u): continue
                    mn = lam * (u * s + 4 * j * j)
                    if mn % (2 * T * j - s): continue
                    for sol in verify(L, u, a, j, mn // (2 * T * j - s), relax): sols.append(('iii', u, a, lam, j, sol))
                s += 1
            lam += 1
        # regime (ii): lambda<0, 8*7^a*|lambda|*j < T^2
        lam = 1
        while 8 * A7 * lam < T * T:
            kap = 8 * A7 * lam; j = 1
            while kap * j < T * T:
                K = T * T - kap * j; E = 2 * kap * T * j * j
                C = E * E + 6 * T * j * E * K + 4 * kap * j ** 3 * K * K
                for Dp in divisors(C):
                    ncase += 1
                    if (Dp + E) % K: continue
                    x = (Dp + E) // K
                    num = x * x + 6 * T * j * x + 4 * kap * j ** 3
                    if num % Dp: continue
                    u = num // Dp
                    if not ok7(u): continue
                    mn = lam * (u * (2 * T * j + x) + 4 * j * j)
                    if mn % x: continue
                    for sol in verify(L, u, a, j, mn // x, relax): sols.append(('ii', u, a, -lam, j, sol))
                j += 2
            lam += 1
        a += 2
    return sols, ncase

if __name__ == '__main__':
    L = int(sys.argv[1]); relax = sys.argv[2] == 'relax'
    sols, nc = run(L, relax)
    for s_ in sols: print(L, *s_)
    print(f'# L={L} mode={sys.argv[2]}: {nc} divisor cases, {len(sols)} solutions')
