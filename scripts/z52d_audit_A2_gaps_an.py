"""Analyse min gaps y-x, z-y over all ES solutions of 4/p (output of z52d_audit_A2_gaps.c)."""
import numpy as np, sys
A=np.loadtxt(sys.argv[1],dtype=np.float64); p=A[:,0]; g1=A[:,2]; x1=A[:,3]; g2=A[:,4]
for lab,m in [("p=1(4)",p%4==1),("p=3(4)",p%4==3)]:
    P=p[m]; G1=g1[m]; G2=g2[m]; X1=x1[m]; sel=P>1000
    print(lab, "n=",m.sum(), " min(y-x): frac==0",np.mean(G1==0).round(4))
    if lab=="p=1(4)":
        for lo,hi in [(1e3,1e4),(1e4,5e4),(5e4,1e5),(1e5,2e5)]:
            s=(P>=lo)&(P<hi)
            r1=np.log(G1[s])/np.log(P[s]); r2=np.log(G2[s])/np.log(P[s])
            print(f"  [{lo:.0e},{hi:.0e}) n={s.sum()} log(min y-x)/log p: median {np.median(r1):.3f} q10 {np.quantile(r1,.1):.3f} q90 {np.quantile(r1,.9):.3f} max {r1.max():.3f};"
                  f" min(y-x)<=log^2 p: {np.mean(G1[s]<=np.log(P[s])**2):.3f};  log(min z-y)/log p median {np.median(r2):.3f} min {r2.min():.3f} max {r2.max():.3f}")
        # which gap values: small ones
        print("  smallest min(y-x) values overall:", sorted(set(G1.astype(int)))[:15])
        print("  primes>1e5 with largest min(y-x)/p^0.5:", sorted(zip(G1[P>1e5]/np.sqrt(P[P>1e5]),P[P>1e5]))[-3:])
        # min(z-y) relative to p: is z-y >= p always?
        print("  min over p of min(z-y)/p:", np.min(G2/P).round(4), " frac min(z-y) divisible by p:", np.mean(G2%P==0).round(3))
        print("  corr(log min(y-x), log U):", np.corrcoef(np.log(G1[sel]),np.log(A[m][sel,1]))[0,1].round(3))
