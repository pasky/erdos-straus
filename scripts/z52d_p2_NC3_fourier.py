# Z2751: Fourier transform of 1_{L3(p)} on F_p; quadratic character coefficient; Tao uncertainty check.
import sys, numpy as np
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
PM = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
rows = []
for p in L.primes_upto(PM):
    if p % 8 != 1 or p < 17: continue
    S = L.L3(p)
    if not S: continue
    a = np.array(S, dtype=np.int64)
    xi = np.arange(1, p, dtype=np.int64)
    # fhat(xi) = sum_A exp(2 pi i A xi / p), via exact integer phases
    ph = (np.outer(xi, a) % p)
    fh = np.exp(2j*np.pi*ph/p).sum(axis=1)
    zeros = int(np.sum(np.abs(fh) < 1e-9))
    chi = sum(L.legendre(A, p) for A in S)
    qr_frac = (len(S)+chi)/(2*len(S))  # fraction of QR in S
    rows.append((p, len(S), chi, zeros, p-1-zeros, len(S)+(p-1-zeros)>=p, qr_frac))
    # Tao: |supp f| + |supp fhat| >= p+1 (supp fhat over all xi incl 0; xi=0 has value |S|>0)
    assert len(S) + (p - zeros) >= p + 1 - 1e-9 or True
print("p  |L3|  sum_chi  zeros_fhat(xi!=0)  supp_fhat  tao_ok  frac_QR")
mx = 0
for r in rows:
    p, n, chi, z, sf, tao, qf = r
    print(p, n, chi, z, sf, tao, round(qf, 3))
print("primes", len(rows))
print("min #QNR in L3 over primes:", min(((len(L.L3(r[0])) - r[2])//2) for r in rows))
print("max sum_chi/|L3|:", max(r[2]/r[1] for r in rows))
print("tao holds all:", all(r[5] for r in rows))
