"""z52b pass1 U05: Z1537 (exact linear relations among ES count U(n) and arithmetic functions, n≤2000, least-squares residual),
Z1538 (fit of Σ U(n)q^n to divisor-sum basis n≤5000 by least squares), Z1579 (−1-free index-2 subgroups for C≤100),
Z1346/Z1964 (solution graph of 4/p for p≤2e4: components under 'share a denominator' and 'share two denominators')."""
import numpy as np, math
from collections import Counter, defaultdict
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
D = "data/z52b/pass1/U05/2nd/"
U = {}
for l in open(D+"U_2_30000.txt"):
    n, u, nx = map(int, l.split()); U[n] = u
N = 5000
spf = list(range(N+1))
for i in range(2, int(N**.5)+1):
    if spf[i] == i:
        for j in range(i*i, N+1, i):
            if spf[j] == j: spf[j] = i
def fac(n):
    f = Counter()
    while n > 1: q = spf[n]; f[q] += 1; n //= q
    return f
def sigma_k(n, k): return sum(d**k for d in range(1, n+1) if n % d == 0)
def tau(n): return sum(1 for d in range(1, n+1) if n % d == 0)
def r2(n):
    # number of representations as sum of two squares (ordered, signed)
    return sum(1 for a in range(-int(n**.5)-1, int(n**.5)+2) for b in range(-int(n**.5)-1, int(n**.5)+2) if a*a+b*b == n)
ns = list(range(2, 2001))
# Z1537: U(n) vs basis {1, tau, sigma, sigma_2?, r2, n, n^2 ...}: residual relative
def tfun(n): return tau(n)
B = {'1': lambda n: 1.0, 'n': lambda n: n, 'tau': tfun, 'sigma': lambda n: sigma_k(n, 1), 'sigma_2/n': lambda n: sigma_k(n, 2)/n,
     'phi': lambda n: sum(1 for k in range(1, n+1) if math.gcd(k, n) == 1), 'omega': lambda n: len(fac(n)), 'Omega': lambda n: sum(fac(n).values())}
A = np.array([[B[k](n) for k in B] for n in ns], float)
y = np.array([U[n] for n in ns], float)
c, *_ = np.linalg.lstsq(A, y, rcond=None)
res = y - A @ c
log(f"Z1537 least-squares fit of U(n) (n≤2000) on {list(B)}: relative residual norm {np.linalg.norm(res)/np.linalg.norm(y):.3f}, max |res| {np.abs(res).max():.2f} (exact relation would give 0)")
# Z1538: fit U(n) to divisor-sum basis on n≤5000 (need U(n) for n≤5000)
UU = {}
import subprocess
nsl = list(range(2, 5001))
outp = subprocess.run(["/tmp/ucount"], input="\n".join(map(str, nsl)), capture_output=True, text=True).stdout.split("\n")
for l in outp:
    if l: n, u, _ = map(int, l.split()); UU[n] = u
basis_names = ['sigma_1/n', 'sigma_3/n^3', 'tau', 'sigma_1(n/2)', 'sigma_1(n/4)', 'r2(n)/4']
def bas(n, name):
    if name == 'sigma_1/n': return sigma_k(n, 1)/n
    if name == 'sigma_3/n^3': return sigma_k(n, 3)/n**3
    if name == 'tau': return tau(n)
    if name == 'sigma_1(n/2)': return sigma_k(n//2, 1)/n if n % 2 == 0 else 0.0
    if name == 'sigma_1(n/4)': return sigma_k(n//4, 1)/n if n % 4 == 0 else 0.0
    if name == 'r2(n)/4': return r2(n)/4 if n <= 2000 else 0.0
sub = [n for n in range(2, 2001)]
A2 = np.array([[bas(n, b) for b in basis_names[:5]] + [1.0] for n in sub])
y2 = np.array([UU[n] for n in sub], float)
c2, *_ = np.linalg.lstsq(A2, y2, rcond=None)
log(f"Z1538 fit of U(n) (n≤2000) on σ₁/n, σ₃/n³, τ, σ₁(n/2)/n, σ₁(n/4)/n, 1: relative residual {np.linalg.norm(y2-A2@c2)/np.linalg.norm(y2):.3f} (quasi-modular/Eisenstein-type fit would be ~0)")
# Z1579: −1-free index-2 subgroup in (Z/4C)^× for C≤100 (index of smallest subgroup avoiding -1 that is maximal)
def units(m): return [x for x in range(1, m) if math.gcd(x, m) == 1]
ok = 0
for C in range(1, 101):
    m = 4*C; G = units(m); sq = {(x*x) % m for x in G}
    # index-2 subgroups ↔ characters of G/G²; −1 ∉ G² always (−1 is not a square mod 4)
    ok += ((m-1) not in sq)
log(f"Z1579 C≤100: −1 is not a square mod 4C for {ok} of 100 values ⇒ an index-2 subgroup avoiding −1 exists (all C)")
# Z1346/Z1964: solution graph for primes p≡1(4), p≤2e4 from dump
sols = defaultdict(list)
for l in open("/tmp/u05/dump_p2e4.txt"):
    _, n, x, y_, z = l.split(); sols[int(n)].append((int(x), int(y_), int(z)))
def comps(p, mode):
    S = sols[p]; idx = {s: i for i, s in enumerate(S)}
    par = list(range(len(S)))
    def f_(i):
        while par[i] != i: par[i] = par[par[i]]; i = par[i]
        return i
    keyf = (lambda s: set([s[0]]) ) if False else None
    for a in range(len(S)):
        for b in range(a+1, len(S)):
            sa, sb = set(S[a]), set(S[b])
            share = len(sa & sb)
            if (mode == 1 and share >= 1) or (mode == 2 and share >= 2):
                par[f_(a)] = f_(b)
    return len({f_(i) for i in range(len(S))})
cs1 = []; cs2 = []
for p in list(sols)[:200]:
    if p % 4 != 1 or p < 5: continue
    cs1.append(comps(p, 1)); cs2.append(comps(p, 2))
log(f"Z1346/Z1964 solution graph (p≡1(4), first 200 primes ≤2e4): components with 'share ≥1 denominator': median {int(np.median(cs1))}, "
    f"max {max(cs1)}; with 'share ≥2 denominators': median {int(np.median(cs2))}, max {max(cs2)}; graph connected for p with 1 comp: {sum(1 for c in cs1 if c==1)}")
open(D+"fits_out.txt","w").write("\n".join(out)+"\n")
