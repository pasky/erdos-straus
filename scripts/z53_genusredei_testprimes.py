# Summarise z53_genusredei_freemodel L-mode output: per test prime, hits on the 15 A-lines (4Cp+1, C<=15) and 15 B-lines
# (p+4d, d<=15) and the free-model probability (harmonic-weighted, product law only) of missing all of them.
import sys, math, collections
rows = collections.defaultdict(list)
for line in open(sys.argv[1]):
    f = line.rstrip('\n').split('\t')
    if line.startswith('#') or not f[0].isdigit() or not f[1].startswith('L'): continue
    rows[int(f[0])].append((int(f[1][1:]), int(f[5][3:]), float(f[6][2:])))
print("n\tA hits/15\tlog10 Pmodel(all A miss)\tB hits/15\tlog10 Pmodel(all B miss)")
for n in rows:
    A = [r for r in rows[n] if r[0] < 15]; B = [r for r in rows[n] if r[0] >= 15]
    la = sum(math.log10(max(1e-300, 1 - r[2])) for r in A); lb = sum(math.log10(max(1e-300, 1 - r[2])) for r in B)
    print("%d\t%d/%d\t%.2f\t%d/%d\t%.2f" % (n, sum(r[1] for r in A), len(A), la, sum(r[1] for r in B), len(B), lb))
