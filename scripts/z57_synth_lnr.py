# z57 SYNTH: least quadratic non-residue n_p (prime) at the zero sets of R (14 (★)-zeros), R_G* (38 F4-zeros <= 1e10) and,
# for comparison, p mod 840 and whether p is in Mordell's six square classes mod 840.  Exact (Euler criterion).
# usage: python3 scripts/z57_synth_lnr.py
import sys
def lnr(p):
    q = 2
    while True:
        if all(q % r for r in range(2, int(q ** 0.5) + 1)) and pow(q, (p - 1) // 2, p) == p - 1: return q
        q += 1
star = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281]
F4 = []
for line in open('data/z56/famdesign/zeros_le1e8.txt'):
    if line.startswith('#'): continue
    t = line.split()
    if t[8] == '0': F4.append(int(t[0]))
F4.append(564661441)
mord = {1, 121, 169, 289, 361, 529}
for name, L in (('star', star), ('F4', F4)):
    print(f'# {name}: {len(L)} primes; columns p n_p p%840 mordell')
    for p in L: print(name, p, lnr(p), p % 840, int(p % 840 in mord))
