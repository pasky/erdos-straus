# z37 — The RS-type invariant cannot tell numerator 4 from 8 (O267)

## Idea
Brief goal 4: does the reciprocity invariant distinguish 4/n from 8/n (real exceptions 131, 241 for k = 8)?

## Literature
AMPLIFY_EXCEPTION Thm 2.5 (numerator models), (J)41 numerator blindness, DEDEKIND Thm 4.5.

## Content (QUESTION_R §4.1)
The (A)3_k slice k·abc − a − b = n is the set of length-3 words with k | t. The sign (A/n) is constant (−1) on it iff
4 | k (PROVED for 4 | k via Cor 1.3; EVIDENCE that it is non-constant for all other k ≤ 16). So 4 and 8 have the same
character and the same square obstruction; the 8-slice is a sub-slice of the 4-slice of half the congruence density.
At p = 241 neither slice has a word; 215 primes p ≡ 1 (4) < 2·10⁴ lack an 8 | t word.

## Barrier screen
B3: the 4-vs-8 difference is main-term size only. T1: both obstructed at squares.

## Cheap numerics
`scripts/z37_numerators.py 20000`.

## Assessment
PROVED + EVIDENCE; negative for any reciprocity-based distinction between numerators.
