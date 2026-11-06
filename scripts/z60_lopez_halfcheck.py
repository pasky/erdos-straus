"""z60 LOPEZ (review fix): branch-specific check of the U_7 halves against word enumeration.
B-half: words (x,y,z), xyz - x - z = n, with 8 | xy and 4 | y;  A-half: 8 | xy and 4 | x  (x = residue letter r; the
A residue 1 = 4 m_f mod f is the word (f+1, 1, z)).  Compares with scripts/z60_lopez_u7.c (TGT = 1, 2; f ≡ 7 mod 8).
Usage: python z60_lopez_halfcheck.py N engine_binary"""
import sys, subprocess, math
N = int(sys.argv[1]); eng = sys.argv[2]
B = bytearray(N + 1); A = bytearray(N + 1)
for x in range(1, N + 3):
    for y in range(1, N + 3):
        d = x * y - 1
        if d - x > N: break
        if d <= 0 or (x * y) % 8: continue
        z = 1
        while d * z - x <= N:
            n = d * z - x
            if n >= 1:
                if y % 4 == 0: B[n] = 1
                if x % 4 == 0: A[n] = 1
            z += 1
for t, arr in ((1, B), (2, A)):
    out = subprocess.run([eng, "7", "1", str(N + 1), "200", "0", "0"], env={"Z60_TGT": str(t)}, capture_output=True, text=True).stdout
    ez = sorted(int(l.split()[1]) for l in out.splitlines() if l.startswith("ZERO"))
    wz = [n for n in range(1, N + 1, 2) if not arr[n] and math.isqrt(n) ** 2 != n]
    print("TGT", t, "engine zeros", len(ez), "word zeros", len(wz), "identical", ez == wz, "13 in engine zeros:", 13 in ez)
