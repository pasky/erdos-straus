# AGENT_REPORT_O217 — spark relay Y8: the three-squares side of the ES sign and the adelic "continuity of T1" (checkpoint 1)

Branch side-agent/three-squares (merged side-agent/two-fibres first; README conflict resolved by keeping both sides).
Deep file THREE_SQUARES.md; memos BRAINSTORM/y8_*.md (6, indexed); scripts `scripts/y8_*`. **ES is not solved, nor any
infinite case of it.**

## SHARP:
1. **"Near squares" is adelic and is explained exactly by clean levels + one reciprocity constraint.** χ(w) = (A/p) =
   ∏_{r | A}(r/p); call level t *clean* if every prime r | tp + 1 has (r/p) = +1 (⇒ all level-t words χ = +1).
   T1 = "every level clean" (tm² + 1 = 1² + t·m²); **odd n is a square ⟺ every level is clean** (PROVED, trivial).
   The exact constraint ∏_r (r/p)^{v_r(tp+1)} = ((tp+1)/p) = +1 makes a level clean whenever tp + 1 has ≤ 1 lnr-rough
   prime with odd exponent. A coin model (exact signs ≤ 100, fair coins above, conditioned on the constraint) predicts
   the clean-level fraction within ≈ 0.03 in every lnr bucket (without the constraint: off by ×1.6). Archimedean
   distance to squares has NO effect (N₋/N = 0.643–0.647 in all ten deciles, 39 174 primes < 10⁶); lnr does
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
  Prop 3.1, Lemma 3.2 (Mordell = lnr level), Siegel–Weil weighting + circularity (§4.1, Prop 4.3), conic height bound
  and boundary-genus dictionary (§4.2), 3SQ ⇐ and the trivial n ≡ 3 (4) / ℓ ≡ 3 (4) cases.
* EVIDENCE: §2 law and calibrated model; forced-+ removal flattening (N₋/(N − S) ≈ 0.66); clean clusters; lnr-level
  success rates; 3SQ to 10⁶; h(ℓ(w)) = min letter at p = 1009.
* Assessment: asymptotically (Sathe–Selberg + GRH lnr ≪ log²p) each fixed level is clean with probability → 0; the
  near-square hardness is pre-asymptotic per level. No mechanism closes the admissibility gap (B2).

## Answers to the task goals
(a) The correct weighting is N₊ = Σ_w r(T_w, I₃)/ρ₊(w) (ρ₊ = Siegel product with the χ = +1 p-adic factor; r/48
∈ {1,2,3,4}); comparing with |X_p| is circular (Prop 4.3). The "2-adic" failure is equivalently the p-adic one
(Hilbert reciprocity): no new content.
(b) N₊ − N₋ is a function of the non-square pattern of p, via clean levels; F(p − m²) does not exist (flat deciles);
Thm B does not deform: the only obstruction for a single word is at p (Thm A), near-squareness acts on which words
exist, not on embeddability.
(c) Words sit on conic points of height ≤ min letter (observed =); boundary words on height-1 points, i.e. in the
principal (three-squares) genus of −4p. B6 at fixed p.

## Barrier hypotheses violated, and outcome
* "Term-by-term Siegel–Weil" → family lattice count (x, y, t): t is a modulus in the conditions; dead (B2).
* "Archimedean proximity" → adelic proximity: explained (law), but it is a probability statement (B6).
* "Uncleanness" (free, deterministic) → admissibility: only Mordell's congruence cases are free (B1); rest B2.
* "Product of local signs" (χ) → the signs themselves (ℤ³-embeddability): exception-free 3SQ, no new proof power.

## Sparks (not pursued)
* 3SQ residual case n = ℓ·m², single odd-exponent ℓ ≡ 1 (8): does ES-five(ℓ) imply 3SQ(ℓm²) or vice versa (level
  t of ℓm² is a "pseudo-level" tm² of ℓ with weakened congruence A ≡ −1 mod t)? A transfer in either direction
  would be a genuine structural statement.
* Admissibility via composition: if levels t₁, t₂ are unclean with unclean primes r₁, r₂, is there a level built from
  t₁t₂ (Gauss composition of the ideals (A, 1 + √−tp)) where r₁r₂… — composition changes the field ℚ(√−tp); unclear.
* Rigorous average law: Σ_{p ≤ x, pattern P} #clean levels via BV, giving the Sathe–Selberg exponent with the
  reciprocity-constraint correction (would be PROVED on average; B6-limited).
* Clean-level clusters as a predictor of ET-hard primes in general (Type I/II counts), not just the sign ratio.

## Self-review
Not yet run (checkpoint written first at context budget). Numerics re-runnable: commands in THREE_SQUARES §7; big
census files are in /tmp/y8 (not committed).
