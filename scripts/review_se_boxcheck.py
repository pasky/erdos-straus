"""R222: from-scratch per-box validation of the author's se_box binary for box ratios lam = 2^s, s = 1..4
(the certified tables use s up to 9 in P_q1.txt; the author's own se_box_check.py only exercised s = 1).
For N = r^K (P) resp. F = r^k (Q), enumerate all in-cell data with the reviewer's enumerator (review_se_lemmas.py),
bucket them into the boxes [2^{s i}, 2^{s(i+1)}) of se_box (P: (a, d, c); Q: (c, d, f)), and check every dumped per-box
bound (SE_DUMP 'B' lines) and per-row bound ('R' lines) is >= the true count.  Usage: needs /tmp/r222/se_box compiled
from scripts/se_box.c.   uv run python scripts/review_se_boxcheck.py"""
import subprocess, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from review_se_lemmas import pdata, qdata

def run(mode, N, s):
    # q=1, T chosen so that s = floor(j/T) with j = 40: T = 40 // s gives floor(40/T) = s for s in 1..4 (T=40,20,13,10)
    T = {1: 40, 2: 20, 3: 13, 4: 10}[s]
    env = dict(os.environ, SE_EXACT=str(N), SE_DUMP="1")
    out = subprocess.run(["/tmp/r222/se_box", mode, "40", "40", "1", "1", str(T), "24"], env=env, capture_output=True,
                         text=True, timeout=1200).stdout
    B, R = {}, {}
    for line in out.splitlines():
        f = line.split()
        if f[0] == 'B': B[tuple(int(float(x)) for x in f[1:4])] = float(f[4])
        if f[0] == 'R': R[tuple(int(float(x)) for x in f[1:3])] = float(f[3])
    return B, R

def box(x, s):
    return 1 << (s * ((x.bit_length() - 1) // s))

def check(mode, r, k, s):
    N = r ** k
    B, R = run(mode, N, s)
    cnt, rows = {}, {}
    if mode == 'P':
        for (a, b, c, d, e) in pdata(N):
            if a % r == 0 or b % r == 0 or c % r == 0 or d % r == 0: continue
            key = (box(a, s), box(d, s), box(c, s)); cnt[key] = cnt.get(key, 0) + 1
    else:
        for (a, b, c, d, e, f) in qdata(N):
            if e % r == 0 or c % r == 0: continue
            key = (box(c, s), box(d, s), box(f, s)); cnt[key] = cnt.get(key, 0) + 1
    bad = 0; tight = 0
    for key, n in cnt.items():
        v = B.get(key)
        if v is None or v < n: bad += 1; print("VIOLATION box", mode, r, k, s, key, n, v)
        elif v < 2 * n: tight += 1
        rows[key[:2]] = rows.get(key[:2], 0) + n
    for key, n in rows.items():
        v = R.get(key)
        if v is None or v < n: bad += 1; print("VIOLATION row", mode, r, k, s, key, n, v)
    print(f"{mode} N={r}^{k} lam=2^{s}: data {sum(cnt.values())}, occupied boxes {len(cnt)}, dumped boxes {len(B)}, "
          f"violations {bad}, boxes within factor 2 {tight}")
    return bad

if __name__ == '__main__':
    tot = 0
    for s in (1, 2, 3, 4):
        for (r, k) in [(17, 5), (7, 7), (3, 13), (101, 3), (23, 5)]:
            tot += check('P', r, k, s)
        for (r, k) in [(17, 3), (23, 3), (9973, 1), (99991, 1), (7, 5)]:
            tot += check('Q', r, k, s)
    print("TOTAL violations", tot); sys.exit(1 if tot else 0)
