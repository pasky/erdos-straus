"""O109: compare typei4_lb outputs (lb_L_b.txt) with review_typei4_jsearch outputs (js_L_b.txt) in a directory.
A cell is compared only if the js file has its DONE line.  Key = (L, b, c', k', F, e).
Usage: typei7_xcheck.py DIR"""
import sys, glob, os, re

d = sys.argv[1]
ok = bad = 0
for js in sorted(glob.glob(os.path.join(d, "js_*.txt"))):
    txt = open(js).read()
    if "DONE" not in txt:
        continue
    L, b = map(int, re.findall(r"js_(\d+)_(\d+)", js)[0])
    J = set()
    for line in txt.splitlines():
        if line.startswith("HIT"):
            kv = dict(x.split("=") for x in line.split()[1:])
            J.add((L, b, int(kv["c'"]), int(kv["k'"]), int(kv["F"]), int(kv["e"])))
    lbf = os.path.join(d, f"lb_{L}_{b}.txt")
    B = set()
    for line in open(lbf):
        f = list(map(int, line.split()))
        if len(f) == 10:
            B.add((L, b, f[3], f[7], f[8], f[9]))
    # orientation: js may list (F,e) in either order
    norm = lambda S: {(x[0], x[1], x[2], x[3], min(x[4], x[5]), max(x[4], x[5])) for x in S}
    same = norm(J) == norm(B)
    ok += same; bad += not same
    print(L, b, len(J), len(B), "OK" if same else "MISMATCH")
print("cells agree", ok, "disagree", bad)
