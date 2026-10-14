# AGENT_REPORT_O215 — Spark relay Y7: the sibling numerator 7 (branch side-agent/seven-sibling)

Deliverables: `SEVEN_SIBLING.md` (deep file), 7 memos (all committed) `BRAINSTORM/y7_*.md` (indexed), scripts `scripts/y7_*`
(all ≤ a few minutes; the level-27720 covering run ≈ 30 min). ES is not solved; neither is 7/n; no infinite case of ES claimed.

## SHARP:
1. **The identity-hard core of 7/n is exactly the class of one; for 4/n it is the square coset** (SEVEN_SIBLING Thm 3.1,
   PROVED with explicit families, CERTIFIED on all n ≤ 3·10⁵ and on primes ≤ 10⁶). 7/n holds for every odd n ≢ 0, 1 (mod 7)
   by five level-14 identities, for n ≡ 2 (mod 3) by 7/n = 1/n + 1/b + 1/(bn), b = (n+1)/6, and for n ≢ 1 (mod 5) by three
   level-70 families. So **7/p holds for every odd prime p ≢ 1 (mod 105)**. At levels 14, 42, 70, 210 the menu's survivor set is exactly
   the residue 1, i.e. only what ident_numerators Lemma 3.1 forces; at 840 it is the fibre n ≡ 1 (mod 105) (a feature of the
   menu, not forced). At level 840 the same harness reproduces Mordell's six square
   classes for 4, finds the squares plus 17 more classes (containing the failures 11, 17, 131, 241) for 8, and for 11 at 9240
   finds 28 classes containing 37. The near misses 7/43 and 7/127 have exactly one solution each, and it is the level-70
   identity. Novelty not claimed (classical covering type).
2. **7 does not have full T1** (y7_full_t1). ET-shaped Type I/II solutions exist at 41–42 of 42 odd squares
   (7/9 = 1/2 + 1/4 + 1/36). Only the square-shot subfamily g | n + 7Q² is sterile (O212 Prop 1.1); the wider II-e family
   is not (7/25 = 1/4 + 1/50 + 1/100). Full T1 holds for every 4 | M (PROVED: d ↦ hd reduces to 4) and fails for
   M = 5, 6, 7, 11 (CERTIFIED). This corrects the framing of O212 spark 1. In the barrier sense 7/n is a weaker model of
   ES: no Type I/II route for 7 has to break a step at squares. Its only "T1 control" is n = 1, which is a size obstruction.
3. **No lattice invariant sees S₇** (y7_lattice_invariants, PROVED by example with PARI qfisom). For M = 5, 7, 8, 11 the
   slice membership is not a function of the ℤ-isometry class of the path form (n = 5: (1,2,7) ∈ S₇, (2,1,6) ∉ S₇,
   isometric forms). For M = 4 it is a genus function. So a 7-adic (J)33 on the HJ slices cannot exist: it is marking data.

## Results by goal
(a) No lattice-invariant analogue of (J)33 on 7's length-3 slices (SHARP 3); residue classes of π mod 5, 9 on split primes
show no association (narrow test). The true 7-specific structures: free slices = inert primes of ℚ(√−7); this exactness
holds exactly for M ∈ {4, 6, 7} (fields ℚ(i), ℚ(√−3), ℚ(√−7); PROVED, description), and the class-of-one core (SHARP 1).
(b) Comparative table: SEVEN_SIBLING §1–3 and y7_free_inert. Property P ("menu core at level lcm(840, M) is empty, the
full square set, or a fibre n ≡ 1 mod L′") holds for 3, 4, 5, 7 and fails for 6, 8, 11, 12 (tested M only). It is a description (B1), not an input. No input-type
property was found that is true for 7 and false for 8, 11.
(c) Lottery: f₇(p) = 1 at 43, 127, 211. P(f = 0 | f ≤ 1) ≈ 0.35 pooled over the siblings; a crude exchangeable model gives
≈ 0.28 for 7's record. Consistent with luck; it rules out a mechanism giving f₇ ≥ 2, not one giving f₇ ≥ 1. 4 has larger
small-p counts (min f₄ = 6 on 11 ≤ p ≤ 3·10⁵).
(d) Order 3: 7's e = 6 slices can doubly fail only at p ≡ 1 (21), and do so for 27.8 % of them (≤ 10⁶). Boolean
cube-residuosity indicators of 2, 3, 7 show no detected association (full cubic characters not tested). The near misses 43, 127, 211 are such double failures.

## Labels / caveats for the reviewer
* Thm 3.1: identities are one-line checks; "classes covered" is an exhaustive finite enumeration
  (`y7_mordell_cover.py`), cross-checked by exact Fraction certificates (`y7_cover_verify.py`). Positivity for every n in the
  class is argued per family in y7_mordell_levels.
* Full T1 for 4 | M is PROVED by reduction to 4 (ET Prop 1.6); its failure for 4 ∤ M is CERTIFIED for 5, 6, 7, 11 only.
* The luck estimate pools M = 8–11, 13 and ignores the p- and M-dependence: a calibration, not a fit.
* y7_split_norm: the extension of Lemma 3.1 to polynomial-parameter families in (x, y) is open (Assessment).
* §3.3 "bounded per-prime coverage ⇒ polylog decay" is a heuristic, not a theorem.
* §3.3 per-ℓ coverage counts are finite computations at level 840ℓ only (no larger levels).

## Sparks (not pursued)
1. **7 as an H-A test bed without T1.** For 7 the only barrier left for growing-modulus Type I/II routes is the class of one
   (plus B2/B3). A moving-modulus mechanism for primes with p − 1 highly divisible would be a clean B1-escape test that cannot
   be a disguised T1-violation.
2. **2-adic blindness of 7's core.** At level 840 the core n ≡ 1 (mod 105) keeps all four odd classes mod 8 (4: only 1 mod 8;
   5: 1, 5 mod 8). Is this "2 splits in ℚ(√−7)"? Test M = 15, 23 (also χ(2) = +1).
3. **Which primes are "identity-sharp"?** For both 4 and 7 the core is the forced set exactly at the primes 3, 5, 7 (and 8
   for 4), with only ≈ 6 classes per prime ℓ ≥ 11. Is there a uniform reason (family count vs ℓ − 2 or (ℓ − 1)/2 classes)
   that makes 7 the last sharp prime?
4. Lemma 3.1 for polynomial families in norm-form variables (y7_split_norm): prove that every ET-shaped identity in
   (x, y) with n = N(x + yθ) also misses the class of one.

## Self-review R-O215 (deep reviewer, reviews/seven-sibling-review.md): changes required, all 10 findings accepted and repaired
MAJOR: D1 (II-e ≠ square-shot family; 7/25 counterexample), D2 (M = 6 ↔ ℚ(√−3), exact character test), D4 (asymptotics and
"a 7-proof must…" relabelled heuristic/Assessment; the 840 core is a menu feature), D7 (luck conclusion weakened).
MINOR: D3 (odd primes; n odd in Thm 3.1(c)), D5 (split-norm sieve counted 1 as prime; dof), D6 (P definition), D8 (full T1
for all 4 | M proved), D9 (order-3 wording), D10 (memo committed, levels separated, S₃ note, reproducible commands).
The reviewer verified every identity of Thm 3.1, the positivity of all five family types, the covering tables, the
square-search counts and the qfisom counterexample.
