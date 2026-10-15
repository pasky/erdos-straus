# z14_probe.py — which window classes contain a given profinite point mu (given as residues l:c for l in a list, all other
# odd-prime coordinates = c_default); reports firing windows and their periods.
# Usage: PYTHONPATH=scripts uv run python scripts/z14_probe.py c0 k JMAX MMAX "2:8:16,3:0:9" default
import sys
from math import lcm
from sympy import factorint
from sympy.ntheory.modular import crt
from z14_win import make_windows, window_period, fires
c0, k, JMAX, MMAX = map(int, sys.argv[1:5])
spec = [tuple(map(int, t.split(':'))) for t in sys.argv[5].split(',')]   # l:c:modulus(l-power)
dflt = int(sys.argv[6])
W = make_windows(c0, k, JMAX, MMAX, WMAX=10, HS=(1, 3, 5, 7, 9, 15), T1MAX=40)
hits = []
for w in W:
    P = window_period(w)
    # point: for each prime power of P use spec residue if the prime is in spec, else dflt
    mods, res = [], []
    for q, v in factorint(P).items():
        mods.append(q ** v)
        sp = [c for (l, c, M) in spec if l == q]
        res.append((sp[0] if sp else dflt) % q ** v)
    s, _ = crt(mods, res) if mods else (0, 1)
    s = int(s) + P * 10 ** 3
    if fires(w, s, c0, k): hits.append((w['m'], w['j'], w['kind'], P))
print(len(W), 'windows;', len(hits), 'fire:', sorted(hits, key=lambda h: h[3])[:12])
