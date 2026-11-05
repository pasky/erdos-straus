# z57 SYNTH §2.3: test of the *uniform* sufficient form  X(p) >= -(5/(4 pi^2)) L^2  (X = R - M_gen, L = log p) at the primes
# p = 1 (4) in (1e7, 1e8] with R(p) <= 8 (exact R from data/z57/synth/tri_1e8.txt; M_gen from scripts/z56_famdesign_mgen.c,
# long-double sum of exact rational weights, data/z57/synth/mgen_lowR.txt columns: p L2 M0 M0_G Mgen M_G M_K M_G1/15 M0_G1/15).
import math
R = {}
for line in open('data/z57/synth/tri_1e8.txt'):
    t = line.split(); p = int(t[0])
    if p > 10**7 and int(t[1]) <= 8: R[p] = int(t[1])
M = {}
for line in open('data/z57/synth/mgen_lowR.txt'):
    t = line.split()
    if len(t) == 9: M[int(t[0])] = list(map(float, t[1:]))
cV = 5 / (4 * math.pi ** 2)
viol = []; ratios = []
for p in sorted(R):
    if p not in M: continue
    L2, M0, M0G, Mg, MG, MK = M[p][:6]
    X = R[p] - Mg
    ratios.append((R[p] / Mg, p))
    if X < -cV * L2: viol.append((p, R[p], L2, Mg, X, X / L2, Mg / L2))
print(f'primes tested: {len(ratios)} of {len(R)} (R<=8, p in (1e7,1e8]); c_V = 5/(4pi^2) = {cV:.6f}')
print(f'violations of X >= -c_V L^2: {len(viol)}')
for v in viol: print('  p=%d R=%d L2=%.3f Mgen=%.4f X=%.4f X/L2=%.5f Mgen/L2=%.5f margin=%.3f' % (v + ((-v[4] - cV * v[2]),)))
ratios.sort(); print('smallest R/M_gen:', ['%d:%.4f' % (p, r) for r, p in ratios[:5]])
print('Mgen/L2 over tested primes: min %.4f max %.4f' % (min(M[p][3] / M[p][0] for p in R if p in M), max(M[p][3] / M[p][0] for p in R if p in M)))
