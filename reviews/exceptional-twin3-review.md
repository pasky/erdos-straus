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
