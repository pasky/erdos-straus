# FOUR_ADIC_INPUT — a 4-specific input from the 2-adic χ-fibre (task O224, wave Z-a)

Status: in progress (O224). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on MODEL_SPECIFIC.md ((J)32), CHI_FLIP.md ((J)33), CONSTRUCTIVE_ES.md ((J)35), FOUR_SPECIFIC.md ((J)46),
TWO_FIBRES.md ((J)48), TRANSPORT_LAW.md ((J)45), SEVEN_SIBLING.md ((J)49). Memos BRAINSTORM/z1_*.md, scripts
scripts/z1_*, data data/z1/.

Notation. A word w = (t, u, v) ∈ ℤ³_{≥1} with tuv − u − v = n (n odd); A = tu − 1, A* = tv − 1, AA* = tn + 1; path lattice
L = L_w with Gram G = [[v, −1, 0], [−1, t, −1], [0, −1, u]] (det n), basis e₁, e₂, e₃; Q(x) = xᵀGx; χ(w) = (−A/n) = −ε₂(Q)
(CHI_FLIP Thm 1.1). The **pentagon** of w is P(w) = (t, u, v, A, A*); S_M = {w : M divides some entry of P(w)}.

## 0. Iteration log
(I1) The target property must satisfy (i) true for 4 at every prime, (ii) not a mechanism for 8/131, 8/241, 11/37, TES, ES_q
failures, (iii) false at odd squares. First observation (memo z1_marking_isometry): any argument that produces a path class
in the χ = −1 genus satisfies (ii) and (iii) automatically, because S_4 is a genus invariant while S_8 is not even an isometry
invariant (Prop 2 there). So everything rests on (i).
(I2) Before attacking (i), I asked *why* the five 4-slices are exactly a character fibre (MODEL_SPECIFIC Thm 3.1(a) was proved
by enumerating 320 cells). Found a 3-line conceptual proof: pigeonhole in the Fano plane ℙ(L/2L) (§1). It also explains
the 7/12, 5/16, … fractions for 8, 16, … exactly as "one fair 2-adic bit per further level" (§1.2).
(I3) The bit model, applied to actual words, *fails badly*: bits are strongly correlated inside one prime (§1.3). This is the
quantitative form of "4 needs no bit, 8 needs correlated bits".

## 1. Why 4: pigeonhole in the Fano plane

Let L₂ = L ⊗ ℤ₂. It is unimodular (det n odd) and odd. The map q: L/2L → ℤ/4, q(x̄) = Q(x) mod 4, is well defined
(Q(x + 2y) = Q(x) + 4B(x, y) + 4Q(y)). Since Q(x) ≡ Σ G_ii x_i (mod 2), the set W = {x̄ : q(x̄) even} is a 2-dimensional
subspace, so W ∖ 0 has exactly **3** elements (a line of the Fano plane ℙ(L/2L)).

The five pentagon entries are norms of five explicit primitive vectors of L. Put f = Ae₁ + ue₂ + e₃ and
f* = e₁ + ve₂ + A*e₃ (rows 1 and 3 of adj G = nG⁻¹, so f = n·e₁^#, f* = n·e₃^#, which lie in L). Then
Q(e₁) = v, Q(e₂) = t, Q(e₃) = u, Q(f) = n²(G⁻¹)₁₁ = nA, Q(f*) = nA*.
Each vector has a coordinate equal to 1, so all five are primitive. As n is odd, 4 | A ⟺ q(f̄) = 0, and likewise for A*.

**Lemma 1.1 (frieze parity; PROVED, elementary).** For odd n, exactly two entries of P(w) are even, and the corresponding
two vectors are distinct classes in W ∖ 0.
*Proof.* If t is even, n ≡ u + v (mod 2) forces exactly one of u, v to be even, and A, A* are odd. The even pair is (t, u)
or (t, v), with vectors e₂, e₃ or e₂, e₁. If t is odd, u and v are not both even (else n is even). If u and v are odd,
then A and A* are even and the vectors are f ≡ e₂ + e₃ and f* ≡ e₁ + e₂ (mod 2). If u is even and v odd, the even entries
are u and A* (A = tu − 1 is odd), with vectors e₃ and f* ≡ e₁ + e₂. The last case (v even, u odd) is symmetric. In every
case the two classes are distinct, and they lie in W because their norms are even. ∎

**Lemma 1.2 (CONSTRUCTIVE_ES Lemma 1.1).** An odd unimodular ternary ℤ₂-lattice is isotropic iff Q(x) ≡ 0 (mod 4) for some
primitive x. In that case exactly two classes x̄ ∈ L/2L satisfy q(x̄) = 0. (They lie in W ∖ 0.)

**Theorem 1.3 (the five 4-slices are the χ = −1 fibre: a conceptual proof of MODEL_SPECIFIC Thm 3.1(a); PROVED).** For every
word w of odd n, w ∈ S_4 ⟺ χ(w) = −1. Moreover at most two entries of P(w) are divisible by 4.
*Proof.* (⇐) χ = −1 means L₂ is isotropic (CHI_FLIP Thm 1.1). Then the two zero classes of q (Lemma 1.2) and the two even
pentagon classes (Lemma 1.1) are 2-element subsets of the 3-element set W ∖ 0. So they share an element: some pentagon
vector x has Q(x) ≡ 0 (mod 4), i.e. 4 divides its pentagon entry. (⇒) If 4 divides a pentagon entry, the corresponding
primitive vector has Q ≡ 0 (mod 4), so L₂ is isotropic by Lemma 1.2 and χ = −1. Last claim: a pentagon entry divisible
by 4 is even, so its class is one of the two even pentagon classes. ∎
*Remarks.* (a) No Dedekind sums and no cell enumeration are needed: the input is frieze parity (Lemma 1.1), the mod-4
isotropy test, and CHI_FLIP's reciprocity. (b) "Why 4" in one sentence: **q = Q mod 4 is the finest piece of Q that lives
on L/2L, and in the Fano plane the 2 isotropic points and the 2 even pentagon points must meet on the 3-point line W.**
For any odd M, "M | entry" is unrelated to the 2-adic structure. For M = 2^k with k ≥ 3, "2^k | entry" is a condition on
L/2^{k−1}L, not on L/2L (see §1.2). (c) The two isotropic classes are the classes x̄_i of CONSTRUCTIVE_ES Thm 1.2(b): the
two maximal overorders C₀(L + ℤx_i/2) ⊃ E(L), i.e. the two endpoints of the Eichler edge (the two ends of the supersingular
2-isogeny). So **a five-slice certificate is a word together with a pentagon vector that points at an endpoint of its
2-isogeny edge**, and Thm 1.3 says such a pointer exists whenever the edge does (i.e. χ = −1).
CERTIFIED (`scripts/z1_fano.py`): over all 4096 cells with letters 1..8 and n odd, the five pentagon classes are always
distinct, |iso ∩ pentagon| ∈ {1, 2} when χ = −1, and one non-pentagon class always has odd q.

### 1.2 Numerators 2^k: one fair bit per further level (CERTIFIED by cells)
For k ≥ 2, Q mod 2^{k} is well defined on L/2^{k−1}L. Given an isotropic pentagon vector x, the lifts x + 2y change Q(x) mod 8
by 4(B(x, y) + Q(y)), which is affine-linear in ȳ. So "8 | entry" is a further 2-adic bit attached to each isotropic pentagon
vector. A χ = −1 word has one or two isotropic pentagon vectors (Thm 1.3).
**Proposition 1.4 (CERTIFIED: all cells mod 32, `scripts/z1_depth_cells.py 5`).** Among χ = −1 cells, the share with one
(resp. two) isotropic pentagon vectors is 2/3 (resp. 1/3). The share in S_{2^k} equals
  f_k = (2/3)·2^{−(k−2)} + (1/3)·(1 − (1 − 2^{−(k−2)})²),
i.e. f₃ = 7/12, f₄ = 5/16, f₅ = 31/192 (exact; one-iso cells: 1/2, 1/4, 1/8; two-iso cells: 3/4, 7/16, 15/64). The same
fractions hold in each class n mod 16 (`z1_depth_bycls.py`).
This explains the "unexplained" cell fractions of MODEL_SPECIFIC Thm 3.1(b) (140/240 = 7/12 for m = 8, 600/1920 = 5/16 for
m = 16): **every further power of 2 in the numerator costs one fair bit per isotropic pentagon vector, and 4 costs none.**
(Assessment, not proved: on the Bruhat–Tits tree of PGL₂(ℚ₂) = SO(L ⊗ ℚ₂), depth-k pentagon vectors point at vertices at
distance k − 2 beyond the Eichler edge, so 8/n slices are 2-isogeny edges with an extra marked step, an X₀(4)-type datum.)

### 1.3 The bits are correlated inside a prime (EVIDENCE)
On actual words the bit model fails. Primes p ≡ 1 (mod 4), p < 4000 (`scripts/z1_bits_words.py 5 4000`): 4785 χ = −1 words
modulo reversal; their share in S_8 is 0.501 (cell law 0.583). Treating the bits as independent predicts 0.82 primes with
S_8(p) = ∅; **12 are observed** (17, 113, 241, 257, 353, 593, 1249, 1489, 1601, 2081, 3169, 3361). The reason is visible at
p = 131 and 241 (`scripts/z1_w131.py`): every entry divisible by 4 has v₂ exactly 2, and where both
even entries are A, A*, the 2-power of tp + 1 is split evenly (e.g. (5, 1, 33) at 131: A = 4, A* = 164, v₂(5·131 + 1) = 4 = 2 + 2).
The bit of a word is mostly a function of v₂(tp + 1), i.e. of (t, p) mod 2^k, and of the Ptolemy relation through the even
edge ((J)45: ee′ ∈ {1 + o, N + o, 1 + No}), so many words share one bit.
*Reading.* At 4 there is no bit, so the χ = −1 fibre is the whole target (Thm 1.3). At 8 the target is cut by bits that are
far from independent across the words of one prime. That is why 8/n fails at 131 and 241 although 29 and 12 χ = −1 words
exist there. Any "main term at Planck scale" argument for 8 would have to beat this correlation. For 4 no such
argument is needed; the problem is only whether a χ = −1 word exists at all (SQ₅).
