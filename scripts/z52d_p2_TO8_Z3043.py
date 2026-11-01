# z52d P2 TO8 Z3043: check K1 coefficientwise for t=5:
#   q^{t-2} (Q;Q)^2 θ(X^2)/θ(X)^2 = sum_n (D^-_t - D^+_t)(tn+1) q^n,  X=q^{t-1}, Q=q^t, θ(x)=(x;Q)(Q/x;Q)
# D^-_t(N)=#{d|N: d≡-1 mod t}, D^+_t(N)=#{d|N: d≡+1 mod t}; test both sign conventions.
import sys
from sympy import factorint
t = int(sys.argv[1]) if len(sys.argv) > 1 else 5
NMAX = 60; L = t * NMAX + 5
def mul(a, b):
    c = [0] * (L + 1)
    for i, x in enumerate(a):
        if x:
            for j in range(L + 1 - i):
                if b[j]: c[i + j] += x * b[j]
    return c
def inv(a):
    b = [0] * (L + 1); b[0] = 1
    for n in range(1, L + 1):
        s = 0
        for k in range(1, n + 1):
            if a[k]: s += a[k] * b[n - k]
        b[n] = -s
    return b
def theta(e):
    """Laurent series theta(q^e) = (y;Q)(Q/y;Q), y=q^e, as (offset, list). Factors (1-q^m) with m<=0 handled by -q^m(1-q^-m)."""
    off = 0; sign = 1; s = [0] * (L + 1); s[0] = 1
    exps = []
    for k in range(0, 2 * L):
        for m in (e + t * k, t - e + t * k):
            exps.append(m)
    for m in exps:
        if m == 0:
            return None
        if m > L: continue
        if m > 0:
            f = [0] * (L + 1); f[0] = 1; f[m] = -1; s = mul(s, f)
        else:  # 1 - q^m = -q^m (1 - q^{-m})
            off += m; sign = -sign
            f = [0] * (L + 1); f[0] = 1
            if -m <= L: f[-m] = -1
            s = mul(s, f)
    return off, sign, s
def theta_pow(e, p):
    off = 0; sign = 1; s = [0] * (L + 1); s[0] = 1
    for _ in range(p):
        o, sg, ss = theta(e); off += o; sign *= sg; s = mul(s, ss)
    return off, sign, s
# θ(X^2): X^2 = q^{2(t-1)}, exponent e=2(t-1) ; θ(X)^2 : e=t-1 squared
o1, s1, A = theta(2 * (t - 1))
o2, s2, B = theta_pow(t - 1, 2)
# (Q;Q)^2 = prod (1-q^{tk})^2, k>=1
Qp = [0] * (L + 1); Qp[0] = 1
for k in range(1, L // t + 1):
    f = [0] * (L + 1); f[0] = 1; f[t * k] = -1
    Qp = mul(Qp, f); Qp = mul(Qp, f)
ratio = mul(Qp, mul(A, inv(B)))
off = o1 - o2 + (t - 2)
sign = s1 * s2
# total series = sign * q^{off} * ratio ; want coefficient of q^n
def coeff(n):
    k = n - off
    if k < 0 or k > L: return None
    return sign * ratio[k]
def Dpm(N, r):
    return sum(1 for d in divisors_of(N) if d % t == r % t)
def divisors_of(N):
    ds = [1]
    for q, e in factorint(N).items(): ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds
ok_minus = ok_plus = 0; tot = 0; bad = []
for n in range(1, NMAX + 1):
    c = coeff(n)
    if c is None: continue
    N = t * n + 1
    dm = Dpm(N, t - 1); dp = Dpm(N, 1)
    tot += 1
    if c == dm - dp: ok_minus += 1
    else: bad.append((n, c, dm, dp))
    if c == -(dm - dp): ok_plus += 1
print(f"t={t}: n=1..{NMAX}: coefficient equals (D- - D+)(tn+1) in {ok_minus}/{tot} cases; equals -(D- - D+) in {ok_plus}/{tot}; first mismatches {bad[:5]}")
print("low coefficients q^n (n=0..6):", [coeff(n) for n in range(0, 7)])
