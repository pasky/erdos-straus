# R193 — hostile review of SYNTHESIS_SPARKS2.md (O192, spark synthesis II)

Reviewer branch side-agent/review-synthesis-two (merged side-agent/synthesis-two at the O192 checkpoint-1 commit).
From-scratch scripts: `scripts/review_syn2_sqden.py` (§2, plain ℚ arithmetic + own Hilbert symbols),
`scripts/review_syn2_eis.py` (§3, own ℤ[ω] arithmetic, own cubic residue / tame symbols). Neither imports the
author's scripts or `tw_eis.py`; sympy is used only for integer factoring and primality.

## Summary verdicts

| claim | verdict |
|---|---|
| §2 definition of ES^□, Lemma 2.1 | SOUND |
| §2 Prop 2.2 | SOUND (with a slack: Q < r, not just < 2r) |
| §2 quantitative remark (GRH) | SOUND as Assessment |
| §2 Reading 2 "r(p) > log p/2 for a positive proportion of p" | GAP (false as stated; see m2) |

(continued below, section by section)

## §2 — ES^□

**Definition.** S = all odd primes ∤ n; ES^{(S)}'s condition "v_q(z) even when negative, q ∈ S" together with
z ∈ ℤ[1/S] is exactly "z > 0 rational, denominator odd, coprime to n, and a perfect square". Matches the author's
displayed definition. ES ⊂ ES^{(S)} ⊂ ES^□ for finite S ∌ primes of 2n: correct.

**Lemma 2.1 — SOUND.** Re-derived. UNIT_ORBIT_ES Lemma 1.1 is purely local at q (cases (i)–(iii); only (i) uses
evenness of w), so it holds at every q ∤ 2n; a given solution involves finitely many q, so Hilbert reciprocity is
a finite sum. In Cor 1.2 the list of places is: ∞ (½, positivity), 2 (0, z ∈ ℤ_(2)), q ∤ 2n (0: either z q-integral,
Thm 2.1(b), or muted, Lemma 1.1), ℓ | n (variables ℓ-integral since the denominator is prime to n, so Thm 2.1(d)
applies). The class "odd ℓ ∉ S, ℓ ∤ n" is now empty, which is harmless. Nothing else in Cor 1.2 uses finiteness of S.
*Numerics (`review_syn2_sqden.py`, part C).* Brute force of ES^□(m²), x ≤ 2n, y ≤ 30n, every z with odd square
denominator prime to n: n = 9, 25, 49, 81, 225 give 72, 183, 336, 900, 5313 solutions, **0** with Type I/II shape
at every prime of m (n = 225: 3186 have it at one of 3, 5 — consistent, Lemma 2.1 only forbids "every prime").
On every solution I computed all Hilbert symbols (own implementation, ∞, 2, all odd primes): product formula holds,
inv_∞ = ½, inv_2 = 0, inv_q = 0 at every mute q, Σ_{ℓ|n} inv_ℓ = ½ — 0 failures. *Control* (odd **non-square**
denominators prime to n allowed): n = 9: 1597 / 2967 solutions are Type I/II at 3; n = 25: 16120 / 23087 at 5, with
nonzero mute invariants. So the square normalisation is exactly what carries the T1, as claimed.

**Prop 2.2 — SOUND.** Re-derived: n = n₀m² with n₀ > 1 squarefree, n₀ ≡ n ≡ 1 (mod 4) (m² ≡ 1 mod 8); CRT class
a mod 4n₀ with a ≡ 3 (4), (a/n₀) = −1; Dirichlet prime r ≡ a, r ∤ m; (n/r) = (n₀/r) = (r/n₀) = −1 by Jacobi
reciprocity (n₀ ≡ 1 mod 4, both positive odd); (−n/r) = +1, so 4Q² ≡ −n (mod r) is solvable with Q ≢ 0 (r ∤ n).
Of the two roots s, r − s exactly one is odd; adjusting by 2r makes Q prime to n (no prime of n divides 2r).
UNIT_ORBIT_ES Prop 2.1 uses r only through g ≡ 3 (mod 4), g | n + 4Q², and gcd(Q, n) = 1 (the parity step uses
q ∤ a, which follows from q | Q, q ∤ n). Part (a) (n ≡ 3 mod 4, Q = 1, g = n + 4) is UNIT_ORBIT_ES Prop 3.1. ✓.
Remark (MINOR m1): for p prime the odd root is < r, so the proof gives Q < r(p) (and needs no hypothesis p > 2r:
gcd(Q, p) = 1 holds whenever Q < p, and Q < r < p unless r > p, which happens only for tiny p). The stated
"Q < 2r for p > 2r" is true but slack.
*Numerics (part A, B).* All 17 982 primes 5 ≤ p < 2·10⁵ solved by my own implementation of the recipe, every
solution verified exactly (equation in ℚ, x, y ∈ ℤ_{>0}, z > 0 with odd square denominator prime to p, Type II shape);
max r(p) = 79 (p = 141 157), max Q = 77 < r; r(p) = 3, 7, 11, 19, 23, … for 4505, 2254, 1130, 561, 283, … primes
(geometric ratio ½, as for independent characters). n = 825: r = 7, odd roots < 14 are 3, 11 (both share a factor
with 825), least admissible Q = 17 — the self-review counterexample is correct. (The author's 10⁶ figures were not
re-run at 10⁶; the 2·10⁵ range requested by the brief agrees in shape.)

**Quantitative remark (Assessment) — SOUND as labelled.** The least prime r with χ₋₄(r) = −1 and (n₀/r) = −1,
r ∤ n, is ≪ (log n)² under GRH (Bach / Lagarias–Montgomery–Odlyzko-type bound for a prescribed Frobenius in the
biquadratic field ℚ(i, √n₀); not re-derived, standard). Linnik gives n^{O(1)} unconditionally (one could even
cite Burgess-type bounds; immaterial). |S| ≪ π(2r) ≪ (log p)²/log log p ✓.

**Reading 2 — GAP (MINOR m2, an overclaim inside an Assessment).** "primes ≤ log p would need r(p) ≤ log p/2,
which is false for a positive proportion of p by the usual least-non-residue statistics". (i) *False as stated:*
heuristically and by the Chebotarev density of the independent characters, #{p : r(p) > y} / #{p} ≈ 2^{−π(y; 4, 3)},
which → 0 when y = (log p)/2 → ∞; the exceptional set has density 0, not positive density. Numerics (part D):
the fraction of p ≡ 1 (4) with r(p) > (log p)/2 is 0.50 near 10⁴–10⁶ (threshold between 3 and 7… i.e. "r(p) ≥ 7")
and drops to 0.25 near 10⁸ (threshold 9.2, "r(p) ≥ 11"), exactly 2^{−#{3, 7}}. The correct statement is "for
infinitely many p" (e.g. under GRH by a Linnik/CRT construction p ≡ square mod every r ≡ 3 (4) up to y with
log p ≲ (1 + ε)y; unconditionally only with a smaller constant). (ii) *Mechanism-specific:* "would need r(p) ≤ log p/2"
is a statement about the Q < 2r construction. Seed (ii) allows any Q ∈ ⟨primes ≤ log p⟩ with Q ≤ p^{O(1)}, and then r
can be large (one needs only −p/4 ∈ ⟨S⟩² mod r for some prime r ≡ 3 (4)); that question is not answered either way.
*Repair:* replace by "the Q < 2r(p) construction would need r(p) ≤ (log p)/2, which fails for infinitely many p
(density-zero set; Assessment); whether S = {primes ≤ log p} with larger Q ∈ ⟨S⟩ works is OPEN (an Artin-type
question with |S| growing)". The same overstatement sits in the report's SHARP 1 ("weaker than seed (ii)'s log p")
— fine if read as "we only proved the weaker form".
