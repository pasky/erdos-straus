# R229 — hostile review of O224 (FOUR_ADIC_INPUT.md, BRAINSTORM/z1_*.md)

Reviewer branch: side-agent/review-four-adic (merged side-agent/four-adic-input at 03bbfb1b).
From-scratch scripts: `scripts/review_r229_*.py` (no reuse of the author's z1_* code).

## Summary verdicts (filled in incrementally)

| claim | verdict |
|---|---|
| Lemma 1.1 (frieze parity, two distinct classes in W∖0) | SOUND (but KNOWN: Morier-Genoud / FRIEZE_ES Lemma 1.1 — attribution missing, D2) |
| Lemma 1.2 (= CONSTRUCTIVE_ES Lemma 1.1, applies to every word) | SOUND |
| Thm 1.3 (S₄ = {χ = −1}, Fano pigeonhole) | SOUND as mathematics; novelty framing SOUND-AFTER-REPAIRS (D1) |
| Prop 1.4 (2^k bit law, cell level, all k) | SOUND (label inconsistency D4; n-class uniformity provable, D5) |
| marking Lemma 1, Prop 2 (S_M not isometry-invariant for φ(M) > 2) | SOUND |
| marking Prop 3 (M = 2, 3, 4 PROVED; M = 6 norm-one PROVED, general EVIDENCE) | SOUND (D7: S₆ genus split can be PROVED by one example) |
| small-prime pigeonhole "classification M ∈ {2, 3, 4}" | SOUND-AFTER-REPAIRS (D8: "forced" undefined; precise PROVED form supplied) |
| Prop 3.1 / z1_glue (marked extension criterion c ≡ ±1, D ∣ p + v) | SOUND |
| z1_isogeny_pointer (a) no crossing | SOUND (D9: spine word has χ = +1 only for p ≡ 1 mod 4) |
| Legendre Prop 1, Cor 2, 7 failures ≤ 10⁶, squares | SOUND (all numbers reproduced exactly) |

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

## Claim 2: Proposition 1.4 (2^k bit law)

**Re-derivation.** In each parity pattern of Lemma 1.1 the map to coordinates containing the two even entries is a
bijection of (ℤ/2^K)³ restricted to the pattern: (t, u, v) ↦ (t, tu − 1, tv − 1) for t, u, v odd (t invertible);
(t, u, v) ↦ (t, u, tv − 1) for t odd, u even (v ↦ tv − 1 bijective on odd v onto even residues); identity for t even.
So the two even entries are independent and uniform on 2ℤ/2^K. P(4 | x) = 1/2, P(2^k | x) = 2^{−(k−1)} = s (k ≤ K).
P(χ = −1) = 3/4 (Thm 1.3), one/two isotropic = (1/2)/(3/4), (1/4)/(3/4) = 2/3, 1/3. ✓
f_k = (1 − (1 − s)²)/(3/4) = (4/3)(2s − s²); and (2/3)·2s + (1/3)(1 − (1 − 2s)²) = (8s − 4s²)/3, same. ✓
f₃ = 7/12, f₄ = 5/16, f₅ = 31/192, f₆ = 21/256. ✓ These are MODEL_SPECIFIC Thm 3.1(b)'s 140/240 and 600/1920 (checked
in MODEL_SPECIFIC.md l. 108–109). ✓ (The proof needs K ≥ k, as stated.)

**From-scratch check** (`scripts/review_r229_cells.py 6`, all 64³ cells mod 64): 163 840 odd-n cells (5/8), 122 880
χ = −1 cells (3/4; here χ = −1 is taken as "some entry ≡ 0 (4)", justified by claim 1), one-iso 2/3, two-iso 1/3, never
three; S_{2^k} share for k = 2..6: 1, 7/12, 5/16, 31/192, 21/256 = f_k exactly; one-iso conditional 1/2, 1/4, 1/8, 1/16;
two-iso 3/4, 7/16, 15/64, 31/256. In each class n mod 16 the shares are identical (15 360 χ = −1 cells per class).

**Verdict:** SOUND.

### Defects (claim 2)
**D4 (MINOR, label).** §1.2 labels Prop 1.4 "PROVED at cell level for every k ≥ 2", but §4 Outcome says "Prop 1.4
(CERTIFIED)". *Repair:* §4: "Prop 1.4 (PROVED at cell level; CERTIFIED to k = 5 by the author, k = 6 by R229)".
**D5 (MINOR, strengthening available).** "The same fractions hold in each class n mod 16" is presented as a script
observation, but it is PROVED for every class n mod 2^K by the same coordinates: for t, u, v odd, n ≡ t⁻¹(AA* − 1) and
AA* − 1 is an odd unit, so for fixed (A, A*) the map t ↦ n is a bijection of units; for t odd, u even, n ≡ uA* − (A* + 1)t⁻¹
with A* + 1 a unit, same conclusion for fixed (u, A*); for t even, n ≡ (tu − 1)v − u is a bijection v ↦ n on odd residues
for fixed (t, u). So the even pair is independent of n mod 2^K in every pattern. *Repair:* add this sentence and relabel the
n-class statement PROVED.
**D6 (MINOR, heuristic wording).** §1.2 "lifts x + 2y change Q(x) mod 8 by 4(B(x, y) + Q(y)), affine-linear in ȳ … one fair
bit": this is linear in ȳ (Q(y) mod 2 is linear), and it is a fair bit only if the functional ȳ ↦ B(x, y) + Q(y) mod 2 is
non-zero; the actual proof of Prop 1.4 does not use this picture (it varies the *word*, not the vector). *Repair:* add the one-line reason it is fair: L₂ is unimodular, so Q(y) ≡ B(c, y) (mod 2) for a characteristic
vector c, and B(x, y) + Q(y) ≡ B(x + c, y) (mod 2) is the zero functional only if x̄ = c̄; but q(c̄) is odd (c̄ = (1,1,1) in a
diagonal basis, q = a₁ + a₂ + a₃) while q(x̄) = 0, so the functional is non-zero and the bit is fair. Also "affine-linear" →
"linear".

## Claim 3: z1_marking_isometry (Lemma 1, Props 2, 3) and z1_small_prime_pigeonhole

**Re-derivation.** Lemma 1: n = (a+1)(b+1) − (a+1) − (b+1) = ab − 1 = (a+1)b − 1 − b. For w₁ = (1, a+1, b+1),
Gram [[b+1, −1, 0], [−1, 1, −1], [0, −1, a+1]]: e₂ has norm 1, e₁ + e₂ and e₃ + e₂ are orthogonal to e₂ with norms b, a and
inner product −1; (e₁ + e₂, e₂, e₃ + e₂) is a unimodular basis change. w₂, w₃ likewise. ✓ Prop 2: a ≡ x − 1, b ≡ x⁻¹,
n ≡ −x⁻¹ (unit); entries of P(w₁) = {1, a+1, b+1, a, b} ≡ {1, x, x⁻¹ + 1, x − 1, x⁻¹}, none ≡ 0 iff x ≢ ±1; P(w₂) ∋
(a+1)b − 1 ≡ 0. Parity: M odd → choose a even by CRT; M even → x odd, a ≡ x − 1 even. ✓ Prop 3(a) M = 3: tu ≡ tv ≡ 2
forces u ≡ v and n ≡ 2v − 2v ≡ 0. ✓ The quoted examples (M = 5, n = 3: (1,2,5) ∈ S₅ ∌ (2,1,4); M = 8, n = 5:
(1,3,4) ∉ S₈ ∋ (3,1,3)) verified by hand.

**From-scratch check** (`scripts/review_r229_marking.py 120`, own canonical form for positive ternary lattices = lex-min
Gram over bases drawn from vectors of norm ≤ max diag, which contains a successive-minima basis; own Fincke–Pohst):
Lemma 1 on all 411 factorisations n + 1 = ab, odd n < 120: 0 failures. Prop 2 construction for every M ≤ 60 with
φ(M) > 2: 0 failures. All 356 path classes of odd n < 120: S_M mixes an isometry class (n coprime to M) for exactly
M ∈ {5, 7, 8, …, 30} ∖ {6}, never for M ∈ {2, 3, 4, 6}; interior words isometric only up to reversal (0 exceptions).
`scripts/review_r229_s6.py`: the 21 residue pairs (a, b) mod 6 with gcd(ab − 1, 6) = 1 give agreeing S₆-memberships on
w₁, w₂, w₃ (lifts to 10 × 10 representatives each, 0 disagreements); the author's "36 residue pairs" means "the pairs
among the 36 with n coprime to 6" (wording only).

**Verdict:** Lemma 1, Prop 2 SOUND; Prop 3 SOUND (labels honest; the "⟺ M ∈ {2, 3, 4, 6}" is correctly marked conditional
on EVIDENCE 4 — only its M = 6 part actually needs it, the M = 2, 3, 4 directions are unconditional).

### Defects (claim 3)
**D7 (MINOR, label can be upgraded).** Prop 3(c) "S₆ is not a genus invariant" is supported by pooled counts over all
p < 3000, which do not by themselves exhibit one n with both behaviours in one genus. A single example makes it PROVED:
p = 17, χ = −1 words (1, 4, 7) (P = (1, 4, 7, 3, 6) ∈ S₆) and (2, 3, 4) (P = (2, 3, 4, 5, 7) ∉ S₆); χ = +1 words (1, 2, 19)
∈ S₆, (1, 3, 10) ∉ S₆ (Jacobi signs recomputed). At a prime the genus of a path lattice is fixed by χ. *Repair:* cite this example.
**D8 (MAJOR-label, small-prime pigeonhole).** The memo's Assessment "PROVED classification of forced pentagon slices" and
§2(d)'s "the pigeonhole forcing exists only for M ∈ {2, 3, 4}" do not define "forced". As written the ℓ ≥ 5 part is one
example ((1, 3, 3) ∈ X₃), and the ℓ = 3 "conic language" is not a counting pigeonhole (5 points, a 4-point conic, 13
points in ℙ²(𝔽₃): no forced meeting by counting; the real proof is the residue argument of Prop 3(a)). *Repair:* state the
PROVED theorem that the files actually contain: "For M ≥ 2, S_M ∩ X_n is a union of genera of path lattices for every n
coprime to M iff M ∈ {2, 3, 4} (S₂ = S₃ = X_n, S₄ = χ-fibre). ⇐: Prop 3(a), Thm 1.3. ⇒: φ(M) > 2 by Prop 2 (not even
isometry-invariant); M = 6 by the p = 17 example of D7." Drop or relabel the conic remark as heuristic.

## Claim 4: gluing (Prop 3.1), no crossing, Legendre levels

**Gluing, re-derived.** gcd(D, p) = 1 (for path words AA* = tp + 1), so L is unimodular at ℓ | D, the projection of L to
M ⊗ ℚ is M^#, index [L : M ⊕ ℤz] = D, hence D·|z|² = D²p, |z|² = pD. ✓ With B(e₂^#, e₁) = 0, B(e₂^#, e₂) = 1 and
Q(e₂^#) = (G_M⁻¹)₂₂ = v/D: y = −c e₂^# + z/D has B(y, e₁) = 0, B(y, e₂) = −c, Q(y) = (c²v + p)/D. ✓ Any third basis vector is
e₃ = ±y + αe₁ + βe₂; e₁·e₃ = 0 forces β = αv; then e₂·e₃ = ∓c + αD, which equals −1 iff ±c ≡ 1 (mod D). ✓ So the marked
criterion is right, and c = ±1 is admissible iff D | v + p, giving u = (v + p)/D. ✓ The self-review counterexample
(p = 11, v = t = 4, D = 15, c = 4: Gram [[4,−1,0],[−1,4,−4],[0,−4,5]], det 11; basis (e₂, e₁, e₂ + e₃) gives
[[4,−1,0],[−1,4,−1],[0,−1,1]], the path Gram of (4, 1, 4) ∈ X₁₁) verified by hand, as is the 2-power root example (A* = 8,
v = 1, p = 7: c ∈ {1, 3, 5, 7}). Cosmetic: condition (1) "v | D + 1" is vacuous (D + 1 = tv); what (1) really asks is a basis of
M with off-diagonal −1. The 17.5 % accidental-isometry statistic was not recomputed (EVIDENCE, not load-bearing).
**No crossing, re-derived.** Kneser neighbours, Hecke images, duals live in the same quadratic space L ⊗ ℚ; rescaling
preserves isotropy; χ = −(2-adic isotropy sign) for path lattices. ✓ Trivial but correct.
**Legendre levels, re-derived.** Prop 1: |x × y|² = |x|²|y|² − (x·y)² = AA* − 1 = tn, so χ = +1 forces tn ∈ □+□+□ (TWO_FIBRES
Thm A). The memo's direct check (a = 0: tn + 1 ≡ 1 − n² ≡ 0 (mod 8), so 4 | A or 4 | A*; a ≥ 1: 4 | t) gives an
independent proof through Thm 1.3, so Prop 1 does not even need Thm A. ✓ Level residues t′ ≡ 7 (p ≡ 1 mod 8), 3 (p ≡ 5)
✓; t = 2·odd·4^a is never a level ✓. Cor 2: a divisor pair A·A* = tm² + 1 with A ≡ A* ≡ −1 (mod t) is exactly a word
(u = (A+1)/t, v = (A*+1)/t, tuv − u − v = (AA* − 1)/t), and words at squares have χ = (−A/m)² = +1. ✓
**From-scratch recomputation** (`scripts/review_r229_legendre.c`, own sieve and divisor search, all levels t ≤ p + 2):
39 175 primes p ≡ 1 (mod 4) below 10⁶; no Legendre-level word exactly at **73, 1201, 1489, 9649, 21169, 23041, 44641**;
maximal least level 7119 at p = 704 761; primes without a Legendre-level word having 8 | some entry (levels ≤ 1000): 202.
All identical to the memo. Odd squares 9 ≤ m² ≤ 10⁸, levels ≤ 3000: 0 words; odd squares ≤ 4·10⁶, **all** levels: 0 words.

### Defects (claim 4)
**D9 (MINOR).** z1_isogeny_pointer (a): "The spine word (p + 2, 1, 1) has L ≅ ⟨1, 1, p⟩ ∈ 𝔊⁺_p" holds only for p ≡ 1
(mod 4): A = p + 1, χ = (−(p+1)/p) = (−1/p), which is −1 for p ≡ 3 (mod 4) (⟨1, 1, 3⟩ is ℚ₂-isotropic). *Repair:* add
"(p ≡ 1 mod 4, the only case of interest)".
**D10 (MINOR, cosmetic).** Prop 3.1(1) "v | D + 1" is automatic; replace by "a basis with off-diagonal entry −1".
