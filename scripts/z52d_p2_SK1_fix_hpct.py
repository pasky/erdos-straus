# z52d pass2 SK1 fix (Z0815 correction): percentiles of h(-4p)/sqrt(p) for R-zeros against a random sample of
# primes 1 mod 4 in [1e5,1e8] (2000 primes, data/z52b/pass2/SK1/Z0815_hneg_sample_1e8.txt). The sample is restricted to
# [1e5,1e8], so only the 8 R-zeros >= 1e5 are compared; the 6 R-zeros below 1e5 are reported separately vs the <=1e5 set.
import math, statistics
D='data/z52b/pass2/SK1/'
H={int(l.split()[0]):int(l.split()[1]) for l in open(D+'Z0815_hneg_sample_1e8.txt')}
R0=sorted(int(l.split()[1]) for l in open(D+'Z0849_star_1e8_primes.txt') if l.startswith('R0'))
samp=[p for p in H if p not in set(R0)]
v={p:H[p]/math.sqrt(p) for p in H}
allv=sorted(v[p] for p in samp)
pc=lambda x: sum(1 for y in allv if y<x)/len(allv)
big=[p for p in R0 if p>=100000]
pcs=[pc(v[p]) for p in big]
print("R-zeros >= 1e5 (n=%d):"%len(big), [(p,round(pc(v[p]),3)) for p in big])
print("mean percentile %.3f; uniform sd of mean %.3f; z = %.2f"%(statistics.mean(pcs), (1/12)**.5/len(pcs)**.5, (statistics.mean(pcs)-0.5)/((1/12)**.5/len(pcs)**.5)))
# restricted to primes <= 1e5 (p>=5) separately, from the full list in Z0815_hneg4p_1e5.txt
H5={int(l.split()[0]):int(l.split()[1]) for l in open(D+'Z0815_hneg4p_1e5.txt')}
v5=[H5[p]/math.sqrt(p) for p in H5 if p%4==1 and p>7]
small=[p for p in R0 if p<100000 and p in H5]
p5=[sum(1 for y in v5 if y<H5[p]/math.sqrt(p))/len(v5) for p in small]
print("R-zeros < 1e5 (n=%d) percentile in all p=1 mod 4 <=1e5:"%len(small), [round(x,3) for x in p5], "mean %.3f"%statistics.mean(p5))
