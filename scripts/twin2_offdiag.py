"""EXCEPTIONAL_TWIN2 §5 (H_O) numerics: the off-diagonal / deadly-value term S_j
on the real Case-B system restricted to two-large-prime moduli M = k*j*m.

For a prime j, partners m (primes > w, m != j), cofactors k (odd, w-smooth, k <= K),
M = k j m <= X, M = 3 mod 4, classes -4D mod M with D | A^2, A = (M+1)/4.
Fibre: a random integer c; class active iff c = -4D (mod k).
deg(a) = sum over active classes with -4D = a (mod j) of 1/m.
Reports j*w_j, j*q_j, j*S_j (S_j = (1/j) sum_a min(deg,1)^2), #hubs (deg>=1),
and the smallest hub D values.   usage: X w K seed j1 j2 ...
"""
import sys, random
import numpy as np

def spf_sieve(n):
    spf = np.zeros(n + 1, dtype=np.int32)
    spf[1] = 1
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == 0:
            spf[p] = p
            idx = np.arange(p * p, n + 1, p)
            sub = spf[idx]
            spf[idx] = np.where(sub == 0, p, sub)
    z = np.nonzero(spf == 0)[0]
    spf[z] = z
    return spf

def factor(n, spf):
    f = {}
    while n > 1:
        p = int(spf[n]); f[p] = f.get(p, 0) + 1; n //= p
    return f

def divisors_sq(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** i for d in ds for i in range(2 * e + 1)]
    return ds

def canon(D, A):
    # residue of class -4D at any j | M is -(4D)(4A)^{-t}; pick least-height representative
    from math import gcd
    cands = []
    for num, den in ((4 * D, 1), (D, A), (D, 4 * A * A)):
        g = gcd(num, den); cands.append((max(num // g, den // g), num // g, den // g))
    return min(cands)[1:]

def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for p in range(2, int(n ** .5) + 1):
        if s[p]: s[p * p::p] = False
    return np.nonzero(s)[0]

def main():
    X, w, K, seed = int(float(sys.argv[1])), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    js = [int(x) for x in sys.argv[5:]]
    spf = spf_sieve(X // 4 + 2)
    P = primes_upto(X // (min(js) * 1) + 1)
    smallp = [p for p in primes_upto(w) if p > 2]
    ks = [k for k in range(1, K + 1, 2) if all(p <= w for p in factor(k, spf))] if K >= 1 else [1]
    rng = random.Random(seed)
    c = rng.randrange(10 ** 30)
    print(f"# X={X:.0e} w={w} K={K} ks={ks} seed={seed}")
    print("# j  j*w_j  j*q_j  j*S_j  hubs  minHubD")
    for j in js:
        deg = {}
        hubD = {}
        ncls = 0
        diag = 0.0
        null = {}
        lab = {}
        rr = random.Random(j)
        for k in ks:
            for m in P:
                m = int(m)
                if m <= w or m == j: continue
                M = k * j * m
                if M > X: break
                if M % 4 != 3: continue
                A = (M + 1) // 4
                for D in divisors_sq(factor(A, spf)):
                    ncls += 1
                    if (c + 4 * D) % k: continue
                    a = (-4 * D) % j
                    diag += 1.0 / m ** 2
                    key = canon(D, A)
                    lab[key] = lab.get(key, 0.0) + 1.0 / m
                    b = rr.randrange(j)
                    null[b] = null.get(b, 0.0) + 1.0 / m
                    deg[a] = deg.get(a, 0.0) + 1.0 / m
                    if D < hubD.get(a, 10 ** 30): hubD[a] = D
        v = np.array(list(deg.values())) if deg else np.zeros(1)
        hubs = sorted(hubD[a] for a in deg if deg[a] >= 1)
        nv = np.array(list(null.values())) if null else np.zeros(1)
        same = sum(x * x for x in lab.values())
        cross = float((v ** 2).sum()) - same
        tot = float(v.sum())
        H = 30
        sh = {(-u * pow(v, -1, j)) % j for u in range(1, H + 1) for v in range(1, H + 1)}
        Shub = sum(min(deg[a], 1) ** 2 for a in deg if a in sh)
        Srest = sum(min(deg[a], 1) ** 2 for a in deg if a not in sh)
        nrest = sum(min(null[b], 1) ** 2 for b in null if b not in sh)
        print(f"{j} classes={ncls} jw={v.sum():.3f} jq={(v**2).sum():.3f} jS={(np.minimum(v,1)**2).sum():.3f} "
              f"same={same:.3f} cross={cross:.3f} cross_rand={tot*tot/j:.3f} diag={diag:.3f} null_jS={(np.minimum(nv,1)**2).sum():.3f} | height<=30: jS_hub={Shub:.3f} jS_rest={Srest:.3f} null_rest={nrest:.3f} hubs={len(hubs)} {hubs[:6]}")

if __name__ == "__main__":
    main()
