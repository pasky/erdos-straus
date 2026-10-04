# AGENT REPORT O12 — Λ² cap for moduli with r large primes (branch side-agent/twin-ternary)

Deliverable: `EXCEPTIONAL_TWIN4.md` (§0 status table), `scripts/twin4_rough_bt.py`.

## Results
1. **Goal (1)** is already TW3 Lemmas 6.1 + 6.2 (any arity, reviewed SOUND).
   They need no codegree hypothesis: the codegree terms are part of the
   bound as capped squares. POINTWISE_OMEGA2 Lemma 10.2 is not needed (§1).
2. **Goal (2): the ternary residual `ℓ_b < w₂q` is closed, with no BFI input (PROVED).**
   Key point: in the residual, `ℓ_a = R/ℓ_b > R/(w₂q)`, so the partner
   `R = ℓ_aℓ_b` is itself rough. The question is only an *upper bound* for
   rough integers in one class mod q of length `R/q ≫ 1`. More generally,
   Lemma 2.3 (rough-partner Brun–Titchmarsh, via the arithmetic large
   sieve) splits R into its Z-smooth part d and its Z-rough part n, and
   sieves n mod q. This gives
   `Σ 1/R ≤ 3(s+1)ΣH^i/(φ(q)log(x/q))` for any partner with `Ω(R) ≤ s` and
   all primes `> w`. It replaces BT over the prime partner in TW3 Lemma
   3.1, and needs only `R/q ≥ 2^{s+1}`, which holds for every large partner
   (`R > (kQ)^{C₀}`, L large; Lemma 6.1; review F4b).
3. **Goal (3): Theorem 7.1 (PROVED, internal; not yet reviewed).** For
   fixed r and B, ℛ(M)-families with `M ≤ P(M)^{1+B}` and at most r primes
   above `(log X)^8` have Λ² saving `≪ L^{3/4}(log L)^{3r+O(1)}`. Inputs:
   * Prop 3.1: the TW3 Prop 6.3 chain, with r-ary inflation handled through
     the per-vertex condition `w_ℓ ≤ δ_r`.
   * Lemma 4.1: fibre law `G_L^{(r)}` (`w₂ = L^8` suffices for fixed r).
     This closes TW3 review E11.
   * Cor 5.2: whole events, and prime powers.
   * Lemma 5.3: small partners at every star, by Shiu along the top prime.
   * Lemmas 6.1–6.4: large partners at every star, with box counting mod a
     squarefree Q.
4. **Open (§7.1, Assessment):** uniformity in r. The proof costs
   `(log L)^{O(r)}e^{O(r)}`, so it should extend to
   `r ≤ ε log L/log log L` (constants not tracked). The range up to
   `L/(8 log L)` is not covered, and the B-hypothesis is still assumed.
   No BFI-type obstruction appears anywhere.

## Evidence
* Lemma 2.3 checked exactly in 1228 cases (`s ≤ 3`, `q ≤ 10007`,
  `x ≤ 10⁶`). Worst ratio to the bound: 0.13.
* Toy ternary system (X = 10⁹, j = 1009, 10007). The former residual
  carries 80–86% of the mass, so it really had to be proved. Its second
  moment is within a factor 1.5 of random.

## Points for the hostile reviewer
* Prop 3.1 constants (`δ_r = (21/32)^r/(16r)`; `(4/3)^{|S(E)|}` inflation
  after the vertex quarantine).
* Lemma 6.4: sf classes depend only on `a mod Q`, and the lift mass is
  `≤ (8/7)^h/Q`.
* Lemma 5.3(b): Shiu block hypotheses (`q = kQ_VR′ ≤ P^B`).
* Lemma 6.1 claim `R ≥ 2^r q` (uses `C₀ ≥ 6` and `kQ > w₂`).
* Suggested ledger text after review, (D)14 update: "Moduli with ≤ r large
  primes, r fixed: cap `≪ L^{3/4}(log L)^{O(r)}` PROVED (EXCEPTIONAL_TWIN4
  Thm 7.1). The ternary residual closes by a large-sieve upper bound for
  rough partners. Open: r unbounded, and dropping B."
  DISCOVERIES/STATUS were not edited (left for the merge).

Replay: see `EXCEPTIONAL_TWIN4.md` Replay (~1 min total, ≤ 1.2 GB).

---

# Checkpoint 2 (parts 2a, 2b): EXCEPTIONAL_TWIN4 §§9–10

## Results
* **(b) The B-hypothesis is removed for fixed r: Thm 10.4 (PROVED, internal).**
  Classes split three ways:
  * (D): the w₂-smooth cofactor dominates, `k > M_L²`.
  * (H): some large prime appears to exponent ≥ 12.
  * (G): the rest. These satisfy `M ≤ P(M)^{33r}`, so Thm 7.1 applies with
    `B = 33r−1`.

  The (D) classes have *polylogarithmic unweighted* first moment
  (Lemma 10.1): Cauchy–Schwarz splits off the smooth weight, Rankin on
  the smooth k gives `e^{−u}`, and Shiu runs along k itself (the modulus
  `M_L` is short there). (H) is `L^{−3}` by Cauchy–Schwarz. The fibre
  law is redone without B (Lemma 10.3); small moduli are now unbounded.
  The TW gapped/QR machinery is not needed.
* **(a) Uniformity in r.**
  * Prop 9.1: explicit constants `(C_B log L)^{Cr}`, hence the cap
    `L^{3/4+O(ε)}` for `r ≤ ε log L/log log L`.
  * Lemma 9.2: a general **unweighted payment** lemma. Any subfamily
    with small total mass can be added at cost `3m₂`, via the LLL with
    `x_G = 2^{|S(G)|}P(G)`.
  * Cor 9.3: moduli with `ω_L ≥ 330 log L` cost `o(1)` (Rankin).
* **Sharp failure point (§9.3, OPEN).** The middle window
  `ε log L/log log L < r < 330 log L` is the bulk of the ρ-weighted mass
  (≈ `(1/4)log L` primes in `(L^8, e^{L^{1/4}}]`). Of the method's losses
  there:
  * the inflation factors `c^r` are removable (use a polynomial-decay G_L);
  * the missing `1/s!` in the harmonic sums is removable;
  * the genuine loss is Lemma 5.3's first moment over the `2^r` proper
    stars with short partners. The diagonal is harmless
    (`Π(ρ_ℓ+1/ℓ)`, TW Conj 6.8's main term). What is needed is an
    off-diagonal second moment at short-partner stars that is efficient
    per prime: a multi-prime analogue of TW2's (H_O^≠). It is an
    equidistribution question for divisors of `(kQR+1)²/16` mod Q,
    averaged over Q.

## Points for the hostile reviewer
* Lemma 9.2: the LLL hypothesis for the mixed family (`x_F = 2P(F)` on
  𝓔₁, `2^{|S|}P` on 𝓔₂), and the fact that TW2 Lemma 2.1 accepts
  `A⁺ = A₁⁺ ∩ {no 𝓔₂}`.
* Lemma 10.1: the Shiu hypotheses along k (modulus m, length `mK/4`,
  `K ≥ m²`), and Rankin at p = 3.
* Lemma 10.3: the small-class `μ_p` bound without B, and the (D)
  second moment.
* Theorem 10.4: that §§5–6 use B only for the (G) classes they sum over.

Not edited: DISCOVERIES/STATUS. Suggested addition to (D)14: "B-hypothesis
removed for fixed r (TWIN4 Thm 10.4); uniform for
`r ≤ ε log L/log log L` with `L^{3/4+O(ε)}`; ≥ 330 log L primes free;
window `r ≍ log L` open (needs a multi-prime H_O^≠)."

## Addendum: review nits and KARY coordination
* Review nits F1–F4 (exceptional-twin4-review) are applied in one commit.
  §0 now marks Thm 7.1 as reviewed SOUND.
* §11 (coordination note, SKETCH). If KARY Thm 4.5 survives review, it
  supersedes Thm 7.1 and Prop 9.1 under the B-hypothesis, and B becomes
  the main restriction for both routes. KARY uses B in its Lemma 4.2(2),(3).
  The Lemma 10.1 technique (Rankin on the smooth cofactor, Shiu along it
  modulo the short top-prime power) should transfer with `s^{O(1)}`
  losses. KARY's `d·log(EM/d)` cost turns those into `λ^{3/4}log λ`,
  which would rule out θ > 3/4 for *all* ℛ(M)-families with general
  majorants. Suggested next task, once KARY is reviewed: write this out
  (and check ETw Lemma 1.1, the base).
