# R229 from-scratch: S_8 on chi=-1 words of primes p = 1 mod 4 < PMAX vs independent-bit model.
import sys, math
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
def isprime(p): return p > 1 and all(p % q for q in range(2, int(p**.5) + 1))
def words(p):
    for t in range(1, p + 3):
        N = t * p + 1
        for u in range(1, p + 3):
            A = t * u - 1
            if A <= 0: continue
            if A * A > N: break
            if N % A == 0 and (N // A + 1) % t == 0:
                v = (N // A + 1) // t
                yield (t, u, v)  # one representative per reversal pair (A <= A*)
W4 = W8 = 0; pred = 0.0; empt = []; v2over = 0; fourA = 0
for p in range(5, PMAX, 4):
    if not isprime(p): continue
    lp = 0.0; any8 = False
    for t, u, v in words(p):
        P = (t, u, v, t*u - 1, t*v - 1)
        c4 = sum(x % 4 == 0 for x in P)
        if not c4: continue
        W4 += 1
        if any(x % 8 == 0 for x in P): W8 += 1; any8 = True
        lp += math.log(0.5 if c4 == 1 else 0.25)
    pred += math.exp(lp)
    if not any8: empt.append(p)
print(f"p=1 mod 4 < {PMAX}: chi=-1 words mod reversal {W4}, S8 share {W8/W4:.4f}; predicted empties {pred:.2f}; observed {len(empt)}: {empt}")
for p in (131, 241):
    ws = [w for w in words(p) if any(x % 4 == 0 for x in (w[0], w[1], w[2], w[0]*w[1]-1, w[0]*w[2]-1))]
    vals = [x for t, u, v in ws for x in (t, u, v, t*u-1, t*v-1) if x % 4 == 0]
    print(p, "chi=-1 words mod reversal:", len(ws), "max v2 of 4-divisible entries:", max((x & -x).bit_length() - 1 for x in vals))
