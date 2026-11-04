# EVIDENCE check of Lemma 3.3 + Prop 3.4 + Lemma 3.5 constants: exact slice sums (z56slice, C) vs the predicted main term
#   region 1 (o fixed):  ½(1-1/p)(1/o) 𝓛(χ_{D_o}; 2op) log(X/Y),   region 2 (e fixed): ½(1-1/p)(1/e) 𝓛(χ_{E_e}; 2pe') log(X/Y)
# with 𝓛(χ;S) = L(1,χ) ∏_{l|S}(1-χ(l)/l) ∏_{l∤S}(1+χ(l)/l^2) (PARI lfun; Euler product to 1e6).
import subprocess, math, cypari2
pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)
def LL(D, S):
    L1 = float(pari.lfun(D, 1))
    prod = 1.0
    for l in pari.primes(78498):  # primes < 1e6
        l = int(l); c = int(pari.kronecker(D, l))
        prod *= (1 - c / l) if S % l == 0 else (1 + c / l**2)
    return L1 * prod
jobs = []
for p in (100000049, 1000000009):
    for o in (1, 3, 5, 7, 9, 11, 15, 21, 25, 27, 45, 105):
        Y = int(4 * (16 * o * p) ** 0.25); X = p // (8 * o); jobs.append((1, p, o, Y, X))
    for e in (2, 4, 6, 8, 10, 12, 16, 18, 24, 50, 90):
        ep = e
        while ep % 2 == 0: ep //= 2
        Y = int(4 * (64 * ep * p) ** 0.25); X = p // (8 * e); jobs.append((2, p, e, Y, X))
out = subprocess.run(['/tmp/z56slice'], input='\n'.join(' '.join(map(str, j)) for j in jobs), capture_output=True, text=True).stdout.split('\n')
print('reg p          var   Y      X          exact     predicted  ratio')
for line in out:
    if not line.strip(): continue
    t, p, v, Y, X, s = line.split(); t, p, v, Y, X, s = int(t), int(p), int(v), int(Y), int(X), float(s)
    if t == 1:
        o1 = int(pari.core(v)); D = int(pari.coredisc(-p * o1)); pred = 0.5 * (1 - 1 / p) / v * LL(D, 2 * v * p) * math.log(X / Y)
    else:
        k = 0; ep = v
        while ep % 2 == 0: ep //= 2; k += 1
        e1 = int(pari.core(ep)); D = int(pari.coredisc(-p * (2 ** (k % 2)) * e1)); pred = 0.5 * (1 - 1 / p) / v * LL(D, 2 * p * ep) * math.log(X / Y)
    print(f'{t}   {p:10d} {v:4d} {Y:6d} {X:10d} {s:10.5f} {pred:10.5f} {s / pred:7.4f}')
