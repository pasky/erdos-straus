"""z60 RAYCLASS small exact checks.
(1) Cor 2.1: for non-square n = s*m^2 ≡ 1 (4), s squarefree, m > 1, n ≤ NMAX: no (★) hit at any level C with s | C.
    Also: for every level C with s ∤ C ... (not claimed).
(2) Group lemma 4.1: G = {(x,y) in D4 x D4 : pi(x) = psi(pi(y))}, psi swapping rbar <-> sbar; |G|, [G,G], order of (r,s) in G^ab.
"""
import math, itertools
def sqfree_part(n):
    s, m = 1, 1; x = n; p = 2
    while p * p <= x:
        e = 0
        while x % p == 0: x //= p; e += 1
        if e % 2: s *= p
        m *= p ** (e // 2); p += 1
    return s * x, m
def hits_levels(n):
    # all (★) solutions: d ≡ 3 (4), d ≤ (4n+1)/3, r = -n mod d, r | (d+1)/4 ; level C = (d+1)/(4r)
    out = set()
    for d in range(3, (4 * n + 1) // 3 + 1, 4):
        r = (-n) % d
        if r and ((d + 1) // 4) % r == 0: out.add((d + 1) // (4 * r))
    return out
NMAX = 60000; cnt = viol = 0
for n in range(5, NMAX + 1, 4):
    s, m = sqfree_part(n)
    if m == 1 or s == 1: continue
    cnt += 1
    viol += sum(1 for C in hits_levels(n) if C % s == 0)
print(f"(1) non-square non-squarefree n ≡ 1 (4) ≤ {NMAX}: {cnt} integers, hits at levels C ≡ 0 (mod s): {viol}")
# (2) D4 as permutations of the square's vertices
def comp(a, b): return tuple(a[b[i]] for i in range(4))   # a∘b
def inv(a):
    r = [0] * 4
    for i, x in enumerate(a): r[x] = i
    return tuple(r)
e = (0, 1, 2, 3); r = (1, 2, 3, 0); s = (0, 3, 2, 1)
D = {e}
while True:
    new = {comp(a, b) for a in D | {r, s} for b in D | {r, s}} | D
    if new == D: break
    D = new
assert len(D) == 8
rot = {e, r, comp(r, r), comp(r, comp(r, r))}
def pi(x):  # (rotation class mod r^2 , reflection bit)
    refl = 0 if x in rot else 1
    y = x if refl == 0 else comp(x, s)    # rotation part
    k = [e, r, comp(r, r), comp(r, comp(r, r))].index(y)
    return (k % 2, refl)
psi = lambda t: (t[1], t[0])
G = [(x, y) for x in D for y in D if pi(x) == psi(pi(y))]
def gm(a, b): return (comp(a[0], b[0]), comp(a[1], b[1]))
def gi(a): return (inv(a[0]), inv(a[1]))
comms = {gm(gm(a, b), gm(gi(a), gi(b))) for a in G for b in G}
H = set(comms)
while True:
    new = {gm(a, b) for a in H for b in H} | H
    if new == H: break
    H = new
g = (r, s); g2 = gm(g, g)
print(f"(2) |G| = {len(G)}, |[G,G]| = {len(H)}, (r,s) in G: {g in set(G)}, (r,s)^2 in [G,G]: {g2 in H}, (r,s)^4 in [G,G]: {gm(g2, g2) in H}")
cc = [(x, y) for (x, y) in G if x not in rot and y not in rot]
print(f"    elements that are reflections in both factors (complex-conjugation candidates): {len(cc)}")
