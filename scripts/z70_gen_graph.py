# z70 GEN item 4 — fixed-n solution graphs on the word set T_n = {(x,y,z) >= 1 : xyz - x - z = n} (Z70_LOOSE §3).
# Seeds: Triv_n = words with a letter 1 (always present: divisor words of n+1, Lemma P5).  Certificates C_n (LOOSE cert()).
# Q1: components under the explicit partial maps of z69-z70 (s, tau_xy, tau_yz, mu, mu^s, rho_L, rho_R, rho_C [n <= 3e4]).
# Q2: slice graph (two words adjacent iff they share a coordinate = re-factorisation of n+x, ny+1 or n+z):
#     BFS distance Triv -> C, and for every first-entry edge the slice and the congruence it needs.
import sys, json, collections
import cypari2
pari = cypari2.Pari()
sys.path.insert(0, 'scripts')

def words(n):
    out = []
    for y in range(1, n + 3):
        N = n * y + 1
        for u in pari.divisors(N):
            u = int(u)
            if (u + 1) % y: continue
            v = N // u
            if (v + 1) % y: continue
            x, z = (u + 1) // y, (v + 1) // y
            if x >= 1 and z >= 1: out.append((x, y, z))
    return sorted(set(out))

def cert(w):
    x, y, z = w
    return x % 4 == 0 or y % 4 == 0 or z % 4 == 0 or (x % 4 == 3 and y % 4 == 3) or (z % 4 == 3 and y % 4 == 3)

def swap(w): return (w[2], w[1], w[0])
def tau_xy(w, n):
    x, y, z = w
    if x * y >= 2 and (n + y) % (x * y - 1) == 0: return (y, x, (n + y) // (x * y - 1))
    return None
def tau_yz(w, n):
    t = tau_xy(swap(w), n); return swap(t) if t else None
def mu(w, n):
    x, y, z = w
    if y == 1 and x >= 2 and z >= 2: return (1, x, z - 1)
    if x == 1 and y >= 2: return (y, 1, z + 1)
    return None
def mus(w, n):
    t = mu(swap(w), n); return swap(t) if t else None

def left_orbit(w, n, S):
    # gamma = [[a, n],[c, d]], a = xy-1, c = y, d = zy-1; left unipotent keeps a; words: c' = c mod a (+a), c' | a+1
    x, y, z = w; a = x * y - 1; out = []
    if a <= 0: return [w]
    for cp in (y % a, y % a + a, y % a - a, y % a + 2 * a):
        if cp < 1 or (a + 1) % cp or (1 + n * cp) % a: continue
        dp = (1 + n * cp) // a
        if (dp + 1) % cp: continue
        u = ((a + 1) // cp, cp, (dp + 1) // cp)
        if u in S: out.append(u)
    return sorted(set(out)) or [w]

def rho_L(w, n, S):
    o = left_orbit(w, n, S); o = sorted(o, key=lambda u: u[1]); i = o.index(w); return o[len(o) - 1 - i]
def rho_R(w, n, S):
    return swap(rho_L(swap(w), n, S))

def components(T, edges):
    par = {w: w for w in T}
    def f(w):
        while par[w] != w: par[w] = par[par[w]]; w = par[w]
        return w
    for u, v in edges:
        a, b = f(u), f(v)
        if a != b: par[a] = b
    comp = collections.defaultdict(list)
    for w in T: comp[f(w)].append(w)
    return list(comp.values())

def analyse(n, rhoC=True):
    T = words(n); S = set(T)
    triv = [w for w in T if 1 in w]; C = [w for w in T if cert(w)]
    maps = {'s': lambda w: swap(w), 'txy': lambda w: tau_xy(w, n), 'tyz': lambda w: tau_yz(w, n),
            'mu': lambda w: mu(w, n), 'mus': lambda w: mus(w, n),
            'rL': lambda w: rho_L(w, n, S), 'rR': lambda w: rho_R(w, n, S)}
    if rhoC and n <= 30000:
        from z70_loose_i5 import rho
        rc = rho('C', n); maps['rC'] = rc
    edges = []; used = collections.Counter()
    for nm, f in maps.items():
        for w in T:
            v = f(w)
            if v is not None and v in S and v != w: edges.append((w, v)); used[nm] += 1
    comps = components(T, edges)
    mixed = [c for c in comps if any(1 in w for w in c) and any(cert(w) for w in c)]
    trivcomp_certs = sorted({w for c in mixed for w in c if cert(w)})
    # Q2 slice graph BFS from Triv
    byx = collections.defaultdict(list); byy = collections.defaultdict(list); byz = collections.defaultdict(list)
    for w in T: byx[w[0]].append(w); byy[w[1]].append(w); byz[w[2]].append(w)
    dist = {w: 0 for w in triv}; q = collections.deque(triv); entry = []
    while q:
        w = q.popleft()
        for lab, nb in (('x', byx[w[0]]), ('y', byy[w[1]]), ('z', byz[w[2]])):
            for v in nb:
                if v not in dist:
                    dist[v] = dist[w] + 1; q.append(v)
                    if cert(v) and not cert(w): entry.append((w, v, lab))
    dC = [dist.get(w) for w in C]
    reach = sum(1 for w in T if w in dist)
    return dict(n=n, T=len(T), triv=len(triv), C=len(C), triv_cert=sum(1 for w in triv if cert(w)), moves=dict(used),
                ncomp=len(comps), mixed_components=len(mixed), certs_in_triv_components=len(trivcomp_certs),
                examples=[str(c) for c in trivcomp_certs[:6]],
                slice_reach=reach, slice_dist_C=dict(collections.Counter(dC)),
                entry_examples=[str(e) for e in entry[:6]])

if __name__ == '__main__':
    out = sys.argv[1]
    with open(out, 'a') as fo:
        for n in map(int, sys.argv[2:]):
            r = analyse(n); fo.write(json.dumps(r) + '\n'); fo.flush()
            print(json.dumps(r))
