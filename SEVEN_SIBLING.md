# SEVEN_SIBLING — the sibling numerator 7: what 4/n and 7/n share and what 8/n, 11/n lack (task O215, spark relay Y7)

Builds on FOUR_SPECIFIC (O212), MODEL_SPECIFIC (J)32, CHI_FLIP (J)33, SYNTHESIS_SPARKS3 (J)41, BRAINSTORM/ident_numerators.
Memos `BRAINSTORM/y7_*.md`, scripts `scripts/y7_*`, tiny data `data/y7/`.
**ES is not solved here, nor any infinite case of it; nor is 7/n.** Labels as in DISCOVERIES.md.

Source check (brief item): 7/n has no exception n ≥ 3 up to 10¹³ (Pomerance–Weingartner Table 1, row m = 7: exceptions
{1, 2}, N = 10¹³; sources/pw.txt l. 850–866), independently no failing prime ≤ 10⁸ (MODEL_SPECIFIC census; R212 re-run).

## 0. Iteration log (construction → kill → hypothesis → modification)
(I1) *7-adic (J)33.* Look for a lattice invariant of the path form Q_w deciding S₇(w). Kill: for n ∤ 14 the 7-adic
Hasse invariant is identically 1, and the ℚ-class/genus carry only (χ, (A/n)); worse, S₇ is not even a function of the
ℤ-isometry class (PARI qfisom, 59 mixed classes for n ≤ 150; Prop 2.1). Hypothesis used by the idea: "slices are lattice
data". Violated for every M ≠ 4: slices are marking data. Modification: leave the HJ/lattice frame (I2).
(I2) *The split field ℚ(√−7).* The free slices (e = 1, 2) are exactly the inert primes iff M ∈ {4, 6, 7} (§1). Try a
Hecke-angle input on the split primes. Kill: no angle effect (y7_split_norm, χ² at noise level). Hypothesis: the slice
events are factorisation events of p + e, which has no factorisation in ℤ[θ].
(I3) *Mordell levels.* Compare the shape of the identity-hard core. **Find: 7's core is exactly the class of one at
levels 14, 42, 70, 210** (Thm 3.1), while 4's is the square coset. This is the cleanest 4-vs-7 separation and it also
says what *kind* of input a 7-proof needs (§3). Kill as a mechanism: B1 (class of one never covered; per-prime coverage
≈ 6/ℓ beyond 7, §3.3).
(I4) *Full T1.* O212 called 7 T1-bearing. Only its shot subfamily is: Type I/II solutions exist at 41–42 of 42 odd
squares (§2). Full T1 ⟺ 4 | M (evidence; theorem for Type II). This corrects the framing of spark 1.
(I5) *Luck.* f₇(p) = 1 at 43, 127, 211: lottery (§4). (I6) *Order 3:* no cubic-residue pattern (§5).

## 1. Free slices = inert primes (PROVED; y7_free_inert)
A slice with e ∈ {1, 2} fires whenever its N is an integer (a = b = 1). Its classes are p ≡ −1, −2, −2⁻¹ (mod M).
**Prop 1.1.** The non-free classes mod M are exactly the primes split in ℚ(√−M) iff M ∈ {4, 6, 7} (for 3 all are free).
For 7: χ_{−7}(−1) = −1 and χ_{−7}(2) = +1 put −1, −2, −2⁻¹ exactly onto the non-residues {6, 5, 3}. For 11, 2 is inert,
so −2 and −2⁻¹ are squares mod 11 and four inert classes stay hard. Description only (B1).

## 2. 7 does not have full T1 (CERTIFIED / PROVED; y7_full_t1)
ET-shaped Type II (M·abd = n + e, e | a + b) and Type I (M·abd = ne + 1) solutions at odd squares k² ≤ 99²:
4, 8, 12: none (theorem: ET Prop 1.6; POINTWISE_MN Lemma 1.1(d) for Type II, 4 | M). 7: Type II at 41/42, Type I at
42/42 (7/9 = 1/2 + 1/4 + 1/36). 11: 36 and 42 of 44. O212 Prop 1.1 is correct, but its T1 lives only on the shot
subfamily (II-e of §3). **Consequence:** a 7/n proof route via Type I/II has no step that must be false at squares;
the B5 barrier that any ES proof must break does not apply to 7. 7/n is therefore a strictly weaker model of ES, and
its clean record cannot be read as evidence about ES's T1 problem.

## 3. The identity-hard core: squares for 4, the class of one for 7 (PROVED + CERTIFIED; y7_mordell_levels)
Families (one free parameter, identities exact; positivity holds for every n ≥ 1 in the class):
II-d n ≡ −e (mod Mab), e | a+b; II-c n ≡ −Ma²d − e (mod Made); II-e n ≡ −Ma²d (mod Macd − 1) [shot family];
I-d n ≡ −e⁻¹ (mod Mab), e | a+b; I-c n ≡ −(Ma²d + 1)/e (mod Mad), e | Ma²d + 1. Here Type II means
M/n = 1/(abd) + 1/(acdn) + 1/(bcdn) with Mabd = n + e, a + b = ce; Type I means 1/(abdn) + 1/(acd) + 1/(bcd) with
Mabd = ne + 1, a + b = ce.
**Theorem 3.1.** (a) For every odd n with 7 ∤ n and n ≢ 1 (mod 7), 7/n is a sum of three unit fractions:
n ≡ 6: 7/n = 1/d + 1/(2dn) + 1/(2dn), 7d = n + 1; n ≡ 5: 1/d + 2/(dn) (split as 1/(dn) + 1/(dn)), 7d = n + 2;
n ≡ 3: 1/(dn) + 1/d + 1/d, 7d = 2n + 1; n ≡ 2: 1/(2dn) + 1/d + 1/(2d), 14d = 3n + 1; n ≡ 4: 1/(2d) + 1/(dn) + 1/(2dn),
14d = n + 3 (each a one-line check; n odd makes d an integer in the last two).
(b) n ≡ 2 (mod 3), n odd: 7/n = 1/n + 1/b + 1/(bn), b = (n + 1)/6 (II-e with a = c = d = 1, g = 6).
(c) n ≡ 1 (mod 7) and n ≡ 4, 3, 2 (mod 5): II-d (a, b, e) = (1, 5, 6), 35d = n + 6, 7/n = 1/(5d) + 1/(dn) + 1/(5dn);
I-c (a, d, e) = (5, 2, 13) and (5, 2, 27) (n ≡ 43, 57 mod 70).
Hence **7/p holds for every prime p ≢ 1 (mod 105)**, and the identity-hard core of 7 at levels 14, 42, 70, 210 is
exactly the class of one (one unit class each). CERTIFIED: all n ≤ 3·10⁵ coprime to the level (composites included),
and all primes ≤ 10⁶ at level 840, get exact certificates; the uncertified residues are exactly {1}
(`scripts/y7_cover_verify.py`; the M = 4 run reproduces Mordell's six classes). Novelty not claimed (classical type;
PW sift with the ET Prop 1.9 congruences adapted to m).
**3.2 Comparison** (unit classes uncovered / total, `scripts/y7_mordell_cover.py`):
| L | 840 | 2520 | 9240 | 27720 |
|---|---|---|---|---|
| M = 4 | 6/192 (squares) | 18/576 (squares) | 34/1920 (30 squares + 4) | 96/5760 (90 squares + 6) |
| M = 7 | 4/192 (≡ 1 mod 105) | 10/576 (⊂ 1 mod 210) | 10/1920 | 17/5760 (all ≡ 1 mod 210) |
| M = 8 | 23/192 (6 squares + 17, incl. 11, 17, 131, 241) | 48/576 | | |
| M = 11 | | | 28/1920 (incl. 37) | |
| M = 5 | 2/192 (≡ 1 mod 420) | 2/576 | | |
**Prop 3.2 (property P; finite computation).** P(M) := "the identity core at level 840 (for 11: 9240) is either the full
unit-square coset, or a class of one {n ≡ 1 (mod L′)} for a sublevel L′ | 840". It holds for 3 (∅), 4 (squares), 5
(L′ = 420), 7 (L′ = 105) and fails for 6, 8 (squares + 17), 11 (28 classes containing 37, not of that form) and 12. So
P(4) ∧ P(7) ∧ ¬P(8) ∧ ¬P(11) ∧ ¬P(12); 6 is the only failure-free numerator outside P. P is a **description** (a finite
covering at one level), not an input. (Curiosity: 7's core puts no condition mod 8, all four odd classes survive;
4's core is n ≡ 1 mod 8 and 5's is n ≡ 1, 5 mod 8. 2 splits in ℚ(√−7). Not pursued.)
**3.3 The core is still a lottery (B1).** Per prime ℓ beyond 7, lifting the core n ≡ 1 (mod 105) to level 840ℓ covers whole
residue classes mod ℓ for only 6, 5, 5, 5, 6, 2, 9 of the ℓ − 1 non-trivial classes (ℓ = 11 … 31; `scripts/y7_core_ell.py`).
For 4 (class 1 mod 840 lifted): 3, 4, 6, 5, 9 (ℓ = 11 … 23). Both are O(1) per prime, so the Haar-CRT survival of the core
decays like a power of log, the B1/B3 polylog lottery for both numerators.
**3.4 What a 7-proof must do.** For 4 the core is fixed by a quadratic obstruction (T1) and an ES proof must break a
step at odd squares. For 7 the core is the class of one, whose only integer witness is n = 1 (7/1 > 3: an archimedean
size obstruction). So a 7/p proof must handle primes with p − 1 divisible by every small prime, using size/positivity
and nothing else (cf. y2_positivity_is_T1: T1 = positivity for 4). The near misses confirm it: 7/43 and 7/127 have exactly one
solution each, and it is the level-70 identity I-c (5, 2, 13) resp. (5, 2, 27); 7/211 (≡ 1 mod 210) has one solution off
all level-840 families.

## 4. Luck (EVIDENCE + Assessment; y7_near_misses)
Primes p ≥ 11 with f = 0 / f = 1: M = 7: none / 43, 127, 211; 8: 4 / 3; 9: 2 / 7; 10: 5 / 9; 11: 1 / 7; 13: 6 / 8.
P(f = 0 | f ≤ 1) ≈ 0.35 pooled, so 7's record has probability ≈ 0.65³ ≈ 0.27 given its near misses. 4 has min f = 6 on
p ≥ 11, so it needs less luck than 7. **Answer to goal (c): 7 is lottery-lucky; f₇ = 1 rules out a positive-margin mechanism.**

## 5. Order 3 (EVIDENCE, negative; y7_order3)
7's e = 6 slices (p ≡ 1 mod 7) can doubly fail only at p ≡ 1 (mod 21) (PROVED); they do so for 27.8 % of those primes
≤ 10⁶ (4's e = 3 slices: 9.1 %; 7's N are odd). Cubic characters of 2, 3, 7 mod p: no correlation (8 cells each, within
noise). The near misses 43, 127, 211 are all such double failures.

## 6. Verdict (Assessment)
* The shared structure of 4 and 7 is real but descriptive: both reduce to split primes of their class-number-one field
  (§1), and both have an identity core equal to a PROVED-forced set at level 840 (§3). 8, 11, 12 have neither.
* The difference is deeper than the sharing: 4's core is quadratic (T1), 7's is the class of one. 7/n is a weaker model
  of ES (no full T1), and its failure-free record is consistent with luck (§4). An input that is "true for 7 and false for
  8, 11" need not be relevant to 4 at all.
* No 7-adic or ℚ(√−7) analogue of (J)33 exists on the length-3 slices: no lattice invariant sees S₇ (Prop 2.1 of
  y7_lattice_invariants, PROVED by example), and the Hecke angle does not see the hard slices (EVIDENCE).
* Nothing found opens a route to ES or to 7/n.
