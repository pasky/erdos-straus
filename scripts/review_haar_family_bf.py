"""R46 from-scratch check of POINTWISE_HAAR Lemmas 2.3-2.4 counting on a scaled family.

Family (scaled): M squarefree, y-rough, M = 3 (4), sqrt(T) <= M <= T; n = D* in [N0, N1]
with 4 N1^2 < sqrt(T) (so (F1) holds), n | A_M. Event (M, D) <-> residues -4D mod q, q | M.
Computes exactly: mu, Delta_a (D = D'), Delta_b (D != D'), max_E sum_{Gamma(E)} P,
max_q w_q, and compares with the proof's explicit intermediate bounds.
Usage: review_haar_family_bf.py T y N0 N1
"""
import sys, math
import numpy as np

T, y, N0, N1 = (int(a) for a in sys.argv[1:5])
L = math.log(T)
assert 4 * N1 * N1 < math.isqrt(T)
# spf sieve
spf = np.zeros(T + 1, dtype=np.int64)
for p in range(2, T + 1):
    if spf[p] == 0:
        spf[p::p][spf[p::p] == 0] = p
def factor(m):
    fs = []
    while m > 1:
        p = int(spf[m]); fs.append(p)
        while m % p == 0:
            m //= p
    return fs
def dstar(D):
    r = 1
    for p in factor(D):
        e = 0; d = D
        while d % p == 0:
            d //= p; e += 1
        r *= p ** ((e + 1) // 2)
    return r
# D's by n
Dby = {}
for D in range(1, N1 * N1 + 1):
    n = dstar(D)
    if N0 <= n <= N1:
        Dby.setdefault(n, []).append(D)
for n in Dby:
    assert len(Dby[n]) == 2 ** len(factor(n)), n
evM, evD, evN, evPhi = [], [], [], []
lo = math.isqrt(T - 1) + 1  # ceil sqrt
for M in range(lo, T + 1):
    if M % 4 != 3:
        continue
    fs = factor(M)
    if fs[0] <= y or math.prod(fs) != M:
        continue
    A = (M + 1) // 4
    ph = math.prod(p - 1 for p in fs)
    for n in Dby:
        if A % n == 0:
            for D in Dby[n]:
                evM.append(M); evD.append(D); evN.append(n); evPhi.append(ph)
evM = np.array(evM); evD = np.array(evD); evN = np.array(evN); evPhi = np.array(evPhi, dtype=float)
NE = len(evM)
P = 1.0 / evPhi
mu = P.sum()
print(f"T={T} y={y} n in [{N0},{N1}]  events={NE}  mu={mu:.6f}")
# buckets by prime
byq = {}
for i in range(NE):
    for q in factor(int(evM[i])):
        byq.setdefault(q, []).append(i)
wq = {q: P[idx].sum() for q, idx in byq.items()}
# Gamma sums: conflicting events share a prime q with different residue
gam_max = 0.0
for i in range(0, NE, max(1, NE // 2000)):  # sample events
    M, D = int(evM[i]), int(evD[i])
    js = np.unique(np.concatenate([np.array(byq[q]) for q in factor(M)]))
    g = np.gcd(evM[js], M)
    # conflict iff some prime of g has different residue  <=> D-D' not = 0 mod g
    conf = ((evD[js] - D) % g) != 0
    gam_max = max(gam_max, P[js][conf].sum())
# Delta: count pair at its least common prime q
Da = Db = 0.0
for q, idx in byq.items():
    idx = np.array(idx)
    r = (-4 * evD[idx]) % q
    for rv in np.unique(r):
        b = idx[r == rv]
        if len(b) < 2:
            continue
        for k in range(len(b) - 1):
            i = b[k]; js = b[k + 1:]
            g = np.gcd(evM[js], evM[i])
            ok = ((evD[js] - evD[i]) % g) == 0
            ok &= spf[g] == q
            if not ok.any():
                continue
            gg = g[ok]
            phg = np.array([math.prod(p - 1 for p in factor(int(t))) for t in gg], dtype=float)
            pr = phg / (evPhi[i] * evPhi[js][ok])
            same = evD[js][ok] == evD[i]
            assert not ((evM[js][ok] == evM[i]) & same).any()
            Da += pr[same].sum(); Db += pr[~same].sum()
print(f"Delta_a={Da:.6f} Delta_b={Db:.6f}  max sum_Gamma P (sampled)={gam_max:.3e}  max w_q={max(wq.values()):.3e}")
# proof bounds
om = lambda n: len(factor(n))
ns = sorted(Dby)
Da_bd = 8 * sum(2 ** om(n) * (1 / y + L / (4 * n)) * (1 + L) ** 2 / (4 * n) for n in ns)
wq_bd = max((2 / q) * sum(2 ** om(n) * (L / (4 * n) + min(1, q / math.sqrt(T))) for n in ns) for q in byq)
omax = max(len(factor(int(M))) for M in set(evM.tolist()))
# Delta_b intermediate bound: sum over ordered D != D', g | m y-rough sqfree >1 of (8/g) sigma sigma
def sig(g, n):
    return L / (4 * n) + min(1, g / math.sqrt(T))
allD = [(D, n) for n in ns for D in Dby[n]]
Db_bd = 0.0
for D, n in allD:
    for D2, n2 in allD:
        if D2 == D:
            continue
        m = abs(D - D2)
        for g in range(y + 1, m + 1):
            if m % g == 0:
                fs = factor(g)
                if fs[0] > y and math.prod(fs) == g:
                    Db_bd += 8 / g * sig(g, n) * sig(g, n2)
print(f"bounds: Delta_a<={Da_bd:.4f} Delta_b<={Db_bd:.6f} w_q<={wq_bd:.3e} sumGamma<=omega*max_wq={omax*max(wq.values()):.3e}")
print("CHECK", Da <= Da_bd, Db <= Db_bd + 1e-12, max(wq.values()) <= wq_bd)
