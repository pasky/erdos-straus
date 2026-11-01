# Z0077 part 2: search totally positive z in O_K (K cyclic cubic, conductor 7/9/13/19) with Tr(1/z) = s2(z)/N(z) in 4Z.
# Any such z gives x = p*(Tr(1/z)/4)*z with Tr(1/x) = 4/p for EVERY p (and every n), so for p inert in K
# (where p | N(x) forces p | x) the problem is p-independent: solvable for all inert p or for none.
# Also records every prime p <= 1e4 with a solution x of Tr(1/x) = 4/p in the box (p*s2(x) = 4N(x)).
# Exact integer arithmetic: N, s2 via closed forms from the multiplication matrix (int64 numpy, |coords| <= B).
import numpy as np, sys, json
FIELDS = {7: [1, 1, -2, -1], 9: [1, 0, -3, 1], 13: [1, 1, -4, 1], 19: [1, 1, -6, -7]}
import os
if os.environ.get("SPLIT2"): FIELDS = {31: [1, 1, -10, -8], 43: [1, 1, -14, 8], 73: [1, 1, -24, -27]}  # Z[theta] of index 2, 2, 3; 2 splits for 31, 43, inert for 73
B = int(sys.argv[1]); ALLSIGN = len(sys.argv) > 2
res = {}
for f, co in FIELDS.items():
    c2, c1, c0 = co[1], co[2], co[3]
    M = np.array([[0, 0, -c0], [1, 0, -c1], [0, 1, -c2]], dtype=np.int64); M2 = M @ M
    roots = np.roots(co).real
    r = np.arange(-B, B + 1, dtype=np.int64)
    found = []; ntp = 0; tr_hist = {}; hitp = {}
    for a in r:
        bb, cc = np.meshgrid(r, r, indexing='ij'); bb = bb.ravel(); cc = cc.ravel()
        conj = a + bb[:, None] * roots + cc[:, None] * roots**2
        pos = (np.abs(conj) > 1e-9).all(axis=1) if ALLSIGN else (conj > 1e-9).all(axis=1)
        bb, cc = bb[pos], cc[pos]; ntp += len(bb)
        # matrix entries A = a I + b M + c M2 (vectorised), then trace, s2, det exactly
        A = a * np.eye(3, dtype=np.int64)[None] + bb[:, None, None] * M[None] + cc[:, None, None] * M2[None]
        tr = A[:, 0, 0] + A[:, 1, 1] + A[:, 2, 2]
        s2 = (A[:, 0, 0] * A[:, 1, 1] - A[:, 0, 1] * A[:, 1, 0] + A[:, 0, 0] * A[:, 2, 2] - A[:, 0, 2] * A[:, 2, 0]
              + A[:, 1, 1] * A[:, 2, 2] - A[:, 1, 2] * A[:, 2, 1])
        det = (A[:, 0, 0] * (A[:, 1, 1] * A[:, 2, 2] - A[:, 1, 2] * A[:, 2, 1]) - A[:, 0, 1] * (A[:, 1, 0] * A[:, 2, 2] - A[:, 1, 2] * A[:, 2, 0])
               + A[:, 0, 2] * (A[:, 1, 0] * A[:, 2, 1] - A[:, 1, 1] * A[:, 2, 0]))
        okp = (s2 > 0) & ((4 * det) % np.where(s2 > 0, s2, 1) == 0)
        for b_, c_, s, d in zip(bb[okp], cc[okp], s2[okp], det[okp]):
            pp = int(4 * d // s)
            if 2 < pp <= 10**4 and all(pp % k for k in range(2, int(pp**0.5) + 1)): hitp.setdefault(pp, [int(a), int(b_), int(c_)])
        ok = (s2 % det == 0)
        for b_, c_, s, d in zip(bb[ok], cc[ok], s2[ok], det[ok]):
            t = int(s // d); tr_hist[t % 4] = tr_hist.get(t % 4, 0) + 1
            if t % 4 == 0: found.append(dict(z=[int(a), int(b_), int(c_)], N=int(d), TrInv=t))
    res[f] = dict(B=B, totally_positive=ntp, integral_TrInv_mod4_hist=tr_hist, n_found=len(found), found=found[:20])
    print(f"conductor {f}, box {B}: {ntp} totally positive z; Tr(1/z) integral: residues mod 4 histogram {tr_hist}; "
          f"with 4 | Tr(1/z): {len(found)} e.g. {found[:4]}; primes p<=1e4 with Tr(1/x)=4/p solved in box: {len(hitp)}: {sorted(hitp)[:40]}", flush=True)
    res[f]['primes_hit'] = {str(k): v for k, v in sorted(hitp.items())}
json.dump(res, open(f'data/z52b/pass2/ZF1/Z0077/tr4_B{B}{'_allsign' if ALLSIGN else ''}{'_f31_43_73' if os.environ.get('SPLIT2') else ''}.json', 'w'), indent=1)
