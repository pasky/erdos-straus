# z70 CLASS item 1: translation profile of X_d(n) = {+-[E]} (G_d(n) = T_d + X) against SYMMETRY-PRESERVING nulls.
# Objects: see z70_class_core.py.  Every good e-ideal E factors into split prime ideals: [E] = sum_q eps_q k_q [Q_q].
# NULL "PS" (prime-swap, registered in Z70_CLASS.md §1.2): a random injection pi on the primes occurring in good norms,
#   pi(q) = q for q <= QFIX and for the translation primes l of L1/L3;  otherwise pi(q) = a uniformly random unused split
#   prime q' with the same genus signature (q' mod 8, Legendre symbols at the odd primes of dn) and |log q' - log q| <= delta
#   (delta = 0.1, widened until >= 8 candidates).  [E]_pi = sum_q eps_q k_q [Q_pi(q)].
#   Preserves exactly: every ideal-level product identity among good ideals (all Lemma-DL pairs), inversion closure,
#   genus coset, norms up to the window.  Randomises: class-level coincidences that are not ideal identities (Lemma CS for
#   d > 1 is one: its pairs sit at the order-2 translation T_d and serve as positive control A2).
# NULL "PSC" (the registered one): PS with the Lemma-CS relations imposed exactly — for each CS pair (E, A-ideal) of a
#   fibre a with 4ad | n-1 the null class of one is derived from the other, [A]_null = T_d - [E]_null (BFS tree over the
#   CS graph; inversion closure kept).  So PSC preserves DL (ideal identities) AND CS (class identities) exactly.
#   For d = 1, T_1 = 0 and CS makes the A-ideal collide with conj(E): C0 is then the positive control.
# NULL "FL" (conjugation flips, s_q = +-1): kept for the record — DEGENERATE: X_s = X whenever all good norms are prime
#   powers (symmetrised set), so it cannot randomise prime-norm coincidences.  Not used for conclusions.
# Usage:  python scripts/z70_class_null.py NULL d R seed  range P0 P1 [mod res]  |  list n1 n2 ...  |  file path [max]
import sys, math, random, bisect
sys.path.insert(0, 'scripts')
from collections import Counter
from sympy import isprime, primerange, jacobi_symbol, factorint
from z69_twist_i17 import reduce
from z70_class_core import Fact, ClassData, solutions, good_ideals

SS = ('K', 'C0', 'M', 'E', 'L1', 'L3', 'A2', 'Mx', 'Ex')
QFIX = 50

def stats(G, Xlist, tl):
    X = list(set(Xlist)); k = len(X)
    C = Counter()
    for x in X:
        nx = G.negd[x]
        for y in X:
            if y != x: C[G.add(y, nx)] += 1
    vals = list(C.values())
    o2 = [v for t, v in C.items() if G.add(t, t) == G.one]
    rest = [v for t, v in C.items() if G.add(t, t) != G.one]
    return dict(K=k, C0=len(Xlist) - k, M=max(vals) if vals else 0, E=sum(v*v for v in vals),
                L1=C.get(tl[0], 0) if tl else 0, L3=sum(C.get(t, 0) for t in tl),
                A2=sum(o2), Mx=max(rest) if rest else 0, Ex=sum(v*v for v in rest))

def translations(C, nmax=3):
    G = C.G; D = C.D
    H = set(G.add(u, u) for u in G.coords.values())
    tl = []; tlp = []; l = 3
    while len(tl) < nmax and l < 10**5:
        if isprime(l) and D % l != 0 and jacobi_symbol(D % l, l) == 1:
            r = next(t for t in range(l) if (t*t - D//4) % l == 0)
            u = G.coords[reduce(l, 2*r, (r*r - D//4)//l)]
            if u in H and u != G.one and u not in tl and G.negd[u] not in tl: tl.append(u); tlp.append(l)
        l += 2
    return tl, tlp

class SplitPrimes:
    def __init__(self, n, d, qmax):
        self.dn = d*n
        self.oddp = sorted(q for q in factorint(d*n) if q > 2)
        self.by = {}
        for q in primerange(3, qmax + 1):
            if (d*n) % q == 0 or jacobi_symbol((-d*n) % q, q) != 1: continue
            self.by.setdefault(self.sig(q), []).append(q)
    def sig(self, q):
        return (q % 8,) + tuple(jacobi_symbol(q % p, p) for p in self.oddp)
    def pool(self, q, delta=0.1, kmin=8):
        L = self.by[self.sig(q)]
        while True:
            lo = bisect.bisect_left(L, q*math.exp(-delta)); hi = bisect.bisect_right(L, q*math.exp(delta))
            if hi - lo >= kmin or (lo == 0 and hi == len(L)): return L[lo:hi]
            delta *= 1.5

def analyse(n, d, R, rng, F, null):
    sols = solutions(n, d, F)
    gi = good_ideals(n, d, F, sols)
    if not gi: return dict(n=n, d=d, k=0)
    # composite n: an ideal norm sharing a prime with dn is not coprime to the discriminant -> not handled; skip n (reported)
    if any(math.gcd(x, d*n) > 1 for (a, b, c, e) in sols for x in (e, 4*a*c*d - 1)): return dict(n=n, d=d, k=-1)
    C = ClassData(n, d); G = C.G
    vk = {}
    for (e, rho) in gi:
        v = tuple(C.ideal_vector(e, rho, F)); vc = tuple((q, -k) for q, k in v)
        vk[v] = 1; vk[vc] = 1                                     # distinct ideals (E and conj E)
    vecs = list(vk); idx = {v: i for i, v in enumerate(vecs)}
    conj = [idx[tuple((q, -k) for q, k in v)] for v in vecs]
    # Lemma CS relations: for a solution with 4ad | n-1, the complement A is a good e-ideal of the same fibre and
    # [ (A, 2ad + sqrt) ] = T_d - [ (e, 2ad + sqrt) ].  Edges i -- j with x_j = T_d - x_i (symmetric).
    adj = {}
    ncs = 0
    for (a, b, c, e) in sols:
        if (n - 1) % (4*a*d) == 0:
            A = 4*a*c*d - 1
            for sg in (1, -1):
                vi = tuple((q, sg*k) for q, k in C.ideal_vector(e, (2*a*d) % e, F))
                vj = tuple((q, sg*k) for q, k in C.ideal_vector(A, (2*a*d) % A, F))
                assert vj in idx, (n, d, a, A)
                i, j = idx[vi], idx[vj]; adj.setdefault(i, set()).add(j); adj.setdefault(j, set()).add(i); ncs += 1
    comp_order = []                      # BFS order: (vertex, parent or None)
    seen = set()
    for r in range(len(vecs)):
        if r in seen: continue
        seen.add(r); comp_order.append((r, None)); qd = [r]
        while qd:
            u = qd.pop()
            for w in adj.get(u, ()):
                if w not in seen: seen.add(w); comp_order.append((w, u)); qd.append(w)
    primes = sorted(set(q for v in vecs for q, _ in v))
    Xobs = [C.vec_class(v) for v in vecs]
    if len(set(Xobs)) < 2: return dict(n=n, d=d, k=len(set(Xobs)))
    tl, tlp = translations(C)
    obs = stats(G, Xobs, tl)
    L1id = 0
    if tl:
        l0 = tlp[0]; byclass = {}
        for v, x in zip(vecs, Xobs): byclass.setdefault(x, []).append(dict(v))
        for x in set(Xobs):
            y = G.add(x, tl[0])
            if y not in byclass: continue
            hit = False
            for v1 in byclass[x]:
                for v2 in byclass[y]:
                    diff = dict(v2)
                    for q, k in v1.items(): diff[q] = diff.get(q, 0) - k
                    diff = {q: k for q, k in diff.items() if k}
                    if len(diff) == 1 and l0 in diff and abs(diff[l0]) == 1: hit = True; break
                if hit: break
            L1id += hit
    # sanity: the observed classes satisfy every CS relation exactly
    for (w, par) in comp_order:
        if par is not None: assert Xobs[w] == G.add(C.Td, G.negd[Xobs[par]]), (n, d, 'CS relation fails')
    if null in ('PS', 'PSC'):
        SP = SplitPrimes(n, d, int(max(primes) * 1.6) + 100)
        fixed = set(q for q in primes if q <= QFIX) | set(tlp)
        movable = [q for q in primes if q not in fixed]
        pools = {q: SP.pool(q) for q in movable}
    acc = {s: [] for s in SS}
    for _ in range(R):
        if null == 'FL':
            s = {q: rng.choice((1, -1)) for q in primes}
            Y = [C.vec_class(v, s) for v in vecs]
        else:
            used = set(fixed); pi = {q: q for q in fixed}
            for q in rng.sample(movable, len(movable)):
                cand = [x for x in pools[q] if x not in used]
                if not cand:
                    cand = [x for x in SP.pool(q, delta=1.0, kmin=len(used) + 8) if x not in used]
                x = rng.choice(cand); used.add(x); pi[q] = x
            if null == 'PS':
                Y = [C.vec_class([(pi[q], k) for q, k in v]) for v in vecs]
            else:                        # PSC: prime swap with the CS relations imposed (derived classes along a BFS tree)
                Y = [None]*len(vecs)
                for (w, par) in comp_order:
                    if Y[w] is not None: continue          # already set as the inverse of its conjugate (keeps X = -X)
                    val = C.vec_class([(pi[q], k) for q, k in vecs[w]]) if par is None else G.add(C.Td, G.negd[Y[par]])
                    Y[w] = val; Y[conj[w]] = G.negd[val]
        st = stats(G, Y, tl)
        for k_ in SS: acc[k_].append(st[k_])
    nullst = {k_: (sum(v)/R, (sum(x*x for x in v)/R - (sum(v)/R)**2) ** 0.5) for k_, v in acc.items()}
    return dict(n=n, d=d, h=G.h, k=obs['K'], nsol=len(sols), NI=len(vecs), obs=obs, null=nullst, L1id=L1id,
                l0=tlp[0] if tlp else None, nprimes=len(primes), ncs=ncs, nmov=len(movable) if null != 'FL' else 0)

def run(null, d, R, nlist, F, seed, out=sys.stdout, tag=''):
    rng = random.Random(seed)
    agg = {s: [0.0, 0.0] for s in SS}; npr = 0; tot = Counter()
    for n in nlist:
        o = analyse(n, d, R, rng, F, null)
        if 'obs' not in o:
            print(f"n={n} d={d} k={o['k']} (skipped)", file=out, flush=True); continue
        npr += 1; ob = o['obs']
        line = f"n={n} d={d} h={o['h']} nsol={o['nsol']} NI={o['NI']} k={o['k']} cs={o['ncs']} mov={o['nmov']}/{o['nprimes']} l0={o['l0']} L1id={o['L1id']} |"
        for s in SS:
            mu, sd = o['null'][s]; line += f" {s} {ob[s]} ({mu:.1f}±{sd:.1f})"
            agg[s][0] += ob[s] - mu; agg[s][1] += sd*sd; tot['obs_'+s] += ob[s]; tot['null_'+s] += mu
        tot['L1id'] += o['L1id']
        print(line, file=out, flush=True)
    Z = lambda a: a[0]/math.sqrt(a[1]) if a[1] > 0 else float('nan')
    print(f"# {tag} null={null} d={d} n analysed {npr}; R={R}; seed={seed}; QFIX={QFIX}; L1 overlaps realised by ideal identities: {tot['L1id']} of {tot['obs_L1']}", file=out)
    print(f"# {tag} null={null} d={d}: " + "; ".join(f"Z_{s} = {Z(agg[s]):+.2f} (obs {tot['obs_'+s]:.0f}, null {tot['null_'+s]:.1f})" for s in SS), file=out, flush=True)
    return {s: Z(agg[s]) for s in SS}

if __name__ == "__main__":
    null = sys.argv[1]; d = int(sys.argv[2]); R = int(sys.argv[3]); seed = int(sys.argv[4]); spec = sys.argv[5:]
    if spec[0] == 'range':
        P0, P1 = int(spec[1]), int(spec[2])
        mod, res = (int(spec[3]), int(spec[4])) if len(spec) > 4 else (8, 1)
        nl = [p for p in primerange(P0, P1) if p % mod == res]
    elif spec[0] == 'file':
        nl = [int(l.split()[0]) for l in open(spec[1]) if l.strip() and not l.startswith('#')]
        if len(spec) > 2: nl = [x for x in nl if x <= int(spec[2])]
    else:
        nl = sorted(set(int(x) for x in spec[1:]))
    F = Fact(max(nl)//3 + 10)
    run(null, d, R, nl, F, seed=seed, tag=' '.join(spec[:3]))
