# z59 MSPLUS: negative-binomial (group mean/variance) prediction of zero counts per group and decade, from the 'A' lines
# of scripts/z59_msplus_strat.c output (n <= 1e9). Usage: python z59_msplus_nb.py STRAT_OUTPUT
import sys, math
M = {1, 121, 169, 289, 361, 529}
tab = {}
for line in open(sys.argv[1]):
    if line[0] != 'A': continue
    _, cat, a, b, cnt, s, s2, z, l2 = line.split()
    a=int(a); b=int(b)
    if cat=='S': continue
    g = math.gcd(a,105)
    key=(cat, 'M' if a in M else ('unit' if g==1 else f'g{g}'), b//4)
    G=tab.setdefault(key,[0,0,0,0,0])
    for i,x in enumerate((cnt,s,s2,z,l2)): G[i]+=float(x)
for key in sorted(tab):
    cnt,s,s2,z,l2=tab[key]
    m=s/cnt; var=s2/cnt-m*m; k=m*m/(var-m) if var>m else float('inf')
    p0=(1+m/k)**(-k)
    print(f"{key[0]} {key[1]:5s} dec{key[2]} cnt={cnt:11.0f} mean={m:7.2f} sd={math.sqrt(var):6.2f} cv={math.sqrt(var)/m:.3f} k={k:6.2f} zeros={z:4.0f} le2={l2:6.0f} NBpred0={cnt*p0:9.3g}")
