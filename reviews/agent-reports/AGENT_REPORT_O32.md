# AGENT REPORT O32 — window statistic from above (branch `side-agent/xwin-average`)

Deliverable: `POINTWISE_XWIN.md`; scripts `scripts/xwin_checks.py`,
`scripts/xwin_tail_table.py`; data `data/xwin/`. Not merged.

## Results

1. **Lemma 1.1 (half-set lemma, PROVED).** For any `a≡3 (4)` (prime or
   composite), failure of `−1∈Rat_a(x)` forces all prime factors of x into
   one of `2^{β(a)}` explicit sets of exactly `φ(a)/2` classes (Klein-group
   orbits `{g,g⁻¹,−g,−g⁻¹}`, using only 1- and 2-prime ratios). No
   budget exceptions — this removes the F3 obstacle of notes (71.4) /
   POINTWISE_WINDOW Lemma 6.1.
2. **Theorem 1.2 / Cor 1.3 (PROVED).** For every fixed set A of windows,
   `#{p≤N: all a∈A fail}≪_A N/(log N)^{1+|A|/2}`; so
   `T(N,Z)=#{a_min>Z}≪_Z π(N)(log N)^{−J(Z)/2}` — the random model's exact
   exponent. Improves notes Cor 71.4 (`δ_J≈½log log Z`) and turns
   POINTWISE_WINDOW §6's joint-dimension Assessment into a theorem.
   **Cor 1.4:** `#{a_min≥7}≍x/(log x)^{3/2}`; `#{a_min≥11}≍x/(log x)^2`
   on EH (W2 is sharp). Census evidence (§1.3) flat at this scale.
3. **Theorem 1.5 (PROVED; SW only for moduli `≤(log y)^{1/2}`).** Uniform
   for `Z≤C_0 log log N`: exponent exactly `1/2−o(1)` per window for
   `Z=o(log log N)`; `N exp(−(π²/(64 log 2)−o(1))(log log N)²)`
   (`0.2225…`) at `Z≈3.56 log log N`.
4. **§2 (Lemma 2.1, Thm 2.2, Cor 2.3; PROVED mod SW): NOT a new frontier.**
   A prime-side pattern-summed large sieve gives
   `T(N,(log N)^θ)≤N exp(−(d(θ)/4−ε)(log N)^θ log log N)` for every
   `θ<θ_*=log3/(1+log3)`, explicit `d(θ)` (`≥4(1−θ)/9` for θ≤2/11).
   **Priority:** notes Thm 14.4/14.9 already imply this window tail (their
   sufficiency step is a signed witness at window `w≤W`); Lemma 2.1 =
   notes Lemma 12.5. My contribution there is an independent second proof
   by a different architecture with explicit constants — useful as a
   cross-check since DISCOVERIES (A)5 lists Thm 14.9's review status as
   "not stated". I initially missed §14; the deep self-review caught it.
5. **Goal-1 answer.** "o(π(x))" holds trivially with f=3 (notes Thm 70.9).
   Best window tail: `f=(log x)^{θ_*−σ}`, exceptional set
   `x exp(−c(log x)^{θ_*−σ}log log x)` (notes 14.9; re-proved here). Exact
   exponents for fixed Z: new (item 2).
6. **Goal 2.** Trivial density-1 sets exist (window 3) but are certified by
   a bounded procedure; inside thin hard families (W1, W2) the next window
   already wins almost always (by Thm 1.2). The meaningful question reduces
   to Ω-type lower bounds for `|F_K|` (O29 side). No new set.
7. **Goal 3.** Seeded windows: only a proposed adaptation, expected weaker
   than Cor 2.3; nothing specific to X_QNR.
8. **Goal 4.** GRH only removes ineffectivity/δ-loss; EH does not help this
   argument. Prop 3.2 (scoped): Lemma-12.1-type window majorants under the
   level constraint cannot go below `N^{1−1/e}` — an obstruction for that
   majorant class only, not for sieve methods in general nor against the
   conditional notes Thm 71.6. No "ES ⇐ standard hypothesis" found.

## Review status

One deep self-review (reviewer subagent): no fatal issues in Lemmas 1.1,
2.1, Theorems 1.2, 2.2; majors fixed: priority vs notes §14 (rebaselined),
2/5 was not the method's barrier (capped Poisson ⇒ θ_*), dyadic step,
GRH floor `y>Z`, piecewise per-window exponent, Goal-2 misframing, seeded
"verbatim" claim, Prop 3.2 overreach; minors fixed (ρ lower-bound remark,
`F_a` pattern-sum vs majorant notation, scripts now exit non-zero on
violations). Theorem 1.5 was added after that review.

**Hostile review R32** (`reviews/pointwise-xwin-review.md`, branch
`side-agent/review-xwin`): Lemma 1.1, Thm 1.2/Cor 1.3, Lemma 2.1,
Thm 2.2/Cor 2.3 SOUND; census table reproduced bit-for-bit. Repairs
applied, one commit each:
* MAJOR-1: Thm 1.5 now stated for `3≤Z≤C_0L` (the advertised `Z≈3.56L` is
  inside); MINOR-3: constant written `π²/(64log2)−o(1)`, with the
  optimisation shown.
* MINOR-1/2: Cor 1.4 lower halves labelled "PROVED modulo the sieve
  theorems cited for W1" / "CONDITIONAL on EH"; counts restricted to
  `p≡1 (24)` (with a note on `p=4t+1`).
* MINOR-4: Chernoff term uses the Poisson mean `λ+η`.
* MINOR-5: `ρ_k≥2^{−k}` for every `a≡3 (4)` via the kernel of `(·/a)`.
* MINOR-6: §3.3 GRH and EH bullets labelled Assessment; GRH floor
  `y=ℒ^C` with `C>2θ`.

## Suggested ledger entry (for the parent to decide)

(H)17: Half-set lemma; fixed-set window stacking with exact exponent
`J/2` (`T(N,Z)≪_Zπ(N)(log N)^{−J(Z)/2}`), uniform for `Z=o(log log N)`;
two-sided orders for `a_min≥7` (uncond.) and `a_min≥11` (EH). PROVED
(mod SW for the uniform version). Window tail for `θ<θ_*` re-proved
independently (prime-side), priority notes Thm 14.9.
