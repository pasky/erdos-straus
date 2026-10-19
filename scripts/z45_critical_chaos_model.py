"""Finite Walsh/CRT-Cox diagnostics; not an ES simulation or proof.
Run: OPENBLAS_NUM_THREADS=1 uv run python scripts/z45_critical_chaos_model.py
Memory: O(max height), no sample-by-integer Cartesian arrays. All sign states
(2048) are enumerated by a Walsh transform; no Monte Carlo rare-event error.
"""
import json
import math
from pathlib import Path
import numpy as np

OUT = Path('data/z45_critical_chaos')
Q = 840
SMALL = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
HEIGHTS = [100, 1000, 10000, 100000, 1000000]


def sieve(n):
    phi = list(range(n + 1))
    spf = [0] * (n + 1)
    sf = [1] * (n + 1)
    mask = [-1] * (n + 1)
    mask[1] = 0
    bits = {p: 1 << j for j, p in enumerate(SMALL)}
    for p in range(2, n + 1):
        if not spf[p]:
            for j in range(p, n + 1, p):
                if not spf[j]:
                    spf[j] = p
                phi[j] -= phi[j] // p
    for j in range(2, n + 1):
        p = spf[j]
        m = j // p
        sf[j] = sf[m] // p if sf[m] % p == 0 else sf[m] * p
        if sf[j] == 1:
            mask[j] = 0
        elif sf[j] < j:
            mask[j] = mask[sf[j]]
        elif p in bits and mask[m] >= 0:
            mask[j] = mask[m] ^ bits[p]
    return phi, sf, mask


def walsh(a):
    a = np.array(a, dtype=float)
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2*h):
            x, y = a[j:j+h].copy(), a[j+h:j+2*h].copy()
            a[j:j+h], a[j+h:j+2*h] = x+y, x-y
        h *= 2
    return a


def model(k, height, phi, sf, mask):
    # Unordered coprime pairs (u,v). The diagonal only occurs at (1,1).
    local = {}
    local_logno = {}
    coeff = {}
    principal = 0.0
    pairs = 0
    u = 1
    while k*u*u-2*u <= height:
        vmax = (height+u)//(k*u-1)
        for v in range(u, vmax+1):
            if math.gcd(u, v) != 1 or math.gcd(u+v, k) != 1:
                continue
            q, a = k*u*v, -u-v
            w = 1.0/phi[q]
            principal += w
            pairs += 1
            g = math.gcd(q, Q)
            key = (g, a % g)
            h = w*phi[g]
            local[key] = local.get(key, 0.0) + h
            logno = math.log1p(-h) if h < 1-1e-14 else -math.inf
            local_logno[key] = local_logno.get(key, 0.0) + logno
            if k in (4, 8):
                s = sf[u*v]
                coeff[s] = coeff.get(s, 0.0) + w
        u += 1
    cells = [a for a in range(Q) if math.gcd(a,Q) == 1]
    lambdas = [sum(w for (g,r),w in local.items() if a%g == r) for a in cells]
    zero = float(np.mean(np.exp(-np.array(lambdas))))
    bernoulli = [math.exp(sum(w for (g,r),w in local_logno.items() if a%g == r)) for a in cells]
    hard_bernoulli = [x for a,x in zip(cells,bernoulli) if a in (1,121,169,289,361,529)]
    hard = [x for a,x in zip(cells,lambdas) if a in (1,121,169,289,361,529)]
    result = dict(k=k, height=height, log_height=math.log(height), pairs=pairs,
                  principal_unordered=principal, crt_zero=zero,
                  crt_hard_zero=float(np.mean(np.exp(-np.array(hard)))),
                  crt_lambda_min=min(lambdas), crt_lambda_max=max(lambdas),
                  crt_bernoulli_zero=float(np.mean(bernoulli)),
                  crt_bernoulli_hard_zero=float(np.mean(hard_bernoulli)),
                  expected_zero_per_log_height=height/math.log(height)*float(np.mean(bernoulli)))
    if math.gcd(height,Q) == 1:
        result['crt_quenched_zero'] = math.exp(-lambdas[cells.index(height%Q)])
        result['crt_bernoulli_quenched_zero'] = bernoulli[cells.index(height%Q)]
    if coeff:
        w = [0.0]*(1<<len(SMALL))
        for s,c in coeff.items():
            if mask[s] >= 0:
                w[mask[s]] += c
        intensity = principal-walsh(w)
        assert min(intensity) >= -1e-9
        hard_intensity = intensity[np.arange(len(w)) % 16 == 0]
        result.update(bm_centered_variance=sum(c*c for s,c in coeff.items() if s != 1),
                      bm_square_kernel=coeff.get(1,0.0),
                      bm_projected_zero=float(np.mean(np.exp(-intensity))),
                      bm_projected_hard_zero=float(np.mean(np.exp(-hard_intensity))),
                      bm_projected_intensity_min=float(min(intensity)),
                      bm_projected_intensity_max=float(max(intensity)))
    return result


def main():
    # 4uv <= 4(height+1)/3; 2*height+100 comfortably covers every q.
    phi, sf, mask = sieve(2*max(HEIGHTS)+100)
    rows = []
    for h in HEIGHTS:
        for k in (4,8,15):
            row = model(k,h,phi,sf,mask)
            rows.append(row)
            print(json.dumps(row), flush=True)
    # Exact small Walsh covariance check, not an existing ES census test.
    c = np.array([.2,.3,.7,.11,.13,.17,.19,.23])
    vals = walsh(c)
    assert abs(float(np.var(vals))-float(sum(c[1:]**2))) < 1e-12
    # Compare representative baseline rates at genuinely asymptotic log heights.
    asymptotic = []
    for L in (10,20,40,80):
        for k in (4,8):
            a = (3/(4*math.pi**2))*(1 if k == 4 else .5)
            poisson_logzero = -a*L*L
            stretched_logzero = -.535*((2*a*L*L)**.88)
            asymptotic.append(dict(k=k,L=L,poisson_logzero=poisson_logzero,
                stretched_logzero=stretched_logzero,
                poisson_log_expected_per_log_height=L-math.log(L)+poisson_logzero,
                stretched_log_expected_per_log_height=L-math.log(L)+stretched_logzero))
    # Coarse descriptive quadrature: log-linear interpolation of probabilities,
    # prime density dx/log(x). It is not an exact prime sum or fitted tail law.
    cumulative = []
    for k in (4,8,15):
        rr = [r for r in rows if r['k'] == k]
        for end in (10000,100000,1000000):
            grid = np.linspace(math.log(100),math.log(end),20001)
            logprob = np.interp(grid,[r['log_height'] for r in rr],
                               [math.log(r['crt_bernoulli_zero']) for r in rr])
            value = float(np.trapezoid(np.exp(grid+logprob)/grid,grid))
            cumulative.append(dict(k=k,lower=100,upper=end,approx_expected=value))
    # These benchmarks already have exact arithmetic censuses in the repo.
    # Here we only compute NEW probabilistic predictions, not duplicate tests.
    benchmarks = []
    for k, heights in ((4,(193,409,577,2521,3361,66529)),
                       (8,(11,17,131,241)), (15,(17,131,241,20521))):
        for h in heights:
            r = model(k,h,phi,sf,mask)
            benchmarks.append(r)
            print('benchmark',json.dumps(r),flush=True)
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'model.json').write_text(json.dumps(dict(rows=rows,asymptotic=asymptotic,
                                                benchmarks=benchmarks,cumulative=cumulative),indent=2)+'\n')

if __name__ == '__main__':
    main()
