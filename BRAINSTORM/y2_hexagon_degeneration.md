# y2 — Hexagon vs pentagon: the 4-term proof, and exactly where it degenerates at k = 3 (O210)

Labels as in DISCOVERIES.md. **ES is not solved.** A word of HJ length r at N is an (r+2)-gon frieze with frozen
(1, …, 1, N). A vertex whose short diagonal (quiddity) is 4w gives 4/N as r unit fractions (the vertex fan, as in
LENGTH_THREE Thm 2.1). r = 3 is ES; r = 4 is the "hexagon ES".

## Idea
Find a frieze proof for the hexagon, and name the hypothesis the pentagon violates.

**Proposition 1 (hexagon proof; PROVED).** For N ≡ 1 (4), N ≥ 5, put k = (N + 3)/4. The interior word (2, 2, 2, k) has
K = 4k − 3 = N, and its diagonal λ₁₅ = K(2, 2, 2) = 4. The fan at V₆ gives
`  4/N = 1/k + 1/(k(2k−1)) + 1/((2k−1)(3k−2)) + 1/(N(3k−2))`   (sympy-verified identity).
For N ≡ 3 (4), ES itself is trivial, and its 3-term solution splits into 4 terms. So the hexagon problem has a
one-line uniform frieze solution, in particular at every odd square (no T1).

**Mechanism.** The diagonal λ₁₅ = 4 cuts the hexagon into
* a sub-pentagon (V₁…V₅) with frozen (1, 1, 1, 1, **4**), i.e. the N-independent interior word (2, 2, 2) at 4, and
* a **triangle** (V₁, V₅, V₆) with sides 4, 1, N.
A triangle carries no Ptolemy relation, so V₆ = kV₅ − V₄ is free and N = 4k − K(2, 2) is *linear* in one letter.
The N-dependence sits in a piece with no divisibility constraint.

**Theorem 2 (where the pentagon degenerates; PROVED, elementary).** In a pentagon with frozen (1, 1, 1, 1, N), a
diagonal that cuts off a triangle containing the N-side is h = λ₁₄ or h′ = λ₂₅. The other piece is a quadrilateral with
frozen (1, 1, 1, h), i.e. a length-2 word with K(x, y) = xy − 1 = h.
* For h = 4w the quadrilateral needs a factorisation 4w + 1 = xy, and N = 4ws − y then needs y ≡ −N (mod 4w). This is
  the Type I a = 1 slice: a divisor of the moving integer 4w + 1 in a residue class modulo the moving modulus 4w (B2).
* For h = 4 (no N-independent piece is left) the only quadrilaterals are the formal (1, 5) and (5, 1), which give
  N = 4s − 1 ≡ 3 (mod 4), exactly the class where ES is already trivial.
Diagonals that cut off a triangle *not* containing N (c, m, s = 4w) leave a quadrilateral that contains the N-side.
Its Ptolemy relation is a product = N + const, again a divisor event (e.g. c = 4w: hs = N + 4w).

**The violated hypothesis, in one sentence.** The hexagon proof needs an **interior frieze on the sub-polygon with
frozen (1, …, 1, 4)**. For the hexagon that sub-polygon is a pentagon, and K(2, 2, 2) = 4 exists. For the pentagon it is
a quadrilateral, and K(x, y) = 4 forces 5 = xy, which has no interior factorisation because 5 is prime. In general,
the free-triangle cut of an (r+2)-gon needs an interior word at 4 (or at 4w) of length r − 1. Interior words of
length ℓ have K ≥ ℓ + 1, so the interior words at 4 are exactly (4) and (2, 2, 2) (lengths 1 and 3). A length-2 word at 4w
is a factorisation 4w + 1 = xy, i.e. B2. So **among the polygon sizes, the pentagon (r = 3) is the one where the
"4-diagonal + free triangle" decomposition needs a divisor of a moving integer**. For r = 4 it is N-free via
(2, 2, 2). For r ≥ 5 one uses 4w-words of length r − 1, or simply (2, 2, 2) plus extra letters on the N-side. The obstruction is
the arithmetic of the number 4 itself, which parallels (J)32 (m = 4 is the unique numerator whose five slices form a
character fibre).

**Mod-2 rigidity, the other face of the same fact (EVIDENCE + PROVED pentagon side).** Up to the dihedral group the
pentagon has one mod-2 quiddity pattern (FRIEZE_ES Lemma 1.1). The hexagon has four: (1⁶), (0,1,1,0,1,1),
(0,0,0,1,0,1) and (0⁶) (walks on K₃ of winding 6 or 0). Their numbers among interior words with N ≡ 1 (4), N ≤ 5000,
are 3020, 15510, 39810 and 23413. Zero-mod-4 hexagon words occur with both Jacobi signs (e.g. pattern (0⁶):
11 039 with −1, 12 374 with +1). So the hexagon's zero locus is not a character fibre, and T1 has no hexagon analogue.

## Extra decoration (the brief's question)
Can a "pentagon + one decoration" restore the free triangle? A decoration that makes the sub-quadrilateral at
4 exist must change xy − 1 = 4. Two options were tried.
* **Non-tangent side Q² (ES^{(S)}).** Here the quadrilateral relation becomes xy = 4 + Q² (with the 4-diagonal opposite
  the Q²-side). That is the fixed-modulus shot (divisors ≡ 3 mod 4 of 4n + Q², LENGTH_THREE §6), still a divisor event,
  not a free triangle. ES^{(S)} is provable for |S| ≥ 4 because the shot family is *infinite* (Q varies), not
  because a triangle is freed.
* **Inserting an ear** (a letter 1) makes the pentagon a hexagon, but then the fan has 4 arcs, so it is not ES.
So the free-triangle mechanism is intrinsically "r ≥ 4". Assessment: no decoration keeps r = 3 and frees a triangle,
because r = 3 with the N-side in a triangle *is* the quadrilateral constraint.

## Literature
Continuants / HJ words: classical. Vertex-fan identities: Penner λ-lengths (LENGTH_THREE §2). The k ≥ 4 analogue of
ES with distinct terms is classical and easy; this memo only gives the frieze reading. Cuntz–Holm–Jørgensen
(arXiv:1909.02332) treat sub-polygons of friezes ("cutting out subpolygons"), which is the decomposition used here.

## Barrier screen
* T1: the hexagon proof works at squares, which is consistent with the absence of T1 for k = 4.
* B2: Theorem 2 shows that every pentagon decomposition reintroduces a divisor of a moving integer.
* B1: Prop 1 *is* a polynomial identity family, legal because k = 4 has no T1.

## Cheap numerics
`scripts/y2_hexagon.py 5000 3|4`.
* r = 4: every odd N ≤ 5000 except 3, 7, 15 has an interior hexagon word with a zero-mod-4 quiddity, including all
  odd squares.
* r = 3: there are 34 odd-square failures (all odd squares from 25 to 4761, plus 9) and 13 non-square failures
  (N ≡ 3 (4) cases and 105).

## Assessment
PROVED dictionary/obstruction (elementary). It answers (b) precisely: the hexagon proof uses an interior frieze on a
sub-polygon at 4, and at the pentagon that sub-polygon is a quadrilateral with K(x, y) = 4, impossible since 5 is prime.
Promise as a route: 0/5. SHARP as a statement: "at r = 3 the free-triangle cut needs a length-2 word at 4w, i.e. a divisor of 4w + 1 (no length-2 interior word at 4: 5 is prime)."
