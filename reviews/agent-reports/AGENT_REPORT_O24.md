# AGENT REPORT O24 — TC_θ above 3/4 (branch `side-agent/tc-theta`)

Deliverable: `EXCEPTIONAL_TUPLES2.md` (§§0–7 + Replay), scripts
`scripts/tuples2_{forced,allforms,translates}.py`, data `data/tuples2/`.
Self-review (deep reviewer subagent): verdict "needs revision"; all six
defects and the smaller items have been repaired (commits after 8882481).
The reviewer checked Lemma 1.1, Cor 1.2, Thms 2.1–2.2, Thm 4.1, Cor 6.1 and
Prop 7.1 as sound, and reproduced the §5 data byte for byte.

## Main finding (B, negative, with exact scope)

* **Forms (Lemma 1.1, PROVED).** Each class of 𝓡(ℓ) is `−r/s mod ℓ` with
  `rsm = (ℓ+1)/4`, and `n ∈ class ⟺ ℓ | ns + r`. The class −1 (form (1,1))
  lies in **every** 𝓡(ℓ), so its hits are prime divisors of the single
  integer n+1. T1's shift form hid this, because D = A_ℓ varies with ℓ.
* **Forced zeros (Cor 1.2, Thm 2.1–2.2, PROVED).** Tuples whose form-group
  has product > Ns + r have interval count 0 but positive CRT mass. In the
  TC_θ calibration this forced-zero mass at order
  `u₀ ≍ (log N)^{1−θ/2}` exceeds the TC precision η_K by `e^{K/(2e²)}` for
  **every θ > 2/3**.
* **Cor 2.3 (PROVED).** For θ > 2/3, TC_θ holds only if the admissible
  tuples carry an aggregate CRT excess ≥ N(Z − η). It is incompatible with
  "admissible tuples are CRT-accurate".
* **Assessment 3.2 (CONJECTURE, not proved).** The literal TC_θ is false
  for every θ ∈ (2/3, 1): the required excess is N^{1/2−o(1)} times the
  square-root noise floor and would come from unrelated multi-form tuples.
  So the expected failure threshold of the literal hypothesis is 2/3,
  not ≈ 1 (squares).
* **The door survives in repaired form (Thm 4.1, Cor 4.2, PROVED
  implications).** In the alternating sum the forced-zero correction is an
  Euler-characteristic term and cancels, two-sidedly:
  `|Σ_{j≤K}(−1)^j Z_j| ≤ 2εΠ(1−p) + 2e^{−K}` (4.1′). TC^𝔄_θ (CRT accuracy on admissible
  tuples) and TC^alt_θ (a one-sided Bonferroni/Brun-sieve bound) each imply
  `E(N) ≤ C N exp(−(2/e²)(log N)^θ)`. TC^alt is the correct form of the
  door. TC^𝔄 is itself expected false (floor deficits, Assessment).

## (A) Positive direction: none; precise requirement

* Cor 6.1 (PROVED from T1 Thm 3.1): the pure prime family's CRT cap is
  (log N)^{2/3}. So TC^alt_θ for any θ > 2/3 needs CRT accuracy for terms
  of modulus `exp(c(log N)^{3θ/2})`.
* Assessment 6.2: no known theorem reaches this (BV/EH/BFI/dispersion are
  below N; roots-of-congruence equidistribution is macroscopic and for a
  fixed polynomial; fixed-shift/form correlations are capped by T1 Prop 4.3;
  Kubilius holds only inside one form). The "tuple-count door" is Brun's
  sieve used beyond its level of distribution. No structured obstruction to
  TC^alt below θ = 1 was found.

## (C) T1 Cor 3.4 gap

Prop 7.1 (PROVED, reviewer-checked adaptation of K2 Thm 5.1's proof): for
K2 families with at most r primes per modulus in each dyadic block,
order-k majorants save at most `C(log N)^{3/4}(log log N)^{3/4} + Ckr(log log N)²`.
The real obstruction in general is many primes of one modulus in one
block, not the weights; the unbounded-r case is open (leak absorption not
attempted).

## Numerics (EVIDENCE)

At T1's test parameters, class −1 forced zeros alone exceed η_K by
10³–10⁵. T1 §5(b)'s moment deficits are an initial-segment effect: they
vanish on far translates `[t+1, t+N]`, t up to 10¹⁵. Single-form effects
give roughly a third of the deficit; this is an uncontrolled estimate.

## Suggested ledger update ((D)21 amendment)

"TC_θ (θ > 2/3) holds only if admissible tuples carry an aggregate CRT
excess ≥ N(Z_{u₀} − η_K) (EXCEPTIONAL_TUPLES2 Cor 2.3, PROVED); expected
false (Assessment 3.2). The correct hypothesis is the one-sided alternating
TC^alt_θ, which still implies the θ bound (Thm 4.1/Cor 4.2, PROVED
implication; essentially the Bonferroni majorant's conclusion itself). It
is non-CRT for every θ > 2/3 (Cor 6.1), and no known theorem supplies it."

## Open / for the parent

* Is a rigorous refutation of literal TC_θ for some θ < 1 within reach?
  It needs an upper bound for multi-form tuple counts above modulus N.
  I see no route.
* The unexplained remaining two thirds of the toy deficit (§5(c)) may come
  from two-form small-height relations. Untested.
* The unbounded-r case of the Cor 3.4 gap.
