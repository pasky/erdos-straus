# AGENT_REPORT_O169 — Dedekind sums, HJ continued fractions and ES certificates (checkpoint 1)

Main file: `DEDEKIND_ES.md`. Scripts: `scripts/dk_*`. ES is not solved, and neither is any infinite case of it.

## Results
1. **Dictionary (PROVED, Lemma 1.1).** The X-slice certificates `tuv − u − v = n` (t,u,v ≥ 2) are exactly the
   fractions with HJ continued fraction `n/A = [[v,t,u]]` of length 3, with `A = tu − 1`, `A* = tv − 1`.
   Equivalently they are the matrices `T^vST^tST^uS` with top-left entry n. On these points the Hirzebruch–Zagier
   formula gives `12 s(A,n) = t+u+v−9 + (A+A*)/n`. (D3) is the general identity `r − r' = −12 s(A,n) − 1 + (A+A*)/n`,
   so Dedekind sums determine the *difference* of the HJ lengths of A and n−A, not the length.
2. **T1 via Rademacher (PROVED, Prop 3.1).** Rademacher's mod-8 congruence combined with (D2) forces the Jacobi
   symbol `(A/n) = −1` on the 4|A and 4|t slices when n ≡ 1 (4). Since `(A/m²) = 1` for every A, these slices are
   empty at squares.
3. **Theorem 4.5 (PROVED: a finite cell check mod 8 relative to classical (R) and (D2); brute force to 10⁶).** For
   n ≡ 1 (4), a length-3 HJ fraction is an ES certificate of one of five slices (4 | tu−1, tv−1, t, u, v; the last
   two are a Type II e-slice that I identified) **iff `(A/n) = −1`**. In HJ coordinates the moving moduli disappear
   completely. Cor 4.6: for p ≡ 1 (8), these slices hold ⟺ `λ(p) ≤ 3`, where λ(p) is the least HJ length
   (Farey left-turn distance from ∞) of a quadratic non-residue. That makes ES a "least non-residue in the Farey
   metric" problem.
4. **EVIDENCE.** λ(p) ≤ 3 (in fact an interior r = 3 hit exists) for all 19 552 primes p ≡ 1 (8) ≤ 10⁶, and no odd
   square ≤ 10⁶ has a hit. Over all non-square n ≡ 1 (4) ≤ 2·10⁵ (composite n included), the two interior slices
   both vanish at only 22 n, the largest 28225. **CONJECTURE:** the Jacobi symbol is the only obstruction for
   n > 28225.
5. **Negative findings.**
   - Dedekind data mod any fixed modulus is genus data (C1), so Prop S kills it.
   - The real value of s(A,p) only gives r − r'. The missing r + r' satisfies no reciprocity law, and its exact sums
     are shifted convolutions (C2, H-A).
   - The Smith-palindrome mechanism yields nothing on L₃ (C3).
   - The Hecke–Knopp family reduces to H-A (C4).
   - No size-literal parity law among 820 sub-counts (C5).
   - In thin-group terms, ES sits at critical exponent 2δ = 1 (B3).

Honest bottom line: what is new is the dictionary, i.e. the exactly characterised T1 obstruction (Jacobi = −1 ⟺
certificate on the length-3 locus). I found no reciprocity-forced existence mechanism.

## Sparks (not pursued)
* **Zagier-reduced cycles.** `γ = T^vST^tST^uS` is hyperbolic with trace p − t. Its Zagier (minus-CF) reduced cycle
  is the cyclic word (v,t,u), and cyclic rotations give certificates for the *other* numerators `K(t,u,v)`,
  `K(u,v,t)`. Look for a mechanism on cycles of length 3 in discriminant `(p−t)² − 4`, comparing with WR §5.2.
* **The 40 "+1 cells"** (non-ES length-3 points). Is there a bijection or transfer between +1 and −1 cells
  across different n (for example rotations, or n ↦ n + u − t), which would turn "L₃(p) ⊄ QR" into a counting
  identity with a sign?
* **Composite vanishing-set conjecture (4.4).** Prove `a₀ + a_T > 0` for non-square n with a prime factor
  ≡ 3 (4) by explicit construction. This would at least show that the Jacobi obstruction is exact on that part.
* **Knot-surgery reading (5.2).** The short-plumbing lens spaces with QR slope may be Berge-type surgeries, which
  would give a possible structural reason why QR length-3 points are "special". This is speculative.
* **λ(p) statistics.** Compare `P(λ(p) > 3)` with the independent-coin heuristic `2^{−|L₃(p)|/2}` (reversal pairs
  share their Jacobi symbol). Do the Jacobi values on L₃(p) show any correlation beyond the cell structure?

# Checkpoint 2 (parent follow-up; DEDEKIND_ES.md Part II, §§8–10)

1. **Sign transfer.**
   - The sign is a mod-4 function (PROVED, §8.1). It is +1 exactly on `(t,u,v) ≡ (1,2,3), (1,3,2), (2,1,2),
     (2,2,1), (3,1,1) mod 4`, and these are the only classes occupied at squares.
   - Three candidate maps preserve the sign (PROVED, §8.2): the Klein group (reversal, duality), and rotations
     `(v,t,u) ↦ (t,u,v)` whenever n, n' ≡ 1 (4). Rotation is conjugation of γ, so the sign is a conjugacy-type
     invariant.
   - **One genuine sign-flipping transfer exists: scaling** (PROVED, §8.3).
     `K(av', t, au') = a·K(v', at, u')` keeps A, and `(A/am) = (−1/a)(A/m)`. A +1 word of m with a | middle
     becomes a certificate for am whenever a ≡ 3 (4). It needs composite n, so it is useless at primes.
   - Signed sum S(n) = N₊ − N₋: no closed form. It is a ±1-weighted (★)-type family; the exact facts are only
     "N₋ even" and "N₋(m²) = 0".
2. **Composites.**
   - EVIDENCE (`dk_vanish5.py 1000000`): among all non-square n ≡ 1 (4) ≤ 10⁶, the five slices plus the boundary
     case vanish **only at n = 105**.
   - This gives **CONJECTURE SQ₅**: for n ≡ 1 (4), n ≠ 105, λ(n) ≤ 3 ⟺ n is not a square. It strengthens O146's
     SQ on n ≡ 1 (4), and implies ES for p ≡ 1 (4).
   - The composite case with a factor a ≡ 3 (4) reduces (PROVED lemma, §9.2) to a divisor of m+1 that is
     ≡ −1 (mod a). This gives the explicit family `n = a(at−2)`, and the inherited certificates cover 79 % of
     such n ≤ 2·10⁵.
   - **Not proved in general**: the factor supplies the sign but never the length-3 word (B2).
3. **Complexity (§10.1).**
   - Cor 4.6 is the exact converse of T4 on the five slices.
   - Full ES has no algorithmic consequence. The polylog-height version (t_min ≤ (log p)^C) would give
     deterministic QNR-finding with a factoring oracle, which is not currently known (literature from memory).
   - EVIDENCE: t_min(p) ≤ 64 for all p ≡ 1 (8) ≤ 10⁶.
4. **Coin statistics (§10.2).** At primes ≈ 70 % of words are −1 (15 of 20 mod-4 classes); the biased-coin model
   predicts < 1 failure to 3·10⁵, and 0 are observed. At squares all words are +1.

Sparks: (a) identify the sign as an explicit genus character of the conjugacy class of γ (disc (n−t)²−4), which
could make rotation-invariance conceptual; (b) the scaling transfer combined with a "descent" n ↦ n/a might give
SQ₅ for composites, conditionally on SQ₅ for smaller m with a | middle; (c) test SQ₅ beyond 10⁶ (the 10⁶ runs take minutes
in pure Python; a C port would reach 10⁸).
