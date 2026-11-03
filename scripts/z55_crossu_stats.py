# z55 CROSSU stats (v2, after hostile review): twisted layers N_c - G_c per class c, with CLASS-SPECIFIC model variance
# V_c (engine: independent points, j uniform in its coset).  Per tag: table over all 18 classes of
#   mean(N_c-G_c), sd(N_c-G_c)/sqrt(mean V_c), z_c = sum(N_c-G_c)/sqrt(sum V_c);
# summary ranges over all classes; max |corr| over all pairs of the 18 classes (sample correlation across the
# tag's n values); j/u histograms with max deviation from 1/NB.   Usage: python scripts/z55_crossu_stats.py main.tsv
import sys, math, collections, itertools
rows = [l.rstrip('\n').split('\t') for l in open(sys.argv[1])]
hdr = rows[0]; rows = rows[1:]; H = {k: i for i, k in enumerate(hdr)}
CL = [1,2,3,4,5,6,7,8,9,10,11,12,16,25,-1,-2,-3,-4]
by = collections.defaultdict(list)
for r in rows: by[r[0]].append(r)
def f(r, k): return float(r[H[k]])
def corr(a, b):
    n = len(a); ma = sum(a)/n; mb = sum(b)/n
    sa = math.sqrt(sum((x-ma)**2 for x in a)); sb = math.sqrt(sum((x-mb)**2 for x in b))
    return sum((x-ma)*(y-mb) for x, y in zip(a, b))/(sa*sb) if sa*sb > 0 else float('nan')
print("# checks: badj/badA/badB totals =", sum(f(r,'badj') for r in rows), sum(f(r,'badA') for r in rows), sum(f(r,'badB') for r in rows), " nA total =", sum(f(r,'nA') for r in rows), " nsh3 total =", sum(f(r,'nsh3') for r in rows))
for tag, rs in by.items():
    n = len(rs)
    print(f"\n== {tag}  n={n}  meanR={sum(f(r,'R') for r in rs)/n:.3f} meanG={sum(f(r,'G') for r in rs)/n:.3f} meanV1={sum(f(r,'V1') for r in rs)/n:.3f} meanShell3={sum(f(r,'nsh3') for r in rs)/n:.1f} meanHits={sum(f(r,'nhit') for r in rs)/n:.2f}")
    print("    c  mean(N-G)  sd/sqrt(meanV_c)   z_c    mean(G-E)  mean(N)")
    D = {}; summ = []
    for c in CL:
        d = [f(r,f'N{c}') - f(r,f'G{c}') for r in rs]; D[c] = d
        m = sum(d)/n; sd = math.sqrt(sum((x-m)**2 for x in d)/(n-1)) if n > 1 else 0
        V = sum(f(r,f'V{c}') for r in rs); mV = V/n
        ratio = sd/math.sqrt(mV) if mV > 0 else float('nan'); z = sum(d)/math.sqrt(V) if V > 0 else float('nan')
        ge = sum(f(r,f'G{c}') - f(r,f'E{c}') for r in rs)/n
        summ.append((m, ratio, z))
        print(f"  {c:3d}   {m:7.3f}      {ratio:6.3f}       {z:6.2f}    {ge:7.3f}   {sum(f(r,f'N{c}') for r in rs)/n:7.3f}")
    fin = [s for s in summ if not math.isnan(s[1])]
    if fin:
        print(f"  ranges over classes: mean(N-G) in [{min(s[0] for s in fin):.3f}, {max(s[0] for s in fin):.3f}], sd-ratio in [{min(s[1] for s in fin):.3f}, {max(s[1] for s in fin):.3f}], z in [{min(s[2] for s in fin):.2f}, {max(s[2] for s in fin):.2f}]")
    cs = [(abs(corr(D[a], D[b])), a, b) for a, b in itertools.combinations(CL, 2)]
    cs = [x for x in cs if not math.isnan(x[0])]
    if cs:
        cs.sort(reverse=True)
        print(f"  max |corr| over {len(cs)} class pairs: " + ", ".join(f"({a},{b})={v:.3f}" for v, a, b in cs[:4]) + f";  expected max for independent classes ~ {math.sqrt(2*math.log(2*len(cs)))/math.sqrt(n):.2f} (sqrt(2 ln(2·#pairs))/sqrt(n))")
    hb = [sum(f(r,f'HB{b}') for r in rs) for b in range(10)]; hg = [sum(f(r,f'HBg{b}') for r in rs) for b in range(10)]
    tb = sum(hb); tg = sum(hg)
    print("  j/u hist (all):   " + " ".join(f"{x/tb:.4f}" for x in hb) + f"   N={tb:.0f}  maxdev={max(abs(x/tb-0.1) for x in hb):.4f}")
    if tg > 0: print("  j/u hist (genus): " + " ".join(f"{x/tg:.4f}" for x in hg) + f"   N={tg:.0f}")
# pooled over random primes
pr = [r for r in rows if r[0].startswith('p1e')]
print(f"\n== pooled random primes n={len(pr)}: z_c (class-specific V_c):")
print("  " + "  ".join(f"c={c}:{sum(f(r,f'N{c}')-f(r,f'G{c}') for r in pr)/math.sqrt(sum(f(r,f'V{c}') for r in pr)):+.2f}" for c in CL))
