# z52 L6 — Pointwise divisor-in-class results at one integer

## §0 Summary
- **Genuinely new since 2026-09-28:** Research pending; no verified novelty claim yet.
- **Transferable structural features:** Pending source audit.
- **Campaign verdict change:** None established; ES remains open.

## §1 Verified entries

Access dates below are 2026-10-30. Primary-source excerpts are saved under `sources/z52/divisor_class/`.

1. **H. W. Lenstra, Jr., “Divisors in Residue Classes,” Math. Comp. 42 (165) (1984), 331–340; DOI not listed in consulted source.** Source: author-hosted journal scan (1984), Theorem p. 332. If `0<r<s<n`, `s>n^(1/3)`, and `(r,s)=1`, at most 11 positive divisors of `n` are congruent to `r mod s`, and all can be found in polynomial time. **Status:** published. **Relation:** `BRAINSTORM/s3_lll_lenstra.md`, `BRAINSTORM/bsN_divisor_box.md`, `BRAINSTORM/s6_divisor_pigeonhole.md`; grep also surfaced `EXSET_SHIFT_DIVISORS.md`. It is an upper bound/algorithm, not existence; `s≈N^(1/4)` is outside the theorem.
2. **Don Coppersmith, Nick Howgrave-Graham, S. V. Nagaraj, “Divisors in Residue Classes, Constructively,” Math. Comp. 77 (2008), 531–545; Cryptology ePrint 2004/339 (2004-12-07).** Primary ePrint abstract: reexamines Lenstra’s problem and improves its divisor-count bound while constructing the divisors; its parameter condition and bound are lost in accessible abstract transcription, so I do not quote them. **Status:** published; source abstract accessed. **Relation:** same repo files as entry 1; no existence guarantee.
3. **Kevin Ford, “Integers with a divisor in (y,2y],” arXiv:math/0607473v5 (2013-03-17); published in *Anatomy of Integers*, CRM Proc. Lect. Notes 46 (2008), 65–80.** Abstract / (1.1): `H(x,y,2y) ≍ x/((log y)^δ(log log y)^(3/2))`, `3≤y≤√x`, where `H` counts integers `n≤x` having a divisor in `(y,2y]` and `δ=1−(1+log log 2)/log 2`. **Status:** published. **Relation:** `BRAINSTORM/s6_divisor_pigeonhole.md`, `EXSET_SHIFT_DIVISORS.md`; ambient counting only, no pointwise structured-`N` statement.
4. **Marc Munsch, “On the minimal number of small elements generating prime fields,” arXiv:1703.06673v1 (2017-03-20).** Theorem 3.2 bounds the number of elements ≤`p^(1/(4√e)+ε)` needed to generate `F_p*` by `≪ ω_l(p−1)+(ω(p−1)−ω_l(p−1))/log l`; Corollary 3.7 gives `≪(log_3 p)^2` for almost all `p`. **Status:** preprint. **Relation:** `BRAINSTORM/bsN_divisor_box.md` (group/coset route), `BRAINSTORM/z35_modp_least_residue.md`; pointwise generating-set conclusion, not an arbitrary prescribed residue or a factor of `4Cp+1`.
5. **N. A. Carella, “Upper Bound of the Least Quadratic Nonresidues,” arXiv:2106.00544v9 (2025-10-09).** Theorem 1.1 claims unconditionally `n(p)≪(log p)^(1+ε)`. **Status:** claimed proof with a gap. In §5, (5.4) uses `1/|sin(πuv/p)| ≪ p/(uv)` for all `1≤v<p`; this ignores reduction modulo `p` and fails for `uv>p` (and at `p|uv`). The error estimate and theorem do not follow from the displayed argument. **Relation:** `FRONTIER.md` §3/§4 and `BRAINSTORM/z35_modp_least_residue.md` contain the established pointwise QNR context; no verdict change.
6. **Jonathon Hales, “Divisors in Residue Classes Revisited,” arXiv:2410.05030v1 (2024-10-07).** Abstract: generalizes Lenstra’s algorithm to other Euclidean rings and `Z[x]`; integer algorithm referenced under `s^3>N`. **Status:** preprint. **Relation:** `BRAINSTORM/s3_lll_lenstra.md`, `BRAINSTORM/gon_lll_relation_lattice.md`; algorithmic generalization, not a lower bound or pointwise existence theorem.

## §2 Structural-feature table

| Problem | Solvability feature | Does ES share it? | Transfer verdict |
|---|---|---|---|
| Enumerating divisors in one large-modulus residue class (Lenstra; Coppersmith–Howgrave-Graham–Nagaraj; Hales) | **Algorithmic sparsity:** `s>N^(1/3)` forces at most 11 divisors (Lenstra); Euclidean/lattice structure enumerates them efficiently. | **No:** B2 asks for forcing existence in a prescribed class at one N; enumeration after a suitable large modulus does not force a hit, and the exponent threshold does not reach the target regime. | **known-dead** as an existence transfer; `BRAINSTORM/s3_lll_lenstra.md`, `BRAINSTORM/gon_lll_relation_lattice.md`. |
| Divisor in `(y,2y]` among `n≤x` (Ford) | **Averaging over all integers:** factorization statistics and logarithmic divisor clustering yield an order-of-magnitude population count. | **No:** B6; a positive fraction of ambient integers with such a divisor gives no conclusion for any specific shifted prime or its associated integer. | **known-dead** as direct pointwise transfer; `EXSET_SHIFT_DIVISORS.md`. |
| Small elements generate `F_p*` (Munsch) | **Burgess bound supplies small witnesses against large prime-power obstructions**, then group-theoretic aggregation; the almost-all strengthening additionally uses a prime sieve. | **Partial:** Theorem 3.2 is for each prime p, but its target is generation of the whole group—not a specified class among divisors of a fixed shifted integer. B2’s prescribed-class forcing remains. | **known-dead** as direct transfer; `BRAINSTORM/bsN_divisor_box.md` (group/coset mismatch). |
| Least quadratic nonresidue | Burgess gives a pointwise power-scale bound; GRH gives logarithmic-square scale. Carella’s claimed unconditional polylog bound would matter but has the gap in §1. | **Partial:** QNRs are pointwise character data at one prime, but B2 requires a divisor of a linked, prescribed shifted integer in one class; no implication is known. B2/B6. | **known-dead** for verified results; `FRONTIER.md` §§3–4, `BRAINSTORM/z35_modp_least_residue.md`. The Carella claim is unusable absent a repair. |
| Products of small elements / generators modulo a prime | Burgess bounds find small representatives; combining them handles all prime divisors of the group order. | **Partial:** group generation is a pointwise target, but the prime factors of `4Cp+1` are not freely selectable representatives modulo p, and the target is a particular class/product. B2. | **known-dead** as direct transfer; `BRAINSTORM/bsN_divisor_box.md` already assesses subgroup/coset routes. |

## §3 NEW candidates

(Research pending.)

## §4 Not accessed / could not verify

(Research pending.)
