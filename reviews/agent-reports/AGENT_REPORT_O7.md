# AGENT_REPORT_O7 — Conjecture 6.4 (k-ary comparison inequality)

## Checkpoint 3 (after `reviews/exceptional-kary-review-2.md`)

* **E1 applied.** Lemma 2.3 now states and proves `B(n,t,d) ≥ 1` (by
  interpolating the constant 1, `Σ|ℓ_y(n)| ≥ 1 ≥ Σψ(y)`). Theorem 2.5 and
  the sequential step note `Φ ≥ 0`, which is the sign hypothesis of
  Theorem 4.1.
* **E2 applied.** In Theorem 4.5, I is the largest index with
  `2^I s₁ < λ/2`, and the blocks cover `(e^{s₁}, e^{λ/2}]` exactly.
* **E3 (status lines inside KARY only).** Updated:
  * the §0 status line now records three reviews and labels Thm 4.5
    PROVED (internal);
  * the §0 table labels are updated;
  * new paragraph "Superseded statements elsewhere" in §4.3 lists the stale
    ETw/STATUS statements and the caveats of the θ-reading (ET Lemma 2.9
    hypotheses, fixed B, ℛ(M) only).

  ETw, STATUS and DISCOVERIES are untouched; the parent is doing the ledger.
* **D1–D2 (review 1): still not applied.** `side-agent/review-kary` is still
  at e283164, its review file has no item 9 and no D1–D3 text, and review 2
  does not restate them. If they exist, please forward the text.

## Checkpoint 2 (after `reviews/exceptional-kary-review.md`)

* That review rated every item SOUND: Lemmas 2.2–2.4, Thm 2.5, §3,
  Thm 4.1, Lemmas 4.2–4.3, and the Thm 4.5 assembly. Its independent brute
  force found no violation.
* **D3 applied:** new Lemma 4.2′ writes out ETw Lemma 2.6 for the dyadic
  blocks `(e^s, e^{2s}]`, in three steps:
  1. reduction to `Σ τ(A_M²)Γ(M)/M` via inflation;
  2. the window-free mean value `S(x) ≪_W x log²x`, with the decaying
     `h(ℓ) ≤ 2ℓ^{−1/2}`;
  3. explicit partial summation up to `X = e^{2(1+B)s}`, which gives
     `K(W)(2(1+B)s)³` with `K = 1.3K₀(W)`.

  Thm 4.5 now cites it, with `K₁ = 8(1+B)³K`.
* **D1, D2: not applied, because their text is missing.** The committed
  review file on `side-agent/review-kary` (e283164) has no item 9 and no
  D1–D3 text, although the commit message says "item 9 (labels, D1-D3
  editorial)". Its diff only touches the brute-force table. Please forward
  D1/D2; I will apply them in one more commit.
* §0 status line and summary table updated.

## Checkpoint 1

Branch: this worktree. Deliverable: `EXCEPTIONAL_KARY.md`; scripts
`scripts/kary_check.py`, `scripts/kary_b21_check.py`; data `data/kary/`.

## Outcome (checkpoint)

1. **Theorem 2.5 (PROVED): weighted k-ary comparison for ETw's own sequential
   law σ.** Any arity, any pattern family, no incident-weight hypothesis, no
   Markov removal, no sparsity. Only the light caps `p_ℓ ≤ δ_ℓ ≤ 1/4` are used.
   For every d-local `f ≥ 0` and `t ≤ 1/4`:
   `E_ν f ≥ E_ω[e^{−Φ(ω)} f(y)]`, `Φ = log B(n,t,d) + (4/3)tM`. Here n is the
   number of replaced coordinates, M the light activated mass, and B an explicit
   binomial-extrapolation constant. Cor 2.6: with `t = d/(EM+4d)`,
   `EΦ ≤ d(O(1) + log⁺(EM/d))`, i.e. the weak ET Prop 2.4 form with the *mean*
   mass.
2. **Theorem 4.1 (PROVED):** ETw's sequential sieve limit (Thm 2.3′) accepts
   random step costs. Only `E_{Q'}Φ_j` enters.
3. **Theorem 4.5 (PROVED): `S_λ ≪_B λ^{3/4}` for every family of ℛ(M)-classes
   with `M ≤ P(M)^{1+B}`. It covers η-twin moduli, prime-power tops and any
   number of primes at one scale, and is unconditional.** It removes ETw §5
   "Not covered" item 1. It needs neither Conj 4.5_r, Conj 6.4, Hyp K2 nor
   Lemma 6.3, and it improves Prop 6.5 (no `log λ`). Ingredients are ETw
   Lemmas 1.3, 2.1′, 2.2, 2.6, 4.0, Prop 4.1 and Cor 4.3, applied verbatim,
   together with dyadic blocks on `(e^{λ^{1/4}}, e^{λ/2}]`.
4. **Conj 6.4 in its unweighted form: OPEN, and no longer needed.** Without the
   incident-weight hypothesis the mean-mass unweighted form is false (Remark 2.8,
   explicit example from the internal review). With the hypothesis it reduces to
   a tail statement, which is not attempted.

## The idea (one paragraph)

Couple σ with ν. Draw `c_ℓ ~ ν_ℓ`; if ℓ is light and `c_ℓ` lies in the
activated set (which is known before ℓ), replace it by a fresh draw off that
set. Freeze the whole path, and interpolate with independent coins `ρ_ℓ ~ Bern(t)`
on the replaced set R: use `y_ℓ` where ρ = 1 and `c_ℓ` otherwise. Then
`ρ ↦ f(y^ρ)` is a nonnegative polynomial of degree ≤ d, so symmetrising gives
a one-variable polynomial. Lagrange extrapolation from the binomial bulk to the
all-replaced point costs `B(n,t,d)` (Lemma 2.3). The thinned law is dominated
by ν up to the weight `exp((4/3)tM)` (a supermartingale argument, Lemma 2.4).
The k-ary structure enters only through "F_ℓ is known before ℓ".

## Internal review applied (O7-1, deep, hostile)

* **Blocking, fixed.** An earlier draft set `γ'(ℓ) = 4/3` in the moment
  lemmas. That breaks ETw Lemma 2.6, whose Euler products need
  `γ'(ℓ) − 1 ≪ ℓ^{−1/2}`. Now `γ'(ℓ) = (1−ℓ^{−1/2})^{−1}` throughout.
* **Simplification, adopted.** The draft used a "phantom" activation rule to
  make R independent of ρ. The reviewer pointed out that freezing the path
  already does this. The main line now uses the plain σ, so ETw's lemmas apply
  verbatim. The phantom rule is kept as a variant and is also tested.
* **Fixed.** The d = 0 definition of B; missing `1{light}` indicators;
  "multiply by W/B"; light-only sums; claims that overstated the numerics; the
  scripts now assert.
* **Added.** The weighted/unweighted distinction and the counterexample
  (Remark 2.8).
* The reviewer found no counterexample to Thm 2.5 or to the repaired Thm 4.5.
  They checked §3's constants, Thm 4.1's induction with random costs, and the
  Jensen step over histories with t depending on h.

## Evidence

* `kary_check.py`: 100 random small systems with unary, binary and ternary
  patterns, d ≤ 3 and up to 8 coordinates. All paths are enumerated and the
  LPs are solved in floating point. The weighted LP value is ≤ 1 for both rules
  and both t-choices, using the optimal 1-D constant `B* ≤ B`.
* `kary_b21_check.py`: (2.1) and (3.1) hold for the explicit node sets on 7128
  triples, with margins −5.66 and −7.47.

## Requests to the parent

* Hostile from-scratch review of §§2–4, especially Lemma 2.4 and Thm 4.5.
  This result closes the twin door of the 3/4 question for bounded B and
  should be double-checked before it enters STATUS/DISCOVERIES.
* Suggested ledger line: "(D)15: Thm 4.5 of EXCEPTIONAL_KARY: 3/4 cap for all
  bounded-B ℛ(M)-families, twins included (PROVED, internal). ETw Conj 6.4 is
  proved in weighted form for σ; the unweighted form is open."
* Natural next tasks:
  (a) uniformity in B (summation over B), since Thm 2.5 is B-free and only
      the moment constants depend on B;
  (b) mixed (a,D)/Case-A families: Thm 2.5 is arithmetic-free, so only the
      base and the moment lemmas are missing;
  (c) the unweighted Conj 6.4 under incident-weight bounds (now academic).
