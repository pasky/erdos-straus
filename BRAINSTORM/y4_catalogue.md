# y4_catalogue — what is true for numerator 4 and false for 8 (and 7, 11, 12, …)? Input or description? (O212, goal (a))

## Idea
List structural facts (not counts) that distinguish 4. For each, decide: **INPUT** (implies existence at a single n,
at least on a slice) vs **DESCRIPTION** (re-labels the solution set or explains a known covering).

**New Prop 1 (PROVED, elementary).** 4 is the unique M ≥ 3 such that every prime p ∤ M has a Type I or Type II slice
with e ∈ {1, 3}. (Type II slices need e ≡ −p, Type I slices e ≡ −p⁻¹ (mod M).) *Proof.* At most the three unit classes
−1, −3, −3⁻¹ are covered, so φ(M) ≤ 3, hence M ∈ {3, 4, 6}. For M = 3, 6, e = 3 is not a unit, and p ≡ 1 is missed. For M = 4:
p ≡ 3 has e = 1, and p ≡ 1 has e = 3 (both types). ∎ (Brute-force check M < 200: `scripts/y4_slice3.py`.)
Meaning: (ℤ/e)^* = {±1} exactly for e ∈ {1, 2, 3, 4, 6}. (R-O212 repair: with all five such e allowed, a {±1}-slice exists
at every prime exactly for M ∈ {3, 4, 5, 7} (check M < 200), so the {±1} reading is NOT 4-specific; only the literal
e ∈ {1, 3} statement is.) On an e ≤ 3 slice the event −1 ∈ Σ_e(N) is just
"Σ_e(N) ≠ {1}". For e = 3 that is: N has a prime factor ≡ 2 (mod 3), a non-triviality event and not a
"hit −1 in a big group" event. For p ≡ 1 (mod 12), ES has TWO such slices, N_II = (p+3)/4 and N_I = (3p+1)/4 (both ≡ 1
mod 3). Both are empty for 9.1% of p ≡ 1 (mod 12) below 10⁶ (1771/19564; 10.7% below 10⁴: decay ≈ c/log p), first at
241, 409, 769. So the slices are strong but not deterministic.
EVIDENCE that the failures of other numerators avoid such slices: of all census failures (M = 5–24; e = 1 is the
trivial two-term class), only M = 10 (4 of 7), 16 (4/37) and 22 (9/53) have failures in an e = 3 class, all with N
having only primes ≡ 1 (mod 3) (e.g. 10/67: N = 7). M = 20 has 0 of 62 failures in its two e = 3 classes (2/8 of the units;
(6/8)⁶² ≈ 2·10⁻⁸ under independence, which the slice structure itself violates: Assessment only).

## Catalogue
| fact (4 vs 8) | status | input or description |
|---|---|---|
| (J)32 S₄ = {χ = −1} on length-3 words; S₈ ⊊ | PROVED | **input candidate** (SQ₅ ⇒ ES on the slices); numerator-free |
| (J)33 χ = −ε₂(Q_w): certificate ⟺ ℚ₂-isotropic | PROVED | same input as above, in local form; BM-only for β in Ω₂ is equivalent to SQ₅ |
| one-odd half f₄^{odd} (d odd), no 8-analogue | PROVED split; EVIDENCE ≥ 1 to 10⁸ | **description** (y4_oneodd_slices: no ℤ₂-invariant, composite exceptions 321, …) |
| slice parity = v₂(slot) (2 ↔ one-odd, ≥ 3 ↔ 8/n) | PROVED (y4_oneodd_slices) | description: S₄ = S₄^{odd} ∪ S₈, 140/240 cells each |
| e ∈ {1, 3} slice at every p (Prop 1) | PROVED, unique to 4 (literal e ∈ {1, 3}) | no: congruence (B1); e = 3 slices fail ~9%; {±1} reading shared by 3, 5, 7 |
| (ℤ/4)^* = {±1}: the two-term class p ≡ −1 is the whole non-T1 class mod 4 | PROVED (trivial) | description (for 3 as well) |
| Mordell 840 = reach of universal one-slot χ-witnesses {2, 3, 5, 7, 8, 15, 20} | PROVED (y4_mordell_witness) | description of B1's ceiling |
| U₄(840) = the 6 square classes; U₈(840) has 29 non-square classes | CERTIFIED (MODEL_SPECIFIC §4.1) | description (B1); not tight at 9240 either |
| T1 in the shot family | PROVED for all M ≡ 0, 3 (4) (y4_t1_numerators) | **not 4-specific** (3, 7, 8, 11, …) |
| the norm N ε_μ of absolute value 4tj − 1, Ptolemy/pentagon relations ((J)38–(J)39) | PROVED | uniform: 4 enters as Mtj − 1 |
| Type I alone never fails | EVIDENCE (4: ≤ 10⁸; 7: ≤ 10⁶; 8: only at the true failures) | not a discriminator (also robust for 7 and 8) |

## Literature
MODEL_SPECIFIC (O197) §§2–6; CHI_FLIP (O198); FIXED_MODULUS_SHOTS; ET (Elsholtz–Tao) §2 for the e-slice
parametrisation; Landau: the integers with all prime factors ≡ 1 (mod 3) have density ≍ 1/√log x.

## Barrier screen
Prop 1 is a congruence statement (B1): it tells which slice exists, not that it fires. The e = 3 event "N has a prime
factor ≡ 2 (mod 3)" fails on a set of relative density ≍ 1/√log N per slice (Landau), and for two slices about 1/log
(observed 9%). B6: averages say nothing pointwise. T1: at p = k² the e = 3 slices are not slices (p is not prime), so no
conflict. Harness: 4-specific (unique M), so not killed by numerator-blindness.

## Cheap numerics
`scripts/y4_slice3.py` (< 1 min): failure placement, the uniqueness check M < 200, and the both-e = 3-empty frequency.

## Assessment
Most 4-specific facts are DESCRIPTIONS. The only one with input character is the χ-fibre ((J)32/(J)33, i.e. SQ₅). Prop 1
is a literal uniqueness statement for e ∈ {1, 3}, B1/B2 when used as an input. Its {±1}-unit-group reading is shared by
M = 3, 5, 7 (R-O212), so it does not distinguish 4. Curiosity: the failure-free numerators ≤ 10⁸ are 3–7, and among them only 6
lacks a {±1}-slice at every prime.
