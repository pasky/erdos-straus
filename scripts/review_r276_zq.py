"""R276 from-scratch: ZQ_M evidence. For primes p in [lo, hi): z(p) = min_a max digit of a/p (Zaremba),
zq(p) = min over quadratic non-residues a. Exhaustive (with pruning) unless --first, which only searches
for a QNR with max digit <= 3."""
import sys, math
lo, hi = int(sys.argv[1]), int(sys.argv[2]); first = '--first' in sys.argv
def primes(n):
    s = bytearray([1])*(n+1); s[0:2] = b'\0\0'
    for i in range(2, math.isqrt(n)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
def maxdig(a, p, cap):  # max CF digit of a/p, early exit once > cap (returns cap+1)
    m = 0; x, y = p, a
    while y:
        q, r = divmod(x, y)
        if q > m:
            m = q
            if m > cap: return cap + 1
        x, y = y, r
    return m
out = []
for p in primes(hi):
    if p < max(lo, 7): continue
    if first:
        ok = any(pow(a, (p-1)//2, p) != 1 and maxdig(a, p, 3) <= 3 for a in range(1, p))
        out.append((p, ok)); continue
    z = zq = 10**9
    for a in range(1, p):
        qnr = pow(a, (p-1)//2, p) != 1
        cap = max(z, zq) if qnr else z
        m = maxdig(a, p, min(cap, 50))
        if m < z: z = m
        if qnr and m < zq: zq = m
    out.append((p, z, zq))
if first:
    bad = [p for p, ok in out if not ok]
    print(f"[{lo},{hi}): {len(out)} primes; no QNR with digits<=3 at: {bad}")
else:
    print(f"[{lo},{hi}): {len(out)} primes; max zq={max(o[2] for o in out)}; zq>3 at {[o[0] for o in out if o[2]>3]};"
          f" #zq>z {sum(o[2]>o[1] for o in out)} (z=2,zq=3: {sum(o[1]==2 and o[2]==3 for o in out)}), zq>z at {[(o[0],o[1],o[2]) for o in out if o[2]>o[1]][:12]}; z>3 at {[o[0] for o in out if o[1]>3]}")
