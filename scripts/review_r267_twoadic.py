"""R267: for k in {4,8,12,16}, points x = r in Z_2 (r = 3,5,7 as 2-adic integers), x = 1 at every odd prime.
Which slices (a<=b<=B) cover them?  II: e ≡ -1 (H_odd), e ≡ -r (2^v); I: e ≡ -1 (H_odd), r e ≡ -1 (2^v)."""
import sys
B = int(sys.argv[1])
for k in (4, 8, 12, 16, 20, 24):
    for r in (3, 5, 7):
        hits = []
        for a in range(1, B + 1):
            for b in range(a, B + 1):
                H = k * a * b; v = 1
                Ho = H
                while Ho % 2 == 0:
                    Ho //= 2; v *= 2
                s = a + b
                for c in range(1, s + 1):
                    if s % c: continue
                    e = s // c
                    if (e + 1) % Ho: continue
                    if (e + r) % v == 0: hits.append(("II", a, b, c, e))
                    if (r * e + 1) % v == 0: hits.append(("I", a, b, c, e))
        print(k, r, len(hits), hits[:4])
