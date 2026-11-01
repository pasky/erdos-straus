import sys, math
rows=[l.split() for l in open(sys.argv[1])]
ps=[int(r[0]) for r in rows]; R=[int(r[1]) for r in rows]; bits=[r[2] for r in rows]
J=len(bits[0]); Cs=[2**j for j in range(J)]
n=len(rows)
marg=[sum(b[j]=='1' for b in bits)/n for j in range(J)]
print("n primes",n, "levels C=2^j:", Cs)
print("marginal fail P_j:", ' '.join(f"{m:.4f}" for m in marg))
# joint failure of levels 0..k (prefix), vs independent product
for k in range(1,J+1):
    emp=sum(all(b[j]=='1' for j in range(k)) for b in bits)
    ind=n*math.prod(marg[:k])
    print(f"fail all j<{k}: emp={emp} indep={ind:.2f} ratio={emp/max(ind,1e-9):.3f}")
# pairwise correlation (phi coefficient) among j
import itertools
for a,b in [(0,1),(0,2),(1,2),(2,3),(3,4),(0,5)]:
    ca=[b_[a]=='1' for b_ in bits]; cb=[b_[b]=='1' for b_ in bits]
    n11=sum(x and y for x,y in zip(ca,cb)); 
    pa,pb=marg[a],marg[b]; p11=n11/n
    phi=(p11-pa*pb)/math.sqrt(pa*(1-pa)*pb*(1-pb))
    print(f"j={a},{b}: P(both)={p11:.5f} indep={pa*pb:.5f} phi={phi:+.4f}")
# failures count distribution vs binomial-independent
from collections import Counter
cnt=Counter(sum(c=='1' for c in b) for b in bits)
print("number of failing levels among j<=10 distribution:", sorted(cnt.items())[:12])
# all-levels-fail primes
print("primes failing at all 11 levels:", [p for p,b in zip(ps,bits) if b.count('1')==J][:20])
# dependence on p mod 8 (nested moduli): marginal P_j by p mod 8
for r in [1,5]:
    idx=[i for i,p in enumerate(ps) if p%8==r]
    print("p%8=",r," P_j:", ' '.join(f"{sum(bits[i][j]=='1' for i in idx)/len(idx):.3f}" for j in range(J)), "n=",len(idx))
# tail: primes > 1e5 fail counts
big=[i for i,p in enumerate(ps) if p>1e5]
print("p>1e5 n=",len(big)," P_j:", ' '.join(f"{sum(bits[i][j]=='1' for i in big)/len(big):.4f}" for j in range(J)))
print("p>1e5 fail all j<=4 count:", sum(all(bits[i][j]=='1' for j in range(5)) for i in big), " indep:", round(len(big)*math.prod(sum(bits[i][j]=='1' for i in big)/len(big) for j in range(5)),2))
