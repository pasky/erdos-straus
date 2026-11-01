"""z52d pass2 TO0b. (a) Z0122: for numerators m in the census (p<30000), which residue classes of p mod 24 (and mod 840 for
m=4 check) are NEVER representable (candidate uncovered square/residue classes). (b) Z0195: regression of the
solution count of 4/p on omega(p+3), omega((p+1)/2), omega(p-1) for p = 1 mod 4 < 1e5 (TO1 census, col 2).
(c) Z0198: the filter profile of p = 241 and 2521 across constrained worlds (filters_2e4.tsv)."""
import glob, re, math
D = 'data/z52b/pass2/TO0b/numer/'
M = {}
for f in glob.glob(D + 'numer_m*_N30000.tsv'):
    m = int(re.search(r'numer_m(\d+)_', f).group(1))
    for line in open(f):
        p, cnt, E, Mz = line.split()
        M.setdefault(int(p), {})[m] = int(cnt)
ps = sorted(M)
print('(a) m, classes mod 24 with zero representable primes (of those present), count of primes in class:')
for m in sorted({m for p in M for m in M[p]}):
    if m < 5: continue
    zero = []
    for r in range(24):
        cls = [p for p in ps if p % 24 == r and p > 5]
        if cls and all(M[p][m] == 0 for p in cls):
            zero.append(r)
    fails = sum(1 for p in ps if M[p][m] == 0)
    print(f'  m={m}: fails {fails}; classes mod 24 fully failing: {zero}')
def omega(n):
    k = 0; d = 2
    while d * d <= n:
        if n % d == 0:
            k += 1
            while n % d == 0: n //= d
        d += 1
    return k + (1 if n > 1 else 0)
rows = [l.split() for l in open('data/z52b/pass2/TO1/es_100000.tsv')]
X = []; Y = []
for r in rows:
    p = int(r[0]); cnt = int(r[1])
    X.append((omega(p + 3), omega((p + 1) // 2), omega(p - 1))); Y.append(cnt)
import statistics as st
mean = st.mean(Y)
print('(b) p=1 mod 4 < 1e5 (n=%d): mean #solutions %.3f; zero-solution primes: %d (check 4-sol count, p>5 only)' % (len(Y), mean, sum(1 for y in Y if y == 0)))
for idx, name in enumerate(['omega(p+3)', 'omega((p+1)/2)', 'omega(p-1)']):
    g = {}
    for x, y in zip(X, Y): g.setdefault(x[idx], []).append(y)
    print('  by', name, ' '.join(f'{k}:{st.mean(v):.2f}({len(v)})' for k, v in sorted(g.items()) if len(v) >= 20))
print('(c) filter profile (cols: p total no1mod3 pnx sz chain):')
for l in open('data/z52b/pass2/TO0b/filters_2e4.tsv'):
    a = l.split()
    if a[0] in ('241', '2521', '17', '3', '13', '5'):
        print('  ', ' '.join(a[:6]))
