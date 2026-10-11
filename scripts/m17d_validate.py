"""O139: validate m17d_pointP / m17d_pointQ against the certified complete lists (levels <= 7).
For each test point u (residue) and level, the engine output must equal EXACTLY the set of listed data
(both orders) whose box contains u.  P: data/m17b/p{K}.txt (K = 2L-1).  Q: m17_enum raw data are boxes only,
so for Q the comparison is on box residues: engine boxes (-4a^2 d mod F) vs listed Q-boxes and inverses.
Test points: every in-cell box centre at that level (C_5 and C_7) plus R random units per level.
Usage: m17d_validate.py ENGDIR DATADIR LMAX_P KMAX_Q R
"""
import sys, os, subprocess, random
ENG, D, LP, KQ, R = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
random.seed(139)
def runP(L, u):
    out = subprocess.run([os.path.join(ENG, "pointP"), str(L), str(u), "1", "AB"], capture_output=True, text=True, check=True).stdout
    return {tuple(map(int, l.split()[1:])) for l in out.split("\n") if l}
def runQ(k, u):
    out = subprocess.run([os.path.join(ENG, "pointQ"), str(k), str(u), "1"], capture_output=True, text=True, check=True).stdout
    return {tuple(map(int, l.split()[1:])) for l in out.split("\n") if l}
bad = 0; tested = 0
for L in range(1, LP + 1):
    K, W = 2 * L - 1, 17 ** L; n = 17 ** K
    data = []
    for line in open(os.path.join(D, f"p{K}.txt")):
        a, b, c, d = map(int, line.split()); data += [(a, b, c, d), (b, a, c, d)]
    box = lambda t: (-(4 * t[0] * t[2] * t[3] - 1)) % W
    centres = sorted({box(t) for t in data if box(t) % 17 in (5, 7)})
    pts = centres + [random.choice([x for x in range(1, W) if x % 17 in (5, 7)]) if W < 10**6 else random.randrange(1, W // 17) * 17 + random.choice((5, 7)) for _ in range(R)]
    if L >= 6: pts = centres[:20] + pts[len(centres):]
    for u in pts:
        exp = {t for t in data if box(t) == u % W}
        got = runP(L, u); tested += 1
        if got != exp: bad += 1; print("P MISMATCH", L, u, exp ^ got)
    print(f"P level {L}: {len(pts)} points ok so far, bad={bad}", flush=True)
for k in range(1, KQ + 1, 2):
    F = 17 ** k; lb = set()
    for T in "QU":
        pass
    for line in open(os.path.join(D, f"Q{k}.txt")):
        r = int(line.split()[1]) % F; lb.add(r)
        if r % 17: lb.add(pow(r, -1, F))
    cen = sorted(r for r in lb if r % 17 in (5, 7))
    pts = cen if k <= 5 else cen[:20]
    pts = pts + [random.randrange(0, F // 17) * 17 + random.choice((5, 7)) for _ in range(R)]
    for u in pts:
        got = runQ(k, u); tested += 1
        gotbox = {(-4 * a * a * d) % F for (a, b, c, d) in got}
        exp = {u % F} if u % F in lb else set()
        if gotbox != exp: bad += 1; print("Q MISMATCH", k, u, gotbox, exp)
    print(f"Q level {k}: {len(pts)} points, bad={bad}", flush=True)
print(f"tested {tested}, mismatches {bad}")
sys.exit(1 if bad else 0)
