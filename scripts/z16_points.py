"""z16_points.py (O241): alive depth of chosen points of the c-slices against the tuple balls dumped by z16_tree.py.
Points: (i) all rationals u = P/Q in X_c (P, Q in F3[T], T ∤ Q, max(deg P, deg Q) <= H, as distinct power series mod T^DMAX);
(ii) Mahler-type algebraic Liouville points u = 1 + cT + T^9 + T^81 (mod T^DMAX) etc.  Prints, per height, the fraction of
rational points alive to depth DMAX (i.e. in no ball), against the cylinder-average alive fraction.
usage: python3 scripts/z16_points.py BALLFILE DMAX H"""
import sys, itertools
bf, D, H = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
balls = set(l.split()[1] for l in open(bf))
def alive(u):  # u: list of D digits
    s = "".join(map(str, u))
    return not any(s[:d] in balls for d in range(3, D + 1))
def mul(a, b):
    r = [0] * D
    for i, x in enumerate(a[:D]):
        if x:
            for j, y in enumerate(b[:D - i]): r[i + j] = (r[i + j] + x * y) % 3
    return r
def inv(a):  # power-series inverse mod T^D, a[0] != 0
    r = [0] * D; r[0] = 1 if a[0] == 1 else 2
    for n in range(1, D):
        s = sum(a[i] * r[n - i] for i in range(1, min(n, len(a) - 1) + 1)) % 3
        r[n] = (-s * r[0]) % 3
    return r
seen = {}
for h in range(0, H + 1):
    for P in itertools.product(range(3), repeat=h + 1):
        for Q in itertools.product(range(3), repeat=h + 1):
            if Q[0] == 0 or max([i for i, x in enumerate(P) if x] + [-1]) < 0: continue
            u = mul(list(P), inv(list(Q)))
            if u[0] != 1 or u[1] == 0: continue
            key = tuple(u)
            ht = max(max([i for i, x in enumerate(P) if x]), max([i for i, x in enumerate(Q) if x]))
            if key not in seen or seen[key] > ht: seen[key] = ht
for h in range(1, H + 1):
    pts = [k for k, v in seen.items() if v == h]
    al = sum(alive(list(k)) for k in pts)
    print(f"height {h}: {len(pts)} rational points in X_1 ∪ X_2, alive to depth {D}: {al} ({al / max(1, len(pts)):.3f})")
for c in (1, 2):
    for name, ex in (("1+cT+T^9+T^81", [9, 81]), ("1+cT+T^3+T^9+T^27", [3, 9, 27]), ("1+cT", [])):
        u = [0] * D; u[0] = 1; u[1] = c
        for e in ex:
            if e < D: u[e] = (u[e] + 1) % 3
        print(f"c={c} {name}: alive to depth {D}: {alive(u)}")
