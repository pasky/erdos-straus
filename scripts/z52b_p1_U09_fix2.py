# z52b pass1 U09 (fix round 2): Z1071 (autocorrelation of R/log^2 p over consecutive primes) and Z1235 (calibration with C=1 target).
import numpy as np, random
from scipy.stats import pearsonr
rows=[list(map(int,l.split())) for l in open('data/z52b/pass1/U09/R7.txt')]
P=np.array([r[0] for r in rows]); R=np.array([r[1] for r in rows],float); mask=[r[4] for r in rows]
y=R/np.log(P.astype(float))**2
print("== Z1071 (normalised): lag-1 autocorrelation of R/log^2 p over consecutive primes")
for name,m in [("p≡1 (4), all",np.ones(len(P),bool)),("p≡1 (mod 840)",P%840==1),("p≡1 (mod 24)",P%24==1)]:
    s=y[m]; r1=pearsonr(s[:-1],s[1:])[0]
    sh=[pearsonr(np.random.permutation(s)[:-1],np.random.permutation(s)[1:])[0] for _ in range(300)]
    print(f"  {name}: n={len(s)}, lag-1 r={r1:.4f}; shuffled mean {np.mean(sh):.4f} sd {np.std(sh):.4f}")
# what drives it? lag-1 with class-mean removed by p mod 840 (residual)
cm={}
for c in set((P%840).tolist()):
    cm[c]=y[P%840==c].mean()
res=y-np.array([cm[c] for c in (P%840).tolist()])
print(f"  after removing mod-840 class means: lag-1 r={pearsonr(res[:-1],res[1:])[0]:.4f}")
print("== Z1235: calibration of 'C=1 succeeds' predictor (train p<=1e5, test p>1e5), predictor = mod-840 class mean")
succ=np.array([(int(m)&1) for m in mask],float)
train=P<=10**5; test=~train; cls=P%840
pm={c:succ[train&(cls==c)].mean() for c in set(cls[train].tolist()) if (train&(cls==c)).sum()>0}
pt=np.array([pm.get(int(c),succ[train].mean()) for c in cls[test]]); st=succ[test]
print(f"  test n={int(test.sum())}, base rate {st.mean():.3f}; Brier(class) {np.mean((pt-st)**2):.4f} vs Brier(base) {np.mean((st.mean()-st)**2):.4f}")
bins=[0,0.1,0.2,0.3,0.4,0.6,1.01]
for lo,hi in zip(bins[:-1],bins[1:]):
    s=(pt>=lo)&(pt<hi)
    if s.sum()>0: print(f"   predicted in [{lo},{hi}): n={int(s.sum())}, mean pred {pt[s].mean():.3f}, observed {st[s].mean():.3f}")
