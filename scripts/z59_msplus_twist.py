# z59 MSPLUS: zero data on near-square families s*m^2 (Lemma 4.1 companion), from the z58 LOGIC all-n zero census to
# 1e10 (data/z58/logic/zeros_1e10.txt.gz).  For every non-square s = 1 (mod 4), 5 <= s < 3000: number of odd m with
# s m^2 <= 1e10 and the number of those with R(s m^2) = 0.  Also q^2-scaling inheritance of zeros.
import gzip, math
Z = set(int(x) for x in gzip.open('data/z58/logic/zeros_1e10.txt.gz', 'rt'))
M = {1, 121, 169, 289, 361, 529}
rows = []
for s in range(5, 3000, 4):
    r = math.isqrt(s)
    if r * r == s: continue
    ms = [m for m in range(1, math.isqrt(10**10 // s) + 1, 2)]
    zs = [m for m in ms if s * m * m in Z]
    rows.append((s, len(ms), zs, s % 840 in M))
mx = max(len(r[2]) for r in rows)
print(f"s-set: non-square s = 1 (4), 5 <= s < 3000: {len(rows)} values; #odd m per s: {min(r[1] for r in rows)}..{max(r[1] for r in rows)}")
print(f"max #zeros per s: {mx}; s attaining it: {[(r[0], r[2]) for r in rows if len(r[2]) == mx]}")
rM = [r for r in rows if r[3]]
print(f"s in M classes: {len(rM)} values; #odd m per s: {min(r[1] for r in rM)}..{max(r[1] for r in rM)}; "
      f"max #zeros per s: {max(len(r[2]) for r in rM)}")
print("distribution of #zeros per s:", {k: sum(1 for r in rows if len(r[2]) == k) for k in range(mx + 1)})
ns = [n for n in Z if math.isqrt(n) ** 2 != n]
for q in [3, 5, 7, 11, 13]:
    up = sum(1 for n in ns if q * q * n <= 10**10 and q * q * n in Z)
    tot = sum(1 for n in ns if q * q * n <= 10**10)
    dn = sum(1 for n in ns if n % (q * q) == 0 and n // (q * q) in Z)
    dtot = sum(1 for n in ns if n % (q * q) == 0)
    print(f"q={q}: non-square zeros n with q^2 n <= 1e10: {tot}, q^2 n also zero: {up}; zeros with q^2 | n: {dtot}, n/q^2 zero: {dn}")
