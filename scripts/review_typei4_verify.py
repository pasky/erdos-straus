"""R89: big-integer re-check of HIT lines of review_typei4_jsearch against the certificate definition
(TYPEI2 (2.2) at some w = 9 mod 16): F*e = N = 1+4ck^2 with c = 2^al 7^a c', k = 2^ga 7^b k' (al+2ga = L),
F = -1 mod c'k', F = 1 mod 7^{a+b}, F = 7 mod 16; reports v2(F+9), v2(e+9) and t_min = 2+ceil(L/2).
Usage: ... | python3 scripts/review_typei4_verify.py"""
import sys, re
def v2(x):
    x = abs(x); e = 0
    while x and x % 2 == 0: x //= 2; e += 1
    return e
bad = 0; n = 0; x9 = 0
for line in sys.stdin:
    if not line.startswith("HIT"): continue
    d = dict(kv.split("=") for kv in line.split()[1:])
    L, a, b, c, k, F, e = (int(d[x]) for x in ("L", "a", "b", "c'", "k'", "F", "e"))
    N = 1 + 2 ** (L + 2) * c * 7 ** (a + 2 * b) * k * k
    ok = F * e == N and (F + 1) % (c * k) == 0 and (F - 1) % 7 ** (a + b) == 0 and F % 16 == 7
    ok &= c % 2 == 1 and k % 2 == 1 and c % 7 and k % 7 and a % 2 == 1
    tmin = 2 + (L + 1) // 2
    at9 = max(v2(F + 9), v2(e + 9)) >= tmin
    n += 1; bad += not ok; x9 += at9
    print(L, a, b, c, k, F, e, "v2(F+9)=%d v2(e+9)=%d tmin=%d" % (v2(F + 9), v2(e + 9), tmin), "OK" if ok else "BAD", "AT_X9!" if at9 else "")
print("hits", n, "bad", bad, "certificates at x9:", x9)
