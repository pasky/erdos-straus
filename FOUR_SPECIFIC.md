# FOUR_SPECIFIC — hunting 4-specific inputs after the numerator-blindness barrier (task O212, spark relay Y4)

Builds on SYNTHESIS_SPARKS3 (O208; R207 repair: the "must be 4-specific" reading is an Assessment, since thresholds
n > n₀(M) are not excluded by finitely many failures; threshold-robust form via Pomerance–Weingartner Thm 1.2),
MODEL_SPECIFIC (J)32, CHI_FLIP (J)33. Memos: `BRAINSTORM/y4_*.md`; scripts `scripts/y4_*`.
**ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.

## 0. Iteration log (construction → kill → hypothesis → modification)
(Y1) *Which numerators are blind?* O208 Thm 1.1 used (−M/g) = −1 for g ≡ −1 (M). This holds exactly for M ≡ 0, 3 (mod 4)
(−M a discriminant), §1. Result: T1 is not 4-specific; 7 is a T1-bearing, failure-free sibling. It becomes the control
for every candidate (§5).
(Y2) *One-odd SQ₅.* ES = 8/n ⊔ one-odd. On the five slices the parity is v₂ of the slot (§2). "S₄^{odd}(p) ≠ ∅" holds at
every prime ≤ 10⁷, while S₈ fails 27 times. Kill: it is false at composites (321, 4545, …), where SQ₅ holds, and it has
no 2-adic lattice meaning (§2.3). Hypothesis violated: none; it is strictly harder than SQ₅. Modification: none worth it.
(Y3) *Genus of path forms as a deterministic mechanism* (certificate ⟺ Q_w ℚ₂-isotropic ⟺ Q_w in the "B_{p,∞}" genus).
Kill: already bsA_selling_sandpile D3. The genus has ≍ p classes, only ≍ log²p of which are path forms (B3).
(Y4) *Universal witnesses.* Can a single slot value A serve all of its χ = −1 classes? Exactly for
A ∈ {2, 3, 5, 7, 8, 15, 20}, and their reach is exactly Mordell's 840 (§4, PROVED). Hypothesis of B1 (a finite menu)
satisfied, hence the ceiling. Modification: let A grow. This gives the τ(A+1)/φ(A) lottery (B2).
(Y5) *First lottery.* 4 is the unique M ≥ 3 with a {±1}-unit-group slice (e ∈ {1, 3}) at every prime (§3, PROVED).
For p ≡ 1 (mod 12) both e = 3 slices are empty 9.1% of the time (p < 10⁶): not deterministic. Modification: combine
with the χ-fibre. The e = 3 slices are a sub-union of the χ = −1 words at t = 3 and t = 1 (§3.2), so nothing new.
(Y6) *Harness on the hatches* (§6). All are uniform skeletons with a lottery content. Only the χ-fibre passes as a
stated 4-specific input.

## 1. T1-bearing numerators (PROVED; BRAINSTORM/y4_t1_numerators, `scripts/y4_t1_numerators.py`)
**Prop 1.1.** For M ≥ 3, (−M/g) = −1 for all odd g ≡ −1 (mod M) ⟺ M ≡ 0, 3 (mod 4). Hence (Cor 1.2): the
M-shot relaxation M^□ is a theorem at every odd non-square prime to M for every M ≥ 3 (Dirichlet); its odd-g shot family
has T1 exactly when M ≡ 0, 3 (mod 4) (even g sneak in iff M ≡ 3 mod 8); for M ≡ 1, 2 (mod 4) the relaxation holds at
squares too. Checked for M = 3..24 (odd squares k ≤ 99, Q ≤ 40) and at every census failure (exact certificates).
New harness entry: **11/37** (non-trivial: 11/37 < 3), `11/37 = 1/8 + 1/148 + 49/296`.
T1-bearing and failure-free to 10⁸: **3 (trivial), 4, 7**.

## 2. The one-odd half on the five slices (BRAINSTORM/y4_oneodd_slices)
**Lemma 2.1 (PROVED).** For a word w = (t, u, v) of odd n and a slot X ∈ {A, A*, t, u, v} with 4 | X, the (J)32 slice
solution has exactly one odd denominator iff v₂(X) = 2, and is all-even (an 8/n solution, (J)32 Lemma 2.1(b)) iff
v₂(X) ≥ 3. So S₄ = S₄^{odd} ∪ S₈. 0 violations on 16 242 words (n ≤ 801), exact check.
**Pentagon dictionary.** With Gram G_w = [[v, −1, 0], [−1, t, −1], [0, −1, u]] (basis e₁, e₂, e₃), the five slots are
the norms Q(e₁) = v, Q(e₂) = t, Q(e₃) = u and the determinants of the two adjacent planes, det⟨e₂, e₃⟩ = A,
det⟨e₁, e₂⟩ = A*. (J)32 + (J)33: Q_w is ℚ₂-isotropic ⟺ one of the five pentagon quantities is ≡ 0 (mod 4). Lemma 2.1:
the certificate is one-odd ⟺ that quantity is ≡ 4 (mod 8).
**Cells (CERTIFIED).** The 240 χ = −1 cells mod 8 split 100 / 100 / 40 (one-odd only / S₈ only / both). S₄^{odd} and S₈
each fill 140/240.
**Theorem 2.3 (PROVED relative to the classification of ℤ₂-lattices by 2-adic symbols, Conway–Sloane SPLAG Ch. 15
§7 / O'Meara §93).** For odd n and every word w with χ(w) = −1, Q_w ⊗ ℤ₂ ≅ ⟨1, −1, −n⟩. Hence all certificate
lattices of a fixed n are ℤ₂-isometric, and **no invariant of the ℤ₂-lattice separates one-odd from all-even
certificates**. The distinction is a property of the marking (which pentagon quantity carries the 4).
*Proof.* det G_w = n is odd, so L = Q_w ⊗ ℤ₂ is unimodular. χ = −1 ⟺ L ⊗ ℚ₂ is isotropic ((J)33 Thm 1.1); take a primitive
isotropic x ∈ L. Unimodularity gives y with B(x, y) = 1, so P = ⟨x, y⟩ is a unimodular plane of determinant −1 (Gram
[[0, 1], [1, Q(y)]]), either H or ≅ ⟨1, −1⟩, both of oddity 0. Then L = P ⊥ ⟨−n·s²⟩ with s a 2-adic unit, so L has
determinant n and oddity ≡ −n (mod 8), the same 2-adic symbol as ⟨1, −1, −n⟩ (L is odd, since rank 3 with odd
determinant). Same symbol ⇒ isometric. ∎
(Cross-check, `scripts/y4_oddity.py`: on all χ = −1 words of n ≤ 401 the computed oddity is 7, 5, 3, 1 for n ≡ 1, 3, 5, 7 (8),
i.e. −n mod 8, and all three parity classes occur within each oddity class.)
**Census (EVIDENCE; `scripts/y4_oddslice.c`, every hit verified in 128-bit with its parity).** S₄^{odd}(p) ≠ ∅ for every
prime 3 ≤ p ≤ 10⁷. S₈(p) = ∅ at 27 primes (reproduces (J)32). Odd squares ≤ 10⁶: S₄^{odd} = S₈ = ∅ (T1). The full
one-odd ES half has no failing prime ≤ 10⁶ (`ms_census 4 10⁶ p 1`). The one-odd half of 8/p fails at 3, 11, 17, 59, 131,
241, 449. Composite odd non-squares n ≤ 2·10⁵ with S₄ ≠ ∅ but S₄^{odd} = ∅: 321, 4545, 5481, 8745, 9121, 13041, 25305,
57481, 169425.
**Where 8/n's failures sit.** At 131, 241 every ES solution is one-odd (32 and 8 solutions; MODEL_SPECIFIC §2). All five
8/p failures are p ≡ 1, 3 (mod 8): exactly the classes where 8 has no slice with e ∈ {1, 3} (§3). For p ≡ 1 (mod 8)
and odd t, v₂(tp + 1) = v₂(t + 1), so I-slices at t ≡ 3 (mod 8) (e.g. t = 3) are always one-odd. This small-t bias makes
S₄^{odd} fire at t ≤ 4 for 98% of p ≡ 1 (mod 8), against 86% for S₈ (first 3000 such primes).
**Verdict on goal (b) (Assessment).** The one-odd half is 4-specific, but it is a description: it has no character or
ℤ₂-lattice meaning (Thm 2.3), it is strictly harder than SQ₅, and it is false at composites. A "parity mechanism forcing a
one-odd solution" would have to act on the marking, i.e. on the word itself. That is the χ-flip problem of (J)33 plus a
2-adic refinement, so it is harder, not easier.

## 3. The first lottery: 4 is the only numerator with a {±1}-slice at every prime (BRAINSTORM/y4_catalogue)
**Prop 3.1 (PROVED).** Type II slices of M/p need e ≡ −p (mod M), and Type I slices need e ≡ −p⁻¹ (mod M). The only
M ≥ 3 for which every prime p ∤ M has such a slice with e ∈ {1, 3} is **M = 4**. (At most the three classes −1, −3, −3⁻¹
are covered, so φ(M) ≤ 3 and M ∈ {3, 4, 6}. For 3 and 6, e = 3 is not a unit.) Brute check M < 200: `scripts/y4_slice3.py`.
**3.2 Meaning.** (ℤ/e)^* = {±1} for e ∈ {1, 2, 3, 4, 6}. On an e = 3 slice the event −1 ∈ Σ₃(N) is "N has a prime factor
≡ 2 (mod 3)", a non-triviality event and not a hitting event. For p ≡ 1 (mod 12), ES has two such slices,
N_II = (p+3)/4 and N_I = (3p+1)/4. Both fail iff all their prime factors are ≡ 1 (mod 3). This happens for 1771 of the
19564 primes p ≡ 1 (mod 12) below 10⁶ (9.1%; 10.7% below 10⁴), first at 241, 409, 769 (EVIDENCE). The e = 3 Type I slice
is the t = 3 word family and the e = 3 Type II slice is a t = 1 family (MODEL_SPECIFIC §7 C2), so both lie inside the
χ-fibre: Prop 3.1 refines the χ-fibre at small t and is not an independent input.
**3.3 Failures of other numerators avoid such slices (EVIDENCE).** Across all census failures (M = 5–24), failures in a
class with an e = 3 slice occur only for M = 10 (4 of 7), 16 (4/37) and 22 (9/53), and then always with N having only
primes ≡ 1 (mod 3) (e.g. 10/67: N = 7). M = 8: 0/5; M = 20: 0/62 (its e = 3 classes are 2/8 of the units). e = 1 is the
trivial two-term class, so it never fails.

## 4. Mordell's 840 is the exact reach of universal one-slot witnesses (PROVED; BRAINSTORM/y4_mordell_witness)
**Lemma 4.1.** A word of the prime p with first slot A exists ⟺ some t | A + 1 has tp ≡ −1 (mod A) (⟺ A | p + u for some
u | A + 1). By (J)32 it is an ES certificate iff (−A/p) = −1.
**Theorem 4.2.** The non-square A ≥ 2 such that every prime p ≡ 1 (mod 4) with (−A/p) = −1 has a word with slot A are
exactly {2, 3, 5, 7, 8, 15, 20}. The union of their χ = −1 classes is the complement, among p ≡ 1 (mod 4), of Mordell's
six square classes mod 840. (Proof: Dirichlet reduces this to a class check mod lcm(8, A), done for A ≤ 3000. For A > 3000,
the needed image has ≥ φ(A)/2 residues mod A, but |D_A| ≤ τ(A+1) ≤ 2√(A+1) < φ(A)/2, by Rosser–Schoenfeld.)
Cross-check: for all primes p ≡ 1 (mod 4) below 10⁶, the witnesses produce verified certificates exactly off Mordell's
classes (0 mismatches, `crosscheck(10**6)`).
**Reading.** The classical 840 is the point where single slot values stop covering their character half: beyond it a
slot A covers a τ(A+1)/φ(A) fraction of its χ = −1 classes. That is the B2 lottery written one slot at a time. It
also explains why the 8-analogue covering leaves non-square classes: for 8 a χ = −1 word is not a certificate
((J)32 Thm 3.1(b)).
