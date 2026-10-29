"""z50 ncrt §3 toy check of the U-atom family: atoms (k, l, w), k = 1 mod 4, k <= K, l prime in (sqrt X, X],
1 <= w <= W0, 4w | kl+1; class n = -4w mod kl.  Every n in the class with n > kl - 4w has a U-word (t,u,4w).
(toy: w >= 1, so several atoms may share a class mod l; the model counts DISTINCT active classes mod l)
(a) actual fraction of primes p = 1 mod 4, p <= N, hitting no atom, vs the prime-Haar CRT prediction
    E_c prod_l (1 - f_c(l)/(l-1)) with c = p mod L_K uniform over units, and  vs exp(-E mu_c);
(b) mean fibre mass E mu_c and mu/(log X)^2;  (c) controls: odd squares hit no atom.
Usage: uv run --with numpy --with sympy python z50_ncrt_uatoms.py N X K W0"""
import sys, math
import numpy as np
from sympy import primerange, divisors
from math import gcd
N, X, K, W0 = map(int, sys.argv[1:5])
ks = [k for k in range(1, K + 1) if k % 4 == 1]
ls = list(primerange(int(math.isqrt(X)) + 1, X + 1))
atoms = []  # (k, l, w)
for l in ls:
    for k in ks:
        M = k * l
        if (M + 1) % 4: continue
        for w in divisors((M + 1) // 4):
            if w <= W0 and math.gcd(w, k) == 1:
                atoms.append((k, l, w))
print("N", N, "X", X, "K", K, "W0", W0, "atoms", len(atoms))
# (a) actual
sieve = np.ones(N + 1, dtype=bool); sieve[:2] = False
for i in range(2, int(N ** 0.5) + 1):
    if sieve[i]: sieve[i * i::i] = False
P = np.nonzero(sieve)[0]; P = P[(P % 4 == 1) & (P > K * X)]
hit = np.zeros(len(P), dtype=bool)
byM = {}
for k, l, w in atoms: byM.setdefault(k * l, []).append((-4 * w) % (k * l))
for M, res in byM.items():
    tab = np.zeros(M, dtype=bool); tab[res] = True
    hit |= tab[P % M]
actual = 1 - hit.mean()
# (b),(a-model): fibres c mod L_K (units), primes p = 1 mod 4
L = 1
for k in ks: L = L * k // gcd(L, k)
units = [c for c in range(L) if gcd(c, L) == 1]
mus = []; prods = []
for c in units:
    f = {}
    for k, l, w in atoms:
        if (c + 4 * w) % k == 0: f.setdefault(l, set()).add((-4 * w) % l)   # DISTINCT classes mod l
    mus.append(sum(len(v) / l for l, v in f.items()))
    prods.append(math.prod(1 - len(v) / (l - 1) for l, v in f.items()))
Emu = np.mean(mus); model = np.mean(prods); poiss = np.mean(np.exp(-np.array(mus)))
print("primes p=1 mod 4 in (KX, N]:", len(P))
print("actual avoid fraction %.5f | CRT prime-Haar model %.5f | E exp(-mu_c) %.5f" % (actual, model, poiss))
print("E mu_c %.3f, min mu_c %.3f, (log X)^2 = %.2f, E mu/(log X)^2 = %.4f" % (Emu, min(mus), math.log(X) ** 2, Emu / math.log(X) ** 2))
# (c) controls: odd squares
sq = np.arange(1, int(math.isqrt(N)) + 1, 2) ** 2; sq = sq[sq > K * X]
hs = np.zeros(len(sq), dtype=bool)
for M, res in byM.items():
    tab = np.zeros(M, dtype=bool); tab[res] = True
    hs |= tab[sq % M]
print("odd squares in (KX,N] hit by an atom:", int(hs.sum()), "of", len(sq))
for p in [193, 409, 577, 2521, 3361, 5569, 9601, 66529, 8813281]:
    h = [(k, l, w) for k, l, w in atoms if (p + 4 * w) % (k * l) == 0 and p > k * l - 4 * w]
    print("hard prime", p, "atoms hit:", h[:3], "(count %d)" % len(h))
