"""z56 PRIMET1 PC2 (Z56_PRIMET1.md §3.6): planted-signal power simulation on C.
Y* ~ NB(mu*exp(beta*Z), k) with Z a balanced random binary; r*, hard* (mid-PIT < 0.01) recomputed under the unperturbed mu;
detection = P-cont F-test (resp. P-tail LR test) p < 0.05/32 (the strictest Holm step). Also a 'hidden subclass' variant:
a fraction pi of primes gets mu*rho (rho < 1), Z = indicator of the subclass.
Usage: uv run --with numpy --with scipy python z56_primet1_pc2.py PRED_C.npy OUT.tsv [nsim]"""
import sys, math
import numpy as np
from scipy import stats
from scipy.special import expit

K = 58.49571586614124
def sim(mu, mult, rng):
    lam = rng.gamma(K, (mu * mult) / K)   # NB(mu*mult, K) as Gamma-Poisson
    return rng.poisson(lam).astype(float)

def pit(y, mu):
    pr = K / (K + mu)
    return stats.nbinom.cdf(y - 1, K, pr) + 0.5 * stats.nbinom.pmf(y, K, pr)

def tests(y, mu, Z):
    r = (y - mu) / np.sqrt(mu + mu * mu / K)
    zc = Z - Z.mean(); b = (zc @ r) / (zc @ zc); e = r - r.mean() - b * zc
    t = b / math.sqrt((e @ e) / (len(r) - 2) / (zc @ zc)); pc = 2 * stats.norm.sf(abs(t))
    h = pit(y, mu) < 0.01
    a = np.array([[np.sum(h & (Z == 1)), np.sum(~h & (Z == 1))], [np.sum(h & (Z == 0)), np.sum(~h & (Z == 0))]], float)
    a = a + 0.5  # Haldane correction (zero cells occur for strongly depleted small subclasses)
    lor = math.log(a[0, 0] * a[1, 1] / (a[0, 1] * a[1, 0])); se = math.sqrt((1 / a).sum()); pt = 2 * stats.norm.sf(abs(lor / se))
    return pc, pt, math.exp(lor)

if __name__ == '__main__':
    pred = np.load(sys.argv[1]); mu = pred['mu']; n = len(mu)
    nsim = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    rng = np.random.default_rng(5602); alpha = 0.05 / 32
    out = open(sys.argv[2], 'w'); out.write('design\tparam\tpower_cont\tpower_tail\tmean_tail_OR\n')
    for beta in [0.0, 0.001, 0.002, 0.003, 0.005, 0.01, 0.02, 0.05]:
        dc = dt = 0; ors = []
        for s in range(nsim):
            Z = (rng.random(n) < 0.5).astype(float)
            y = sim(mu, np.exp(beta * Z), rng); pc, pt, o = tests(y, mu, Z)
            dc += pc < alpha; dt += pt < alpha; ors.append(o)
        out.write(f'balanced_binary\tbeta={beta}\t{dc/nsim:.2f}\t{dt/nsim:.2f}\t{np.mean(ors):.3f}\n'); out.flush()
    for pi, rho in [(0.01, 0.5), (0.001, 0.5), (0.001, 0.25), (0.0001, 0.25), (0.0001, 0.1)]:
        dc = dt = 0; ors = []
        for s in range(nsim):
            Z = (rng.random(n) < pi).astype(float)
            y = sim(mu, np.where(Z > 0, rho, 1.0), rng); pc, pt, o = tests(y, mu, Z)
            dc += pc < alpha; dt += pt < alpha; ors.append(o)
        out.write(f'hidden_subclass\tpi={pi},rho={rho}\t{dc/nsim:.2f}\t{dt/nsim:.2f}\t{np.mean(ors):.3f}\n'); out.flush()
    out.close(); print(open(sys.argv[2]).read())
