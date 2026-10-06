# AGENT_REPORT_O67 — (CC)/(A*) for residue-dense multi-rough classes (checkpoint 1)

Branch `side-agent/astar-dense`; deliverable `EXCEPTIONAL_LARGESIEVE5.md`
(LS5), script `scripts/largesieve5_cover_toy.py`.

**Verdict:** (CC)/(A*) is **not proved** for large supports. The checkpoint
contains four proved structural steps and one finding that redirects the
approach. It also gives a precise diagnosis of what is still missing, and
toy evidence that (CC) is true.

## Proved

1. **Lemma 1.1: the full family suffices.** Large-sieve caps pass down to
   subfamilies. So (A*) is needed only for the full forced family `𝔊_X`,
   uniformly in X. No adversarial selection of moduli has to be handled.
2. **Lemma 1.2: rational labels.** Every forced class (ℛ, (a,D), Case A,
   selector) is `−r/s mod G`. Two *distinct* labels that are congruent mod g
   have `H₁H₂ ≥ g/2`. So a residue class mod g contains at most one label of
   height `< √(g/2)`.
3. **Prop 2.1: a tilted fibre law.** Use `σ ∝ Q'·1_𝒜·e^{−2Σw_ℓp̃_ℓ}`.
   Its damped collision is `≤ Z^{−2} ≤ e^{6m_c+1}`. This is LS4's (B), but
   without the global threshold event `G_B`. LS4 Thm 4.2 and Thm 5.2 hold
   verbatim with this law.
4. **Lemma 3.1: label partition.** In the product model,
   `P(E_S) = Π_{ℓ∈S}ℓ^{−1} ×` (a sum over partitions of S and *distinct*
   labels). Same-label coincidences, the "structured" case of LS4 §3.2,
   collapse exactly.

## Findings that matter for the route (Assessment)

* **Rem 2.2: LS4's conditioning is the wrong law for the pivotal method.**
  In the full family, every value of every rough coordinate changes the
  activated sets at many later tops. So under the threshold-conditioned law
  `σ_B` a single coordinate can flip `1_{G_B}`. The pivotal bound then gives
  decay from only one prime, not `Π_{ℓ∈S}`. The tilt removes this: each
  activation at a top q is paid `≤ 2w_q/q`.
* **§4 (S): pointwise divisor-in-residue-class bounds do not suffice.**
  Lenstra, Coppersmith–Howgrave-Graham–Nagaraj and Shiu do not close (CC)
  by themselves. The witness weight of a label splits into two parts:
  * a "long" part, uniform in the modulus and harmless;
  * a "short" part: one witness with outside cofactor `< 4D^♮`, of weight up
    to 1, for every label however high.

  In the overlap sums one then needs `Σ_{g|L}` (labels ≡ c mod g) `≪ 1`
  over the `2^{ω(L)}` divisors g. Short witnesses defeat any sup-over-c
  bound. What is needed is an **averaged label-pair correlation**, averaged
  over the moduli and labels of both blocks, not a pointwise divisor bound.
  This is stated as **(LCH)**, a CONJECTURE that suffices for (CC) in the
  product model.
* The remaining correlations are of two types:
  * (C2): cross-label coincidences at S-primes. The trivial bound
    `4^{|S|}` per prime is fine only for `|S| ≤ (1/2−γ)log₂ z`.
  * (C3): sharing of outside primes. Without compatibility this costs
    `(C log X)^{2^k}`.

  Cor 4.2 ((CC) for `|S| ≤ c₀ log log N`) is only a **SKETCH**. Its gap is
  the k-th moments of `τ(A²_{Qe})` over shared prime sets.

## Evidence

Exact enumeration on the full ℛ(M) family over 6 primes (1428 classes,
`4.5·10⁷` points):
* Lemma 1.2 checked: minimum ratio 2.0 against the required 1.
* `P(E_S)/Π P(ℓ covered)` is at most 4.09 for |S| = 4, i.e. a per-prime
  correlation loss of at most 1.42. This is consistent with (CC) at a
  bounded K. It is toy scale only.

## Not done / open

* (A*) and (CC) for large |S|. The gap is now located precisely, in (C2)/(C3)
  with short witnesses.
* The transfer from the product model to the fibre law. This needs a "soft
  pivotal" lemma for the tilted law, so that the top is paid by `w_q/q`.
  It also needs the smooth-part uniformity over S that Markov does not give
  for free.
* No counterexample. The random-residue model and the toy data both predict
  (CC).

## Decision requested from the parent

Three options:
* **(a)** Continue on (LCH): a global, multi-block averaged sum over labels
  and moduli, built from Shiu-type averages over moduli. This is research
  level. A natural first target is k = 2 blocks with large S.
* **(b)** Formalise the soft-pivotal transfer, plus Cor 4.2, as a modest
  rigorous partial theorem: all-level cap for frequencies with
  `≤ c log log N` rough primes.
* **(c)** Stop here. The checkpoint records the obstruction analysis.

Replay: see LS5 §Replay; the run takes about 1 minute.
