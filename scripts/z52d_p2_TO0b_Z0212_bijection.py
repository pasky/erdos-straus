"""z52d pass2 TO0b Z0212: exact bijection 8/p = sum 1/x_i  <->  4/p = sum 1/(2x_i) (all denominators even).
Checks per prime p = 1 mod 4 below 30000: #8-solutions (numer census, ordered x<=y<=z) == #all-even 4-solutions (es census col 9)
and the existence sets coincide. Also: #4-solutions with some denominator = 0 mod 8 vs 8-solutions (not an identity; reported)."""
import re
M8 = {}; 
for line in open('data/z52b/pass2/TO0b/numer/numer_m8_N30000.tsv'):
    p, c, E, Mz = map(int, line.split()); M8[p] = c
ce = {}; c8 = {}
for line in open('data/z52b/pass2/TO1/es_100000.tsv'):
    f = line.split()
    p = int(f[0])
    if p < 30000:
        ce[p] = int(f[8]); c8[p] = int(f[5])
ps = sorted(ce)
eq = sum(1 for p in ps if M8[p] == ce[p]); ex = sum(1 for p in ps if (M8[p] > 0) == (ce[p] > 0))
print(f'primes 1 mod 4 < 30000: {len(ps)}; count-equal {eq}; existence-equal {ex}')
mism = [(p, M8[p], ce[p]) for p in ps if M8[p] != ce[p]][:10]
print('mismatches (p, #8sol, #allEven4sol):', mism)
print('#4-solutions with some den = 0 mod 8 >0 but no 8-solution:', [p for p in ps if c8[p] > 0 and M8[p] == 0][:10], ' (c8 counts all-even with den=0 mod 8, so this should be empty if c8>0 <=> 8-sol)')
