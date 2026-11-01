"""z52d pass2 TO0b Z0107: divisor closure of numerator sets, checked on census output.
Lemma (exact): if m/p = sum of k unit fractions and d | m then (m/d)/p = sum of k unit fractions (divide each denominator by d).
So M(p) is divisor-closed and ES(p) <=> 4 in M(p) <=> M(p) contains a multiple of 4 (with 4|m => m/(m/4)=4).
Check: for every prime p < 30000 and every pair (d, m) of censused numerators with d | m: m in M(p) => m/d in M(p)."""
import sys, glob, re
D = 'data/z52b/pass2/TO0b/numer/'
M = {}
for f in glob.glob(D + 'numer_m*_N30000.tsv'):
    m = int(re.search(r'numer_m(\d+)_', f).group(1))
    for line in open(f):
        p, cnt, E, Mz = line.split()
        M.setdefault(int(p), {})[m] = int(cnt) > 0
nums = sorted({m for p in M for m in M[p]})
viol = []
for p in M:
    for m in nums:
        if M[p].get(m) and m % 2 == 0:
            for d in nums:
                if d > 1 and m % d == 0 and (m // d) in M[p] and not M[p][m // d]:
                    viol.append((p, m, m // d))
print('numerators censused:', nums, ' primes:', len(M))
print('closure violations (m in M, m/d not in M, d|m):', len(viol), viol[:10])
allp = sorted(M)
for m in nums:
    have = [p for p in allp if M[p].get(m)]
    print(f'm={m}: representable for {len(have)}/{len(allp)} primes < 30000')
