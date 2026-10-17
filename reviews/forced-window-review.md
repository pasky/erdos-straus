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

**Prop 4.1 (covering ⟺ balanced lattice up to 2; Minkowski floor) — SOUND.** (i) Λ + B_L is closed (Λ discrete, B_L compact),
so μ ≤ 1 gives Λ + B_L = ℝ^S; x − λ ∈ L/2 + B_L is an integer point of ∏[0, L_s] ✓. (ii) ⌊x⌋ ≡ j (mod Λ) with
j ∈ ∏[0, L_s], so x ∈ ∏[0, L_s + 1) + Λ, a translate of (max (L_s+1)/L_s)·B_L ✓ (needs integer L_s ≥ 1, as repaired).
(iii) |W_L| ≤ ∏(L_s+1); k ≤ (1+o(1)) log q/log log q for ∏S ≤ q; ((q−1)/2)^{1/k} ≥ (log q)^{1−o(1)} ✓.

**Prop 4.5 — SOUND.** Index 2: forcing gives some s | K with (s/q) = −1; a non-square g = −u (u ∈ U_q of odd order n′) has
g^{n′} = −1, so −1 ∈ ⟨S⟩ ✓. det Λ_± = |⟨S⟩|/2 ✓. "Probability ≈ τ(K²)/q" is Assessment (order of magnitude; the random-model
value is τ(K²)/|⟨S⟩|).

**Hypothesis W (as repaired) — not false as far as I can determine; not ES in disguise.** I tried to falsify the p-dependent
version: (1) the class a mod 8P (q ≡ 3 (8), q ≡ −p (P)) is reduced (p > y) and does not determine χ_p(q) (p ∤ 8P), so the
candidate set is non-empty under GRH (count re-derived, below). (2) The class can force structure: if p ≡ −1 (mod s) then every
candidate has q ≡ 1 (mod s), so s | |U_q| and an "all generators are s-th powers" obstruction becomes possible; but by Kummer
disjointness (ℚ(ζ_s, S^{1/s}) ∩ ℚ^{ab} = ℚ(ζ_s)) this has relative density ≈ s^{−k} inside the class, and the class contains
≫ φ(8P) log⁴p/log X candidates — no structural kill found (even for p ≡ −1 (mod P), where |U_q| is divisible by P for all
candidates). (3) Unlike the first version, no CRT choice of p empties the candidate set, since X(p) grows with p. W is
stronger than what Thm 4.3 needs (D6: discrete covering W_L = U_q suffices). W ⇒ only
e*(p) ≤ L − 1, never cap 0, so it is not ES in disguise. It is however NOT known to follow from GRH (the P-loss is real: the
unbalanced primes are not Chebotarev-controlled at the needed level) — the document says so.

**Thm 4.3 (CONDITIONAL on W) — SOUND.** Checked every step the brief asked for: p ≡ 1 (8), q ≡ 3 (8) ⇒ K_q odd ✓; P odd,
q ≡ −p (P) ⇒ P | 4K ⇒ P | K ✓; (q/p) = −1 ⇒ q forced, (K/q) = (p/q) = (q/p) = −1 ✓ (valid also for q > p; X(p) can exceed p
when y ≍ log p); q ∤ K (else q | p) ✓; q ∤ P automatic (q | P and P | p + q would give q | p) ✓; Lemma 1.1 with j_s = 0 off P:
δ_s = −ε_s admissible ✓; on P, ⌊(b_s + ε_s)/2⌋ ≥ 1 for b_s ≥ 1, so j_s ≤ L is within cap e = L − 1 ✓; target −c ∈ U_q includes
the odd-exponent primes of the uncontrolled cofactor, and Prop 4.1(i) covers ALL of U_q, so no control of the cofactor is
needed ✓; gcd(K, p) = 1 ✓, so CAP_DOWN Lemma 1.1 gives the ES^{(y,L−1)} solution. From scratch
(`review_r264_thm43.py 300000 20000 1`): 4 356 pairs (hard p ≤ 3·10⁵, every admissible q ≤ 2·10⁴, y = 7), certificate built from
generators 3, 5, 7 only with sides L_min(q), cap ≤ L_min − 1 in all cases, exact ES rebuild.
*GRH count paragraph* — SOUND: χχ_p is non-principal mod 8Pp; under GRH ψ(X, χχ_p) ≪ √X log²(8PpX) (imprimitivity costs
O(log X·ω(8Pp))); with y ≤ log p, log(8PpX) ≤ (5 + o(1)) log p, so √X = √C φ(8P) log²p beats φ(8P)·log²(8PpX) for C absolute ✓.
It is correctly NOT a hypothesis of the theorem.

**Cor 4.4 — SOUND as labelled (CONDITIONAL on W; exponent at random-lattice L is Assessment)**, with D7. Arithmetic re-derived:
y = LL·LLL, log P = (1+o(1))y, log X = 2y(1+o(1)) + 4LL + O(1) = 2y(1+o(1)) since LL = o(y); k = π(y) − 1 ~ y/log y;
exp(log X/k) = y^{2+o(1)} = (log log p)^{2+o(1)} ✓; (log k)^{O(1)} = y^{o(1)} ✓; y ≤ log p ✓. Optimality within the method:
exponent (2 + 4LL/y)·log y forces y/LL → ∞, so 2 + o(1) is the best this W gives; the "2" is the price of X ≈ φ(8P)² (a
Linnik-type X = φ(8P)^{1+ε} would give 1 + ε, matching the floor). The ℓ^∞ covering radius of a Haar-random lattice of
covolume D in dimension k is D^{1/k}·k^{o(1)} (lattice covering density k^{O(log log k)}, Rogers), so the stated
(log k)^{O(1)} is harmless; whether relation lattices of primes behave like random lattices is the Assessment content.
*Floor (log₂p)^{1−o(1)}*: CAP_INTERPOLATION Prop 4.1 checked on main — it is a statement about covering at a single prime window
with generator product ≤ r for p ≡ 1 (mod 8∏_{r≤R} r), matching the use here ✓.
*"GRH alone reaches only exp(O(√(log₂p log₃p)))"* — GAP in wording (D8): this is the best GRH-conditional bound in the campaign
(CAP_INTERPOLATION Thm 4.2(b), whose mechanism is a global count of short-relation primes (3B)^{k+1} log P against the class main
term x/φ(4P) — i.e. the P-loss, as stated), not a barrier theorem about GRH.

## Defects

(numbered; FATAL / MAJOR / MINOR)
