# AGENT REPORT O269 — metaplectic / theta-multiplier view of T1; ES-side half-integral weight objects

Branch side-agent/metaplectic-es (merged side-agent/question-r first; README conflict resolved keeping R276-corrected
z36 rows). Main file `METAPLECTIC_ES.md`; memos `BRAINSTORM/z39_*.md` (6); scripts `scripts/z39_*.py`.
**ES is not solved; no infinite case claimed; no positive ES claim made.** R278 note applied (QUESTION_R Thm 1.5 cited as
classical/RS; Cor 1.3's t ≡ 3 half not used; TG not used). A deep self-review (reviewer subagent) was run and its
repairs applied (last section).

## SHARP:
1. **Thm K (identity PROVED, classical input; modular reading Assessment).** For each level t,
   Σ_{u,v≥2} q^{tuv−u−v} − Σ_{r,s≥0} q^{trs+r+s} = q^{t−2}[(Q;Q)²θ(X²)/θ(X)² − (1+X)/(1−X)], X = q^{t−1}, Q = q^t:
   the ES level series minus its partner quadrant is Kronecker's theta quotient θ'(0)θ(2z)/θ(z)² at the t-torsion
   point z = (t−1)τ'/t, τ' = tτ (Jacobi normalisation not carried out; the raw quotient has a −q^{2−t} term).
   Coefficientwise (PROVED): R_t(n) = ½E_t(tn+1) + ½O_t(tn+1) − β_t(n), with E_t/O_t the even/odd Dirichlet-character
   divisor sums mod t (weight-0 Maass / weight-1 holomorphic Eisenstein data) plus an elementary ±2 per coefficient,
   and β_t the boundary (u or v = 1). **Every term is a character divisor sum: no cusp form at any level.**
   Checked: identity numerically t ≤ 6; coefficient form t ≤ 30, n ≤ 1500 (0 failures).
2. **Cor K1.** The log² main term sits in the even-character (weight-0) part (𝔈 ≈ 116 at 10⁵, ≈ 163 at 10⁶ — log²
   scaling); the odd-character part averages ≈ 0 at generic primes (not on every polynomial family: m² − 3 is
   strongly negative). **T1 is an exact cancellation E_t + O_t = 0 on every level 4 | t at n = m²** (PROVED; R_t(m²)
   = 0 and β_t(m²) = 0 there).
3. **Prop S (Serre–Stark).** Weight-½ supports are finitely many periodic square classes; the T1 squares are exactly
   supp(θ(z) − θ(4z)); the five-slice failure set {λ(n) > 3} (which contains the non-square 105) is **not an exact
   weight-½ support** (periods ≤ 96 excluded by the 10⁶ census plus a parity argument; all periods under SQ₅). An
   exact-support obstruction only. (The interior-only zero set {N₋ = 0} also contains 5.)
Possible relay seed: the per-level even/odd (weight-0 vs weight-1) Eisenstein competition as the automorphic normal
form of R(n); Borisov–Gunnells toric modular forms (Kronecker quotients at torsion points ↔ toric fans ↔ HJ continued
fractions = ES words) — see sparks.

## Results by brief question
* (1) Generating functions: R's g.f. is not a finite modular object ((J)39), but each level is a Kronecker quotient
  plus even-character data (Thm K); the full sum is a boundary-truncated, additively shifted relative of d₃
  (GL(3) analogy, §4). Sturm/Duke template inapplicable: no cusp part; main term in the non-holomorphic even part,
  T1 an exact even/odd cancellation. Red team 2 Thm 2.2: a metaplectic construction of this kind violates only the
  finiteness hypothesis (H-A); the constructions examined do not open H-D (per-level content is congruence data);
  other metaplectic constructions are not excluded by this (§5).
* (2) Matrix side: the self-level condition is ⟨T⟩-bi-invariant — level-t words = elements with b = n and
  a, d ≥ 2t − 1 of the Bruhat cell of −I in Γ₁(t); the +I cell (Thm K's partner) is never empty; ν_θ ≡ −i on positive
  self-levelled elements of −Γ₁(4); the self-levelled set is not a semigroup (0/4096 products), so not a multiplier
  kernel (§3).
* (3) Quartic: u↔v inverts χ₄(A), so χ₄(A) is not a symmetric sign on the k | t slices (PROVED; other quartic
  invariants not excluded); ordered smaller-divisor bit balanced (EVIDENCE p < 2·10⁴, k = 4, 8, 16); no quartic
  signature in the 8/p exceptions (§6).
* (4) Numerics: Thm K checks; size split at primes ≈ 10⁵, 10⁶, odd squares (T1 control: N₋ = 0, odd part strongly
  negative), near-square families. Modularity tests of R itself are moot ((J)39 proves non-modularity by growth).

## Labels
Thm K identity/coefficients, Cor K1.1, Prop S(1,2), §3 dictionary, narrow quartic no-go: PROVED. Modular readings of
Thm K: Assessment. Prop S(3): PROVED for periods ≤ 96, CONDITIONAL (SQ₅) in general. Sizes: EVIDENCE. GL(3)/shadow
readings, Thm 2.2 screen: Assessment.

## Sparks (not pursued)
1. **Borisov–Gunnells toric modular forms** (Invent. Math. 144 (2001)): weight-1/2 forms from Kronecker quotients at
   l-torsion points attached to complete toric fans with a degree function. ES words are HJ fractions of length 3 =
   5-ray fans / Farey pentagons (LENGTH_THREE). Is the ES sign (some cluster variable ≡ 0 mod 4) visible in the BG
   form of level 4 of the pentagon fan? Dictionary hunt only.
2. Levels with many odd characters: D⁻ − D⁺ = −(2/φ(t))Σ_{χ odd}σ_χ(N); for φ(t) = 2 it is ≤ 0 (theta positivity
   against ES); can genus data force it positive at larger t? (likely B2).
3. Holomorphic projection of E_{1,χψ}·\bar θ_t to package Σ_m D⁻_t(tm² + 1) = 0 as a vanishing Rankin–Selberg
   period; probably tautological.
4. Bruinier–Funke–Imamoglu cycle integrals at square discriminants vs the split level forms tuv (analogy only).

## Self-review (reviewer subagent, deep) — applied
High: modular reading of Thm K demoted to Assessment (normalisation; ±2 in every coefficient; t = 2 has no odd
characters); t = 2 `elif` bug in z39_split/z39_nearsq fixed, 10⁵ and near-square numbers re-run, 10⁶ corrected by the
reviewer's mean bias (3.92); summation convention t ≤ (n+4)/4 stated; Prop S failure set defined as {λ > 3},
period-parity argument added, stated as exact-support obstruction. Medium: a, d ≥ 2t − 1 restored in the cell
dictionary; "split ⇒ shadow-free" withdrawn; GL(3) link stated up to boundary terms; no-go scopes narrowed (H-D,
quartic). Passed per reviewer: Thm K substitutions, boundary term, (K2), character formulas incl. ±2; Cor K1.1;
ν_θ ≡ −i on positive self-levelled elements of −Γ₁(4); quartic census reproduces.
