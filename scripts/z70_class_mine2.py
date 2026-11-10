# z70 CLASS item 2 (Z70_CLASS.md §2, pre-registered): class-group structure beyond h vs U7 witnesses.
# 2a  prime-level invariants: v2 h(-4p), v2 h(-8p) (capped at 6), 1[3 | h(-4p)], 1[3 | h(-8p)], 1[h(p) = 1],
#     rho_l = log ord[L1] / log h(-4p) for the prime ideal over the least split prime l of Q(sqrt(-p)).
#     H_train / H_test vs CTRL: two-sample z on means.
# 2b  representation ideal of a witness (f, x, y, z): (f, 1 + sqrt(-yp)) <-> form [f, 2, zy - 1] of disc -4yp
#     (f (zy - 1) = yp + 1).  Exact decoys: same disc, f' == f (8), |f'/f - 1| <= 0.05, gcd(f', 2yp) = 1, same Legendre
#     symbols (f'/q) at the odd primes q | yp, a random root r of r^2 = -yp (f'); 2 decoys per witness.
#     S1 = log ord / log h, S2 = v2(ord), S3 = 1[3 | ord].  Witnesses with yp <= 1e13, <= 8 per prime (uniform).
#     Estimator: per witness real - mean(decoys), averaged per prime; cluster-by-prime z.
# Usage: python scripts/z70_class_mine2.py 2a OUT | 2b SET OUT   (SET = H_train | H_test | CTRL | BAND)
#   BAND (added after the registration, same statistics): 2000 primes of the z69 MINE disjoint band B, seed 7071.
import sys, math, random, gzip
import cypari2
from sympy import factorint, jacobi_symbol, isprime, primerange
from sympy.ntheory import sqrt_mod
pari = cypari2.Pari(); pari.allocatemem(2*10**8)

def v2(x):
    k = 0
    while x % 2 == 0: x //= 2; k += 1
    return k

def h_of(D):
    return int(pari.quadclassunit(D)[0])

def form_order(f, D, h, hfac):
    one = pari.qfbred(pari.Qfb(1, 0, -D//4)) if D % 4 == 0 else None
    o = h
    for q in hfac:
        while o % q == 0 and pari.qfbred(pari.qfbpow(f, o // q)) == one: o //= q
    return o

BANDW = 'data/z70/class/band2000_witnesses.txt.gz'   # 2000 primes of the z69 MINE disjoint band B (allwit engine)
def prime_set(name):
    if name == 'BAND': return [int(l.split()[1]) for l in gzip.open(BANDW, 'rt') if l.startswith('W')]
    base = 'data/z69/mine/'
    return [int(l.split()[0]) for l in open(base + name + '.txt') if l.strip() and not l.startswith('#')]

def part2a(out):
    res = {}
    for name in ('H_train', 'H_test', 'CTRL'):
        rows = []
        for p in prime_set(name):
            h4 = h_of(-4*p); h8 = h_of(-8*p); hp = int(pari.quadclassunit(p)[0])
            l = 3
            while not (isprime(l) and jacobi_symbol(-p % l, l) == 1): l += 2
            r = int(sqrt_mod(-p % l, l)); D = -4*p
            fq = pari.Qfb(l, 2*r, (r*r + p)//l)
            o = form_order(fq, D, h4, list(factorint(h4)))
            rows.append((p, min(v2(h4), 6), min(v2(h8), 6), int(h4 % 3 == 0), int(h8 % 3 == 0), int(hp == 1),
                         math.log(o)/math.log(h4) if h4 > 1 else 0.0))
        res[name] = rows
        with open(out + f'_{name}.tsv', 'w') as fh:
            fh.write('# p v2h(-4p) v2h(-8p) 3|h(-4p) 3|h(-8p) h(p)=1 rho_l\n')
            for r_ in rows: fh.write(' '.join(str(x) for x in r_) + '\n')
    names = ['v2h4', 'v2h8', 'three4', 'three8', 'hp1', 'rho_l']
    lines = []
    for i, nm in enumerate(names):
        def ms(rows):
            v = [r_[i+1] for r_ in rows]; m = sum(v)/len(v); s2 = sum((x-m)**2 for x in v)/(len(v)-1); return m, s2, len(v)
        mc, sc, nc = ms(res['CTRL'])
        zz = []
        for name in ('H_train', 'H_test'):
            m, s2, nn = ms(res[name]); z = (m - mc)/math.sqrt(s2/nn + sc/nc); zz.append((name, m, z))
        lines.append(f"{nm}: CTRL mean {mc:.4f} (n={nc}) | " + ' | '.join(f"{a} mean {m:.4f} z {z:+.2f}" for a, m, z in zz))
    with open(out + '_summary.txt', 'w') as fh:
        fh.write('# z70 CLASS item 2a (registered): H_train / H_test vs CTRL, two-sample z (Welch)\n')
        for l_ in lines: fh.write(l_ + '\n')
    print('\n'.join(lines))

def witnesses(setname):
    fn = BANDW if setname == 'BAND' else 'data/z69/mine/' + ('CTRL' if setname == 'CTRL' else 'H') + '_witnesses.txt.gz'
    keep = set(prime_set(setname)); W = {}; cur = None
    for l in gzip.open(fn, 'rt'):
        t = l.split()
        if t[0] == 'W': cur = int(t[1]) if int(t[1]) in keep else None; continue
        if cur is not None: W.setdefault(cur, []).append(tuple(int(x) for x in t[:4]))
    return W

def decoy(f, y, p, rng):
    yp = y*p; oddq = [q for q in factorint(yp) if q > 2]
    target = [jacobi_symbol(f % q, q) for q in oddq]
    lo, hi = math.ceil(f*0.95), math.floor(f*1.05)
    for _ in range(4000):
        g = rng.randint(lo, hi)
        if g % 8 != f % 8 or g == f or math.gcd(g, 2*yp) != 1: continue
        if [jacobi_symbol(g % q, q) for q in oddq] != target: continue
        roots = sqrt_mod(-yp % g, g, all_roots=True)
        if not roots: continue
        r = rng.choice(sorted(roots))
        if (r*r + yp) % g: continue
        return g, r
    return None

def part2b(setname, out, cap=8, seed=7070):
    rng = random.Random(seed + {'H_train': 1, 'H_test': 2, 'CTRL': 3, 'BAND': 4}[setname])
    W = witnesses(setname)
    dsum = {'S1': [], 'S2': [], 'S3': []}; nwit = 0; ndec_fail = 0
    with open(out, 'w') as fh:
        fh.write('# p f x y z h | real S1 S2 S3 | decoy1 (f r S1 S2 S3) | decoy2\n')
        for p in sorted(W):
            ws = [w for w in W[p] if w[2]*p <= 10**13]
            if not ws: continue
            ws = rng.sample(ws, min(cap, len(ws)))
            per = {'S1': [], 'S2': [], 'S3': []}
            for (f, x, y, z) in ws:
                assert x*y*z - x - z == p and f == x*y - 1 and f*(z*y - 1) == y*p + 1
                D = -4*y*p; h = h_of(D); hf = list(factorint(h))
                def st(fr):
                    o = form_order(fr, D, h, hf)
                    return (math.log(o)/math.log(h) if h > 1 else 0.0, v2(o), int(o % 3 == 0))
                real = st(pari.Qfb(f, 2, z*y - 1))
                decs = []
                for _ in range(2):
                    dd = decoy(f, y, p, rng)
                    if dd is None: break
                    g, r = dd; decs.append((g, r) + st(pari.Qfb(g, 2*r, (r*r + y*p)//g)))
                if len(decs) < 2: ndec_fail += 1; continue
                nwit += 1
                for i, k in enumerate(('S1', 'S2', 'S3')):
                    per[k].append(real[i] - (decs[0][2+i] + decs[1][2+i])/2)
                fh.write(f"{p} {f} {x} {y} {z} {h} | {real[0]:.4f} {real[1]} {real[2]} | " +
                         ' | '.join(f"{g} {r} {a:.4f} {b} {c}" for (g, r, a, b, c) in decs) + '\n')
            if per['S1']:
                for k in per: dsum[k].append(sum(per[k])/len(per[k]))
        lines = []
        for k, v in dsum.items():
            m = sum(v)/len(v); s = math.sqrt(sum((x-m)**2 for x in v)/(len(v)-1)/len(v))
            lines.append(f"{k}: mean(real - decoy) {m:+.4f} ± {s:.4f}  z {m/s if s > 0 else float('nan'):+.2f}")
        fh.write(f"# {setname}: primes {len(dsum['S1'])}, witnesses {nwit}, decoy failures {ndec_fail}\n")
        for l_ in lines: fh.write('# ' + l_ + '\n')
    print(setname, len(dsum['S1']), nwit, ndec_fail); print('\n'.join(lines))

if __name__ == "__main__":
    if sys.argv[1] == '2a': part2a(sys.argv[2])
    else: part2b(sys.argv[2], sys.argv[3])
