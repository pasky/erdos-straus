# Hostile review: EXCEPTIONAL_TWIN3.md (task O5), commit 2bbe184

Subject: Theorem 4.1 ((H_O) unconditional) and Corollary 4.2 (two-prime Λ²
cap `≪ L^{3/4}(log L)^{O(1)}` unconditional in Setting 3.0), via (2.1),
Lemma 2.1, Lemmas 3.1–3.4, Cor 3.3. Context checked against
EXCEPTIONAL_TWIN2.md (TW2: Setting 1.0, Lemma 2.2, Setting 3.0, Lemmas
3.2–3.3, (3.1), Thm 5.1, Lemmas 5.3–5.4) and reviews/exceptional-twin2-review.md.

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered
E1, E2, … (severity: major / minor / nit).

## Item 1. Is S_j the right quantity? (2.1) bookkeeping — SOUND

* TW2 Lemma 2.2 defines `S_ℓ = Σ_a ν_ℓ(a) min(deg(ℓ,a),1)²` with
  `deg(ℓ,a) = Σ ν_m(c)` over edges of Setting 1.0 at the vertex `(ℓ,a)`,
  `a ∈ Ω_ℓ ⊆ ℤ/ℓ^{e_ℓ}`; Theorem 5.1 uses this S_j with the active binary
  classes of fibre c as edges. Counting classes with multiplicity (several
  classes can give the same edge) and ignoring the removal of unary vertices
  only enlarges deg, so every bound in TW3 on a class-indexed deg is an
  upper bound for TW2's S_j. A `kjm`-class constrains `y_j` only mod j, so it
  produces an edge at every lift of its residue; `deg(j,a)` then depends on
  `a mod j` only, and `Σ_{lifts} ν_j ≤ (8/7)/j` on supp P. Partner weight:
  `Σ_{lifts b} ν_m(b) ≤ (8/7)/m`. Both are what TW3 uses (§2, Lemma 3.4).
* Prime-power split (TW2 D5): `min(x+y,1)² ≤ min(x,1)² + 3y` re-checked
  (cases `x+y ≤ 1`; `x ≥ 1`; `x < 1 < x+y`, where `1−x² ≤ 2(1−x) < 2y`).
* (2.1): `min(x+z,1) ≤ min(x,1)+z` for `x,z ≥ 0`; `(p+q)² ≤ 2p²+2q²`;
  `min(x,1)² ≤ min(x,1) ≤ x`. Then `Σ_a ν_j(a)x(a) = w_j^{sm}(c)` by
  definition of x. Correct, with no label restriction, as claimed.
  Each binary class is counted at both endpoints, with the small/large
  split taken relative to the vertex; this is consistent (Lemma 2.1 covers
  "small at j", Lemma 3.4 "large at j", for every j).
* Numerical check (own code, item 6): (2.1) and the D5 inequality tested on
  10⁶ random `(x,y,z)` triples incl. edge cases; no violation.

## Item 2. Lemma 2.1 (first moment of the small part) — SOUND (nits E1, E2)

Re-derived line by line.
* Setup: on supp P, `ν ≤ (8/7)U` at both ends, activity `≤ 4Γ(k)/k` (TW2
  Lemma 3.2(1), k w₂-smooth — this is where "at most two primes above w₂"
  is used: every binary modulus is `kjm` with k dividing `Q_F`), `≤ τ(A²)`
  classes per modulus. Correct.
* (a) j top: `M ≤ j^{1+B}` ⇒ `km ≤ j^B`; A is linear in j with slope km, so
  TW2 Lemma 3.3 applies with `q = km` and j as the running variable.
  Blocks `(y,2y]` with `km > (2y)^B` contain no family modulus and can be
  dropped, so the hypothesis `q ≤ (2y)^{B+2}` holds on every block used.
  `Σ_i y_i^{−α}(a + i log 2)² ≤ m^{−α}·2^{α}(a²/α + a/α² + 1/α³)` and the
  prime sums `Σ_{m>w₂} m^{−1−α}(log m)^i ≪ (i−1)!α^{−i}` (`i ≥ 1`),
  `≪ log L` (`i = 0`; indeed `= E₁(8α log L)+O(1) ≈ (1/4)log L`) give
  `≪ (k/φ(k))[α^{−3}log L + (log 2k)²α^{−1}log L + …]` — at most the
  stated `(k/φ(k))(log 2k)²α^{−3}log L`.
* (b) m top, `j < m ≤ (kj)^{C₀}`: `kj ≤ m^B` gives Lemma 3.3 with `q = kj`;
  `≤ C₀log₂(kj)+2` blocks, each `≪ (kj/φ(kj))(C₀+2)²(log 2kj)²`. Then
  `(log 2kj)³ ≤ 4((log 2k)³ + (log j)³)` and `Σ_j j^{−1−α}(log j)³ ≪ 2α^{−3}`.
  Correct; m-primality indeed unused.
* k-sum: `Σ_k Γ(k)(log 2k)³/φ(k) ≪ (log L)^{O(1)}` is TW2 (3.1) with i = 3.
  The total is `≪ α^{−3}(log L)^{O(1)}` — the whole α^{−3} budget, as the
  author says (Remark 2.2). This is the only place where α^{−3} appears.
* **E1 (nit).** (a) should say explicitly that blocks with `km > (2y)^B`
  are empty and dropped; as written ("holds because `km ≤ j^B ≤ (2y)^B`")
  the reader must supply that the hypothesis is only needed on non-empty
  blocks.
* **E2 (nit).** In (a), `a = log(2km²)` vs the first block `y₀ = m/2`:
  `log(2km·y₀) = log(km²)`, so `a` is an upper bound, fine; but the stated
  intermediate `(k/φ(k)) m^{−α}(…)` silently absorbs `(m/2)^{−α} ≤ 2m^{−α}`
  and `m/φ(m) ≤ 2`. Harmless constants.
