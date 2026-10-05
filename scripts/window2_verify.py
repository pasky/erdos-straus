#!/usr/bin/env python3
"""POINTWISE_WINDOW2 §3.5 -- independent check of an LP fake (dump of window2_lp.py --dump=F).

Recomputes, without reusing window2_lp code: the bins g, w from (eps,K); the
true weights mu(C) from the §3.3 formula; the parity of every configuration;
and every visible correlation rho(S) (S=(s3,s7), sum <= theta) for mu and for
the fake nu by brute force over the configurations.  Reports min nu/tau,
nu(empty)/tau and the max relative correlation residual.
Usage: window2_verify.py DUMP.json
"""
import sys, json, itertools
from math import comb, factorial, log, exp, sqrt
d = json.load(open(sys.argv[1]))
eps, K, theta = d["eps"], d["K"], d["theta"]
e = [exp(log(eps) * (1 - i / K)) for i in range(K + 1)]
g = [sqrt(e[i] * e[i + 1]) * (1 + 1e-7 * (i + 1)) for i in range(K)]
w = [0.5 * log(e[i + 1] / e[i]) for i in range(K)]
assert max(abs(a - b) for a, b in zip(g, d["g"])) < 1e-12
def muw(m):
    s = sum(a * b for a, b in zip(m, g)); assert s < 1 and sum(m) % 2 == 0
    v = max(1 - s, 1e-3) ** -0.5
    for k in range(K): v *= w[k] ** m[k] / factorial(m[k])
    return v
C = [tuple(map(tuple, c)) for c in d["configs"]]
nu = d["nu"]
mu = [muw(a) * muw(b) for a, b in C]
assert max(abs(x - y) / y for x, y in zip(mu, d["mu"])) < 1e-9
j0 = C.index((tuple([0] * K), tuple([0] * K))); tau = mu[j0]
rho_mu, rho_nu = {}, {}
for (a, b), x, y in zip(C, mu, nu):
    subs_a = [(s, sum(si * gi for si, gi in zip(s, g))) for s in itertools.product(*[range(m + 1) for m in a])]
    subs_b = [(s, sum(si * gi for si, gi in zip(s, g))) for s in itertools.product(*[range(m + 1) for m in b])]
    for sa, ta in subs_a:
        ea = 1
        for m, s in zip(a, sa): ea *= comb(m, s)
        for sb, tb in subs_b:
            if ta + tb <= theta + 1e-12:
                eb = 1
                for m, s in zip(b, sb): eb *= comb(m, s)
                key = (sa, sb)
                rho_mu[key] = rho_mu.get(key, 0) + ea * eb * x
                rho_nu[key] = rho_nu.get(key, 0) + ea * eb * y
res = max(abs(rho_nu[k] - rho_mu[k]) / rho_mu[k] for k in rho_mu)
print(json.dumps({"n_visible": len(rho_mu), "nu_empty_over_tau": nu[j0] / tau,
                  "min_nu_over_tau": min(nu) / tau, "max_rel_residual": res,
                  "removed_mass_over_tau": sum(max(0, m - n) for m, n in zip(mu, nu)) / tau}, indent=1))
