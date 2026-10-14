# R215 — independent re-implementation of the "five-family menu" covering at level L (own derivation).
# Type II: M a b d = n + e, a + b = c e  -> M/n = 1/(abd) + 1/(acdn) + 1/(bcdn)
# Type I : M a b d = n e + 1, a + b = c e -> M/n = 1/(abdn) + 1/(acd) + 1/(bcd)
# One-parameter linear subfamilies (free variable in brackets):
#  II[d]: n = Mab d - e                         (mod Mab)
#  II[c] (b = ce - a): n = Made c - Ma^2 d - e   (mod Made)
#  II[e] (b = ce - a): n = (Macd - 1) e - Ma^2 d (mod Macd - 1)
#  I[d] : n = (Mab d - 1)/e, d runs over a class mod e  (mod Mab, needs gcd(e, Mab) = 1)
#  I[c] (b = ce - a): n = Mad c - (Ma^2 d + 1)/e (mod Mad, needs e | Ma^2 d + 1)
# Every n >= 1 in each class gives positive denominators (checked numerically below on the smallest lifts).
import sys
from math import gcd
from fractions import Fraction as F

def menu(M, L):
    out = []  # (modulus, residue, tag, params)
    for a in range(1, L+1):
        if M*a > L: break
        for b in range(1, L+1):
            q = M*a*b
            if q > L: break
            if L % q: continue
            for e in range(1, a+b+1):
                if (a+b) % e: continue
                out.append((q, (-e) % q, 'II[d]', (a, b, e)))
                if gcd(e, q) == 1:
                    out.append((q, (-pow(e, -1, q)) % q, 'I[d]', (a, b, e)))
    for a in range(1, L+1):
        if M*a > L: break
        for d in range(1, L+1):
            q = M*a*d
            if q > L: break
            for e in range(1, L+1):
                if q*e > L: break
                if L % (q*e) == 0:
                    out.append((q*e, (-M*a*a*d - e) % (q*e), 'II[c]', (a, d, e)))
            if L % q == 0:
                t = M*a*a*d + 1
                for e in range(1, t+1):
                    if t % e == 0:
                        out.append((q, (-(t//e)) % q, 'I[c]', (a, d, e)))
    for a in range(1, L+1):
        if M*a - 1 > L: break
        for c in range(1, L+1):
            if M*a*c - 1 > L: break
            for d in range(1, L+1):
                g = M*a*c*d - 1
                if g > L: break
                if L % g == 0:
                    out.append((g, (-M*a*a*d) % g, 'II[e]', (a, c, d)))
    return out

def witness(M, n, fam):
    q, r, t, P = fam
    if t == 'II[d]':
        a, b, e = P; d = (n+e)//(M*a*b); c = (a+b)//e; return (a*b*d, a*c*d*n, b*c*d*n)
    if t == 'I[d]':
        a, b, e = P; d = (n*e+1)//(M*a*b); c = (a+b)//e; return (a*b*d*n, a*c*d, b*c*d)
    if t == 'II[c]':
        a, d, e = P; c = (n+M*a*a*d+e)//(M*a*d*e); b = c*e-a; return (a*b*d, a*c*d*n, b*c*d*n)
    if t == 'I[c]':
        a, d, e = P; c = (n+(M*a*a*d+1)//e)//(M*a*d); b = c*e-a; return (a*b*d*n, a*c*d, b*c*d)
    if t == 'II[e]':
        a, c, d = P; e = (n+M*a*a*d)//q; b = c*e-a; return (a*b*d, a*c*d*n, b*c*d*n)

def uncovered(M, L, check=True):
    fams = menu(M, L)
    cov = set()
    for f in fams:
        q, r = f[0], f[1]
        for R in range(r, L, q):
            if gcd(R, L) == 1 and R not in cov:
                cov.add(R)
                if check:  # exact witness at the smallest positive lift n = R and n = R + L
                    for nn in (R, R+L):
                        D = witness(M, nn, f)
                        assert min(D) > 0 and sum(F(1, x) for x in D) == F(M, nn), (M, L, f, nn, D)
    U = [r for r in range(1, L) if gcd(r, L) == 1]
    return U, [r for r in U if r not in cov and r % M]

def issq(r, L): return any((x*x - r) % L == 0 for x in range(L))

if __name__ == "__main__":
    M = int(sys.argv[1])
    for L in map(int, sys.argv[2:]):
        U, unc = uncovered(M, L)
        sq = [r for r in unc if issq(r, L)]
        nsq = sum(1 for r in U if issq(r, L))
        print(f"M={M} L={L}: units {len(U)} uncovered {len(unc)} (squares {len(sq)}/{nsq}) {unc[:40]}")
