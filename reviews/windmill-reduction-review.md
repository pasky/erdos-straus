# R164 — hostile review of O164 `WINDMILL_REDUCTION.md` (§1–§10)

Reviewer branch `side-agent/review-windmill-reduction`; merged `side-agent/windmill-reduction` at review start.
From-scratch scripts: `scripts/review_wr_*.py` (none of the author's `wr_*` code reused).
**ES is not solved; nothing in O164 claims otherwise.**

## Summary verdicts

| item | verdict |
|---|---|
| §1 Computation 1.2 + dictionary | SOUND (re-certified independently to 20000; see D1, D2 minor) |

(table extended below as the review proceeds)

## §1 — Zagier windmill ↔ rivers

**Independent check** (`scripts/review_wr_zagier.py lo hi`). h⁺(p) is computed *without* the river map R: Gauss-reduced
indefinite forms of disc p, cycles of the standard ρ-operator (Buchmann normalisation), canonical cycle representative.
Then: ζσ-cycles on X(p) are enumerated, each cycle's forms `[y,x,−z]` are reduced to a class; checked that (a) each cycle is
contained in one class, (b) cycles ↔ classes is a bijection, (c) `#cycles = h⁺(p)`, (d) `2·|cycle| = ` R-period of the river
(R as defined in the doc, implemented separately), (e) ζ maps the cycle of C onto the cycle of `[a,−b,c]` = C⁻¹ and is
self-paired iff C is principal; ζ is verified to be an involution of X(p).
Result: **0 failures for all 1125 primes p ≡ 1 (4), p < 20000** (author: p ≤ 1300). p = 1297 reproduces
h⁺ = 11 and cycle lengths `[11,11,11,11,13,13,17,17,21,21,37]` (doc writes `[11,…,37]`, consistent). Class numbers
h(229)=3, h(257)=3, h(401)=5, h(577)=7 agree with tables.

The "Reading" paragraph: `σρσ = σζ = ρ⁻¹` and `ζρζ = σζ = ρ⁻¹` verified by hand. Fixed points: ζ fixes exactly
`x = y` (middle piece), giving `(1,1,(p−1)/4)` ↦ principal form; σ fixes `y = z` ↦ `[a,b,−a]`. Correct.
Genus theory: disc p prime ⇒ one genus, 2-rank 0, h⁺ odd, principal class the only ambiguous one. Correct.

Verdict: **SOUND**, with two minor presentation defects (D1, D2).

## Defects (numbered; FATAL / MAJOR / MINOR)

**D1 (MINOR, §1 "Reading", line "The principal cycle has odd length L_1/2 (because |X(p)| = Σ_C L_C/2 …)").**
The oddness of `|X(p)|` is itself obtained from ζ having a unique fixed point — i.e. Zagier's argument. So the sentence
"Zagier's proof is the statement *the principal river has odd half-period*" is a *reformulation*, not an independent
proof route: in the doc the odd half-period is derived from Zagier, not vice versa. Repair: say explicitly that the
odd half-period is equivalent to (and here deduced from) the ζ-fixed-point count; an independent proof is Smith's /
Legendre's continuant-palindrome argument (cite where it shows the principal period is odd for p prime ≡ 1 (4)).

**D2 (MINOR, §1 Computation 1.2 / "Reading" label).** The Reading is "PROVED given 1.2's structure", but 1.2 (i)–(iii) is
only CERTIFIED for p ≤ 1300 (now p < 20000 by R164). As written, the general dictionary is CONDITIONAL on a statement
proved nowhere in the doc. It is in fact a known theorem (folklore; e.g. the literature on "Zagier's one-sentence proof
and reduction of binary quadratic forms"); either give a reference or a proof sketch (each ζσ step is a composite of
R-steps, by Observation 1.1, and covers exactly two R-steps), or relabel the general statement CONDITIONAL/folklore.
