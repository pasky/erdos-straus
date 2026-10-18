# AGENT REPORT O269 — metaplectic / theta-multiplier view of T1; ES-side half-integral weight objects

Branch side-agent/metaplectic-es (merged side-agent/question-r first; README conflict resolved keeping R276-corrected
z36 rows). Main file `METAPLECTIC_ES.md`; memos `BRAINSTORM/z39_*.md` (6); scripts `scripts/z39_*.py`.
**ES is not solved; no infinite case claimed; no positive ES claim made.** R278 note applied (QUESTION_R Thm 1.5 cited as
classical/RS; Cor 1.3's t ≡ 3 half not used; TG not used). A deep self-review (reviewer subagent) was run and its
repairs applied (last section).

## SHARP: (revised after R280; no FATAL)
1. **Thm K (classical identity, new only as a packaging in the campaign — R280 D2).** For each level t,
   Σ_{u,v≥2} q^{tuv−u−v} − Σ_{r,s≥0} q^{trs+r+s} = q^{t−2}[(Q;Q)²θ(X²)/θ(X)² − (1+X)/(1−X)], X = q^{t−1}, Q = q^t, and
   (K1′, R280 D1) the theta quotient term alone has coefficients **exactly** (D⁻_t − D⁺_t)(tn + 1) =
   −(2/φ(t))Σ_{χ odd}σ_χ(tn+1), the boundary term exactly β_t(n) = 2·1[(t−1) | (n+1)] − 1[n = t−2]. So
   R_t = ½(D⁻ + D⁺) + ½(D⁻ − D⁺) − β_t: every term a character divisor sum, **no cusp form at any level**. Modular
   reading (Kronecker quotient at a t-torsion point = weight-1 Eisenstein after Jacobi normalisation; even part =
   weight-0 Maass data): Assessment.
2. **Prop S (PROVED, unconditional after R280 D6; holomorphic scope, D7).** Holomorphic weight-½ supports are finitely
   many periodic square classes; the T1 squares are exactly supp(θ(z) − θ(4z)); the five-slice failure set
   Z = {λ > 3} (containing 105) is **not the exact support of any holomorphic weight-½ form** (R280's argument:
   primes ℓ ≡ 3 (4) with (ℓ/105) = −1 give length-2 certificates on whole classes of 105m²). Elementary, exact-support
   only; mock / weakly holomorphic / harmonic weight-½ objects not covered.
Demoted (R280 D3/D4): "T1 as exact weight-0/weight-1 cancellation" is the classical D⁻_t(tm²+1) = 0 relabelled;
"log² in weight 0, oscillation in weight 1" holds only after a non-modular renormalisation of size ≍ n and amounts
to elementary equidistribution of non-trivial divisors between ±1 mod t (Assessment with caveat).
Possible relay seed: Borisov–Gunnells *Toric varieties and modular forms* (weight-r forms from rank-r fans, built
from Kronecker-type quotients at torsion points) vs ES words = 5-ray (rank-2) fans — see sparks.

## Results by brief question
* (1) Generating functions: R's g.f. is not a finite modular object ((J)39), but each level is a Kronecker quotient
  plus even-character data (Thm K); the full sum is a boundary-truncated, additively shifted relative of d₃
  (GL(3) Eisenstein analogy, abelian, §4). Sturm/Duke template inapplicable: no cusp part at any level. Hatch screen
  (R280 D9, §5): the examined constructions touch H-A (quantitatively blocked as assessed) and formally H-E (exact
  signed expansion with positive main term, but its error is the same single-n level sum of ≍ n/4 terms — not
  opened); H-D not opened (per-level content is congruence data); other metaplectic constructions not excluded.
* (2) Matrix side: the self-level condition is ⟨T⟩-bi-invariant — level-t words = elements with b = n and
  a, d ≥ 2t − 1 of the Bruhat cell of −I in Γ₁(t); the +I cell (Thm K's partner) is never empty; ν_θ ≡ −i on positive
  self-levelled elements of −Γ₁(4); the self-levelled set is not a semigroup (0/4096 products), so not a multiplier
  kernel (§3).
* (3) Quartic: u↔v inverts χ₄(A), so χ₄(A) is not a symmetric sign on the k | t slices (PROVED; other quartic
  invariants not excluded); ordered smaller-divisor bit balanced (EVIDENCE p < 2·10⁴, k = 4, 8, 16); no quartic
  signature in the 8/p exceptions (§6).
* (4) Numerics: Thm K checks; size split at primes ≈ 10⁵, 10⁶ (exact per-n t = 2 correction, R280 D5), odd squares
  (T1 control: N₋ = 0), near-square families; R280 reproduced the 10⁵ and square numbers exactly. Modularity tests of R itself are moot ((J)39 proves non-modularity by growth).

## Labels
Thm K identity/(K1′)/coefficients, Cor K1.1 (classical, relabelled), Prop S(1,2,3) (S(3) unconditional), §3
dictionary incl. the precise (c/d) = −(−1/b)(a/b) lemma, narrow quartic no-go: PROVED. Modular readings of Thm K,
Cor K1.3 reading (with caveat): Assessment. Sizes: EVIDENCE. GL(3)/shadow readings, hatch screen: Assessment.

## Sparks (not pursued)
1. **Borisov–Gunnells, "Toric varieties and modular forms"** (Invent. Math. 144 (2001) 297–325): weight-r forms on
   Γ₁(l) attached to complete rank-r fans with a degree function (the 2-dimensional ES pentagon fans give weight 2). ES words are HJ fractions of length 3 =
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

## R280 hostile review — applied
All "(R280 repair)" items: D1 (K1′) clean form + β_t closed form; D2 novelty framing; D3 Cor K1.1 restated as the
classical D⁻_t(tm²+1) = 0 with R280's direct Jacobi proof (all m); D4 Cor K1 reading caveated (non-modular
renormalisation; equidistribution) and removed from headlines; D5 exact per-n t = 2 correction at 10⁶ (𝔈 = 162.7,
𝔒 = −0.5; squares 𝔒 = −103, −37, −23, −72); D6 Prop S(3) unconditional (adopted R280's proof); D7 holomorphic scope
everywhere; D8 §3 precise lemma, "b odd"; D9 §5 rewritten as a hatch screen incl. H-E; D10 Borisov–Gunnells title and
weight; D11 citation pointers marked not re-checked; minor remarks (r_K = σ_χ in C6; exact 𝔅; GL(3) Eisenstein is
abelian, does not touch H-D).
