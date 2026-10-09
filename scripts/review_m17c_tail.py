# R98b from-scratch: closed-form geometric tails for M17B Thm 4.1 / M17C Lemma 1.1
from mpmath import mp, mpf, floor
mp.dps = 40
def TQ(fac=1):
    q = mpf(17)**(-mpf(2)/5)
    return 2*17*q**9/(1-q**2)*fac
def Cstar(theta, K0, rho, cum):
    r = mpf(17)**(mpf(theta)-mpf(1)/2)
    S = mpf(17)**mpf(0.5)*r**K0/(1-r**2)   # sum_{K>=K0 odd} 17^{theta K+(1-K)/2}
    fac = mpf(16)/17 if cum else 1
    return (rho - TQ())/(2*fac*S)
rho1 = mpf(16344335)/24137569; rho2 = mpf(961421)/1419857
print("TQ", TQ(), "TQ*(1-17^-2)", TQ(1-mpf(17)**-2))
def fl(x):
    # floor to 4 significant digits
    import math
    e = math.floor(math.log10(float(x))) - 3
    return floor(x/mpf(10)**e)*mpf(10)**e
for th in [0.25,0.30,0.35,0.40,0.42,0.45]:
    a=Cstar(th,13,rho1,False); b=Cstar(th,13,rho1,True); c=Cstar(th,15,rho2,True); d=Cstar(th,15,rho2,False)
    print(th, [mp.nstr(fl(x),6) for x in (a,b,c,d)], mp.nstr(a,10), mp.nstr(b,10), mp.nstr(c,10))
print("17^5.2*1.497", mpf(17)**5.2*1.497)
