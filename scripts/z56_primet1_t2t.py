"""z56 PRIMET1 Amendment 3, test T2T: residual correlation of the two disjoint ticket families
A1 (smallest coordinate C; tickets 4Cp+1) and A2 (smallest coordinate u; tickets p+u), conditionally on the local design 𝓛.
Usage: python z56_primet1_t2t.py RONE_OUT.txt OUTPREFIX [--sieve SIEVE.npy] [--label S3]
RONE_OUT: lines "p R A1 A2 A3" from z56_primet1_rone. Fit half: splitmix64(p) mod 32 < 16; evaluation half: the rest.
Reports rho-hat (Pearson residual correlation), Fisher-z CI, sigma_H^2 estimate = mean[(y1-mu1)(y2-mu2)]/mean[mu1 mu2]
with a normal-theory 99 % upper bound, and a planted-H positive control.
"""
import sys, math, argparse
import numpy as np
from scipy import stats
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z56_primet1_local import Design, fit
from z56_primet1_split import splitmix64

def run(p, y1, y2, des, fitm, evm):
    out = {}
    mus = []
    for y in (y1, y2):
        beta, k, phi, _ = fit(p[fitm], y[fitm].astype(float), des, iters=12)
        mu = np.exp(des.build(p[evm]) @ beta); mus.append((mu, phi, k))
    (m1, f1, k1), (m2, f2, k2) = mus
    e1 = y1[evm] - m1; e2 = y2[evm] - m2
    r1 = e1 / np.sqrt(f1 * m1); r2 = e2 / np.sqrt(f2 * m2)
    n = len(r1); rho = np.corrcoef(r1, r2)[0, 1]; z = math.atanh(rho); se = 1 / math.sqrt(n - 3)
    prod = e1 * e2; s2 = prod.mean() / (m1 * m2).mean(); s2se = prod.std() / math.sqrt(n) / (m1 * m2).mean()
    out.update(n=n, rho=rho, lo99=math.tanh(z - 2.576 * se), hi99=math.tanh(z + 2.576 * se),
               p_gt_0005=stats.norm.sf((z - math.atanh(0.005)) / se), sigma2=s2, sigma2_hi99=s2 + 2.326 * s2se,
               mean1=float(y1[evm].mean()), mean2=float(y2[evm].mean()), phi1=f1, phi2=f2)
    return out, (m1, m2, k1, k2, f1, f2)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('rone'); ap.add_argument('out'); ap.add_argument('--sieve')
    ap.add_argument('--label', default='S3')
    a = ap.parse_args()
    d = np.loadtxt(a.rone, dtype=np.int64)
    p = d[:, 0].astype(np.uint64); R = d[:, 1]; A1 = d[:, 2]; A2 = d[:, 3]; A3 = d[:, 4]
    assert np.all(R == A1 + A2 + A3)
    if a.sieve:
        s = np.load(a.sieve); sd = dict(zip(s['p'].tolist(), s['r'].tolist()))
        bad = sum(1 for x, rr in zip(p.tolist(), R.tolist()) if sd[x] != rr); print('sieve mismatches', bad)
    h = splitmix64(p) % np.uint64(32); fitm = h < 16; evm = ~fitm
    des = Design(1000)
    res, (m1, m2, k1, k2, f1, f2) = run(p, A1, A2, des, fitm, evm)
    lines = [f'# T2T label={a.label} n_total={len(p)} n_eval={res["n"]}',
             '\t'.join(f'{k}={v:.6g}' if isinstance(v, float) else f'{k}={v}' for k, v in res.items())]
    # planted positive control: Gamma-Poisson draws with the fitted means and dispersions, common multiplier e^H
    rng = np.random.default_rng(5603)
    for sig in [0.0, 0.02, 0.05, 0.1]:
        est = []
        for rep in range(5):
            H = rng.normal(0, sig, len(m1)) if sig > 0 else np.zeros(len(m1))
            def draw(m, f):
                # quasi-Poisson-like: NB with variance f*m approx via Gamma-Poisson with shape m/(f-1)
                if f <= 1.0001: return rng.poisson(m)
                shape = m / (f - 1); return rng.poisson(rng.gamma(shape, (m * np.exp(H)) / shape))
            z1 = draw(m1, f1); z2 = draw(m2, f2)
            e1 = z1 - m1; e2 = z2 - m2
            est.append(((e1 * e2).mean() / (m1 * m2).mean(), np.corrcoef(e1 / np.sqrt(m1), e2 / np.sqrt(m2))[0, 1]))
        est = np.array(est)
        lines.append(f'planted sigma_H={sig}: sigma2_hat mean={est[:,0].mean():.5f} (true {sig**2:.5f}), rho mean={est[:,1].mean():.4f}')
    open(a.out + '_t2t.txt', 'w').write('\n'.join(lines) + '\n'); print('\n'.join(lines))
