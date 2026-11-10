# z70 LOOSE I6: two-term fit (A log(1/y) + B)/y + C (3 y values) for the fibre g_1; compares A(r)/A(0) with
# the prediction c^{-1} e(-a0 * inv(4)/c) (gcd(c,4) = 1), 0 otherwise.
import re, numpy as np, cmath
txt = open('data/z70/loose/i6_fibre_check.txt').read().split('y=')[1:]
ys, G0, rat = [], [], {}
for blk in txt:
    y = float(blk.split()[0]); g0 = float(re.search(r'G\(iy\)=([0-9.e+]+)', blk).group(1)); ys.append(y); G0.append(g0)
    for m in re.finditer(r'r=(\d+)/(\d+) G\(r\+iy\)/G\(iy\) = ([+-][0-9.]+) ([+-][0-9.]+)i', blk):
        rat.setdefault((int(m.group(1)), int(m.group(2))), []).append(complex(float(m.group(3)), float(m.group(4))))
Mx = np.array([[np.log(1 / y) / y, 1 / y, 1.0] for y in ys], dtype=complex)
A0 = None
for (a, c), rs in sorted(rat.items(), key=lambda t: t[0][1]):
    A = np.linalg.solve(Mx, np.array([r * g for r, g in zip(rs, G0)]))[0]
    if c == 1: A0 = A
    pred = cmath.exp(-2j * cmath.pi * a * pow(4, -1, c) / c) / c if c % 2 else 0
    print(f"r={a}/{c}: A(r)/A(0) = {A/A0:.4f}   prediction: {pred:.4f}")
