# Z57_SYNTH — the minimal missing statement for ES at large primes; three mechanisms revisited with new diagnostics

Status: z57 lane SYNTH (brief `z52bbriefs/z57_lanes.md` §SYNTH, common rules `z52bbriefs/z53_depth.md`). Internal,
internally reviewed only. The first hostile review (§7, `data/z57/synth/internal_review.md`, REJECT with 23 findings) has
been applied in this revision. **ES is OPEN; nothing here proves or disproves ES, (★), or the positivity of any family at
any infinite set of primes.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts
`scripts/z57_synth_*`, data `data/z57/synth/` (≈ 1 MB). Read for this lane: Z53–Z56 SUMMARY files, FRONTIER §§2–4, §6, §7,
`Z56_FAMDESIGN.md` §§0–5, `Z55_HCF.md` §§1–3, `Z56_FAMATTACK.md` §3.

## 0. Summary

* **(MS), the minimal missing statement (§1).** *Every prime p > 10¹⁷ with p mod 840 in Mordell's six classes has some
  d ≡ 3 (mod 4) for which the remainder of −p mod d divides (d + 1)/4.*
  * Equivalent forms: R(p) ≥ 1; X(p) > −M_gen(p).
  * Together with Mordell's classical reduction and Salez's verification to 10¹⁷ (abstract checked), (MS) implies ES
    (PROVED relative to those).
  * (MS) is sufficient, not necessary: ES could be proved by other lines or by a non-counting argument.
  * Among the subfamily-positivity statements carried by the (★) machinery, (MS) is the weakest sufficient target
    (Assessment).
  * The proved main terms do not weaken (MS) logically (Lemma 1.2: R ≥ 1 ⟺ X > −M_gen).
* **Data checks (§2).**
  * All 14 (★)-zeros and all 38 𝔊*-zeros lie below 10¹⁰.
  * (MS) is restricted to primes. Its analogue over all n ≡ 1 (4) is false (285 non-square composite zeros
    ≤ 7 999 801, FAMATTACK).
  * **Numerator 8 becomes concrete (CERTIFIED).** The C-even half of (★) is exactly the c = 1 line of 8/p (Lemma 2.1).
    Its count R₈ vanishes at 1 270 primes p ≡ 1 (4) ≤ 10⁸ and at **12 primes in [10¹⁰, 1.1·10¹⁰]** (4 of them in
    Mordell's classes, the largest 10 868 474 401). All twelve were re-verified by two independent enumerators.
    * So "R₈(p) ≥ 1 for all primes p > 10¹⁰ in Mordell's classes" is false.
    * (MS) at threshold 10¹⁰ is consistent with all data.
    * An argument for (MS) at threshold 10¹⁰ that stays valid on the C-even sub-line proves a false statement.
  * **The uniform form (EVIDENCE).** "X(p) ≥ −(5/(4π²))L²" fails at 7 of 334 tested primes in (10⁷, 10⁸]. All 7 lie
    *outside* Mordell's classes.
    * On the 249 tested Mordell-class primes it holds, with closest margin +0.0064 L².
    * There M_gen/L² ≤ 0.135, with mean 0.117 < 5/(4π²): at these sizes the asymptotic constant of Theorem V is not yet
      reached in Mordell classes.
* **Three mechanisms (§3), each partly prior; the new content is diagnostics.**
  * **I (pushed): an effectivity calibration.** Lemma E1 (PROVED): on a Theorem-V slice at Burgess margin μ the
    optimised Burgess bound saves at most p^{−μ²/(1+a)}. Lemma E2 (PROVED): the margin set has exact area 2μ/3 + 4μ²/3.
    Assessment, hypothetical envelope plus fitted model: as the margin μ grows, the envelope crossover falls but the
    family's own zero tail rises.
    * At 50 % of the Burgess-only area the envelope crossover is ≥ 10³⁴, while the family's fitted last zero is
      ≈ 10^{23.9}.
    * At 79 % the zeros end near 10^{14.4} (model), but the envelope needs ≥ 10^{163}.
    * Within this envelope no uniform-margin family is both positive and effective near 10¹⁷.
    * The remainder X has no explicit-constant input at all.
  * **II: split-and-complement** (C-parity; (★) against López). Not killed. Complementarity above 8 813 281 is just
    (MS) (CERTIFIED to 10¹⁰). The halves are positively associated in bulk (corr ≈ +0.29, EVIDENCE). No mechanism
    explaining eventual disjointness of their zero sets was found.
  * **III: covering rigidity plus explicit least non-residue.** Lemma A.1 (PROVED): R(n) = #{d ≡ 3 (4) : n mod d ∈ H_d}
    for every n ≥ 1, and every hit class has Jacobi symbol −1. Prop A.2 (PROVED, corrected): the implication SMCR ⟹ hit,
    for p ≡ 1 (8). Prop A.3 (PROVED via `Z55_HCF.md` T3.1): for every finite D and every g ≥ 11, SMCR(D, g) is false.
    Size-controlled variants are not excluded.
* **Verdict: narrowed (§4).** (MS) is pinned down with its ladder. The numerator-8 screen gets CERTIFIED counterexamples
  above the certified range. The uniform form is not the right target outside Mordell's classes. The effective route has
  a calibrated trade-off. B2 did not move.

## 1. The minimal missing statement

Notation (FRONTIER §2.1, `Z56_FAMDESIGN.md` §1):
* R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n} (ordered);
* M_gen(n) = the genus (character order ≤ 2) part of R; X := R − M_gen; L := log p;
* 𝔊* = {(o, e) : max(o, e)⁴ > min(o, e)·p}; R_𝔊, M_𝔊, X_𝔊 = the same quantities restricted to a pair family 𝔊;
* 𝔐 := {1, 121, 169, 289, 361, 529} ⊂ ℤ/840 (Mordell's classes); every class in 𝔐 is ≡ 1 (mod 8);
* c_V := 5/(4π²) ≈ 0.12665.

### 1.1 Statement

**(MS)** *For every prime p > 10¹⁷ with p mod 840 ∈ 𝔐 there is an integer d ≡ 3 (mod 4) such that the least positive
residue r of −p modulo d is a divisor of (d + 1)/4.*

*Equivalent forms (PROVED).* Lemma A.1 (§3.III; FAMTRY Lemma 1.4 for primes) gives a bijection between the solutions
(u, B, C) and the d ≡ 3 (4) with r := (−n mod d) ≥ 1 and r | (d + 1)/4:
d = 4uC − 1, u = r, C = (d + 1)/(4r), B = (n + r)/d.
Hence, for a prime p: R(p) ≥ 1 ⟺ ∃C, ∃d | 4Cp + 1 with d ≡ −1 (mod 4C) ⟺ ∃u such that p + u has a divisor
≡ −1 (mod 4u) ⟺ X(p) > −M_gen(p).

*Sufficiency for ES (PROVED relative to the cited results).*
* Classical (Mordell's identities): ES for all n reduces to primes p ≡ 1 (4) with p mod 840 ∈ 𝔐. For p ≡ 1 (8) this is
  re-proved as UPPER2 Prop 3.1 / Lean `HC.lean` (d).
* R(p) ≥ 1 gives 4/p = 1/(uBC) + 1/(pBC) + 1/(puC) (Lean `HC.lean` (a)).
* ES holds for every n ≤ 10¹⁷ (Salez, arXiv:1406.6307, abstract checked 2026-11-05). Mihnea–Bogdan, arXiv:2509.00128,
  report 10¹⁸ (abstract checked; unrefereed).
* *Internal-census variant.* Threshold 10¹⁰ also suffices, using:
  * R(p) has no prime zero p ≡ 1 (4) in (8 813 281, 10¹⁰] (CERTIFIED, FRONTIER §2.1);
  * the (★) ∪ López-line census never fails up to 10⁸ ((J)89), which covers ES at the 14 (★)-zeros.

*Scope (FRONTIER §4).* (MS) is a *sufficient* target for ES by the (★) route. It is not necessary: a proof of ES may use
other Type II lines, Type I, or a non-counting construction.

### 1.2 The ladder of sufficient targets

**Proposition 1.1 (PROVED).** For each prime p:
* (i) R_𝔊 is monotone in 𝔊. Hence L4 ⟹ L3 ⟹ L2, since H3 ⊂ 𝔊* (FAMDESIGN §1), and L3′ ⟹ L2, L3″ ⟹ L2.
* (ii) L5 ⟹ L3 whenever M_𝔊*(p) > 0.
* (iii) For fixed η > 0 there is p_V(η) (Theorem V) with M_gen(p) ≥ (c_V − η/2)L² for p ≥ p_V. For such p,
  L6(η) ⟹ R(p) ≥ ηL²/2 > 0 ⟹ L2.

No arrow L6 ⟹ L5 or L5 ⟹ L4 is claimed. A full-family bound does not bound X_𝔊*, and positivity in 𝔊* need not occur
in H3.

| rung | statement for primes p > P (Mordell classes) | data (zeros among primes p ≡ 1 (4)) | at P = 10¹⁰ |
|---|---|---|---|
| L0 | ES(p) | none known; verified ≤ 10¹⁷ (Salez) | true ≤ 10¹⁷ |
| **L2 = (MS)** | R(p) ≥ 1 | 14 zeros, last 8 813 281; none in (8 813 281, 10¹⁰] (CERTIFIED); fit x* ≈ 10^{7.3} (§2.1) | consistent |
| L3 | R_𝔊*(p) ≥ 1 | 38 zeros ≤ 10¹⁰, last 564 661 441; fit x* ≈ 10^{8.3} (FAMDESIGN) | consistent |
| L3′ | R_odd(p) ≥ 1 (C odd) | 423 zeros ≤ 10⁸, 156 in [10⁷, 10⁸) (§2.1) | not tested above 10⁸ |
| L3″ | R₈(p) ≥ 1 (C even = numerator 8) | **12 zeros in [10¹⁰, 1.1·10¹⁰], 4 in Mordell classes** (§2.1) | **false** |
| L4 | R_H3(p) ≥ 1 (complete levels 64C³ ≤ p) | 873 zeros ≤ 10¹⁰, last 9 466 909 909; fit x* ≈ 10^{12.6} (FAMDESIGN) | at risk (model) |
| L5 | X_𝔊* ≥ −(1 − ε)M_𝔊* (H⁻) | false at every 𝔊*-zero with M_𝔊* > 0; vacuous where M_𝔊* = 0 (e.g. p = 37) | not refuted |
| L6(η) | X(p) ≥ −(c_V − η)L², η > 0 | η = 0 diagnostic: fails at 7 non-Mordell primes in (10⁷, 10⁸]; holds on the 249 tested Mordell primes (§2.3) | not refuted |

*Minimality (Assessment).*
* Every proved positivity-side input of z53–z56 concerns (★) or a sub-family: Thm U, Thm X, Thm V, CROSSO Thm P/A,
  EXACTSPIN, FAMATTACK Thm J.
* Within that menu of subfamily-positivity statements, full (★) positivity is the weakest sufficient target. It has the
  largest expected count (0.152 L², against 0.127 L² for 𝔊*) and the same proved genus main term.
* Weaker single-p targets lie outside the menu: unions with the López b-line, the Type II lines c ≥ 2, Type I, and
  ultimately ES(p) itself. None has a proved polylog main term at a fixed prime.
* Strict logical separation of these eventual statements above 10¹⁰ is not claimed. All separating primes known lie
  below the thresholds, except for L3″.

### 1.3 What the proved main terms buy

**Lemma 1.2 (PROVED, definitions).** For every n: R(n) ≥ 1 ⟺ X(n) > −M_gen(n). The same holds for every family 𝔊.

Theorem V therefore leaves the logical content of (MS) unchanged. It makes available the sufficient form L6(η), η > 0,
for p ≥ p_V(η) (Prop 1.1(iii)). A proof through L6 must control the remainder at the scale of the proved constant. The
relative form L5 instead needs a threshold above every zero with positive genus mass: > 564 661 441 for 𝔊* and
> 8 813 281 for the full family.

### 1.4 Effectivity of the (★) route

To finish ES by the (★) route, with the verified range as the only bridge, one needs (MS) at *every* p > 10¹⁷. An
eventual statement with an unspecified or astronomical p₀ does not suffice. One natural implementation is a "main term −
error" argument with explicit constants; §3.I calibrates what such an implementation would need. This is a statement
about one class of proofs, not a necessity theorem for ES or for (MS).

## 2. Data checks

### 2.1 Numerator 8: the C-even half of (★)

**Lemma 2.1 (PROVED).** (u, B, 2C′) solves (★) iff 8uBC′ − u − B = p iff 8/p = 1/(uBC′) + 1/(pBC′) + 1/(puC′). (The
common denominator is puBC′, and (p + u + B)/(puBC′) = 8/p.) So R = R_odd + R₈, where R₈ := #{(★) solutions with C even}
is the c = 1 Type II line of numerator 8. Doubling denominators maps 8/p-solutions to 4/p-solutions. In general there is
no converse implication: a (★) solution with C odd does not halve.

**Scan to 10⁸ (CERTIFIED).** `scripts/z57_synth_tri.c` enumerates all triples with 4uBC − u − B ≤ N (per-n counters
capped at 65535; zero/non-zero decisions and the R ≤ 8 rows are unaffected).
* Validation: it reproduces exactly the 14 known (★)-zeros, and it agrees with `z57_synth_dec8.c` on [10³, 2·10⁶]
  (502 R₈-zeros, identical R values).
* Results among the 2 880 504 primes p ≡ 1 (4) ≤ 10⁸:
  * R = 0 at the 14 known primes.
  * **R₈ = 0 at 1 270 primes** (including the 14). By decade: 1, 3, 12, 48, 115, 235, 384, 472 in [10⁷, 10⁸). The last
    is 99 671 381.
  * R_odd = 0 at 423 primes (including the 14), 156 of them in [10⁷, 10⁸) (last 99 111 841).
  * Among primes p ≡ 3 (4) ≤ 10⁸: R₈ = 0 at 1 161, including 131. Files `tri_1e8.{txt,log}`.

**Above 10¹⁰ (CERTIFIED: one exhaustive engine for the interval; every zero independently re-verified).**
`scripts/z57_synth_dec8.c` decides R₈ ≥ 1 exhaustively: an even-level scan with early exit, then the exact three-loop
enumeration of FAMDESIGN's engine, which the internal review audited case by case.
* Over all 21 668 737 primes p ≡ 1 (4) in [10¹⁰, 1.1·10¹⁰] it finds **R₈ = 0 at exactly 12 primes** (R in parentheses;
  Mordell-class ones marked M) (`dec8_1e10.{txt,log}`):
  * 10 156 800 001 (56); 10 243 598 993 (52); 10 301 993 881 (30, M); 10 529 331 121 (42, M);
  * 10 532 106 649 (12, M); 10 553 835 713 (28); 10 619 482 193 (66); 10 663 548 737 (58);
  * 10 723 946 017 (30); 10 773 657 233 (66); 10 868 474 401 (18, M); 10 917 229 157 (52).
* Independent checks:
  * `scripts/z57_synth_check8.py` (sympy divisor enumeration over min(u, B, C) ≤ (p/3)^{1/3} + 2) confirms the first
    and fifth; controls are in `check8.txt`.
  * The internal reviewer's separate SymPy enumerator, written from scratch, reproduced R₈ = 0 and all twelve R values
    (§7).
* "Exactly twelve" across the interval rests on the single audited engine.

**Model (Assessment; FAMDESIGN §4.4 method, `scripts/z57_synth_zerofit8.py`, `zerofit8.txt`).**
* P(R₈ = 0) ≈ exp(−0.627 − 0.0260 L²) on [10⁵, 10⁸].
* It predicts ≈ 11.1 zeros in [10¹⁰, 1.1·10¹⁰]; 12 were found.
* Expected zeros beyond 10¹⁰ ≈ 331, beyond 10¹² ≈ 41, beyond 10¹⁷ ≈ 0.003; crossover x* ≈ 10^{14.4}.
* The same fit for R gives x* ≈ 10^{7.3}.

**Association (EVIDENCE, `tri_1e8.log`).** corr(R_odd, R₈) over all primes p ≡ 1 (4) by decade: 0.123 (10⁴), 0.191,
0.246, 0.285 (10⁷). Means of R_odd/L² and R₈/L² ≈ 0.088 and 0.0753. At the 472 R₈-zeros in [10⁷, 10⁸), mean R/L² =
0.0816.

*Screen consequence.*
* **CERTIFIED part.** Let P_M be the threshold of a Mordell-restricted "∀p > P_M" statement; take "∀p ≥ P_M" so that a
  zero z forces P_M > z. Then "R₈(p) ≥ 1 for all primes p ≥ P_M in Mordell's classes" requires
  P_M > 10 868 474 401. Without the Mordell restriction it requires P > 10 917 229 157.
* Hence an argument for (MS) at threshold 10¹⁰ that remains valid on the C-even sub-line proves a false statement. It
  must contain a step that fails for that sub-line, or a larger threshold for it.
* **Model part.** The model places the sub-line's last zeros near 10^{14.4} and predicts ≈ 0.003 zeros above 10¹⁷.
  At the Salez threshold the screen therefore reverts to the qualitative FRONTIER §4 item 2.

### 2.2 Least non-residues at the zeros (CERTIFIED; `scripts/z57_synth_lnr.py`, `lnr_zeros.txt`)

n_p := least prime q with (q/p) = −1.
* **The 14 (★)-zeros:** n_p ∈ {5, 7, 11, 13, 17, 19, 23}. Examples: 329 617: 5; 409, 23 929, 1 134 241: 7; 5 212 561: 11.
  Five of them (409, 577, 23 929, 329 617, 1 134 241) lie outside 𝔐.
* **The 38 𝔊*-zeros:** n_p ∈ {2, 5, 7, 11, 13, 17, 19, 23, 29}.
* **Comparison with 2 log²p (finite check):** every (★)-zero has n_p < 2 log²p.

### 2.3 The uniform form L6 at moderate p (EVIDENCE-grade numerics of exact finite sums)

All 334 primes p ≡ 1 (4) in (10⁷, 10⁸] with R(p) ≤ 8 were tested. Exact R comes from `tri_1e8.txt`; M_gen comes from
`scripts/z56_famdesign_mgen.c` (a long-double sum of Lemma 3.2's exact weights). Script `scripts/z57_synth_uniform.py`,
output `uniform.txt`.

*η = 0 diagnostic:* X(p) < −c_V L² at exactly 7 of them. Margin = −X − c_V L².

| p | p mod 840 | R | M_gen | X/L² | margin |
|---|---|---|---|---|---|
| 11 814 001 | 241 | 2 | 35.68 | −0.12699 | ≈ 0.090 |
| 12 252 497 | 257 | 8 | 41.83 | −0.12700 | ≈ 0.093 |
| 18 550 297 | 577 | 6 | 42.75 | −0.13120 | 1.27 |
| 19 071 769 | 409 | 2 | 40.51 | −0.13703 | 2.92 |
| 35 693 521 | 241 | 8 | 46.40 | −0.12699 | ≈ 0.102 |
| 54 619 057 | 577 | 4 | 46.44 | −0.13372 | 2.24 |
| 92 640 649 | 409 | 6 | 52.40 | −0.13790 | 3.78 |

*Reading.*
* **No violation is in 𝔐**, so this does not touch L6 on the domain of (MS).
* On the 249 tested Mordell-class primes:
  * the closest approach is 72 690 361 (R = 4), with X + c_V L² = +0.0064 L²;
  * M_gen/L² ∈ [0.101, 0.135], mean 0.117, which is *below* c_V. L6 is often trivially satisfied there.
* The non-Mordell primes have M_gen/L² ∈ [0.126, 0.157], mean 0.138. They are Type-II-hard for (★) but solvable by
  Mordell's identities.
* The violation count is a lower bound, because primes with R > 8 were not tested.
* Near 10⁹ the two hardest primes of PRIMET1 (both in 𝔐) satisfy L6 (`mgen_hard1e9.txt`):
  * 1 397 190 001: R = 2, M_gen = 51.63, X/L² = −0.112;
  * 1 327 670 401: R = 6, M_gen = 58.14, X/L² = −0.118.
* Theorem V is asymptotic, and the Mordell-class mean 0.117 < c_V shows that its o(1) is substantial at 10⁸. None of
  this contradicts it, and none of it says anything about L6 above 10¹⁰.

## 3. Three mechanisms revisited, with new diagnostics

*Novelty (Assessment, search-limited: `git grep` and the z53–z56 summaries).*
* No z53–z56 memo sizes an effective threshold. "Effective p₀" is asserted (GENUSLVAL, FAMDESIGN) but never computed.
* No memo splits (★) by the parity of C or identifies the C-even half with numerator 8.
* Partitions into sub-counts, their correlations and joint emptiness *are* studied in `Z56_FAMATTACK.md` §§3.2–3.3, for
  size windows.
* Covering rigidity via the least non-residue appears in `Z55_HCF.md` §3 (fixed certificate families; "the GRH route
  cannot be completed by coverings"), with related treatments in `Z53_NONCRTLOGIC.md` and `Z53_FORESTCLASS.md`.

So the three mechanisms below are prior in shape. What is new are the diagnostics: the effectivity calibration, the
parity/numerator-8 data, and the growing-modulus (★)-specific statements.

### 3.I Effective explicit implementation — a calibrated trade-off (PUSHED)

*Mechanism.* Prove (MS) above a threshold ≤ 10¹⁷ by "main term of a sub-family 𝔉 minus an explicit error", with
certified computation below. Two requirements must hold together: the error envelope must cross below the main term
before 10¹⁷, and R_𝔉 must actually be positive above 10¹⁷.

**Lemma E1 (PROVED, elementary).** Let a ≥ 0 and μ > 0, and for real r ≥ 1 put δ(r) := (1/r)(μ − (1 + a)/(4r)). Then
δ(r) ≤ μ²/(1 + a), with equality iff r = (1 + a)/(2μ) ≥ 1.
*Proof.* δ = μx − ((1+a)/4)x² with x = 1/r, maximal at x = 2μ/(1+a). ∎

*Scope of E1 (PROVED arithmetic about one bound expression).* Burgess for a primitive character of cube-free conductor f
gives |Σ_{M<n≤M+N}χ(n)| ≤ C_r N^{1−1/r} f^{(r+1)/(4r²)+ε}.
* On a Theorem-V slice the outer length is N = p^b and the conductor obeys f ≤ 64p^{1+a} (FAMDESIGN Prop 3.4(2)).
* For a conductor of that worst size, the bound is ≤ C′_r N p^{−δ(r)+O(ε)}, with margin μ := b − (1 + a)/4 to the Burgess
  line.
* So *this application* of Burgess saves at most p^{−μ²/(1+a)}. It is not a bound on the true cancellation, nor on other
  uses of Burgess, PV or the large sieve.
* Theorem V's proof as written has further error terms whose constants are not computed here: the inner hyperbola step
  p^{−κε/2} with r, ε adjustable; the p^{o(1)}-absorbed 2^{O(ω)} factors; O(L); truncation; outer averaging; tiling.

**Lemma E2 (PROVED, geometry).** Let S_μ := {(a, b) ∈ G : 0 < max(a, b) − (1 + min(a, b))/4 < μ}. For 0 < μ ≤ 1/12,
area(S_μ) = 2μ/3 + 4μ²/3.
*Proof.* Put x = min, y = max (two mirror halves). For x ≤ 1/3 the y-range is ((1+x)/4, (1+x)/4 + μ), of length μ. For
1/3 ≤ x ≤ (1 + 4μ)/3 it is (x, (1+x)/4 + μ), of length μ − (3x − 1)/4. The constraint x + y < 1 is inactive for
μ ≤ 1/12. Each half has area μ/3 + (1/3)∫_0^{4μ}(μ − t/4)dt = μ/3 + 2μ²/3. ∎
CERTIFIED numerically by `scripts/z57_synth_pincer.py` at μ = 0.01, 0.05, 1/12.

**Proposition E3 (PROVED arithmetic; a sufficient budget, not a necessity).** Let m > 0 and K > 0. Suppose an argument
gives R(p) ≥ M(p) − E(p) with M(p) ≥ mL² and E(p) ≤ K L^k p^{−δ}. Then R(p) ≥ 1 is certified at p as soon as
δ > [log(K/m) + (k − 2)·log L]/log p, because mL² − KL^k p^{−δ} > 0 and R is an integer. Here the *relative* envelope is
E/M ≤ (K/m)L^{k−2}p^{−δ}. With m = 0.10, the smallest M_gen/L² observed on the tested primes:

| (K, k) | δ at p = 10¹⁷ | at 10¹⁸ |
|---|---|---|
| (1, 2) | 0.0588 | 0.0556 |
| (10, 2) | 0.1176 | 0.1111 |
| (10, 3) | 0.2113 | 0.2010 |
| (100, 4) | 0.3638 | 0.3464 |

**Assessment E4 (the trade-off; hypothetical envelope plus fitted model).** Take the uniform-margin sub-families
F_μ := {(★) solutions with min(u,B)^{15} > p and max⁴ ≥ min·p^{1+4μ}} ⊂ 𝔊*_{1/15} (μ = 0 is FAMDESIGN's F4L).
`scripts/z57_synth_pincer.py` computes the exact kept area, the smallest envelope exponent over the kept slices, and the
envelope crossovers with m = (3/π²)·(kept area). `scripts/z57_synth_trimargin.c` and `z57_synth_zerofitm.py` give the zero
sets ≤ 10⁸ and the fitted model tails of F_μ. At μ = 0 they reproduce FAMDESIGN's 302 F4L-zeros ≤ 10⁸ and x* ≈ 10^{10.2}.

| μ | share of area(G_{1/15}) | δ_min = μ²/(1+x_max) | envelope crossover, (K,k) = (1,2) / (100,3) | zeros ≤ 10⁸ | model x* (zeros) | E(zeros > 10¹⁷) |
|---|---|---|---|---|---|---|
| 0 (F4L) | 1 | 0 | none | 302 | 10^{10.2} | 5·10⁻¹⁴ |
| 0.0533 | 0.90 | 0.0020 | 10^{521} / 10^{3436} | 702 | 10^{12.0} | 1·10⁻⁹ |
| 0.1 | 0.79 | 0.0068 | 10^{163} / 10^{946} | 1 754 | 10^{14.4} | 0.003 |
| 0.2179 | 0.50 | 0.0333 | 10^{39} / 10^{178} | 21 632 | 10^{23.9} | 2.6·10⁴ |

A slice-varying envelope (margin √((1 + x)δ₀)) gives the same picture: 50 % of the area at δ₀ = 0.0383 (crossover
10^{34} / 10^{153}); 30 % at δ₀ = 0.085 (10^{18.1} / 10^{67.5}); 10 % at δ₀ = 0.19 (10^{10.6} / 10^{30.9}).

*Reading.*
* Within this hypothetical Burgess-envelope class, raising the margin lowers the envelope crossover but raises the
  family's own zero tail. Assuming the model x* increases as the kept share decreases, max(envelope crossover, x*) ≥ 10^{23.9} for
  every share with (K, k) = (1, 2): shares ≥ 50 % have crossovers ≥ 10^{34}, and shares ≤ 50 % have x* ≥ 10^{23.9}.
* So no uniform-margin family is both (model-)positive above 10¹⁷ and envelope-effective below 10¹⁷.
* These are envelope crossovers and model extrapolations, not lower bounds on the threshold of any actual theorem.
* Separately, the remainder X has no explicit-constant input at all in z53–z56. Tools with relative savings
  δ ≳ 0.06–0.3 and explicit constants (Pólya–Vinogradov, Weil/Deligne, the large sieve) either need power-size main
  terms (B3; Weil on the modular hyperbola costs p^{1/2} per box, PARITY_AUDIT) or act on congruence data (B1/HCF).
  This part is Assessment.
* The explicit EXACTSUM example window certifies only conductors ≤ p^{θ}, θ < 1/2800. It is one example, not an
  optimality statement.

*Escape hatches (none developed).*
1. GRH-explicit character-sum bounds for the main term. LOWERTAIL_DEEP_ASTRA Thm 5.4 gives a zero-free-strip main term
   (CONDITIONAL; main term only).
2. A high-multiplicity encoding that keeps the tie (B3 Remark 2.4). Congruence-coset relaxations of the SL₂ form fix the
   lower-left entry only mod c and lose it.
3. Larger certified ranges. Salez's ≈ 16 h for 10¹⁷ scales linearly to ≈ 1.6·10⁵ machine-hours at 10²¹. This is an
   illustrative resource scenario, nowhere near the 10^{30+} crossovers above.
4. A non-counting proof, which is B1/B2-limited as recorded in FRONTIER §3.

*Falsifier for I.* The calibration would be refuted by an explicit-constant estimate for a (★) sub-family with polylog
main term whose family is model-positive above 10¹⁷ and whose crossover is below 10¹⁷. None is known in z53–z56. The
actual explicit constants of Theorem V's Burgess-only version are not computed here.

### 3.II Split-and-complement (not killed; no mechanism found)

*Mechanism.* Partition (★) into sub-lotteries and explain why their zero sets are disjoint, so that each half needs only
its own positivity. Natural splits: C odd / C even (Lemma 2.1); (★) against the López b-line on the shared integers
p + 4d.

**Lemma S1 (PROVED).**
* (a) R = R_odd + R₈.
* (b) A (★) hit at u = 4d, i.e. a divisor of p + 4d ≡ −1 (mod 16d), is a López hit at d (≡ −1 (mod 4d)). A López hit at
  d lies in one of the classes −1 + 4dj (mod 16d), j ∈ ℤ/4, and is a (★) hit iff j = 0.
* (c) If δ₁, δ₂, δ₃ are pairwise coprime López divisors of p + 4d in classes j₁, j₂, j₃, then δ₁δ₂δ₃ | p + 4d and lies in
  class j₁ + j₂ + j₃.
* Consequently odd products of pairwise coprime López divisors reach j = 0 iff some odd sub-multiset of the j's sums to
  0 mod 4. Constant j ∈ {1, 2, 3} never does.
*Proof of (c).* (−1 + 4dj₁)(−1 + 4dj₂) ≡ 1 − 4d(j₁ + j₂) (mod 16d), as 16d² ≡ 0. Multiplying by −1 + 4dj₃ gives
−1 + 4d(j₁ + j₂ + j₃). ∎

*Diagnostics (run).*
* (i) The 14 (★)-zeros are zeros of both halves (CERTIFIED). Above 8 813 281 the two zero sets are disjoint up to 10¹⁰,
  because R has no zero there. This is (MS) itself, not a mechanism.
* (ii) In bulk the halves are positively associated (corr ≈ +0.29 at 10⁷–10⁸, EVIDENCE). Correlation does not decide
  zero-set disjointness, and no anti-correlation mechanism is visible.
* (iii) Each half alone fails beyond 10¹⁰ (R₈, CERTIFIED) or at least up to 10⁸ (R_odd).
* (iv) The lifting route (b)–(c) is the Davenport-forcing shape (board-refuted, FRONTIER §6) on one integer, and the
  constant-class example shows nothing is forced.
*Verdict.* No mechanism for eventual disjointness was found. The route is not excluded. By-product: the numerator-8
screen of §2.1.

### 3.III Covering rigidity with growing moduli and explicit least non-residue (finite-D form refuted)

*Mechanism.* (★) hits are pure congruence events (Lemma A.1). If every avoider of all hit classes of modulus ≤ D were a
quadratic residue modulo all small primes, explicit least-non-residue bounds would force a hit:
* Bach, Math. Comp. 55 (1990): n_p ≤ 2 log²p under GRH (the internal reviewer could not re-open the abstract; the
  statement is used only conditionally);
* Burgess–Vinogradov unconditionally.
The mechanism is effective by design and T1-native.

**Lemma A.1 (PROVED).** For d ≡ 3 (mod 4) put H_d := {−k mod d : k | (d + 1)/4}.
* (a) For every integer n ≥ 1, R(n) = #{d ≡ 3 (4) : n mod d ∈ H_d}.
* (b) Every element of H_d is a unit mod d with Jacobi symbol (·/d) = −1.
* Hence n = m² never lies in any H_d (T1, for every m).
*Proof.*
* (a) A solution gives d := 4uC − 1 ≡ 3 (4) and n + u = Bd, so n ≡ −u (mod d) with 1 ≤ u ≤ (d + 1)/4 < d and
  u | (d + 1)/4.
* Conversely, if n ≡ −k (mod d) with k | (d + 1)/4, then u := k, C := (d + 1)/(4k), B := (n + k)/d ≥ 1 is a solution
  with 4uC − 1 = d.
* The maps are inverse, since d determines k = (−n mod d) (k < d), and k determines C and B.
* (b) Write d = 4kC − 1. Then d ≡ −1 (mod k), so gcd(k, d) = 1, and (−k/d) = −(k/d). Write k = 2^s k′ with k′ odd.
  * If s ≥ 1 then d ≡ −1 (mod 8), so (2/d) = 1.
  * Reciprocity, with d ≡ −1 (mod k′) and (d − 1)/2 odd, gives (k′/d) = (−1/k′)(−1)^{(k′−1)/2} = 1. ∎
* CERTIFIED check: all 548 725 classes with d ≤ 2·10⁵ (`hitjacobi.txt`).

**Proposition A.2 (PROVED implication; corrected per review).** Let L_D := lcm{d ≤ D : d ≡ 3 (4)} and
P_g := ∏_{ℓ ≤ g} ℓ. Define SMCR(D, g): every unit class a mod lcm(L_D, P_g) with a mod d ∉ H_d for all d ≤ D satisfies
(a/ℓ) = 1 for every odd prime ℓ ≤ g. If SMCR(D, g) holds and p > max(D, g) is a prime with p ≡ 1 (8) and n_p ≤ g, then
R(p) ≥ 1.
*Proof.* p ≡ 1 (8) gives (2/p) = 1, so n_p is odd. Since p ≡ 1 (4), reciprocity gives (p/n_p) = (n_p/p) = −1. So the
unit class of p mod lcm(L_D, P_g) is a non-residue mod the odd prime n_p ≤ g. By SMCR it is not an avoider; some d ≤ D
has p mod d ∈ H_d, and Lemma A.1(a) applies. ∎
(Without p ≡ 1 (8) the statement fails: D = g = 3, p = 7.)

**Proposition A.3 (PROVED relative to `Z55_HCF.md` Theorem 3.1).** For every finite D ≥ 3 and every g ≥ 11, SMCR(D, g)
is false.
*Proof.*
* A (★) hit with divisor d ≤ D at level C is an HCF line-T certificate: c = 4C ∈ 4ℕ, d ≡ −1 (mod c), d | cp + 1,
  c ≤ d + 1 ≤ D + 1, and d is supported on primes ≤ D.
* Apply T3.1 with S = {11}, R = 2 (1 ≤ 2 < 10/3), C_HCF = D + 1, Y = max(D, 11).
* It gives infinitely many primes p ≡ 1 (mod M), p ≡ 2 (mod 11^J) with no such certificate. Such p avoid H_d for all
  d ≤ D.
* Choose p > g larger than every prime factor of L_D. Its class mod lcm(L_D, P_g) is a unit avoider, and
  (p/11) = (2/11) = −1. ∎

*CERTIFIED complement.* R(329 617) = 0 and (329 617/5) = −1. So SMCR(D, g) also fails for 5 ≤ g < 329 617 and every D
with gcd(329 617, L_D) = 1, which includes all D < 3·329 617.

**Remark A.4 (what remains; Assessment).** A.3 is a finite-D statement. Its avoider p may be huge relative to D, so
*size-controlled* variants are not excluded: an avoider bound in a prescribed size range relative to D, or additional
arithmetic hypotheses. One such variant is "R(p) = 0 ⟹ n_p > h(p)".
* With h(p) = 2 log²p it would, under GRH (Bach), give R(p) ≥ 1 for all primes p ≡ 1 (8) beyond its range of validity.
* It fails at all 14 (★)-zeros: n_p < 2 log²p there (§2.2).
* On a domain where n_p ≤ h(p) is known (GRH: all p), it is equivalent to (★)-positivity on that domain.
No intermediate size-controlled statement was formulated here. Lemma A.1(b) records why quadratic data decide only the
coset: every hit class is a Jacobi non-residue. The (★)-zeros have ordinary n_p (§2.2), and their G-part genus mass is
roughly 0.83–0.88 of typical (FAMDESIGN §4.5, a rough reading, not a bound).

## 4. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict: narrowed.**
* (1) (MS) is the weakest sufficient target inside the (★) menu (Assessment). The main-term theorems do not weaken it
  (Lemma 1.2).
  * The C-even sub-line has CERTIFIED zeros above the internal threshold (§2.1). This makes the numerator-8 screen
    concrete.
  * The uniform diagnostic fails only outside Mordell's classes, and at moderate p the Mordell classes sit below the
    asymptotic constant (§2.3).
* (2) Three mechanisms, prior in shape, with new diagnostics.
  * I: a calibrated trade-off between effectivity and family size, within a hypothetical Burgess envelope and a fitted
    model.
  * II: no mechanism for eventual complementarity found; not excluded.
  * III: the finite-D covering rigidity is refuted for every D (A.3 via HCF); size-controlled variants are open.
* (3) B2 did not move.

**FRONTIER §4 hard screens for the pushed calibration (I).**
1. *T1.* Not a positivity mechanism. Lemma A.1(b) records the T1 structure of the hit classes.
2. *8/131.* Sharpened (§2.1): CERTIFIED C-even zeros up to 1.09·10¹⁰, four of them in Mordell's classes.
3. *Tied modulus.* Untouched. I concerns the effectivity of the untied main-term half and the size of the family.
4. *Fixed p.* Passes: all statements are pointwise.

**Proposed FRONTIER text (for the summary lane; do not apply here).**
* §2.4, append: *(z57, `Z57_SYNTH.md`; Assessment where marked.)*
  * A sufficient target for ES by the (★) route: R(p) ≥ 1 for primes p > 10¹⁷ in Mordell's classes, equivalently
    ∃d ≡ 3 (4) with (−p mod d) | (d+1)/4.
  * It is the weakest such target among the (★) subfamily-positivity statements (Assessment).
  * Main-term theorems do not weaken it (R ≥ 1 ⟺ X > −M_gen).
  * The C-even half of (★) is the c = 1 line of 8/p. It has CERTIFIED zeros at 12 primes in [10¹⁰, 1.1·10¹⁰], four in
    Mordell's classes, the largest 10 868 474 401. An argument at threshold 10¹⁰ must therefore fail for that sub-line.
  * The η = 0 uniform diagnostic X ≥ −(5/(4π²))L² fails at 7 non-Mordell primes in (10⁷, 10⁸] and at none of the 249
    tested Mordell primes. At that size the Mordell-class mean of M_gen/L² is 0.117 < 5/(4π²) (numerics).
* §3, append to "Tied modulus" or new entry, **"Effectivity trade-off"** (Assessment, `Z57_SYNTH.md` §3.I):
  * Lemma E1 (PROVED): the optimised Burgess bound on a slice at margin μ saves at most p^{−μ²/(1+a)}.
  * Within that envelope, sub-families with high margins have late zeros (model x* ≈ 10^{23.9} at half the area), and
    families with zeros ending below 10¹⁷ need envelope crossovers ≥ 10^{163}.
  * No input in z53–z56 controls the remainder with explicit constants.
  * Envelope and model statements only.
* §6, add:
  * (z57) Covering rigidity with least non-residue, finite D: SMCR(D, g) false for every D and g ≥ 11 (PROVED via HCF
    T3.1). Size-controlled variants not excluded.
  * (z57) Split-and-complement by C-parity: positively associated halves, no disjointness mechanism (EVIDENCE; not
    excluded).

**Bottom line.**
* Given everything proved through z56, the target for ES at large primes by the (★) route is one sentence: every prime
  p > 10¹⁷ in Mordell's classes has some d ≡ 3 (mod 4) for which the remainder of −p mod d divides (d + 1)/4.
* The 5/6 genus main term does not shorten that sentence; it suggests the shape of an asymptotic proof.
* The data checks add three things:
  * the numerator-8 half of (★) keeps failing past 10¹⁰ (CERTIFIED), so a proof at that threshold must see the parity
    of C;
  * the uniform-constant form is not the right target outside Mordell's classes;
  * at moderate p the Mordell classes sit below the asymptotic constant.
* Making the route effective faces a calibrated trade-off between envelope and family size (hypothetical; model-based).
* A positivity mechanism at one prime is still missing. **ES is OPEN.**

## 5. Commands, files, ranges (all runs used `ulimit -v 6000000` and `timeout`)

* **(★) enumeration to 10⁸.** `gcc -O2 -o /tmp/z57tri scripts/z57_synth_tri.c -lm`, then
  `/tmp/z57tri 100000000 8 > data/z57/synth/tri_1e8.txt 2> data/z57/synth/tri_1e8.log` (≈ 3 min).
* **R₈ zero fit.** `uv run --with numpy --with scipy python scripts/z57_synth_zerofit8.py data/z57/synth/tri_1e8.txt` →
  `zerofit8.txt`.
* **R₈ decision above 10¹⁰.** `gcc -O2 -fopenmp -o /tmp/z57dec8 scripts/z57_synth_dec8.c -lm`, then
  `OMP_NUM_THREADS=20 /tmp/z57dec8 10000000000 11000000000` → `dec8_1e10.{txt,log}` (≈ 4 min). Validation:
  `/tmp/z57dec8 1000 2000000` equals the tri output on that range.
* **Independent check.** `uv run --with sympy python scripts/z57_synth_check8.py 10156800001 10532106649 10000000097 1397190001`
  → `check8.txt`.
* **Small checks.** `python3 scripts/z57_synth_lnr.py` → `lnr_zeros.txt`;
  `python3 scripts/z57_synth_hitjacobi.py 200000` → `hitjacobi.txt`.
* **Genus mass and the uniform diagnostic.** `gcc -O2 -o /tmp/z56mgen scripts/z56_famdesign_mgen.c -lm`; run on the 334
  primes → `mgen_lowR.txt` and on 1 397 190 001, 1 327 670 401 → `mgen_hard1e9.txt`; then
  `python3 scripts/z57_synth_uniform.py` → `uniform.txt`.
* **Margin families and calibration.** `gcc -O2 -o /tmp/z57trim scripts/z57_synth_trimargin.c -lm`, then
  `/tmp/z57trim 100000000` → `trimargin_1e8.{txt,log}` (≈ 4 min; long-double membership near region boundaries, so the
  margin families are model families). Then `uv run --with numpy --with scipy python scripts/z57_synth_zerofitm.py …` →
  `zerofitm.txt`, and `uv run --with scipy python scripts/z57_synth_pincer.py` → `pincer.txt`.

## 6. Literature used

* Salez, arXiv:1406.6307 (abstract: verification to N = 10¹⁷, ≈ 16 h).
* Mihnea–Bogdan, arXiv:2509.00128 (abstract: 10¹⁸; unrefereed).
* Bach, Math. Comp. 55 (1990) 355–380: under ERH the least element outside a proper subgroup is ≤ 2 log² m. This was
  seen in a search-result abstract snippet only, not re-verified at source by the reviewer. It is used only in the
  conditional Remark A.4.
* Burgess as quoted in `Z56_FAMDESIGN.md` §3.1 (Bu).

## 7. Review log

* **Internal hostile review (deep subagent), `data/z57/synth/internal_review.md`: REJECT, 23 findings (13 MAJOR).**
  It independently re-verified all twelve C-even zeros above 10¹⁰, Lemma A.1, Prop A.3's use of HCF T3.1, the 10⁸ data,
  the fits and the least non-residue table. All findings were applied in this revision:
  * **#1.** The L6 violations lie outside 𝔐 (verified: residues 241, 257, 577, 409). They are now reported as such, with
    the Mordell subset holding; the derived reading is removed.
  * **#2.** The ladder arrows are corrected (Prop 1.1).
  * **#3.** L5 at M_𝔊* = 0 (p = 37) is now called vacuous.
  * **#4.** Prop A.2 is restricted to p ≡ 1 (8), with reciprocity; the counterexample D = g = 3, p = 7 is noted.
  * **#5, #6.** E3 is restated as a sufficient strict budget. The E4 thresholds are recomputed in E3's normalisation by
    `z57_synth_pincer.py`; the old "10^{100}–10^{8000}", "≥ 10^{100} for every K ≥ 1" and "pincer" claims are withdrawn.
  * **#7, #8.** E2 is redefined with S_μ, with exact area 2μ/3 + 4μ²/3. The half-area margin and envelope are recomputed
    exactly (μ = (8 − √29)/12, δ₀ = 0.0383).
  * **#9.** E1's scope is limited to one bound expression. The "δ = κε/2 ≲ 10⁻⁴" claim is removed.
  * **#10.** (MS) is called sufficient, not necessary.
  * **#11.** Mechanism II is no longer "killed".
  * **#12.** III's claim is limited to finite D.
  * **#13.** "Strictly"/"weakest" claims are labelled Assessment and restricted to the menu.
  * **#14.** L6 is restricted to η > 0 with explicit slack.
  * **#15.** The interval prediction is corrected to 11.1.
  * **#16.** Mordell-restricted witnesses and endpoint conventions are stated.
  * **#17.** Rounding is fixed.
  * **#18.** The EXACTSUM claim is scoped to its example.
  * **#19.** The section is retitled "revisited, with new diagnostics", with the FAMATTACK, NONCRTLOGIC and FORESTCLASS
    precedents cited.
  * **#20.** The 329 617 witness is restricted to g < 329 617.
  * **#21.** The "non-square composites n ≡ 1 (4) ≤ 7 999 801" wording, the interval (8 813 281, 10¹⁰] and the
    internal-census bridge via the (★) ∪ López census are fixed.
  * **#22.** "Never conversely" becomes "no general converse".
  * **#23.** The certification scenario is now called illustrative.
* *New after the review:* the uniform-margin family scan (`trimargin_1e8`, `zerofitm.txt`) and the trade-off table of
  E4, which replace the withdrawn pincer.
* Cross-model review: pending.
