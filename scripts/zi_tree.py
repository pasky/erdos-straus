"""zi_tree.py (O244): q = 3, A = T^2 slice tree with the ET-I4 analogue balls added.
Ball sets on the slice u = 1 + cT + ... (c != 0):
  B  : Case B balls (from the O241 ball file minus the Case A balls; Case B is inversion-closed, SIBLING Prop 1.3)
  A  : Case A balls  u == -E (mod T^{alpha+2}) (bsE_caseA.route_A4, complete for alpha <= DMAX-2)
  I4 : u == -1/E (mod T^{alpha+2}) for the same data (a1, b1, E)  [FF_INVERSION_CHECK Prop 2.3]
Prints per depth the survivor counts for (A+B) and (A+B+I4), and checks inversion closure of each ball set.
usage: PYTHONPATH=scripts uv run python scripts/zi_tree.py BALLFILE DMAX"""
import sys
from collections import defaultdict
import bsE_caseA as CA
from zi_lib import inv_mod_Tn
P = 3
bf, DMAX = sys.argv[1], int(sys.argv[2])
allb = defaultdict(set)
for line in open(bf):
    d, s = line.split(); d = int(d)
    if d <= DMAX: allb[d].add(tuple(map(int, s)))
A = defaultdict(set); I4 = defaultdict(set)
for al in range(1, DMAX - 1):
    for (a1, b1, E) in CA.route_A4(P, al):
        d = al + 2
        E = list(E) + [0] * d
        u = tuple((-E[i]) % P for i in range(d))
        if u[0] != 1 or u[1] == 0: continue
        A[d].add(u)
        I4[d].add(tuple(inv_mod_Tn(list(u), d, P)))
B = {d: allb[d] - A[d] for d in allb}
for d in A: assert A[d] <= allb[d], d
def invset(S): return {tuple(inv_mod_Tn(list(u), len(u), P)) for u in S}
for name, S in (("A", A), ("B", B), ("I4", I4), ("A+I4", {d: A[d] | I4[d] for d in A}), ("A+B", allb),
                ("A+B+I4", {d: allb[d] | I4[d] for d in allb})):
    tot = sum(len(v) for v in S.values()); miss = sum(len(v - invset(v)) for v in S.values())
    print(f"{name:7s}: balls {tot:4d}, without ball at 1/u: {miss}")
print("I4 balls not already in A+B, per depth:", {d: len(I4[d] - allb[d]) for d in sorted(I4)})
for label, S in (("A+B", allb), ("A+B+I4", {d: allb[d] | I4[d] for d in range(1, DMAX + 1)})):
    print(label)
    for c in (1, 2):
        surv = {(1, c)}; row = []
        for n in range(3, DMAX + 1):
            forb = {u for u in S.get(n, ()) if u[1] == c}
            new = set(); full = 0
            for v in surv:
                ch = [v + (x,) for x in range(P)]
                if all(w in forb for w in ch): full += 1
                new.update(w for w in ch if w not in forb)
            row.append(f"d{n}:{len(new)}"); surv = new
        star = tuple(inv_mod_Tn([1, (-c) % P], DMAX, P)); sx = tuple([1, c] + [0] * (DMAX - 2))
        print(f"  c={c}: survivors {' '.join(row)};  x*_c=1+cT alive: {sx in surv};  1/x*_(-c) (lies in this slice) alive: {star in surv}")

# containment: is each A (resp. I4) ball inside a strictly larger-or-equal Case B ball / any other ball?
def anc(u, S, exclude_self=True):
    out = []
    for d in range(3, len(u) + 1):
        if u[:d] in S.get(d, ()) and not (exclude_self and d == len(u)): out.append(d)
    return out
for name, S in (("A", A), ("I4", I4)):
    inB = inBeq = inAny = 0; lst = []
    for d in sorted(S):
        for u in S[d]:
            hb = [e for e in range(3, d + 1) if u[:e] in B.get(e, ())]
            ha = [e for e in range(3, d) if u[:e] in allb.get(e, ()) or u[:e] in I4.get(e, ())]
            inB += bool(hb); inAny += bool(hb or ha)
            if not (hb or ha): lst.append((d, "".join(map(str, u))))
    print(f"{name}: {sum(len(v) for v in S.values())} balls; inside a Case B ball of depth <= own: {inB}; inside some ball (B or smaller A/I4): {inAny}; maximal: {lst}")
