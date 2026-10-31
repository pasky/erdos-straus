"""RESIDUE_HARDNESS §2.3: fold the full-residue factor into the (★) hardness model, M_BM -> M_BM·F_S(p), and test whether
the (★)-failure primes and the hard primes become less surprising.
Inputs: /tmp/rh/mbm_1e6.txt (z38_mbm.c 3 1000000 0: n isprime R M0 MBM MBM8), /tmp/rh/mbm_fail.txt (same, the 5 failures
in (1e6, 1e7]), data/z52c/rh/model_tables.json, U(p) arrays as in z52c_rh_regress.py.
Swap-Poisson model of BM_CORRECTED_COUNT §3.2: R/2 ~ Poi(M/2), P(R = 0) = exp(−M/2).
Usage: uv run --with numpy --with scipy python scripts/z52c_rh_hard.py"""
import numpy as np, json
from scipy.stats import poisson
MT = json.load(open('data/z52c/rh/model_tables.json')); REF = '1e6'
COMP = [(840, 1), (16, 1), (8, -1), (11, 1), (13, 1)]


def lfac(PP, fam):
    PP = np.asarray(PP, dtype=np.int64); L0 = MT[REF]['L']; L = np.log(PP.astype(float)); lf = np.zeros(len(PP))
    for Q, sgn in COMP:
        d = MT[REF][str(Q)]; fac = dict(zip(d['classes'], d[fam]['model']))
        lf += sgn*np.log(1 + (np.array([fac[int(x)] for x in PP % Q]) - 1)*L0/L)
    return lf


A = np.loadtxt('/tmp/rh/mbm_1e6.txt'); A = A[(A[:, 1] == 1) & (A[:, 0] % 4 == 1) & (A[:, 0] > 1000)]
Fl = np.loadtxt('/tmp/rh/mbm_fail.txt', ndmin=2)
P = A[:, 0].astype(np.int64); R = A[:, 2]; M = A[:, 4]; Fraw = np.exp(lfac(P, 'S'))
# M_BM already contains part of the class dependence (the Brauer character χ_{-4uB}(p), through T(p)). To avoid counting it
# twice, divide F_S by the class factor of M_BM itself, computed from M_BM alone (no R data) on p ∈ [2e5, 1e6], same
# components and 1/L rescaling:  F := F_S / F_MBM.
W = (P >= 200000); LW = np.log(np.sqrt(200000*1e6)); lbm = np.zeros(len(P))
for Q, sgn in COMP:
    cl = MT[REF][str(Q)]['classes']; mm = M[W].mean()
    fac = {c: M[W & (P % Q == c)].mean()/mm for c in cl}
    lbm += sgn*np.log(1 + (np.array([fac[int(x)] for x in P % Q]) - 1)*LW/np.log(P.astype(float)))
FBM = np.exp(lbm); F = Fraw/FBM; MF = M*F
out_pre = dict(mean_log_Fraw=float(np.log(Fraw).mean()), mean_log_FBM=float(lbm.mean()), corr_logFraw_logFBM=float(np.corrcoef(np.log(Fraw), lbm)[0, 1]))
out = {'F_construction': out_pre}
for nm_, Mx_ in [('M_BM*F_S_raw(double-counts BM)', M*Fraw)]:
    out['expected_zeros_' + nm_] = float(np.exp(-Mx_/2).sum())
# global fit quality
def ll(Mx): return float(poisson.logpmf(R/2, Mx/2).sum())
beta = np.linalg.lstsq(np.column_stack([np.ones(len(P)), np.log(M), np.log(F)]), np.log(R + 1), rcond=None)[0]
out['n_primes'] = int(len(P))
out['loglik_swapPoisson'] = {'M_BM': ll(M), 'M_BM*F': ll(MF)}
out['corr_logR1'] = {'M_BM': float(np.corrcoef(np.log(R + 1), np.log(M))[0, 1]), 'M_BM*F': float(np.corrcoef(np.log(R + 1), np.log(MF))[0, 1])}
out['free_fit_logR1_on_logM_logF'] = [round(float(b), 3) for b in beta]
for name, Mx in [('M_BM', M), ('M_BM*F', MF)]:
    z = (R - Mx)/np.sqrt(2*Mx)
    out['z_' + name] = dict(sd=float(z.std()), min=float(z.min()), argmin=int(P[z.argmin()]), frac_R_lt_half=float((R < Mx/2).mean()),
                            expected_zeros=float(np.exp(-Mx/2).sum()), observed_zeros=int((R == 0).sum()))
# the 14 (★) failures p ≡ 1 (4) ≤ 1e7
fails = [(int(p), m) for p, m in zip(P[R == 0], M[R == 0])] + [(int(r[0]), r[4]) for r in Fl]
fp = np.array([f[0] for f in fails]); fm = np.array([f[1] for f in fails])
# F at the failures: F_S/F_MBM; for the 5 failures > 1e6 use the same class tables
def F_at(pp):
    pp = np.asarray(pp, dtype=np.int64); l = lfac(pp, 'S'); L = np.log(pp.astype(float))
    for Q, sgn in COMP:
        cl = MT[REF][str(Q)]['classes']; mm = M[W].mean(); fac = {c: M[W & (P % Q == c)].mean()/mm for c in cl}
        l -= sgn*np.log(1 + (np.array([fac[int(x)] for x in pp % Q]) - 1)*LW/L)
    return np.exp(l)
ff = F_at(fp)
out['failures'] = [dict(p=int(p), M_BM=round(float(m), 2), F_S=round(float(f), 3), M_BM_F=round(float(m*f), 2),
                        mlog10P0_before=round(float(m/2/np.log(10)), 2), mlog10P0_after=round(float(m*f/2/np.log(10)), 2),
                        p_mod_840=int(p % 840), p_mod_16=int(p % 16)) for p, m, f in zip(fp, fm, ff)]
# quantile of F among the primes of (1e3, 1e6], for the failures in that range (R-review fix: was ff[:9], which picked
# 1134241, 1724209 instead of 409, 577; those two are < 1e3 and outside the sample, so the 7 failures in (1e3, 1e6] are used)
sel_q = (fp > 1000) & (fp <= 10**6)
out['failures_F_quantile'] = {int(p): round(float((F < f).mean()), 4) for p, f in zip(fp[sel_q], ff[sel_q])}
out['failures_total_log10_surprise'] = {'before': float(np.sum(fm)/2/np.log(10)), 'after': float(np.sum(fm*ff)/2/np.log(10))}
# where do the expected zeros sit? share of sum exp(-MF/2) carried by the lowest-F decile of primes, vs share of primes
dec = F <= np.quantile(F, 0.1)
out['expected_zero_share_lowest_F_decile'] = {'M_BM*F': float(np.exp(-MF[dec]/2).sum()/np.exp(-MF/2).sum()),
                                              'M_BM': float(np.exp(-M[dec]/2).sum()/np.exp(-M/2).sum()), 'observed_zeros_in_decile': int((R[dec] == 0).sum())}
# the 5% of primes with the lowest R/M_BM: their mean log F (hard primes sit in low-F classes?)
q = R/M; low = q <= np.quantile(q, 0.01)
out['lowest1pct_R_over_M'] = dict(n=int(low.sum()), mean_logF=float(np.log(F[low]).mean()), mean_logF_all=float(np.log(F).mean()),
                                   ratio_after_median=float(np.median((R/MF)[low])), ratio_before_median=float(np.median(q[low])))
# U-hard primes: Type-A failures and lcm+1 primes (U from the tuple arrays)
T = '/tmp/rh/'
TI = np.fromfile(T + 't2e5full_TI.f32', np.float32); TII = np.fromfile(T + 't2e5full_TII.f32', np.float32)
named = {}
for p in [193, 409, 577, 2521, 5569, 9601, 23929, 66529, 83449]:
    named[p] = dict(U=float((TI[p - 101] + TII[p - 101])/2) if p <= 200000 else None, F_U=round(float(np.exp(lfac([p], 'U'))[0]), 3),
                    F_S=round(float(np.exp(lfac([p], 'S'))[0]), 3), p_mod_840=p % 840, p_mod_16=p % 16)
out['named_hard_primes'] = named
print(json.dumps(out, indent=1))
json.dump(out, open('data/z52c/rh/hard.json', 'w'), indent=1)
# expected vs observed zeros by range (calibration of the zero law under the two main terms)
byr = {}
for a, b in [(1e3, 1e4), (1e4, 1e5), (1e5, 3e5), (3e5, 1e6)]:
    s = (P >= a) & (P < b)
    byr[f'{a:.0e}-{b:.0e}'] = dict(n=int(s.sum()), obs=int((R[s] == 0).sum()), exp_MBM=round(float(np.exp(-M[s]/2).sum()), 2),
                                   exp_MBMF=round(float(np.exp(-MF[s]/2).sum()), 2), sd_z_MBM=round(float(((R[s]-M[s])/np.sqrt(2*M[s])).std()), 3),
                                   sd_z_MBMF=round(float(((R[s]-MF[s])/np.sqrt(2*MF[s])).std()), 3))
print('zeros by range', json.dumps(byr))
out['zeros_by_range'] = byr
json.dump(out, open('data/z52c/rh/hard.json', 'w'), indent=1)
