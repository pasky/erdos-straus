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
   3.1, and needs only `R/q ≥ 2^{s+1}`, which always holds (Lemma 6.1).
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
