# z57 BFII: dispersion of the order>=3 remainder in a witness block, Type II (all c) vs c=1 line.
import sys, numpy as np
d=np.loadtxt(sys.argv[1]); p,A,G,A1,G1=d.T
for name,a,g in (("TypeII",A,G),("c=1",A1,G1)):
    z=(a-g)/np.sqrt(g)
    print(f"{name}: mean actual {a.mean():.2f} mean genus {g.mean():.2f} mean naive-ratio actual/genus {a.mean()/g.mean():.3f};"
          f" var(actual-genus)/mean(genus) = {np.var(a-g)/g.mean():.2f};  var(actual)/mean(actual) = {np.var(a)/a.mean():.2f};"
          f" corr(actual,genus) = {np.corrcoef(a,g)[0,1]:.3f}; frac actual==0: {(a==0).mean():.4f}; min actual/genus {np.min(a/g):.3f}")
    print(f"   relative remainder |actual-genus|/genus: mean {np.mean(np.abs(a-g)/g):.3f}, 99th pct {np.percentile(np.abs(a-g)/g,99):.3f}")
