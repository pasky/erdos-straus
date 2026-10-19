# R289 — independent hostile review #2 (round 1)

Author revision reviewed: `5e418734`, `paper/es-threequarter-note.tex` (C2). Reviewer branch: `side-agent/review-threequarter-2`. No author files changed; no access to reviewer #1's report or branch. This report is being built claim by claim.

## Cold referee summary

The argument fixes a family of Type II congruences modulo `kℓ`, with multipliers `k ≤ X^κ`, large primes `√X < ℓ ≤ X`, and reduced pairs `H < u,v ≤ x^(1/6)` satisfying `4uv | kℓ+1`. The large lower cutoff makes the classes modulo a given `ℓ` distinct even across different multipliers. Revealing the entire small-modulus residue `c mod L_K` therefore turns the hit count into a sum of independent Bernoulli variables, not independent individual atoms.

The analytic core is a uniform-in-`c` supply estimate. A lattice calculation supplies mass `t² Σ φ(k)/k²`. Brun–Titchmarsh gives its upper bound. The lower bound uses Bombieri–Vinogradov and Cauchy–Schwarz with a weighted second incidence moment; Shiu bounds the latter after replacing two multiplier conditions by one condition modulo their least common multiple. This avoids multiplying a BV error bound by the maximum incidence multiplicity.

Nonunit fibres can have small supply. Conditioning on avoidance of primes up to `y = B t³` makes severe loss of multiplier mass exponentially rare, by an exponential-moment estimate on `Σ_{p|c,p>y} 1/p`. The resulting conditional void probability is `exp(-c t³)`. The same fibre decomposition gives factorial moment bounds with a base independent of the moment order. An even Bonferroni polynomial of degree `O(t³)`, multiplied by the exact small-prime selector, is a nonnegative majorant with small CRT mean. Expanding it into actual congruence classes costs `exp(O(t⁴))` coefficients. Integer counting then costs at most one per coefficient, without ever splitting the interval into fibres modulo `L_K`. Choosing `t` proportional to `(log N)^(1/4)` yields the prime exceptional-set saving. Rankin's trick transfers this to all integers because an exceptional integer can only have exceptional prime factors.

The logical route is reconstructible from the note alone. In particular, the enormous conditioning modulus is not itself an integer-counting cost. The issue to test is uniform supply, not a supposed requirement that `L_K ≤ N`.

## Scope and evidence

This is an independent mathematical audit, not external refereeing or a claim that ES is solved. Numerical tests below will be finite sanity checks, not validation of asymptotic analytic estimates. Source-access limitations will be stated explicitly.

## Claim-by-claim verdicts (in progress)

- Sections 1–2, identity and conditional independence: pending detailed checks.
- Sections 3–4, analytic inputs and uniform cubic supply: pending.
- Sections 5–6, moments and conditioned void: pending.
- Section 7, Bonferroni and coefficient ledger: pending.
- Section 8, primes and Rankin transfer: pending.
- Section 9 and introductory comparison/cap remarks: pending.

## Numbered defects

None entered yet; this is not a final clean bill of health.
