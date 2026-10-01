# AGENT_REPORT_C2: unconditional superlinear Ω-result for W(p) (checkpoint 1)

Branch `side-agent/pointwise-omega`. All work is in this worktree; nothing
has been merged. The deliverable is `POINTWISE_OMEGA.md`.

## Outcome

**Theorem 5.1.** For infinitely many Mordell-hard primes,
`W(p) ≥ (log p)^2·exp(−C log log p/log log log p)`. In particular:

* `W(p) > (log p)^{2−ε}` i.o. for every ε;
* `W(p)/log p → ∞` along a sequence;
* for every large T, `log L_h(T) ≤ T^{1/2+o(1)}`.

**Status: PROVED modulo one cited theorem; effective.** The cited theorem is
Thorner–Zaman, Math. Z. 306 (2024), Cor. 1.4 (arXiv:2108.10878v2). Its
statement was read in the archived PDF/text under `sources/lit2026/`.

* Siegel zeros are handled; there is no caveat.
* Chang's theorem is not used.
* The previous record was `(5/8−ε) log p` (POINTWISE_SIZE Thm 11.2).
* This refutes `H_MOD(A)` (notes (51.19)) for every `A<2`. Before, only
  `A<1` was refuted.

## The proof

1. **Prime-local reduction (Lemma 2.1).** Impose the class of one modulo all
   prime powers `≤T` of primes `≤y`, with `y=T^{1/2+o(1)}≥√T`. Every
   surviving modulus `M≤T` then has exactly one free prime ℓ. The residual
   system is "`n mod ℓ ∉ F_ℓ`", with
   `F_ℓ={−4D mod ℓ : D|A_{mℓ}², m | 4D+1}`.
2. **The new input (Lemma 2.3, PROVED).** The sieve mass satisfies
   `S=Σ|F_ℓ|/(ℓ−1) ≤ T^{o(1)}`.
   * Write `D=sr²`, `A=srk`. The congruences force `m | r+k`, and this saves
     the factor m.
   * The crude bound underlying POINTWISE_SIZE Lemma 11.7 is
     `S≤T^{1/2−η+o(1)}`. That was exactly the bottleneck of Assessment 11.6,
     which therefore stopped at a linear range.
   * Numerically `S≈0.054(log T)^{2.5}` for T up to `10^6`.
3. **Brun pure-sieve minorant.** The minorant is a Bonferroni truncation of
   degree `J≍S`. Its moduli are `Q·d` with `log ≤ 3y`. Its ℓ¹-mass is `e^S`
   and its mean is `≥ e^{−2S}`.
4. **Transfer (Theorem 4.1, a general criterion).** This uses Thorner–Zaman
   Cor. 1.4, a Linnik-range PNT with relative error that is scaled by the
   exceptional factor λ, i.e. with Deuring–Heilbronn built in.
   * Lemma 3.2 shows that at most one "severe" real character exists across
     the whole family of moduli, via McCurley's region applied to lcm's of
     two moduli.
   * Case A: its conductor divides Q. Then λ is common to all terms and
     cancels.
   * Case B: otherwise. Then a twisted mean appears, and it is small.
   * Result: `log p ≪ log Z·S ≈ y·T^{o(1)} = T^{1/2+o(1)}`.

Note on the brief's step (ii). PNT uniform only for `q≤exp(c√log x)` would
give back the linear range. The Linnik range `x≥q^{12}` is essential.

## Precise obstruction above exponent 2 (§6)

* **Prop 6.1 (PROVED).** Every prime-local class-of-one design has
  `log p ≥ (1/√3−o(1))√T`. So exponent 2 is the ceiling of this method.
* **Hypothesis H_MIN(θ).** A pointwise congruence minorant for the
  non-prime-local residual system, with:
  * modulus budget `T^{θ+o(1)}`;
  * `log(mass/mean) ≤ T^{o(1)}`;
  * a twist condition.

  This is a purely combinatorial CRT statement in which primes do not enter.
  **Theorem 6.2 (PROVED):** H_MIN(θ) implies `W > (log p)^{1/θ−ε}`. A
  polylogarithmic H_MIN gives `W > exp(c(log p)^{1/(2A)})`. So the
  correlation wall (iv) is the only remaining gap: (ii) and (iii) are solved
  by Theorem 4.1.
* **Prop 6.3 (PROVED, raw atom list).** Event-level Bonferroni fails for
  `θ<1/2` at degrees `4.2θ²(log T)² ≲ J ≤ T^θ`. The cause is hub classes
  (`−4`, `−4d²`, …), on which `K_{r,r}` many two-prime atoms fire together.
  * EVIDENCE: after deleting atoms implied by single-prime atoms, 51–65% of
    the multi-prime atoms remain. Hub classes `−16, −36, −12` keep about 300
    irredundant edges each at `T=10^5`.
  * That the deduplicated hub graphs contain `K_{r,r}` asymptotically is
    **not** shown.

## Self-review

A reviewer subagent ran a deep, hostile review. Its findings:

* The exponent-2 argument survives. It checked the citation lines and
  Lemmas 2.1, 2.3 and 3.2, Theorem 4.1, and the Bonferroni sign.
* Six defects were found in §§0, 5 and 6. All six are repaired, in commit
  "self-review repairs":
  * Prop 6.3 was false without an upper bound on J;
  * Theorem 6.2's polylogarithmic exponent should be `1/(2A)`;
  * a twist constant was off (0.7 → 0.69);
  * a sign `(−1)^r` was missing;
  * distinctness of the primes now uses `p>Q`;
  * the headline transfer bound needed its `K·max(log Z,K)` form.
* The scripts now exit nonzero on failure. Atoms with a prime-power free
  part are now separated from genuinely multi-prime atoms.

## Things the parent should check hardest

1. The citation: Thorner–Zaman Cor. 1.4 together with Remark 1.5 and the
   McCurley quotation, in `sources/lit2026/arxiv-2108.10878-thorner-zaman-pntap.txt`
   lines 37–39 and 121–131. In particular, check that the O-term is relative
   to `λx/φ(q)`, with absolute constants.
2. Lemma 3.2 (uniqueness of the severe character across a family) and the
   Case A/B split in Theorem 4.1.
3. Lemma 2.3, especially the involution and the identity `m | r+k`.
   `pointwise_omega_check.py lemma` checks the algebra. Lemma 2.1 is checked
   by `local`, with 0 mismatches.

## Suggested ledger entries (for the parent to place)

* **(H)-new.** Theorem 5.1: `W(p) ≥ (log p)^{2−o(1)}` i.o. and
  `log L_h(T) ≤ T^{1/2+o(1)}`. Label: PROVED modulo Thorner–Zaman Cor. 1.4;
  effective.
* **(H)-new.** Lemma 2.3: the prime-local mass is `T^{o(1)}`. Label: PROVED.
* **(H)-new.** Theorem 4.1, the transfer criterion. Label: PROVED modulo the
  citation.
* **(D)-new.** Prop 6.1: the prime-local ceiling is exponent 2. Label:
  PROVED.
* **(E)-new.** H_MIN(θ) is the exact sufficient input above exponent 2
  (Theorem 6.2). Label: PROVED implication; the hypothesis is open.
* **(F).** `H_MOD(A)` is refuted for `A<2`. This updates notes Cor. 54.2.

## Possible next steps (awaiting parent decision)

* **(a) Haar polylog bound.** `δ*(T) ≥ exp(−(log T)^{O(1)})` via the local
  lemma with a polylogarithmic class-of-one quarantine. This is step (i) of
  the brief and the open input of POINTWISE_SIZE §7.3(i). It needs a
  per-prime version of Lemma 2.3, namely
  `w_ℓ := Σ_{atoms ∋ ℓ} P(atom) ≤ (log T)^C/ℓ` uniformly in ℓ. That looks
  feasible but technical. It would be a Haar-level result only, so it would
  make the RA-heuristic input rigorous but would not prove anything about
  primes.
* **(b) Attack on H_MIN(θ), θ<1/2.** This needs a hub-adapted hypergraph
  minorant. It is a genuine research problem.
* **(c) Type-I frame (`ck_min`, Thm 11.2′).** An analogous prime-local
  analysis might give `(log p)^{2−o(1)}` there as well. Not attempted.

Replay: see `POINTWISE_OMEGA.md` § Replay. All scripts run in under 30
minutes at a 12 GB limit.
