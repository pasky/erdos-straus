"""Fix round TO3: word census to 1e8 (binary dumps from /tmp/z52/big/*.bin, produced by
scripts/z52d_p2_TO3_census_bin.c and scripts/z52d_p2_TO3_minwords_bin.c, same logic as scripts/z52b_fingerprint_words.c /
z52b_fingerprint_minwords.c). Items: Z0753 (re-certify census), Z0754 (odd I3 zeros), Z0755 (I3 at squares m^2, m<=1e4),
Z0756 (smooth-m test), Z0761 (C_min for n = 5 mod 8), Z0763 (mean R/log^2 n windows), Z0766 (zero rates by n mod 840),
Z0767 (I3=1), Z0770 (diagonal-parity check), Z0771 (joint Uv/I3 zeros). Writes data/z52b/pass2/TO3/census1e8_results.json"""
import json, math, numpy as np
N = 10**8
W = np.memmap('/tmp/z52/big/words1e8.bin', dtype=np.uint32, mode='r', shape=(N + 1, 7))
MW = np.memmap('/tmp/z52/big/minwords1e8.bin', dtype=np.uint32, mode='r', shape=(N + 1, 3))
n = np.arange(N + 1, dtype=np.int64)
W_ = np.asarray(W[:, 0]); I3 = np.asarray(W[:, 1]); R = np.asarray(W[:, 2]); Uv = np.asarray(W[:, 3]); ESC = np.asarray(W[:, 4])
cm = np.asarray(MW[:, 0]); vm = np.asarray(MW[:, 1])
out = {}
sq = np.zeros(N + 1, bool)
r = np.arange(0, 10**4 + 1, dtype=np.int64); sq[r * r] = True; sq[0] = False  # squares up to 1e8 incl 1e8 handled below
sq[(np.arange(10**4 + 1, dtype=np.int64)) ** 2] = True
# squares up to 1e8 are m^2 with m<=1e4
sq[0] = False
ns = n[1:]
def isq(a): return sq[a]
I3z = ns[I3[1:] == 0]
out['Z0753'] = dict(I3_zero_count_le1e8=int(len(I3z)), I3_zero_max=int(I3z.max()),
                    I3_zeros_gt1e6=[int(x) for x in I3z if x > 10**6][:50],
                    R_zero_count_le1e8=int((R[1:] == 0).sum()),
                    Uv_zero_odd_nonsq_1mod4_list=[int(x) for x in ns[(Uv[1:] == 0) & (ns % 4 == 1) & ~isq(ns)]][:50],
                    ESC_zero_nonsquare_list=[int(x) for x in ns[(ESC[1:] == 0) & ~isq(ns)]])
odd_I3 = ns[(I3[1:] == 0) & (ns % 2 == 1) & (ns > 50)]
out['Z0754'] = dict(odd_I3_zeros_gt50=[int(x) for x in odd_I3], last_odd_I3_zero=int(odd_I3.max()) if len(odd_I3) else None)
sqs = np.arange(1, 10**4 + 1, dtype=np.int64)
I3sq = I3[sqs * sqs]
out['Z0755'] = dict(I3sq_zero_m=[int(m) for m in sqs[I3sq == 0]],
                    mean_I3sq_by_div={d: float(I3sq[sqs % d == 0].mean()) for d in (2, 4, 12, 60, 780)},
                    mean_I3sq_not={d: float(I3sq[sqs % d != 0].mean()) for d in (4, 780)},
                    frac_zero_by_div={d: float((I3sq[sqs % d == 0] == 0).mean()) for d in (4, 12, 60, 780)},
                    div780_count=int((sqs % 780 == 0).sum()),
                    zeros_div_by_780=[int(m) for m in sqs[(I3sq == 0) & (sqs % 780 == 0)]])
m_zero = sqs[I3sq == 0]
def smooth(m, B=7):
    x = int(m)
    for p in (2, 3, 5, 7):
        while x % p == 0: x //= p
    return x == 1
out['Z0756'] = dict(I3sq_zero_m_le1e4=[int(m) for m in m_zero],
                    largest_prime_factor={int(m): max([p for p in range(2, int(m) + 1) if int(m) % p == 0 and all(p % q for q in range(2, int(p ** .5) + 1))] or [1]) for m in m_zero})
# Z0761: C_min for n = 5 mod 8 (minimal t/4 over R-words); R zero counts
m5 = ns[(ns % 8 == 5)]
c5 = cm[m5]
out['Z0761'] = dict(n_5mod8=int(len(m5)), R0_count_5mod8_nonsq=int(((R[m5] == 0) & ~isq(m5)).sum()),
                    cmin_hist={int(k): int(v) for k, v in zip(*np.unique(c5, return_counts=True)) if k <= 40},
                    max_cmin_5mod8_le1e8=int(c5.max()), argmax=[int(x) for x in m5[c5 == c5.max()][:5]],
                    frac_cmin1=float((c5 == 1).mean()))
c5b = cm[m5[m5 <= 10**6]]
out['Z0761']['max_cmin_5mod8_le1e6'] = int(c5b.max())
# Z0763: window means of R/log^2 n over n = 1 (mod 4)
mask4 = (ns % 4 == 1)
w = {}
for X in [10**3, 10**4, 10**5, 10**6, 10**7]:
    s = mask4 & (ns >= X) & (ns < 2 * X)
    w[X] = dict(mean=float((R[1:][s[:]] / np.log(ns[s]) ** 2).mean()) if False else float((R[ns[s]] / np.log(ns[s].astype(float)) ** 2).mean()), n=int(s.sum()))
out['Z0763_windows'] = w
Xs = np.array(list(w.keys()), float); ys = np.array([w[k]['mean'] for k in w])
Lg = np.log(Xs)
A = np.column_stack([np.ones(len(Xs)), 1 / Lg, 1 / Lg ** 2])
# fit mean = c0 + a/logX + b/log^2 X  (c0 free) and compare with 1/8 fixed
coef = np.linalg.lstsq(A, ys, rcond=None)[0]
A2 = np.column_stack([1 / Lg, 1 / Lg ** 2])
coef2 = np.linalg.lstsq(A2, ys - 0.125, rcond=None)[0]
out['Z0763_fit_free_const'] = [float(c) for c in coef]
out['Z0763_fit_const_1_over_8'] = [float(c) for c in coef2]
out['Z0763_note'] = 'windows [X,2X) with n = 1 mod 4; 5 dyadic points only (X=1e3..1e7); R used = words col R (= (*) count)'
# Z0766: zero rates by n mod 840 for non-squares, families R, I3, Uv, ESC
ok = ~isq(ns)
res = {}
for name, arr in (('R', R), ('I3', I3), ('Uv', Uv), ('ESC', ESC)):
    z = (arr[1:] == 0) & ok
    res[name] = dict(zero_count_nonsq=int(z.sum()),
                     residues_mod840_with_zero=sorted(set(int(x) for x in (ns[z] % 840)))[:60],
                     n_residue_classes_hit=int(len(set((ns[z] % 840).tolist()))))
out['Z0766_zero_sets_mod840'] = res
oddsq = ns[(ns % 2 == 1) & (~isq(ns)) & (ns % 4 == 1)]
out['Z0766_R0_rate_by_mod8_nonsq'] = {int(r): float((R[ns[(ns % 8 == r) & ok]] == 0).mean()) for r in (1, 3, 5, 7)}
out['Z0766_R0_by_mod8_including_squares'] = {int(r): float((R[ns[(ns % 8 == r)]] == 0).mean()) for r in (1,)}
# Z0767 I3==1 beyond 1000
out['Z0767'] = dict(I3_eq1_gt1000_count=int(((I3[1:] == 1) & (ns > 1000)).sum()), first=[int(x) for x in ns[(I3[1:] == 1) & (ns > 1000)]][:20])
# Z0771: joint zero sets among n = 1 mod 4 non-square
z_uv = (Uv[1:] == 0) & (ns % 4 == 1) & ok
z_i3 = (I3[1:] == 0) & (ns % 4 == 1) & ok
out['Z0771'] = dict(Uv0_count=int(z_uv.sum()), I3_0_count=int(z_i3.sum()), intersection=[int(x) for x in ns[z_uv & z_i3]],
                    Uv0_list=[int(x) for x in ns[z_uv]][:30], I3_0_list=[int(x) for x in ns[z_i3]][:40])
# Z0770: diagonal parity (u = v) vs R parity on n <= 1e5 (R from the census)
diag_par_ok = 0; tot = 0; mism = []
for nn in range(2, 100001):
    D = 0
    for u in range(1, int(math.isqrt(nn)) + 3):
        num = nn + 2 * u
        if num % (u * u) == 0:
            t = num // (u * u)
            if t % 4 == 0 and t >= 4 and t > 0: D += 1
    tot += 1
    if (int(R[nn]) - D) % 2 == 0: diag_par_ok += 1
    elif len(mism) < 5: mism.append(nn)
out['Z0770_diag_parity_agreement_le1e5'] = [diag_par_ok, tot]
out['Z0770_mismatch_first'] = mism
json.dump(out, open('data/z52b/pass2/TO3/census1e8_results.json', 'w'), indent=1, default=str)
for k, v in out.items(): print(k, str(v)[:500])
