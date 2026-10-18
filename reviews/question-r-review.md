# R278 — hostile review of O267 (QUESTION_R.md, Question R)

**Repairs applied (author quiet; marked "(R278 repair)"):** QUESTION_R.md — Cor 1.3 restated (D5), Prop 1.2 title (D10),
Thm 1.5 attribution + sharpened cocycle condition + T := R (D1–D3), "squarefree part" (D6), CONJECTURE R-main precise
form (D8), Hypothesis TG quantification (D9), §3 conditioned-model/truncation/look-elsewhere note (D11, D12), 2510.21702
bullet (D4); AGENT_REPORT_O267 (SHARP item 1 downgraded, Cor 1.3 line), memo z37_theta_multiplier title, README z37 rows.
Not applied: D7 (one-clause caveat, left to the author).

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

* **Prop 2.1** (Question R for Γ⁺ ⟺ some Γ̃-numerator over n is a Jacobi non-residue): **SOUND** (it is RS Lemma
  3.4 + Lemma 3.1 verbatim; the Γ⁺ ≠ Γ'_n self-repair is correct).
* **Prop 2.2** (conditional form): **SOUND-AFTER-REPAIRS** (D6 terminology "squarefree kernel"; D7 convergence caveat).
* **CONJECTURE R-main**: **GAP** — not stated precisely (D8).
* **Hypothesis TG**: **GAP / false as literally quantified** (D9: with unrestricted Λ₁, Λ₂ it fails by a planting
  construction; must be restricted to Γ̃-digit sets).
* **§3 reciprocity series M_R** (EVIDENCE): numbers **reproduced exactly** by an independent implementation; label
  SOUND; wording SOUND-AFTER-REPAIRS (D11, D12).
* **§4.1** (sign constant on the k | t slice iff 4 | k, k ≤ 16): **SOUND** (PROVED direction 4 | k ⇒ constant; the
  converse is EVIDENCE for k ≤ 16 and is labelled so in the memo).
* **Labels overall**: one false PROVED item (Cor 1.3 t ≡ 3 half), one overclaimed novelty (Thm 1.5 "SHARP"), two
  imprecise conjecture/hypothesis statements (R-main, TG). Everything else is correctly labelled.

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

## §2 — re-derivation and checks
* Prop 2.1: for γ ∈ Γ̃ ⊆ Γ₁(4)_{≥0}, (x, y) coprime non-negative, y odd: RS Lemma 3.4 (last sentence) gives
  ((ax+by)/(cx+dy)) = (a/b)(x/y), and Lemma 3.1 gives (a/b) = (c/d) = σ(γ). n = cx + dy is odd (4 | c, y, d odd), so the
  Kronecker symbol is Jacobi. Hence (a_γ/n) = −σ(γ), R⁺ = (R + R_σ)/2, R_σ = −Σ(a_γ/n), and R⁺(m²) = 0. Correct; the
  equivalence counts γ's (with multiplicity), which is what R counts. The "Proof" line cites "Ψ′ flips it (Lemma 3.4)"
  — correct in substance (RS §7.3 states γΨ ⊆ Ψ′ for γ ∈ Ψ′).
* Self-review example: S₄ = {γ ∈ Ψ : entries ≤ 4} = {R^k (k ≤ 4), L⁴, I}, so Γ'₄ = ⟨R, L⁴⟩ = Ψ₁; and
  [[49,20],[120,49]] = L²R²L⁴R²L² (computed: `scripts/review_r278_tg.py`), whose L-runs 2, 2 are not multiples of 4,
  so it is not in ⟨R, L⁴⟩ (unique R/L factorisation in SL₂(ℕ)). Correct.
* Prop 2.2(i)–(ii): with the extra hypothesis "arbitrarily large squares are congruence-admissible" stated explicitly
  (RS Def 2.4(1) alone — *some* square residue modulo every m — does not give a single integer square in all admissible
  classes simultaneously; the author correctly adds it as an assumption), (ii) follows from R⁺(m²) = 0. One hidden
  hypothesis: an infinite product of positive local factors can be 0; "positive" must mean "bounded below at the
  admissible squares" (D7). (iii): (a/m²k) = (a/k) for gcd(a, m) = 1 is right, but the conductor is the *squarefree
  part* k of n, not the "squarefree kernel" (= radical; e.g. n = p²q has radical pq, character (·/q)) (D6).
* Item 1 (middle window): (c/n)(x/y) = σ(P)σ(M)σ(S) with σ(P) = σ(S) = 1 and (x/y) = −1 gives σ(M) = −(c/n). Correct.
* Item 3: "mod 129599, [255, 509]² has 11 inverse pairs" reproduced (11). Window arithmetic: twisted box count
  main term N²/n vs Weil error n^{1/2+o(1)} ⇒ N ≥ n^{3/4}, N = n^{2ε} ⇒ ε ≥ 3/8. Correct as a method threshold (and
  correctly labelled so).
* Hypothesis TG: as written, Λ₁, Λ₂ are unquantified ("for sets A = Λ₁ ∔ [N] …"), and "∔" is undefined. If Λ's are
  arbitrary, TG is false: take K quadratic residues C mod a prime p, A = C + [N], B = C⁻¹ + [N]. Then C ⊆ A ∩ B⁻¹,
  each c ∈ C contributes +1, and with K ≍ p/N² the planted points dominate: S ≍ K ≍ |A||B|/p, which beats
  |A||B|N^{−κ}/p + p^{1−κ} as soon as N^{2} < p^{κ}, i.e. ε < κ/4 — inside TG's range ε ≤ ε₀. Numerically
  (`scripts/review_r278_tg.py`, p = 10⁶ + 3): N = 4, K = 15 625: |A||B|/p = 3 719, Σ(c/p) = 15 384; N = 8: 948 vs
  3 872; N = 16: 241 vs 945. So TG is only meaningful for Λ's coming from Γ̃-digit (Cantor) sets, and must say so.
* "Distance to ES" paragraph: Assessment; consistent with R276 (δ = 1/2 with log² excess). No issue.

## §3 and §4.1 — independent recomputation
* `scripts/review_r278_rss.py` re-implements N₋, W, M_R, M₀ from the §3.1 definitions with a *different* factoring
  method (linear sieve over t: q | tn + 1 ⟺ t ≡ −n⁻¹ (q)) and computes (d/n) directly (not via Prop 1.2). Brute-force
  word enumeration agrees on 1009, 9409, 10009, 233, 4001. Agreement with the author's `z37_rss.c` (compiled into /tmp):
  0 per-n mismatches on 219 generic primes (every 10th of the author's 2 183), all 132 (K = 1) and 163 (K = 25) primes,
  69 squares.
* Pooled ratios (`scripts/review_r278_rss_stats.py`, bootstrap SEs, 2 000 resamples):

  | set | #n | N₋/W | N₋/M₀ | N₋/M_R | se | share of deficit removed by M_R | z vs generic |
  |---|---|---|---|---|---|---|---|
  | generic (1/10 sample) | 219 | 0.733 | 1.052 | 1.042 | 0.013 | — | — |
  | K = 1 | 132 | 0.722 | 0.885 | 0.968 | 0.016 | 56 % | 3.7 |
  | K = 4 | 131 | 0.700 | 0.889 | 0.956 | 0.014 | 47 % | 4.6 |
  | K = 16 | 134 | 0.643 | 0.868 | 0.920 | 0.013 | 33 % | 6.8 |
  | K = 24 | 76 | 0.568 | 0.790 | 0.891 | 0.020 | 42 % | 6.5 |
  | K = 25 | 163 | 0.749 | 1.018 | 0.999 | 0.013 | — | 2.4 |
  | squares (1/10) | 69 | 0 | 0 | M_R = 0 | | | |

  The family rows coincide with the author's table to the printed digits; shares 33–56 % vs the author's 33–54 % (the
  difference is only my 1/10 generic baseline, 1.042 vs 1.046). With the author's full generic set (SE ≈ 0.004) the
  K = 25 residual is (1.046 − 0.999)/√(0.013² + 0.004²) ≈ 3.4σ, as stated; note it is the most extreme of 15
  families, so the look-elsewhere-corrected significance is ≈ 2.5σ (two-sided p ≈ 7·10⁻⁴ × 15 ≈ 0.01).
  M₀/W at squares: 1.10 on the full 684-square set (author's value, recomputed with their binary on my list), 1.05 on my
  1/10 subsample — sampling variation only.
* Truncation: levels t ≤ 3000 capture ≈ 85 % of words at n ≈ 10⁶ (all-levels brute force: n = 1 000 033: 128 words,
  110 at t ≤ 3000; 1 000 037: 112/98; 1 000 081: 84/70). The table's "N₋" is the truncated count — stated in the
  heading, but the column label invites reading it as the five-slice count.
* §3.1 example t = 7, n = 149: N = 1044 = 2²·3²·29, range [13, 80], χ = −1 range divisors 18, 58, both with e = 1 and
  class −2⁻¹ ≡ 3 (mod 7) where J(−7, a) = (3/7) = −1 ≠ s = +1, so ρ_R = 0 ✓; τ = 18 ✓; S_t = 2 only if the
  2-factor uses (2/149) = −1 (i.e. S_t is the sum of (d/n), not of the conductor-4t character, which would give 6).
  §3.3 example p = 37, word (3, 3, 5), A = 8: (8/37) = −1 ✓.
* §4.1 (`scripts/review_r278_ksign.py 20000`): sign constant on the k | t slice exactly for k ∈ {4, 8, 12, 16} among
  2 ≤ k ≤ 16 ✓; 215 primes p ≡ 1 (4) < 2·10⁴ without an 8 | t word, first 5, 13, 17, 29 ✓; 241 has neither a 4 | t nor
  an 8 | t word ✓. Identity k/n = 1/(abc) + 1/(acn) + 1/(bcn) for kabc − a − b = n ✓.

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

**D6 (MINOR) — Prop 2.2(iii) and the following Assessment sentence.** "squarefree kernel" should be "squarefree part"
(n = m²k, k squarefree). *Repair:* replace both occurrences.

**D7 (MINOR, hidden hypothesis) — Prop 2.2(i).** "positive on all admissible classes ⇒ positive at admissible m²"
needs the Euler product to converge to a value bounded below on the admissible squares (otherwise R⁺(m²) = 0 is not in
contradiction with ~ c𝔖 n^{2δ−1}). *Repair:* add "with ∏_p σ_p(n) ≫ 1 uniformly on admissible n (as for BK-type
singular series, where σ_p = 1 + O(p^{−2}) for p ∤ qn)".

**D8 (MAJOR, precision) — CONJECTURE R-main.** (a) The normalisation is missing: R depends on both n and the height cutoff
X; the asymptotic should be for n ∈ [X/2, X] (or n ≍ X) with X → ∞. (b) n is always odd here (4 | c, y odd), so "D =
the finite set of 2-adic square classes" and "RS Table 1 … 2-adic variants" are vacuous or refer to other seed types;
for the stated setting the factor is simply 1 − 1_□(n). (c) "𝔖(n)" and c_Γ: of Γ̃ or of Γ⁺? (Γ⁺ = ker σ|Γ̃ is not a
congruence condition, so its reductions mod q presumably coincide with Γ̃'s — should be stated.) (d) Restrict to n in
the admissible classes of Γ⁺ (else 𝔖 = 0 and the statement is vacuous anyway). (e) The heuristic itself assumes the full
asymptotic R(n) ~ c𝔖 n^{2δ−1} for Γ̃ (a pointwise local–global statement not known for any thin semigroup); say
"conditional on the corresponding conjecture for Γ̃". *Repair:* restate as: "Assume R(n) ~ c_Γ̃ 𝔖_Γ̃(n) X^{2δ−1}
for admissible n ≍ X. Conjecture: R⁺(n) = ½ c_Γ̃ 𝔖_Γ̃(n) X^{2δ−1}(1 − 1_□(n) + o(1)) for admissible n ≍ X."

**D9 (MAJOR, precision; false as literally quantified) — Hypothesis TG (§2 item 4, memo z37_twisted_gluing).** With
unrestricted Λ₁, Λ₂ TG is refuted by planting (above; numerics in `scripts/review_r278_tg.py`). *Repair:* quantify Λ_i
as the residue sets produced by Γ̃-prefixes/suffixes (Shkredov's A, B for the digit set of Γ̃), or add a
"non-planted" hypothesis (e.g. bounded multiplicative energy / additive spread of Λ_i at scale N); define "∔" (direct
sumset, all sums distinct). Then also the claim "TG is false for squares (as it must be)" stays true, and the
"proof of Question R would go through for δ > 1 − O(κ)" remains an Assessment conditional on the preprints *and* on
the transport, as stated.

**D10 (MINOR) — Prop 1.2 title / README row "per-level sign = character mod 4t".** For even A (t odd) the value at 2 is
(2/n), not the Kronecker value (−t/2) (e.g. t = 3, n = 233: (2/233) = +1, (−3/2) = −1), and v₂(d) is not determined
by d mod 4t. So the sign is J(−t, ·) of conductor | 4t on *odd* divisors, extended multiplicatively by (2/n) at 2. This
is exactly the source of D5. *Repair:* say so in the title.

**D11 (MINOR, naming) — §3.** M_R is not a singular series (no product of local densities; it is computed from the
factorisations of the N_t and conditions on the χ-signature of the range divisors — admitted in §3.4/§4.2 B4). Calling
it "reciprocity singular series" and saying it "explains 33–54 % of the deficit" overstates: it *decomposes* the
deficit into a χ-signature part (≈ 33–56 %) and a class-placement part. *Repair:* "reciprocity-conditioned model";
"the χ-signature of the range divisors accounts for ≈ 33–56 % of the deficit".

**D12 (MINOR) — §3.2 table and (iii).** (a) Say "N₋ (levels t ≤ 3000, ≈ 85 % of words at n ≈ 10⁶)". (b) The K = 25
3.4σ should mention it is the extreme of 15 families (≈ 2.5σ after look-elsewhere). (c) §3.1 "S_t(1044) = 2" uses
(d/n) at 2, not the stated χ_t; add "(with the 2-factor (2/n))".

**D4 (MINOR) — §5, 2510.21702 bullet.** Their metaplectic remark concerns SL(2, ℤ[i]) for the Apollonian superpacking.
*Repair:* "…suggests (for SL(2, ℤ[i]) and the superpacking) …; Thm 1.5 is the classical SL(2, ℤ) analogue".
