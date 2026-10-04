# AGENT_REPORT_O18 — inter-frequency cancellation door (checkpoint 2)

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
3. **Thm 2.5 + Rem 2.6, the coefficient-budget cap (PROVED, K2 proviso,
   family primes ≤ N^A).** Any bound `B ≥ Σ_{n≤N}ν` with `T_>^* ≤ cB` saves
   `≤ log(2+12c) + C(log N)^{3/4}(log log N)^{3/4}`. Here T_>^* is the least
   coefficient mass on moduli > N/2 over representations of ν, and c may be
   as large as `exp(O((log N)^{3/4}(log log N)^{3/4}))`. The same order of
   cap holds whenever `T_>^* ≤ (N/24)exp(−C(log N)^{3/4}(log log N)^{3/4})`,
   whatever B is. This contains K2 Cor 6.1 (c = 1). **Hybrid methods (any
   evaluation below N/2, trivial count `N/d_i + O(1)` charged per class
   above N/2) are NOT proved to be capped**, since their bound can be ≪ T_>.
   This is a proof gap, not a refutation.
4. **Prop 3.1/3.2 (PROVED).** By LP duality, the exact-interval value of
   level-λ hit-pattern majorants depends only on interval correlation
   counts. By Jensen, averaged over shifts it is ≤ the CRT value. "ν ≥ 0
   on ℤ" means G ≥ 0 on the whole cube, so patterns absent from [1,N] cannot
   be exploited.
5. **§3.3 (Assessment, not a theorem).** Read via the contrapositive of
   Thm 2.5, the remaining door is the non-CRT tuple-count door. One must count n ≤ N with prescribed sets of witnesses
   of combined modulus > N/2, better than termwise.
6. **(H_eq).** Lemma 4.1 shows a polynomial loss N^{−A} suffices. Lemma
   4.2 gives a sufficient condition via window correlations. (H_eq) is
   **neither proved nor disproved**, and it is not needed when all moduli
   are ≤ N/2.
7. **§5 (needed input).** BV/BFI/DI/Zhang-type remainder estimates are
   capped for the integer count, whatever their strength, in two cases:
   on majorants whose moduli are all ≤ N/2 (Cor 2.3), and inside methods
   whose bound dominates T_>^*/c (Thm 2.5). They are not shown to be capped
   inside hybrid methods. The input that would be needed is correlations of
   ES witnesses of growing order above modulus N. No such technique is
   known (Assessment).
8. **§3.2 (EVIDENCE, toy).** Full hit-pattern LPs on 12 primes: the
   interval is within 0.005 of CRT up to Q = N. Above N the deviations
   have either sign, mostly gains at Q = N². [1,N] has no systematic
   advantage over shifted windows (it is best at Q = N and worse for
   Q ≥ N^{5/4}).

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
* Suggested ledger entry **(D)20** (since (D)19 is taken): "Inter-frequency
  cancellation is worthless for majorants built from classes of modulus
  ≤ N/2 (Selberg minorant, Cor 2.3; any coefficients, any evaluation).
  With larger classes present, the cap holds for methods whose bound
  dominates T_>^*/c, c ≤ exp(O((log N)^{3/4}(log log N)^{3/4})), where
  T_>^* is the minimal coefficient mass on moduli > N/2 (Thm 2.5,
  Rem 2.6). It is **not** proved for hybrid methods that charge large
  classes only their trivial count. (Assessment) what remains is
  multi-witness tuple counting. (H_eq) is open; it is not needed when all
  moduli are ≤ N/2. PROVED (internal; review
  `reviews/exceptional-interfreq-review.md`, SOUND-WITH-REPAIRS)." 

## Hostile review (round 1) repairs

`reviews/exceptional-interfreq-review.md` found Thm 2.2, Cor 2.3, Lemma 2.4,
Thm 2.5, Props 3.1/3.2 and Lemmas 4.1/4.2 SOUND. All defects are repaired.
* D1 (MAJOR, scope): the hybrid-method claim was withdrawn everywhere (§0,
  Scope → Rem 2.6, §5(i), report, ledger text). The gap is stated
  explicitly, with the review's suggested route.
* D2: `T_>^*` (infimum over representations) is used in all door
  statements.
* D3: Cor 2.3 is contained in Thm 2.5 only for families with primes
  ≤ N^A.
* D4: Rem 2.6 adds that T_>/N binds and that c may be as large as
  `exp(O(S_max))`.
* D5: numerics text corrected ([1,N] is best at Q = N; Thm 2.2 is vacuous
  at Q = N; the squares explanation is labelled unverified).
* D6: §3.3 relabelled Assessment, with its scope mismatch noted; the
  `e^{−c(log N)^3}` remark is labelled heuristic.
* D7: B notation in §5(ii), the majorant/minorant constant in Rem (ii),
  the docstring `\n`, and the ledger number (D)20.

## Open / next

* Close the hybrid gap (Rem 2.6, last bullet). The route is
  `Σ_{n≡b (d)}(1_{[1,N]} − F)(n) ≤ 1 + N/(2d)` for d > N, plus F ≥ 0 on
  [1,N]; the review gives numerics only. Even then the mean side needs
  `T_> ≤ N^{O(1)}`.

* (H_eq) above level N/2. A proof would need the short-window
  distribution of hit sets of combined modulus > N.
* Prime-only analogue of Thm 2.5. Lemma 2.4 is a statement about
  integers; BV-type prime remainders at d ≤ N/2 are not covered here.
* Majorants ≥ 0 only on [1,N] remain excluded (Thm 2.2 needs ν ≥ 0 on ℤ).
