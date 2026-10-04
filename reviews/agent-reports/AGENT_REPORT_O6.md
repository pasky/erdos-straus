# AGENT_REPORT_O6 — explicit rate beyond fixed powers (checkpoint 1)

Branch `side-agent/omega-rate`. Deliverables:

* `POINTWISE_OMEGA4.md`;
* `scripts/omega4_rates.py`;
* `data/omega4/{recursion,rates}.txt`.

STATUS/DISCOVERIES are not edited; that is left to the parent.

## Outcome

**The first target is reached.** Modulo Thorner–Zaman and Elsholtz–Tao
Prop 1.4, for infinitely many Mordell-hard p:

```
W(p) > (log p)^{κ(log₂p)},   κ(X) ~ log X/log log X,   i.e.   log W ≥ (1+o(1))log₂p·log₃p/log₄p.
```

Modulo Thorner–Zaman alone: `log W ≥ (1+o(1))log₂p·log₄p/log₅p`
(Cor 3.1–3.3).

**Targets 2 and 3 are not reached.** The failure point is isolated.

## What was done

1. **Thm 1.1.** O3 Thm 5.1 with explicit constants:
   `log K ≤ (k−1)!(log(3Ŝ+k+1)+8.06k+5log k+10.1)+102`.
   * The proof introduces a single potential
     `Ẑ_r = Σ_r+H_r+Σ_{t>r}Λ_t+Ŝ_{≥r}+Ŝ+k` and shows
     `log Ẑ_{r−1}+b_k ≤ (r−1)(log Ẑ_r+b_k)`.
   * Per-prime amplification is `≤ e^{k+A_k}` (telescoping
     `Σ(r−2)/(r−1)!=1`), which gives `c_k(Ŝ)=k^{−2}e^{−56−2A_k}`.
   * No step of O3 is changed; this is bookkeeping on the reviewed
     proof.
2. **Thm 2.1.** The explicit ES pipeline: `(C_{k,T})`, i.e.
   `A_k(S*+1)+log(C_2𝓛) ≤ 𝓛/(6k²)`, implies a hard p with `W(p)>T` and
   `log p≤T^{1/k}`.
   * **Check this:** I replaced O3's `y=T^{1/k}exp(2𝓛/log𝓛)` by
     `y=2T^{1/(k+1)}`. I argue the exp factor is unused once Lemma 11.2
     supplies the per-prime bounds: O2 Lemma 4.3 (I) needs only
     `Π⊇{ℓ≤y}`. The factor would be fatal for growing k.
3. **§4 bottleneck.**
   * The factorial is exactly the Markov push-down cascade. Markov is
     sharp at the first push (O2 Prop 11.4). The cascade is an artefact:
     the heavy sets are κ-monochromatic and end up as singles anyway.
   * Precise sufficient input: **HC(a,B)**, i.e. `Δ_O ≤ 𝓛^B H^{−a}`
     outside the hub set `𝓗_H`.
   * **Thm 4.2** (PROVED implication): HC implies
     `log W ≥ 0.2√a·(log₂p)^{3/2}` i.o., via hub quarantine (O3 §1),
     single-level O2 Thm 10.3 and `k≍𝓛^{1/3}`.
   * Assessment ceilings (§4.3):
     * `(log₂p)²/log₃p` would need HC **and** an event-sensitive
       truncation, because O2 Lemma 1.2's `4^{L}` counts primes and
       forces `L≥e^{ck}Ŝ`. This loss is not intrinsic: for disjoint
       events the true error is `≈2^{#events}`.
     * `exp((log p)^c)` needs `y≤𝓛^{O(1)}` (PROVED: `log p≥θ(y)`), hence
       `k≍𝓛/log𝓛`, where the Lemma 10.2 thresholds give `log K≳𝓛`. It is
       outside the method.
4. **Haar side (Prop 5.1).** `log(1/δ*) ≤ π(z)𝓛+8k_z²S*𝓛+4S*`, which is
   polynomial in k. Under ET it is the Haar form of
   `exp((log p)^{1/7})`.

## Checks

`omega4_rates.py recursion` runs the O3 parameter recursion exactly, in
the log domain, with worst-case Markov pushes, for `k=3..8` and
`Ŝ=10,10³,10⁶`.

* Thm 1.1's bounds hold, about 2× in the log to spare.
* The exact recursion is itself factorial (`log K/(k−1)!≈41` at k=8).

## Points for the reviewer

* Thm 1.1 Steps 1–2: the inequalities `L_r+1≤Ẑ_r/δ_r`,
  `4N_r≤8kẐ_r/δ_*`, and `Ẑ_{r−1}≤3k(β_kẐ_r)^{r−1}`.
* Thm 4.2 step 3: combining O3 Thm 1.1/Lemma 1.3 (P′) with O2 Thm 10.3,
  under the codegree factor `e^{0.011k}`.
* The removal of the exp factor in y (item 2).
* Cor 3.1 relies on ET Prop 1.4, a cited published theorem, as in PO
  Lemma 9.2 and O2 Lemma 11.1. Cor 3.2 does not.
