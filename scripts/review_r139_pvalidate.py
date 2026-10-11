"""R139: validate review_r139_pengine against (i) own brute force (review_r139_lemmas.Pdata) for L<=3 and
(ii) the certified lists data/m17b/p{K}.txt for L<=7, at box centres and random in-cell residues.
Requirement: engine output set == expected set of ordered data (17∤b, 17∤cd, a ≡ -u b mod W)."""
import subprocess, random, sys
random.seed(1391)
ENG = sys.argv[1]
exec(open('scripts/review_r139_lemmas.py').read().split("def Qdata")[0])
def run(L, R):
    out = subprocess.run([ENG, str(L), "res", str(R)], capture_output=True, text=True, check=True).stdout
    return {tuple(int(t.split('=')[1]) for t in ln.split()[1:5]) for ln in out.splitlines() if ln.startswith("HIT")}
def data(L):
    K = 2*L-1
    if L <= 3: D = {(a,b,c,d) for (a,b,c,d,e) in Pdata(K)}
    else:
        D = set()
        for ln in open(f"data/m17b/p{K}.txt"):
            a,b,c,d = map(int, ln.split()); D.add((a,b,c,d)); D.add((b,a,c,d))
    return {x for x in D if x[1] % 17 and x[2] % 17 and x[3] % 17}
tests = mism = 0
for L in range(1, 8):
    W = 17**L; D = data(L)
    cents = sorted({(-a*pow(b,-1,W)) % W for (a,b,c,d) in D})
    cents = [u for u in cents if u % 17 in (5, 7)]
    if L >= 5: cents = random.sample(cents, min(25, len(cents)))
    rnd = [random.randrange(W) for _ in range(400)]
    rnd = [u for u in rnd if u % 17 in (5, 7)][:15]
    for u in cents + rnd:
        exp = {x for x in D if (x[0] + u*x[1]) % W == 0}
        got = run(L, u); tests += 1
        if got != exp: mism += 1; print("MISMATCH", L, u, got ^ exp)
    print("L", L, "data", len(D), "centres tested", len(cents), "random", len(rnd), flush=True)
print("tests", tests, "mismatches", mism); sys.exit(1 if mism else 0)
