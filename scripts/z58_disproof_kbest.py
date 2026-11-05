# z58 DISPROOF §5.3: offsets k = 0 (mod 840) such that many u-lines are dead on the whole family p = m^2 + k
# (Lemma 2.3: u-line dead if k + u = c t^2 with c | u and gcd(m, c t) = 1).  Lists the best k <= KMAX by the share of
# R carried by the killed lines (weights from data/z58/disproof/lines_D1a.txt for u <= 12, 0.01 for 12 < u <= 40).
import math, sys
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10**7
W = {1: .0645, 2: .0770, 3: .0341, 4: .0341, 5: .0382, 6: .0326, 7: .0084, 8: .0175, 9: .0208, 10: .0076, 11: .0165, 12: .0091}
def dead(k, u):
    for c in range(1, u + 1):
        if u % c == 0 and (k + u) % c == 0:
            q = (k + u) // c; t = math.isqrt(q)
            if t * t == q: return (c, t)
    return None
best = []
for k in range(840, KMAX + 1, 840):
    ks = [(u, dead(k, u)) for u in range(1, 41)]
    ks = [(u, d) for u, d in ks if d]
    w = sum(W.get(u, 0.01) for u, _ in ks)
    if len(ks) >= 2: best.append((w, k, ks))
best.sort(reverse=True)
for w, k, ks in best[:15]: print(f"k={k} killed share~{w:.3f} lines {[(u, c, t) for u, (c, t) in ks]}")
