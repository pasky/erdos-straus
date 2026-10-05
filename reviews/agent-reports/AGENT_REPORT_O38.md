# AGENT REPORT O38 (branch side-agent/esw-suppression): ESW via a generating function

Deliverable: `POINTWISE_OMEGA10.md`, `scripts/omega10_*.py`.
Checkpoint 2 supersedes checkpoint 1: Conjecture Q is now proved.
Self-review R38a (deep subagent) found no FATAL or MAJOR issue in the
mathematics. Its minors are applied. Its one MAJOR concerned the
checkpoint-1 wording of this report, which is rewritten below.

## Results

1. **O9 §4 check (§1).** Lemma 4.1 and Cor 4.2 are correct.
   * Arithmetic slip: `kS*𝓛≍𝓛^6`, not `𝓛^6/log𝓛`.
   * Scope: the "1/6 ceiling" assumes every junta coordinate costs `≍𝓛`.
     A modulus-weighted argument has floor `≍S𝓛`.
2. **C-1 (Cor 3.5, PROVED).** For every single-value system on a finite
   product of uniform spaces (any alphabet sizes), and all weights `λ_v≥1`
   with `∏_{v∈supp E}λ_v≤2` for every event:
   `G_F(λ)=Σ_U∏_{v∈U}λ_v‖F^{=U}‖²≤1`. There is no mass, codegree,
   quarantine or width hypothesis. The proof has three steps.
   * **Lemma 3.1, cover bound:** `G_F ≤ E_x Q_μ(𝓗(x))`. Here
     `Q_μ(𝓗)=Σ_Vμ^V τ̂_𝓗(V)²`, and 𝓗(x) collects the supports of the events
     that hold at x. The local-lemma-type suppression is exact here.
   * **Lemma 3.2, polarization:** `Q_μ(𝓗)=E_P[Θ(𝓗_P)²]`. Here
     `Θ(𝒞)=Σ_{𝒥⊆𝒞}(−1)^{|𝒥|}λ^{∪𝒥}`, P is a random set with
     `P(v∈P)=μ_v/λ_v`, and `𝓗_P` are the edges avoiding P. The proof uses
     the two-point law `p_v∈{1,−μ_v}` for a mean-zero, variance-`μ_v`
     multilinear polynomial.
   * **Lemma 3.3, deletion–contraction:** `Θ(𝒞)=λ_vΘ(𝒞/v)−μ_vΘ(𝒞−v)`.
     The triangle inequality closes the induction exactly:
     `|Θ|≤∏_{E∈𝓜}(w_E−1)` for every matching 𝓜, in particular `|Θ|≤1`.
   * **Thm 3.4:** `Q≤∏_{E∈𝓜}(w_E−1)≤1` (conjectures Q, Q′ and QM).
3. **Cor 4.1 (PROVED, q-ary energy concentration).** If every event has
   support `≤k`, then `energy(f;t)≤2^{−(t+1)/k}` for every integer `t≥0`.
   This is ESW's energy form, independent of the alphabet size. It is the
   q-ary analogue of DNF Fourier concentration, so there is no bit
   encoding and no Håstad.
4. **Thm 4.2 (PROVED implication in O8 Thm 3.4 / O9 Thm 2.2).** The junta
   becomes `t≍k(S+k𝓛)`, so `log Z≪log Q_Π+𝓛^6`, where it was `≍𝓛^7`.
   Already now `log L_h(T)≪𝓛^7/log𝓛` (a log gain), and **the quarantine
   `log Q_Π≪𝓛^7/log𝓛` is the sole bottleneck.**
   * `log Q_Π≪𝓛^6` would give exponent 1/6.
   * **Remark 4.3** (modulus weighting): this further gives
     `log Z≪log Q_Π+𝓛^5log𝓛`, which leads to `(log p/loglog p)^{1/5}` if
     also `log Q_Π≪𝓛^5log𝓛`. It holds **only under an extra hypothesis**:
     free primes appear in event moduli to bounded total exponent
     (`∏_{ℓ∈supp E}ℓ^{a_ℓ}≤T^ρ` with ρ=O(1)). This is not checked for ES.
5. MONO (adding one event never raises G) is false (explicit
   counterexample). FM (the fractional-matching form) and C-exp (`w_E>2`)
   remain conjectures with evidence. Neither is needed.

## For the parent / the quarantine agent

* The junta side is done. The exponent is now set by `log Q_Π`:
  * `log Q_Π≪𝓛^6` gives 1/6;
  * `≪𝓛^5log𝓛` plus Remark 4.3's hypothesis gives ≈1/5.
* Attack points for the hostile review:
  * Lemma 3.1's restriction / top-component step;
  * the law of `p_v` in Lemma 3.2;
  * the base cases of Lemma 3.3: an empty edge, an empty family, the
    empty matching;
  * Thm 4.2's bookkeeping against O8 Thm 3.4 / O9 Thm 2.2;
  * whether ES event moduli satisfy Remark 4.3 with ρ=O(1).
