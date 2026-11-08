# Z65_LOGIC2 — which principle does a proof of ES on Mordell classes need? (CHECKPOINT 1 skeleton)

Status: z65 lane LOGIC2 (brief `z52bbriefs/z65_lanes.md` §LOGIC2; common rules `z58_lanes.md`, `z53_depth.md`).
**ES is OPEN. Nothing here proves or disproves ES, (MS), or any case of them.** Internal, unrefereed.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z65_logic2_*`,
data `data/z65/logic2/`. Builds on `Z64_UNPROV.md` (cited as U64: Thm A/A′/A″, Lemmas 2.3–2.4, §2.7, Prop 6.2) and
`Z58_LOGIC.md`.

## 0. Falsifier table (mandatory; checkpoint form)

| screen | behaviour |
|---|---|
| F1 odd squares | Every non-provability result here is T1 imported into a model by analytic arcs (U64 §2.3). New: T1 *itself*, as an ordered ℕ-sentence, holds in these models (Thm P), so "use T1" is not a principle that helps. |
| F2 C-even | All model results transfer verbatim to R₈ and every (★)-sub-line (subsets of R vanish at squares). No positivity claimed. |
| F3 composites | The counterexamples are primes of the model. The rigidity statement (§5, CONDITIONAL on CONV-II-15) says arc-type counter-models for full ES can only live at square-mimicking primes; composite R-zeros cannot serve as landing values for a *prime* n. |
| F4 known zeros | No positivity claimed. |

## 1. Precise statements attacked

Language L_or = {0, 1, +, −, ·, ≤}; OI, NOI, IOpen, ES(n), ES★(n), Prime(n), ES_prime[r mod q] exactly as U64 §1.
Natural axioms considered (all true in ℕ; quantifiers over the non-negative part):
* **Bez** (Bezout): ∀a, b ∃u, v, d (d = ua + vb ∧ d | a ∧ d | b) (signed u, v in the ring).
* **PB** (prime Bezout = "residue rings modulo primes are fields"): ∀p ∀a (Prime(p) ∧ p ∤ a → ∃b p | ab − 1).
* **TS** (two squares): ∀p (Prime(p) ∧ p ≡ 1 (4) → ∃a, b p = a² + b²).
* **E(−1)**: ∀p (Prime(p) ∧ p ≡ 1 (4) → ∃x p | x² + 1).
* **QR_std** (reciprocity against standard primes; a schema): for each standard odd prime ℓ,
  ∀p (Prime(p) ∧ p > ℓ ∧ p ≡ □ unit (mod 4ℓ) → ∃x p | x² − ℓ*), ℓ* = (−1)^{(ℓ−1)/2}ℓ; together with the instances for
  −1 and 2.
* **Lag** (Lagrange): ∀x ∃a, b, c, d x = a² + b² + c² + d².
* **NR** (non-residue certificate): ∀p (Prime(p) ∧ p ≡ 1 (4) → ∃d, x, y, k, u, v (d = 4k + 3 ∧ d ≥ 1 ∧ x² + p = dy ∧
  ud + vp = 1)).
* **T1** (ordered ℕ-sentence): ∀u, B, C ≥ 1 ∀s (4uBC − u − B ≠ s²).

Questions (brief (1)): for T ∈ {OI + Bez, + TS, + QR, IE₁, IΔ₀, IΔ₀ + exp}, does T prove ES_prime[r mod q] for a
unit-square class r (e.g. 1 mod 840), or (MS)? Brief (2): the weakest natural axiom the square-mimicking-prime
construction cannot accommodate, and what that tells a proof.

## 2. Why this is not closed

U64 closed NOI + GCD + PD + Th_∀(ℤ) (ring language) and left open: ordered/ℕ facts (T1 in particular) in M_ϕ; TS, QR,
Bez/IE₁, IΔ₀ (U64 §§2.8, 5, 6.2 CONJECTURE, 9 O1–O4). This lane attacks exactly those.

## 3. First lemma (PROVED at checkpoint; full text in §2 of the final memo)

**Theorem P (ordered universal facts transfer).** Call a finite polynomial system Σ(x̄, ȳ) over ℤ, with "positive"
variables x̄ and free variables ȳ, *positively closed* if every real point of V_Σ(ℝ) that is a limit of real points of
V_Σ(ℝ) with x̄ ∈ (0, ∞)^k itself has x̄ ∈ (0, ∞)^k. If Σ is positively closed and has no integer solution with x̄ ≥ 1, then
every U64-type model M_ϕ (any residues ϕ(β_i) ∈ Ẑ) satisfies ∀x̄ ≥ 1 ∀ȳ ¬Σ(x̄, ȳ).
Proof: U64 Lemma 2.3 arc + connectedness of [0, ∞). The T1 system 4uBC − u − B = s² (positive u, B, C; free s) and the
full Type II system 4abcd = a + b + s²c are positively closed; T1 holds for every m (Z57_SYNTH Lemma A.1(b) is stated for
all m; K3 below re-checks even m). **Hence M_ϕ ⊨ T1, answering U64 §2.8's OPEN item: NOI + T1 ⊬ ES_prime[square class].**

## 4. Pre-registered kill tests

* **K1 (Thm T landing / coprimality lemma).** The planned model for NOI + TS has n = β₁² + β₂² as its *only*
  nonstandard prime. Its arcs must land at Pythagorean points b with b ≡ ϕ (mod D) and with Y(b) coprime to ℓ = √n(b)
  for every Y ∉ (n). Kill: a residue pattern a with a₁ + ia₂ a Gaussian unit square that no primitive (s² − t², 2st) hits,
  or a Y ∉ (n) whose values at all admissible points share a factor with ℓ. (Proof sketch passes; numeric spot-check
  planned.)
* **K2 (only-prime lemma, CERTIFIED numerics for the stated range).** Under the conditioned residue law ((a₁, a₂) uniform
  on Gaussian unit squares mod ℓ, others uniform), every irreducible f ≠ n must have ℓ·P(ℓ | f(a)) ≥ c > 0 on a set of
  primes of positive density; f = n must have P = 0. `scripts/z65_logic2_onlyprime.py 200` →
  `data/z65/logic2/onlyprime_200.txt`: **passed** for 11 test polynomials (means 0.78–2.06 on the relevant half of the
  primes; 0 for n). Kill would have been a test f ≠ n with P = 0 on almost all ℓ.
* **K3 (T1 for even squares).** `scripts/z65_logic2_t1all.c 3000` (all triples with 4uBC − u − B ≤ 9·10⁶):
  **0 square hits for m ≤ 3000**, odd and even (`data/z65/logic2/t1all_3000.txt`). Consistent with Lemma A.1(b).

## 5. Plan
* §3 Theorem T: NOI + GCD + PD + TS (+ Th_∀(ℤ) + positively closed Th_∀(ℕ)) ⊬ ES_prime[unit-square class].
* §4 No-go for polynomial models: PB/Bez, QR_std, Lag fail in *every* model with M ⊗ ℚ a polynomial ring.
* §5 Arc-compatible vs arc-killing principles; NR is arc-killing; rigidity (CONDITIONAL on CONV-II-15); compactness:
  square-mimicking primes exist in models of every true theory.
* §6 IE₁ / IΔ₀ / IΔ₀ + exp: literature (research subagents) and the precise status.
