"""zi_AinB.py (O244): for every Case A datum (a1', b1, E) of depth alpha+2 <= DMAX (bsE_caseA.route_A4) list the Case B
tuples (census file of bsE_famcount ... print) whose ball u == -E_B (mod T^{N(s)+1}) contains the Case A ball.
usage: PYTHONPATH=scripts uv run python scripts/zi_AinB.py CENSUS DMAX"""
import sys, re
import bsE_caseA as CA
from zi_lib import show
P = 3
cen, DMAX = sys.argv[1], int(sys.argv[2])
Bt = []
for line in open(cen):
    m = re.match(r"s=(\d+) .*w=\[([0-9,]*)\] C=\[([0-9,]*)\] m'=\[([0-9,]*)\] g'=\[([0-9,]*)\] E=\[([0-9,]*)\]", line)
    if not m: continue
    s = int(m.group(1)); w, C, mm, g, E = ([int(x) for x in m.group(i).split(",")] for i in range(2, 7))
    Bt.append((s, (s + 1) // 2 + 1, w, C, mm, g, E))
def ball(E, d): E = list(E) + [0] * d; return tuple((-E[i]) % P for i in range(d))
for al in range(1, DMAX - 1):
    for (a1, b1, E) in sorted(CA.route_A4(P, al)):
        d = al + 2; u = ball(E, d)
        hits = [(s, dB, show(w), show(C), show(mm), show(g), show(EB)) for (s, dB, w, C, mm, g, EB) in Bt if dB <= d and ball(EB, dB) == u[:dB]]
        print(f"A: alpha={al} a1'={show(a1)} b1={show(b1)} E={show(E)} ball={''.join(map(str,u))}")
        for h in hits[:4]: print("    in B: s=%d depth=%d w=%s C=%s m'=%s g'=%s E_B=%s" % h)
        if not hits: print("    NOT inside any census Case B ball")
