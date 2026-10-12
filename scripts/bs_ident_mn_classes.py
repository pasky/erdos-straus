"""O145 (c): solution counts f_m(p) (from bs_ident_mn MODE 1) by residue type of p mod Q:
'one' (p ≡ 1 mod Q), 'sq' (other squares mod Q), 'non' (non-squares).  Q = 840 (or argv[2]).
Prints mean and min of f/(log p)^2 and of the Type I+II count; p > 1000 only."""
import sys, math, numpy as np
Q = int(sys.argv[2]) if len(sys.argv) > 2 else 840
sq = {x * x % Q for x in range(Q) if math.gcd(x, Q) == 1}
D = np.loadtxt(sys.argv[1], dtype=np.int64); D = D[D[:, 0] > 1000]
for lab in ("one", "sq", "non"):
    sel = [r for r in D if (r[0] % Q == 1 if lab == "one" else (r[0] % Q in sq and r[0] % Q != 1) if lab == "sq" else r[0] % Q not in sq)]
    if not sel: print(f"  {lab:4s}: none"); continue
    s = np.array(sel); v = s[:, 1] / np.log(s[:, 0]) ** 2
    print(f"  {lab:4s}: n={len(s):5d}  mean f/log^2p={v.mean():.3f}  min={v.min():.3f}  (argmin p={s[v.argmin(),0]})")
