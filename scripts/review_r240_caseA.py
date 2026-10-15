"""R240: independent Case A (k = 1) counts at q = 9 via review_r240_enum.gp caseA(); compares with the author's six-slice
counts data/zc/caseA9_4.txt (lines "A al lam be ka count", lam = deg a1').  usage: review_r240_caseA.py AL [TMAX=AL]"""
import sys, os, cypari2
pari = cypari2.Pari()
pari('read("%s")' % os.path.join(os.path.dirname(os.path.abspath(__file__)), "review_r240_enum.gp"))
al = int(sys.argv[1]); tmax = int(sys.argv[2]) if len(sys.argv) > 2 else al
M = pari("Mat(caseA(%d, %d))" % (al, tmax))
res = {}
for i in range(len(M[0]) if len(M) else 0):
    pass
rows = pari("my(M = Mat(caseA(%d, %d))); vector(matsize(M)[1], i, concat(M[i,1], M[i,2]))" % (al, tmax))
bad = 0
for r in rows:
    r = [int(v) for v in r]
    key, (n, noff, np8, lawf) = tuple(r[:4]), r[4:]
    res[key] = (n, noff, np8)
    print("A", *key, "all", n, "offF3", noff, "P8", np8, "lawfail", lawf)
    bad += lawf
au = {}
for l in open("data/zc/caseA9_4.txt"):
    f = l.split()
    if int(f[1]) == al:
        au[tuple(map(int, f[1:5]))] = int(f[5])
for k in set(au) | set(res):
    mine = res.get(k, (0, 0, 0))[1]
    if au.get(k, 0) != mine:
        print("MISMATCH six-slice", k, "author", au.get(k), "ours", mine); bad += 1
mass6 = sum(v[1] for v in res.values()) / 9**al; mass8 = sum(v[2] for v in res.values()) / 9**al
print(f"# al={al}: data {sum(v[0] for v in res.values())}, six-slice mass {mass6:.6e}, P8 mass {mass8:.6e}; author six-slice "
      f"mass {sum(au.values())/9**al:.6e}; bad = {bad}")
sys.exit(1 if bad else 0)
