# AGENT REPORT O270 — board finalists F2 + F1 (EXP_15.md) — checkpoint 1

**ES is not solved. Nothing here is an infinite ES family theorem beyond restatements of existing ones; the new PROVED
items are an obstruction subcase (Thm 2.2) and two small structural lemmas.**

SHARP:
* (S1) **The II-ad u ≡ 3 (mod 8) branch at μ = 0 of 15·2^s + 1 is sterile for every root degree D and every
  factorisation, using only the values at Y = 1** (EXP_15 Thm 2.2). Argon's P₀(Y^{2^r}) argument is not needed and is
  false: Y⁶ + 27 = (Y² + 3)(Y² + 3Y + 3)(Y² − 3Y + 3) (Remark 2.3).
* (S2) The open u ≡ 7 (mod 8) branch (and, by the same computation, II-ac) reduces to **2-adic Diophantine approximation**:
  a solution needs 15u^p − 1 to have a 2^E·a₁² part with 2^E·a₁ ≳ √(15u^p) (for a = 1: u is a very good 2-adic
  approximation of 15^{−1/p}). Ridout (integer approximants, exponent 1 + ε) gives finiteness, ineffectively, for every odd
  p including p = 3 when a₁ ≤ u^{p/2−1−ε}; the large-a₁ part is superelliptic-type. So (C1)–(C2) alone reduce the branch to
  effective Ridout/superelliptic problems (Assessment). (R281 repair, D1/D2.)

## Step 1 (F2) — result
* As posed, F2 conflates the two {2,3}-unit-square boundary points of 2^a3^b + 1. At (0,1) (n = 48X⁴ + 1) the (J)74 window
  identities are identities in X valid for every integer X in a class mod 11, so they hold verbatim for X = 2^t3^{t′} with
  the same Aurifeuillean budget (Lemma 1.1; PROVED, trivial). At (3,0) (n = 8X³ + 1) n itself factors, so the point is
  dissolved by cyclotomic descent to the smaller Pierpont number 2^{a/3}3^{b/3} + 1 (Lemma 1.2; PROVED, elementary).
  Neither a new two-base identity nor a two-base obstruction arises.
* "ES for all 2^a3^b + 1" (a genuine 2D theorem) was attempted by a 2D covering tree (descent + windows + ET/divisor
  classes + general 2D window rules): NOT FOUND. Open density falls (1.5·10⁻³ at L = 120 → 2.9·10⁻⁷ at L = 60480) but
  the open count grows; every open cell is a non-residue mod some admissible prime, so no sterile point was detected
  (EVIDENCE; supply-limited).

## Step 2 (F1 gate) — what is PROVED / CONDITIONAL
* PROVED: Lemma 2.1 (II-ad limit conditions (C1)–(C3), with Capelli: 1 + 4a²d = 15u^p, u ≡ 3 mod 4, p odd prime | D);
  Theorem 2.2 (u ≡ 3 mod 8 sterile ∀D); Lemma 2.2′ (boxed equation: exactly 39 solutions, d ≤ 21, a ≤ 81, m₁ ≤ 36;
  hand bounds + independent exhaustive script; reproduces astra's count; only (1, 11) has 15 | 4a²d + 1, quotient 3).
* REFUTED: argon's round-4 claim that factors of Y^{e2^r} + u^e are P₀(Y^{2^r}).
* OPEN/CONDITIONAL: u ≡ 7 (mod 8) branch of II-ad (2-adic bookkeeping and magnitude reduction PROVED, §2.4), menus II-ac,
  I-ac, II-cd (§2.5). EVIDENCE: no (C1)+(C2) solution for p = 3, u ≤ 2·10⁴ (and smaller ranges up to p = 23); positive
  control recovers the 63·2^s + 1 class exactly.

## Step 3 (F1 construction) — bounded wave, negative so far
* Menu II-d (d constant, a(Y) moving): the identity is unchanged, with a | f′ + 1. Lemma 3.1 (PROVED): for even D, a has no
  real roots (positivity), so linear a is impossible.
* Searches (EVIDENCE): z40_trinom (a linear, quadratic factor, height ≤ 40): 0 valid families for (15,1), D = 3…8 (also 0
  for (3,1), (63,1)); z40_seeded (seeded by the 39 boxed solutions, exact resultants): D = 3 gives 2 rational solutions,
  both degenerate (f ≡ 14 constant, B irreducible: constant-gap, Theorem W) — no genuine II-d configuration (R281 repair, D3).
* 4^s + 297 (μ = 3): not attempted in this checkpoint.
* No forced-budget identity for 15·2^s + 1 found. Per the drop condition the publishable content is §2 (proved subcases)
  + the exact search bounds above.

## Files
EXP_15.md; scripts z40_pierpont_cover.py, z40_tree2d.py, z40_boxed.py, z40_iiad7.py, z40_trinom.py, z40_seeded.py;
BRAINSTORM/z40_pierpont_boundary.md, z40_iiad_branches.md (third memo pending); data/z40 (small logs).

## Sparks (not pursued)
1. Effective version of §2.4: linear forms in 2-adic logarithms (Baker/Yu) for 15u^p − c·2^E = 1 might close the q ≤ 16
   sub-branch for all p.
2. Menu II-d with deg a = 2 without real roots (forced for even D by Lemma 3.1), seeded by the 39 targets.
3. Pierpont: a targeted supply for the open cells (primes with prescribed v₂(ord_q 2), v₂(ord_q 3)) as in
   EXPONENT_COVERING §4.3, instead of uniform lifts.
4. 4^s + 297 at μ = 3 with the II-d menu (the binomial menus are tied to unit squares; II-d is not).
