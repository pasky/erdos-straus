import sys, math
import numpy as np
for name in sys.argv[1:]:
    rows=[list(map(float,l.split())) for l in open(name) if l.strip()]
    a=np.array(rows)
    n,R,cL,cC,uL,uC,anyL,anyC,ratio,defect=a.T
    tot=R.sum()
    print(name, 'N=%d meanR=%.2f  meanR/L^2=%.4f  zeros=%d'%(len(R),R.mean(),(R/np.log(n)**2).mean(),(R==0).sum()))
    if tot>0:
        print('  shares: C-Lenstra %.3f (asym 1/4)  C-CHN %.3f (4/9=.444)  u-Lenstra %.3f (4/9) u-CHN %.3f (9/16=.5625)  anyLenstra %.3f anyCHN %.3f'%(cL.sum()/tot,cC.sum()/tot,uL.sum()/tot,uC.sum()/tot,anyL.sum()/tot,anyC.sum()/tot))
    m=R>0
    if ratio.min()>=0 and len(R)>50:
        L2=np.log(n)**2
        y=R/L2
        print('  corr(R/L^2, b/a)=%.3f  corr(R/L^2, log(defect+1))=%.3f'%(np.corrcoef(y,ratio)[0,1], np.corrcoef(y,np.log(defect+1))[0,1]))
