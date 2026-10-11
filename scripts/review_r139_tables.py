"""R139 from-scratch recomputation of 17D Comp 1.2, 1.3 and the §4 constant table.
Uses mpmath at 50 digits, closed-form geometric tails (no truncation)."""
from mpmath import mp, mpf, log, floor
mp.dps = 50
S = mpf(17); rho2 = mpf(961421)/1419857
def geo(th, K0):  # sum_{K>=K0 odd} 17^(th K + (1-K)/2), closed form
    r = S**(2*th-1); return S**(th*K0+(1-K0)/mpf(2))/(1-r)
def TQ(k0):       # 2 sum_{k>=k0 odd} 17^(3k/5+1-k)
    k0 = k0 + (k0 % 2 == 0); r = S**(mpf(-4)/5); return 2*S**(mpf(3)*k0/5+1-k0)/(1-r)
print("T_Q(9) =", mp.nstr(TQ(9), 8))
print("Comp 1.2: C*(K0) = (rho2 - TQ9)/(2*(16/17)*geo)")
for th in (0.35, 0.40, 0.45):
    print(th, [mp.nstr((rho2-TQ(9))/(2*mpf(16)/17*geo(mpf(th),K0)), 5) for K0 in range(15,33,2)])
print("Comp 1.3: least odd K0>=15 with 2*sum_{K>=K0} 17^((1-K)/2) A 17^(th K)(K ln17)^B < rho2 - TQ9")
def tailB(th, A, B, K0):
    s = mpf(0); K = K0
    while True:
        t = 2*A*S**((1-K)/mpf(2)+th*K)*(K*log(S))**B; s += t
        if t < mpf(10)**-40: return s
        K += 2
for th, B in ((0.40,0),(0.40,1),(0.40,2),(0.45,1),(0.45,2)):
    row = []
    for A in (1,11,44,1000):
        K0 = 15
        while tailB(mpf(th),A,B,K0) >= rho2-TQ(9): K0 += 2
        row.append(K0)
    print((th,B), row)
print("pointwise (H_P) K>=15 rho2, D-units:", mp.nstr((rho2-TQ(9))/(2*geo(mpf(0.4),15)),6))
print("Sec 4 table (box units)")
print("global K>=15:", [mp.nstr((rho2-TQ(9))/geo(mpf(t),15),6) for t in (0.30,0.35,0.40,0.45)])
for Ls in (9,10):
    print("local L*=%d:"%Ls, [mp.nstr((1-TQ(Ls+1))/geo(mpf(t),2*Ls+1),6) for t in (0.30,0.35,0.40,0.45)], "TQ^R", mp.nstr(TQ(Ls+1),4))
