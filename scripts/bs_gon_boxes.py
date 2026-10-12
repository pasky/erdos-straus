"""O148 brainstorm (BRAINSTORM/gon_incidence_kloosterman.md), Type I in dyadic boxes.

Type I(p) <=> exists a,b,d >= 1 with (4abd - 1) | p(a+b)   [equivalently 4abd = pe+1, e | a+b].
Per dyadic box a in [A,2A), b in [B,2B), d in [D,2D) we count
  H1 = #{4abd = 1 (mod p)}            (Weil/Kloosterman-controlled: ~ ABD/p when ABD >> p^{3/2+eps}... or on average)
  S  = #{additionally e | a+b, e = (4abd-1)/p}   (moving modulus)
and the naive expectation H1/E with E ~ 4ABD/p (prob. 1/e that e | a+b).
Usage: bs_gon_boxes.py p [BMAX/p]  (boxes with a <= b-box, a*d <= p, B <= BMAX)
"""
import sys
from sympy import isprime

p = int(sys.argv[1]) if len(sys.argv) > 1 else 1000609
assert isprime(p)
BMAX = int(sys.argv[2]) * p if len(sys.argv) > 2 else 8 * p   # truncation of the b-range (b < 2*BMAX)
rows = []
A = 1
while A <= p:
    D = 1
    while A * D <= p:          # Type I needs a*d <~ p/2 (a+b >= e ~ 4abd/p)
        B = A                  # count each unordered pair once: b >= a by dyadic order (b-box >= a-box)
        while B <= BMAX:
            h1 = s = 0
            nv = 0.0
            for a in range(A, 2 * A):
                for d in range(D, 2 * D):
                    if (a * d) % p == 0:
                        continue
                    inv = pow(4 * a * d, -1, p)
                    b = inv + ((B - inv + p - 1) // p) * p if inv < B else inv
                    while b < 2 * B:
                        h1 += 1
                        e = (4 * a * b * d - 1) // p
                        if e <= a + b:
                            nv += 1.0 / e      # heuristic P(e | a+b) for a 'random' a+b
                        if (a + b) % e == 0:
                            s += 1
                        b += p
            E = 4 * A * B * D / p
            if h1:
                rows.append((A, B, D, h1, s, nv))
            B *= 2
        D *= 2
    A *= 2
tot_h = sum(r[3] for r in rows); tot_s = sum(r[4] for r in rows)
print(f"p={p}: boxes with hyperbola points: {len(rows)}, total H1={tot_h}, total Type I hits S={tot_s}")
nz = [r for r in rows if r[4]]
print(f"boxes with S>0: {len(nz)}; max S in a box: {max((r[4] for r in rows), default=0)}")
big = [r for r in rows if r[3] >= 100]
print(f"boxes with H1>=100: {len(big)}, of which S=0: {sum(1 for r in big if r[4] == 0)}; "
      f"mean S there {sum(r[4] for r in big)/max(len(big),1):.2f}, mean naive sum 1/e {sum(r[5] for r in big)/max(len(big),1):.3f}")
print(f"total naive sum_[e<=a+b] 1/e = {sum(r[5] for r in rows):.1f} vs actual S = {tot_s}")
act = [r for r in rows if r[5] >= 0.5]
print(f"boxes with naive >= 0.5: {len(act)}, actual S summed there {sum(r[4] for r in act)}, naive summed {sum(r[5] for r in act):.1f}")
