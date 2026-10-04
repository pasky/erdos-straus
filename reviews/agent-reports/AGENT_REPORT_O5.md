# AGENT_REPORT_O5 — (H_O^≠) / the two-prime Λ² cap (checkpoint 1)

Branch: this worktree. Deliverable: `EXCEPTIONAL_TWIN3.md`, plus
`scripts/twin3_short_sums.py` and `scripts/twin3_system.py`.

## Claim (PROVED here, internal check only)

The whole of (H_O) holds: `E_P Σ_{j>w₂} ρ_j S_j ≪_B α^{−3}(log L)^{O(1)}`
(Theorem 4.1). (Correction after review E5: (H_O^≠), (H_O^=) and H_div, as
un-quarantined pair sums, are *bypassed*, not proved; they remain open as
stated.) So TW2 Cor 5.2 becomes unconditional: the two-prime Λ² cap is
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

---

# Checkpoint 2 — three or more large primes (EXCEPTIONAL_TWIN3 §6)

## Proved (internal)

* **Lemma 6.1 (noise stability, any arity).** For a hypergraph event system
  under (H_δ), i.e. `Σ_{ℓ∈S(E)} w_ℓ ≤ δ ≤ 1/16` for every event E:
  `log(Z₂/Z₁²) ≤ (1+25δ) Σ_{stars σ} π_σ ρ̃^σ D_σ²`, where
  `D_σ = Σ_{E⊇σ} π_{E∖σ}` is the codegree mass. The proof is TW2 Thm 1.4
  verbatim; the only change is that the coupling factor
  `Π_{agreeing m}(1+tρ̃_m/ν_m)` is expanded over sub-stars. For graphs this
  is exactly TW2 (1.2). It is TW Conj 6.8 in log form, with no codegree
  hypothesis.
* **Lemma 6.2 (codegree quarantine by promotion).** A star with
  `D_σ > 1` is replaced by the single event σ. This is monotone (A⁺ ⊆ A;
  no mass grows), so it is free, and it caps every star with `|σ| ≥ 2` at
  `min(D_σ,1)²`. So the POINTWISE_OMEGA2 codegree-hub obstruction does not
  block the Λ² route.
* **Exact check.** `scripts/twin3_kary_check.py`, 1200 random hypergraph
  systems, 276 inside (H_δ): the largest ratio is 0.949 for both lemmas.
  Promotions inside (H_δ) are rare in these toys.

## Reduction and residual

* **Prop 6.3.** For the full family (any number of large primes, fixed B)
  the Λ² saving is at most `L^{3/4}` plus the fibre cost, plus the star
  sums `E_P[Σρp + ΣρS + Σ_{|σ|≥2}π_σρ^σ min(D_σ,1)²]`.
* **Inputs 1–2 are routine or already covered:**
  * the good event (H_δ) needs `w₂ = L^{10}` in place of `L^8`;
  * the unary and whole-event terms are covered by Shiu along the top prime.
* **Open (3a).** For the small-partner first moment with *composite*
  partner R, Lemma 2.1(a) sums the top prime over all integers. That loses
  `1/α`, giving `≈ L/log L`. The fix needs a Shiu bound over the *prime*
  top variable.
* **Open (3b).** For large composite partners, Brun–Titchmarsh over the
  prime m is replaced by a rough-number sieve with weight `L/log L`. This
  needs Lemma 3.2's `j^{−1/3}` sharpened to `j^{−1/2+o(1)}`, which looks
  feasible.
* **Open (3c), the main point.** The sum over star supports V: a
  first-moment bound over all sub-stars costs `Π_{ℓ∈S(C)}(1+ρ_ℓ) ≤ 2^r`
  per class. The decay in |V| must come from second moments, not first
  moments.
* **No cheap reduction.** Projection to the two largest primes and
  unweighted payment for k-ary events both fail. The reasons are stated in
  §6.2.

Recommendation: next task = (3a)–(3c), starting with (3c) for `r = 3`
(ternary moduli with fixed B).

Stopping for parent review.

---

# Checkpoint 3 — ternary moduli, fixed B (EXCEPTIONAL_TWIN3 §6.3)

* **(3c) is trivial for r = 3.** There are at most 7 sub-stars per class.
  The `2^r` problem exists only for an unbounded number of large primes.
* **Prop 6.4 (proved, same inputs as §§2–3).** Each of the following is
  `≪ α^{−3}(log L)^{O(1)}`:
  1. pair stars, i.e. vertex modulus `Q = ℓ₁ℓ₂` with a *prime* partner;
     the §§2–3 template runs mod Q, with ≤ 4 square roots;
  2. vertex stars with a small partner `R = ℓ_aℓ_b ≤ (kj)^{C₀}`; (3a) is
     harmless when R has a bounded number of primes, since
     `Σ1/R ≪ (log L)²`;
  3. vertex stars with an unbalanced large partner `ℓ_b > (kjℓ_a)^{C₀}`,
     taking `kℓ_a` as the cofactor;
  4. the balanced-partner case whenever the largest of u, v, t is
     `≥ 8w₂(kjA)^{1/2}`.
* **Exact residual (OPEN).** It is the vertex stars at j with all three of
  the following:
  * balanced partners: `(kj)^{C₀} < ℓ_aℓ_b`, `ℓ_b ≤ (kjℓ_a)^{C₀}`;
  * a balanced divisor triple: every one of u, v, t is `< 8w₂(kjA)^{1/2}`;
  * the resulting modulus `q = 4·(two short divisors) ≈ A^{1/2±}`, which
    is comparable to or larger than both partner primes.

  What is needed is an upper bound of the expected order for products of
  two primes in progressions mod q, on average over the occurring q. This
  is the Bombieri–Friedlander–Iwaniec range. The cap does not help, since
  the τ-mass of this part is a positive proportion of `L³`.
* Not done in this checkpoint: numerics for the residual; (3a)/(3b) for
  unbounded r.

Stopping for parent review (context ≈ 75%).

---

# Review response (exceptional-twin3-review.md)

The verdicts are SOUND for Lemmas 2.1, 3.1, 3.2/Cor 3.3 and 3.4, and
SOUND-AFTER-REPAIRS for Thm 4.1/Cor 4.2 and for the exposition.
Repairs E1–E8 are applied in one commit:
* E1: empty Shiu blocks are dropped explicitly.
* E2: the constants are absorbed explicitly.
* E3: the block range is `(M₁, X/(kj)]`, with ℓ₀ computed at `M₁/2`.
* E4: `X ≥ j` is dropped; the bound reads `HH′ ≥ j`.
* E5: (H_O^≠), (H_O^=) and H_div are *bypassed, open as stated*. This is
  fixed in the Thm 4.1 title, the Remarks, the new §0 table and this
  report.
* E6: the factor reads "5–16".
* E7: Route 3 is marked as heuristic and unused.
* E8: the remark on what `m > (kj)^{C₀}` buys is reworded (`M₁ ≥ q w₂/8`),
  and the note `C₀ ≥ 5` suffices is added.

E9 (TW2 status lines, DISCOVERIES) is left to the parent at merge.
§6 (Lemmas 6.1–6.2, Props 6.3–6.4) has not yet been reviewed.
