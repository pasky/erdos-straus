# AGENT_REPORT_O2 — checkpoint 1 (branch `side-agent/omega-hub`)

## Headline

**H_MIN(θ) holds for every θ>1/3**, hence (with PO Theorem 4.1, i.e. modulo
Thorner–Zaman, as for PO Thm 5.1):

```
W(p) ≥ (log p)^3 · exp(−C log log p / log log log p)   for infinitely many Mordell-hard p,
log L_h(T) ≤ T^{1/3+o(1)}.
```

This is POINTWISE_OMEGA2.md Theorem 5.1. Label: **PROVED modulo
Thorner–Zaman** (same citation as PO Thm 5.1; effective). It is not yet
reviewed by the parent. It improves exponent 2 to 3, refutes `H_MOD(A)` for
all `A<3`, and brings the prime side level with the best proved Haar bound
(PO Thm 9.3, `T^{1/3+o(1)}`).

## How the hub obstruction is bypassed

PO Prop 6.3 (still true) kills *event-count* truncation. The new minorant
(POINTWISE_OMEGA2 §§1–3) has three ingredients.

1. **Support truncation.** Lemma 1.1 gives
   `B_L = Σ_{F⊆A(n), |supp F|≤L}(−1)^{|F|}`, in exact closed form. Lemma 1.2
   gives the pointwise minorant `B_L − 4^{L+1}e_{L+1}(a) ≤ 1[no event]`,
   where `a_ℓ` counts the occurring events at ℓ. The error is exponential
   in the number of *primes*, not events, so a K_{r,r} hub costs `16^r`
   against `y^{−2r}`.
2. **Mass bound.** After grouping by support, the coefficients are at most
   `2^{|U|}`. So `M_1 ≤ E∏(1+2a_ℓ)` (Lemma 1.3).
3. **Pseudoforest moment bound.** Lemma 2.1:
   `log E∏(1+z a_ℓ) ≤ zS_1 + O_z(S_2)`, provided every vertex
   `(ℓ, c mod ℓ)` has degree `≤e^{−3z−2}`. Lemma 2.2 enforces this by
   forbidding the high-degree hub *vertices*. Markov bounds the cost:
   `≤2S_2/δ` in total, and `≤w_ℓ/δ` per prime.

Theorem 3.1 (pure CRT combinatorics) adds the LLL lower bound and the twist
condition, using the conditional LLL (Haeupler–Saha–Srinivasan). §4 applies
it to ES:
* class-of-one quarantine at `y=T^{1/3}e^{2𝓛/log 𝓛}`, plus `T^{o(1)}` bad
  primes;
* all surviving events have support ≤2;
* per-prime masses are `o(1)` by the crude count;
* the global mass is `T^{o(1)}`, by PO Lemma 9.2 extended to an arbitrary
  quarantine set (Lemma 4.1).

## Verification done

* `scripts/omega2_abstract_check.py`: brute force of Lemmas 1.1–1.2 on random
  systems, ≈1.37M cases, 0 failures.
* `scripts/omega2_es.py checkI`: implication (I) checked directly on
  CRT-built integers at `T=1000, 3000`. 300 forced survivors, all with
  `W(n)>T`.
* Finite-T illustration of Construction 4.2 at `10^4, 10^5`. It is not an
  instance of the theorem, since the constants (`δ=e^{−50}`) are
  astronomical.
* An independent deep self-review (the `review` tool, codex) re-derived
  every lemma and found **no fatal defect**. Its five repairs are applied
  in commit "Self-review repairs":
  * `2|Q` added to Setting 3.0;
  * `+1` added in the budgets;
  * k-cutoff in Lemma 4.1;
  * θ<1/3 wording;
  * the script now really checks (I), and the vacuous Lemma 1.2 line at
    `10^5` is disclosed.

## Not done / open

* **θ<1/3.** It needs an H_PP-type per-prime bound and a hypergraph version
  of Lemma 2.1 (codegree issue, §7). Both are open; this is labelled
  Assessment.
* **H_PP with polylogarithmic z** (second part of the brief). Not attempted
  beyond the §7 remarks. I have a lead on the single-prime part: it reduces
  to bounding `|F_ℓ^{full}|` individually, and for `r'=1` the solutions
  correspond to pairs `(v,t)` with `v | ℓ+t`, `4t | ℓ+v`. This might give
  `|F^{full}_ℓ| ≤ ℓ^{1/2+o(1)}`, i.e. the single part of H_PP for
  `z≥(log T)^{2+ε}`. The multi-prime part is the real obstacle. Not
  written up.

## Suggested ledger updates (for the parent; I did not edit them)

* DISCOVERIES (H)8: append "exponent improved to 3 by POINTWISE_OMEGA2
  Thm 5.1 (H_MIN(θ) for θ>1/3)".
* (F)10: `H_MOD(A)` refuted for every `A<3`.
* (H)8 / PO §6.3: Prop 6.3 is an obstruction only to event-level
  Bonferroni.
* STATUS.md, line "Unconditionally, `W(p)≥(log p)^{2−o(1)}`…": change to
  exponent 3.
* paper/es-omega-note.tex would need a new section. It is untouched.

## Requested review focus

Lemma 2.1 (the expansion and the pseudoforest structure), Theorem 3.1
Step 4 (twist via conditional LLL), Lemma 4.3 (G)/(W) exponents, and the
application of PO Thm 4.1/6.2 in Thm 5.1.
