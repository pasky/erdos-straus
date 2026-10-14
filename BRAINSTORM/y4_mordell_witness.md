# y4_mordell_witness — Mordell's 840 is exactly the reach of universal one-slot χ-witnesses (O212, goal (a))

## Idea
(J)33 §3.1: for q ∈ {3, 5, 7} a non-residue, "A = q" gives an ES certificate word. Make this exact: for which A is
the slot value A a *universal* witness, and why does it stop where Mordell's covering stops?

**Lemma 1 (PROVED, algebra).** For a prime p ∤ A, a word (t, u, v) of p with first slot tu − 1 = A exists iff some
divisor t of A + 1 satisfies tp ≡ −1 (mod A). (Then u = (A+1)/t; gcd(t, A) = 1, so A* = (tp+1)/A ≡ −1 (mod t)
follows from A ≡ −1 (mod t), and v = (A*+1)/t ≥ 1.) By (J)32 Thm 3.1(a) it is an ES certificate iff (−A/p) = −1.

**Theorem 2 (PROVED: Lemma 1 + Dirichlet + a finite check + an explicit size bound).** Call a non-square A ≥ 2 a
*universal witness* if every prime p ≡ 1 (mod 4) with (−A/p) = −1 has a word with first slot A. Then the
universal witnesses are exactly **A ∈ {2, 3, 5, 7, 8, 15, 20}**. Their χ = −1 classes cover exactly the
p ≡ 1 (mod 4) outside {p ≡ 1 (8), (p/3) = (p/5) = (p/7) = 1}, i.e. **precisely Mordell's six square classes mod 840
remain.**
*Proof.* For p ≡ 1 (4), (−A/p) = (A/p) depends on r = p mod L = lcm(8, A); by Dirichlet every admissible class r
contains primes, so universality ⟺ for each r ≡ 1 (4), gcd(r, A) = 1, (A/r) = −1: −r⁻¹ mod A ∈ D_A := {t mod A : t | A+1}.
This is a finite check per A (`scripts/y4_witness.py`, `exact_scan(3000)`: non-squares passing it = {2, 3, 5, 7, 8, 15, 20};
squares pass vacuously). For A > 3000: the χ = −1 classes number φ(L)/4 (A non-square ⇒ (A/·) non-trivial on r ≡ 1 (4)),
each residue a mod A has φ(L)/(2φ(A)) lifts, so the needed image has ≥ φ(A)/2 elements, while |D_A| ≤ τ(A+1) ≤ 2√(A+1).
Rosser–Schoenfeld φ(A) > A/(e^γ log log A + 3/log log A) (valid for all A ≥ 3) gives φ(A)/2 > 2√(A+1) for all A ≥ 3000 (at A = 3000:
292 vs 110; the ratio increases). Coverage: A = 2, 8 ↔ p ≡ 5 (8); 3 ↔ (p/3) = −1; 5, 20 ↔ (p/5) = −1; 7 ↔ (p/7) = −1;
15 ↔ (p/15) = −1, which is already covered by 3 or 5. ∎
EVIDENCE cross-check (independent route: build the word, verify every slice solution in exact rationals) for all
primes p < 10⁵: A ∈ {2, 3, 7, 15} never miss (all p); A = 5 misses 1206 primes, all ≡ 3 (mod 4) (handled by the
two-term identity); all other prime A ≤ 59 miss 36–92%.

## Literature
Mordell (Diophantine Equations, 1969, p. 287–290): ES for all p except p ≡ 1, 121, 169, 289, 361, 529 (mod 840).
Yamamoto (1965) / ET Prop 1.6: such classes cannot be covered (T1). DEDEKIND_ES Thm 4.5, (J)32, (J)33 §3.1.
The "exactly these A, by τ(A + 1) ≥ φ(A)/2" explanation is, to my knowledge, not in the literature (not searched exhaustively).

## Barrier screen
B1: this is a congruence covering, so it stops at a finite level by POINTWISE_SIZE Thm M. Theorem 2 makes the stop
**intrinsic**: a single slot value A can serve all of its χ = −1 classes only if the ≤ τ(A + 1) divisors of A + 1 hit
φ(A)/2 residues, so the reach is finite and equals Mordell's. T1: the remaining classes are the squares, as they must be.
Numerator harness: Thm 2 rests on (J)32 Thm 3.1(a), so it is 4-specific. For 8, a χ = −1 word with A = q is not an
8-certificate (no slot divisible by 8 is forced), and indeed the 8-analogue of Mordell's covering leaves non-square
classes (131, 241; MODEL_SPECIFIC §4.1).

## Assessment
PROVED (clean, small): the classical level 840 is the exact reach of one-slot universal χ-witnesses. It is a
*description* of why the 4-specific χ-fibre gives exactly Mordell's covering and no more. As an *input* it is B1,
and it fixes the size of the remaining lottery: beyond 840 every witness A covers only a τ(A+1)/φ(A) fraction of its
classes. This is the B2 lottery in "one slot at a time" form.
