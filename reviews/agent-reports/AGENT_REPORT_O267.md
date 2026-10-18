# AGENT_REPORT_O267 — Question R: thin-orbit local–global with a reciprocity obstruction as a model for ES

Branch side-agent/question-r (merged side-agent/zaremba-transfer = O266 and side-agent/review-zaremba = R276 first).
Main file `QUESTION_R.md`; memos `BRAINSTORM/z37_*.md` (6, indexed); scripts `scripts/z37_*`.
**ES is not solved; no infinite case is claimed; Question R remains open.** Preprint-dependent statements are CONDITIONAL.

## SHARP:
1. **RS's Kronecker character is the theta multiplier, and that is why Ψ is a semigroup but not a group (Thm 1.5,
   PROVED from the classical theta law).** σ(γ) = (c/d) on Γ₁(4) is multiplicative up to the archimedean square-root
   cocycle w(γ₁, γ₂), and w = 1 on non-negative matrices; Ψ = ker σ on Γ₁(4)_{≥0}; σ does not extend to
   Γ₁(4) = ⟨T, L⁴⟩. This makes RS §10's "the place at infinity" and arXiv:2510.21702's "metaplectic covers" suggestion
   exact for RS's case, and ties T1 to the campaign's positivity/archimedean theme ((J)52, (J)55): squares are the
   support of θ. Spawnable: reciprocity obstructions = kernels of metaplectic multipliers on positive cones (quartic
   HKRS case over ℤ[i]?); is there an ES-side "multiplier" whose kernel is the five-slice set?
2. **Question R reduces exactly to "a Γ̃-numerator over n is a Jacobi non-residue" (Prop 2.1)**, putting RS fat case
   (PROVED, PV), Thm A, Question R, ZQ_M and ES-five on one ladder indexed by |G(n)|. Euler-product main terms cannot
   vanish at squares (Prop 2.2); the reciprocity factor is 1 − ∏_p 1[n ∈ ℚ_p^{×2}] and the twisted term lives at
   denominators q | n. The missing input for growth methods is precisely a χ-twisted gluing count (Hypothesis TG);
   window 3/8 (Weil) vs 1/18 (Shkredov middle step).

## Main results (labels)
* Prop 1.1 (PROVED): ES words ↔ self-levelled matrices [[A, n],[t, A*]] ∈ SL₂(ℤ), A ≡ A* ≡ −1 (mod t).
* Prop 1.2 (PROVED): χ(w) = (2/n)^e J(−t, A_o) — the RS symbol mod the target becomes a character mod 4t of a divisor of
  tn + 1; RS run the same reciprocity the other way (to a character mod the target, summed over a line by PV).
  Cor 1.3: every word at a level t ≡ 3 (4) or 4 | t is a slice word. Checked: 192 283 words, 0 failures.
* Prop 1.4 (PROVED): the (A)3 matrices lie in the a ≡ d ≡ 3 coset of Γ₀(4), where (a/b) = −(c/d); self-levelling forces
  (c/d) = 1 ⇒ (A/n) = −1 ⇒ T1. R276's row-2 exactness (RS Def 2.4 for the slice sets) recorded.
* Prop 2.1, 2.2 (PROVED), CONJECTURE R-main, Hypothesis TG (open), window Assessment.
* §3 reciprocity singular series M_R (EVIDENCE): exact at squares; level factor ∝ τ(N_t) − Σ_{d|N_t} χ_t(d)
  ("divisors minus quadratic-form representations"); explains ≈ 35–55 % of the near-square deficit at levels ≤ 3000
  (generic N₋/M_R = 1.05; m² + K, K ∈ {1, 4, 8, 16, 24}: 0.89–0.97); an L(1, χ_{tK+1}) refinement is refuted
  (Spearman |ρ| ≤ 0.14). The residual is an admissibility (B2) correlation — answers NEAR_SQUARE spark S2 negatively for
  t-side mechanisms.
* §4.1 (PROVED + EVIDENCE): the sign on the k∣t slice is constant iff 4∣k (k ≤ 16): the RS-type invariant does not
  distinguish numerator 4 from 8; their difference is B3.

## Answers to the brief
(1) Exact at the level of Props 1.1–1.4 + R276 row 2; ES slices are *not* a Ψ-orbit sub-family in a useful sense (the
moving level is the obstruction), and the RS invariant equal to ES's T1 sign is the Kronecker symbol of the column (A, n).
(2) Question R open; exact requirements identified (§2: middle-in-Γ ⟺ sign condition; TG; errors). Distance to ES-five:
numerator-set size n^{1−O(κ)} vs log² n — the full B3 gap. (3) Done (§3), partial explanation. (4) No lever on B2 at a
single p; a model and a dictionary, not a route.

## Numerical controls
Odd squares: M_R = 0 and N₋ = 0 at all 684 odd squares in [4·10⁵, 4·10⁶]; no 4∣t word at any odd square ≤ 2·10⁴.
No positive ES claim is made, so no prime-to-10⁶ triple check was required.

## Sparks (not pursued)
* Metaplectic-kernel formulation for HKRS quartic obstructions (Kubota quartic symbol on a positive cone of SL₂(ℤ[i])).
* Two-side (t and u/v) reciprocity model for N₋ — test whether u/v-side cleanliness explains the remaining 7–15 %.
* Hypothesis TG as a stand-alone problem: χ-twisted Kloosterman counts on Cantor sets; maybe provable for *thin
  multiplicatively structured* A (e.g. A closed under a large multiplicative subgroup) where Burgess is replaced by
  subgroup character sums (Bourgain–Glibichuk–Konyagin).
* Density-one Question R via BK machinery for Γ'_n: seems to follow from standard inputs plus the σ-twisted transfer
  operator (I3); worth writing down carefully as a CONDITIONAL theorem.
* The theta interpretation suggests an ES question: is the five-slice sign a value of a multiplier of a half-integral
  weight form on some self-levelled family (e.g. via the u-side Γ₀(4u) structure)?
