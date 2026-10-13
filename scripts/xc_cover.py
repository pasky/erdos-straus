"""O200: least box side L(r) with {s1^{2a} s2^{2b} : 0<=a,b<=L} = (F_r^*)^2, for primes r = -1 mod 4 s1 s2 with
<s1^2,s2^2> = (F_r^*)^2.  Prop 3.1(c): L(r) >= sqrt((r-1)/2) - 1 (k=2).  Reports L(r)/sqrt(r) stats.
usage: xc_cover.py s1 s2 RMAX"""
import sys
from sympy import primerange
s1, s2, R = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
M = 4 * s1 * s2
rat = []
for r in primerange(M, R):
    if r % M != M - 1: continue
    h = (r - 1) // 2
    A, B = s1 * s1 % r, s2 * s2 % r
    seen = bytearray(r); cnt = 0
    # grow L; maintain powers lists
    pa = [1]; pb = [1]; L = 0
    seen[1] = 1; cnt = 1
    # check generation first: order of group generated must be h
    while cnt < h and L < r:
        L += 1
        pa.append(pa[-1] * A % r); pb.append(pb[-1] * B % r)
        for b in range(L + 1):  # new row a=L and new column b=L
            for v in (pa[L] * pb[b] % r, pa[b] * pb[L] % r):
                if not seen[v]: seen[v] = 1; cnt += 1
        if L > 4 * int(r ** .5) + 10: break
    if cnt == h:
        rat.append((L / (r ** .5), r, L))
rat.sort()
print("primes r covered:", len(rat))
print("min L/sqrt r: %.3f (r=%d,L=%d)" % rat[0], " median %.3f" % rat[len(rat)//2][0], " max %.3f (r=%d,L=%d)" % rat[-1])
print("lower bound sqrt(1/2)=0.707; fraction with L/sqrt r <= 2: %.3f" % (sum(1 for x in rat if x[0] <= 2) / len(rat)))
