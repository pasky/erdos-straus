"""z58 WITNESS: first-firing dynamics in the raw d-form, Mordell classes.
(1) exact Dirichlet density dens(d) of {p in 𝔐 : d fires} (p uniform over 𝔐-compatible units mod lcm(d, 840)),
    E(D) = sum_{d<=D} dens(d) = mean number of firing moduli d <= D;
(2) empirical survival S(D) = P(d_min(p) > D) over 𝔐-primes in (A, B] from the z58_witness_scan output;
compare log S(D) with the Poisson value -E(D) (independence of the events "d fires").
Usage: python3 z58_witness_surv.py A B DMAX scanfiles...   -> prints table."""
import sys, math, bisect
A, B, DMAX = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
SQ = {3: {1}, 5: {1, 4}, 7: {1, 2, 4}}
# divisor lists of m <= DMAX//4 + 1 via sieve
M = DMAX // 4 + 2
divs = [[] for _ in range(M + 1)]
for k in range(1, M + 1):
    for m in range(k, M + 1, k):
        divs[m].append(k)
def phi_sieve(n):
    ph = list(range(n + 1))
    for i in range(2, n + 1):
        if ph[i] == i:
            for j in range(i, n + 1, i):
                ph[j] -= ph[j] // i
    return ph
ph = phi_sieve(DMAX)
E = 0.0; Ecum = {}
grid = [int(round(10 ** (x / 4))) for x in range(2, 4 * int(math.log10(DMAX)) + 1)]
grid = sorted(set(g for g in grid if g <= DMAX))
gi = 0
for d in range(3, DMAX + 1, 4):
    h = (d + 1) // 4
    comp = 0; frac = 1.0
    small = [l for l in (3, 5, 7) if d % l == 0]
    for k in divs[h]:
        c = (-k) % d
        if all((c % l) in SQ[l] for l in small):
            comp += 1
    for l in small:
        frac *= 0.5
    E += comp / (ph[d] * frac)
    while gi < len(grid) and grid[gi] <= d + 3:
        Ecum[grid[gi]] = E; gi += 1
while gi < len(grid):
    Ecum[grid[gi]] = E; gi += 1
# empirical
dm = []
for fn in sys.argv[4:]:
    for line in open(fn):
        if line[0] == '#':
            continue
        f = line.split()
        p = int(f[0])
        if p <= A or p > B or f[2] != '1':
            continue
        d = int(f[3]); dm.append(d if d > 0 else 10 ** 18)
dm.sort(); N = len(dm)
print(f"# 𝔐-primes in ({A},{B}]: N={N}; D, E(D)=sum dens, S(D)=P(d_min>D), -log S, ratio -logS/E, Poisson exp(-E)")
for D in grid:
    k = N - bisect.bisect_right(dm, D)
    S = k / N
    print(f"{D:>9} E={Ecum[D]:8.4f} S={S:.3e} (k={k}) -logS={(-math.log(S) if k else float('inf')):7.3f} "
          f"ratio={(-math.log(S) / Ecum[D] if k and Ecum[D] > 0 else float("nan")):6.3f} exp(-E)={math.exp(-Ecum[D]):.3e}")
