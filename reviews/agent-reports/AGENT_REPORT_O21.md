# AGENT REPORT O21 — tuple-count / witness-correlation door (checkpoint 1)

Branch `side-agent/tuple-door`. Deliverable: `EXCEPTIONAL_TUPLES.md`, with
`scripts/tuples_moments.py`, `scripts/tuples_checks.py` and `data/tuples/`.
No θ > 3/4 is claimed unconditionally. ES is not solved.

## Results

1. **Formalisation (PROVED, §1).** Order-k witness correlations are
   `S_k(N) = Σ_{n≤N} binom(f(n),k)` with CRT prediction `N m_k`. For the
   prime family (`𝓡(ℓ)`, ℓ ≡ 3 mod 4, ℓ ≤ y), Lemma 1.3 rewrites them as
   k-point correlations of ω-type functions `ω_{y,D}(n+4D)` along shifts
   `4D`, `D | ((ℓ+1)/4)²`.
2. **Conditional implication (PROVED implication, §2).** Hypothesis
   TC(N;K,y,η) says `|S_j − N e_j(p)| ≤ ηN` for j ≤ K. It gives
   `#{f_y=0} ≤ N(Π(1−p) + e_K + Kη)` (Bonferroni). At `μ_y ≈ K/e²` and
   `η = e^{−K/e²}/K` this is `E(N) ≤ (e+2)N e^{−K/e²}`. Hence
   **TC_θ ⇒ E(N) ≤ N exp(−(2/e²−o(1))(log N)^θ)** (Cor 2.3).
   * TC is a theorem for `K ≤ c(log N)^{2/3}` (Prop 2.4; Brun, recovers
     2/3), so TC_θ holds for θ < 2/3.
   * TC is false for even `K ≥ (e²/2+ε) log N`, because squares avoid
     every class (Prop 4.2, Jacobi argument). TC_θ at θ = 1 itself is not
     decided.
   * TC_θ for 3/4 < θ < 1 is the open CONJECTURE: natural and
     falsifiable.
3. **No-go for bounded order (PROVED, §3).**
   * Thm 3.1 is ET Prop 2.4 with truncated weights `min(log ℓ, L₀)`. It
     gives, for prime-slice ES families (ET Cor 3.4 hypotheses), majorants
     whose terms have level ≤ A log N *or* at most k slice primes: saving
     `≤ C[(log N)^{3/4} + k log log N]` (Cor 3.2) when evaluated with CRT
     main terms.
   * So bounded-order correlation input, of any precision, cannot give
     θ > 3/4. Saving `(log N)^θ` needs order `≥ c(log N)^θ/log log N`;
     with item 2, order `(log N)^θ` suffices. The order is pinned down
     up to `log log N`.
   * For all K2 families there is a weaker version from K2 Thm 5.1:
     order `≥ (log N)^{4θ/3−1−o(1)}` is needed (Cor 3.4).
4. **Literature (§4, Assessment).**
   * Heath-Brown/Deshouillers–Iwaniec (Σττ), the triple correlations
     (averaged only), Matomäki–Radziwiłł–Tao and Tao–Teräväinen all have
     a fixed number of shifts. That axis is distinct from witness order.
     Prop 4.3 (PROVED): any information about a fixed set of r shifts
     saves at most `2r(log log N + O(1))` under CRT-main-term
     evaluation. EH-type level results live below N.
   * The Kubilius model is all-order but single-shift. Prop 4.1 (PROVED):
     the ES hit vector has entropy `≍(log y)³`, so no total-variation
     model holds once `log y ≥ C(log N)^{1/3}`.
   * No known theorem or standard conjecture supplies TC_θ for any
     θ > 2/3.
5. **Numerics (EVIDENCE, toy, N ≤ 10⁸).**
   * The avoider excess over CRT is positive and rises with y towards
     the square density. A random-non-residue control reproduces it.
   * For y ≤ 1000 and j ≤ 12, moments above N are a few % below CRT and
     approach it as N grows. This is not uniform (y = 3000 fluctuates).
   * The TC test at the supplied y passes for y ≤ 100 and fails for
     y ≥ 300. The random control fails too, so this is not
     ES-specific.

## Self-review (deep reviewer subagent, round 1)

Seven defects were found, all repaired:
* the TC_θ endpoints were overstated;
* fixed shift count was conflated with witness order (Prop 4.3 added);
* `y_K` was ill-defined, and the numerics used the supplied y, not `y_K`;
* the avoider-excess and moment-deficit claims were overstated;
* the random-control explanation was unsupported;
* the selector hypothesis in Cor 3.3 was missing;
* even K was missing in Prop 4.2.

The reviewer confirmed that Thm 3.1 (truncated weights in ET Prop 2.4),
Cor 3.2's parameters, Prop 4.1 and Prop 4.2 are sound.

## Points for the parent's review

* Thm 3.1: check that ET Prop 2.4/Thm 2.5 really allow c-independent
  arbitrary weights with the Jensen step unchanged (NC Thm 2.3 already
  does this with other weights). Check also the Cor 3.2 parameter choice
  `L₀ = λ₀/k`, `α = max(λ₀^{−1/4}, 3k log(A log N)/λ₀)`.
* Cor 3.3 scope: it covers methods whose bound is ≥ ½N·Eν (CRT main
  terms asserted). Exact low-level evaluation with a large favourable
  rounding deficit inside a *mixed* majorant is not covered (stated).
* The §4.2 literature table is from memory, apart from Tenenbaum/Kubilius
  and Ford 2408.03803, which were checked online. It is used in no proof.
  Dates/exponents may deserve a check.
* Suggested ledger entry: (D)20 "tuple-count door" (Cor 3.2–3.4 PROVED;
  Cor 2.3 CONDITIONAL on TC_θ; Prop 4.1–4.3 PROVED).

## Replay

See `EXCEPTIONAL_TUPLES.md` §Replay. `scripts/tuples_checks.py` takes
about 3 s. The moments runs take about 1 min each at N = 10⁸, under 3 GB.
