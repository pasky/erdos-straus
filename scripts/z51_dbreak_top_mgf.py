# z51 dbreak round 4: normalised log-mgf of the centred top-band count X_top (fixed scale, cand_N*.txt), with
# delta-method SEs including both fitted quantities (mean m used for centring and for mu = m).
import math, sys
files = {'1e8': 'data/z51_dbreak/cand_N1e8_s1e5.txt', '1e9': 'data/z51_dbreak/cand_N1e9_s1e5.txt',
         '1e10': 'data/z51_dbreak/cand_N1e10_s1e5.txt', '1e11': 'data/z51_dbreak/cand_N1e11_s3e4.txt'}
for N, f in files.items():
    X = [int(l.split()[2]) for l in open(f)]; n = len(X); m = sum(X) / n
    out = []
    for t in (0.25, 1.0):
        e = [math.exp(-t * (x - m)) for x in X]; E = sum(e) / n; A = math.log(E) / (m * t * t)
        psi = [((a / E - 1 + t * (x - m)) / (m * t * t)) - A * (x - m) / m for a, x in zip(e, X)]
        mp = sum(psi) / n; se = math.sqrt(sum((p - mp) ** 2 for p in psi) / n) / math.sqrt(n)
        out.append(f"t={t}: {A:.4f} +- {se:.4f} (Poisson {(math.exp(-t) - 1 + t) / t ** 2:.4f})")
    print(f"N={N} S={n} mu={m:.3f}  " + "  ".join(out))
