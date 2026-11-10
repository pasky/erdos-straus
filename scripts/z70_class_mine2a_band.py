# z70 CLASS item 2a on the disjoint band (added after the registration; descriptive): correlation of log W(p) (U7 witness
# count, allwit engine) with the class-group invariants of 2a, overall and within the stratum of l mod 4 (l = least split
# prime of Q(sqrt(-p)); [L] is in the principal genus iff l == 1 (4)).  Fisher z = atanh(r) sqrt(n-3).
import sys, math, gzip, cypari2
from sympy import factorint, jacobi_symbol, isprime
from sympy.ntheory import sqrt_mod
sys.path.insert(0, 'scripts')
from z70_class_mine2 import h_of, form_order, v2, BANDW
pari = cypari2.Pari()
W = {int(l.split()[1]): int(l.split()[2]) for l in gzip.open(BANDW, 'rt') if l.startswith('W')}
rows = []
for p, w in sorted(W.items()):
    h4 = h_of(-4*p); h8 = h_of(-8*p); hp = int(pari.quadclassunit(p)[0]); l = 3
    while not (isprime(l) and jacobi_symbol(-p % l, l) == 1): l += 2
    r = int(sqrt_mod(-p % l, l)); o = form_order(pari.Qfb(l, 2*r, (r*r + p)//l), -4*p, h4, list(factorint(h4)))
    rows.append(dict(lw=math.log(w), v2h4=min(v2(h4), 6), v2h8=min(v2(h8), 6), three4=int(h4 % 3 == 0), three8=int(h8 % 3 == 0),
                     hp1=int(hp == 1), rho_l=math.log(o)/math.log(h4), l4=l % 4))
def corr(R, k):
    n = len(R); x = [r[k] for r in R]; y = [r['lw'] for r in R]
    mx, my = sum(x)/n, sum(y)/n; sx = math.sqrt(sum((a-mx)**2 for a in x)); sy = math.sqrt(sum((b-my)**2 for b in y))
    if sx == 0 or sy == 0: return float('nan'), float('nan')
    c = sum((a-mx)*(b-my) for a, b in zip(x, y))/(sx*sy); return c, math.atanh(c)*math.sqrt(n-3)
print(f"# band B: {len(rows)} primes; mean W {sum(math.exp(r['lw']) for r in rows)/len(rows):.1f}; share l==1(4) {sum(r['l4']==1 for r in rows)/len(rows):.3f}")
for k in ('v2h4', 'v2h8', 'three4', 'three8', 'hp1', 'rho_l'):
    parts = []
    for lab, R in (('all', rows), ('l==1(4)', [r for r in rows if r['l4'] == 1]), ('l==3(4)', [r for r in rows if r['l4'] == 3])):
        c, z = corr(R, k); parts.append(f"{lab} (n={len(R)}): r {c:+.3f} z {z:+.2f}")
    print(f"{k}: " + ' | '.join(parts))
