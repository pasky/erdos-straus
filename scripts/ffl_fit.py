"""Summaries of data/ffl/grid.txt (FUNCTIONFIELD_ES.md §3): theta = -ln(frac)/mean for NII0 and FAIL."""
import re, math, sys
rows = []
for line in open('data/ffl/grid.txt'):
    m = dict(re.findall(r'(\w+)=([\w.,]+)', line))
    rows.append(m)
for m in rows:
    q, A, n = int(m['q']), m['A'], int(m['n']); irr = int(m['irr']); z = int(m['NII0']); f = int(m['FAIL']); mu = float(m['meanNII'])
    th = -math.log(z / irr) / mu if z else float('nan')
    print(f"q={q:2d} A={A:5s} n={n:2d} irr={irr:9d} meanNII={mu:8.2f} q^k*mean/n^3={mu*q**(len(A)-1)/n**3:6.3f} NII0={z:6d} thetaII={th:5.2f} FAIL={f}")
