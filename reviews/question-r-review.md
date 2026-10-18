# R278 — hostile review of O267 (QUESTION_R.md, Question R)

Reviewer: R278 side agent. Merged side-agent/question-r at its tip (README conflict resolved keeping both z36(R276) and z37 rows).
From-scratch scripts: `scripts/review_r278_*.py`. Sources: RS arXiv:2401.01860v3 and arXiv:2510.21702v2 fetched to /tmp (full PDFs, pdftotext).

## Summary verdicts
* **Thm 1.5** (σ = theta multiplier; multiplicative on Γ₁(4)_{≥0}; Ψ = ker σ; no extension to Γ₁(4)): mathematics **SOUND**;
  novelty/label **SOUND-AFTER-REPAIRS** (D1, D2: the semigroup-character statement is already in RS §7.3; the cocycle
  reading is the classical Kubota/Hilbert-symbol fact; "SHARP candidate" is an overclaim).

* **Prop 1.1** (words ↔ self-levelled matrices): **SOUND**.
* **Prop 1.2** (χ(w) = (2/n)^e J(−t, A_o)): **SOUND**.
* **Cor 1.3**: **FATAL as stated for t ≡ 3 (mod 4)** (false; D5) — the 4 | t half and the mod-8 dependence are SOUND.
  Local: nothing downstream uses the t ≡ 3 half, so the document survives after the statement is corrected.
* **Prop 1.4** ((A)3 = opposite Γ₀(4) coset; self-levelling ⇒ (c/d) = 1 ⇒ T1): **SOUND**.

## §1 Props 1.1–1.4 — re-derivation and checks (`scripts/review_r278_dict.py 20000`)
* Prop 1.1: re-derived (AA* = t(tuv − u − v) + 1; converse a = cu − 1, d = cv − 1, u, v ≥ 2 ⟺ a, d ≥ 2c − 1). Checked
  by enumerating *both* sides independently for n ≤ 2·10⁴: 610 533 words, 610 533 matrices (enumerated from the matrix
  side: c ≥ 2, a, d ≡ −1 (c), a, d ≥ 2c − 1, b = (ad − 1)/c ≤ 2·10⁴), sets equal, map injective.
* Prop 1.2: re-derived (r | A_o ⇒ tn ≡ −1 (r) ⇒ (n/r) = (−t/r); reciprocity in n ≡ 1 (4)). 192 283 words with n ≡ 1 (4),
  0 failures (author's count reproduced). Mod-8 determinacy: 76 cells (t, A, n mod 8), 0 ambiguous. I also checked
  why this survives 8 | A (where e is not determined by A mod 8): 8 | A forces t ≡ −n⁻¹ (8), so t ≡ 3 (4) and
  χ = −(2/nt)^e = −1 since nt ≡ 7 (8); for t ≡ 1 (4) and A even, v₂(tn + 1) = 1 so e = 1. So the mod-8 claim is true
  (it is DEDEKIND Cor 4.1 in other coordinates).
* Cor 1.3, t ≡ 3 (mod 4): **false for even A.** For odd t, A_o ≡ −2^{−e} (mod t), so χ = (2/n)^e(A_o/t) =
  −((2/n)(2/t))^e = −(2/nt)^e, which is +1 when e is odd and nt ≡ 3 (8). Counterexample (prime n): w = (3, 5, 17),
  n = 3·5·17 − 5 − 17 = 233 ≡ 1 (8), A = 14, (14/233) = (2/233)(233/7) = (2/7) = +1. Also (3,5,29,401), (3,5,33,457),
  (3,5,41,569), … . Among the 76 163 words with t ≡ 3 (4), n ≡ 1 (4), n ≤ 2·10⁴: 54 564 have A even and **6 364 have
  χ = +1**. This is consistent with DEDEKIND Thm 4.5 (t ≡ 3 (4), u ≡ v ≡ 1 (4) meets none of the five conditions) and
  even with the author's own printed cell table (cells (3,6,1), (7,2,5), (7,6,5) are absent from the χ = −1 list).
  The "proof" covers only odd A, and the "all cells checked" / report line "Checked: 192 283 words, 0 failures" refers
  to the Prop 1.2 formula, not to Cor 1.3.
* Prop 1.4: re-derived line by line: (a/b)(d/b) = ((1 + bc)/b) = 1; (d/b) = (b/d) (b ≡ 1 (4)); (b/d)(c/d) =
  ((ad − 1)/d) = (−1/d) = −1. Self-level: (c_o/d) = (d/c_o)(−1)^{(c_o−1)/2} = (−1/c_o)² = 1 and (2/d)^s = 1 (s = 2 even;
  s ≥ 3 ⇒ d ≡ −1 (8)). Correct. Numerics: (A)3 words t, u, v < 200, n ≡ 1 (4): **480 200** (author's count reproduced),
  0 failures of (t/A*) = 1, (A/n) = −1; plus the general coset law (a/b) = −(c/d) on 20 000 random non-self-levelled
  matrices with 4 | c, a ≡ d ≡ 3, b ≡ 1 (4): 0 failures. "Other coset" = −Γ₁(4) inside Γ₀(4): correct.

## Thm 1.5 — re-derivation and checks
*Re-derivation.* Shimura/Koblitz: for γ ∈ Γ₀(4), θ(γz) = ε_d^{-1}(c/d)(cz+d)^{1/2}θ(z) (principal branch; Shimura's
extension of (c/d) to d < 0). On Γ₁(4), d ≡ 1 (4) so ε_d = 1. Writing j(γ, z) = (c/d)(cz+d)^{1/2}, the chain rule
θ(γ₁γ₂z) = j(γ₁, γ₂z)j(γ₂, z)θ(z) and (c₁γ₂z + d₁)(c₂z + d₂) = c₃z + d₃ give (c₃/d₃) = (c₁/d₁)(c₂/d₂)·w with
w ∈ {±1} continuous, hence constant on ℍ. At z = iy, y → 0⁺: c₂z + d₂ → d₂, c₃z + d₃ → d₃, and
c₁γ₂z + d₁ = (c₃z+d₃)/(c₂z+d₂) → d₃/d₂. So **w = 1 as soon as d₂ > 0 and d₃ > 0** — no condition on c's, b's or d₁.
The author's statement (all entries ≥ 0) is a special case; the proof is correct (the phrase "all three arguments tend
to 0" means the *angles*; fine). The non-extension argument is correct: Γ₁(4) is free on T = R and U = L⁴ (−I ∉ Γ₁(4)),
σ(T) = σ(U) = 1, so any extending homomorphism is trivial, contradicting σ([[5,2],[12,5]]) = (12/5) = −1.

*From-scratch numerics* (`scripts/review_r278_theta.py`):
* (a) theta law evaluated numerically (θ by direct summation, z chosen with Im z = Im γz = 1/|c|) for 400 random
  γ ∈ Γ₁(4) of all sign patterns: factor θ(γz)/(θ(z)√(cz+d)) is ±1 to 1e-6 every time and equals Shimura's (c/d) in
  400/400 (incl. 90 cases with d < 0).
* (b) 20 000 products of random non-negative Γ₁(4) matrices (96 of the 3000-element pool have σ = −1): 0 failures of
  σ(γ₁γ₂) = σ(γ₁)σ(γ₂), 0 failures of (a/b) = (c/d) (b odd).
* (c) 5 000 pairs with c ≥ 0, d > 0 for γ₁, γ₂, γ₁γ₂ but negative a/b entries allowed: principal-branch w = 1 and
  multiplicativity in all 5 000. Broader test (Shimura symbol, any signs): 11 489 pairs with d₂, d₃ > 0, 0 failures;
  among the other 8 511 pairs multiplicativity fails 1 868 times. So the cocycle is exactly the sign of d (Kubota's
  archimedean Hilbert symbol), not "positivity of the matrix".
* (d) U T⁻¹ U T⁻¹ U = [[5,2],[12,5]], σ = −1 ✓. (Its partial product U T⁻¹ = [[1,−1],[4,−3]] has d < 0 — that is where
  w = −1 enters.)

*Novelty / attribution.* RS (arXiv:2401.01860v3, proof of Prop 7.3, p. 20): "Γ₁(4)_{≥0} = Ψ ∪ Ψ′ … If γ ∈ Ψ′, then
γΨ ⊆ Ψ′ and γΨ′ ⊆ Ψ by (3.0.1)". That *is* the statement that σ is a homomorphism Γ₁(4)_{≥0} → {±1} with kernel Ψ;
it also follows in two lines from RS Lemma 3.4 applied to the column (b₂, d₂) plus Lemma 3.1. The identification
(c/d) = theta multiplier on Γ₁(4) is textbook, and the failure of (c/d) to be a character because of an archimedean
cocycle is Kubota (1969) over ℚ. RS §10 themselves already locate the failure in "(−1/x) tracks the sign of x".
arXiv:2510.21702v2 exists (Shi–Shi–Whitehead–Williams-Tracy–Zhang, "The local-global conjecture is false for
generalized circle packings", v2 25 Mar 2026); its §1 sentence is about the superpacking symmetry group SL(2, ℤ[i]):
"perhaps lifting to metaplectic covers of this group would help to explain reciprocity phenomena generally". Quote is
accurate; "Thm 1.5 is an instance of exactly this" is a stretch (different group; Thm 1.5 lifts nothing new).
Neither RS nor 2510.21702 states the theta-multiplier formulation explicitly (grep of full text: no "theta",
"multiplier", "cocycle", "Kubota" in RS; only the one "metaplectic" sentence in 2510.21702), so "not found in RS or
its citers" is literally true, but the content is a classical reformulation, not a SHARP finding.

## Defects
**D1 (MAJOR, attribution/label) — Thm 1.5 and §4.3 item 1, memo z37_theta_multiplier, README z37 row ("SHARP
candidate").** The homomorphism property on Γ₁(4)_{≥0} and Ψ = ker σ are in RS (Prop 7.3 proof via (3.0.1)); the text
presents them as consequences of Thm 1.5. *Repair:* cite RS §7.3/(3.0.1) for multiplicativity; relabel Thm 1.5 as
"PROVED (classical: Shimura/Kubota); reformulation of RS (3.0.1)"; drop "SHARP candidate"; keep only the non-extension
remark and the cocycle reading as the (modest) addition.

**D2 (MINOR, sharpening) — Thm 1.5 proof.** The cocycle is trivial whenever d₂ > 0 and d₃ > 0 (verified above), so the
"archimedean obstruction" is precisely sign changes of the d-entry along a word, which matches RS §10's own example
(R⁴L⁻²: entries "dipped into the negatives"). *Repair:* state the sharper condition; it makes the Reading paragraph
exact rather than suggestive.

**D3 (MINOR, notation) — Thm 1.5.** "Γ₁(4) = ⟨T, L⁴⟩" uses T, which is never defined (header defines R = [[1,1],[0,1]]).
Also say "free on R, L⁴" (−I ∉ Γ₁(4)), which is what makes the non-extension argument one line. *Repair:* T → R.

**D5 (MAJOR — false statement; local) — QUESTION_R §1 Cor 1.3 (line ≈ 51), AGENT_REPORT_O267 "Main results" Cor 1.3
line.** "If t ≡ 3 (mod 4), every word of level t is a slice word" is false (6 364 counterexamples to 2·10⁴; prime
example (3, 5, 17) at n = 233). The report's "Checked: 192 283 words, 0 failures" misattributes the Prop 1.2 check.
*Repair:* "If t ≡ 3 (mod 4) and A is odd (u even), the word is a slice word; for A = 2^e A_o even, χ = −(2/nt)^e, so
+1 exactly when e is odd and nt ≡ 3 (mod 8). If 4 | t, every word is a slice word (DEDEKIND Thm 4.5)." Fix the report
line the same way. Downstream: §4.1 and §4.2 B1 use only the 4 | t half / the mod-8 dependence — unaffected.

**D4 (MINOR) — §5, 2510.21702 bullet.** Their metaplectic remark concerns SL(2, ℤ[i]) for the Apollonian superpacking.
*Repair:* "…suggests (for SL(2, ℤ[i]) and the superpacking) …; Thm 1.5 is the classical SL(2, ℤ) analogue".
