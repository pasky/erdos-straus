"""z50 lsmass: the prime-local U family, sieve bounds vs true counts.

Fibre n == 1 (mod 8) (U holds for every n == 5 mod 8, n > 5, via the class -3 mod 8).
Prime-local U classes at an odd prime l: n == -u (mod l), u | l+1, and the word (t,u,v),
t=(l+1)/u, v=(n+u)/l has an endpoint in S = 4Z u (8Z+7). In the fibre n == 1 mod 8, v mod 8
is (1+u)*l^{-1} mod 8, so the class is active iff u in S or (1+u)l^{-1} mod 8 in S.
omega(l) = number of distinct active residues.

Outputs (data/z50_lsmass/primelocal.json):
  * profile: mass(y)=sum omega/l, Lam(y)=sum omega log l / l, fitted a = mass/log y;
  * L(Q) (Montgomery) for Q up to QMAX, vs saddle 2 sqrt(a log Q) and Rankin bound;
  * true sifted counts S(N,z) of n<=N, n==1 mod 8, avoiding all prime-local classes l<=z,
    vs the Haar prediction (N/8) prod(1-omega/l), vs Montgomery's bound, vs true E_U count.
"""
import math, json, sys
import numpy as np

def spf_sieve(n):
    spf = np.zeros(n + 1, dtype=np.int32)
    spf[1] = 1
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == 0:
            spf[i] = i
            s = spf[i*i::i]
            mask = s == 0
            s[mask] = i
            spf[i*i::i] = s
    rest = np.nonzero(spf == 0)[0]
    spf[rest] = rest
    return spf

def factor(n, spf):
    f = {}
    while n > 1:
        p = int(spf[n])
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        f[p] = e
    return f

def divs_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return ds

def inS(x):
    return x % 4 == 0 or x % 8 == 7

def forbidden(l, spf):
    linv8 = pow(l, -1, 8)
    res = set()
    for u in divs_from(factor(l + 1, spf)):
        v8 = ((1 + u) * linv8) % 8
        if inS(u) or inS(v8 if v8 else 8):
            res.add((-u) % l)
    return res

def main(N, QMAX):
    LIM = max(QMAX, int(math.isqrt(N)) + 2) + 2
    spf = spf_sieve(LIM)
    primes = [p for p in range(3, LIM - 1) if spf[p] == p]
    om = {}
    for l in primes:
        om[l] = len(forbidden(l, spf))
    # profile
    prof = []
    mass = lam = 0.0
    marks = set(int(10**(k/2)) for k in range(2, 30))
    for l in primes:
        mass += om[l] / l
        lam += om[l] * math.log(l) / l
        if l >= 10 and any(l <= m < l + 2*l**0.5+10 for m in []):
            pass
    ys = [10**k for k in range(1, 8) if 10**k <= LIM]
    for y in ys:
        ms = sum(om[l]/l for l in primes if l <= y)
        ls = sum(om[l]*math.log(l)/l for l in primes if l <= y)
        prof.append({"y": y, "mass": ms, "a_fit": ms/math.log(y), "Lam": ls, "Lam_div_log2": ls/math.log(y)**2,
                     "mean_omega_over_logl": sum(om[l]/math.log(l) for l in primes if l <= y)/sum(1 for l in primes if l <= y)})
    # Montgomery L(Q): h multiplicative on squarefree odd q
    Q = QMAX
    h = np.ones(Q + 1)
    h[0] = 0
    for l in primes:
        if l > Q:
            break
        g = om[l] / (l - om[l])
        h[l::l] *= g
        if l * l <= Q:
            h[l*l::l*l] = 0
    h[2::2] = 0  # odd moduli only (fibre is mod 8 already)
    h[1] = 1
    cum = np.cumsum(h)
    Ls = []
    a_hat = prof[-1]["a_fit"]
    for k in range(2, 30):
        q = int(10**(k/4))
        if q > Q:
            break
        LQ = cum[q]
        # Rankin bound inf_sigma Q^sigma prod(1+g l^-sigma)
        best = None
        for sig in np.linspace(0.02, 1.0, 99):
            s = sig * math.log(q) + sum(math.log1p(om[l]/(l-om[l]) * l**(-sig)) for l in primes if l <= q)
            best = s if best is None or s < best else best
        Ls.append({"Q": q, "logL": math.log(LQ), "two_sqrt_a_logQ": 2*math.sqrt(a_hat*math.log(q)),
                   "rankin_log_upper": best, "full_euler_log": sum(-math.log1p(-om[l]/l) for l in primes if l <= q)})
    # true sifted counts in fibre n = 8m+1
    M = N // 8
    alive = np.ones(M + 1, dtype=bool)
    alive[0] = False  # n=1 excluded
    n_of = lambda m: 8*m + 1
    zs = sorted(set([10, 30, 100, 300, 1000, 3000, 10000, int(math.isqrt(N))]))
    zs = [z for z in zs if z <= math.isqrt(N)]
    counts = []
    haar = M
    zi = 0
    inv8cache = {}
    for l in primes:
        if l > zs[-1]:
            break
        # classes n == r mod l  <->  8m+1 == r mod l  <-> m == (r-1)*8^{-1} mod l
        i8 = pow(8, -1, l)
        F = forbidden(l, spf)
        for r in F:
            m0 = ((r - 1) * i8) % l
            # only n >= 2l - u needed for forcedness; ignore tiny n effect (n < 2l)
            alive[m0::l] = False
        haar *= (1 - len(F)/l)
        while zi < len(zs) and (l >= zs[zi] or l == primes[-1]):
            # record at first prime >= z: approximate by recording after primes <= z
            zi += 1
        # record when next prime exceeds a checkpoint
        nxt = None
    # recompute counts per z by re-running (simple and clear)
    for z in zs:
        alive = np.ones(M + 1, dtype=bool); alive[0] = False
        hz = M * 1.0
        for l in primes:
            if l > z:
                break
            i8 = pow(8, -1, l)
            F = forbidden(l, spf)
            for r in F:
                alive[((r - 1) * i8) % l::l] = False
            hz *= (1 - len(F)/l)
        cnt = int(alive.sum())
        # Montgomery bound with Q <= sqrt(M) and moduli built from primes <= z
        Qm = int(math.isqrt(M))
        hh = np.ones(Qm + 1); hh[0] = 0
        rem = np.arange(Qm + 1, dtype=np.int64)
        for l in primes:
            if l > min(z, Qm):
                break
            g = om[l]/(l-om[l])
            hh[l::l] *= g
            rem[l::l] //= l
            if l*l <= Qm:
                hh[l*l::l*l] = 0
        hh[rem != 1] = 0  # keep only odd squarefree z-smooth moduli
        hh[2::2] = 0; hh[1] = 1
        LQm = float(hh.sum())
        mont = (M + Qm*Qm) / LQm
        counts.append({"z": z, "true_sifted": cnt, "haar": hz, "montgomery": mont,
                       "log_saving_true": math.log(M/cnt), "log_saving_haar": math.log(M/hz),
                       "log_saving_mont": math.log(M/mont) if mont < M else 0.0})
    # true U-exceptional count in fibre (odd squares == 1 mod 8 plus the six)
    six = [105, 2961, 3985, 25305, 111969, 978145]
    sq = sum(1 for m in range(1, math.isqrt(N) + 1, 2) if m*m > 1)
    EU = sq + sum(1 for s in six if s <= N)
    out = {"N": N, "QMAX": QMAX, "profile": prof, "L": Ls, "counts": counts, "E_U_true": EU}
    json.dump(out, open("data/z50_lsmass/primelocal.json", "w"), indent=1)
    for r in prof: print(r)
    for r in Ls: print(r)
    for r in counts: print(r)
    print("E_U true (fibre 1 mod 8, n<=N):", EU)

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
