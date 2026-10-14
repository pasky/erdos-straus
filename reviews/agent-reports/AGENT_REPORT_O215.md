# AGENT_REPORT_O215 — Spark relay Y7: the sibling numerator 7 (branch side-agent/seven-sibling)

Deliverables: `SEVEN_SIBLING.md` (deep file), 7 memos `BRAINSTORM/y7_*.md` (indexed), scripts `scripts/y7_*`
(all ≤ a few minutes; the level-27720 covering run ≈ 30 min). ES is not solved; neither is 7/n; no infinite case of ES claimed.

## SHARP:
1. **The identity-hard core of 7/n is exactly the class of one; for 4/n it is the square coset** (SEVEN_SIBLING Thm 3.1,
   PROVED with explicit families, CERTIFIED on all n ≤ 3·10⁵ and on primes ≤ 10⁶). 7/n holds for every odd n ≢ 0, 1 (mod 7)
   by five level-14 identities, for n ≡ 2 (mod 3) by 7/n = 1/n + 1/b + 1/(bn), b = (n+1)/6, and for n ≢ 1 (mod 5) by three
   level-70 families. So **7/p holds for every prime p ≢ 1 (mod 105)**. The core is the ident_numerators Lemma 3.1
   obstruction and nothing else, at levels 14, 42, 70, 210. At level 840 the same harness reproduces Mordell's six square
   classes for 4, finds the squares plus 17 more classes (containing the failures 11, 17, 131, 241) for 8, and for 11 at 9240
   finds 28 classes containing 37. The near misses 7/43 and 7/127 have exactly one solution each, and it is the level-70
   identity. Novelty not claimed (classical covering type).
2. **7 does not have full T1** (y7_full_t1). ET-shaped Type I/II solutions exist at 41–42 of 42 odd squares
   (7/9 = 1/2 + 1/4 + 1/36). Only the shot subfamily is sterile (O212 Prop 1.1). Full T1 ⟺ 4 | M (theorem for Type II;
   evidence for Type I at M = 8, 12). This corrects the framing of O212 spark 1. 7/n is a strictly weaker model of ES:
   no 7-proof has to break a step at squares. Its only "T1 control" is n = 1, which is a size obstruction.
3. **No lattice invariant sees S₇** (y7_lattice_invariants, PROVED by example with PARI qfisom). For M = 5, 7, 8, 11 the
   slice membership is not a function of the ℤ-isometry class of the path form (n = 5: (1,2,7) ∈ S₇, (2,1,6) ∉ S₇,
   isometric forms). For M = 4 it is a genus function. So a 7-adic (J)33 on the HJ slices cannot exist: it is marking data.

## Results by goal
(a) No 7-adic / ℚ(√−7) analogue of (J)33 on length-3 slices: SHARP 3, plus a Hecke-angle test on split primes (none). The
true 7-specific structures: free slices = inert primes of ℚ(√−7), exactly for M ∈ {4, 6, 7} (PROVED, description), and the
class-of-one core (SHARP 1).
(b) Comparative table: SEVEN_SIBLING §1–3 and y7_free_inert. Property P ("level-840 core is the full square coset or a
class of one") holds for 3, 4, 5, 7 and fails for 6, 8, 11, 12. It is a description (B1), not an input. No input-type
property was found that is true for 7 and false for 8, 11.
(c) Lottery: f₇(p) = 1 at 43, 127, 211. P(f = 0 | f ≤ 1) ≈ 0.35 pooled over the siblings, so 7's record is ≈ 1-in-4 luck. 4 needs
less (min f₄ = 6 on p ≥ 11).
(d) Order 3: 7's e = 6 slices can doubly fail only at p ≡ 1 (21), and do so for 27.8 % of them (≤ 10⁶). Cubic characters of
2, 3, 7 show no correlation. The near misses 43, 127, 211 are such double failures.

## Labels / caveats for the reviewer
* Thm 3.1: identities are one-line checks; "classes covered" is an exhaustive finite enumeration
  (`y7_mordell_cover.py`), cross-checked by exact Fraction certificates (`y7_cover_verify.py`). Positivity for every n in the
  class is argued per family in y7_mordell_levels.
* Full T1 for Type I at 8, 12 is EVIDENCE (k ≤ 99, e ≤ 200). The Type II zero rows rely on POINTWISE_MN Lemma 1.1(d).
* The luck estimate pools M = 8–11, 13 and ignores the p- and M-dependence: a calibration, not a fit.
* y7_split_norm: the extension of Lemma 3.1 to polynomial-parameter families in (x, y) is open (Assessment).
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
