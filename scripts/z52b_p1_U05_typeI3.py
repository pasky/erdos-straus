"""z52b pass1 U05 (Z1521 follow-up, interesting-candidate): for primes p≡1 (mod 24), p≤2e4, which d≤12 admit a Type I
solution (c≤30)? Also the d=3 mod-3 argument check. Output: counts per d and per class mod 24."""
import sys
from collections import Counter
exec(open("scripts/z52b_p1_U05_typeI.py").read().split("TI = {}")[0])
cls1 = [p for p in primes if p % 24 == 1]
dcount = Counter(); none = 0
for p in cls1:
    ds = set()
    for c in range(1, 31):
        for d in range(1, 13):
            if typeI_ok(p, c, d): ds.add(d)
    for d in ds: dcount[d] += 1
    if not ds: none += 1
log(f"p≡1(24), p≤2e4: {len(cls1)} primes; with no Type I solution for any d≤12, c≤30: {none}")
log("  number of these primes having a solution with given d:", dict(sorted(dcount.items())))
# d=3 check: for p≡1 mod 3 and c with gcd(c,p)=1, no Type I with d=3 (mod-3 argument: f≡-p≡2 mod 3, all primes q|N, q∤6c, are ≡1 mod 3)
viol = 0; tests = 0
for p in primes:
    if p % 3 != 1: continue
    for c in range(1, 31):
        if c % p == 0: continue
        tests += 1
        if typeI_ok(p, c, 3): viol += 1
log(f"d=3 mod-3 argument check: p≡1(3), c≤30, gcd(c,p)=1: {tests} tests, Type I with d=3 found: {viol} (predicted 0)")
open("data/z52b/pass1/U05/2nd/typeI3_out.txt","w").write("\n".join(out)+"\n")
