"""zc_drive.py (O226): per-pattern exact enumeration driver for q = 9, k = 1, primitive slices (FF_ODD_ABSENCE §2).
Runs zc_enum (binary path argv[1]) on every eps-compatible pattern of level s (ZC_ONLY), in decreasing order of route-bound
mass (file from `ZC_PAT=1 zc_sum9 s s -`), each with a wall-clock timeout; patterns already present in an existing partial
file (exact lines) are reused. Timeouts are written as 'SKIP' lines (zc_sum9 then uses the route bound).
usage: zc_drive.py ZC_ENUM s patbounds.txt out.txt timeout_s [partial.txt]"""
import sys, subprocess
exe, s, pb, out, TO = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], float(sys.argv[5])
have = {}
if len(sys.argv) > 6:
    for l in open(sys.argv[6]):
        x = l.split()
        if x[5] != 'SKIP':
            have[tuple(map(int, x[1:4]))] = l.strip()
rows = []
for l in open(pb):
    x = l.split()
    if x[0] == 'P' and int(x[1]) == s:
        rows.append((float(x[6]), tuple(map(int, x[2:5])), int(x[5])))
rows.sort(reverse=True)
res = {}
for mass, (a, z, y), t in rows:
    if (a, z, y) in have:
        res[(a, z, y)] = have[(a, z, y)]; continue
    try:
        r = subprocess.run([exe, '9', str(s), str(s), '30', '0', '1', '3', '2', '0', '1'], env={'ZC_ONLY': f'{a} {z} {y}'},
                           capture_output=True, text=True, timeout=TO)
        ls = [l for l in r.stdout.splitlines() if l.strip()]
        if r.returncode != 0 or len(ls) != 1 or ls[0].split()[:5] != [str(s), str(a), str(z), str(y), str(t)]:
            sys.exit(f'bad run {a} {z} {y}: rc={r.returncode} {r.stdout!r} {r.stderr!r}')
        res[(a, z, y)] = ls[0]
    except subprocess.TimeoutExpired:
        res[(a, z, y)] = f'{s} {a} {z} {y} {t} SKIP timeout'
        print(f'timeout {a} {z} {y} mass {mass:.4g}', file=sys.stderr, flush=True)
with open(out, 'w') as f:
    for k in sorted(res):
        f.write(res[k] + '\n')
