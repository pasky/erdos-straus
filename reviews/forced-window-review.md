# R264 — hostile review of O252 (FORCED_WINDOW.md, BRAINSTORM/z24_*.md)

Reviewer: R264 side agent (branch side-agent/review-forced-window). Reviewed commit: merge of side-agent/forced-window
(O252 checkpoint 1, after self-review R-O252). From-scratch scripts: `scripts/review_r264_*.py` (no author code reused).
Status: IN PROGRESS.

## Summary verdicts

**Lemma 1.1 (parity split) — SOUND.** Re-derived: p ≡ 1 (8), q ≡ 3 (8) ⇒ K odd; (K/q) = (p/q) = (q/p) = −1 ⇒ (c/q) = −1,
t = −c ∈ U_q; δ_s = −ε_s + 2j_s has δ_s ≡ b_s (2), δ_s ≥ −1 ≥ −b_s, and δ_s ≤ b_s + 2e exactly by the j-range, so δ_s ∈ D_s(e).
D_s(e) matches CAP_DOWN Lemma 1.1 via δ_s = c_s − b_s (c_s ≤ 2b_s, or c_s even with overflow (c_s − 2b_s)/2 = i). From scratch
(`review_r264_prop21.py 20000 300`): for every p ≡ 1 (8) ≤ 2·10⁴ and every forced q ≡ 3 (8), q ≤ 300 (4 580 pairs) the least
parity-box cap was found, δ checked in D_s(e), and the ES^{(y,e)} solution x = K, y = pA, z = pKA/d rebuilt with exact rationals
(den z = r², r odd, v_ℓ(r) ≤ e, rad r | y). "Sufficient only" confirmed: p = 241, q = 11 reproduced (W₀ = {1, 5, 9} ∌ 4); 133 of
the 4 580 pairs have parity-cap > 0 although cap(q) = 0.

**Prop 1.2 (Fourier criterion) — SOUND.** Standard; |Σ_{j≤L} e(jθ)| ≤ 1/|sin πθ| ≤ 1/(2‖θ‖) (sin πx ≥ 2x on [0, ½]).
Random test (3 000 boxes in ℤ/n, n odd ≤ 400): criterion fired 59 times, W = G every time. Note the hypothesis "odd order" is
not used. **Prop 1.3 — SOUND** (pigeonhole on the character torus; |W| ≤ ∏(L_i + 1)).

**Prop 2.1 (cap-0 certificates = least-residue events) — SOUND.** Re-derived: m ≤ u + v ≤ uv + 1 ((u−1)(v−1) ≥ 0) < 4uv and
uv ≥ max(u, v) ≥ (u+v)/2 ≥ m/2; converse: gcd(u, r) | gcd(u, u+v) = 1, r ≡ 3 (4), primes of K_r ∤ r unless = p. Exhaustive
from-scratch check (`review_r264_prop21.py`): for every prime p ≡ 1 (4) ≤ 2·10⁴ the three window sets (A) brute-force Type II
solutions 4/p = 1/x + 1/(py′) + 1/(pz′) with m = 4x − p, (B) windows with a cap-0 δ-box certificate, (C) residues
r = (−p mod 4uv) with r | u + v over ALL coprime (u, v), uv < p/2, coincide; all 50 958 certificates satisfy gcd(u,v) = 1,
uv | K, m | u+v, m = (−p mod 4uv), 4uv ≥ 2m. (A) also confirms "cap 0 = honest Type II": every Type II solution has window
m < p and is a box certificate. The "Reading" (no main term for least-residue events) is Assessment and correctly labelled.

**Prop 2.2 (decoupling at cap ≥ 1) — SOUND** (with a MINOR wording point, D2). δ_s = j = b_s + 2i at b_s = 1 gives
i = (j−1)/2; s ∥ K ⟺ 4s | p + q, s² ∤ p + q. The parenthetical "prime factors of Φ_{2j}(s) above 4s² occur" checked:
none for j = 3 (s < 400), and e.g. j = 5: s = 13, q = 2411 > 676; j = 7: s = 3, q = 547 > 36 (`review_r264_misc.py`).


**Thm 3.1 (covering needs a box of window size) — SOUND.** (a) the Jacobi coset of −1 has φ(m)/2 elements (m ≡ 3 (4) is never
a square); (b) 2b+1+e ≤ (2b+1)(e+1), ω(n) ≤ (1+o(1)) log n/log log n, limsup log τ(n²)·log log n/log n = log 3; the o(1)
depends on n only, so the bound is uniform in e as repaired; (c) re-derived: log φ(m) ≥ (θ − o(1)) log p and K ≤ p give
log(3(e+1)) ≥ (θ − o(1)) log log p. The cap-0 statement and "m = p^{2/log log p} is uncoverable" follow (log 3 < 2). Windows
m > 3p: correct but vacuous at cap 0 (Prop 2.1: cap-0 windows are < p).

**Thm 3.2 (CRT in a window interval) — SOUND-AFTER-REPAIRS** (D3). Main statement re-derived: P(y) ≤ h consecutive K contain a
multiple of P(y); gcd(m, p) = 1 as 0 < K < p; F_e ≥ 3(e+3)^{π(y)−1} (s = 2 has no overflow); threshold
log(e+3) ≥ (1+o(1)) log log h. Only the parenthetical about m ≥ h is wrong (D3).

**Cor 3.3 (CRT shortfall) — SOUND as labelled (PROVED inequality + Assessment).** Ratio (A/log 3)·LL : A·LL/log(A·LL)
= log(A log log p)/log 3 ≍ log₃p/log 3 ✓. Random-model count: f(A) = A − (α log α − α + 1) with α = A/log 3 is maximal at α = 3,
A = 3 log 3, f = 2 ✓ (Selberg–Sathe for ω is uniform for α ≤ any fixed constant). Caveat D3: the CRT window need not be ≍ h
(it can be ≍ h/log h); the shortfall factor is unchanged to leading order.

## Defects

(numbered; FATAL / MAJOR / MINOR)
