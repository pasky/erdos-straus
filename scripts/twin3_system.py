"""EXCEPTIONAL_TWIN3 Cor 3.3 / (2.1) on the real class system (toy scale, k=1).
For prime j and primes m with jm <= X, jm = 3 (4), A=(jm+1)/4, vertex residues
a = -4D mod j over all D | A^2. Splits partners into small (m <= j^C0) and large.
Reports: total mass sum_a V, second moment sum_a V^2, max_a V, random (sum V)^2/j,
for small and large parts, and the (2.1) proxy  2*mass_small + 2*sum V_large^2
against sum_a min(V,1)^2 (all quantities are j*nu-normalised, i.e. without the 1/j).
Usage: uv run --with numpy python scripts/twin3_system.py X C0 j1 j2 ..."""
import sys
import numpy as np

def spf_sieve(n):
    s = np.zeros(n + 1, dtype=np.int32)
    for p in range(2, int(n ** 0.5) + 1):
        if s[p] == 0:
            blk = s[p * p::p]
            blk[blk == 0] = p
    idx = np.nonzero(s == 0)[0]
    s[idx] = idx
    return s

def factor(n, spf):
    f = {}
    while n > 1:
        p = int(spf[n]); e = 0
        while n % p == 0:
            n //= p; e += 1
        f[p] = e
    return f

def divisors_sq_mod(f, j):
    # residues mod j of all divisors of A^2 (with multiplicity)
    res = [1]
    for p, e in f.items():
        pm = p % j
        new = []
        pw = 1
        for _ in range(2 * e + 1):
            new.extend((r * pw) % j for r in res)
            pw = pw * pm % j
        res = new
    return res

def main():
    X = int(float(sys.argv[1])); C0 = float(sys.argv[2]); js = list(map(int, sys.argv[3:]))
    spf = spf_sieve(X // 4 + 2)
    primes = np.nonzero(spf == np.arange(len(spf)))[0]
    primes = primes[primes > 2]
    print(f"X={X:.0e} C0={C0}; columns per part: mass | sumV^2 | maxV | rand")
    print("j | small: mass, V2, max, rand | large: mass, V2, max, rand | sum min(V,1)^2 | (2.1) proxy")
    for j in js:
        Vs = np.zeros(j); Vl = np.zeros(j)
        for m in primes:
            m = int(m)
            if m == j or j * m > X: 
                if j * m > X: break
                continue
            if (j * m) % 4 != 3: continue
            A = (j * m + 1) // 4
            res = divisors_sq_mod(factor(A, spf), j)
            a = (-4 * np.array(res, dtype=np.int64)) % j
            tgt = Vs if m <= j ** C0 else Vl
            tgt += np.bincount(a, minlength=j) / m
        V = Vs + Vl
        def st(W): return f"{W.sum():.2f}, {np.dot(W, W):.3f}, {W.max():.3f}, {W.sum()**2/j:.3f}"
        print(f"{j} | {st(Vs)} | {st(Vl)} | {np.sum(np.minimum(V,1)**2):.3f} | {2*Vs.sum()+2*np.dot(Vl,Vl):.3f}")

main()
