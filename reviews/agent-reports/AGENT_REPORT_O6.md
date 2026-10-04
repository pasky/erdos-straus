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

# Checkpoint 2 — attack on HC(a,B) (§7 of POINTWISE_OMEGA4)

**Verdict: sharply reduced, not proved.** Thm 4.2 stays conditional.

* **Lemma 7.1 (PROVED).** For an event containing O (class c mod q),
  the atom conditions collapse to `a≡κb` and `s≡(4κb²)^{−1}` (mod q),
  with `κ=−c`. For each residue of b, both a and s are determined
  mod q. The three O3 hub families appear as the three coordinate
  planes, each with its own height `h_1,h_2,h_3`.
* **Prop 7.2.**
  * The full-period and two-variable boundary terms are
    `≪𝓛³/q + 𝓛²2^{ω(q)/2}(h_1^{−1/2}+h_2^{−1/2}) + 𝓛³h_3^{−1}`. This is
    the HC shape with `a=1/2`.
  * Open gap (iii): the smooth-part factor `m|a+b` costs a τ(a+b)
    average over lattice points. It looks routine, but I have not done
    it.
* **Prop 7.3 (the obstruction).** The core consists of triples with
  `s,a,b<q`.
  * For `q≤y^{2−ε}` it closes by counting. The off-ray part is
    sketched only.
  * For `q≫y²` (for example a pair with one prime near `T/y`), take a
    non-hub ray `(a,b)=t(u,v)` with `s_t` small. Its contribution is
    governed by `#{t≤(q/h)^{1/2} : w·t^{−2} mod q ≤ Y}` for `Y≥y`.
    Bounding this is a short-interval equidistribution problem for
    inverses of squares, beyond the Weil range.
  * Counting that ignores the residues cannot beat `O(2^{ω(q)})`.
* **Suggested next steps.**
  * (α) An averaged HC plus a Markov push for the rare bad sets.
  * (β) Rescale the construction so that large-q vertex sets cannot
    occur.

# Checkpoint 3 — route (β) (§7.4)

* **Lemma 7.4 (PROVED).** Every surviving atom must be an event, by
  (I). So vertex sets with `q≍T/y≫y²` occur in every construction of
  this family. "Restricting atoms" is impossible, and quarantining the
  large primes costs `θ(T/y²)`.
* **Assessment.** The only form left is a composition level with the
  large-prime coordinates as outer variables. That moves the
  short-interval inverse problem to the outer level, a `k→k/2`
  recursion. I do not expect it to remove the obstruction.
* **Unconditional rate unchanged:** Cor 3.1/3.2.
* **Not done (context exhausted):** the off-ray core estimate and gap
  (iii) (the τ(a+b) lattice average). Both matter only once the core
  obstruction is solved.

# Checkpoint 4 — route (α), inverse-square problem (§7.5)

* **Precise obstruction IS(q;t_0,Y).** For every `(w,q)=1`:
  `#{t≤t_0≤(q/h)^{1/2} : w·t̄² mod q ≤ Y} ≪ 𝓛^BYh^{−a}`, with `Y≥y`.
  * Completion plus Weil gives an error of `2^{ω}q^{1/2}`, above the
    target `Y≤q^{1/2}`. So the problem is beyond Weil.
  * The second moment over w gives a rarity factor `1/(ηh)+1/(ηY)`
    against Markov. A large sieve over q adds nothing essential.
* **(α) Assessment.** The rarity keeps the pushed mass `O(Ŝ)`, so
  truncations are not inflated. The remaining threshold cascade gives
  `log(1/η)≈k³`, hence plausibly `log W ≳ (log₂p)^{4/3}`, mod TZ+ET.
  * This needs three unproved inputs: full-codegree rarity (including
    gap (iii) and the off-ray core), uniformity in q, and induced-mass
    control.
  * Not proved. The proved rates remain Cor 3.1 (TZ+ET) and Cor 3.2
    (TZ only).
* I stopped at the context limit. The recommended next task for a
  fresh agent is to prove inputs (1)–(3) of §7.5, which would give
  `(log₂p)^{4/3}`.
