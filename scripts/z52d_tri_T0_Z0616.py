# z52d triage T0, Z0616: E_1/E_2 (★)-slice correlation within classes p mod 3, 8, 24, 120. Needs /tmp/mask1e6.txt from scripts/z52d_p2_TO2_mask.c 1000000 /tmp/mask1e6.txt
import numpy as np
M = np.loadtxt('/tmp/mask1e6.txt', dtype=np.int64)
mask = np.zeros(10**6+1, np.int64); mask[M[:,0]] = M[:,1]
s = np.ones(10**6+1, bool); s[:2] = False
for i in range(2, 1001):
    if s[i]: s[i*i::i] = False
P = np.nonzero(s)[0]; P = P[(P % 4 == 1) & (P > 5)]
E1=(mask[P]&1).astype(float); E2=((mask[P]>>1)&1).astype(float)
print('overall', np.corrcoef(E1,E2)[0,1])
for mod in (3,8,24,120):
    cs=[];ws=[]
    for r in sorted(set(P%mod)):
        sel=P%mod==r
        if E1[sel].std()>0 and E2[sel].std()>0:
            cs.append(np.corrcoef(E1[sel],E2[sel])[0,1]); ws.append(sel.sum())
        print(mod, r, 'P(E1)=%.2f P(E2)=%.2f'%(E1[sel].mean(),E2[sel].mean()), 'n',sel.sum()) if mod<=24 else None
    print('mod',mod,'weighted within-class corr', np.average(cs,weights=ws))
