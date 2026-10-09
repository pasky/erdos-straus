# R106 from-scratch recomputation of Thm 6.7 (explicit17) constants
from mpmath import mp, mpf, nsum, inf
mp.dps=40
rho1=mpf(16344335)/24137569
print("rho1",rho1)
Q=2*nsum(lambda j: mpf(17)**(mpf(3)*(2*j+9)/5+1-(2*j+9)), [0,inf])
print("Q-term",Q)
th=mpf(2)/5
SP=nsum(lambda j: mpf(17)**(th*(2*j+13)+(1-(2*j+13))/mpf(2)), [0,inf])
Ccum=(rho1-mpf('1.411e-3'))/(mpf(32)/17*SP)
Cpt=(rho1-mpf('1.411e-3'))/(2*SP)
print("C cumulative (1.411e-3)",Ccum, " with exact Q", (rho1-Q)/(mpf(32)/17*SP))
print("C pointwise",Cpt, (rho1-Q)/(2*SP))
for C in [mpf('1.497'),mpf('1.498'),mpf('1.409'),mpf('1.41')]:
    print(C, mpf(32)/17*C*SP+mpf('1.411e-3')<rho1, 2*C*SP+mpf('1.411e-3')<rho1)
# D_P(13)/17^{5.2}
print("DP13 ratio",1463/mpf(17)**5.2)
# conj 4.2 tail: D_P(K)<=K^5 K>=15 (K=13 exact 1463), D_Q(k)<=k^5 k>=9
tP=2*(1463*mpf(17)**(-6)+nsum(lambda j:(2*j+15)**5*mpf(17)**((1-(2*j+15))/mpf(2)),[0,inf]))
tQ=2*nsum(lambda j:(2*j+9)**5*mpf(17)**(1-(2*j+9)),[0,inf])
print("conj tail P",tP,"Q",tQ,"sum",tP+tQ)
# Cor 2.2 of 17C: large-c Q cost
import math
print("Cor2.2 cost", sum(3*mpf(17)**(1-mpf(k)/2)*(1+k*mp.log(17)) for k in range(9,601,2)))
# Abel summation check on random nonneg data: sum w D <= 16/17 sum w S  (finite truncation incl boundary)
import random
for t in range(5):
    D={K:random.randint(0,10**6) for K in range(13,80,2)}
    w=lambda K: mpf(17)**((1-K)/mpf(2))
    S={};s=0
    for K in range(13,80,2): s+=D[K]; S[K]=s
    lhs=sum(w(K)*D[K] for K in D); rhs=mpf(16)/17*sum(w(K)*S[K] for K in D)+w(81)*S[79]
    assert abs(lhs-rhs)<mpf(10)**-25*lhs, (lhs,rhs)
print("Abel identity ok")
