# AGENT REPORT O269 — metaplectic / theta-multiplier view of T1; ES-side half-integral weight objects

Branch side-agent/metaplectic-es (merged side-agent/question-r first; README conflict resolved keeping R276-corrected
z36 rows). Main file `METAPLECTIC_ES.md`; memos `BRAINSTORM/z39_*.md` (6); scripts `scripts/z39_*.py`.
**ES is not solved; no infinite case claimed; no positive ES claim made.** R278 note applied (QUESTION_R Thm 1.5 cited as
classical/RS; Cor 1.3's t ≡ 3 half not used; TG not used).

## SHARP:
1. **Thm K (PROVED, classical input):** for each level t, Σ_{u,v≥2} q^{tuv−u−v} − Σ_{r,s≥0} q^{trs+r+s} =
   q^{t−2}[(Q;Q)²θ(X²)/θ(X)² − (1+X)/(1−X)], X = q^{t−1}, Q = q^t — i.e. the ES level series is half of Kronecker's
   theta quotient θ'(0)θ(2z)/θ(z)² at the t-torsion point z = (t−1)τ'/t (a weight-1 holomorphic Eisenstein series,
   odd characters mod t) plus half the coefficient sequence of a weight-0 Maass Eisenstein series (even
   characters), minus boundary terms. **No cusp form at any level.** Checked: identity numerically t ≤ 6,
   coefficient form t ≤ 30, n ≤ 1500 (0 failures).
2. **Cor K1:** the log² main term sits in the weight-0 non-holomorphic part (𝔈 ≈ 113 at 10⁵, ≈ 159 at 10⁶, log²
   scaling); the holomorphic weight-1 part averages ≈ 0 at generic primes; **T1 is an exact cancellation of the
   weight-1 against the weight-0 coefficient on every level 4 | t at n = m²** (PROVED). Caveat: the holomorphic part
   is not a T1 detector by itself (m² − 3 primes have it strongly negative without an N₋ deficit).
3. **Prop S (Serre–Stark):** weight-½ supports are finitely many periodic square classes; the T1 squares are exactly
   supp(θ(z) − θ(4z)); the non-square five-slice failure 105 is **not metaplectic** (excluded for periods ≤ 96 by the
   10⁶ census; for all periods under SQ₅).
Possible relay seed: the per-level weight-0 vs weight-1 Eisenstein competition (Thm K) as the automorphic normal
form of R(n); and Borisov–Gunnells toric modular forms (Kronecker quotients at torsion points ↔ toric fans ↔ HJ
continued fractions, which is what ES words are) — see sparks.

## Results by brief question
* (1) Generating functions: R's g.f. is not a (finite) modular object ((J)39), but each level is exactly modular in
  mixed weight 0/1 (Thm K); the full sum is an additively shifted d₃ (GL(3)-Eisenstein type; §4,
  z39_gl3_shifted_divisor). Sturm/Duke template inapplicable: no cusp part; main term is non-holomorphic weight 0,
  T1 lives in the holomorphic weight-1 part. Red team 2 Thm 2.2: a metaplectic construction violates only the
  finiteness hypothesis (H-A); it does not open H-D (per-level content is congruence data) (§5).
* (2) Matrix side: the self-level condition is Γ_∞-bi-invariant — level-t words = positive elements with b = n of the
  Bruhat cell of −I in Γ₁(t); the +I cell (Thm K's partner) is never empty; ν_θ ≡ −i on positive self-levelled
  elements of −Γ₁(4); the self-levelled set is not a semigroup (0/4096 products), so not a multiplier kernel (§3).
* (3) Quartic: u↔v inverts χ₄(A), so no symmetric quartic sign on any k | t slice (PROVED); ordered bit balanced
  (EVIDENCE p < 2·10⁴, k = 4, 8, 16); no quartic signature in the 8/p exceptions (§6).
* (4) Numerics: Thm K checks; size split at primes ≈ 10⁵, 10⁶, odd squares (T1 control: N₋ = 0, 𝔒 strongly
  negative), near-square families. Modularity tests of R itself are moot ((J)39 proves non-modularity by growth).

## Labels
Thm K, Cor K1.1, Prop S(1,2), §3 dictionary, quartic no-go: PROVED. Prop S(3): PROVED for periods ≤ 96, CONDITIONAL
(SQ₅) in general. Sizes: EVIDENCE. GL(3)/shadow readings, Thm 2.2 screen: Assessment.

## Sparks (not pursued)
1. **Borisov–Gunnells toric modular forms** (Invent. Math. 144 (2001)): they attach weight-1/weight-2 modular forms
   (products of Kronecker quotients at l-torsion points) to complete toric fans with a degree function. ES words are
   HJ fractions of length 3 = 5-ray fans / Farey pentagons (LENGTH_THREE). Is the ES sign (some cluster variable
   ≡ 0 mod 4) visible in the BG form of level 4 of the pentagon fan? Dictionary hunt only.
2. Weight-1 positivity at levels with many odd characters: D⁻ − D⁺ = −(2/φ(t))Σ_{χ odd}σ_χ(N); for φ(t) = 2 it is
   ≤ 0 (theta positivity against ES); for large t it can be forced positive by genus data? (likely B2).
3. Holomorphic projection of E_{1,χψ}·\bar θ_t (weight ½ via Sturm) to package Σ_m D⁻_t(tm² + 1) = 0 — T1 as a
   vanishing Rankin–Selberg period; probably tautological.
4. Bruinier–Funke–Imamoglu cycle integrals at square discriminants vs the split level forms tuv (analogy only).
