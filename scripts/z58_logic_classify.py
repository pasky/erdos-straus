# z58 LOGIC: classify the R(n)=0 list from z58_logic_zeros.c: prime / odd square / composite; factor structure of
# composite zeros (least prime factor exponent theta = log P^-(n)/log n, omega, Omega, squarefull part, Mordell class).
# usage: uv run --with sympy python scripts/z58_logic_classify.py zeros.txt N > summary
import sys, math
from sympy import factorint, isprime
M = {1, 121, 169, 289, 361, 529}
f, N = sys.argv[1], int(float(sys.argv[2]))
zs = [int(l) for l in open(f)]
rows = []
for n in zs:
    if isprime(n): rows.append((n, 'P', None)); continue
    s = math.isqrt(n)
    if s * s == n: rows.append((n, 'SQ', None)); continue
    rows.append((n, 'C', factorint(n)))
dec = {}
for n, t, fa in rows:
    k = int(math.log10(n)); d = dec.setdefault(k, {'P': 0, 'SQ': 0, 'C': 0, 'CM': 0, 'C2': 0, 'Cbal': 0, 'Csqf': 0})
    d[t] += 1
    if t == 'C':
        if n % 840 in M: d['CM'] += 1
        if sum(fa.values()) == 2 and len(fa) == 2: d['C2'] += 1
        if math.log(min(fa)) / math.log(n) >= 1 / 3: d['Cbal'] += 1
        if all(e == 1 for e in fa.values()): d['Csqf'] += 1
print(f"# R(n)=0 census over n = 1 (4), 5 <= n <= {N}: per decade floor(log10 n)")
print("# cols: decade P SQ C  C_in_Mordell_840  C_semiprime_pq  C_with_minprime>=n^(1/3)  C_squarefree")
for k in sorted(dec):
    d = dec[k]; print(k, d['P'], d['SQ'], d['C'], d['CM'], d['C2'], d['Cbal'], d['Csqf'])
print("# composite zeros with least prime factor >= n^(1/3) (largest 40), and all Mordell-class composite zeros > 1e7:")
bal = [(n, fa) for n, t, fa in rows if t == 'C' and math.log(min(fa)) / math.log(n) >= 1 / 3]
for n, fa in bal[-40:]: print('BAL', n, dict(fa), n % 840, round(math.log(min(fa)) / math.log(n), 3))
for n, t, fa in rows:
    if t == 'C' and n % 840 in M and n > 10**7: print('MORD', n, dict(fa), n % 840)
print("# primes:", [n for n, t, _ in rows if t == 'P'])
