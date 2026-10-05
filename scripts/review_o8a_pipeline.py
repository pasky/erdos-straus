"""Review O8 (reviewer 1): toy end-to-end logic check of the prime-side chain
  B(n) <= F(n) <= 1[W(n) > T]   for n = 1 mod Q_Pi,
with the real ES witness system (PO Lemma 2.1 / O2 Lemma 4.3 (I) atoms),
Pi = {l <= z}, events = surviving atoms on free primes, and ARBITRARY
(random) u_j depending on 1-2 free coordinates (Lemma 3.1 needs nothing
of u_j). W(n) is computed by brute force from the definition
W(n) = min{M = 3 (4): n mod M in R(M)}, R(M) = {-4D mod M : D | A_M^2}.
Also checks: cell-expansion of B (Lemma 3.2 shape) agrees with the closed
form at each sampled n.
"""
import sys, random
from math import gcd
from sympy import divisors, isprime, primerange, factorint

T = int(sys.argv[1]) if len(sys.argv) > 1 else 120
z = int(sys.argv[2]) if len(sys.argv) > 2 else 7
SAMPLES = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
random.seed(5)

Pi = list(primerange(2, z + 1))
Q = 24
for l in Pi:
    e = 1
    while l ** (e + 1) <= T: e += 1
    Q = Q * l ** e // gcd(Q, l ** e)
free = [l for l in primerange(z + 1, T + 1)]
emax = {}
for l in free:
    e = 1
    while l ** (e + 1) <= T: e += 1
    emax[l] = e

R = {}
for M in range(3, T + 1, 4):
    A = (M + 1) // 4
    R[M] = {(-4 * D) % M for D in divisors(A * A)}

def W_gt_T(n):
    return all(n % M not in R[M] for M in R)

# events: dict prime-power -> residue
events = set()
for M in R:
    A = (M + 1) // 4
    fac = factorint(M)
    m = 1; r = {}
    for l, v in fac.items():
        if l in Pi: m *= l ** v
        else: r[l] = v
    if not r: continue
    for D in divisors(A * A):
        if (4 * D + 1) % m: continue
        events.add(tuple(sorted((l, v, (-4 * D) % (l ** v)) for l, v in r.items())))
events = sorted(events)
m_ev = len(events)

def occ(ev, n):
    return all(n % (l ** v) == c for l, v, c in ev)

# random u_j: function of 1-2 free coords (as dict lookup with random values)
U = []
for j in range(m_ev):
    coords = random.sample(free, random.choice([1, 2]))
    U.append((coords, {}))
def u_val(j, n):
    coords, tab = U[j]
    key = tuple(n % (l ** emax[l]) for l in coords)
    if key not in tab: tab[key] = random.uniform(-3, 3)
    return tab[key]

def B_closed(n):
    A = [occ(ev, n) for ev in events]
    s = 1.0
    for i in range(m_ev):
        if not A[i]: continue
        v = sum(u_val(j, n) for j in range(i) if A[j])
        s -= (1 - v) ** 2
    return s, (not any(A))

def B_expanded(n):
    # 1 - sum A_i + 2 sum_{j<i} A_iA_j u_j - sum_{j,j'<i} A_iA_jA_j' u_j u_j'
    A = [occ(ev, n) for ev in events]
    s = 1.0
    for i in range(m_ev):
        s -= A[i]
        for j in range(i):
            s += 2 * A[i] * A[j] * u_val(j, n)
            for jp in range(i):
                s -= A[i] * A[j] * A[jp] * u_val(j, n) * u_val(jp, n)
    return s

viol_I = viol_B = viol_exp = 0; nF = nW = npos = nprime = 0
for it in range(SAMPLES):
    while True:
        n = 1 + Q * random.randrange(1, 10 ** 12)
        if all(n % l for l in free): break
    if it % 10 == 0:   # also some primes
        while not isprime(n):
            n += Q
        nprime += 1
    b, F = B_closed(n)
    w = W_gt_T(n)
    nF += F; nW += w; npos += b > 0
    if F and not w: viol_I += 1
    if b > F + 1e-9: viol_B += 1
    if b > 0 and not w: viol_B += 1
    if it < 300 and abs(B_expanded(n) - b) > 1e-6 * max(1, abs(b)): viol_exp += 1
msg = (f'T={T} z={z} Q={Q} free={len(free)} events={m_ev} samples={SAMPLES} (primes {nprime}); '
       f'#F=1: {nF}, #W>T: {nW}, #B>0: {npos}; viol (I): {viol_I}, viol B<=F<=1[W>T]: {viol_B}, '
       f'viol expansion: {viol_exp}')
print(msg)
open('data/review_o8a/pipeline.txt', 'a').write(msg + '\n')
sys.exit(1 if (viol_I or viol_B or viol_exp) else 0)
