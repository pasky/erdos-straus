# z58 MORDELL: the fixed-(u,B) (★) families K_{u,B} = {n ≡ -(u+B) mod 4uB} at the 1-points x_{l,R}
# (x = R at l, 1 elsewhere).  x ∈ K_{u,B}  iff, with a = v_l(4uB) >= 1 and w = 4uB/l^a:  w | u+B+1 and l^a | u+B+R.
# Equivalently 4uBs = l^a (u+B+1) with s = (u+B+1)/w; for u <= B this forces u <= 3 l^a/4 + 1 and
# B = l^a (u+1)/(4us - l^a).  We enumerate (a, u, s) exhaustively for a <= AMAX and list the hit residues R in [1, l-1].
# Thm S3 (memo): a hit forces a = 1 and R >= (2l-1)/3.  Also cross-checks by direct brute force over 4uB <= PMAX.
import sys
from sympy import primerange
LMAX = int(sys.argv[1]); AMAX = int(sys.argv[2]); PMAX = int(sys.argv[3])
def vl(n, l):
    a = 0
    while n % l == 0: n //= l; a += 1
    return a
viol = 0
for l in primerange(3, LMAX):
    hits = {}
    for a in range(1, AMAX + 1):
        la = l ** a
        for u in range(1, 3 * la // 4 + 2):
            s = la // (4 * u) + 1
            while True:
                D = 4 * u * s - la
                if D > la * (u + 1): break
                if D > 0 and (la * (u + 1)) % D == 0:
                    B = la * (u + 1) // D
                    if B >= u and vl(4 * u * B, l) == a:
                        w = 4 * u * B // la
                        if (u + B + 1) % w == 0:
                            R = (-(u + B)) % la
                            if 1 <= R < l: hits.setdefault(R, (u, B, a))
                s += 1
    # direct brute force (independent of the parametrisation)
    brute = {}
    for u in range(1, PMAX // 4 + 1):
        for B in range(u, PMAX // (4 * u) + 1):
            M = 4 * u * B; a = vl(M, l)
            if a == 0: continue
            la = l ** a; w = M // la
            if (u + B + 1) % w: continue
            R = (-(u + B)) % la
            if 1 <= R < l: brute.setdefault(R, (u, B, a))
    bad = [R for R in hits if not (hits[R][2] == 1 and 3 * R >= 2 * l - 1)]
    viol += len(bad)
    miss = [R for R in brute if R not in hits]
    print(f"l={l}: (u,B)-hit residues {sorted(hits)} examples {[hits[R] for R in sorted(hits)]}; "
          f"S3 violations {bad}; brute(4uB<={PMAX}) residues not found by enumeration {miss}", flush=True)
print("total S3 violations:", viol)
# Exact B criterion (memo Thm S3, after cross-model review): B-hit at (l,R) iff with u = l-R there is s >= 1 with
# 1 <= D = 4us - l <= u+1 and D | u+1.  Compare with the enumeration above (re-run for a = 1 only, l < LMAX).
def exact_b(l, R):
    u = l - R
    return any(1 <= 4 * u * s - l <= u + 1 and (u + 1) % (4 * u * s - l) == 0 for s in range(1, (l + u + 1) // (4 * u) + 2))
mm = 0
for l in primerange(3, LMAX):
    enum = set()
    for u in range(1, l + 2):
        for s in range(1, l * (u + 2) // (4 * u) + 2):
            D = 4 * u * s - l
            if D > 0 and (l * (u + 1)) % D == 0:
                B = l * (u + 1) // D
                if vl(4 * u * B, l) == 1 and (u + B + 1) % (4 * u * B // l) == 0:
                    R = (-(u + B)) % l
                    if R: enum.add(R)
    ex = {R for R in range(1, l) if exact_b(l, R)}
    if ex != enum: mm += 1; print("exact-B MISMATCH", l, sorted(ex), sorted(enum))
print("exact B criterion vs enumeration mismatches:", mm)
