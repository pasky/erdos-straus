"""R249 (note for O244): for the O241 depth<=9 ball list, which balls lack an inverse ball, and is the inverse cylinder
already covered by a ball of smaller depth? Also: which balls are Case B (own enumeration, s <= 16)."""
import sys
import review_r249_caseb as cb
Q = 3
def inv(p, n):
    p = list(p) + [0] * n; r = [0] * n; i0 = pow(p[0], Q - 2, Q)
    for i in range(n):
        acc = (1 if i == 0 else 0) - sum(p[j] * r[i - j] for j in range(1, i + 1)); r[i] = acc * i0 % Q
    return tuple(r)
balls = set()
for line in open(sys.argv[1]):
    d, u = line.split(); balls.add((int(d), tuple(int(c) for c in u)))
caseB = set()
for f in sys.argv[2:]:
    for line in open(f):
        s, m, g, w1, C1 = line.split(); s = int(s)
        E = cb.E_of(*(tuple(int(c) for c in x) for x in (m, g, w1)))
        N = (s + 1) // 2; c = list(cb.neg(E)) + [0] * 20; caseB.add((N + 1, tuple(c[:N + 1])))
def covered_by_lower(d, u):
    return [dd for dd in range(1, d) if (dd, u[:dd]) in balls]
miss = 0; miss_dead = 0; A = [b for b in balls if b not in caseB]
print("balls", len(balls), "Case B (own, s<=16):", len(balls & caseB), "others (Case A):", len(A), "own CaseB not in list:", len({b for b in caseB if b[0] <= 9} - balls))
for (d, u) in sorted(balls):
    ui = inv(u, d)
    if (d, ui) not in balls:
        miss += 1; low = covered_by_lower(d, ui)
        if low: miss_dead += 1
        print("no inverse:", d, "".join(map(str, u)), "CaseB" if (d, u) in caseB else "CaseA", "inverse", "".join(map(str, ui)), "covered at depths", low)
print("missing inverses", miss, "of which inverse cylinder already inside a lower-depth ball:", miss_dead)
