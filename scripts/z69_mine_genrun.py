# z69 MINE round 2 Part B (pre-registered, data/z69/mine/round2_prereg.md): bounded-complexity candidate-letter
# generators built from p's own data (no witness consulted), each candidate c >= 65 tried in all three U7 roles by the
# exact engine z69_mine_gen.c; size/2-adic-matched decoy generators; K5 Lambda-type bookkeeping.
# Usage: python z69_mine_genrun.py <list file | band:SEED:N> <out.jsonl> [--lo 65]
import sys, json, math, random, subprocess, collections
import cypari2
from sympy import isprime
pari = cypari2.Pari(); pari.allocatemem(1 << 30)
LO = 65
SPLIT_A = False
GENS = ['G', 'N', 'J', 'Q', 'A', 'C']

def rep(form, n):
    try:
        r = pari('qfbsolve(Qfb(%s),%d)' % (form, n))
    except cypari2.PariError:
        return None
    return [abs(int(t)) for t in r] if len(r) else None

def lin(u, v, R=3):
    out = set()
    for al in range(0, R + 1):
        for be in range(-R, R + 1):
            if al == 0 and be <= 0: continue
            if math.gcd(al, abs(be)) != 1: continue
            out.add(abs(al * u + be * v))
    return out

def cf(p):
    a0 = math.isqrt(p)
    if a0 * a0 == p: return [], []
    P, Q, a = 0, 1, a0; Qs = []; qs = []
    while True:
        P = a * Q - P; Q = (p - P * P) // Q; a = (a0 + P) // Q; Qs.append(Q); qs.append(a)
        if Q == 1: break
    return Qs, qs

def conv_den(num, den, cap=200):
    out = []; k0, k1 = 1, 0
    while den and len(out) < cap:
        q, rem = divmod(num, den); k0, k1 = k1, q * k1 + k0; out.append(k1); num, den = den, rem
    return out

def candidates(p):
    G = collections.defaultdict(set)
    reps = {}
    ab = rep('1,0,1', p)
    if ab: reps['ab'] = ab
    cd = rep('1,0,2', p)
    if cd: reps['cd'] = cd
    if p % 8 == 1:
        g = 1
        while g < 10 ** 7:
            e2 = p + 2 * g * g; e = math.isqrt(e2)
            if e * e == e2: reps['eg'] = [e, g]; break
            g += 1
    if p % 3 == 1:
        uv = rep('1,0,3', p)
        if uv: reps['uv'] = uv
    if p % 7 in (1, 2, 4):
        st = rep('1,0,7', p)
        if st: reps['st'] = st
    if 'ab' in reps: G['G'] |= set(reps['ab']) | lin(*reps['ab'])
    for k in ('cd', 'eg', 'uv', 'st'):
        if k in reps: G['N'] |= set(reps[k]) | lin(*reps[k])
    coords = [v for k in reps for v in reps[k]]
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            X, Y = coords[i], coords[j]
            G['J'] |= {X + Y, abs(X - Y), math.gcd(X, Y)}
    Qs, qs = cf(p)
    if Qs:
        L = len(Qs); pos = list(range(0, min(10, L))) + [i for i in range(L // 2 - 4, L // 2 + 3) if 0 <= i < L]
        G['Q'] |= {Qs[i] for i in pos} | {qs[i] for i in pos} | set(sorted(set(Qs))[-10:])
    for k in ('ab', 'cd', 'eg'):
        if k in reps:
            for nm, A in zip(k, reps[k]):
                if A:
                    dens = conv_den(p, A)
                    G['A'] |= set(dens)
                    if SPLIT_A:
                        G['A_' + nm] |= set(dens)
                        if len(dens) >= 2: G['Apen'].add(dens[-2])      # penultimate: k p = +-1 mod A
                        G['Anopen'] |= set(dens[:-2]) | set(dens[-1:])
    try:
        hs = [int(pari('qfbclassno(%d)' % (-4 * p))), int(pari('qfbclassno(%d)' % (-8 * p))), int(pari('quadclassunit(%d)[1]' % p))]
    except cypari2.PariError:
        hs = []
    for h in hs:
        odd = h >> ((h & -h).bit_length() - 1) if h else 0
        G['C'] |= {h, odd} | {h // 2 ** k for k in (1, 2, 3) if h % 2 ** k == 0}
    return {k: sorted(v for v in G[k] if v >= LO) for k in (GENS + (['A_a', 'A_b', 'A_c', 'A_d', 'A_e', 'A_g', 'Apen', 'Anopen'] if SPLIT_A else []))}

def decoy_map(cands, rng):
    m = {}
    for c in cands:
        k = (c & -c).bit_length() - 1; o = c >> k
        lo, hi = max(1, int(o * math.exp(-0.05))), int(o * math.exp(0.05))
        for _ in range(50):
            t = rng.randint(lo, max(lo, hi)) | 1
            if lo <= t <= hi and (t << k) >= LO: break
        else:
            t = o
        m[c] = t << k
    return m

def lam(p, c):
    return any((p + j) % c == 0 or (j * p + 1) % c == 0 for j in range(1, 65))

def main():
    global LO, SPLIT_A, GENS
    if '--splitA' in sys.argv:
        SPLIT_A = True; GENS = GENS + ['A_a', 'A_b', 'A_c', 'A_d', 'A_e', 'A_g', 'Apen', 'Anopen']
    src, outfn = sys.argv[1], sys.argv[2]
    if '--lo' in sys.argv: LO = int(sys.argv[sys.argv.index('--lo') + 1])
    if src.startswith('band:'):
        _, seed, n = src.split(':'); rng0 = random.Random(int(seed)); ps = set()
        while len(ps) < int(n):
            t = 5 * 10 ** 9 + 8 * rng0.randrange(4 * 10 ** 7 // 8) + 1
            if isprime(t): ps.add(t)
        ps = sorted(ps)
    else:
        ps = [int(l.split()[0]) for l in open(src) if l.strip() and not l.startswith('#')]
    rng = random.Random(4242)
    eng = subprocess.Popen(['/tmp/z69mine/gen'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1)
    fo = open(outfn, 'w')
    for p in ps:
        C = candidates(p)
        allc = sorted(set().union(*C.values()))
        dm = decoy_map(allc, rng)
        dec = sorted(set(dm.values()))
        lst = allc + dec
        eng.stdin.write('%d %d %s\n' % (p, len(lst), ' '.join(map(str, lst)))); eng.stdin.flush()
        ok = collections.defaultdict(list)
        while True:
            line = eng.stdout.readline().split()
            if line[0] == 'END': break
            i, role = int(line[1]), int(line[2])
            ok[lst[i]].append((role, int(line[3]), int(line[4]), int(line[5])))
        res = {}
        for g in GENS + ['ALL']:
            cs = allc if g == 'ALL' else C[g]
            real = [c for c in cs if c in ok and ok[c]]
            decs = [dm[c] for c in cs if dm[c] in ok and ok[dm[c]]]
            realNL = [c for c in real if not lam(p, c)]
            res[g] = [len(cs), int(bool(real)), int(bool(decs)), int(bool(realNL))]
        ex = None
        for c in allc:
            if c in ok and ok[c]: ex = [c] + list(ok[c][0]); break
        fo.write(json.dumps({'p': p, 'res': res, 'ex': ex}) + '\n'); fo.flush()
    eng.stdin.close(); eng.wait()

if __name__ == '__main__':
    main()
