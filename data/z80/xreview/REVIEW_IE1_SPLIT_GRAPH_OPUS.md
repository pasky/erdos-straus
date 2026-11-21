<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="1129194ee">
A separate reviewer subagent was asked to review the changes in `git log 1129194ee..`. Its request and review follow.

Request: review changes since 1129194ee carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review, scope new §14 quadratic-modulus cofactor path theorem in notes/z80/IE1_SPLIT.md. Verify every claim at π=P²−8J² and every x_j, simultaneous tower properties / squareclass independence and optional character, distinguish external-finite failures, standard length bounds, and coded internal paths; check original P one/two-step edge cases; flag fixes and give commit + verdict. No edits/computation needed.

Commit log:
commit 94440a1cdcb920c3f072d2b15d7248cd7f7a40ac
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 19:41:14 2026 +0100

    Exhibit a forced infinite positive cofactor path at a second prime in the window model

 notes/z80/IE1_SPLIT.md | 20 +++++++++++++++++---
 1 file changed, 17 insertions(+), 3 deletions(-)

Review:
**Verdict on 94440a1cd: ACCEPT WITH MINOR FIXES.** I re-derived every claim at π and at each x_j by hand and found no mathematical error. The fixes below are about missing steps, wording, and how much the result is worth. I made no edits.

## What checks out

**The prime π = P² − 8J²**
- **It is a quadratic prime in K[X].** Its roots satisfy P = ±2√2·J, and 2 is not a square in K (PA 2-adic parity).
- **Positive, ≡1 mod 8, and ≡1 mod d for every d∈D⁺.** This follows from P odd, P ≡ 1 (d), d | J and X > C₀.
- **Its content is 1.** It equals 1 + J(2X + JX² − 8J), so its residue is 1 at every ℓ | J (X stays integral). At ℓ ∤ J the leading coefficient J² is a unit.
- **It stays prime.** The invariants that keep old horizontal primes prime cover it, and R/πR = A/πA as in §10.
- **The base fibre is K(√2),** because (P/(2J))² ≡ 2.
- **K(√2) stays relatively algebraically closed in the fibre.** Row fibres are lines even when one coefficient vanishes, sphere fibres are rank-four quadrics (cones included), and lines and floors are free. So squareclasses inject into R/πR.

**Squareclasses at π**
- 1 and 2 are squares.
- 3 is not a square in K(√2): (a+b√2)² = 3 forces a² = 3 or b² = 3/2, both excluded by v₃.
- No negative scalar is a square, since K(√2) is formally real.
- So 3 is the least positive nonsquare. The classes of −1 and 3 are independent, and the external character is fine: extend a functional on the countable 𝔽₂-space; it sends 2 to +1 and every x_j to −1.

**Each x_j = π − 3J²/2^j**
- **Well defined:** J²/2^j ∈ B because v₂J is nonstandard.
- **Odd, increasing, inside (3, π):** checked directly.
- **Quadratic prime:** it needs 8 + 3/2^j to be a nonsquare. That holds by odd 2-adic order for odd j, and by 2^{j+3} + 3 ≡ 3 (mod 4) for even j.
- **Content 1:** same argument as for π.
- **The chain identity holds:** π + x_j = 2π − 3J²/2^j = 2x_{j+1}.
- **Only one way forward:** the positive divisors of 2x_{j+1} are 1, 2, x_{j+1}, 2x_{j+1}. Of these, 1 and 2 are squares and 2x_{j+1} = π + x_j > π. So x_{j+1} is the unique out-neighbour, the same holds on the external-character graph, and induction on path length gives reachable set {x_j}, with 3 not in it.

**The original-P cases**
- **One step:** every odd vertex x has 2 | P + x, and 2 is a nonsquare vertex.
- **Two steps:** for even x, P + x is odd. If it is composite, both factors are odd, at least 3, and at most (P + x)/3 < P. One of them is a nonsquare because their product is ≡ x. Then x → e → 2.
- **No out-arrow:** if P + x is prime, its divisors are 1 (a square) and P + x (> P).
- **x = 2:** 3 | P + 2 and 3 is a nonsquare (§10), so Thm A's "if and only if" survives.
- The conditional length-≤2 lemma is trivially correct; "whenever x is a vertex" is redundant there.

**The logic paragraph** is correct. It separates three readings of "x reaches 3":
- a path of a fixed standard length (first order; refuted);
- a path of some externally finite length (a countable semantic disjunction; false here);
- an internally coded path of possibly nonstandard length (not refuted). The internal halving orbit continues to nonstandard j, and T has no canonical sequence coding anyway.

## Fixes

1. **Missing step (substance).** "Thus x_j ≡ −3J²/2^j is nonsquare" needs J²/2^j to be a square in K(√2). It is (J/2^{j/2})² for even j and 2·(J/2^{(j+1)/2})² for odd j. So the class of x_j is the class of −3, which is what "nonsquare" relies on. Add this sentence.

2. **Overweighting (substance).** "No fixed standard bound … can be proved from T" is true but carries little T-specific content. Each fixed-length statement is expected to be false in ℕ as well. The same chain in ℕ — p ≡ 17 (24) prime, every x_j = p − 3·2^{L−j}·n prime, with n a product of small primes dividing p − 1 to rule out local obstructions — is a one-variable prime-tuples instance, so it exists conditionally on Dickson.
   - Say that the bounded variants are plausibly false in ℕ.
   - Say that the real gain is an *unconditional* failure of the externally-finite reading with 2 a square.
   - Replace "Dirichlet prime tuples" with "Dickson/Schinzel prime tuples". Dirichlet is the one-progression theorem.

3. **Sharpen the diagnosis (substance and form).**
   - State explicitly that x₀ is odd and π + x₀ is composite. Both of Thm A's sufficient conditions hold, so this is a direct external failure of its "if" direction.
   - The chain is exactly Thm A's first-return halving map x ↦ (p + x)/2^{ν₂(p+x)}, which never returns. So the step that fails is the "permutation cycle on odd representatives" step (finiteness of the 2-orbit), not the covering step.
   - That is more accurate than "explains precisely why the finite-field return argument … cannot simply be read".

4. **Wording.**
   - "completed fibre" should be "directed-union fibre"; no completion is used.
   - "this ordered coefficient field" should be "formally real field". The residue field is not ordered by R, although the conclusion holds for every ordering.
   - "this is where *all later* row and sphere edges are checked" is unclear. Cite the "old horizontal primes stay prime" invariant (§2 factor calculus, §4, §9.1).
   - The §14 heading ("the model's exceptional modulus") is now stale.

5. **§0 block.**
   - The Scope line still says nothing about §14. Add something like: "§14: external-finite and fixed-length cofactor reachability fails at π = P² − 8J² in the §9 model; coded paths are not addressed; ES at π is not asserted."
   - Triage METHOD-CX and "cross-review owed" are correct.
   - At export a FRONTIER §6 line is owed. `git grep IE1_SPLIT` finds no reference in any master file, so the whole note is still awaiting export, not just §14.

These fixes do not touch the theorem's statement or proof structure.
</code-review>
