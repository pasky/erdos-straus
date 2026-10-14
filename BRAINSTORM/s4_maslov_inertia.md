# s4_maslov_inertia — the (J)45 Maslov count is half the negative inertia index; at HJ length 3 it is all-or-nothing (O218)

**ES is not solved here.** Labels as in DISCOVERIES.md. Cross-combination O218 (3): Maslov count (J)45 × HJ length 3
(J)9/(J)40 × frieze positivity (J)42 §3.

## Idea
TRANSPORT_LAW Thm 3.1: (K_{r−1}/N) = ∏(K_i, −K_{i+1})₂ · (−1)^{μ(w)}, μ(w) = #{i : K_i < 0 < K_{i+1}}. Ask: is there a
*signed* relaxation of ES with μ even (same Jacobi law as positive words, hence T1-bearing in the 2-adic form), and
does it say anything at length 3?

## Statements
**Lemma I (PROVED; Jacobi's signature rule).** For a word of length r with all leading continuants K_i ≠ 0 and
K_r = N > 0, the tridiagonal path matrix has negative inertia index ind_− = #{sign changes in 1, K₁, …, K_r} = 2μ(w).
*(LDLᵀ gives ⟨K_i/K_{i−1}⟩; a negative entry is a sign change; K₀ = 1 and K_r > 0 make − → + changes exactly half.)*
So (−1)^μ = (−1)^{ind_−/2} is the ∞-Hasse factor in the guise of the signature; CERTIFIED on 75 097 random signed words
(r = 3, 5, 7), 0 failures.
**Cor (PROVED).** At r = 3, ind_− ∈ {0, 2} (det N > 0), so μ ∈ {0, 1}: **μ even ⟺ μ = 0 ⟺ the word is positive**
(= L1 of s4_three_bits_meta). An "even-Maslov relaxation" at length 3 *is* ES: there is no room for a cancelling pair
of sign changes. At r ≥ 5, words with μ = 2 (signature (r − 4, 4)) exist and satisfy the positive-word Jacobi law; but
words of length ≥ 5 are not ES certificates and for positive r ≥ 5 the zero-mod-4 locus already fails T1 (FRIEZE §4
polygon-size uniqueness). So the even-Maslov relaxation is empty of ES content.

## Construction attempt
Use μ = 2 words of length 5 at p with the right 2-adic factors as *witnesses* of χ = −1 for their fraction p/A, then
contract to length 3? The HJ expansion of p/A is unique; its length is a property of A, not of the witness word, so a
length-5 signed witness only certifies (A/p) = −1 (the n-adic bit), which is the s4_three_bits_meta (R_n) lottery
again, and the length-3 requirement is B2. Dead.

## Barrier screen
T1: Cor is the length-3 rigidity of the anchor. B2: unchanged. Harness: numerator-free.

## Cheap numerics
`scripts/s4_inertia.py 9 r 50000` for r = 3, 5, 7: 25 116 / 25 065 / 24 916 words, 0 failures.

## Assessment
Small exact clarification (PROVED, classical in substance): the Maslov count is ind_−/2, and at length 3 positivity is
the *only* way to have trivial ∞-factor. The archimedean factor of ES is a single all-or-nothing bit, which is why
signed friezes have no T1 and no "partially signed" T1-bearing variant of ES exists on the five slices. Promise 0/5.
