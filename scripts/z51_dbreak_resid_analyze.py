# z51 dbreak round 4: analyse outputs of z51_dbreak_resid.c.
# For each run: mu, model normalised log-mgf, empirical normalised log-mgf of the CENTRED residual R - E R,
# (log E exp(-t(R - m)))/(mu t^2), and the excess over the independent model. Sample files ("n R H Q" per line)
# are pooled per (beta, N); standard errors by the delta method.
import sys, re, glob, math, collections, gzip
opn = lambda p: gzip.open(p, 'rt') if p.endswith('.gz') else open(p)

def model_from_header(lines):
    hdr = [l for l in lines if l.startswith('# N=')][0]
    mu = float(re.search(r'mu=([0-9.]+)', hdr).group(1)); s2 = float(re.search(r'sigma2_model=([0-9.]+)', hdr).group(1))
    model = {}
    for l in lines:
        m = re.match(r'M t=([0-9.]+) model_log_mgf=([-0-9.e]+)', l)
        if m: model[float(m.group(1))] = float(m.group(2))
    return hdr, mu, s2, model

def exact(path):
    lines = open(path).read().splitlines()
    if not any(l.startswith('E ') for l in lines): return None
    hdr, mu, s2, model = model_from_header(lines)
    m1 = float([l for l in lines if l.startswith('MOM 1 ')][0].split()[2])
    m2 = float([l for l in lines if l.startswith('MOM 2 ')][0].split()[2])
    out = []
    for l in lines:
        m = re.match(r'E t=([0-9.]+) log_mgf=([-0-9.e]+)', l)
        if m:
            t = float(m.group(1)); lm = float(m.group(2)); c = lm + t * m1
            out.append((t, c / (mu * t * t), model[t] / (mu * t * t), (c - model[t]) / (mu * t * t)))
    return hdr, mu, s2, m1, m2 - m1 * m1, out

def sample(paths):
    R = []
    for p in paths:
        for l in opn(p):
            if l.startswith('#') or l.startswith('M'): continue
            f = l.split()
            if len(f) == 4: R.append(float(f[1]))
    lines = opn(paths[0]).read().splitlines()
    hdr, mu, s2, model = model_from_header(lines)
    n = len(R); m = sum(R) / n; var = sum((r - m) ** 2 for r in R) / n
    out = []
    for t in sorted(model):
        e = [math.exp(-t * (r - m)) for r in R]; E = sum(e) / n; sd = math.sqrt(sum((x - E) ** 2 for x in e) / n)
        c = math.log(E); se = sd / (E * math.sqrt(n)) / (mu * t * t)
        out.append((t, c / (mu * t * t), model[t] / (mu * t * t), (c - model[t]) / (mu * t * t), se))
    return hdr, mu, s2, m, var, n, out

if __name__ == '__main__':
    d = sys.argv[1] if len(sys.argv) > 1 else 'data/z51_dbreak'
    for p in sorted(glob.glob(d + '/resid_exact_*.txt')):
        r = exact(p)
        if not r: continue
        hdr, mu, s2, m1, var, out = r
        print(f"EXACT {p.split('/')[-1]}: mu={mu:.3f} model_var={s2:.3f} emp_mean={m1:.2e} emp_var={var:.4f} (var/model {var/s2:.4f})")
        for t, a, b, x in out: print(f"   t={t:.2f} centred_norm={a:.5f} model_norm={b:.5f} excess={x:+.5f}")
    groups = collections.defaultdict(list)
    for p in glob.glob(d + '/samp_*.txt.gz') + glob.glob(d + '/samp_*.txt'):
        key = re.search(r'samp_(b[0-9.]+_N[0-9]+)', p).group(1); groups[key].append(p)
    for k in sorted(groups):
        hdr, mu, s2, m, var, n, out = sample(groups[k])
        print(f"SAMPLE {k}: S={n} mu={mu:.3f} model_var={s2:.3f} emp_mean={m:.3e} emp_var={var:.4f} (var/model {var/s2:.4f})")
        for t, a, b, x, se in out: print(f"   t={t:.2f} centred_norm={a:.5f} model_norm={b:.5f} excess={x:+.5f} +- {se:.5f}")
