# z55 CROSSU stats: twisted layers N_c - G_c (c-class index counts vs genus-coset prediction), pooled per tag.
# Usage: python scripts/z55_crossu_stats.py data/z55/crossu/main.tsv > data/z55/crossu/stats.txt
import sys, math, collections
rows = [l.rstrip('\n').split('\t') for l in open(sys.argv[1])]
hdr = rows[0]; rows = rows[1:]
H = {k: i for i, k in enumerate(hdr)}
CL = [1,2,3,4,5,6,7,8,9,10,11,12,16,25,-1,-2,-3,-4]
by = collections.defaultdict(list)
for r in rows: by[r[0]].append(r)
def f(r, k): return float(r[H[k]])
print("# per tag: n, mean R, mean G, mean VRG;  then per c: mean(N_c-G_c), sd, z_pooled = sum(N_c-G_c)/sqrt(sum VRG), mean(G_c-E_c)")
for tag, rs in by.items():
    n = len(rs)
    print(f"\n== {tag}  n={n}  meanR={sum(f(r,'R') for r in rs)/n:.3f} meanG={sum(f(r,'G') for r in rs)/n:.3f} meanVRG={sum(f(r,'VRG') for r in rs)/n:.3f} meanShell3={sum(f(r,'nsh3') for r in rs)/n:.1f}")
    sV = sum(f(r,'VRG') for r in rs)
    print("   c   mean(N-G)   sd(N-G)   z_pooled   mean(G-E)   mean(N)")
    for c in CL:
        d = [f(r,f'N{c}') - f(r,f'G{c}') for r in rs]
        m = sum(d)/n; sd = math.sqrt(max(sum((x-m)**2 for x in d)/(n-1), 0)) if n > 1 else 0
        ge = sum(f(r,f'G{c}') - f(r,f'E{c}') for r in rs)/n
        print(f"  {c:3d}   {m:8.3f}   {sd:7.3f}   {(sum(d)/math.sqrt(sV) if sV>0 else float("nan")):7.2f}    {ge:7.3f}    {sum(f(r,f'N{c}') for r in rs)/n:7.3f}")
    # correlation matrix of N_c - G_c across c (first 8 c's + -1)
    cs = [1,2,3,4,5,-1]
    D = {c: [f(r,f'N{c}') - f(r,f'G{c}') for r in rs] for c in cs}
    def corr(a, b):
        ma = sum(a)/n; mb = sum(b)/n
        sa = math.sqrt(sum((x-ma)**2 for x in a)); sb = math.sqrt(sum((x-mb)**2 for x in b))
        return sum((x-ma)*(y-mb) for x, y in zip(a, b))/(sa*sb) if sa*sb > 0 else float('nan')
    print("  corr(N_c-G_c, N_c'-G_c'):  " + "  ".join(f"({c},{c2})={corr(D[c],D[c2]):+.2f}" for i, c in enumerate(cs) for c2 in cs[i+1:]))
    # j/u histograms pooled
    hb = [sum(f(r,f'HB{b}') for r in rs) for b in range(10)]; hg = [sum(f(r,f'HBg{b}') for r in rs) for b in range(10)]
    tb = sum(hb); tg = sum(hg)
    print("  j/u hist (all):   " + " ".join(f"{x/tb:.3f}" for x in hb) + f"   N={tb:.0f}")
    print("  j/u hist (genus): " + " ".join(f"{x/tg:.3f}" for x in hg) + f"   N={tg:.0f}" if tg > 0 else "  (no genus points)")
