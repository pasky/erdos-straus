# AGENT REPORT O30 (branch side-agent/haar-primes-2): Haar → primes

Deliverable: `POINTWISE_OMEGA8.md`, scripts `scripts/omega8_brw_check.py`,
`scripts/omega8_levels.py`, data `data/omega8/`.

## Result (checkpoint 1; needs hostile review)

* **Thm 4.3 (PROVED mod Thorner–Zaman + Elsholtz–Tao Prop 1.4):**
  `W(p) ≥ exp(c(log p)^{1/14})` for infinitely many Mordell-hard p;
  `log L_h(T) ≪ (log T)^{14}`. This replaces O4 Cor 3.1
  (`log₂p·log₃p/log₄p`) and reaches O4 §4.4's "third target".
* **Thm 4.4 (PROVED mod Thorner–Zaman only):**
  `log W ≥ (1/(2log2)−o(1))·log₂p·log₃p` (was `log₂p·log₄p/log₅p`).

## How

1. **Diagnosis (goal 1, §2).** The Haar local lemma uses suppression:
   good configurations rarely contain partial clusters with large
   completion mass. Alternating expansions (PO Brun, O2 support
   truncation, O3/O4 levels) amplify on such clusters. That produces the
   codegree thresholds `(kL)^{−(i−1)}`, an unsolvable single-family Markov
   recursion, the levels, and the `(k−1)!`. Lemma 2.1 (locally minimal
   events) shows that the outer inclusion–exclusion needs no codegree
   input; all the trouble is in the neighbourhood factors.
2. **Construction (§3).** Bazzi's one-sided ℓ² sandwich in
   Razborov–Wigderson form:
   `B = 1 − Σ_i A_i(1−Σ_{j<i}A_ju_j)²` satisfies `B ≤ F` pointwise for
   any `u_j`, with `F−B = Σ_iA_i(Σ_{j<i}A_j(F_{<j}−u_j))²` (Lemma 3.1,
   brute-force checked). Take `u_j` = Efron–Stein truncation of
   `F_{<j}|_{E_j}`. Then the error is an Efron–Stein tail, and ℓ¹ mass
   and moduli are `e^{O(t𝓛)}` (Lemma 3.2). The twist follows as in O2
   (Lemma 3.3). Thm 3.4 feeds this into PO Thm 4.1.
3. **The tail (§4).** Encode each residue coordinate in
   `b≈2log₂T` bits (`π(u)=g_{⌊q·int(u)/2^b⌋}`; fibres are intervals, so
   unions of `≤2b` subcubes). The bad-indicator becomes a DNF of width
   `≤kb`. Håstad's switching lemma with the LMN argument then gives a
   Fourier tail `≤2·2^{−k_0}` beyond degree `2C_H·kb·k_0`, independent
   of the number of terms. Pulling back by conditional expectation keeps
   the junta size; the Haar/encoding density ratio is `≤e^{1/2}`
   (Lemma 4.1). So `t ≍ k𝓛(S+𝓛)`, polynomial, with no hypothesis.

## Things a reviewer should attack

* Lemma 4.1(b): constants of the switching lemma and LMN step (median
  argument), and whether the DNF width really is `≤kb` after the interval
  encoding (vertex sets that are unions of classes mod `ℓ^{e}` give many
  subcubes but the same width).
* Lemma 4.1(c): the measure change (`π_*` vs Haar) and Jensen.
* Lemma 3.2: the ℓ¹ bookkeeping of products of cells on overlapping
  coordinates (the `T^{|I∩J|}` inflation).
* Thm 3.4: is PO Thm 4.1 applicable verbatim (finite combination of unit
  cells, `gcd(d_i,Q)=1`, the auxiliary prime `ℓ_0` as in O4 Thm 2.1)?
  Is O2 Lemma 4.3 (I) valid for the iterated-quarantine Π (O2 Thm 11.3
  asserts it)?
* The twist (Lemma 3.3) for hypergraph events.

## Not done / scope

* The exponent 1/14 is not optimised. ES is not touched.
* §1 (budget lemma) and §2 are now mostly diagnostic. The old route's
  requirement `log K ≤ k^{O(1)}` is moot.
* No ledger or STATUS edits (parent's call). If the result survives
  review, these become obsolete as stated: DISCOVERIES (H)14 "proved rate
  remains Cor 3.1", STATUS's "for every fixed k, W ≥ (log p)^k", and O4
  §4.4.
