# Analytic-input audit for the review follow-up

## Published source: ordinary PNT and effective exceptional-zero gap

H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I: Classical Theory*, Cambridge Studies in Advanced Mathematics 97 (2007), chapter 11.

Verified directly from the author-hosted chapter:
https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/15.0_pp_358_396_Primes_in_arithmetic_progressions_II.pdf

Chapter DOI: https://doi.org/10.1017/CBO9780511618314.013

- Corollary 11.10 (Page), p. 369: the product over primitive characters of conductors at most Q has at most one zero in the stated region σ≥1−c/log(Qτ); it is real with quadratic character. At height zero this supplies one global exception for the whole modulus range.
- Corollary 11.12, p. 370: for an exceptional zero of a quadratic character modulo q, `1−β ≥ c/(sqrt(q)(log q)^2)`. This is effective; the proof uses the effective lower bound for L(1,χ) in Theorem 11.11 and equation (11.10), not Siegel's theorem.
- Theorem 11.16, p. 378: uniform character PNT for q≤exp(2c₁ sqrt(log x)), with the exceptional-zero term separated.
- Corollary 11.17, p. 379, and the statement on p. 380: the PNT constants are effectively computable.
- Corollary 11.20, p. 381, equations (11.32), (11.34): the required θ(x;q,a) formula, with the per-modulus exceptional term. Combine with Corollary 11.10 and absorb any exceptional zero below the common threshold to obtain equation (14) with one global exceptional pair. The derivation is retained in the main note.

The local downloaded PDF/text were inspected but are not added to the repository. These precise citations replace the earlier chapter-level citation and the unnecessary ineffective Siegel input. No new assumption is introduced by the effectivity repair.

## Stronger transfer: exact Gallagher input

The source already archived in this repository is `sources/omega9/montgomery-mnt3.pdf`, with provenance and SHA-256 in `sources/omega9/README.md`:
https://personal.science.psu.edu/rcv4/571s25/Vol3.pdf

Its Theorem 28.19, pp. 229–232, was re-read for this follow-up. It gives exactly (G0)/(G1) in H4_NOT_POLYLOG §5. The exceptional factor `(1−β)log x` multiplies both right-hand-side terms. We use the fixed sufficiently large parameter range justified in POINTWISE_OMEGA9 §1, including its corrections to the draft's parameter-range slip and its separate use of a height-correct Page theorem.

Attribution: P. X. Gallagher, “A large sieve density estimate near σ=1”, *Inventiones Mathematicae* 11 (1970), 329–339. The original paper and its theorem numbering have not been independently checked in this task. Thus the stronger conclusion is explicitly PROVED relative to the exact classical input (G) as stated, as well as to the internally proved energy lemma. This audit does not purport to verify all of the unpublished draft.

Interface: POINTWISE_OMEGA9 Theorem 1.1, with the already proved overlapping-modulus extension POINTWISE_OMEGA11 Lemma 3.1. H4_NOT_POLYLOG Lemma 7b writes out the fibre coefficient bound, conductor support, real-character dichotomy, induced-prime correction and parameter choice. It needs no Type-II-specific arithmetic and no additional divisor bound. The ordinary-PNT proof remains independently available without (G).
