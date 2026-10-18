# z39_quartic_slices — no quartic (Kubota-type) sign on the k | t slices (O269)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
HKRS found quartic reciprocity obstructions in Apollonian packings beyond the quadratic ones. ES's T1 is the
quadratic (theta) multiplier. Is there a quartic multiplier analogue on the numerator-k slices (k = 8, 16: words
with k | t, QUESTION_R §4.1), which might explain numerator-8 exceptions (8/p: 2, 3, 11, 17, 131, 241 below 2000)?

## Results
1. **Symmetry no-go (PROVED, one line).** For a word w, AA* = tp + 1 ≡ 1 (mod p), so for p ≡ 1 (mod 4) the quartic
   residue characters satisfy χ₄(A*) = χ₄(A)⁻¹. The slice {k | t} is invariant under u ↔ v (A ↔ A*). On the 4 | t
   slice A is a non-residue, χ₄(A) = ±i, and the two orderings give i and −i: **no u↔v-symmetric quartic sign of A
   exists on any slice**; only an ordered (e.g. smaller-divisor) bit can be tested.
2. **Smaller-divisor quartic bit (EVIDENCE, negative; `scripts/z39_quartic.py 20000 k`).** Primes p ≡ 1 (8) < 2·10⁴,
   i := a/b mod p for p = a² + b² (a odd): the bit χ₄(min(A, A*)) ∈ {i, −i} is constant on the slice only when the
   slice has very few words; among constant cases the value is i in 60/127 (k = 4), 134/264 (k = 8), 125/242
   (k = 16) — balanced. Mixed for 413/540 (k = 4), 190/454 (k = 8), 39/281 (k = 16) primes; empty slices 16, 102,
   275. No quartic invariant.
3. **Numerator exceptions (Assessment).** 131 ≡ 3 (4) is inert in ℤ[i] (no quartic symbol at all); 17 and 241 are
   ≡ 1 (16) with 2 a quartic non-residue, shared by many soluble primes (97, 193, 401, 433, 449). QUESTION_R §4.1
   already showed 8 and 4 share the quadratic invariant; the exceptions are a B3 (slice size) phenomenon. Agrees
   with z35_free_quartic_bit (balanced quartic bit in a different normalisation) and bsD_missed_primes.

## Literature
Haag–Kertzer–Rickards–Stange, "The local-global conjecture for Apollonian circle packings is false", Ann. of Math.
200 (2024) (quartic obstructions); Kubota, "On automorphic functions and the reciprocity law in a number field"
(1969); Ireland–Rosen Ch. 9 (quartic reciprocity, 2 as quartic residue).

## Barrier screen
T1: the quadratic obstruction is unchanged; no quartic analogue. B3: numerator-8 exceptions are size effects
(QUESTION_R §4.1, (J)41). B2/B1/B4/B6: n/a.

## Assessment
PROVED no-go (item 1) + EVIDENCE (item 2). Brief's question (3) answered negatively in this setting. Promise 0.
