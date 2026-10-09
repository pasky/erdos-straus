"""R122 from-scratch checks for Appendix A of paper/es-typei-heegner-note.tex.
Independent of the author's scripts. Run: PYTHONPATH=scripts uv run --with sympy --with mpmath python scripts/review_r122_checks.py
"""
import math, random
import mpmath as mp
import sympy as sp

ok = True
def check(name, cond):
    global ok
    print(("OK  " if cond else "FAIL"), name)
    ok &= bool(cond)

# --- Prop A.3 numerals -------------------------------------------------------
for d in [1e-4, 1e-3, 1e-2, 0.05, 0.1]:
    check(f"(C1) 2*sqrt2*pi*pi^(5d)<=45 d={d}", 2*math.sqrt(2)*math.pi*math.pi**(5*d) <= 45)
    check(f"(B) 4*2^d<=10 d={d}", 4*2**d <= 10)
    # (C2): (1+sqrt(Y/N)) K1 (2N^2)^d 4N^2 <= 10 K1 Q^{1+2d} N  with N<=Q^{1-2d}, sqrt(YN)=Q^{1-d}
    worst = 0
    for lq in [0.5, 1, 2, 5, 10, 30]:
        Q = 10**lq
        for f in [0, .3, .6, .9, 1.0]:
            N = max(1.0, Q**((1-2*d)*f))
            Y = Q**(2-2*d)/N
            C = math.pi*Q**(1-2*d)  # q0=1 upper bound; q0>1 only lowers C
            lhs = (1+math.sqrt(Y/N))*(2*N*N)**d*4*N*N
            worst = max(worst, lhs/(Q**(1+2*d)*N))
    check(f"(C2) ratio<=10 d={d} (got {worst:.3f})", worst <= 10)
check("(C2) main 2*sqrt2*pi*10<=90", 2*math.sqrt(2)*math.pi*10 <= 90)
check("int (1+t^2)/(1+t^4) = sqrt2*pi", abs(mp.quad(lambda t: (1+t*t)/(1+t**4), [-mp.inf, mp.inf]) - mp.sqrt(2)*mp.pi) < 1e-12)

# --- (PS): S(t;I) <= 2(1+t^2) sup_I S(0;I), random weighted sums --------------
random.seed(1)
worst = 0
for trial in range(300):
    Nn = random.randint(1, 40); N1 = random.randint(Nn, 2*Nn)
    J = random.randint(1, 4)
    w = [random.random() for _ in range(J)]
    a = [[complex(random.gauss(0,1), random.gauss(0,1)) for _ in range(N1+1)] for _ in range(J)]
    t = random.uniform(-20, 20)
    def S(lo, hi, tt):
        return sum(w[j]*abs(sum(a[j][n]*n**(1j*tt) for n in range(lo, hi+1)))**2 for j in range(J))
    sup = max(S(Nn, h, 0) for h in range(Nn, N1+1))
    # admissible I=[N,N1] closed real intervals, N<=N1<=2N; integer N here suffices for the sup over prefixes
    worst = max(worst, S(Nn, N1, t)/((1+t*t)*sup))
check(f"(PS) ratio<=2 (worst {worst:.3f})", worst <= 2)

# --- Thm A.4 growth: K1,c,K2<=exp(exp(B/d)) => K7<=exp(exp((B+3)/d)) ----------
def logK7_upper(B, d):
    E = mp.e**(B/d)  # log of each of K1,c,K2
    logQ0 = max((mp.log(90)+E)/(10*d*d), mp.log(2*mp.pi)/(2*d))
    logH = max(mp.log(2)+E+logQ0, mp.log(10)+E, mp.log(200)+2*E)
    return logH
worst = -mp.inf
for B in [1, 2, 5, 50, 400, 3000]:
    for d in [1e-3, 0.01, 0.03, 0.05, 0.08, 0.1]:
        r = logK7_upper(B, d) / mp.e**((B+3)/d)
        worst = max(worst, r)
check(f"A.4 growth ratio<=1 (worst {mp.nstr(worst,3)})", worst <= 1)

# --- Conversion to Cor 9.1 ----------------------------------------------------
check("K^2<=3log^2(2t)", all(((math.floor(math.log2(t))+1)**2) <= 3*math.log(2*t)**2 for t in [1,1.5,2,3,7.9,8,1e3,1e9]))
check("K<=3log^2(2t) (as printed) fails at t=1? (K=1, 3log^2 2=1.44)", 1 <= 3*math.log(2)**2)
worst = -1e9
for eps in [1e-3, 0.01, 0.1, 0.25]:
    dlt = eps/6
    for lM in [0, 1, 5, 20, 100, 1000]:
        for lt in [0, 1, 10, 100]:
            pass
            lhs = 5*dlt*(math.log(2)+lM+lt) + math.log(2+lM)
            rhs = math.log(12/eps) + eps*(lM+lt)
            worst = max(worst, lhs-rhs)
check(f"(2M0t)^(5d)(2+logM0)<=(12/e)(M0t)^e (worst log-gap {worst:.3f})", worst <= 0)
check("blocks (Q_i,16Q_i], Q_i>=1/16, cover q<=M0 with <=2+log M0", all(
    (math.floor(math.log(max(M0,1), 16))+2) <= 2+math.log(M0) or M0 < 16 and 2 <= 2+math.log(M0) for M0 in [1,2,15,16,17,1e3,1e9]))
# loglog(200/eps*K7(eps/6)) <= (24Bc+30)/eps with K7<=exp(exp((4Bc+4)/delta))
worst = -1e9
for Bc in [400, 700, 2000]:
    for eps in [1e-3, 0.01, 0.1, 0.25]:
        L = mp.log(mp.log(200/eps) + mp.e**((4*Bc+4)*6/eps))
        worst = max(worst, L - (24*Bc+30)/eps)
check("loglog bound", worst <= 0)
b = 4; Bchi = 400+64*b+16*math.log(2+10)
check(f"A0={24*Bchi+30:.0f} < 2e4 for B_W<=3, C_W<=10", 24*Bchi+30 < 2e4)

# --- Lemma A.2 ----------------------------------------------------------------
def f_tau_pow(n, B):
    r = 1; m = n; p = 2
    while p*p <= m:
        a = 0
        while m % p == 0: m//=p; a+=1
        r *= (a+1)**B; p += 1
    if m > 1: r *= 2**B
    return r
worst = 0
for B in [1, 2, 3]:
    for d in [0.5, 1.0]:
        bound = (2*B/d)**(B*2**(B/d))
        for n in range(1, 20001):
            worst = max(worst, f_tau_pow(n, B)/n**d/bound)
check(f"A.2(a) tau^B bound on n<=2e4 (worst ratio {worst:.2e})", worst <= 1)
check("A.2(a) max_a (a+1)2^{-a d/B} <= 2B/d", all(max((a+1)*2**(-a*d/B) for a in range(0, 5000)) <= 2*B/d
      for B in [1,2,4,8] for d in [0.01, 0.1, 0.5, 1]))
x = sp.symbols('x', positive=True)
h = sp.exp(-1/x)
worst = 0
der = h
for p in range(0, 11):
    if p: der = sp.diff(der, x)
    fn = sp.lambdify(x, der, 'mpmath')
    m = max(abs(fn(mp.mpf(k)/200)) for k in range(1, 2000))
    worst = max(worst, m/(9**p*math.factorial(p)**2))
check(f"A.2(c) |h^(p)|<=9^p p!^2, p<=10 (worst ratio {float(worst):.3e})", worst <= 1)
print("ALL OK" if ok else "SOME FAILED")
