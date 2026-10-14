# y5_general_r_jacobi — the general-r frieze Jacobi law and r-uniqueness (O213, brief item (c), O210 spark 1)

## Idea
O210 spark 1 asked for two things for (r+2)-gon friezes with frozen boundary (1, …, 1, N):
* a closed form for (A/N) as a function of the mod-8 frieze;
* a proof that r = 3 is the only HJ length whose zero-mod-4 locus is a Jacobi fibre (CONJECTURE in FRIEZE §4).

Both follow cleanly.

Notation. Word a = (a₁, …, a_r), K_i = K(a₁, …, a_i) (the leading continuants, K₀ = 1), N = K_r. The path form
Q_a = Σ a_i x_i² − 2Σ x_i x_{i+1} has leading principal minors K_i.

**Theorem 1 (general-r Jacobi law; PROVED).** For every integer word with N > 0 odd and all K_i ≠ 0:

`(K_{r−1}/N) = ∏_{i=1}^{r−1} (K_i, −K_{i+1})₂ · ∏_{i=1}^{r−1} (K_i, −K_{i+1})_∞.`

The ∞-factor equals (−1)^{#{i : K_i < 0 < K_{i+1}}}. For positive words (letters ≥ 2) it is 1.

*Proof.*
1. Over ℚ, Q_a ≅ ⟨K₁/K₀, K₂/K₁, …, K_r/K_{r−1}⟩ (LDLᵀ with pivots = ratios of leading minors). The Hasse invariant
   s_v = ∏_{i<j}(d_i, d_j)_v of this diagonal form equals ∏_{i=1}^{r−1}(K_i, −K_{i+1})_v. This is the classical
   leading-minor formula, checked for r = 2 by (K₁, K₁K₂) = (K₁, −K₂) and by induction.
2. At an odd ℓ ∤ N the lattice is unimodular, so s_ℓ = 1, even if ℓ divides some intermediate K_i: the invariant
   depends only on the ℚ_ℓ-class.
3. At ℓ | N, split L = M ⊥ ⟨N/K_{r−1}⟩ over ℤ_ℓ, with M the span of the first r − 1 basis vectors (det K_{r−1}, a
   unit at ℓ because consecutive continuants are coprime). Then s_ℓ = (K_{r−1}, N/K_{r−1})_ℓ = (K_{r−1}/ℓ)^{v_ℓ(N)}.
4. The product formula gives ∏_{ℓ|N}(K_{r−1}/ℓ)^{v_ℓ(N)} = s₂ s_∞, which is the claim. ∎

Since K_{r−1}·K(a₂..a_r) ≡ 1 (mod N), the other end quiddity has the same symbol.

* **r = 3** is FRIEZE Thm 1.2 and CHI_FLIP Thm 1.1 (rank-3 case).
* **The closed form spark 1 asked for** is a product of 2-adic Hilbert symbols of *consecutive leading continuants*:
  one local factor per step of the SL₂ walk. It is not a product over backtrack runs. The shape resembles a 2-adic
  Kubota-cocycle product along the walk, as in the theta-multiplier dictionary of (J)15. That identification is NOT
  verified here (Assessment only). The product depends only on Q_a ⊗ ℤ₂, hence on the word mod 8.
* **Item (d), positivity = archimedean factor, made explicit.** For signed words the defect is
  (−1)^{#(sign changes − → + in K₁, …, K_r)}, a Maslov-type count of the continuant sign sequence. Positivity of the
  frieze (all K_i > 0) is exactly "the ∞-factor is 1". This is O210 §3, now with an explicit formula valid for all r.

**Theorem 2 (r-uniqueness; PROVED, closes FRIEZE §4 CONJECTURE).** For every r ≥ 4 there are words of HJ length r
(letters ≥ 2) with N an odd square and some quiddity ≡ 0 (mod 4). So the zero-mod-4 locus Z_r meets the squares, where
every Jacobi symbol (A/N) with gcd(A, N) = 1 is +1. Hence Z_r is not contained in a Jacobi fibre {(A/N) = −1}.

*Proof.*
* r = 4: FRIEZE (2, 2, 2, k).
* r ≥ 5: take the word (2, 2, 2, 4, 2^{r−5}, k), whose letter 4 is a quiddity. Write A = K(2,2,2,4,2^{r−5}) and
  B = K(2,2,2,4,2^{r−6}). Then K(2^i, x, 2^j) = x·IJ − (I−1)J − I(J−1), with I = i + 1, J = j + 1. Here i = 3, x = 4,
  so I = 4 and A − B = 2I + 1 = 9.
* Hence N = kA − B ≡ 9 (mod A). Take N = (3 + 2A)², which is odd and ≡ 9 (mod A), with k = (N + B)/A ≥ 2. ∎

CERTIFIED for r = 5, …, 200 by `y5_general_r.py`.

Reading. Combined with Z₃ = {(h′/N) = −1} (FRIEZE Thm 1.2), this proves: **for N ≡ 1 (4), r = 3 is the unique HJ length r ≥ 2 (Z₂ = ∅
there) whose zero-mod-4 locus is a nonempty Jacobi fibre.** This was the ES analogue of
(J)32's "m = 4 unique", and is now PROVED. The mechanism is visible:
* for r ≥ 4 a 4 can be placed as a letter with ≥ 3 other letters, so that the prefix continuant difference A − B is a
  square (here 9);
* for r = 3 the only freedom is the three letters, and Thm 1 forces the symbol.

## Literature
* Leading-minor formula for the Hasse invariant: Cassels, *Rational Quadratic Forms* (1978), Ch. 4 (Hasse–Minkowski,
  Lemma on diagonalisation by principal minors); Lam, *Introduction to Quadratic Forms over Fields*, Ch. V.
* Kubota cocycle: Kubota, *On automorphic functions and the reciprocity law in a number field* (1969).
* Frieze/continuant dictionary: Conway–Coxeter; Morier-Genoud–Ovsienko arXiv:1811.01229.

## Barrier screen
These are structural theorems, not existence mechanisms. They sharpen the steering rule: the ES sign is the
2-adic Hasse invariant of the path form, and the only global input is the product formula with s_∞ = 1 (positivity).
T1 = "s₂ = 1 at squares" is the r = 3 instance of Thm 1. For r ≥ 4 no zero-mod-4 statement is a character fibre, so
"use longer HJ words" cannot import the clean sign mechanism (it produces 4/N as r unit fractions anyway).

## Cheap numerics
`scripts/y5_general_r.py 200000 200` (CERTIFIED):
* Thm 1 on 131 467 random positive words (r ≤ 12), 0 failures;
* the signed version on 65 589 signed words, 0 failures;
* the Thm 2 family for r = 5 … 200, 0 failures.

## Assessment
PROVED: Thm 1 (an elementary generalisation of CHI_FLIP Thm 1.1 to rank r with an explicit per-step formula) and
Thm 2 (closes the O210 polygon-size CONJECTURE). Neither gives existence. They are clean and close spark 1 and the
formula half of spark 5.
