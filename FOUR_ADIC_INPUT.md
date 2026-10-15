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
CERTIFIED at word level (`scripts/z1_thm13_check.py 1500`): all 35 179 words of all odd n < 1500 have exactly two even pentagon
entries, at most two entries divisible by 4, and (4 | some entry) ⟺ χ = −1 (sympy Jacobi), with 0 violations.

## 2. The requirements (i)–(iv) after Theorem 1.3

**Proposition 2.1 (steering; PROVED parts as labelled).** Let P(p) := "X_p has a word w with L_w ⊗ ℤ₂ isotropic" (= SQ₅ at
primes, CHI_FLIP C1).
(a) P(p) ⟺ ES-five(p) (Thm 1.3 + MODEL_SPECIFIC Lemma 3.0). PROVED.
(b) (iii) holds for P: at odd squares no path lattice is 2-adically isotropic (T1 = CHI_FLIP Cor 1.3; T1 in Legendre form:
z1_legendre_levels Cor 2). PROVED. P also fails at the composite 105 (CHI_FLIP §4.1), so a proof of P must use more than
non-squareness.
(c) (ii) holds for P in the strong sense: P(131) and P(241) are true (29 resp. 12 χ = −1 words), while 8/131 and 8/241 are
false. So P does not imply 8/p. What 8/p additionally needs is one 2-adic bit per isotropic pentagon vector (§1.2), and at 131,
241 every bit fails (§1.3). For 11/37 there is no character description of S₁₁ (MODEL_SPECIFIC Thm 3.1(c)), so P has no
11-analogue at all. TES and ES_q: P is a statement about the path lattices of X_p over ℤ and has no transcription there in
this file. So (ii) for those failure sets is "not applicable", not "checked".
(d) (iv) fails for P: S₇ is not a character fibre, and S₇(p) = ∅ at 10 primes ≤ 10⁵ (FOUR_SPECIFIC). z1_small_prime_pigeonhole:
the pigeonhole forcing exists only for M ∈ {2, 3, 4}.
(e) (i) for P is CONJECTURE SQ₅ (EVIDENCE to 10⁸, DEDEKIND/HJ_DEEP; 10⁷ with boundary words, MODEL_SPECIFIC).
*Reading.* After Thm 1.3, the 4-specific 2-adic input is **used up**. ES-five is equivalent to P, and P has no numerator in
it. So a proof of P need not itself be 4-specific: it cannot prove 8/131, because P ⇏ 8/p. The (J)41 demand ("an ES
proof needs a 4-specific input") is discharged by routing through Thm 1.3. MODEL_SPECIFIC §3 said this for λ(p) ≤ 3; Thm 1.3
says why the routing costs nothing. Every 2-adic *refinement* of the target (2^k-slices, the one-odd half S₄^{odd} of
FOUR_SPECIFIC, the Legendre levels) is a strict sub-lottery. Two of them fail at primes: S₈ at 27 primes ≤ 10⁷, the Legendre
levels at 7 primes ≤ 10⁶. Every 2-adic *coarsening* of the target contains χ = +1 cells, which certify nothing.

| candidate property (numerator 4) | (i) primes | (ii) 8/131, 8/241 | (iii) odd squares | (iv) 7 | file |
|---|---|---|---|---|---|
| P = SQ₅ (some 2-adically isotropic path lattice) | EVIDENCE 10⁸ | not implied ✓ | fails ✓ (T1) | ✗ | §2 |
| Legendre levels (tp = 4^a(8b+7) carries a word) | **fails at 73**, 1201, 1489, 9649, 21169, 23041, 44641 | ✓ | fails ✓ | ✗ | z1_legendre_levels |
| spine t = 1 | fails (5013 primes p ≡ 1 mod 8 < 10⁶) | ✓ | ✓ | ✗ | CONSTRUCTIVE_ES 3.3 |
| one-odd five-slice half S₄^{odd} | EVIDENCE 10⁷ | ✓ | ✓ | ✗ | FOUR_SPECIFIC §2 |
| Siegel/mass weight of 𝔊⁻_p on lattices ⊃ M | genus shadow only | — | ✓ | ✗ | z1_glue_square_roots |
| 2-isogeny walk from χ = +1 | impossible (no crossing) | — | — | — | z1_isogeny_pointer |
| "4 is a square" | refuted by 9/p, 16/p | — | — | — | z1_square_numerator |

## 3. Attempts at (i): what a global object would have to do

**Proposition 3.1 (path classes as glued planes; PROVED, z1_glue_square_roots).** A positive ternary lattice L of det p
(unimodular away from p) is a path lattice iff it contains a primitive plane M with
(1) a basis of Gram [[v, −1], [−1, t]], so D := det M = tv − 1 and v | D + 1 (a *divisor form* in M's class), and
(2) gluing class c ≡ ±1 (mod D) with respect to that basis (L/(M ⊕ M^⊥) ≅ ℤ/D, generator ↦ c·e₂^#), equivalently D | p + v.
Siegel–Weil / mass formulas on 𝔊⁻_p see only the genus of (M, c), i.e. whether −p·v⁻¹ is a square mod D. Condition (2) is a
residue condition (B2, Prop 10.3), and (1) is a second divisor event at the binary level. Path lattices are the "elongated"
classes of 𝔊⁻_p (two small successive minima, λ₁λ₂ ≍ D, λ₃ ≍ p/D), of which there are ≍ log²p among ≍ p/16 classes.

*Construction attempts, each pushed against the barrier it met (iteration record).*
1. **Global 2-adic forcing** (brief angle 4, Hilbert symbol). Thm 1.3 is a pigeonhole *inside one word*. A global analogue
   would be a pigeonhole over the words of X_p. But a word's χ is (−A/p), and there is no finite structure on X_p whose
   size beats the number of χ-classes: X_p has no group action (CHI_FLIP §2: linear in each letter, no Vieta moves), and
   the classical moves leave X_p. *Hypothesis met:* B2 (moving modulus). *Modification tried:* replace the word set by the
   Legendre levels, where χ is forced to −1 by ℤ³, so only existence remains. Result: existence still fails (73, …), so
   removing the character does not remove the lottery (z1_legendre_levels).
2. **ℤ³ input** (one-class genus of I₃). If ES-five fails at p, every word gives x, y ∈ ℤ³ with |x|² = A*, |y|² = A, x·y = 1
   (TWO_FIBRES Thm A). For the word (1, 3, (p+3)/2) this is p = X² + 2Y² (y = (1, 1, 0) forces x = (x₁, 1 − x₁, x₃), and
   (2x₁ − 1)² + 2x₃² = p), which is always solvable for p ≡ 1, 3 (mod 8). Every such consequence is a genus statement that is
   true, so no contradiction can arise from ℤ³ data word by word (Prop 10.3). *Modification tried:* combine several words
   through z = x × y (|z|² = tp): different words have different t, hence different z-norms, and no relation links them.
3. **Mass at Planck scale** (angle 1): z1_depth_bits and z1_glue_square_roots. For 4 the conditional 2-adic density is 1, so
   nothing is to be forced. The count of χ = −1 words is the SQ₅ lottery itself.
4. **Isogeny walks** (angle 2): z1_isogeny_pointer (no crossing; pointer automatic; path edges below expander resolution).
5. **Exponent 2** (angle 3): what survives of "4 = 2²" is v₂(M) = 2 with odd part 1, i.e. Thm 1.3 (z1_square_numerator).

## 4. Outcome (Assessment)
* **Positive (PROVED):** Thm 1.3, a conceptual proof that the five 4-slices are the χ = −1 fibre (Fano pigeonhole). It uses
  frieze parity plus the mod-4 isotropy test, and identifies a certificate as "path-shaped 2-isogeny edge + pointer to an
  endpoint". Prop 1.4 (CERTIFIED): the fair-bit law for numerators 2^k (7/12, 5/16, 31/192, …). It explains MODEL_SPECIFIC's cell
  fractions and puts 4 at zero bits.
* **Negative (precise):** after Thm 1.3 no 4-specific 2-adic input is left. The requirements (ii) and (iii) are automatic for
  any proof of SQ₅, and (iv) is not available from this mechanism. Requirement (i) is SQ₅, whose obstruction is the thin
  path-shape set (Prop 3.1: divisor form + glue residue), i.e. B2. None of the four brief angles produces a forcing
  mechanism. Each fails at an identified hypothesis (table §2, list §3).
* **EVIDENCE:** inside one prime the depth bits for 8 are strongly correlated (12 observed against 0.82 predicted S₈-empty
  primes below 4000). This is the quantitative reason why 8/p fails where 4/p does not.
