# AGENT_REPORT_O18 — inter-frequency cancellation door (checkpoint 1)

Branch `side-agent/interfreq`. Deliverable: `EXCEPTIONAL_INTERFREQ.md`.
Scripts: `scripts/interfreq_selberg_check.py`, `scripts/interfreq_hitpattern_lp.py`.
Data: `data/interfreq/`. No θ > 3/4. Main/STATUS/DISCOVERIES untouched.

## Results

1. **Thm 2.2 (PROVED, classical tool).** Let ν ≥ 0 on ℤ have every
   nonzero frequency of denominator ≤ D < N. Then
   `Σ_{n≤N}ν ≥ (N−D)Eν`. The proof uses a Selberg minorant plus Poisson,
   and an exact LP check for D ≤ 8 confirms it.
2. **Cor 2.3 (PROVED, K2 proviso).** Majorants built from classes of
   modulus ≤ N/2 save `≤ C(log N)^{3/4}(log log N)^{3/4}` for every K2
   forced-class mixture. Coefficients may be of any size and the interval
   sum may be evaluated in any way: exact, dispersion, Kloosterman,
   Vaaler, floor/ceiling, smooth windows, any Q₀.
3. **Thm 2.5, the hybrid cap (PROVED, K2 proviso).** Any bound
   `B ≥ Σ_{n≤N}ν` with `Σ_{d_i>N/2}|a_i| ≤ cB` saves
   `≤ log(2+12c) + C(log N)^{3/4}(log log N)^{3/4}`. This strictly contains
   K2 Cor 6.1, where c = 1 and B ≥ Σ|a_i|. Classes of modulus ≤ N/2 cost
   nothing, however they are treated.
4. **Prop 3.1/3.2 (PROVED).** By LP duality, the exact-interval value of
   level-λ hit-pattern majorants depends only on interval correlation
   counts. By Jensen, averaged over shifts it is ≤ the CRT value. "ν ≥ 0
   on ℤ" means G ≥ 0 on the whole cube, so patterns absent from [1,N] cannot
   be exploited.
5. **§3.3 reduction.** Above N/2 the inter-frequency door is the non-CRT
   tuple-count door. One must count n ≤ N with prescribed sets of witnesses
   of combined modulus > N/2, better than termwise.
6. **(H_eq).** Lemma 4.1 shows a polynomial loss N^{−A} suffices. Lemma
   4.2 gives a sufficient condition via window correlations. (H_eq) is
   **neither proved nor disproved**, and it is not needed when all moduli
   are ≤ N/2.
7. **§5 (needed input).** BV/BFI/DI/Zhang-type remainder estimates at
   moduli ≤ N/2 are useless for the integer count, whatever their
   strength (Thm 2.5). The input that would be needed is correlations of
   ES witnesses of growing order above modulus N. No such technique is
   known (Assessment).
8. **§3.2 (EVIDENCE, toy).** Full hit-pattern LPs on 12 primes: the
   interval is within 0.005 of CRT up to Q = N. Above N the deviations
   have either sign, mostly gains at Q = N². [1,N] is never the best of
   three shifts.

## Self-review

A deep reviewer subagent found no refutation. It reported nine defects:
overclaimed scope in the verdict and §5, the Lemma 4.1 cutoff, Thm 2.5 case
handling, a CRT lower bound in Prop 3.1 that needs the ES-family hypothesis,
over-read numerics, level vs modulus in §4, Lemma 4.2 being sufficient only,
a switching counterexample (an unrestricted (a,D)-class adds hits in
[1,N]), and incomplete replay data. All nine are repaired (commits
"review repairs"). The reviewer checked Thm 2.2, Lemma 2.4 (constant 6) and
the restricted ET Lemma 2.9 step as sound.

## Points for the parent's hostile review

* Thm 2.5 mean side: ET Lemma 2.9 is applied only to terms of level
  > log(N/2), after the K2 projection. Check that the projection cannot
  raise levels.
* Novelty: Thm 2.2 is essentially classical (the dual of the large
  sieve). The new content is its use with the K2 cap: Cor 2.3 and Thm 2.5.
* Suggested ledger entry (D)19: "Inter-frequency cancellation below
  modulus N/2 is worthless (Selberg minorant). Every method charging
  classes of modulus > N/2 at coefficient cost is capped at 3/4 (Thm 2.5).
  Above N/2 the door reduces to multi-witness tuple counts. (H_eq) is
  open, needed only above N/2."

## Open / next

* (H_eq) above level N/2. A proof would need the short-window
  distribution of hit sets of combined modulus > N.
* Prime-only analogue of Thm 2.5. Lemma 2.4 is a statement about
  integers; BV-type prime remainders at d ≤ N/2 are not covered here.
* Majorants ≥ 0 only on [1,N] remain excluded (Thm 2.2 needs ν ≥ 0 on ℤ).
