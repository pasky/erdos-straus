"""R139: validate review_r139_qengine. Reference box sets: own brute force (review_r139_lemmas.Qdata) for k=1,3;
m17_enum Q-box lists (R83-confirmed) for k=5 (/tmp/r139/Q5.txt) and k=7 (data/m17b/qu7_o93/Q7.txt).
For in-cell box centres u: engine must hit; for random in-cell u: engine hits iff u is a listed centre.
Also: for k=3 the engine's hit set must equal the brute-force data set (both boxes)."""
import subprocess, random, sys
random.seed(1392); ENG = sys.argv[1]
exec(open('scripts/review_r139_lemmas.py').read().split("fails = 0")[0].replace("def Pdata","def _P"))
def run(k, R):
    out = subprocess.run([ENG, str(k), str(R), "1"], capture_output=True, text=True, check=True).stdout
    return {tuple(int(t.split('=')[1]) for t in ln.split()[2:6]) for ln in out.splitlines() if ln.startswith("HIT")}
tests = mism = 0
for k in (1, 3, 5, 7):
    F = 17**k
    if k <= 3:
        D = [x for x in Qdata(k) if x[4] % 17]
        boxes = {(-4*a*a*d) % F for (a,b,c,d,e) in D} | {(-4*b*b*d) % F for (a,b,c,d,e) in D}
    else:
        fn = "/tmp/r139/Q5.txt" if k == 5 else "data/m17b/qu7_o93/Q7.txt"
        boxes = {int(l.split()[1]) for l in open(fn)}
    cell = sorted(u for u in boxes if u % 17 in (5, 7))
    cs = cell if len(cell) <= 60 else random.sample(cell, 60)
    rnd = [u for u in (random.randrange(F) for _ in range(300)) if u % 17 in (5, 7)][:20]
    for u in cs + rnd:
        got = run(k, u); tests += 1
        if bool(got) != (u in boxes): mism += 1; print("MISMATCH", k, u, got)
        if k <= 3:
            exp = {(a,b,c,d) for (a,b,c,d,e) in D if (-4*a*a*d - u) % F == 0 or (-4*b*b*d - u) % F == 0}
            if got != exp: mism += 1; print("SETMISMATCH", k, u, got ^ exp)
    print("k", k, "boxes", len(boxes), "in-cell", len(cell), "tested", len(cs), "+", len(rnd), flush=True)
print("tests", tests, "mismatches", mism); sys.exit(1 if mism else 0)
