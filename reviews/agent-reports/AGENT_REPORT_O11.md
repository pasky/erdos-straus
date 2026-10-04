# AGENT_REPORT_O11 — non-CRT inputs vs θ = 3/4 (checkpoint 1)

Branch `side-agent/noncrt-inputs-2`. Deliverable: `EXCEPTIONAL_NONCRT.md`,
`scripts/noncrt_checks.py`, `data/noncrt/checks_m8.txt`.

## Outcome
No θ > 3/4. Each of the three candidates is formalised and capped by a
proved theorem with exact scope. One conditional piece is isolated.

* **(a) signed rounding.** Thm 2.3 / Cor 2.4–2.5 (PROVED). Any bound
  `N·Eν + Σ_{θ≠0}|ν̂(θ)|w(θ)` with w ≥ 1 saves `≤ C(log N)^{3/4}` for the
  ET-file Cor 3.4 families. This covers Σ|a_i|, the sawtooth bound and all
  Gauss/Kloosterman/divisor-sum cancellation within a frequency. The new
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
  raises the bound by `O((log log N)²)`. So BV/BDH/EH/GRH-level inputs
  cannot beat 3/4. Rem 3.4 (Assessment): unconditional prime error terms
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
  about 1 min, under 1 GB.

## Suggested ledger text (parent's call)
(D)15: "Per-frequency signed rounding, prime-only majorants and CRT-evaluated
moment methods are all capped at (log N)^{3/4} for the Cor 3.4 families
(EXCEPTIONAL_NONCRT Thm 2.3, Thms 3.2–3.3, Props 4.1–4.2). PROVED,
internal. Open: inter-frequency cancellation; weights < 1 (H_eq);
non-CRT tuple counts."

Parent review should hit Prop 2.1 (the modified interpolation step) and
Lemma 2.2 hardest.
