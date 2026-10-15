"""Validation of se_box.c (EVIDENCE): exact enumeration of P-data (resp. Q-data) for given N, bucketed into the
dyadic boxes/rows of se_box (g=1, t=1), compared with the printed per-box and per-row bounds. Exit 1 on violation.
P: (a,b), a <= b, 2ab <= N: e = -N mod 4ab, need 1 <= e <= a+b, e | a+b; c=(a+b)/e, d=(N+e)/(4ab)  (no primitivity filter:
   the bound is checked against the larger set of all N-points with gcd(N, abcd)=1 where the unit-class steps are valid).
Q: (a,d) pairs with f | 4a^2d+1, f == -F (mod 4ad), 0 < f <= F+2 ; c=(f+F)/(4ad), e=(4a^2d+1)/f, b=ce-a >= a, r∤abcde."""
import sys, subprocess, math, collections
mode, N = sys.argv[1], int(sys.argv[2])
exe = sys.argv[3] if len(sys.argv) > 3 else '/tmp/se/se_box_v'
out = subprocess.run([exe, mode, '0', '0', '1', '1', '1000'], env={'SE_EXACT': str(N), 'SE_DUMP': '1'},
                     capture_output=True, text=True).stdout
B, Rw = {}, {}
for line in out.splitlines():
    f = line.split()
    if f[0] == 'B': B[(int(f[1]), int(f[2]), int(f[3]))] = float(f[4])
    if f[0] == 'R': Rw[(int(f[1]), int(f[2]))] = float(f[3])
def p2(x): return 1 << (x.bit_length() - 1)
cnt, rcnt = collections.Counter(), collections.Counter()
if mode == 'P':
    a = 1
    while 2 * a * a <= N:
        for b in range(a, N // (2 * a) + 1):
            e = (-N) % (4 * a * b)
            if e == 0 or e > a + b or (a + b) % e: continue
            c, d = (a + b) // e, (N + e) // (4 * a * b)
            if math.gcd(N, a * b * c * d) != 1: continue
            cnt[(p2(a), p2(d), p2(c))] += 1; rcnt[(p2(a), p2(d))] += 1
        a += 1
else:
    F = N
    for a in range(1, F + 1):
        if a > (F + 1) // 2: break
        for d in range(1, (F + 1) // (2 * a) + 1):
            m = 4 * a * a * d + 1
            for f in range((-F) % (4 * a * d) or 4 * a * d, F + 3, 4 * a * d):
                if m % f: continue
                c = (f + F) // (4 * a * d); e = m // f; b = c * e - a
                if b < a or math.gcd(F, a * b * c * d * e) != 1: continue
                assert 4 * a * b * c * d == F * (a + b) + c
                cnt[(p2(c), p2(d), p2(f))] += 1; rcnt[(p2(c), p2(d))] += 1
viol = [(k, v, B.get(k, 0)) for k, v in cnt.items() if v > B.get(k, 0)]
rviol = [(k, v, Rw.get(k, 0)) for k, v in rcnt.items() if v > Rw.get(k, 0)]
print(mode, N, "data", sum(cnt.values()), "boxes", len(cnt), "box-violations", len(viol), "row-violations", len(rviol),
      "bound", f"{sum(Rw.values()):.4g}")
if viol or rviol: print(viol[:5], rviol[:5]); sys.exit(1)
