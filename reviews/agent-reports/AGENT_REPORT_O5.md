# AGENT_REPORT_O5 — (H_O^≠) / the two-prime Λ² cap (checkpoint 1)

Branch: this worktree. Deliverable: `EXCEPTIONAL_TWIN3.md`, plus
`scripts/twin3_short_sums.py` and `scripts/twin3_system.py`.

## Claim (PROVED here, internal check only)

The whole of (H_O) holds: `E_P Σ_{j>w₂} ρ_j S_j ≪_B α^{−3}(log L)^{O(1)}`
(Theorem 4.1). That covers (H_O^≠) and gives (H_O^=) again. So TW2
Cor 5.2 becomes unconditional: the two-prime Λ² cap is
`≪ L^{3/4}(log L)^{O(1)}`, twins included, in Setting 3.0 (B-hypothesis
`M ≤ P(M)^{1+B}`; Corollary 4.2).

## Proof skeleton (4 steps, each a short lemma)

1. **(2.1).** Split the classes at vertex prime j into *small* partners
   `m ≤ (kj)^{C₀}` (C₀ = 6) and *large* partners. The quarantine gives
   `min(x+z,1)² ≤ 2x + 2z²`, so small classes are paid for by their first
   moment.
2. **Lemma 2.1.** The small first moment is `≪ α^{−3}(log L)^{O(1)}`, by
   Shiu along the top prime (TW2 Lemma 3.3). It is `(log kj)^3`, not
   `L^3`, and `Σ_j ρ_j(log j)^3/j ≍ α^{−3}`. This includes every class
   whose top prime is the vertex prime.
3. **Lemma 3.1.** For large partners, write `A = uvt` (TW2 Lemma 5.3).
   The largest coordinate is `≥ A^{1/3}`. Brun–Titchmarsh
   (Montgomery–Vaughan) over the *prime partner m* in the class mod
   4·(product of the two short variables) costs `2 log L/φ(·)`. The residue
   mod j depends only on the short pair (`−u/v`, `−1/(4v²t)` or `−4u²t`).
4. **Lemma 3.2 / Cor 3.3 / Lemma 3.4.** Elementary dyadic box counting
   gives `Σ_ρ r₁² ≤ ζ(2)² + o(1)` and `Σ_c r² ≤ ζ(2)²ζ(3)² + o(1)` for
   `j > L^8`. Hence `Σ_a V(a)² ≪ (log L)^6`, uniformly in j and k. Activity
   inflation and the k-sums are handled as in TW2 Lemma 5.4(ii)–(iii).
   Large partners cost only `(log L)^{O(1)}`.

The same-label / cross-label split is never needed.

## Points the reviewer should attack

* **(2.1) bookkeeping.** "Small" is defined relative to the *vertex* prime
  j. At the top-prime vertex every class is small, and that is case (a) of
  Lemma 2.1.
* **Lemma 2.1(a).** TW2 Lemma 3.3 is applied with the variable j over all
  integers and `q = km ≤ j^B`.
* **Lemma 3.1.** The claim `M₁ ≥ q w₂/8` uses C₀ ≥ 6 and the tie-breaking.
  In the u- and v-largest cases the coprimality `(u,v) = 1` is dropped,
  which is legitimate for an upper bound.
* **Vertices mod `j^{e_j}`.** The prime-power split is taken over verbatim
  from TW2 Lemma 5.4 (D5).
* **Inherited inputs.** Uses of TW2 Lemma 3.2(1) (pair activity
  `≤ 4Γ(lcm)/lcm`) and Lemma 5.4(iii) (`Σ_k Γ(k)h(k)/k ≪ polylog`).

## Numerics (EVIDENCE)

* Lemma 3.2 at Y = 600: the diagonals equal the proved constants and the
  off-diagonals are below random.
* Real system, X = 1e9, toy `C₀ = 1`: the large-partner `Σ_a V²` is O(1)
  (3.66 and 0.18) against masses 48 and 20. Inequality (2.1) holds with a
  factor 5–13 to spare.
* Not tested: the BT constants, the fibre law P, and k > 1.

## Consequences / suggested ledger change

* (D)-entry: TW2 Cor 5.2 moves from CONDITIONAL to PROVED (internal); the
  status of H_div is "bypassed".
* This does **not** move the exponent: the `α^{−3} = L^{3/4}` comes from
  Lemma 2.1 and TW2 Lemma 4.1 (diagonal/unary).

Stopping for parent review.
