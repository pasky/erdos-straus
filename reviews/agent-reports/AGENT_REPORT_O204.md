# AGENT_REPORT_O204 — the (k, Q₁) phase diagram (wave Y-a), checkpoint 1

Main file: PHASE_DIAGRAM.md. Scripts: scripts/pd_band.py, pd_band2.py, pd_k1.py, pd_k1s.py, pd_theta.py (tiny
outputs, quoted in the file). Self-review run (codex deep reviewer): no FATAL; 7 MAJOR + 5 MINOR, all repaired in the
file (marked "R-self-review" where substantive). Then two independent hostile reviews, R209
(reviews/phase-diagram-review.md) and R210 (reviews/phase-diagram-review-2.md): no FATAL; R209 M1 (ES^□ k = 1
infinitude needed a proof — added), M2 (Thm 5.1 quantifier → family form), R209 m1–m12, R210 m1–m13 all applied in
PHASE_DIAGRAM.md, marked (R209 repair)/(R210 repair). **ES is not solved; no bounded-cap variant is proved.**

## SHARP:
1. **The self-mute cap creates a second archimedean wall on SLICES (Thm 2.1(a), PROVED, attained exactly).** For
   ES^{[2]} (den z | y², ⊇ ES^{(y,1)}): Q₁ ≤ (16k³n + 1)/(4k − 1). With EXPONENT_CAP Thm 2.1, every fixed-k and every
   fixed-Q₁ slice of the duality plane D·g = 4k²n + Q₁² is finite; for Q₁ > (n+1)/2 solutions lie in the band
   √(Q₁/6n) ≤ k < Q₁²/2. Equality for every n ≡ 2 (mod 3) via Q₁ = (16n+1)/3, g = (64n+1)/3, D = (4n+1)/3.
   **It does NOT make ES^{(y,1)} or ES^{[2]} a finite search** (R210 m2, R209 m3): the band is unbounded and carries
   infinite Pell orbits (n = 3: (Q₁, k) = (55, 2), (101, 232), (289, 2984), …); R200 M1 (bounded e, growing S: open)
   stands for e = 1, narrowed only to "k and Q₁ grow together".
2. **k-direction dichotomy on ONE slice (Prop 3.1, Cor 3.2, PROVED).** The k = 1 slice is "4n + Q₁² has a divisor
   g ≡ −1 (mod 4M)": ES^□ (M = 1) infinite by Dirichlet; ES^{(y)} (M = rad Q₁, S fixed) infinite by the Thm 4.2 sieve;
   ES^{(y,1)}/ES^{[2]} (M = Q₁) finite; ES (Q₁ = 1) one number. (ES^□: odd non-square n, proof added per R209 M1;
   ES^{(y)}: also 3 ∤ n, ineffective — R209 m4 weakened gcd(n, 15) = 1 to 3 ∤ n.) e = 2 (M = rad Q₁, exponents ≤ 2): no wall seen
   numerically (EVIDENCE). The whole cap ladder is visible inside k = 1.
3. **One axis for all caps (Prop 4.1, PROVED):** ES^{(y,e)} ⟸ n(2k(4kλ)^e)² + 1 has a divisor ≡ −1 (mod 4kλ) with
   (g+1)/(4kλ) squarefree, gcd(λ, n) = 1 (exact for e ≤ 1, pure-power sub-family for e ≥ 2): modulus exponent
   θ_min = 1/(2e+2), the infimum over the face along bounded λ — a property of this parametrisation, not of the cell
   (k fixed, λ → ∞ gives 1/(2e)). ES: ½ (Lenstra); the e = 1 face reaches down to ¼, the N^{1/4} threshold of Lenstra
   (1984) / CHN (2008), with no margin; proved cells θ → 0 on their prime face.
4. **Normal form (Prop 1.1):** every shot is k(4ab − n) = b + aQ₁² — the overflow is a Q₁²-weight in ES's own Type II
   equation (re-expression of EXPONENT_CAP Cor 1.4, but a convenient one). D-face: ES^{[2]} ⟺ 4λtb − n | b + λt³
   (with stated side conditions).

## Results (labels)
* Thm 2.1 (PROVED, numerically checked on 348 + 36 shots, max Q₁/W = 1.000; slices only, see SHARP 1).
* Prop 3.1(a) (PROVED relative to the reviewed FROBENIUS_FIRING Thm 4.2 sieve, ineffective; needs 3 ∤ n for the
  class choice a_ℓ ∉ {0, ±1}); (b) PROVED. Cor 3.2 ES^□ k = 1 infinitude: PROVED by Dirichlet (R209 M1 repair). EVIDENCE: with ONE mute prime 3, every prime p < 10⁶ has a k = 1 shot
  4p + 9^a, a ≤ 21; no odd square does.
* Thm 5.1 (PROVED relative to Bombieri–Vinogradov + Iwaniec linear sieve, ineffective, astronomically late onset):
  for every A, η > 0 and n there is x₀(n, A, η) such that for all x ≥ x₀ some ES^{(y,e)}(n) solution has
  x/8 ≤ y ≤ nx and e ≤ y^{(2+η)log₃y/(A log₂y)} (EXPONENT_CAP Thm 3.2 had y^δ). S grows with x, P ≤ (log x)^A.
* §6 B1 statement (PROVED, elementary; strengthened per R209 m10 / R210 m10): for a prime r ≡ 1 (mod 4) and EVERY
  class u ≢ 0 mod r, no finite set of shot identities of any variant down to ES^□ covers the primes p ≡ u (mod r)
  (same for any modulus with all prime factors ≡ 1 mod 4). Excludes finite shot-identity coverings only.
* §6 class-layer conditional (PROVED): ES^{[2]}(n) holds if some genus-admissible (λ, D) (D admissible, λ²D² − n > 0
  non-square) has one proper form class per genus in discriminant 16(λ²D² − n) — a Gauss/Cohen–Lenstra-type statement, not a standard hypothesis.
* T1: every cell is T1-bearing like ES (no Type I/II-shaped solutions at squares; scaling gives non-shot ones);
  "any proof must use a non-square input" is an Assessment.

## What did NOT work (iteration log in the file, §0)
* Sieving the joint condition at a single n: not blocked by B6 (n fixed, r varies) but by the per-certificate box
  g^{o(1)}; after switching it is a one-number-per-parameter divisor problem in a class whose modulus is a parameter
  of the number (θ > 0); BFI/Fouvry-type level-of-distribution statements have main terms x/φ(q) and do not see it.
* Pell-orbit freedom: multiplies one ES^{[2]} point, does not create it, does not keep Q₁ squarefree.
* Polylog cap: large-sieve/moment attempts fail exactly because self-mute forces ∏S ≤ r (|S| ≤ log r/log log r),
  which is the threshold where high-moment large sieves stop working (sketched, not written up).

## Sparks (not pursued)
1. Gallagher's large-sieve density near σ = 1 with S chosen to avoid the exceptional conductor should push Thm 5.1 to
   e = exp(O(√(log y)·log₂y)) (Remark 5.1(2)), provided the exceptional modulus, if any, does not divide 4 rad(n)
   (R210 m13).
2. The e = 2, k = 1 family "4n + R⁴ has a divisor ≡ −1 (mod 4R)" ⟺ "1024ns⁴ + 1 has a divisor ≡ −1 (mod 4s)"
   (R ↔ s symmetric): a quartic Hooley-type problem; any infinitude result for divisors of nX⁴ + c in classes mod X
   would prove the e = 2 cell's k = 1 slice infinite.
3. Is the ES^{[2]}-sterile set on r-generic lines (r ≡ 3 mod 4) empty? On such a line the certificate equation
   becomes the n-free twisted V₁: A² + B² + rD′ = 2wD′AB, whose Pell orbits act on u = −(A/B)² mod r by Möbius maps;
   transitivity on non-residues would be a crisp contrast with (J)26 (sterile ES points for large r).
4. Effective GRH version of Prop 3.1(a)/Thm 5.1 with r ≤ n^{C}.
