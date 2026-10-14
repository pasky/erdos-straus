# TRANSPORT_LAW — the ES sign as "the character of 2 at a small cluster variable" (task O213, spark relay Y5)

Status: checkpoint 1 (O213). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on FRIEZE_ES (O210, with the R208 repairs merged), LENGTH_THREE, CHI_FLIP, MODEL_SPECIFIC, SIGN_IDENTITY.
Memos BRAINSTORM/y5_* (8), scripts scripts/y5_*, logs logs/y5_*.

Notation: word (c, m, s), N = cms − c − s odd, h = cm − 1, h′ = ms − 1, pentagon (h′, c, m, s, h). The even edge is
{e, e′} and o is the opposite vertex.

## 0. Iteration log (construction first; barrier as steering wheel)

| # | construction | barrier hypothesis it tried to violate | outcome |
|---|---|---|---|
| I1 | (2/o) at small o as a "Burgess-free" sign | sign must be read at a modulus ≍ N | killed: (2/o) is o mod 8 = the slice condition itself (§1) |
| I2 | choose o in a fixed progression (Dirichlet in the o-aspect, O210 spark 2) | B2 "modulus is part of the solution" | exists in P_h: the factorisation moves to the small o + 1, N enters by a congruence mod o. Density τ(o+1)/o, not 1/2: B1 for bounded o, H-A for growing o (§2) |
| I3 | swap which vertex is o (5 positions) | fixed finite slice sets | one relation sh = N + c in all positions; the parity pattern decides which number carries the divisor event (§2) |
| I4 | second-order 2-adic data (mod 16/32) | "congruence-only data" | no extra obstruction at squares: T1 is one bit (EVIDENCE; §4) |
| I5 | longer polygons (r ≥ 4) | fixed r = 3 | general-r law: the sign is one Hasse invariant for every r, and only r = 3 has a character-fibre zero locus (§3) |
| I6 | signed friezes + archimedean correction | positivity (O210 §3) | the ∞-factor is a Maslov count. Signed factorisations sit in the +1 class, certificates in the −1 class = complex conjugation (§3.2) |
| I7 | Siegel–Weil with the sign at ∞ | B6 (averages) | full-rank Siegel–Weil is the genus indicator; path bases are p^{−2/3}-thin (§5) |
| I8 | one position alone (the N-free one) | "needs all five slices" | SQ_H (m even, 8 ∣ m·e) holds at all primes ≡ 1 (8) ≤ 10⁷. A sub-lottery (§6) |

## 1. The transport law is the Ptolemy relation mod 8 (PROVED; memo y5_transport_is_ptolemy)

The relation through the even edge reads ee′ ∈ {1 + o, N + o, 1 + No}:
* {c, m}, {m, s}: ee′ = 1 + o;
* {h′, c}, {s, h}: ee′ = N + o;
* {h, h′}: ee′ = 1 + No.

Hence 4 | ee′ ⟹ o ≡ −N^ε (4), and 8 | ee′ ⟺ o ≡ −N^ε (8). With FRIEZE Thm 1.2 this gives
(h′/N) = −(−1/N)(2/o)(2/N)^ε, which is O210's law, including the (2/N) factor.

**For N ≡ 1 (8): every word has o ≡ 3 (4), and certificate ⟺ o ≡ 7 (8).** "The character of 2 at o" is therefore the
residue of o mod 8, i.e. the 2-adic depth of the even edge read through one Ptolemy relation. It carries no arithmetic
of N. CERTIFIED: 784 732 words, odd N ≤ 2·10⁴, all classes mod 8 (`y5_ptolemy_check.py`).

## 2. Free o: the five positions and where B2 re-enters (PROVED; memo y5_five_positions)

All words are the single relation sh = N + c with h = cm − 1. The parity of (c, m) fixes the position:

| parity | even edge | o | factorisation event | N enters via |
|---|---|---|---|---|
| c, m even | {c, m} | h | cm = o + 1 (N-free) | o ∣ N + c |
| c odd, m even | {m, s} | h′ | ms = o + 1 (N-free) | o ∣ N + s |
| c, m odd, s even | {s, h} | c | sh = N + o (Type II) | divisor of N + o, ≡ −1 (mod o) |
| c even, m odd | {h′, c} | s | h′c = N + o (mirror) | same |
| c, m, s odd | {h, h′} | m | hh′ = 1 + oN (Type I) | divisor of 1 + oN, ≡ −1 (mod o) |

* **Answer to O210 spark 2.**
  * The family with o in a progression independent of N exists. It is P_h: o ≡ 7 (8), and the condition on N is
    N mod o ∈ C(o) = {−c : c ∣ o + 1, c and (o+1)/c even}.
  * C(o) lies in the Jacobi non-residues mod o, because (N/o) = (h/N) = (h′/N).
  * Its density is |C(o)|/o ≤ τ(o+1)/o, not 1/2. The "(2/o) = +1" half is automatic, and what remains is the thin
    divisor image −D(o+1).
  * Bounded o gives a finite congruence covering, killed by B1. By (J)26 Thm 3.1, no finite set of ET classes covers
    the large primes ≡ 1 (24) with prescribed least QNR r (r ≥ r₀). So assuming the P_h classes are ET Prop 1.9 classes
    (they are polynomial families N = o·s − c; identification at the level of an Assessment), there is no bound
    o_h*(p) ≤ f(n_p).
  * Growing o is H-A.
* **T1** shows up as one Jacobi symbol in every position. In P_h it is (N/o) = −1, which is impossible at N = n²
  because gcd(n, o) = 1. So no position escapes T1, as required by B5.
* Census (memo y5_ocensus_hard_primes; EVIDENCE, p ≡ 1 (8) ≤ 10⁷):
  * o* = 7 for 94 %;
  * max o* = 2431 = 11·13·17 at **p = 21841 = 1 + 2⁴·3·5·7·13**, which has a single interior certificate pair,
    (9, 64, 38) and its mirror;
  * the other hard primes are all ≡ 1 (120).
  * o* is a divisor-event statistic, not a residue-symbol one. Only P_h is QNR-shaped.

## 3. The general-r law and the archimedean factor (PROVED; memo y5_general_r_jacobi)

**Thm 3.1.** For every integer word with N = K_r > 0 odd and all leading continuants K_i ≠ 0:

`(K_{r−1}/N) = ∏_{i=1}^{r−1} (K_i, −K_{i+1})₂ · (−1)^{#{i : K_i < 0 < K_{i+1}}}.`

*Proof.*
1. LDLᵀ gives the path form ≅ ⟨K_i/K_{i−1}⟩, so its Hasse invariant at v is ∏(K_i, −K_{i+1})_v.
2. At ℓ | N the splitting L = M ⊥ ⟨N/K_{r−1}⟩ gives s_ℓ = (K_{r−1}/ℓ)^{v_ℓ(N)}.
3. At ℓ ∤ 2N the lattice is unimodular, so s_ℓ = 1.
4. The product formula finishes the proof. ∎

CERTIFIED: 131 467 positive and 65 589 signed random words, 0 failures.

* r = 3 recovers FRIEZE Thm 1.2 / CHI_FLIP Thm 1.1 / MODEL_SPECIFIC Thm 3.1(a).
* The closed form O210 spark 1 asked for is a product of 2-adic Hilbert symbols of consecutive continuants (one factor
  per step of the walk). It is not a product over backtrack runs.
* r-uniqueness for r ≥ 5: the word (2, 2, 2, 4, 2^{r−5}, k) at N = (2Q+3)². This was found independently here and in
  R208, whose version is in FRIEZE §4.
* (Assessment.) Thm 3.1 is classical in substance: the Jacobi symbol computed along a continued fraction, as in
  Zolotarev/Jenkins-style algorithms. What it adds is the explicit ∞-factor.

### 3.2 Positivity = complex conjugation (PROVED dictionary; memo y5_narrow_wide)

Fix m. Positive words ↔ factorisations 1 + Nm = ab with a ≡ b ≡ −1 (mod m). Negative-pair words (c, s < 0) ↔
a ≡ b ≡ +1 (mod m). These have s_∞ = −1. The trivial factorisation always lies in the +1 class.

In the e-slice form −1 ∈ Σ_e(N), the element −1 is complex conjugation in Gal(ℚ(ζ_e)/ℚ). In the wide ray class group
(ℤ/e)*/±1 the condition is trivially satisfied. **The whole ES slice condition is the kernel of narrow → wide at the
real place.** This unifies O210 §3 (positivity), Thm 3.1's ∞-factor, and the "≡ −1" in Type I/II.

## 4. No second-order T1 shadow (EVIDENCE; memo y5_mod16_shadow)

At (position, o mod 32) resolution, no cell is empty at odd squares ≤ 10⁵ yet populated at non-squares of the same
class mod 32. The few empty fine cells have expected count ≈ 2 and shrink with X. Heuristic reason: every
N ≡ 1 (8) is a 2-adic square, and the only global link is the one product-formula bit.

## 5. Siegel–Weil: the sign is not an ∞-factor (memo y5_siegel_weil_chamber)

* For a full-rank form G, the genus average of r(L, G)/|Aut L| is the indicator of G's genus (PROVED, standard).
* χ = −ε₂ is a genus label, and positivity enters only as definiteness (s_∞ = 1).
* SQ₅(p) ⟺ the genus G₋(p) (≍ p classes, CONSTRUCTIVE_ES Thm 2.1) contains a lattice with a path basis. Path-basis
  lattices number ≪ p^{1/3+o(1)} ((J)26 by-product), so this is a thin-set lottery (Assessment).

## 6. The Mordell position alone: SQ_H (CONJECTURE, EVIDENCE; memo y5_even_middle)

SQ_H(N): there is a word with m even and 8 | m·e, where e is the even outer letter. Equivalently, the even edge
avoids h and h′, so o ∈ {h, h′} is N-free.
* All 165 976 primes p ≡ 1 (8) ≤ 10⁷ satisfy SQ_H, for formal and for interior words. Position class C fails at
  10 primes, position class M at 147, and the classical 4 | m slice at 9 primes ≤ 10⁶.
* Among non-square N ≡ 1 (4) ≤ 10⁶, SQ_H fails at exactly 22 composites: 105, 1465, 3865, …, 392505.
* Mean count ≈ 27 words per prime at 10⁷, so no failure is the lottery's prediction (Assessment).

## 7. Verdict (checkpoint 1)
* **PROVED:**
  * transport = Ptolemy mod 8 (§1);
  * the five-position dictionary and the answer to spark 2: the o-progression family exists (P_h) with density
    τ(o+1)/o, and T1 is one Jacobi symbol in every position (§2);
  * the general-r Jacobi law with explicit ∞-factor (§3);
  * the narrow/wide dictionary (§3.2);
  * Siegel–Weil triviality (§5).
* **CERTIFIED / EVIDENCE:**
  * o* census to 10⁷ (fingerprint 21841);
  * no mod-32 shadow;
  * SQ_H to 10⁷ with 22 composite exceptions ≤ 10⁶;
  * T1 controls (499 odd squares) clean.
* **Assessment:** the transport law does not move the sign to a better-behaved quantity. It is the slice condition
  read through a Ptolemy relation. The genuinely structural output is the explicit archimedean factor:
  * positivity = s_∞ = 1 = Maslov count 0;
  * equivalently, "−1 = complex conjugation" in the narrow ray class group.
  Every mechanism that only sees wide or unsigned data cannot detect the ES condition (Assessment). Existence remains
  B2/H-A in every position.
* **ES is not solved; no infinite case of ES is claimed.**
