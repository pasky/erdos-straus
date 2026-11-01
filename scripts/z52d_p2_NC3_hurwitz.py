# Z2732: M_t^lev(n) = (tau(N) - sigma_{chi_{-t}}(N))/phi(t), N = t n + 1 (FRONTIER 2.3/SYNTHESIS_SPARKS9 Prop 2.2),
# versus Hurwitz class-number sums H(4 t n - s^2) (PARI qfbhclassno). Checks: (a) Kronecker-Hurwitz identity
# sum_s H(4N - s^2) = 2 sigma(N) - sum_{d|N} min(d,N/d) (sanity); (b) whether sum_{t<=T} M_t^lev(n) is an exact
# linear function of sum_{t<=T} sum_s H(4tn - s^2) (least squares over n).
import sys, math
import cypari2
import numpy as np
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
from sympy import divisor_sigma, divisors, totient, factorint
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400
T = int(sys.argv[2]) if len(sys.argv) > 2 else 30
def H(D):  # Hurwitz class number of discriminant -D (D>0, D = 0,3 mod 4)
    if D == 0: return -1/12
    if D % 4 in (1, 2): return 0
    return float(pari(f"qfbhclassno({D})"))
def HS(N):  # sum_s H(4N - s^2)
    tot = 0.0; s = 0
    while s*s <= 4*N:
        tot += H(4*N - s*s) * (1 if s == 0 else 2); s += 1
    return tot
def lam(N): return sum(min(d, N//d) for d in divisors(N))
# (a) Kronecker-Hurwitz sanity
for N in [1,2,3,5,10,12,30]:
    lhs = HS(N); rhs = 2*divisor_sigma(N) - lam(N)
    print("KH check", N, round(lhs,6), rhs)
def kron(a, n):  # Kronecker symbol (a/n) for n>0 via pari
    return int(pari(f"kronecker({a},{n})"))
def Mlev(t, n):
    N = t*n + 1
    if t < 2: return None
    tau = len(divisors(N))
    sig = sum(kron(-t, d) for d in divisors(N))
    return float((tau - sig) / int(totient(t)))
rows = []
for n in range(2, NMAX+1):
    m = 0.0; h = 0.0
    for t in range(2, T+1):
        m += float(Mlev(t, n)); h += float(HS(t*n))
    rows.append((n, m, h))
arr = np.array(rows)
A = np.vstack([arr[:,2], np.ones(len(arr))]).T
coef, res, *_ = np.linalg.lstsq(A, arr[:,1], rcond=None)
print("n range", 2, NMAX, "T", T)
print("fit sum_t M_t^lev(n) ~ a*sum_t sum_s H(4tn-s^2) + b : a=%.6f b=%.6f maxresid=%.3e" % (coef[0], coef[1], np.max(np.abs(A@coef-arr[:,1]))))
print("first rows (n, sum M, sum H):", [tuple(round(x,3) for x in r) for r in rows[:6]])
