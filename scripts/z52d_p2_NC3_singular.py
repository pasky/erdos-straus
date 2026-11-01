# Z3055: prime factors of the norms N_p = |H_{-4p}(0)| = |prod_{classes} j(tau)| (norm of j(sqrt(-p))), p ≡ 1 (24), p <= P.
# Relevant C := least level C of p (words with t = 4C; from divisors of 4Cp+1, scripts/z52d_p2_NC3_levels.py).
# Test: fraction of prime factors ℓ of N_p with ℓ ≡ -1 (mod 4C), versus the uniform baseline (≈ 1/φ(4C)·#{-1 class}).
# Also: Gross–Zagier: odd primes ℓ | H_{-4p}(0) are non-split in Q(sqrt(-p)) (i.e. (-4p/ℓ) = -1 or ℓ | 4p).
import sys
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
from z52d_p2_NC3_levels import level_words
from collections import Counter
P = int(sys.argv[1]) if len(sys.argv) > 1 else 300
hits = Counter(); base = Counter(); split = Counter(); tot = 0; fac_cnt = 0
for p in L.primes_upto(P):
    if p < 17 or p % 24 != 1: continue
    Hp = pari(f"polclass({-4*p})")
    N = abs(int(pari.polresultant(Hp, pari('x'), 'x')) if False else int(pari.subst(Hp, 'x', 0)))
    f = pari.factor(N)
    C = next((C for C in range(1, 200) if level_words(p, 4*C)), None)
    if C is None: continue
    for ell in [int(x) for x in f[0]]:
        if ell == 2 or ell == p: continue
        fac_cnt += 1
        hits[(ell % (4*C)) == (4*C - 1)] += 1
        split[pari(f"kronecker({-4*p},{ell})") == 1] += 1
        tot += 1
print("p ≡ 1 (24), p <= %d: prime factors (odd) of N_p counted: %d" % (P, tot))
print("  fraction with ℓ ≡ -1 mod 4C (C = least level):", round(hits[True]/tot, 3))
print("  fraction with (-4p/ℓ)=+1 (split):", round(split[True]/tot, 3), " fraction with (-4p/ℓ)=-1 (inert):", round(1-split[True]/tot,3), " (Gross–Zagier: prime factors of H_D(0) are non-split)")
# control: inert odd primes ℓ < 3000 (ℓ ∤ 4p) for the same p and C; fraction ≡ -1 mod 4C
ctrl_hit = ctrl_tot = 0
for p in L.primes_upto(P):
    if p < 17 or p % 24 != 1: continue
    C = next((C for C in range(1, 200) if level_words(p, 4*C)), None)
    if C is None: continue
    for ell in L.primes_upto(3000):
        if ell in (2, p) or (4*p) % ell == 0: continue
        if pari(f"kronecker({-4*p},{ell})") == -1:
            ctrl_tot += 1; ctrl_hit += (ell % (4*C)) == (4*C - 1)
print("control (all inert odd primes ℓ<3000, same C): fraction ≡ -1 mod 4C:", round(ctrl_hit/ctrl_tot, 3), " n=", ctrl_tot)
# stratify by C (least level) and by ℓ-size class (ℓ < 3000 control vs factor sizes)
from collections import defaultdict
st = defaultdict(lambda: [0, 0, 0, 0])
for p in L.primes_upto(P):
    if p < 17 or p % 24 != 1: continue
    C = next((C for C in range(1, 200) if level_words(p, 4*C)), None)
    if C is None: continue
    Hp = pari(f"polclass({-4*p})")
    N = abs(int(pari.subst(Hp, 'x', 0)))
    for ell in [int(x) for x in pari.factor(N)[0]]:
        if ell in (2, p): continue
        st[C][0] += 1; st[C][1] += (ell % (4*C)) == (4*C-1)
    for ell in L.primes_upto(3000):
        if ell in (2, p) or (4*p) % ell == 0: continue
        if pari(f"kronecker({-4*p},{ell})") == -1:
            st[C][2] += 1; st[C][3] += (ell % (4*C)) == (4*C-1)
for C in sorted(st):
    a = st[C]
    if a[0] >= 5:
        print(f"C={C}: factors n={a[0]} frac(-1 mod 4C)={a[1]/a[0]:.3f} | control n={a[2]} frac={a[3]/max(1,a[2]):.3f}")
# genus-character pattern of the prime factors: ((-1/ℓ), (p/ℓ)) for factors vs controls (all C)
pat = Counter(); patc = Counter()
for p in L.primes_upto(P):
    if p < 17 or p % 24 != 1: continue
    Hp = pari(f"polclass({-4*p})")
    N = abs(int(pari.subst(Hp, 'x', 0)))
    for ell in [int(x) for x in pari.factor(N)[0]]:
        if ell in (2, p): continue
        pat[(L.legendre(-1, ell), L.legendre(p, ell))] += 1
    for ell in L.primes_upto(3000):
        if ell in (2, p) or (4*p) % ell == 0: continue
        if pari(f"kronecker({-4*p},{ell})") == -1:
            patc[(L.legendre(-1, ell), L.legendre(p, ell))] += 1
print("genus pattern ((-1/ℓ),(p/ℓ)) factors:", dict(pat))
print("genus pattern controls (inert ℓ<3000):", {k: round(v/sum(patc.values()),3) for k, v in sorted(patc.items())}, " factors:", {k: round(v/sum(pat.values()),3) for k, v in sorted(pat.items())})
