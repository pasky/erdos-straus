# z52d P2 TO8: Z2941 (R(p) by least non-residue l(p)), Z2947 (gaps among (★)-positive primes p≡1 mod 840), Z2949 (l(p) of (★)-fails)
import math
from collections import defaultdict
D = 'data/z52b/pass2/TO8/'
R = {}
for l in open(D + 'R_all_1e6.txt'):
    p, r, _ = l.split(); R[int(p)] = int(r)
def is_qr(a, p): return pow(a % p, (p - 1) // 2, p) == 1
def lnr(p):
    l = 2
    while True:
        if l % p and not is_qr(l, p): return l
        l += 1
ps = sorted(R)
L = {p: lnr(p) for p in ps if p > 50}
bins = defaultdict(list)
for p in ps:
    if p <= 50: continue
    bins[L[p]].append(p)
print("Z2941: l(p) bin, n, frac(★)-fail, mean R(p)/log^2 p")
for l in sorted(bins)[:8]:
    xs = bins[l]
    print(l, len(xs), round(sum(R[p] == 0 for p in xs) / len(xs), 5), round(sum(R[p] / math.log(p) ** 2 for p in xs) / len(xs), 3))
# Z2947: progression 1 mod 840
prog = [p for p in ps if p % 840 == 1]
pos = [p for p in prog if R[p] > 0]
fails = [p for p in prog if R[p] == 0]
gaps = [b - a for a, b in zip(pos, pos[1:])]
print("Z2947: primes ≡1 mod 840 ≤1e6:", len(prog), " (★)-fail among them:", fails, " max gap between consecutive (★)-positive primes:", max(gaps), " at", pos[gaps.index(max(gaps))], "->", pos[gaps.index(max(gaps))+1])
# Z2949: l(p) of (★)-fails and controls
print("Z2949: l(p) of (★)-fails:", {p: L[p] for p in ps if R[p] == 0 and p in L})
ctrl = [L[p] for p in ps if p in L and p > 1000]
print("control share of l(p)>=7: ", round(sum(x >= 7 for x in ctrl) / len(ctrl), 4), " n=", len(ctrl), "; fails share l>=7:", round(sum(L[p] >= 7 for p in ps if R[p] == 0 and p in L) / max(1, sum(1 for p in ps if R[p] == 0 and p in L)), 3))
# Z2941 refinement: restrict to the hard class p≡1 mod 24 (2,3 are QRs there, so ℓ≥5)
hard_cls = [p for p in ps if p > 1000 and p % 24 == 1]
bins2 = defaultdict(list)
for p in hard_cls: bins2[L[p]].append(p)
print("Z2941 (p≡1 mod 24, p>1000): l, n, frac(★)-fail, mean R/log^2")
for l in sorted(bins2)[:9]:
    xs = bins2[l]
    print(l, len(xs), round(sum(R[p] == 0 for p in xs) / len(xs), 5), round(sum(R[p] / math.log(p) ** 2 for p in xs) / len(xs), 3))
c7 = [p for p in hard_cls if L[p] >= 7]
print("within p≡1 mod 24: share l>=7 =", round(len(c7) / len(hard_cls), 3), "; (★)-fails with l>=7: 7 of 9 (all failures are ≡1 mod 24 except 2 in list? check:", [p for p in ps if R[p] == 0 and p % 24 != 1], ")")
