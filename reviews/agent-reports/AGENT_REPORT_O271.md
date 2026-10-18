# AGENT REPORT O271 — Synthesis IX: the lower tail at a single prime

Branch `side-agent/synthesis-nine` (merged main after (J)100). Deep file `SYNTHESIS_SPARKS9.md`; 10 memos `BRAINSTORM/s9_*.md`
(indexed in `BRAINSTORM/README.md`); scripts `scripts/s9_{words.py, words.c, sign.py, union_stats.py, thinning.py,
ladder_thinning.py, level_bm.py, janson.c, janson_stats.py, level_poisson.py}`; tiny logs `logs/s9_*`. O269/O270 read only via
`git show`. **ES is not solved; no infinite case for primes is claimed; no "standard conjecture ⟹ ES".**

## SHARP (modest; flagged per the relay rule, judge for yourself)
1. **The BM layer of Thm K is one odd character, and it is pointwise free (SPARKS9 Prop 2.1–2.2, PROVED, elementary).** In level
   coordinates BL's class is χ_{−t} (4 | t) at the divisors d of tn + 1 — the twin of O268's χ_{−4uB}(p) in pair coordinates.
   M^{lev}_t = (τ(N) − σ_{χ_{−t}}(N))/φ(t) ≥ 0, = 0 at squares, and **∃ 4 | t with M^{lev}_t(n) > 0 ⟺ n is not a square**, witness
   t ≤ 4ℓ(n), ℓ(n) = least prime with (n/ℓ) = −1 (via (−t/ℓ) = (n/ℓ) when ℓ | tn + 1). So H⁻_BM is purely the class position of a
   divisor inside the coset {χ_{−t} = −1} (one class of φ(t)/2). Checked: all 499 500 odd non-squares ≤ 10⁶, 0 failures; squares
   fully obstructed. Corollary (s9_disproof_class_layer): any structured (★)-failure family at non-squares is invisible to every
   quadratic/reciprocity layer — the level form of BL Thm 1.8.
2. **(★) and b = 1 are correlated only through the size of one numerator-free set (EVIDENCE).** In word coordinates the k/n two-line
   union is "some solution of tuv − u − v = n has a coordinate ≡ 0 (mod k)" (Cor 1.2, PROVED; SPARKS8 Prop 1.3 extended to all odd n
   and all k). Residual correlation of the two lines: +0.37 (≤ 10⁶), +0.39 ((10⁶, 10⁷]) — positive, not negative — and the partial
   correlation given log |W(p)| is **0.03 / 0.01**. If (★) fails, b = 1 is pushed DOWN (to 0.59× its mean).

## Results by mandatory item
* (i) Literature map (s9_lower_tail_literature): no every-n theorem for a natural problem with polylog main term. Polylog
  every-n theorems are designed sets (Erdős–Tetali 1990, M4) or structural (M3); natural polylog problems have structured
  exceptions: Romanov (Erdős 1950), p + 2^a + 2^b (Crocker 1971; Pan 2011: ≫ x^{1−ε} exceptions — checked), Markoff (Ghosh–Sarnak).
  Goldbach/Linnik/Estermann/p + x² + y²/ternary forms all have power main terms (M1a).
* (ii) Thm K × BM: SHARP 1. Dirichlet-coefficient positivity: no fixed-integer packaging (moving almost-coprime integers), and the
  available positive coefficients (σ_χ = R_D/w) enter with a minus sign (D⁻_t ≤ (τ − σ_{χ_{−t}})/2) — Hecke positivity pushes
  against ES (s9_no_fixed_integer).
* (iii) Variance at fixed p: Lemma 3.1 (PROVED) — the ℓ² Fourier/PZ certificate over any fixed group succeeds iff
  m̄² > (|G| − 1)V and then occupies every class (phase-blind; exact form of F4's B3 objection). Lemma 3.2 (tautology): over p the
  exponent must exceed log p. Prop 3.3 (EVIDENCE, ≤ 3·10⁶): word-level Janson dependency Δ/μ = 3.6 → 9.4 (μ²/2Δ ≈ 1–2, useless);
  the near-independent units are levels, E[#hit levels] = (0.44 → 0.97)·log p — critical. Prop 3.4 (EVIDENCE, ≤ 5.4·10⁶):
  level-Poisson predicts 12.6 zeros vs 12 observed in total (swap-Poisson 5.0), but the shape is wrong — the far tail is fatter
  (positive joint dependence of level failures, the Harris direction). Why near-independence cannot become a proof: it is
  pairwise, at one p there is no measure, and the joint tail is exactly where it fails.
* (iv) Union: SHARP 2 — negative answer, no forcing, no identity beyond "same set W(p)". Given W, union = overdispersed
  mirror-pair thinning (dispersion 2.4–3.8 vs 2). Census ≤ 10⁷ reproduces all known (★)/b = 1 failures; union never fails.
* (v) Own: fibration over the level (s9_fibration_level; every fibre has the integral point (0, −n); ES = positivity + "a
  divisor has Frobenius c_∞ in ℚ(ζ_t)"; fibration method collapses because fibre obstruction groups (ℤ/t)^* are unbounded while
  Br = ℤ/2, and Schinzel pushes tn + 1 toward primes — the wrong way); numerator ladder as a thinning ladder (s9_ladder_thinning:
  order of magnitude right for k = 4…32, 1.7–7× under-prediction); thin-orbit growth at the BM level (s9_thin_orbit_bm: nothing to do
  there, density fails at the class layer).

## Controls
T1: Cor 1.2/union and Prop 2.1(c) exact at odd squares (0 union words, σ ≡ +1, W(m²)/L² ≈ 0.45); 105: BM layer free
(ℓ = 11, t = 20) while ES-five fails — the BM layer does not decide; numerator 8: same witness for 8 | t, and the k = 8 union fails at
exactly 34 primes < 8000 incl. 131, 241 — every mechanism here is numerator-blind, as it must be.

## Honest limits
Lemma 3.1 and Prop 2.2 are elementary (no claim of depth). The Janson/level-Poisson numbers are model diagnostics, binned by
O268's M_BM8 (bins confound p-size and arithmetic). z38_mbm was cut at 5.37·10⁶ by the time limit. Harpaz's exact hypotheses were
not checked (only the abstract); the fibration collapse is an Assessment.

## Sparks (not pursued)
1. Climb above the BM layer: Prop 2.2 works because quadratic reciprocity turns (−t/ℓ) into (n/ℓ) once ℓ | tn + 1. For characters
   of order 4 mod t (t with 4 | φ(t)), is there a reciprocity (biquadratic, over ℚ(i)) making ψ(ℓ) a function of n mod ℓ for the
   forced t ≡ −n⁻¹ (ℓ)? If yes, the next 2-power layer is also free and the class lottery shrinks to the odd part of (ℤ/t)^*.
   Likely obstruction: ψ(ℓ) depends on ℓ mod t, not on n — test numerically first.
2. Higher-order dependence of level failures (Prop 3.4): find the integer(s) shared by jointly failing levels (smooth p − 1? common
   small primes of tp + 1?) — a quantitative model for the fatter tail, relevant to the H⁻_BM credence.
3. Cubic characters as the only remaining "algebraic" disproof shape (s9_disproof_class_layer): can a structured family bias all
   cubic characters mod t at the forced primes simultaneously?
4. |W(p)| (the numerator-free word count, mean ≈ 0.92 L²) has a thin lower tail (1 %-quantile ≈ 0.53 L²); a pointwise lower bound
   for |W(p)| alone is a 4-blind B2 problem but with one fewer constraint — is it any easier (e.g. via u = 1, 2 words τ(p+1) + τ(p+2)
   plus a short-interval divisor argument)?
