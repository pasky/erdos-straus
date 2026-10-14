"""review_fs2_lemmas.py (R218, from scratch): adversarial brute force of FF_STERILE_PUSH
Lemma 1.4 (FF Lenstra: 3 rho > n => <= 2 divisors of degree d in a unit class mod Q; d < rho or n-d < rho => <= 1) and
Lemma 1.5 (FF Coppersmith: (C) => <= m+k divisors) over F_p, p = 3, 5, 7.
Moduli Q are chosen ADVERSARIALLY: Q = monic gcd of differences of 2 or 3 divisors of F of equal degree d (and its
monic divisors), so that many divisors fall into one class; plus random Q. Divisors include all scalar multiples
(the lemmas say "monic or not").
usage: uv run --with python-flint python scripts/review_fs2_lemmas.py p NTRIALS seed"""
import sys, random
from itertools import product, combinations
import flint
sys.path.insert(0, 'scripts')
from review_fs2_bounds import make

p, NTR, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
random.seed(seed)
P = lambda c: flint.nmod_poly(c, p)
cop = make(p)['cop']


def rand_monic(d):
    return P([random.randrange(p) for _ in range(d)] + [1])


def divisors(F):
    lc, fac = F.factor()
    divs = [P([1])]
    for g, e in fac:
        divs = [D * g**i for D in divs for i in range(e + 1)]
    return divs


def monic_divs(G):
    return [D for D in divisors(G) if D.degree() >= 1]


def lemma_bounds(n, d, rho):
    b = []
    if d < rho or n - d < rho:
        b.append(('triv', 1))
    if 3 * rho > n:
        b.append(('L14', 2))
    if d >= rho:
        c = cop(n, d, rho)
        if c:
            b.append(('L15', c))
    return b


stats = {'groups': 0, 'viol': 0, 'tight': {}}
for trial in range(NTR):
    n = random.randint(6, 13)
    # highly factorable F: product of small-degree random factors, sometimes powers / T-adic pieces
    F = P([random.randrange(1, p)])
    while F.degree() < n:
        F *= rand_monic(random.choice([1, 1, 1, 2, 2, 3]))
    n = F.degree()
    md = divisors(F * F.coeffs()[-1]**-1 if False else F)
    lcF = int(F.coeffs()[-1])
    mon = [D for D in md]  # divisors(F) yields monic-times-constant? normalise
    mon = list({tuple(int(c) for c in (D * pow(int(D.coeffs()[-1]), -1, p)).coeffs()): D for D in mon}.values())
    allE = [D * l for D in mon for l in range(1, p)]
    byd = {}
    for E in allE:
        byd.setdefault(E.degree(), []).append(E)
    Qs = set()
    for d, Es in byd.items():
        if len(Es) < 2:
            continue
        for _ in range(30):
            k = random.choice([2, 3])
            if len(Es) < k:
                continue
            S = random.sample(Es, k)
            G = S[1] - S[0]
            for X in S[2:]:
                G = G.gcd(X - S[0])
            if G.degree() >= 1:
                for D in monic_divs(G)[:12]:
                    Qs.add(tuple(int(c) for c in D.coeffs()))
    for _ in range(5):
        Qs.add(tuple(int(c) for c in rand_monic(random.randint(1, n)).coeffs()))
    for Qc in Qs:
        Q = P(list(Qc)); rho = Q.degree()
        if rho < 1:
            continue
        for d, Es in byd.items():
            cl = {}
            for E in Es:
                r = E % Q
                if r.gcd(Q).degree() != 0:     # sigma must be a unit mod Q
                    continue
                cl.setdefault(tuple(int(c) for c in r.coeffs()), []).append(E)
            if not cl:
                continue
            mx = max(len(v) for v in cl.values())
            stats['groups'] += 1
            for name, bd in lemma_bounds(n, d, rho):
                key = name
                stats['tight'][key] = max(stats['tight'].get(key, 0), mx / bd)
                if mx > bd:
                    stats['viol'] += 1
                    print('VIOLATION', name, 'p', p, 'F', F, 'Q', Q, 'd', d, 'count', mx, 'bound', bd)
print(f"p={p} trials={NTR} (Q,d)-groups={stats['groups']} violations={stats['viol']} max count/bound per lemma={stats['tight']}")
