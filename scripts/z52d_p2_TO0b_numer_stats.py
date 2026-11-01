"""z52d pass2 TO0b: representability table of numerators m (censused in numer/, p<30000) split by p mod 4, and by
prime vs composite m (Z0149, Z0214, Z0123 ladder), plus exact 8<->all-even bijection check (Z0212)."""
import glob, re
D = 'data/z52b/pass2/TO0b/numer/'
M = {}
for f in glob.glob(D + 'numer_m*_N30000.tsv'):
    m = int(re.search(r'numer_m(\d+)_', f).group(1))
    for line in open(f):
        p, cnt, E, Mz = line.split()
        M.setdefault(int(p), {})[m] = int(cnt)
def isprime(n):
    return n > 1 and all(n % q for q in range(2, int(n ** .5) + 1))
allp = sorted(M)
nums = sorted({m for p in M for m in M[p]})
print('m  prime?  rep_all  rep_p1mod4  rep_p3mod4  (fraction of primes 5..30000 with m/p 3-term representable)')
for m in nums:
    a = [p for p in allp if M[p][m] > 0]
    a1 = [p for p in allp if p % 4 == 1 and M[p][m] > 0]; n1 = [p for p in allp if p % 4 == 1]
    a3 = [p for p in allp if p % 4 == 3 and M[p][m] > 0]; n3 = [p for p in allp if p % 4 == 3]
    print(f"{m:3d} {'P' if isprime(m) else 'c'}  {len(a)/len(allp):.4f}  {len(a1)/len(n1):.4f}  {len(a3)/len(n3):.4f}")
# Z0123 ladder: primes where 4 is 'hard' (few solutions) and their membership in E_j = {p: m*2^j in M(p)}
hard = [p for p in allp if 0 < M[p][4] <= 2]
print('ladder: primes with 1-2 solutions for m=4 (below 30000):', len(hard), hard[:20])
for j, m in [(0, 4), (1, 8), (2, 16)]:
    print(f'  m={m}: in M(p) for hard primes: {sum(1 for p in hard if M[p][m]>0)}/{len(hard)}')
# Z0212: exact bijection 8-solutions <-> all-even 4-solutions (y_i = 2x_i); count check requires es full data
# Z0123 explicit: failure sets for the ladder m=4,8,16 (divisor closure forces Fail(16) ⊇ Fail(8) ⊇ Fail(4))
F = {m: [p for p in allp if M[p][m] == 0] for m in (4, 8, 16, 12, 25)}
print('fail counts <30000: m=4:', len(F[4]), ' m=8:', len(F[8]), ' m=16:', len(F[16]), ' m=12:', len(F[12]), ' m=25:', len(F[25]))
print('nesting Fail(8) subset Fail(16):', set(F[8]) <= set(F[16]), '  Fail(4) empty:', len(F[4]) == 0)
for q in (5, 13, 17, 193):
    print('  prime', q, 'fails for m=8?', M[q][8] == 0, ' m=16?', M[q][16] == 0, ' cnt4=', M[q][4], ' cnt8=', M[q][8], ' cnt16=', M[q][16])
print('largest primes in Fail(16):', F[16][-8:])
print('Fail(8) list:', F[8])
