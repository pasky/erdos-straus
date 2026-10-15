# R229 — hostile review of O224 (FOUR_ADIC_INPUT.md, BRAINSTORM/z1_*.md)

Reviewer branch: side-agent/review-four-adic (merged side-agent/four-adic-input at 03bbfb1b).
From-scratch scripts: `scripts/review_r229_*.py` (no reuse of the author's z1_* code).

## Summary verdicts (filled in incrementally)

| claim | verdict |
|---|---|
| Lemma 1.1 (frieze parity, two distinct classes in W∖0) | SOUND (but KNOWN: Morier-Genoud / FRIEZE_ES Lemma 1.1 — attribution missing, D2) |
| Lemma 1.2 (= CONSTRUCTIVE_ES Lemma 1.1, applies to every word) | SOUND |
| Thm 1.3 (S₄ = {χ = −1}, Fano pigeonhole) | SOUND as mathematics; novelty framing SOUND-AFTER-REPAIRS (D1) |

## Claim 1: Lemma 1.1, Lemma 1.2, Theorem 1.3

**Re-derivation.** Q(x) = v x₁² + t x₂² + u x₃² − 2x₁x₂ − 2x₂x₃, so Q(x + 2y) ≡ Q(x) (mod 4) and Q ≡ v x₁ + t x₂ + u x₃
(mod 2); since (v, t, u) ≢ 0 (mod 2) (else n = tuv − u − v even), W = ker is a 2-plane, |W∖0| = 3. ✓
Cofactors of G: row 1 = (tu−1, u, 1) = (A, u, 1), row 3 = (1, v, tv−1) = (1, v, A*). So f = n·G⁻¹e₁ ∈ L,
Q(f) = n²(G⁻¹)₁₁ = n·A, likewise Q(f*) = nA*. ✓ Each has a coordinate 1, so primitive. ✓ (Careful: the pentagon order
(t, u, v) corresponds to the vectors (e₂, e₃, e₁), not (e₁, e₂, e₃); the text states this correctly: Q(e₁) = v, Q(e₂) = t, Q(e₃) = u.)
Lemma 1.1 case analysis redone: t even ⇒ A, A* odd, exactly one of u, v even (u + v ≡ n); t odd, u, v odd ⇒ A, A* even,
f ≡ e₂ + e₃, f* ≡ e₁ + e₂; t odd, u even ⇒ v odd (else n even), A odd, A* even, classes e₃, e₁ + e₂. All cases give
two distinct nonzero classes in W. ✓
Lemma 1.2: a unimodular ℤ₂-lattice of odd rank is automatically odd (even unimodular ℤ₂-lattices have even rank), so the
author's "odd because t, u, v not all even" is correct but not even needed. Odd unimodular ⇒ diagonalisable ⟨a, b, c⟩;
q on a nonzero class with odd-support S is Σ_{i∈S} a_i mod 4; |S| = 2 gives 0 iff a_i ≢ a_j (mod 4); so 0 or 2 classes. ✓
"isotropic ⟺ 2 classes" is a finite Hilbert-symbol check over unit square classes (redone below). The "exactly two"
in CONSTRUCTIVE_ES Lemma 1.1 tacitly means nonzero classes; the author states this correctly.
Thm 1.3: (⇐) both 2-subsets of the 3-set W∖0 meet. ✓ (⇒) a pentagon entry ≡ 0 (4) gives a primitive x with
Q(x) ≡ 0 (4) (n odd for f, f*). ✓ "At most two" ✓. The bridge isotropic ⟺ χ = −1 is CHI_FLIP Thm 1.1, which is
stated and proved for every positive word of odd n (composite n included; gcd(A, n) = 1 always since AA* = tn + 1). ✓
No circularity: CHI_FLIP Thm 1.1 uses only Hilbert reciprocity and local ε_ℓ computations, not MODEL_SPECIFIC 3.1(a).

**From-scratch check** (`scripts/review_r229_words.py 2000`; own Jacobi symbol, own 2-adic Hilbert symbol via
Gram–Schmidt diagonalisation, own enumeration of the 7 nonzero classes of L/2L): all **50 008** words of all odd
1 ≤ n ≤ 2000 (incl. the 5 words of n = 1). 0 violations of: exactly two even entries; the two even classes distinct and in
W (|W∖0| = 3); norms of (e₂, e₃, e₁, f, f*) = (t, u, v, nA, nA*); #{nonzero q = 0 classes} ∈ {0, 2} and = 2 ⟺ ℚ₂-isotropic
(Hilbert symbol); isotropic ⟺ (−A/n) = −1; ≤ 2 entries ≡ 0 (4); (4 | some entry) ⟺ χ = −1. Split of χ = −1 words by
number of 4-divisible pentagon classes: 24 522 one, 9 485 two. Restricting to 3 ≤ n < 1500 gives 35 179 words, matching
the author's count. Lemma 1.2 diagonal check over all 64 ⟨a, b, c⟩, a, b, c ∈ {1, 3, 5, 7}: 0 failures.

**Verdict:** mathematics SOUND (proof complete, every word covered, boundary words included).

### Defects (claim 1)
**D1 (MAJOR, novelty/framing).** FOUR_ADIC_INPUT §0 (I2) ("MODEL_SPECIFIC Thm 3.1(a) was proved by enumerating 320 cells"),
§1 Thm 1.3 Remark (a) ("No Dedekind sums and no cell enumeration are needed") and z1_fano_pigeonhole Assessment present
Thm 1.3 as the first enumeration-free proof. It is not: FRIEZE_ES Thm 1.2 ((J)42) already gives a computation-free proof
(three Jacobi computations through the even edge), and its R208 addition states exactly "8 | ee′ ⟺ some q_i ≡ 0 (4)", i.e.
χ = −1 ⟺ 4 | some even pentagon entry, which is the statement of Thm 1.3 (including that only the two even entries can
carry the 4). Thm 1.3 is therefore a **third** proof of a known statement (DK Thm 4.5 / MODEL_SPECIFIC 3.1(a) / FRIEZE_ES
1.2). What is new is the lattice-theoretic mechanism: the identification of the pentagon with the norms of five explicit
primitive vectors of L and the 2 + 2 > 3 pigeonhole on W∖0, which explains *why* the modulus is 4 and why the Hasse sign
appears. *Repair:* in (I2) and Remark (a), replace "was proved by enumerating 320 cells" / "no cell enumeration needed" by
"third proof, after the cell enumeration (MODEL_SPECIFIC/CHI_FLIP) and the even-edge Jacobi proof (FRIEZE_ES Thm 1.2, (J)42);
new is the lattice-theoretic pigeonhole"; label Thm 1.3 "PROVED; APPARENTLY NEW proof of a known statement".
**D2 (MINOR, attribution).** Lemma 1.1 ("exactly two entries of P(w) are even") is FRIEZE_ES Lemma 1.1 and, as a statement
about F₂-friezes, Morier-Genoud arXiv:1907.12790 §3.5 (reviews/novelty-audit-2026-10d.md row 1a: KNOWN). The memo cites
this; FOUR_ADIC_INPUT Lemma 1.1 does not. New in Lemma 1.1 is only the lattice half (the two even entries give two distinct
classes of W∖0). *Repair:* add "(parity part: FRIEZE_ES Lemma 1.1 = Morier-Genoud §3.5; new: the class statement)".
**D3 (MINOR).** Lemma 1.2 justification "odd because the three diagonal entries cannot all be even" is correct but
superfluous (odd rank ⇒ odd). No repair needed; optional remark.
