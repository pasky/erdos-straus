# R218 — independent hostile review #2 of FF_STERILE_PUSH.md (O216)

Reviewer: R218 (side agent, branch side-agent/review-ff-push-2). Round 1. Written without reading R217.
Scripts: `scripts/review_fs2_*` (from scratch; none of the author's `fs_*` code reused).

Status: IN PROGRESS.

## Summary verdicts

(filled in at the end)

## Defects

(numbered as found)

## Per-claim notes

### Lemma 1.1 (degree identity) — SOUND
Re-derived. (i) is DEPTH_ASPECT Lemma 2.1 (R4) rewritten with m'wC = T^s + v; correct. (ii) is correct, but the E·v detour is
unnecessary: g'v = w + C with w, C monic and q odd gives deg(w + C) = max(a, b) directly (lc 1 or 2), hence y + t = max(a, b)
(m-1 below). (iii) correct (v₁(0) = m'(0)w₁(0)C₁(0) ≠ 0 since s ≥ 3).
*From-scratch check* (`scripts/review_fs2_brute.py`: enumerates all monic (m', w, C) with the T-conditions for every
degree split, solves for v, g' directly from (B), no use of bsE_famcount): asserts y + t = max(a, b), E v = T^s + m'w²,
E'v = T^s + m'C², T² ∥ v (v₁(0) ≠ 0) and gcd(w₁, Tv₁) = 1 for **all** tuples with p = 3, s ≤ 15; p = 5, s ≤ 9;
p = 7, s ≤ 8 — 0 failures. Tuple totals 122 (p = 3, s ≤ 13) + 32 + 28 = 182, matching the document's "182 tuples".

### Lemma 1.2 (loss-free routes) — SOUND
All four reconstructions re-derived; the counts N*(·) are right (v₁ has fixed lc = lc(w + C) and v₁(0) ≠ 0).

### Lemma 1.3 — SOUND (standard).

### Lemma 1.4 (FF Lenstra) — SOUND
Proof re-derived line by line: (L) is exact; Λ-determinant argument: σ₀(u_x u'_y − u_y u'_x) ≡ 0 (mod Q), degree ≤ X + Y =
n − 2ρ < ρ, so all differences are F_q(T)-collinear; b primitive ⇒ α ∈ F_q[T]; b_x = 0 excluded since Y < ρ; the
α-polynomial is non-zero of degree ≤ 2 (α²-coefficient b_x b_y Q, or α-coefficient b_x e₀ when b_y = 0). The trivial cases
(d < ρ; n − d < ρ) need only that σ is a unit mod Q (τ₀ ≡ Fσ₀⁻¹ is then unique), which is a hypothesis.
*Brute force* (`scripts/review_fs2_lemmas.py`, own code): moduli chosen **adversarially** (Q = monic gcd of differences
of 2–3 divisors of F of equal degree, and its divisors, plus random Q), all scalar multiples of divisors included, only
unit classes. See the Lemma 1.5 paragraph for the counts. 0 violations; the bound 2 is attained (ratio 1.0), so the
search does reach the extremal configurations.

### Lemma 1.5 (FF Coppersmith–Howgrave-Graham) — SOUND (statement and finite form); asymptotic remark sketchy
Re-derived: E | F₁ since E is prime to Q; Q f(x₀) ≡ E (mod E) and Q is a unit mod E, so E | f(x₀); E^m | g_i(x₀), h_j(x₀);
the coefficient embedding P ↦ (p_l T^{lX}) is triangular with diagonal degrees (m − i)deg F₁ + iX and (m + j)X, so
deg det ≤ Δ(m, k); exact Siegel pigeonhole gives deg p_l + lX ≤ ⌊Δ/N⌋ < md, so P(x₀) = 0, ≤ m + k roots. Correct.
The asymptotic sentence ("minimising over 1 + τ = X^{−1/2}·… gives √(nX) < d") is garbled (m-2) but is **not used**:
the certification uses only explicit (m, k) pairs. Brute force: 0 violations of the m + k bound (ratio 1.0 attained).

### Lemma 1.6 (route table) — SOUND
Every row re-derived from Lemmas 1.1–1.5 and DEPTH_ASPECT Lemma 2.1: polynomial degrees (s + 2y + z; s − 1 + y; s − 2
(= deg(T^{s−2} + m'w₁²), lc 2 when z + 2a = s); z + 2b − 2; s − 1 − a; a + b − 2), divisor degrees, modulus degrees
(TL': y + z + 1; Tw₁g': a + y; Tm'w₁: a + z; Tv₁: t − 1), the unit property of every class and the coprimality used
for the cofactor versions (R2: F ≡ 1 mod TL'; R4/R4C: common prime would divide T^{s−2}; R5/R10: prime to Tv₁ by
Lemma 1.1(iii)); R3/R3C correctly E-version only. R10: ≤ 2 square roots of a unit modulo each prime power (q odd,
(1 + P)/(1 + P^e) is a 3-group), so ≤ 2^{ω(Tv₁)} = 2·2^{ω(v₁)} classes. The closed form
Σ_{deg v = e, monic} 2^{ω(v)} = q^e(2 + (e − 1)(1 − 1/q)) was verified by brute force for q = 3, 5, 7, e ≤ 5 (14 cases, exact).
*Brute force*: for every pattern hit by a real tuple (p = 3, s ≤ 15; p = 5, s ≤ 9; p = 7, s ≤ 8) the exact count is
≤ the minimum of my own implementation of the 19 rows (`scripts/review_fs2_bounds.py`); 0 violations, max ratio 1.000.
(Caveat: at these tiny p, s most rows are not binding; this is a sanity check, the proof is the derivation above.)
