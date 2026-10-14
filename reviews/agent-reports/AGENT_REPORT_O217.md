# AGENT_REPORT_O217 — spark relay Y8: the three-squares side of the ES sign and the adelic "continuity of T1" (checkpoint 1)

> **R224 review note (reviews/three-squares-review.md; no FATAL).** (D5) the "not archimedean" reading holds only at the
> √p scale: at bounded p − m² there is a 6–7σ deficit of χ = −1 words, explained by T1-type levels (p = m² + k,
> tk + 1 = c² ⇒ tp + 1 = tm² + c², level odd-clean when gcd(m, c) = 1; THREE_SQUARES Lemma 1.4); (D6) so the GRH
> "→ 0 per level" Assessment is for random p only; (D12) forced-word removal explains about half of the lnr effect,
> not all (N₋/(N − S) = 0.671 → 0.601 over q = 3 … 13 on all primes in (2·10⁵, 10⁶)); h = min letter is PROVED (Lemma 4.2).

Branch side-agent/three-squares (merged side-agent/two-fibres first; README conflict resolved by keeping both sides).
Deep file THREE_SQUARES.md; memos BRAINSTORM/y8_*.md (6, indexed); scripts `scripts/y8_*`. **ES is not solved, nor any
infinite case of it.**

## SHARP:
1. **"Near squares" is adelic and is well described (EVIDENCE) by clean levels + one exact reciprocity constraint.** χ(w) = (A/p) =
   ∏_{r^e ∥ A}(r/p)^e; call level t *clean* if every prime r | tp + 1 has (r/p) = +1 (⇒ all level-t words χ = +1).
   T1 = "every level clean" (tm² + 1 = 1² + t·m²); **odd n is a square ⟺ every level is clean** (PROVED, trivial).
   The exact constraint ∏_r (r/p)^{v_r(tp+1)} = ((tp+1)/p) = +1 makes a level clean whenever tp + 1 = s·ℓ^e with s
   (lnr−1)-smooth, ℓ prime, e odd. A coin model (exact signs ≤ 100, fair coins above, conditioned on the constraint) predicts
   the clean-level fraction within ≈ 0.03 in every lnr bucket (without the constraint: off by ×1.6). No association
   with archimedean distance to squares was detected (N₋/N = 0.643–0.647 in all ten deciles, 39 174 primes < 10⁶); lnr does
   (0.645 → 0.430). The worst sign-dominance primes are clean-level clusters (7.3/10 small levels clean vs 3.95).
2. **ES-five is the admissible version of the square test.** Uncleanness is free at every non-square (level
   t₀ = −p⁻¹ mod lnr); ES-five ⟺ an unclean divisor can be chosen ≡ −1 (mod t). Mordell's 840 theorem is exactly
   "lnr ≤ 7 ⇒ t₀ | q + 1 ⇒ A = q is admissible" (PROVED); for lnr ≥ 11 the lnr level succeeds ≈ 85 % (stable from
   10⁶ to 10¹¹).
3. **3SQ — exception-free SQ (CONJECTURE, EVIDENCE to 10⁶):** for odd n, every path lattice of X_n embeds in ℤ³
   ⟺ n is a square. At primes = ES-five; ⇐ = Thm B; **105 is not an exception** (its 11 words are χ = +1 but
   ramified at two odd primes). 0 exceptions among all odd n ≤ 10⁶.

## Results (labels)
* PROVED: Lemma 1.1/1.2 (clean levels, reciprocity constraint, rank-one sterility), Prop 1.3 (square test),
  Prop 3.1, Lemma 3.2 (Mordell = lnr level), §4.1 (α₂, α_p vanish together on χ = −1; circularity), conic height bound for
  compatible embeddings and boundary-genus dictionary (§4.2), 3SQ ⇐ and the trivial n ≡ 3 (4) / ℓ ≡ 3 (4) cases.
* EVIDENCE: §2 law and calibrated model; forced-+ removal flattening (N₋/(N − S) ≈ 0.66); clean clusters; lnr-level
  success rates; 3SQ to 10⁶; h(ℓ(w)) = min letter at p = 1009.
* Assessment: asymptotically (Sathe–Selberg + GRH lnr ≪ log²p) each fixed level is clean with probability → 0; the
  near-square hardness is pre-asymptotic per level. No mechanism closes the admissibility gap (B2).

## Answers to the task goals
(a) No exact Siegel–Weil weighting beyond the indicator: on χ = −1 words α₂ and α_p vanish together (the failure is
2-adic AND p-adic, Hilbert reciprocity), so the checkpoint's N₊ = Σ r/ρ₊ was 0/0 and is withdrawn (R-O217);
r/48 ∈ {1,2,3,4,6} for p ≤ 157; comparing any r-weighted count with |X_p| is circular (Prop 4.3).
(b) N₊ − N₋ tracks the non-square pattern of p via clean levels (EVIDENCE + heuristic model); no dependence on
p − m² was detected (flat deciles);
Thm B does not deform: the only obstruction for a single word is at p (Thm A), near-squareness acts on which words
exist, not on embeddability.
(c) Words sit on conic points of height ≤ min letter (compatible embeddings; observed =); boundary words on height-1 points, i.e. in the
principal (three-squares) genus of −4p. B6 at fixed p.

## Barrier hypotheses violated, and outcome
* "Term-by-term Siegel–Weil" → family lattice count (x, y, t): t is a modulus in the conditions; dead (B2).
* "Archimedean proximity" → adelic proximity: explained (law), but it is a probability statement (B6).
* "Uncleanness" (free, deterministic) → admissibility: only Mordell's congruence cases are free (B1); rest B2.
* "Product of local signs" (χ) → the signs themselves (ℤ³-embeddability): exception-free 3SQ, no new proof power.

## Sparks (not pursued)
* 3SQ residual case (all odd-exponent primes ≡ 1 mod 8), in particular n = ℓ·m²: does ES-five(ℓ) imply 3SQ(ℓm²) or vice versa (level
  t of ℓm² is a "pseudo-level" tm² of ℓ with weakened congruence A ≡ −1 mod t)? A transfer in either direction
  would be a genuine structural statement.
* Admissibility via composition: if levels t₁, t₂ are unclean with unclean primes r₁, r₂, is there a level built from
  t₁t₂ (Gauss composition of the ideals (A, 1 + √−tp)) where r₁r₂… — composition changes the field ℚ(√−tp); unclear.
* Rigorous average law: Σ_{p ≤ x, pattern P} #clean levels via BV, giving the Sathe–Selberg exponent with the
  reciprocity-constraint correction (would be PROVED on average; B6-limited).
* Clean-level clusters as a predictor of ET-hard primes in general (Type I/II counts), not just the sign ratio.

## Self-review (R-O217, deep reviewer via `review`)
Verdict "request changes"; confirmed Lemma 1.1/1.2(c), Prop 1.3 (with odd-prime convention), Lemma 3.2 (verified for
p < 10⁴), the u = 1 boundary algebra, y8_embed_sq.c (complete enumeration; rerun to 2·10⁵: 0 exceptions), the 166-word
Thm A check, admissibility counts, the p = 1009 conic run, 105/525. Repairs (all accepted):
* FATAL: Siegel–Weil weighting N₊ = Σ r/ρ₊ was 0/0 (α₂ also vanishes on χ = −1) → withdrawn; §4.1 now negative.
* MAJOR: r ≠ r* (p = 61, (63,1,1)); ideal (A, 1+√−tp) non-invertible for imprimitive forms; weights include 6 → fixed.
* MAJOR: conic script used an arbitrary z with z^⊥ ≅ T_w → now compatible pairs (x × y ≡ x + y mod t); reran p = 61, 1009
  (two orbit labels at p = 1009 changed, heights unchanged).
* MAJOR: "≤ 1 rough odd-exponent prime" overstated; coin model ignored even-exponent rough primes → fixed
  (2^{−s−(k−1)⁺}); recalibrated, numbers moved ≤ 0.002.
* MAJOR: 3SQ reduction to a single odd-exponent prime unproved → restated.
* MAJOR: overclaiming ("no effect", "fully explained", heuristic labels) → softened/labelled.
* MINOR: orbit count r₃(p)/48, prime-2 convention, exponents in χ, script input handling, sample committed
  (data/y8/y8_sample600.txt) → fixed. Census files stay in /tmp/y8 (regenerable by si_census in 3 s).
