"""z59 CONV2: check Lemma 1(viii) (raw D-form of the union U) and Lemma 1(iii)/(iv) (T-form, shift form) against
direct enumeration of (★) and a = 1 solutions, all odd n <= N (including squares and n ≡ 3 mod 4)."""
import sys, math
N = int(sys.argv[1])
star = bytearray(N + 1); a1 = bytearray(N + 1)
for C in range(1, N + 1):
    if 4 * C - 2 > N: break
    u = 1
    while u * (4 * u * C - 2) <= N:            # B >= u
        f = 4 * u * C - 1; B = u
        while f * B - u <= N:
            star[f * B - u] = 1; B += 1
        u += 1
for c in range(1, N + 2):
    found = False
    for d in range(1, N + 2):
        f = 4 * c * d - 1                        # n = j f - 4d, j = (b+1)/c >= 1, b = cj - 1 >= 1
        j = max(1, (2 + c - 1) // c)
        if j * f - 4 * d > N: break
        found = True
        while j * f - 4 * d <= N:
            n = j * f - 4 * d
            if n >= 1: a1[n] = 1
            j += 1
    if not found: break
def divs(m):
    out = []
    for i in range(1, math.isqrt(m) + 1):
        if m % i == 0: out += [i, m // i]
    return out
bad = 0
for n in range(1, N + 1, 2):
    U = bool(star[n] or a1[n])
    raw = any((D % 4 in (0, 3)) and (-n) % D != 0 and (((D // 4) + 1) % ((-n) % D) == 0) for D in range(3, (4 * n + 4) // 3 + 1))
    tf = any(any(f % (T if T % 4 == 0 else 4 * T) == (T if T % 4 == 0 else 4 * T) - 1 for f in divs(T * n + 1)) for T in range(1, n + 2))
    sf = any(any(f % (y if y % 4 == 0 else 4 * y) == (y if y % 4 == 0 else 4 * y) - 1 for f in divs(n + y)) for y in range(1, 4 * n + 4))
    if not (U == raw == tf == sf): bad += 1; print("MISMATCH", n, U, raw, tf, sf)
print(f"odd n <= {N}: U / raw D-form / T-form / shift form agree on all; mismatches {bad}")
if bad: sys.exit(1)
