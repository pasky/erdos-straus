# SEVEN_SIBLING — the sibling numerator 7: what 4/n and 7/n share and what 8/n, 11/n lack (task O215, spark relay Y7)

Builds on FOUR_SPECIFIC (O212), MODEL_SPECIFIC (J)32, CHI_FLIP (J)33, SYNTHESIS_SPARKS3 (J)41, BRAINSTORM/ident_numerators.
Memos `BRAINSTORM/y7_*.md`, scripts `scripts/y7_*`, tiny data `data/y7/`.
**ES is not solved here, nor any infinite case of it; nor is 7/n.** Labels as in DISCOVERIES.md.

Source check (brief item): 7/n has no exception n ≥ 3 up to 10¹³ (Pomerance–Weingartner Table 1, row m = 7: exceptions
{1, 2}, N = 10¹³; sources/pw.txt l. 850–866), independently no failing prime ≤ 10⁸ (MODEL_SPECIFIC census; R212 re-run).

## 0. Iteration log (construction → kill → hypothesis → modification)
(I1) *7-adic (J)33.* Look for a lattice invariant of the path form Q_w deciding S₇(w). Kill: for prime n ≠ 2, 7 the 7-adic
isotropy sign ε₇(Q_w) is identically +1 (CHI_FLIP's ε, not the classical Hasse invariant), and the ℚ-class/genus carry only (χ, (A/n)); worse, S₇ is not even a function of the
ℤ-isometry class (PARI qfisom, 59 mixed classes for n ≤ 150; y7_lattice_invariants Prop Y7.2). Hypothesis used by the idea: "slices are lattice
data". Violated for M ∈ {5, 7, 8, 11} (tested; for prime n ≠ 3, S₃ is all words, a constant class function): slices are marking data. Modification: leave the HJ/lattice frame (I2).
(I2) *The split field ℚ(√−7).* The free slices (e = 1, 2) are exactly the inert primes iff M ∈ {4, 6, 7} (§1). Try the
residue class of π = x + yθ mod q on the split primes. Kill: no detected association for q = 5, 9 (y7_split_norm; finite
residue partitions only, not the archimedean Hecke angle). Hypothesis: the slice
events are factorisation events of p + e, which has no factorisation in ℤ[θ].
(I3) *Mordell levels.* Compare the shape of the identity-hard core. **Find: 7's core is exactly the class of one at
levels 14, 42, 70, 210** (Thm 3.1), while 4's is the square coset. This is the cleanest 4-vs-7 separation of the finite menus (§3). Kill as a mechanism: B1 (class of one never covered;
observed per-prime coverage 2–9 classes for 11 ≤ ℓ ≤ 31, §3.3).
(I4) *Full T1.* O212 called 7 T1-bearing. Only its square-shot subfamily is: Type I/II solutions exist at 41–42 of 42
odd squares (§2). Full T1 holds for all 4 | M (PROVED by reduction to 4) and fails for M = 5, 6, 7, 11 (CERTIFIED). This corrects the framing of spark 1.
(I5) *Luck.* f₇(p) = 1 at 43, 127, 211: consistent with a crude lottery model (§4). (I6) *Order 3:* no detected
association with cubic-residuosity indicators (§5).

## 1. Free slices = inert primes of a class-number-one field (PROVED; y7_free_inert)
A slice with e ∈ {1, 2} fires whenever its N is an integer (a = b = 1). Its classes are p ≡ −1, −2, −2⁻¹ (mod M).
**Prop 1.1.** The non-free unit classes mod M are exactly the kernel of an odd quadratic character mod M iff
M ∈ {4, 6, 7} (for 3 all are free); the characters are χ_{−4}, χ_{−3}, χ_{−7}, i.e. the split primes of ℚ(i), ℚ(√−3)
(not ℚ(√−6); R-O215 D2) and ℚ(√−7). Proof: ≤ 3 free classes force φ(M) ≤ 6, i.e. M ∈ {3,…,10, 12, 14, 18}; check each.
For 7: χ_{−7}(−1) = −1 and χ_{−7}(2) = +1 put −1, −2, −2⁻¹ exactly onto the non-residues {6, 5, 3}. For 11, 2 is inert,
so −2 and −2⁻¹ are squares mod 11 and four inert classes stay hard. Description only (B1).

## 2. 7 does not have full T1 (CERTIFIED / PROVED; y7_full_t1)
ET-shaped Type II (M·abd = n + e, e | a + b) and Type I (M·abd = ne + 1) solutions at odd squares k² ≤ 99²:
4, 8, 12: none. Theorem for every M = 4h: replacing d by hd turns an M-tuple into a 4-tuple, which ET Prop 1.6 excludes at
odd squares (R-O215 D8). 7: Type II at 41/42, Type I at
42/42 (7/9 = 1/2 + 1/4 + 1/36). 11: 36 and 42 of 44. O212 Prop 1.1 is correct, but its T1 lives only on the square-shot
subfamily g | n + MQ² (II-e of §3 with d a perfect square). General II-e is NOT sterile: 7/25 = 1/4 + 1/50 + 1/100 is II-e
with (a, c, d) = (1, 1, 2), g = 13 | 25 + 14 (R-O215 D1). The converse (no full T1 for every 4 ∤ M) has a proof sketch via
POINTWISE_MN Prop 2.1 (reviewer); here it is CERTIFIED for M = 5, 6, 7, 11 only. **Consequence:** a 7/n proof route via Type I/II has no step that must be false at squares;
the B5 barrier that any ES proof must break does not apply to 7. In this barrier sense 7/n is a weaker model of ES (not a
proved logical comparison), and its clean record says nothing about ES's T1 problem.

## 3. The identity-hard core: squares for 4, the class of one for 7 (PROVED + CERTIFIED; y7_mordell_levels)
Families (one free parameter, identities exact; positivity holds for every n ≥ 1 in the class):
II-d n ≡ −e (mod Mab), e | a+b; II-c n ≡ −Ma²d − e (mod Made); II-e n ≡ −Ma²d (mod Macd − 1) [contains the square-shot family as d = □];
I-d n ≡ −e⁻¹ (mod Mab), e | a+b, gcd(e, Mab) = 1; I-c n ≡ −(Ma²d + 1)/e (mod Mad), e | Ma²d + 1. Here Type II means
M/n = 1/(abd) + 1/(acdn) + 1/(bcdn) with Mabd = n + e, a + b = ce; Type I means 1/(abdn) + 1/(acd) + 1/(bcd) with
Mabd = ne + 1, a + b = ce.
**Theorem 3.1.** (a) For every odd n with 7 ∤ n and n ≢ 1 (mod 7), 7/n is a sum of three unit fractions:
n ≡ 6: 7/n = 1/d + 1/(2dn) + 1/(2dn), 7d = n + 1; n ≡ 5: 1/d + 2/(dn) (split as 1/(dn) + 1/(dn)), 7d = n + 2;
n ≡ 3: 1/(dn) + 1/d + 1/d, 7d = 2n + 1; n ≡ 2: 1/(2dn) + 1/d + 1/(2d), 14d = 3n + 1; n ≡ 4: 1/(2d) + 1/(dn) + 1/(2dn),
14d = n + 3 (each a one-line check; n odd makes d an integer in the last two).
(b) n ≡ 2 (mod 3), n odd: 7/n = 1/n + 1/b + 1/(bn), b = (n + 1)/6 (II-e with a = c = d = 1, g = 6).
(c) n odd, n ≡ 1 (mod 7) and n ≡ 4, 3, 2 (mod 5): II-d (a, b, e) = (1, 5, 6), 35d = n + 6, 7/n = 1/(5d) + 1/(dn) + 1/(5dn);
I-c (a, d, e) = (5, 2, 13) and (5, 2, 27) (n ≡ 43, 57 mod 70).
Hence **7/p holds for every odd prime p ≢ 1 (mod 105)** (p = 3, 5, 7 directly; p = 2 fails by size). The uncovered unit
residue set of the menu is exactly {1} at each of the levels 14, 42, 70, 210, and {1, 211, 421, 631} at 840.
CERTIFIED: all n ≤ 3·10⁵ coprime to 7L (composites included) at L = 14 and 210 (uncertified residues exactly {1};
`scripts/y7_cover_verify.py 7 L 300000 all`), and all primes ≤ 10⁶ not dividing 840 at L = 840
(uncertified residues exactly the four above; `scripts/y7_cover_verify.py 7 840 1000000`; the M = 4 run reproduces Mordell's six classes). Novelty not claimed (classical type;
PW sift with the ET Prop 1.9 congruences adapted to m).
**3.2 Comparison** (unit classes uncovered / total, `scripts/y7_mordell_cover.py`):
| L | 840 | 2520 | 9240 | 27720 |
|---|---|---|---|---|
| M = 4 | 6/192 (squares) | 18/576 (squares) | 34/1920 (30 squares + 4) | 96/5760 (90 squares + 6) |
| M = 7 | 4/192 (≡ 1 mod 105) | 10/576 (⊂ 1 mod 210) | 10/1920 | 17/5760 (all ≡ 1 mod 210) |
| M = 8 | 23/192 (6 squares + 17, incl. 11, 17, 131, 241) | 48/576 | | |
| M = 11 | | | 28/1920 (incl. 37) | |
| M = 5 | 2/192 (≡ 1 mod 420) | 2/576 | | |
**Prop 3.2 (property P; finite computation, M ∈ {3, …, 8, 11, 12} tested).** With L_M = lcm(840, M), P(M) := "the
uncovered unit set of the five-family menu at level L_M is empty, or the full unit-square set, or a single fibre
{n ≡ 1 (mod L′)} for some L′ | L_M". It holds for 3 (empty), 4 (squares), 5 (L′ = 420), 7 (L′ = 105) and fails for 6
(11 classes), 8 (squares + 17), 11 (28 classes containing 37) and 12. So P(4) ∧ P(7) ∧ ¬P(8) ∧ ¬P(11) ∧ ¬P(12); among
the tested M, 6 is the only failure-free numerator outside P. P is a **description** of one finite menu at one level,
not an input. Lemma 3.1 (class of one) forces only the residue 1 mod L_M to be uncovered; that 7's survivors at 840 are
exactly the fibre n ≡ 1 (mod 105) is a verified feature of this menu, not a forced set (R-O215 D4).
(Curiosity: 7's core at 840 puts no condition mod 8, all four odd classes survive; 4's core is n ≡ 1 mod 8 and 5's is
n ≡ 1, 5 mod 8. 2 splits in ℚ(√−7). Not pursued.)
**3.3 The core is still a lottery (B1; observed counts + heuristic).** Lifting the core n ≡ 1 (mod 105) to level 840ℓ
covers whole residue classes mod ℓ for only 6, 5, 5, 5, 6, 2, 9 of the ℓ − 1 non-trivial classes (ℓ = 11, 13, 17, 19, 23,
29, 31; `scripts/y7_core_ell.py`, which counts classes covered for every base lift, not covered mass, and only level
840ℓ). For 4 (class 1 mod 840 lifted): 3, 4, 6, 5, 9 (ℓ = 11 … 23). If such counts stay bounded (not proved), a
Haar-CRT product model makes the surviving density of the core decay like a power of log: the B1/B3 polylog lottery
for both numerators (heuristic).
**3.4 What the menu says about a 7-proof (Assessment).** For 4 the menu's core contains the square coset, and an ES proof
via Type I/II must break a step at odd squares (ET Prop 1.6). For 7 the forced part of the core is the class of one, whose
only integer witness is n = 1 (7/1 > 3, a size obstruction). So every fixed finite menu of these families leaves an
arithmetic progression n ≡ 1 (mod L) with infinitely many primes, and a 7/p proof must use information outside such
menus (moving parameters, analytic or arithmetic input); it is not forced to break any step at squares. Near misses:
7/43 and 7/127 have exactly one solution each, and it is the level-70 identity I-c (5, 2, 13) resp. (5, 2, 27); 7/211
(≡ 1 mod 210) has exactly one solution, outside all level-840 families.

## 4. Luck (EVIDENCE + Assessment; y7_near_misses)
Primes 11 ≤ p ≤ X with f = 0 / f = 1 (X = 3·10⁵ for M = 4–7, ≈ 2.2·10⁵ for 8, 3·10⁴ for 9–13): M = 7: none / 43, 127, 211;
8: 4 / 3; 9: 2 / 7; 10: 5 / 9; 11: 1 / 7; 13: 6 / 8. Pooled 18/52 ≈ 0.35, and a crude exchangeable model gives
(34/52)³ ≈ 0.28 for "no zero among 7's three f ≤ 1 primes". For 4, min f = 6 on 11 ≤ p ≤ 3·10⁵. **Answer to goal (c):
7's record is consistent with a crude lottery model; f₇ = 1 at three primes rules out a mechanism giving f₇ ≥ 2, not a
mechanism giving f₇ ≥ 1** (R-O215 D7: the pooled model is not calibrated).

## 5. Order 3 (EVIDENCE, negative; y7_order3)
7's e = 6 slices (p ≡ 1 mod 7) can doubly fail only if p ≡ 1 (mod 21) (PROVED; a necessary congruence, not the failure
set); they do so for 27.8 % of those primes ≤ 10⁶ (4's e = 3 slices: 9.1 %; 7's N are odd). Boolean indicators "2, 3,
7 is a cube mod p": no detected association (8 cells each, within noise; the full three-valued characters were not
tested). The near misses 43, 127, 211 are all such double failures.

## 6. Verdict (Assessment)
* The shared structure of 4 and 7 is real but descriptive: both reduce to the split primes of a class-number-one field
  (§1, also 6 with ℚ(√−3)), and both have a level-840 menu core of the simple shape P (§3). 8, 11, 12 have neither.
* The difference is deeper than the sharing: 4's core contains the square coset (T1), 7's forced core is the class of
  one. In the barrier sense 7/n is a weaker model of ES (no full T1), and its failure-free record is consistent with a
  crude lottery model (§4). An input that is "true for 7 and false for 8, 11" need not be relevant to 4.
* No lattice-invariant analogue of (J)33 exists on 7's length-3 slices (y7_lattice_invariants Prop Y7.2, PROVED by
  example), and the residue class of π mod q = 5, 9 shows no detected association with the hard slices (EVIDENCE).
* Nothing found opens a route to ES or to 7/n.

## 7. Repair log (self-review R-O215, reviews/seven-sibling-review.md; all findings accepted)
D1 II-e ≠ square-shot family (7/25 counterexample); D2 M = 6 ↔ ℚ(√−3); D3 odd primes, n odd in (c); D4 asymptotic and
"must use" claims relabelled heuristic/Assessment, P's 840 core called a menu feature; D5 split-norm sieve bug (n = 1)
and degrees of freedom fixed, scope narrowed to residue partitions; D6 P defined with an empty alternative and level
lcm(840, M); D7 luck conclusion weakened; D8 full T1 for all 4 | M proved by d ↦ hd; D9 order-3 wording; D10 memo
committed, levels separated, 7 ∤ n, S₃ note, Prop numbering, reproducibility of low counts.
