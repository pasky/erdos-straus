# O275 / ASTRA — checkpoint 1

## SHARP:

- **PROVED dictionary:** positive-word endpoint graph is a **forest**, with unique possible parent `−n mod v`; five-slice certificates are its bichromatic Jacobi edges. Increasing paths satisfy ordinary continued-fraction recurrences. `LOWER_TAIL_ASTRA.md` §§2,4.
- **PROVED implication / CONDITIONAL infinite obstruction:** four admissible linear prime forms produce an exactly closed eight-vertex all-residue component. Any fixed finite root set, even with unlimited exploration, fails infinitely often under Dickson (§3).
- **Adaptive repair also fails:** for simultaneous primes `p=2521+9240a`, `(p+11)/12=211+770a`, the least non-residue is **11 and isolated**. This uses only two prime forms; infinitude is CONDITIONAL on Dickson (§5).

These are clean structural results and scoped negative theorems, **not lower-tail positivity or a new infinite ES family**. Only the unique-parent / forest structure appears absent from the repository; the endpoint encoding, sign identity and size bound already occur in SIGN_IDENTITY Lemma 1.1 (prime sign case: CONSTRUCTIVE_ES Prop 4.1(c)); DEDEKIND_ES gives a related Farey-graph view. External novelty was not checked. The obstruction mechanism is the existing n=1 shadow, extended to entire components.

## Work

Read the required current results and both boards. Constructed a primality-sensitive graph/descent strategy instead of another density estimate; tested it, then repaired fixed roots to a canonical moving root (least non-residue), and found an explicit obstruction to that repair. No claim that all canonical-data or growing-root methods fail.

Main file: `LOWER_TAIL_ASTRA.md`.
Memo: `BRAINSTORM/z43_astra_word_forest.md`.
Scripts: `scripts/z43_astra_forest.c`, `scripts/z43_astra_check.py`.

## Checks

- All 78,497 odd primes ≤10^6 and 499 odd squares: distinct AP and SPF-divisor edge enumeration algorithms agree exactly, using the same edge predicate; forest and sign identities pass.
- At 39,175 primes p≡1 (4): 3,028,437 edges, 1,964,805 negative edges; no five-slice failure (known census reproduced).
- Root 1 fails at 285 primes; the least-non-residue component fails at 769. Maximum least mixed-component root is 17 at 196561 (EVIDENCE only).
- Third implementation compares direct residue-parent and divisor enumeration on all odd n≤2000; checks 21,135 reconstructed certificates as exact rational identities; independently checks all squares and eight fixtures for each obstruction family.
- Numerator-8 five-slice controls at 131,241: no hits. The 4-specific sign criterion is not asserted for numerator 8.
- Commands: `cc -O2 -Wall -Wextra -std=c11 scripts/z43_astra_forest.c -o /tmp/z43-astra-forest`; run binary with `1000000`; `PYTHONPATH=scripts uv run python scripts/z43_astra_check.py`. All under 8 GB virtual-memory limit and timeout; single-core. Edge storage ≈101 MB; no large outputs retained.

## Status

Natural checkpoint: one constructive lane plus two repairs completed; ES remains open. Work committed on `side-agent/lower-tail-astra`; not merged. Independent reviewer re-derived every theorem, reproduced both scripts and all statistics, and checked additional fixtures independently: SOUND with attribution/scope clarifications, now applied. See `reviews/lower-tail-astra-self-review.md`. The real-quadratic reduction-cycle lane was not undertaken; this report does not pretend otherwise. Awaiting parent review.

## Sparks

1. Prove a bound for the least mixed-component root using a growing, canonically defined root set; bounded roots are conditionally insufficient.
2. Add the level-sharing incidence relation and determine whether its cycles impose a new arithmetic constraint (not just the known divisor count).
3. Seek an inverse theorem for *simultaneous* monochromatic arithmetic components; a per-component theorem alone cannot overcome the explicit closed trees.
