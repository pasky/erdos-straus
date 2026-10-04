# AGENT_REPORT_O11 — non-CRT inputs vs θ = 3/4 (checkpoint 1)

Branch `side-agent/noncrt-inputs-2`. Deliverable: `EXCEPTIONAL_NONCRT.md`,
`scripts/noncrt_checks.py`, `data/noncrt/checks_m8.txt`.

## Outcome
No θ > 3/4. Each of the three candidates is formalised and capped by a
proved theorem with exact scope. One conditional piece is isolated.

* **(a) signed rounding.** Thm 2.3 / Cor 2.4–2.5 (PROVED). Any bound
  `N·Eν + Σ_{θ≠0}|ν̂(θ)|w(θ)` with w ≥ 1 saves `≤ C(log N)^{3/4}` for the
  ET-file Cor 3.4 families. This covers Σ|a_i|, the sawtooth bound as
  `min(N,1/(2‖θ‖))` and complete Gauss/Kloosterman/divisor sums within one
  frequency. It does not cover Vaaler/ψ or floor/ceiling rounding, or
  Kloosterman/dispersion cancellation over moduli (review N2, N3). The new
  tools are:
  * Prop 2.1: the Boolean sieve limit for arbitrary level, paying only the
    biased-Walsh tail above λ;
  * Lemma 2.2: the Walsh coefficient at S is bounded by the Fourier ℓ¹ mass
    on Θ_S.

  Side benefit: the ET-file's "slice primes ≤ N^{O(1)}" proviso (§6.1
  item 7) is not needed for prime-slice families.
* **(a″) weights < 1** (exact |S_N|, smooth windows): not covered. A
  reduction is given for smooth windows with Q₀ = 1 and hit-pattern
  majorants; it is conditional on an equidistribution conjecture (H_eq),
  (2.6). Open otherwise.
* **(b) prime-only majorants.** Thms 3.2, 3.3 (PROVED). These give the same
  LP limit under the Dirichlet measure. Detecting primality by a sieve
  raises the bound by `O((log log N)²)`. So majorants evaluated at level
  `N^{O(1)}` (BV/BDH/EH/GRH) cannot beat 3/4; prime moments of unbounded
  order are capped only via the Remark 3.4 Assessment (review N6). Rem 3.4 (Assessment): unconditional prime error terms
  are weaker than the integer count at this precision.
* **(c) moment/variance methods.** Prop 4.1: P∘f is a CRT majorant.
  Prop 4.2: a degree-k CRT mean saves only `O(k log log N)`, so
  Chebyshev/second moment gives θ = 0 (PROVED). The non-CRT moment route
  needs one of two things:
  * order `≥ (log N)^{3/4+δ}/log log N` tuple counts;
  * true moments that deviate from their CRT values.

  Elsholtz–Tao (Rem 1.3) already call order ≥ 2 out of reach.

## What remains (precise)
* Cancellation *between* frequencies, i.e. a direct count. §2.4 gives the
  dichotomy: either large high-level Fourier mass, or an interval count far
  below the CRT mean.
* Per-frequency weights < 1 for general majorants. Also (H_eq).
* Non-CRT tuple counting.
* Untouched here: balanced moduli and the sequential world of ET-file
  Thm 2.7. Thm 2.3 is prime-slice only.

## Checks
* Self-review by a deep reviewer subagent. Its defects were applied in the
  two "review repairs" commits. The main repair: the earlier claim that a
  θ>3/4 method *needs* superpolynomial Fourier mass was wrong, and is
  replaced by the §2.4 dichotomy. Other repairs:
  * Lemma 3.1 is one-directional;
  * the E* version of Lemma 2.9 uses Mertens on the slice part;
  * the R* selector;
  * the hypotheses of Thm 3.3;
  * the VK remark;
  * numerics labels.
* `noncrt_checks.py` checks Lemma 2.2 by floating-point enumeration on 40
  systems (max violation −1.7e−17). It also runs a toy LP comparing the
  coefficient budget with the Fourier budget (EVIDENCE, toy). Replay takes
  a few seconds, under 1 GB.

## Suggested ledger text (parent's call)
(D)15: "Per-frequency (complete-sum, w ≥ 1) signed rounding, prime-only
majorants at level N^{O(1)} (beyond: Assessment) and CRT-evaluated
moment methods are all capped at (log N)^{3/4} for the Cor 3.4 families
(EXCEPTIONAL_NONCRT Thm 2.3, Thms 3.2–3.3, Props 4.1–4.2). PROVED,
internal. Open: inter-frequency cancellation; weights < 1 (H_eq);
non-CRT tuple counts."

Parent review should hit Prop 2.1 (the modified interpolation step) and
Lemma 2.2 hardest.

---

# Follow-up 1 — inter-frequency cancellation (EXCEPTIONAL_NONCRT §8)

* **Thm 8.1 (PROVED).** Quantitative dichotomy. A direct count with saving
  `(log N)^θ`, θ > 3/4, needs one of two things at every level
  `λ ≤ c(log N)^{4θ/3}`:
  * high-level Fourier mass `> e^{−Cλ^{3/4}}/4`;
  * an interval count a factor `e^{s−Cλ^{3/4}}` below the CRT mean.
* **Lemma 8.2 / Cor 8.3 (PROVED, from notes Thm 60.1).** Forced classes
  with modulus `> 8⌊(N+1)/3⌋²` miss [1,N]. Hit-pattern majorants
  (Bonferroni, Selberg in indicators, P∘f) never gain from them.
* **Prop 8.4 (PROVED).** On [1,N], multiplier-one witnesses of all moduli
  have mean `≤ ¼(1+log N)²`. *Conj 8.5 (O((log N)²) for all moduli > N)
  was WITHDRAWN after review N12*: exact counts give ≍ 0.0133(log N)³, a
  constant factor ~1/17 below CRT. So branch (H) is not excluded on these
  grounds.
* **§8.3 (EVIDENCE, regenerated after N10).** Positivity is now imposed on
  0..200, and no truncation of the laws is asserted. For degree-≤10
  hit-count polynomials of the prime-modulus Case-B family, the exact
  interval optimum saves less than the CRT optimum in all 108 rows with
  Y ≥ N. Example: 4.21 against 11.75 at N = 30000 primes, Y = 3·10⁷. The
  round-1 inference "Δ_N < 0 for the family" is withdrawn (N11): for a
  fixed P the sign of Δ_N varies, and the interval-optimal P has mild
  Δ_N > 0. The LP values are lower bounds on optimal savings (HiGHS at
  degree 10).
* **Prop 8.6 (PROVED) / Cor 8.7 (CONDITIONAL on H_node, untested).**
  Beating 3/4 by exact interval counts of hit-*count* polynomials needs
  degree `≥ (log N)^{3/4+o(1)}`, under the hypothesis
  `m ≥ 16(log N)^{3/4+δ}` (N13). §8.3 does not test this (N14).
  Non-symmetric hit-pattern majorants are not covered.
* **Bottom line.** No structured family was found with an inter-frequency
  gain. Still open:
  * branch (H);
  * high-degree count polynomials;
  * non-symmetric hit-pattern majorants;
  * multiplicative / a-frame weights.

Replay: `uv run --with scipy python scripts/noncrt_interval.py N Ymax
[all|nonsquare|prime]`. Each run takes seconds and < 1 GB; outputs are in
`data/noncrt/interval_*.txt`.

Review round 2 (N9–N14) applied: Lemma 3.2 classes are handled directly
in §8.2 (N9); HCAP and truncation (N10); the Δ_N inference (N11);
Conj 8.5 and its Assessment withdrawn (N12); the m-hypothesis of Cor 8.7
(N13); "numerical check" removed (N14); stale runtimes fixed.

---

Review `reviews/exceptional-noncrt-review.md` (branch side-agent/review-noncrt):
N1–N8 applied in one commit. The changes: finite 𝒫; scope of the sawtooth
bound and of Kloosterman cancellation; R*-term = 0; the Thm 3.3 increment;
the prime-moment clause downgraded to an Assessment beyond level A log N;
the constant `19k(2+log⁺)`; numerics labels. Lemma 2.2 now reports max
ratio 0.923.
