# Hostile review R46 of POINTWISE_HAAR.md (branch side-agent/haar-exponent)

Reviewer branch `side-agent/review-haar`. Reviewed commit: 6f4ca8b.
Status: ROUND 1 COMPLETE.

**Bottom line.** The main result, Thm 2.1 `log(1/δ*(T)) ≫ 𝓛³/log𝓛`, holds up: no FATAL
or MAJOR defect. Thm 1.4 (the new Janson-type inequality) is correct as stated; I re-derived
every step and brute-forced it exactly. Lemmas 2.2–2.4 re-derived; scaled exact check passes.
The event system is the same δ*(T) as POINTWISE_SIZE §7 / OMEGA §9 / OMEGA11 Cor 3.3 (same
definition, same normalisation), so `𝓛³/log𝓛 ≪ Φ ≪ 𝓛^6` is a consistent sandwich. The
defects are MINOR: overclaimed scope for Prop 1.5 / abstract (iii), overclaimed
"explaining" wording in §3 and abstract (iv), and the T_0 is astronomically large.

## Verdicts per claim

* **Lemma 1.1** — SOUND. Re-derived: given A, each compatible C becomes
  C' ⊇ C independent of S_A; ⋂C̄' ⊂ ⋂C̄.
* **Lemma 1.3** — SOUND (re-derived). Lopsided condition P(E|Av(S')) ≤ P(E)
  for S' ∩ Γ(E) = ∅ is exactly Lemma 1.1. Split S = S1 (conflicting with A) ∪ S2;
  P(A|Av(S)) ≤ P(A|Av(S2))/P(Av(S1)|Av(S2)); numerator ≤ P(A) (Lemma 1.1),
  denominator ≥ ∏(1−x_E) by the LLL induction (valid for every subfamily S').
* **Theorem 1.4** — SOUND. Re-derived line by line: P(E_i|B_i) ≥ P(E_i)P(B_i|E_i)/P(B_i^d)
  (B_i ⊂ B_i^d); given E_i, conflicting E_j vanish, compatible E_j become E_j' independent
  of S_i; P(E_j'|B_i^d) ≤ K P(E_j') by Lemma 1.3 (conflicts with E_j' ⊂ Γ(E_j)); sum with
  −log(1−p) ≥ p. Second bound: random thinning, p = min(1, μ/(2KΔ)); K, x_E inherited
  by subfamilies. Directions of all inequalities correct.
  From-scratch exact brute force `scripts/review_haar_janson_bf.py` (Fractions, random
  non-uniform marginals, one-hot coordinates, ranges 2–6, 2–10 events, all subfamilies S
  for Lemma 1.3, plus random external atomic A): seed 1×1500 instances (454 with valid
  LLL weights x_E = tP(E)) and ADV seed 2×300 (292 valid, 6–10 events with ≥2 coordinates
  each): **0 failures** of Lemma 1.1, Lemma 1.3, both bounds of Thm 1.4. Tightest
  (μ−KΔ) − (−log P(Av)) = −2.6e-5 (single-event-like instances).
  Scope caveat (author states it): single-value atomic events only; prime-power moduli not
  covered. §2 uses squarefree y-rough M, so fine.
* **Event system §0 vs δ*(T)** — SOUND. Matches POINTWISE_SIZE §7 Prop 7.1(a)
  definition verbatim (Haar on Ẑ^×, n ≡ 1 (24), forbidden n ≡ −4D (M), M ≡ 3 (4), M ≤ T,
  D | A_M²). gcd(A_M, M) = 1 so residues are units; ℓ | M ⇒ ℓ ∤ D. 𝓕 ⊂ full system, so
  δ*(T) ≤ P(Av(𝓕)) is the correct direction. Coordinates at ℓ > 3 independent uniform on
  (ℤ/ℓ)^× under the 1 (24) normalisation.
* **Lemma 2.2 (mass)** — SOUND (re-derived). D | A² ⟺ D* | A, exactly 2^{ω(n)} D with
  D* = n; n | A_M ⟺ M ≡ −1 (4n). Sieve: modulus 4n ≤ 4X^{1/5}, z = y = 𝓛^5, level X^{1/2},
  s ≥ 𝓛/(20 log 𝓛) → ∞, |r_d| ≤ 1 so remainder ≤ X^{1/2}; main X^{4/5}/(log 𝓛) dominates.
  Hypotheses of the fundamental lemma (dimension 1, g(p) = 1/p for p ∤ 2n) hold uniformly in n.
  Non-squarefree removal fine. Σ_{n≤x} 2^{ω(n)}/n ~ (3/π²) log² x correct.
* **Lemma 2.3 (LLL hypothesis)** — SOUND (re-derived). w_q bound via F2/F4/F3 correct;
  Σ_Γ ≤ (𝓛/log y)(𝓛³/(2y) + 4𝓛T^{−2/5}) = O(1/(𝓛 log 𝓛)). Remark (iii) check:
  ∏(1−2p) ≥ exp(−(8/3)Σp) ≥ e^{−1/3} > 1/2 for p ≤ 1/8, Σp ≤ 1/8. OK.
* **Lemma 2.4 (Δ)** — SOUND (re-derived). Compatible ⇒ g | D−D'; M = M' ⇒ same event by
  (F1); P(E∩E') = 1/φ(gvv') (squarefree). (a) uniform-in-v bound on Σ_g is legitimate;
  Δ_a ≪ 𝓛^4/y + 𝓛³ log N_0/N_0 ≪ 𝓛 log 𝓛. (b) algebra of the bracket checked
  term-by-term (= (16𝓛/y)[𝓛²(ΣD 1/n)²/16 + …]); main term 𝓛^7/y = 𝓛² exactly at y = 𝓛^5
  (so "≪ 𝓛²" is with constant ≈ 10^{−4}, since Σ_D 1/n ≤ (1+𝓛/10)²). Ordered-pair
  overcount only helps.
* **Lemmas 2.3–2.4, scaled exact check** — `scripts/review_haar_family_bf.py T y N0 N1`
  (from scratch, numpy; enumerates the family with the same shape but small parameters,
  4N1² < √T so (F1) holds; computes μ, Δ_a, Δ_b exactly, pairs counted once at their least
  shared prime; compares with the proof's explicit intermediate bounds (2.1)-based Δ_a
  bound, the (8/g)σσ Δ_b bound, the w_q bound). Results:
  T=2·10^5, y=7, n∈[2,10]: 119956 events, μ=3.80, Δ_a=0.506 ≤ 1470, Δ_b=0.095 ≤ 23.8,
  max w_q=0.33 ≤ 2.5. T=10^6, y=11, n∈[3,15]: 619968 events, μ=4.42, Δ_a=0.479 ≤ 1351,
  Δ_b=0.120 ≤ 30.6, max w_q=0.33 ≤ 2.5. All CHECK True; the assertion "M = M' ⇒ D ≠ D'
  impossible among compatible pairs" (F1) also held. (At this scale the LLL hypothesis is
  not met — Σ_Γ ≈ 0.7 — as expected for tiny y; the check only tests the counting.)
* **Theorem 2.1** — SOUND. Proof is Thm 1.4 + Lemmas 2.2–2.4, constants absolute
  (y, N_0 depend only on 𝓛; nothing secretly depends on T beyond what is tracked). Only
  external input: fundamental lemma (dimension-1 sieve, standard). I could not access
  Opera de Cribro / Halberstam–Richert (not in sources/), so the exact numbering
  "Lemma 6.3 / Cor. 6.10" / "Thm 2.5" is unverified; the form used (S ≥ XV(z)(1−O(e^{−s}))
  − Σ_{d<D}|r_d|) is the standard one. Label "PROVED modulo the sieve fundamental lemma" is
  honest (arguably just PROVED, standard input).
* **Proposition 1.5** — SOUND as literally stated (multi-prime squarefree part of a
  singleton-wise literally non-overlapping family has mass ≤ Σ_q 2/q ≪ log 𝓛; re-derived,
  the charging argument and the M=35 example check out: −4·1 ≡ −4·81 ≡ 1 (5), 3 ≢ 5 (7)).
  The interpretation in the abstract/§1 is overclaimed — see D1.
* **§3 MC reconciliation** — numbers SOUND (table reproduced exactly from POINTWISE_SIZE
  §7.2 by `scripts/review_haar_fit_check.py`: ratios 0.0759…0.0679, fits a = 2.394 /
  2.898, residuals 0.043 / 0.028); wording overclaims, see D2. Labels EVIDENCE /
  Assessment / CONJECTURE are present.
* **§4 prime side** — SOUND, labels honest (Haar-only; Prop 7.1(a) fixed-T link; RA
  explicitly heuristic; class-of-one bookkeeping E_H F ≤ δ*/P(H) correct).
* **Same δ* as the upper bounds** — SOUND. POINTWISE_OMEGA §9 l.919, SIZE §7.1(a), OMEGA11
  Cor 3.3 all use `{n∈Ẑ^×: n≡1 (24), n mod M ∉ 𝓡(M) ∀M≤T}` normalised in 1 (24). OMEGA11's
  numerical certificates (≤764 at 10^5, ≤1390 at 10^6) and the MC (≈38 at 65535) are
  consistent with Thm 2.1, which is vacuous at those T (D3).

## Defects

**D1 (MINOR) — Prop 1.5 / abstract (iii) / AGENT_REPORT item 3 overstate the scope.**
Location: header "(iii) Negative-association arguments alone cannot pass 𝓛²"; §1 sentence
after Prop 1.5 ("is the limit of independent/negatively correlated subfamily arguments").
Prop 1.5 only treats the *singleton* use of Lemma 1.2 (bound ∏_{E}(1−P(E))). Lemma 1.2
itself allows groups 𝓕_i with exact (or otherwise bounded) P(Av(𝓕_i)) inside each group;
that is not covered. Also, "≤ 𝓛² + O(log𝓛)" for the *total* needs (i) an upper bound on
the single-prime part, i.e. Σ_{ℓ≤T} #𝓡(ℓ)/(ℓ−1) ≪ 𝓛² (an upper Titchmarsh-divisor bound
Σ_ℓ τ(A_ℓ²)/ℓ ≪ 𝓛², easy via Brun–Titchmarsh but not stated; OMEGA8 (D) is the *lower*
bound), and (ii) a statement about prime-power moduli, which Lemma 1.2's single-bit
framework excludes (events {X_ℓ ≡ a (ℓ^k)} are not single bits). Repair: restate (iii) as
"singleton-NA bounds (Lemma 1.2 with singleton families, squarefree moduli) give at most
S1 + O(log 𝓛), S1 the single-prime mass ≍ 𝓛²", add the one-line upper bound for S1, and
drop "alone" / "the limit of … arguments".

**D2 (MINOR) — §3 and header (iv) "explaining the measured exponent".** The `log 𝓛` in
Thm 2.1 is an artefact of the proof (y = 𝓛^5 roughness), not a derived feature of Φ, and
the family 𝓕 is empty at every T in the table, so the theorem says nothing about those T.
The ratio-constancy test barely discriminates: over 1023 ≤ T ≤ 32767 the spread of
Φ/g is 1.16 % for g = 𝓛³/log𝓛 but 1.85 % for g = 𝓛^{2.5} and 3.1 % for 𝓛² log 𝓛
(`review_haar_fit_check.py`). Moreover I/(𝓛³/log𝓛) rises steadily (0.0856→0.0921) and SIZE §7.2 reports Φ ≈ 0.77·I
on 4095–16383, so over this short range the data cannot separate 𝓛³/log𝓛 from 𝓛^{2.5}
or from 𝓛³ times a slowly decaying correction.
Assessment 3.1 already says "consistency evidence only"; repair: change header (iv) and the
first §3 bullet from "explaining"/"exactly the measured drift" to "consistent with", and
state Conj. 3.1 as `a = 3` without committing to the `/log𝓛` factor (or give both options).

**D3 (MINOR) — T_0 is astronomically large; say so.** Location: Thm 2.1, Remark (iv).
𝓕 ≠ ∅ needs T^{1/10} ≥ 𝓛², i.e. 𝓛 ≳ 90 (T ≳ e^{90}); μ − KΔ > 0 needs much more, since
Lemma 2.2's c_1 includes the sieve constant, 1/(2 log 2), 3/π² /100, and Δ_b ≈ 10^{−4}𝓛^7/y
must be beaten. Remark (iv) says "at T ≤ 10^7 … 𝓕 is empty" — true but understates. Repair:
"T_0 is ineffective-in-practice (≥ e^{90}); Thm 2.1 is purely asymptotic".

**D4 (MINOR) — bookkeeping nits.** (a) Lemma 2.4(a): constant 16 should be 8 (P ≤ 8/(gvv'),
pairs v<v' once) — harmless. (b) Lemma 2.4(b): "Δ_b ≤ 𝓛^7/y" equals 𝓛² exactly at
y = 𝓛^5; fine but Remark (ii) ("y ≥ 𝓛^{4+ε} needed") is the real constraint: with
y = 𝓛^4 the crude Δ_b ≈ 10^{−4}𝓛³ would compete with μ ≍ 𝓛³/log𝓛 — worth one sentence.
(c) AGENT_REPORT_O46 says OMEGA8 Prop 6.6 is "modulo a BV-type divisor bound"; OMEGA8 and
this note say "(D) shifted-prime divisor bound" — harmonise. (d) Remark (ii) of Thm 1.4
("Harris fails for one-hot variables, P(X=r | X≠r') > P(X=r)") is correct; the brute force
confirms K is genuinely needed (not tested whether K=1 ever fails — not required).

## Not checked / limits
* Opera de Cribro and Halberstam–Richert not available locally; fundamental-lemma
  numbering unverified (form used is standard).
* Joag-Dev–Proschan 1983 (multinomial NA, closure under independent unions) and
  Erdős–Spencer 1991 (lopsided LLL) checked against my knowledge of the statements, not
  against PDFs; Lemma 1.2's use is the standard one, and Lemma 1.3 is re-proved in full
  in the note anyway.
* OMEGA12 (𝓛^5 log𝓛) not in this tree; not checked.
