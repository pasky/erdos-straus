"""z58 WITNESS: dispersion of the (★) solution count in the boundary {min log-coordinate <= t} vs the centre {> t},
over control primes (z58_witness_sols output). Usage: python3 z58_witness_disp.py ctrl2_sols.txt"""
import sys, math, statistics as st
fn = sys.argv[1]
for thr in (0.05, 0.1, 0.15):
    bd = []; ce = []
    for line in open(fn):
        a, b = line.split(':'); p = int(a.split()[0]); L = math.log(p / 4)
        S = [tuple(map(int, t.split(','))) for t in b.split()]
        m = [min(math.log(x) / L for x in s) for s in S]
        bd.append(sum(v <= thr for v in m)); ce.append(sum(v > thr for v in m))
    print(thr, 'boundary mean %.2f var/mean %.2f | centre mean %.2f var/mean %.2f | P(bd=0) %.3f exp(-mean) %.2g | P(ce=0) %.3f exp(-mean) %.2g' % (
        st.mean(bd), st.variance(bd) / st.mean(bd), st.mean(ce), st.variance(ce) / st.mean(ce), sum(x == 0 for x in bd) / len(bd),
        math.exp(-st.mean(bd)), sum(x == 0 for x in ce) / len(ce), math.exp(-st.mean(ce))))
