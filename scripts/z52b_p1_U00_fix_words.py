# z52b pass1 U00 fix: analyses on the minwords census (scripts/z52b_fingerprint_minwords.c, N = 1.2e7).
# cm = Cmin (min t/4 over (★) words, 0 = none); vm = Vmin (min v over U-words, 0 = none); im = Tmin_I3 (0 = none).
# cmi = Cmin over INTERIOR (★) words (u,v >= 2; scripts/z52b_p1_U00_fix_minwords.c).
import numpy as np, json, sys
from sympy import primerange, legendre_symbol, isprime
TMP = '/tmp/u00/'
def load(fn):
    a = np.loadtxt(fn, dtype=np.int64)
    return a
A = load(TMP + 'minwords_12e6.txt'); cm, vm, im = A[:, 1], A[:, 2], A[:, 3]
cmi = load(TMP + 'minint_12e6.txt')[:, 1]
N = len(cm)
n = np.arange(1, N + 1)
out = {}
# Z0772: joint zeros among n ≡ 1 (mod 4)
m1 = (n % 4 == 1)
out['Z0772'] = {
 'n1mod4_le_1.2e7': int(m1.sum()),
 'R_zero(cm=0)': int(((cm == 0) & m1).sum()),
 'Uv_zero(vm=0)': int(((vm == 0) & m1).sum()),
 'I3_zero(im=0)': int(((im == 0) & m1).sum()),
 'R&Uv': int(((cm == 0) & (vm == 0) & m1).sum()),
 'R&I3': int(((cm == 0) & (im == 0) & m1).sum()),
 'Uv&I3': int(((vm == 0) & (im == 0) & m1).sum()),
 'R&Uv&I3': int(((cm == 0) & (vm == 0) & (im == 0) & m1).sum()),
 'R&Uv_first': [int(x) for x in n[(cm == 0) & (vm == 0) & m1][:20]],
}
# Z0850: boundary-only (★) primes: primes with a (★) word (cm>0) but no interior word (cmi=0); and R-zero primes
P = np.array([p for p in primerange(3, N + 1) if p % 4 == 1], dtype=np.int64)
cP, cmiP = cm[P - 1], cmi[P - 1]
bnd = P[(cmiP == 0) & (cP > 0)]
rz = P[cP == 0]
out['Z0850'] = {'n_primes_1mod4': int(len(P)), 'R_zero_primes': int(len(rz)), 'R_zero_first': [int(x) for x in rz[:15]],
                'boundary_only_primes(cmi=0,cm>0)': int(len(bnd)), 'boundary_only_first': [int(x) for x in bnd[:15]],
                'interior_zero_primes(cmi=0)': int((cmiP == 0).sum()),
                'interior_zero_and_cm_zero': int(((cmiP == 0) & (cP == 0)).sum()),
                'interior_zero_primes_last': [int(x) for x in P[cmiP == 0][-10:]]}
# Z0844: Cmin (over (★) words) by p mod 840 among primes ≡ 1 (4), cm > 0
cls = {}
for p, c in zip(P.tolist(), cP.tolist()):
    if c > 0: cls.setdefault(p % 840, []).append(c)
means = sorted(((float(np.mean(v)), k, len(v), int(np.max(v))) for k, v in cls.items() if len(v) >= 20), reverse=True)
out['Z0844'] = {'classes_with_ge20': len(means), 'top5_by_mean_Cmin': [(round(m, 2), k, c, mx) for m, k, c, mx in means[:5]],
                'bottom5_by_mean_Cmin': [(round(m, 2), k, c, mx) for m, k, c, mx in means[-5:]],
                'square_classes_mod840': {k: round(float(np.mean(cls[k])), 2) for k in [1, 121, 169, 289, 361, 529] if k in cls},
                'max_Cmin_over_primes': int(cP.max())}
# Z0930: pre-filter test. Filter F(p): p mod 840 in the six square classes AND #{q<=23 prime: (q/p)=1} >= 6.
# Target H(p): R-zero (cm=0) — the hard set the census is for.
sq6 = {1, 121, 169, 289, 361, 529}
qs = [2, 3, 5, 7, 11, 13, 17, 19, 23]
F = np.array([(p % 840 in sq6) and (sum(1 for q in qs if legendre_symbol(q, p) == 1) >= 6) for p in P.tolist()])
H = (cP == 0)
out['Z0930'] = {'n_primes': int(len(P)), 'filter_survivors': int(F.sum()), 'survivor_frac': float(F.mean()),
                'R_zero_total': int(H.sum()), 'R_zero_recall_by_filter': float((F & H).sum() / max(1, H.sum())),
                'R_zero_rate_in_survivors': float((F & H).sum() / max(1, F.sum())), 'R_zero_rate_overall': float(H.mean())}
# Z0938 / Z0945: zero sets vs A396825 (b-file fetched to /tmp/u00/A396825.b)
A396825 = set(int(l.split()[1]) for l in open(TMP + 'A396825.b') if l.strip())
Jv = [int(x) for x in n[(vm == 0) & (cm == 0)][:0]]  # placeholder
J1 = [int(x) for x in n[:1369][(cm[:1369] == 0) & (vm[:1369] == 0)]]
J2 = [int(x) for x in n[:1369][(vm[:1369] == 0)]]
J3 = [int(x) for x in n[:1369][(cm[:1369] == 0)]]
bmax = max(A396825)
out['Z0938'] = {'A396825_bfile_max_n': bmax, 'A396825_terms': len(A396825),
                'zero_both(R&Uv)_le1369': J1, 'in_A396825': [x for x in J1 if x in A396825],
                'Uv_zero_le1369_count': len(J2), 'Uv_zero_not_in_A396825': [x for x in J2 if x not in A396825 and x <= bmax][:30],
                'R_zero_le1369_count': len(J3), 'R_zero_not_in_A396825_(<=bmax)': [x for x in J3 if x not in A396825 and x <= bmax][:30]}
# Z0945: containment of ESC-type zero set (R&Uv zeros) in A396825 ∪ {105,672}, up to bmax
Z = [int(x) for x in n[:bmax][(cm[:bmax] == 0) & (vm[:bmax] == 0)]]
out['Z0945'] = {'upto': bmax, 'R&Uv_zeros': len(Z), 'not_in_A396825_or_105_672': [x for x in Z if x not in A396825 and x not in (105, 672)][:30],
                'A396825_members_in_range': len([x for x in A396825 if x <= bmax])}
# Z0944: record prime 8803369 and 8813281
out['Z0944'] = {}
for p in [8803369, 8813281, 1201, 21169, 118801]:
    out['Z0944'][str(p)] = {'p_mod_840': p % 840, 'cm(Cmin)': int(cm[p - 1]), 'vm(Vmin)': int(vm[p - 1]), 'im(I3)': int(im[p - 1]), 'cmi': int(cmi[p - 1])}
# Z1524: empirical union density of Cmin ≤ c (n ≡ 1 mod 4) and count of zero
d = {}
for c in [1, 2, 3, 5, 10, 20, 50]:
    d[c] = float(((cm >= 1) & (cm <= c) & m1).sum() / m1.sum())
out['Z1524_cmin_density_le_c_n1mod4'] = d
out['Z1524_R_zero_density_n1mod4'] = float(((cm == 0) & m1).sum() / m1.sum())
# Z0844 extra: Cmin histogram for primes
json.dump(out, open('data/z52b/pass1/U00/fix_words.json', 'w'), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)[:6000])
