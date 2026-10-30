"""z52 deep thin-pointwise §2.3 (discharging / within-object exact identities at one prime).
Checks, for primes p ≡ 1 (mod 4):
 (i)  Barkan–Hickerson–Knuth–Zagier: 12 s(a,p) = Σ_i (b_i − 3) + (a + a*)/p, where p/a = [[b_1,...,b_r]] is the
      minus (Hirzebruch–Jung) continued fraction and a a* ≡ 1 (mod p)  [checked numerically, exact rationals];
 (ii) χ-blindness: Σ_{a QNR} 12 s(a,p) = 0, so the 'charge' Σ_i (b_i − 3) has the same total over QNRs as over QRs;
 (iii) ES5 count E5(p) = #{a QNR : HJ-length(p/a) ≤ 3} versus L3(p) = #{a : length ≤ 3} (both parities).
Usage: uv run python scripts/z52_thin_dedekind.py PMAX"""
import sys
from fractions import Fraction as F

def dedekind(a, c):
    s = F(0)
    for k in range(1, c):
        x = F(k, c); y = F(a * k % c, c)
        s += (x - F(1, 2)) * (y - F(1, 2))  # both non-integral since gcd=1 and 0<k<c
    return s

def hj(p, a):
    b = []; x, y = p, a
    while y:
        q = -(-x // y)  # ceil
        b.append(q); x, y = y, q * y - x
    return b

def leg(a, p): return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def isprime(n): return n > 1 and all(n % d for d in range(2, int(n**.5) + 1))

if __name__ == "__main__":
    PMAX = int(sys.argv[1]); bad = 0; rows = []
    for p in range(5, PMAX + 1, 4):
        if not isprime(p): continue
        qnr_charge = qr_charge = 0; tot_qnr_s = F(0); E5 = L3 = 0
        for a in range(1, p):
            b = hj(p, a); astar = pow(a, -1, p)
            lhs = 12 * dedekind(a, p); rhs = sum(x - 3 for x in b) + F(a + astar, p)
            if lhs != rhs: bad += 1
            ch = leg(a, p)
            if ch == -1: qnr_charge += sum(x - 3 for x in b); tot_qnr_s += lhs
            else: qr_charge += sum(x - 3 for x in b)
            if len(b) <= 3:
                L3 += 1; E5 += (ch == -1)
        rows.append((p, tot_qnr_s, qnr_charge, qr_charge, L3, E5))
    print("BHKZ identity violations:", bad)
    for r in rows[:12] + rows[-5:]:
        print("p=%d  sum_QNR 12s=%s  charge QNR=%d QR=%d  (-(p-1)/2=%d)  L3=%d  E5=%d" % (r[0], r[1], r[2], r[3], -(r[0]-1)//2, r[4], r[5]))
    print("all sum_QNR 12s == 0:", all(r[1] == 0 for r in rows), " all charge_QNR == -(p-1)/2:", all(r[2] == -(r[0]-1)//2 for r in rows))
