"""R184 reviewer 2: sanity check of the Titchmarsh constant used in Prop 6.1 for tau(p+1),
and of G = sum_{p in (a,b]} (tau(p+1)-2)/p vs (C/2) log(b/a)... per unit log."""
import numpy as np, sys
from math import log, pi
X = int(sys.argv[1]) if len(sys.argv)>1 else 10**7
tau = np.zeros(X+2, dtype=np.int32)
for d in range(1, X+2): tau[d::d] += 1
s = np.ones(X+1, dtype=bool); s[:2]=False
for i in range(2, int(X**.5)+1):
    if s[i]: s[i*i::i]=False
P = np.nonzero(s)[0]
C = (pi**2/6)*1.2020569031595942/(pi**6/945)
for y in (10**5, 10**6, X):
    p = P[P<=y]; print('y=%d  sum tau(p+1)/y = %.4f   C = %.4f' % (y, tau[p+1].sum()/y, C))
for a,b in ((10**3,10**5),(10**4,10**6),(10**5,10**7)):
    p = P[(P>a)&(P<=b)]; G = ((tau[p+1]-2)/p).sum()
    print('G on (%g,%g] = %.3f   C*log(b/a) - 2log(log b/log a) = %.3f' % (a,b,G, C*log(b/a)-2*log(log(b)/log(a))))
