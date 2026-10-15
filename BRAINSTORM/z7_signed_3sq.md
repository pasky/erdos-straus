# z7_signed_3sq — forced/unforced split on SQ_± and 3SQ (O231, goal 4)

## Idea
Apply the split to the two exception-free companions of SQ₅: the signed n-adic relaxation SQ_± ((J)52) and the
ℤ³-embedding 3SQ ((J)53).

## Results (UNFORCED_WORDS §6)
* Lemma S holds verbatim for signed words (|N_X|; zero side = clean).
* At SQ_±'s records (signed incl. positive: 4 884 441, 97 185; strictly signed: 9 817 305, 297 465, 60 369) with
  |t| ≤ 60 (EVIDENCE):
  * the forced fraction is 0.84–0.94, against 0.24–0.51 at controls n + 8;
  * the least certificate |t| reproduces SPARKS4 exactly (18, 15, 54, 30, 19).
  * So SQ_± hardness is forcedness too.
  * At 9 817 305, unforced words exist from |t| = 7, but the first certificate is at |t| = 54.
* **3SQ at 105.**
  * Jacobi cleanliness is genus-collapsed. Every side prime of 105's 11 words has (r/3) = (r/5) and (r/7) = +1, so
    U(105) = 0.
  * But every word has exactly two local signs ε_ℓ = −1: (J)53's "ramified at two odd primes".
  * Lemma 6.1 (PROVED): a side all of whose primes are ψ_ℓ-residues forces ε_ℓ = (−1/ℓ). This is −1 for ℓ ≡ 3 (4),
    i.e. non-embedding.
  * So 3SQ is the per-prime refinement of the split, and the 105 exception is the Jacobi collapse.

## Literature
SYNTHESIS_SPARKS4 §2 (SQ_±); THREE_SQUARES (3SQ); CHI_FLIP Thm 1.1 (local signs ε_ℓ).

## Barrier screen
SQ_± inherits B2 and "no finite t-set" (SPARKS4 §2.4); T1 respected in both. B6 for the control comparison.

## Cheap numerics
`scripts/z7_sqpm_split.py 60 <n…>` (STRICT=1 for strictly signed).

## Assessment
EVIDENCE + small PROVED lemma. Two outcomes: (i) the steering rule "try it on SQ_± first" gives the same
hardness = forcedness picture; (ii) the 105 exception of SQ₅/U is a genus-collapse artefact of Jacobi cleanliness. A
per-prime CONJECTURE U ("∃ ℓ ∥odd n and a word with no ψ_ℓ-clean side") is the natural exception-free version. Not
computed beyond 105.
