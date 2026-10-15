# z1_marking_isometry — is five-slice membership a property of the lattice or of the marking? (O224)

## Idea
A five-slice certificate for M/n is a word w = (t, u, v) ∈ X_n (tuv − u − v = n) with M dividing one of the five
pentagon quantities P(w) = (t, u, v, A = tu − 1, A* = tv − 1) (MODEL_SPECIFIC Lemma 3.0). The word is a *marked*
lattice: the path lattice L_w (Gram [[v,−1,0],[−1,t,−1],[0,−1,u]], det n) plus a path basis. For M = 4 membership is a
genus invariant of L_w (S_4 = {χ = −1}, χ = −ε₂(Q_w): MODEL_SPECIFIC Thm 3.1, CHI_FLIP Thm 1.1). Question: for which M is
S_M at least an **isometry-class** invariant? If 8's slices were lattice-level too, a lattice-level mechanism (Hecke,
Kneser, theta, Siegel, isogeny graph) could transfer to 8/131 and prove a false statement (requirement (ii)).

## Literature
MODEL_SPECIFIC Thm 3.1 (character description, only M = 4); SEVEN_SIBLING SHARP 3 / (J)49 (S_7 is not an isometry
invariant, one example at n = 5); FOUR_SPECIFIC Thm 2.3 (one-odd / all-even is marking data); Greene, *Lattices, graphs and
Conway mutation*, Invent. Math. 192 (2013) (graph lattices determine 2-isomorphism classes — the expected reason for
uniqueness of interior markings, not re-derived here).

## Results
**Lemma 1 (norm-one triples; PROVED, elementary).** Let n be odd and n + 1 = ab (a, b ≥ 1). The words
w₁ = (1, a+1, b+1), w₂ = (a+1, 1, b), w₃ = (b+1, 1, a) lie in X_n, and L_{w_i} ≅ ⟨1⟩ ⊥ [[b, −1], [−1, a]] for i = 1, 2, 3.
*Proof.* Membership: (u−1)(v−1) = n+1 for t = 1, (t−1)v = n+1 for u = 1. For w₁ the vector e₂ has norm 1; the projections
e₁ + e₂, e₃ + e₂ have norms b, a and inner product 0 − 1 − 1 + 1 = −1. For w₂ the vector e₃ has norm 1, e₁ ⊥ e₃, and
e₂ + e₃ has norm (a+1) − 2 + 1 = a with e₁·(e₂ + e₃) = −1. w₃ is w₂ with a ↔ b. ∎
P(w₁) = {1, a+1, b+1, a, b}, P(w₂) = {a+1, 1, b, a, (a+1)b − 1}, P(w₃) = {b+1, 1, a, b, (b+1)a − 1}.

**Proposition 2 (PROVED).** Let M ≥ 2 with φ(M) > 2, i.e. M ∉ {2, 3, 4, 6}. Then there are infinitely many odd n with
gcd(n, M) = 1 carrying two isometric words, one in S_M and one not. Hence S_M is not a union of isometry classes.
*Proof.* Pick a unit x mod M with x ≢ ±1 (exists iff (ℤ/M)^* ≠ {±1} iff φ(M) > 2). Take a + 1 ≡ x, b ≡ x⁻¹ (mod M),
with a even if M is odd (for even M, x is odd so a is even automatically); then ab is even and n = ab − 1 is odd, and
n ≡ (x − 1)x⁻¹ − 1 = −x⁻¹ is a unit mod M. M ∤ a (x ≢ 1), M ∤ a+1, M ∤ b (units), M ∤ b + 1 (x⁻¹ ≢ −1); so w₁ ∉ S_M,
while (a+1)b − 1 ≡ 0 puts w₂ ∈ S_M. ∎ (First examples: M = 5, n = 3: (1, 2, 5) ∉ S₅ ∋ (2, 1, 4); M = 8, n = 5:
(1, 3, 4) ∉ S₈ ∋ (3, 1, 3).)

**Proposition 3.** (a) M = 2, 3, gcd(n, M) = 1: S_M = X_n (PROVED: if t, u, v are odd, A is even; mod 3, if 3 ∤ tuv and
3 ∤ A, A*, then tu ≡ tv ≡ 2, so u ≡ v and n ≡ 2v − u − v ≡ 0). (b) M = 4: S_4 is a genus invariant (PROVED, χ). (c) M = 6,
gcd(n, 6) = 1: S_6 is not a genus invariant (at primes 5 ≤ p < 3000 both χ-halves split: 8601/18927 χ = −1 words and 3984/8405
χ = +1 words lie in S₆), but **no isometry class is mixed** for odd n < 300 coprime to 6 (EVIDENCE, `z1_marking2.py`). On the norm-one
triples this is PROVED by the {±1} argument: if (ℤ/M)^* = {±1} and M ∤ a, a+1, b, b+1 then a+1 ≡ ±1 forces a+1 ≡ −1,
b ≡ ±1 forces b ≡ 1, and (a+1)b − 1 ≡ −2 ≢ 0, (b+1)a − 1 ≡ 2(−2) − 1 = −5; for M = 6 that is ≡ 1 (mod 6); the cases
where w₁ ∈ S_M are symmetric (check: `z1_marking2.py` finds no exception).
**EVIDENCE 4 (`z1_interior_unique.py`).** For odd n < 600, isometric interior words (all letters ≥ 2) agree up to reversal
(1715 classes, 0 exceptions). Up to n < 400 every multi-marked class found is a norm-one triple.

So, conditional on EVIDENCE 4 (uniqueness of interior markings and "norm-one triples are the only multi-marked classes"):
**S_M is a union of isometry classes for all n coprime to M ⟺ (ℤ/M)^* = {±1} ⟺ M ∈ {2, 3, 4, 6}; among these, S_M is a
non-trivial genus invariant only for M = 4.** Prop 2 (the ⇒ half) is unconditional.

## Barrier screen
Not an existence mechanism; steering only. B5/T1: at odd squares S_4 = ∅ is a genus statement (CHI_FLIP Cor 1.3), so any
argument that produces a path class in the B_{p,∞}-genus is T1-safe and 105-safe by construction (both are statements about
χ). (ii): a mechanism acting on *isometry classes* cannot by itself certify 8/n: for 8 it would have to control markings,
i.e. which of the up to three norm-one markings (or, interiorly, which pentagon vector) carries the 8. B2/B3: unchanged —
existence of a path class in 𝔊⁻_p is the SQ₅ lottery.

## Cheap numerics
`scripts/z1_marking.py 3 400` (1810 path classes, mixed: M = 3, 4: 0; M = 5: 288; 8: 134; 12: 68; 16: 83; all via boundary
words), `scripts/z1_marking2.py 300` (n coprime to M, M ≤ 30: mixed classes exist exactly for M ∉ {2, 3, 4, 6}),
`scripts/z1_interior_unique.py 600`.

## Assessment
PROVED (Lemma 1, Prop 2, Prop 3(a),(b)); EVIDENCE (Prop 3(c), uniqueness of interior markings). The 4-vs-8 difference
at lattice level is real but small: on interior words every S_M is a class function (one marking), and the split shows up
only on norm-one lattices. The useful output is the steering rule: requirement (ii) and T1 are automatic for any argument
that works with the χ = −1 genus of path lattices; the whole difficulty is requirement (i). Promise 1/5.
