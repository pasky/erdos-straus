# z53 HCSHIFTS: model M exponent check. cost(X) = sum_{x<=X} E[1-exp(-2^w/x)], w ~ Poisson(lam), X = exp(kappa*lam*ln2);
# prints log(cost)/lam against g(kappa) = kappa(1+ln2-ln kappa) - 1 (valid for 1 <= kappa < 2).
import math
def cost(lam, kappa):
    lnX = kappa*lam*math.log(2)
    # integrate over x log-uniformly: sum_{x<=X} f(x) ~ int_1^X f(x) dx ; use u = ln x grid
    K = int(6*lam+50)
    lp = [ -lam + k*math.log(lam) - math.lgamma(k+1) for k in range(K)]
    tot = 0.0; N = 4000
    for i in range(N):
        u = lnX*(i+0.5)/N; x = math.exp(u)
        f = 0.0
        for k in range(K):
            t = 2.0**k/x
            f += math.exp(lp[k])*(-math.expm1(-t))
        tot += f*x*lnX/N
    return tot
def g(k): return k*(1+math.log(2)-math.log(k))-1
for lam in [20, 40, 80, 160]:
    print(lam, " ".join(f"k={k}: {math.log(cost(lam,k))/lam:.3f} (g={g(k):.3f})" for k in [1.2,1.5,1.8,2.0,2.3]))
