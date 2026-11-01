import numpy as np, sys
lo, hi = int(sys.argv[1]), int(sys.argv[2])
s = np.ones(hi+1, bool); s[:2]=False
for i in range(2, int(hi**.5)+1):
    if s[i]: s[i*i::i]=False
P = np.nonzero(s)[0]; P = P[(P>=lo)]
mod = sys.argv[3] if len(sys.argv)>3 else None
if mod:
    m, rs = mod.split(':'); m=int(m); rs=set(int(r) for r in rs.split(','))
    P = P[np.isin(P % m, list(rs))]
np.savetxt(sys.stdout, P, fmt='%d')
