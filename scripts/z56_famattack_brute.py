# Brute-force R(n) = #{(u,B,C): 4uBC - u - B = n} for small odd n; compare with wcount output.
import sys
def R(n):
    c = 0
    for u in range(1, n + 1):
        if 3 * u - 1 > n: break
        for B in range(1, n + 1):
            if 4 * u * B - u - B > n: break
            if (n + u + B) % (4 * u * B) == 0: c += 1
    return c
ref = {}
for line in open(sys.argv[1]):
    f = line.split(); ref[int(f[0])] = int(f[1])
bad = 0; checked = 0
for n in sorted(ref)[:int(sys.argv[2])]:
    checked += 1
    if R(n) != ref[n]: bad += 1; print("MISMATCH", n, R(n), ref[n])
print("checked", checked, "mismatches", bad)
