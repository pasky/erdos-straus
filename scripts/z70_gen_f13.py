# z70 GEN — F1 (odd squares) and F3 (composite (★)-zeros) census: |G_d(n)| for d = 1,2,3,5,7 (small-fibre engine).
import sys, math
sys.path.insert(0, 'scripts')
import z70_gen_core as C
out = open(sys.argv[1], 'w')
# F1: odd squares m^2, m <= 301
bad = 0; cnt = 0
for m in range(3, 302, 2):
    for d in (1, 2, 3, 5, 7):
        if math.gcd(m, d) > 1: continue
        cnt += 1
        if C.solutions(m * m, d): bad += 1; out.write('F1 VIOLATION m=%d d=%d\n' % (m, d))
out.write('F1: odd squares m^2, 3 <= m <= 301, d in {1,2,3,5,7} coprime to m: %d pairs, %d with G nonempty\n' % (cnt, bad))
# F3
comps = [int(l.split()[0]) for l in open('data/z58/screens/composite_zeros_le8e6.txt') if l.strip() and not l.startswith('#')]
nz = {d: 0 for d in (1, 2, 3, 5, 7)}; nzc = {d: 0 for d in (1, 2, 3, 5, 7)}; none = []
for n in comps:
    anyG = False
    for d in (1, 2, 3, 5, 7):
        if math.gcd(n, d) > 1: continue
        nzc[d] += 1
        s = C.solutions(n, d)
        if s: nz[d] += 1; anyG = True
    if not anyG: none.append(n)
out.write('F3: %d composite (★)-zeros; per d: G_d nonempty in %s of %s (coprime) inputs; no d<=7 with G nonempty: %d (first: %s)\n'
          % (len(comps), nz, nzc, len(none), none[:20]))
out.close()
