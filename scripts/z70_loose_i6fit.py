# z70 LOOSE I6: three-term fit G(r+iy) ~ (A log^2(1/y) + B log(1/y) + C)/y from i6_singular_check.txt (3 values of y),
# solved exactly per r; compares A(r)/A(0) with Lemma K's 1[c odd] mu(c)/c^2.  Illustration only (o(1/y) terms ignored).
import re, numpy as np
txt = open('data/z70/loose/i6_singular_check.txt').read().split('y=')[1:]
ys, G0, rat = [], [], {}
for blk in txt:
    y = float(blk.split()[0]); g0 = float(re.search(r'G\(iy\)=([0-9.e+]+)', blk).group(1)); ys.append(y); G0.append(g0)
    for m in re.finditer(r'r=(\d+)/(\d+)\s+G\(r\+iy\)/G\(iy\) = ([+-][0-9.]+) ([+-][0-9.]+)i', blk):
        rat.setdefault((int(m.group(1)), int(m.group(2))), []).append(complex(float(m.group(3)), float(m.group(4))))
def mu(c):
    r = 1; d = 2
    while d * d <= c:
        if c % d == 0:
            c //= d
            if c % d == 0: return 0
            r = -r
        d += 1
    return -r if c > 1 else r
Mx = np.array([[np.log(1 / y)**2 / y, np.log(1 / y) / y, 1 / y] for y in ys])
A0 = None
for (a, c), rs in sorted(rat.items(), key=lambda t: t[0][1]):
    vals = np.array([r * g for r, g in zip(rs, G0)])
    A, B, C = np.linalg.solve(Mx.astype(complex), vals)
    if c == 1: A0 = A
    pred = (mu(c) / c**2) if c % 2 else 0.0
    print(f"r={a}/{c}: A(r)/A(0) = {A/A0:.4f}   Lemma K: {pred:+.4f}")
