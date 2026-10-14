# R215 — hostile review of O215 (SEVEN_SIBLING.md + BRAINSTORM/y7_*.md)

Reviewer worktree branch `side-agent/review-seven-sibling`, merged `side-agent/seven-sibling` at start.
From-scratch scripts: `scripts/review_r215_thm31.py` (Thm 3.1 symbolic + n ≤ 10⁵), `scripts/review_r215_menu.py`
(own re-derivation of the five one-parameter families and of the level-L covering), `scripts/review_r215_t1.py`
(odd-square Type I/II, PW divisibility sense), further scripts listed per claim.

## Summary verdicts
| claim | verdict |
|---|---|
| Thm 3.1 (a)(b)(c) and "7/p for odd p ≢ 1 (mod 105)" | SOUND |
| "uncovered unit set is exactly {1} at levels 14, 42, 70, 210; {1, 211, 421, 631} at 840" | SOUND (well-posed; see m1 for a sharper/simpler statement) |
| level-L harness (Mordell's six for 4; 8, 11, 5, 6, 12 counts; §3.2 table) | SOUND (all reproduced independently) |
| novelty of Thm 3.1 | not claimed by author; reviewer could not locate the exact 7/n statement in accessible sources (see §1.4) |
| SHARP 2: full T1 for all 4 ∣ M (PROVED), fails for 5, 6, 7, 11 (CERTIFIED) | (pending) |
| SHARP 3: no lattice invariant sees S₇ | (pending) |
| §1 free slices = inert primes for M ∈ {4, 6, 7} | (pending) |
| §4 lottery calibration, §5 order 3 | (pending) |

## 1. Thm 3.1 and the menu (§3)

### 1.1 Identities (re-derived)
All nine identities re-derived by hand and checked symbolically (sympy, with n eliminated through d):
(a) n ≡ 6: (n+1)/(dn) = 7/n; n ≡ 5: (n+2)/(dn); n ≡ 3: (2n+1)/(dn); n ≡ 2: (3n+1)/(2dn), 14 | 3n+1 ⟺ n ≡ 2 (7), n odd;
n ≡ 4: (n+3)/(2dn). (b) (b + n + 1)/(bn) = 7b/(bn) since n + 1 = 6b. (c) (n + 6)/(5dn) = 7/n;
I-c: 70b = en + 1, c = (5 + b)/e, and 7·25·2 + 1 = 351 = 13·27; 70b ≡ 1 (mod e) forces b ≡ −5 (mod e) for e = 13, 27,
so c is an integer for every n in the class (n ≡ 43, 57 mod 70; 43 ≡ 3, 57 ≡ 2 mod 5, both ≡ 1 mod 7).
In menu language: n ≡ 6, 5 are II[d] with (a, b, e) = (1, 1, 1), (1, 1, 2); n ≡ 3 is I[d] (1, 1, 2); n ≡ 2 (mod 7), odd is
I[d] (1, 2, 3) (class −3⁻¹ ≡ 9 mod 14); n ≡ 4 is II[d] (1, 2, 3) (class 11 mod 14); (b) is II[e] (a, c, d) = (1, 1, 1),
g = 6. So every Thm 3.1 identity is in the menu with modulus dividing 14, 42 resp. 70.
**Brute force** (`review_r215_thm31.py 100000`): for every n ≤ 10⁵ in each of the nine classes the parameter is an integer,
all denominators are positive and the sum is exactly 7/n (14 285 + 14 286 + 14 286 + 7 143 + 7 143 + 16 666 + 2 857 + 1 428
+ 1 428 instances, 0 failures). The odd n ≤ 10⁵ with 7 ∤ n left uncovered are exactly n ≡ 1 (mod 7), n ≢ 2 (mod 3),
n ≡ 0, 1 (mod 5) (1906 numbers); those coprime to 105 are all ≡ 1 (mod 105); every odd prime p ≤ 10⁵, p ≢ 1 (mod 105),
p ∉ {3, 5, 7}, is covered (3, 5 are also covered by (a); 7/7 = 1/2 + 1/3 + 1/6).
The logical deduction "odd prime p ≢ 1 (mod 105) ⇒ (a), (b) or (c) applies" is correct: p ≢ 1 (7) → (a) unless p = 7;
p ≡ 1 (7), p ≢ 1 (3) → p ≡ 2 (3) → (b) unless p = 3; p ≡ 1 (7) ≡ 1 (3), p ≢ 1 (5) → (c) unless p = 5.
Note: (a) for n ≡ 6, 5, 3 and (c, first family) need no parity hypothesis; harmless.
**Verdict: SOUND.** Uses repeated denominators (1/(2dn) + 1/(2dn), 1/d + 1/d), which is the standard ES convention
(PW allow (x, y, z) ∈ ℕ³ unrestricted); worth one word in the statement (m2).

### 1.2 "Exactly {1} at levels 14, 42, 70, 210" — is it well-posed?
The menu is defined (memo y7_mordell_levels table; `y7_mordell_cover.py`) as all one-parameter subfamilies
II[d], II[c], II[e], I[d], I[c] whose modulus divides L. I re-derived these as the complete list of
*one-free-variable* linear subfamilies of the two ET/PW-shaped systems (free a or b reduces to free c by b = ce − a and the
a ↔ b symmetry; in Type I a free e is impossible since e(Macd − n) = Ma²d + 1 bounds e). So the menu is well defined.
Exactness then needs two halves, and both are correct:
* upper bound: Thm 3.1's families have moduli 7, 14, 6, 35, 70, so every unit class ≠ 1 mod 14 / 42 / 70 / 210 is covered;
* lower bound: positivity holds for every n ≥ 1 in each class (re-derived: II[c] c = (n + Ma²d + e)/(Made) > 0,
  b = (n + e)/(Mad) > 0; II[e] e = (n + Ma²d)/g > 0; I[c] c = (n + (Ma²d+1)/e)/(Mad) > 0, b = (ne + 1)/(Mad) > 0;
  my script additionally checks exact witnesses at the two smallest lifts of every covered class). Hence a covered
  class 1 mod q would give 7/1 = 7 as a sum of three unit fractions, impossible (≤ 3).
My independent implementation gives exactly [1] at L = 14, 42, 70, 210 and [1, 211, 421, 631] at 840.
**Verdict: SOUND.** The statement at 14…210 is in fact *menu-independent* (true for any menu that contains the nine
Thm 3.1 families and has uniform positivity), whereas the 840 statement is menu-specific (m1).

### 1.3 Harness / table §3.2 (independently recomputed, `review_r215_menu.py`)
| M, L | mine | author |
|---|---|---|
| 4, 840 | 6, exactly {1, 121, 169, 289, 361, 529} = unit squares (Mordell's six) | 6/192 squares ✓ |
| 4, 2520 / 9240 / 27720 | 18 (all 18 squares) / 34 (30 squares + 4) / 96 (90 squares + 6) | ✓ ✓ ✓ |
| 7, 840 / 2520 / 9240 / 27720 | 4 / 10 (all ≡ 1 mod 210) / 10 / 17 (all ≡ 1 mod 210) | ✓ ✓ ✓ ✓ |
| 8, 840 | 23 = 6 squares + 17, contains 11, 17, 131, 241 | ✓ |
| 11, 9240 | 28 (1 square), contains 37 | ✓ |
| 5, 840 | 2: {1, 421} | ✓ |
| 6, 840 / 12, 840 | 11 (1 square) / 44 (6 squares) | ✓ / ✓ |
Prop 3.2 (property P) is therefore correctly computed for the tested M; it is labelled a description, which is right.

### 1.4 Novelty
Author: "Novelty not claimed (classical type)". Agreed and adequate. I searched for a published "7/n for all n ≢ 1
(mod 105)"-type statement and did not find one in accessible sources; the relevant classical literature (Sierpiński 1956
on 5/n; Stewart 1964, 5/n except n ≡ 1 mod 278460; Bernstein 1962, J. reine angew. Math. 211, general m/n; Aigner 1964;
Webb, Vaughan 1970 density results; PW §6 sifting with ET Prop 1.9 congruences "with 4 replaced by m") was not accessible
to me in full text except PW (sources/pw.txt) and ET (sources/elsholtz-tao-1107.1010.pdf). Statements of the Thm 3.1 type
are routine consequences of PW Cor 2.2/2.4 and almost certainly folklore. Recommend keeping "novelty not claimed" and
citing PW Prop 2.1/2.3 as the m-general parametrisation actually used (m3).

## 2. SHARP 2 — full T1 (§2, memo y7_full_t1)

### 2.1 What "Type I/II for numerator M" means
Two notions are in play and the document mixes them:
* **(div)** PW §2 (sources/pw.txt l. 104–110), = ET §1 for M = 4: (x, y, z) is Type I if n | x and n is coprime to y, z;
  Type II if n | y, z and n is coprime to x. f_I, f_II in ET Prop 1.6 count these.
* **(shape)** the parametric "ET-shaped" tuples of §3: Type II Mabd = n + e, a + b = ce; Type I Mabd = ne + 1,
  a + b = ce, with no coprimality. PW Prop 2.1/2.3: every (div) solution comes from a (shape) tuple; the converse needs
  the coprimality side conditions (automatic for prime n, PW Cor 2.2/2.4, but NOT at composite n, in particular not at
  squares).
"Full T1 for M" should mean: no (div) Type I/II solution at any odd square prime to M. The document's counts are (shape)
counts (see 2.3).

### 2.2 4 | M ⇒ full T1 (PROVED) — re-derived
If M = 4h and (a, b, c, d, e) is a (shape) tuple for M, then (a, b, c, hd, e) satisfies 4ab(hd) = n + e resp. ne + 1 and
ce = a + b, i.e. it is an ℕ-point of ET's Σ^II_n resp. Σ^I_n (ET (2.13)–(2.14), (2.1)–(2.2); the remaining coordinate
f = 4ac(hd) − n is positive because e(Macd − n) = Ma²d + 1 in Type I, and analogously in Type II). ET §4 proves
Prop 1.6 by deriving a contradiction from *any* ℕ-point of Σ^I_n at an odd square, using only (2.1), (2.2) and
reciprocity; the Type II case is "almost identical, omitted" in ET (and is PROVED in-repo by POINTWISE_MN Lemma 1.1(d)
per ident_numerators). So the stronger (shape) statement holds, and with it the (div) statement. **SOUND**, with one
citation precision: the reduction needs the ℕ-point version of the ET §4 *proof*, not the statement of Prop 1.6 (which is
about f_I, f_II, i.e. (div) solutions) — m4. Numerically (`/tmp`-variant of `review_r215_t1.py` without the coprimality
filter): 0 (shape) Type I/II tuples at odd squares 9 ≤ k² ≤ 99² for M = 4, 8, 12, 16, 20.

### 2.3 Failure for M = 5, 6, 7, 11 (CERTIFIED) — re-checked, counts need relabelling
The two witnesses are genuine (div) solutions: 7/9 = 1/2 + 1/4 + 1/36 (9 | 36, gcd(9, 2·4) = 1: Type I,
(a, b, c, d, e) = (1, 2, 1, 2, 3), 7·4 = 9·3 + 1) and 7/25 = 1/4 + 1/50 + 1/100 (25 | 50, 100, gcd(25, 4) = 1: Type II,
7·4 = 25 + 3, e = 3 | a + b = 3). So "7 lacks full T1" is **SOUND** in the strict (div) sense.
My independent search (`review_r215_t1.py 99 M`; PW-parametrised search with a-priori bounds x ≤ n/(M−2) resp.
min(y, z) ≤ 2n/(M−1), every hit verified exactly and re-classified by divisibility), odd k ≤ 99, gcd(k, M) = 1, k ≥ 3:
| M | squares | (shape) II / I (= author's table) | (div) II / I |
|---|---|---|---|
| 5 | 39 | 39 / 39 | 37 / 39 |
| 6 | 32 | 30 / 32 | 30 / 32 |
| 7 | 42 | 41 / 42 | **32 / 41** |
| 11 | 44 | 36 / 42 | 35 / 40 |
| 3 | 32 | — | 32 / 32 (e.g. 3/25 = 1/9 + 1/117 + 1/2925, Type I) |
| 19 | 46 | — | 19 / 40 |
The author's numbers reproduce exactly as (shape) counts, but §2 and the memo call them "Type I/II solutions"; at composite
n a (shape) tuple need not be a Type I/II solution (e.g. for 7 only 32 of the 41 Type II hits are (div) Type II). MINOR
(m5): relabel as "ET-shaped tuples" or report the (div) counts. Conclusion unaffected.

### 2.4 How DISCOVERIES (J)46 must be corrected
(J)46 bullet 2 says "**7 is a T1-bearing numerator with no failure** … Among M ≤ 30000 (PW §6), the T1-bearing
failure-free numerators are 3, 4 and 7." Here "T1-bearing" silently meant FOUR_SPECIFIC Prop 1.1 (the *odd square-shot
family* g | n + MQ², g ≡ −1 mod M odd, is sterile at odd squares iff M ≡ 0, 3 mod 4). Required correction:
> "7 is *shot*-T1-bearing (Prop 1.1: its odd square-shot family is sterile at odd squares) but 7/n itself has **no T1**:
> genuine Type I and Type II solutions exist at odd squares (7/9 = 1/2 + 1/4 + 1/36 Type I; 7/25 = 1/4 + 1/50 + 1/100
> Type II; (div) Type I at 41, Type II at 32 of the 42 odd squares 3 ≤ k ≤ 99, 7 ∤ k). Full T1 (no Type I/II solution
> at any odd square) holds for every 4 | M (ET §4 via d ↦ hd) and fails for M = 3, 5, 6, 7, 11, 19 (certified). Among
> the failure-free numerators the shot-T1-bearing ones are 3, 4, 7, but the only one with full T1 is 4."
Also the headline "7 is the failure-free sibling of 4" should not suggest a shared T1; SEVEN_SIBLING §2/§6 say this
correctly. (Caveat for the editor: the "M ≤ 30000" range relies on PW §6, which excepts m = 19 from its Thm 1.2 check;
FOUR_SPECIFIC covers M ≤ 24 by census, so 19 is handled there, not by PW.)

## 3. SHARP 3 — no lattice invariant of Q_w sees S₇ (memo y7_lattice_invariants, Prop Y7.2)
Definitions checked against MODEL_SPECIFIC §3: word (t, u, v), tuv − u − v = n, A = tu − 1, A* = tv − 1; S_M: M divides
one of A, A*, t, u, v; Q_w = Gram [[v, −1, 0], [−1, t, −1], [0, −1, u]], det n.
**The n = 5 example, re-verified from scratch** (`scripts/review_r215_isom.py`, own short-vector isometry search):
(1, 2, 7): 14 − 9 = 5, 7 | v, so ∈ S₇; (2, 1, 6): 12 − 7 = 5, A = 1, A* = 11, none of 1, 11, 2, 1, 6 divisible by 7, so
∉ S₇. U = [[−1, 0, 0], [−3, 0, 1], [−2, 1, 0]] (det ±1) satisfies Uᵀ G(1,2,7) U = G(2,1,6) exactly. **Isometric: confirmed.**
Independent census (my greedy isometry classes, all words of primes n ≤ 40): mixed classes M = 4: 0; 5: 14; 7: 14; 8: 6;
11: 7. Same qualitative picture as the author's PARI census (n ≤ 150). (Nit: for M = 7 there is a smaller example at
n = 3: (2, 1, 4) ∈ S₇ (A* = 7) and (1, 2, 5) ∉ S₇, isometric; the memo's "smallest example n = 5" is not literally the
smallest — m6.) The 7-adic remark (L_w ⊗ ℤ₇ unimodular of rank 3 ⇒ isotropic, so ε₇ ≡ +1 when 7 ∤ n) is standard and
correct. **Verdict: SOUND**, with the scope exactly as the memo states it (unmarked ℤ-isometry class of the length-3
path form). The SEVEN_SIBLING §6 bullet "No lattice-invariant analogue of (J)33 exists on 7's length-3 slices" is
fine; a headline "no lattice invariant sees S₇" would overclaim, because S₇ is trivially a function of the *marked*
form (it is divisibility of the Gram entries v, t, u and the two adjacent 2×2 minors A, A*) — m7.

## 4. §1 free slices = inert primes (Prop 1.1)
Re-derived: the e ∈ {1, 2} slices with a = b = 1 are II[d] (1,1,1), (1,1,2) and I[d] (1,1,2), classes −1, −2, −2⁻¹
(the last two only for odd M). A set of ≤ 3 classes is a coset of an index-2 subgroup only if φ(M) ≤ 6; checking all
M ≤ 60 by brute force (`scripts/review_r215_misc.py`): the non-free units form an index-2 subgroup not containing −1
exactly for M ∈ {4, 6, 7}, and the free classes are {3} mod 4, {5} mod 6, {3, 5, 6} mod 7 = residues of the primes inert
in ℚ(i), ℚ(√−3), ℚ(√−7) (class number one). The M = 11 remark (four non-residues {2, 6, 7, 8} stay non-free) is right.
**Verdict: SOUND** (a description; the label "PROVED" is fine; "inert primes of a class-number-one field" is decoration:
class number plays no role in the proof — m8).

## 5. §4 lottery calibration (goal (c))
* Near misses re-verified: f₇(p) ≤ 1 for 11 ≤ p ≤ 1500 exactly at 43, 127, 211 (own Python divisor counter, unordered
  x ≤ y ≤ z); the three single solutions 7/43 = 1/10 + 1/16 + 1/3440, 7/127 = 1/20 + 1/196 + 1/62230,
  7/211 = 1/32 + 1/520 + 1/438880 check exactly; 7/43, 7/127 are I-c (5, 2, 13), (5, 2, 27) (b = 8, 49; c = 1, 2). The
  author's C engine (`ms_census.c`, compiled by me) to 3·10⁵ gives the same f ≤ 1 list (run status in §8).
  f₈ = 0 at 11, 17, 131, 241 confirmed.
* **Defect (m9): "For 4, min f = 6 on 11 ≤ p ≤ 3·10⁵" is false.** f₄(13) = 4 (1/4 + 1/18 + 1/468, 1/4 + 1/20 + 1/130,
  1/4 + 1/26 + 1/52, 1/5 + 1/10 + 1/130 — complete list, own brute force) and f₄(17) = 4; ms_census agrees
  (`ms_census 4 11 c 300000`: the only p with f₄ ≤ 6 are 13, 17 (f = 4) and 193 (f = 6)). The memo's second clause
  "no f ≤ 5 on 100 < p ≤ 3·10⁵" is correct. Repair: "min f₄ = 4 (p = 13, 17); no f₄ ≤ 5 on 100 < p ≤ 3·10⁵". This does
  not change the reading (4's small-p counts are still larger than 7's 1s).
* The pooled number 18/52 and (34/52)³ ≈ 0.280 recompute from the memo's table. The model is labelled crude/uncalibrated
  and the conclusion is weakened accordingly; acceptable as Assessment. Two further caveats the text should carry
  (m10): (i) M = 12 (whose PW exception list is long: 5, 7, 13, 25, 29, …) is omitted from the pool without comment;
  including it would only lower P(no zero), i.e. make 7's record look luckier — say so; (ii) 7 was *selected* as the
  failure-free sibling, so any probability of "no zero" computed after the fact is not a test, only a consistency check.
  The logical conclusion "f₇ = 1 at three primes rules out a mechanism giving f₇ ≥ 2, not f₇ ≥ 1" is correct.

## 6. §5 order 3
Re-derived: for p ≡ 1 (mod 7) both e = 6 slices have N_II = (p + 6)/7, N_I = (6p + 1)/7 odd; with ab | N and odd a, b,
the slice fires iff some a, b with a + b ≡ 0 (mod 3), which (for 3 ∤ N) happens iff N has a prime factor ≡ 2 (mod 3).
If p ≡ 2 (mod 3) then N_II ≡ 2 (mod 3) fires; p = 3 is not ≡ 1 (mod 7); so double failure ⇒ p ≡ 1 (mod 21). PROVED,
correct (also brute-checked for all p ≤ 10⁶). Rates recomputed from scratch with sympy factorisation: M = 4, p ≡ 1 (12):
1771/19564 = 9.05 %; M = 7, p ≡ 1 (21): 1817/6530 = 27.83 % — **exact match**. I did not re-run the 8-cell cube-indicator
split; the author's "no detected association" (EVIDENCE, Boolean indicators only, explicitly not the full cubic
characters) is appropriately weak. **Verdict: SOUND as labelled.**
