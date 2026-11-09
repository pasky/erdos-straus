# z69 MINE: p-intrinsic feature dictionary for primes p = 1 mod 8.
# Usage: uv run --with cypari2 --with sympy python scripts/z69_mine_feat.py <primes.txt> <out.jsonl>
# Per prime p, records (JSON line):
#   a,b   p = a^2 + b^2, a odd, b even (Gaussian; Fermat)
#   c,d   p = c^2 + 2 d^2
#   e,g   p = e^2 - 2 g^2 with g > 0 minimal (then e > 0)
#   u,v   p = u^2 + 3 v^2 if p = 1 mod 3 else null
#   s7    p = s^2 + 7 t^2 if (p/7) = 1 else null
#   hm4   h(-4p), hm8 h(-8p), hp h(Q(sqrt p)) (narrow = wide since N(eps) = -1)
#   np    least quadratic non-residue; nq7 least prime q = 7 mod 8 with (p/q) = -1
#   cf    continued fraction of sqrt(p): a0, period length L, partial quotients (first 12 + middle),
#         Qset = all Q_i (h_{i-1}^2 - p k_{i-1}^2 = (-1)^i Q_i) over one period (capped at 4000 values)
#   (Pell T, U are computed modulo witness data by the scan script, not stored)
import sys, json, cypari2, math
pari = cypari2.Pari(); pari.allocatemem(1 << 30)

def rep(form, p):
    r = pari('qfbsolve(Qfb(%s),%d)' % (form, p))
    return [abs(int(t)) for t in r] if len(r) else None

def cf_sqrt(p, cap=4000):
    a0 = math.isqrt(p); P, Q = 0, 1; a = a0; quots = []; Qs = []
    L = 0
    while True:
        P = a * Q - P; Q = (p - P * P) // Q; a = (a0 + P) // Q
        L += 1; quots.append(a); 
        if len(Qs) < cap: Qs.append(Q)
        if Q == 1: break
    return a0, L, quots, Qs

def feats(p):
    F = {'p': p}
    ab = rep('1,0,1', p); a, b = (ab if ab[0] % 2 else ab[::-1]); F['a'], F['b'] = a, b
    cd = rep('1,0,2', p); F['c'], F['d'] = cd
    # e^2 - 2 g^2 = p : minimal g by search over g (p = 1 mod 8 => representable)
    g = 1
    while True:
        e2 = p + 2 * g * g; e = math.isqrt(e2)
        if e * e == e2: break
        g += 1
    F['e'], F['g'] = e, g
    F['u3'] = rep('1,0,3', p) if p % 3 == 1 else None
    F['s7'] = rep('1,0,7', p) if pow(p, 3, 7) == 1 else None
    F['hm4'] = int(pari('qfbclassno(%d)' % (-4 * p)))
    F['hm8'] = int(pari('qfbclassno(%d)' % (-8 * p)))
    F['hp'] = int(pari('quadclassunit(%d)[1]' % p))
    q = 2
    while pow(q, (p - 1) // 2, p) == 1: q = int(pari('nextprime(%d)' % (q + 1)))
    F['np'] = q
    q = 7
    while not (q % 8 == 7 and pow(p % q, (q - 1) // 2, q) == q - 1): q = int(pari('nextprime(%d)' % (q + 1)))
    F['nq7'] = q
    a0, L, quots, Qs = cf_sqrt(p)
    F['a0'] = a0; F['L'] = L
    F['quots'] = quots[:12] + quots[L // 2 - 1:L // 2 + 2]
    F['Qset'] = sorted(set(Qs))
    return F

if __name__ == '__main__':
    ps = [int(l.split()[0]) for l in open(sys.argv[1]) if l.strip()]
    with open(sys.argv[2], 'w') as fo:
        for p in ps:
            if p > 2 * 10 ** 10:   # CF period too long for the Python loop; skip (Dickson C4 tail)
                continue
            fo.write(json.dumps(feats(p)) + '\n'); fo.flush()
