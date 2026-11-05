# Z57_SYNTH — the minimal missing statement for ES at large primes, three new mechanisms, the effectivity pincer

Status: z57 lane SYNTH (brief `z52bbriefs/z57_lanes.md` §SYNTH, common rules `z52bbriefs/z53_depth.md`). Internal,
internally reviewed only (§7). **ES is OPEN; nothing here proves or disproves ES, (★), or the positivity of any family at
any infinite set of primes.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts
`scripts/z57_synth_*`, data `data/z57/synth/` (< 1 MB). Read for this lane: Z53–Z56 SUMMARY files, FRONTIER §§2–4, §6, §7,
`Z56_FAMDESIGN.md` §§0–5, `Z55_HCF.md` §§1–3.

## 0. Summary

* **(MS), the minimal missing statement (§1).** *For every prime p > 10¹⁷ with p mod 840 in Mordell's six classes, some
  d ≡ 3 (mod 4) has (−p mod d) dividing (d + 1)/4* (equivalently R(p) ≥ 1, equivalently X(p) > −M_gen(p)). With the
  classical reductions and Salez's verification to 10¹⁷ (abstract checked) it implies ES (PROVED relative to those). It is the
  weakest statement *inside the (★) infrastructure* (Prop 1.1), and the proved main-term theorems do **not** weaken it
  logically (Lemma 1.2: R ≥ 1 ⟺ X > −M_gen is a tautology); they only make one quantitative proof shape available.
* **Data checks (§2; CERTIFIED unless marked).**
  * The 14 (★)-zeros and the 38 𝔊*-zeros all lie below 10¹⁰: no conflict. Odd squares: (MS) is restricted to primes;
    its uniform-over-integers analogue is false (285 composite zeros ≤ 8·10⁶, FAMATTACK), so a proof must fail at m².
  * **Numerator 8 becomes concrete.** The C-even half of (★) is exactly the c = 1 line of 8/p (Lemma 2.1). Its
    count R₈ vanishes at 1 270 primes p ≡ 1 (4) ≤ 10⁸ and at **12 primes in [10¹⁰, 1.1·10¹⁰]** (first 10 156 800 001,
    where R = 56; two zeros re-checked by an independent factorisation-based enumerator). So "R₈(p) ≥ 1 for all
    p > 10¹⁰" is **false**, while (MS) at threshold 10¹⁰ is consistent with all data: an argument for (MS) must contain a
    step that fails for the C-even sub-line (or carry a threshold above 1.06·10¹⁰ for it; model ≈ 10^{14.4}).
  * **The uniform form fails at moderate p.** "X(p) ≥ −(5/(4π²))L²" (the form that Theorem V's constant would make
    sufficient) fails at ≥ 7 primes in (10⁷, 10⁸] (EVIDENCE-grade numerics with margins ≥ 0.09, §2.3), e.g. at
    92 640 649 (R = 6, M_gen = 52.40, X/L² = −0.138). (MS) must be stated relative to M_gen(p), not to a proved constant.
* **Three mechanisms (§3).** I: *effective explicit closure*, pushed; II: *split-and-complement* (C-parity / numerator-8
  sub-lotteries); III: *growing-modulus covering rigidity + explicit least non-residue* (overlaps z55 HCF; included
  because it is the only effective-by-design route). Results:
  * **I (pushed) — the effectivity pincer (Lemma E1 PROVED, Prop E3 PROVED arithmetic, rest Assessment).** An ES proof
    needs (MS) for *every* p > 10¹⁷ with explicit constants. The best Burgess saving available on a Theorem-V slice at
    margin μ from the Burgess line is p^{−μ²/(1+a)} (E1). With constants K·L^k the error drops below the main term only
    for p ≳ 10^{100} (keeping half of the Burgess-only constant) to ≈ 10^{8000} (near the full constant). Theorem V's own error terms (savings p^{−κε/2}, ε < 1/100, and 2^{O(ω)} factors absorbed as p^{o(1)})
    are worse still. Proving (MS) at p = 10¹⁷–10¹⁸ via "main term − error" needs a relative saving p^{−δ} with
    δ ≳ 0.06–0.3 (E3). Tools with such δ and explicit constants (Pólya–Vinogradov, Weil/Deligne, the large sieve) give
    either power-size main terms (B3) or congruence data (B1); tools that reach polylog main terms have δ ≤ 10⁻². No
    input in z53–z56 escapes. **Escape hatches:** GRH-explicit inputs (main term only), high-multiplicity tie-preserving
    encodings, and certification beyond 10¹⁸ (infeasible past ≈ 10²¹, Assessment).
  * **II — dead as a mechanism (EVIDENCE).** The two halves are positively coupled: corr(R_odd, R₈) = +0.25 (10⁶–10⁷),
    +0.29 (10⁷–10⁸). They share all 14 zeros. Each half alone fails above 10¹⁰ (R₈, CERTIFIED) or at least up to 10⁸
    (R_odd: 156 zeros in [10⁷, 10⁸)). (MS) above 10¹⁰ rests on pooling, not complementarity.
  * **III — dead in every non-vacuous form.** Lemma A.1 (PROVED): R(n) = #{d ≡ 3 (4) : n mod d ∈ H_d} for every n ≥ 1,
    and every hit class has Jacobi symbol (·/d) = −1. Prop A.3 (PROVED via `Z55_HCF.md` T3.1): for every D,
    some avoider of all hit classes with d ≤ D is a non-residue mod 11; CERTIFIED: R(329 617) = 0 with n_p = 5. Remark A.4:
    the size-relative form (R(p) = 0 ⟹ n_p > 2 log²p) fails at all 14 (★)-zeros and is MS-strength above them.
* **Verdict (§4): narrowed.** The missing statement is pinned to (MS) with explicit threshold ≤ 10¹⁷ (effective form
  MS_eff). The effectivity pincer is new and scopes what any analytic route must supply. The numerator-8 screen is now a
  CERTIFIED counterexample above the certified range. Two mechanisms are killed: II by evidence, III by proof.
  B2 did not move.

## 1. The minimal missing statement

Notation (FRONTIER §2.1, `Z56_FAMDESIGN.md` §1): R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n} (ordered), M_gen(n) its
genus (character order ≤ 2) part, X := R − M_gen; L := log p; 𝔊* = {(o, e) : max(o, e)⁴ > min(o, e)·p}; R_𝔊 the count
restricted to a pair family 𝔊; 𝔐 := {1, 121, 169, 289, 361, 529} ⊂ ℤ/840 (Mordell's classes).

### 1.1 Statement

**(MS)** *For every prime p > 10¹⁷ with p mod 840 ∈ 𝔐 there is an integer d ≡ 3 (mod 4) such that the least positive
residue r of −p modulo d is a divisor of (d + 1)/4.*

*Equivalent forms (PROVED).* By Lemma A.1 below (FAMTRY Lemma 1.4 for primes), the solutions (u, B, C) of
4uBC − u − B = n correspond bijectively to the d ≡ 3 (4) with r := (−n mod d) ≥ 1 and r | (d + 1)/4, via
d = 4uC − 1, u = r, C = (d + 1)/(4r), B = (n + r)/d. Hence for a prime p:
(MS)(p) ⟺ R(p) ≥ 1 ⟺ ∃C ∃d | 4Cp + 1, d ≡ −1 (mod 4C) ⟺ ∃u: p + u has a divisor ≡ −1 (mod 4u) ⟺ X(p) > −M_gen(p).

*Sufficiency for ES (PROVED relative to the cited results).*
* ES for all n reduces to primes p ≡ 1 (4) with p mod 840 ∈ 𝔐. This is classical (Mordell's identities). For
  p ≡ 1 (8) it is re-proved as UPPER2 Prop 3.1 / Lean `HC.lean` (d); p ≡ 5 (8) is covered by FAMTRY Prop 2.1.
* R(p) ≥ 1 gives 4/p = 1/(uBC) + 1/(pBC) + 1/(puC) (Lean `HC.lean` (a)).
* ES holds for every n ≤ 10¹⁷: Salez, arXiv:1406.6307 (abstract checked 2026-11-05: "checking up to N = 10¹⁷").
  Mihnea–Bogdan, arXiv:2509.00128, report 10¹⁸ (abstract checked; unrefereed).
* With only the campaign's own census the same statement with threshold 10¹⁰ suffices: R(p) has no prime zero
  p ≡ 1 (4) in (8 813 281, 10¹⁰] (CERTIFIED, FRONTIER §2.1, three engines).

The brief's version, "R_𝔊*(p) ≥ 1 for p > 10¹⁰", implies (MS) and is strictly stronger (Prop 1.1).

### 1.2 The ladder; in what sense (MS) is minimal

**Proposition 1.1 (PROVED, trivial).** R_𝔊 is monotone in 𝔊. For each p each rung below implies the next:
uniform form L6 ⟹ (via Theorem V, for p ≥ p_V) L5 ⟹ L4/L3 ⟹ (MS) = L2 ⟹ ES(p) = L0.
(L5 ⟹ L3 needs M_𝔊*(p) > 0, which holds by Theorem V for p ≥ p_V.)

| rung | statement for primes p > P (Mordell classes) | data (zeros among primes p ≡ 1 (4)) | at P = 10¹⁰ |
|---|---|---|---|
| L0 | ES(p) | none known; verified ≤ 10¹⁷ (Salez) | true ≤ 10¹⁷ |
| **L2 = (MS)** | R(p) ≥ 1 | 14 zeros, last 8 813 281; none in (8.8·10⁶, 10¹⁰] (CERTIFIED); fit x* ≈ 10^{7.3} (§2.1) | consistent |
| L3 | R_𝔊*(p) ≥ 1 | 38 zeros ≤ 10¹⁰, last 564 661 441; fit x* ≈ 10^{8.3} (FAMDESIGN) | consistent |
| L3′ | R_odd(p) ≥ 1 (C odd) | 423 zeros ≤ 10⁸, 156 in [10⁷, 10⁸) (§2.1) | at risk (not scanned) |
| L3″ | R₈(p) ≥ 1 (C even = numerator 8) | **12 zeros in [10¹⁰, 1.1·10¹⁰]** (§2.1) | **false** |
| L4 | R_H3(p) ≥ 1 (complete levels 64C³ ≤ p) | 873 zeros ≤ 10¹⁰, last 9 466 909 909; fit x* ≈ 10^{12.6} (FAMDESIGN) | at risk |
| L5 | X_𝔊* ≥ −(1 − ε)M_𝔊* (H⁻) | false at every 𝔊*-zero (M_𝔊* > 0 there) | not refuted |
| L6 | X(p) ≥ −(5/(4π²) − η)L² | **false at ≥ 7 primes in (10⁷, 10⁸]** for every η ≥ 0 (§2.3) | not refuted, fragile |

*Minimality (Assessment, resting on Prop 1.1 and Lemma 1.2).*
(a) Every proved positivity-side input of z53–z56 (Thm U, Thm X, Thm V, CROSSO Thm P/A, EXACTSPIN, FAMATTACK Thm J)
concerns (★) or a sub-family of it. Within that infrastructure the full family is the weakest target: it has the largest
expected count (0.152 L² against 0.127 L² for 𝔊*), and it has the same proved genus main term, since the corner
contributes ≥ 0 to M_gen.
(b) Weaker single-p statements exist only outside the infrastructure. One can add the López b-line, the other
Type II lines c ≥ 2, or Type I; the union of (★) and the b-line never fails up to 10⁸ ((J)89). The weakest is ES(p).
None of these has a proved polylog main term at a fixed p, so (MS) is the weakest statement on which the proved
machinery bears.
(c) Restricting to Mordell classes, and raising the threshold to 10¹⁷, uses everything proved or verified about the
complement.

### 1.3 What the proved main terms buy (and what they do not)

**Lemma 1.2 (PROVED, definitions).** For every n: R(n) ≥ 1 ⟺ X(n) > −M_gen(n). The same holds for every family 𝔊
with X_𝔊, M_𝔊.

So Theorem V (M_gen(p) ≥ (5/(4π²) − o(1))L²) does not reduce the logical content of (MS). What it buys is a *uniform*
sufficient form, L6: for p ≥ p_V(η), X(p) ≥ −(5/(4π²) − η)L² ⟹ R(p) ≥ 1. L6 is strictly stronger than (MS), and at
moderate p it is false (§2.3). The proved constant is a lower bound and the actual M_gen(p) fluctuates up to 0.157 L²,
so a proof through L6 must beat both the remainder and the main-term fluctuation. The relative form L5 (H⁻) avoids the
second problem but needs p₀ > 564 661 441 for 𝔊* (FAMDESIGN) and > 8 813 281 for the full family.

### 1.4 The effective form

ES needs (MS) for *every* p > 10¹⁷ (or > 10¹⁰ with the internal census), not merely for p ≥ p₀ with an unspecified or
astronomical p₀. **(MS_eff)** := (MS) *proved with every constant explicit and the analytic threshold ≤ 10¹⁷.*
§3.I shows (Assessment) that no analytic input used in z53–z56 can deliver MS_eff. It also quantifies the saving an
input would need.

## 2. Data checks

### 2.1 Numerator 8: the C-even half of (★) (PROVED identity; CERTIFIED scans)

**Lemma 2.1 (PROVED).** (u, B, 2C′) solves (★) iff 8uBC′ − u − B = p iff
8/p = 1/(uBC′) + 1/(pBC′) + 1/(puC′) (common denominator puBC′: (p + u + B)/(puBC′) = 8/p). So R = R_odd + R₈, where
R₈ := #{(★) solutions with C even} is the c = 1 Type II line of numerator 8 and R_odd counts C odd. A positive
solution for 8/p yields one for 4/p by doubling denominators, never conversely.

*Scans.*
* **To 10⁸ (CERTIFIED).** `scripts/z57_synth_tri.c` enumerates all triples with 4uBC − u − B ≤ N. It reproduces exactly
  the 14 known (★)-zeros and agrees with `z57_synth_dec8.c` on [10³, 2·10⁶] (502 R₈-zeros, R values identical).
  Among the 2 880 504 primes p ≡ 1 (4) ≤ 10⁸:
  * R = 0 at exactly the 14 known primes;
  * **R₈ = 0 at 1 270 primes** (including the 14). By decade: 1, 3, 12, 48, 115, 235, 384, **472 in [10⁷, 10⁸)**;
    the last is 99 671 381.
  * R_odd = 0 at 423 primes (including the 14), 156 of them in [10⁷, 10⁸) (last 99 111 841).
  * Primes p ≡ 3 (4) ≤ 10⁸ with R₈ = 0: 1 161, including 131. Files: `tri_1e8.{txt,log}`.
* **Above 10¹⁰ (CERTIFIED by one engine, two cases independently re-checked).** `scripts/z57_synth_dec8.c` decides
  R₈ ≥ 1 exhaustively: an even-level scan with early exit, then the exact three-loop enumeration of FAMDESIGN's engine.
  Over all 21 668 737 primes p ≡ 1 (4) in [10¹⁰, 1.1·10¹⁰] it finds **R₈ = 0 at exactly 12 primes**:
  10 156 800 001 (R = 56), 10 243 598 993 (52), 10 301 993 881 (30), 10 529 331 121 (42), 10 532 106 649 (12),
  10 553 835 713 (28), 10 619 482 193 (66), 10 663 548 737 (58), 10 723 946 017 (30), 10 773 657 233 (66),
  10 868 474 401 (18), 10 917 229 157 (52) (`dec8_1e10.{txt,log}`).
  * `scripts/z57_synth_check8.py` is an independent method: sympy factorisation, divisor enumeration over
    min(u, B, C) ≤ (p/3)^{1/3} + 2. It confirms R = 56, R₈ = 0 at 10 156 800 001 and R = 12, R₈ = 0 at 10 532 106 649.
    Controls: R = 70, R₈ = 30 at 10 000 000 097; R = 2, R₈ = 2 at 1 397 190 001 (`check8.txt`).
* **Model (Assessment).** The binned Poisson-ML fit of FAMDESIGN §4.4 (`scripts/z57_synth_zerofit8.py`, `zerofit8.txt`)
  gives P(R₈ = 0) ≈ exp(−0.627 − 0.0260 L²) on [10⁵, 10⁸]. It predicts ≈ 12.4 zeros in [10¹⁰, 1.1·10¹⁰]; 12 were found.
  Expected R₈-zeros beyond 10¹⁰ ≈ 331, beyond 10¹² ≈ 41, beyond 10¹⁷ ≈ 0.003; crossover x* ≈ 10^{14.4}.
  The same fit for R gives x* ≈ 10^{7.3}.
* **Coupling (EVIDENCE, `tri_1e8.log`).** corr(R_odd, R₈) over all primes p ≡ 1 (4) per decade:
  +0.12 (10⁴), +0.19 (10⁵), +0.25 (10⁶), +0.29 (10⁷).
  * The means R_odd/L² and R₈/L² are ≈ 0.088 and 0.0753.
  * At the 472 R₈-zeros in [10⁷, 10⁸), mean R/L² (= R_odd/L²) is 0.082, a mild depletion.

*Screen consequence (CERTIFIED + Assessment).* "R₈(p) ≥ 1 for all p > 10¹⁰" is false. An argument for (MS) at
threshold 10¹⁰ whose every step stays valid after restricting to the C-even sub-line therefore proves a false statement.
It must contain a step that fails for that sub-line, or carry a threshold above 1.092·10¹⁰ for it (model: ≈ 10^{14.4}).
This is FRONTIER §4 item 2 made concrete inside the target range, sharper than "must not prove 8/131". The CERTIFIED
part requires the threshold to exceed the largest zero found (10 917 229 157 ≈ 1.092·10¹⁰); "≈ 10^{14.4}" is the model's
expected-count crossover, not a certified last zero. At threshold 10¹⁷ the model predicts ≈ 0.003 R₈-zeros, so at the
Salez threshold the screen reverts to the qualitative "4-specific step or threshold".

### 2.2 Least non-residues at the zeros (CERTIFIED; `scripts/z57_synth_lnr.py`, `lnr_zeros.txt`)

n_p := least prime q with (q/p) = −1.
* **The 14 (★)-zeros:** n_p ∈ {5, 7, 11, 13, 17, 19, 23}. Examples: 329 617: 5; 409, 23 929, 1 134 241: 7; 5 212 561: 11.
  Five of them (409, 577, 23 929, 329 617, 1 134 241) are not in 𝔐.
* **The 38 𝔊*-zeros:** n_p ∈ {2, 5, 7, 11, 13, 17, 19, 23, 29}. Examples: 37, 157, 1 621: 2; 564 661 441: 13.
* **Comparison with 2 log²p:** every one of the 14 (★)-zeros has n_p < 2 log²p (2 log²409 ≈ 72). Used in §3.III.

### 2.3 The uniform form L6 at moderate p (EVIDENCE-grade numerics of exact finite sums)

All 334 primes p ≡ 1 (4) in (10⁷, 10⁸] with R(p) ≤ 8 (exact R from `tri_1e8.txt`) were tested; M_gen(p) is computed by
`scripts/z56_famdesign_mgen.c` (long-double sum of Lemma 3.2's exact weights; it reproduces GENUSLVAL's values).
Script `scripts/z57_synth_uniform.py`, output `uniform.txt`. **X(p) < −(5/(4π²))L² at 7 of them:**

| p | R | M_gen | X/L² | margin |
|---|---|---|---|---|
| 11 814 001 | 2 | 35.68 | −0.12699 | 0.090 |
| 12 252 497 | 8 | 41.83 | −0.12700 | 0.093 |
| 18 550 297 | 6 | 42.75 | −0.13120 | 1.28 |
| 19 071 769 | 2 | 40.51 | −0.13703 | 2.92 |
| 35 693 521 | 8 | 46.40 | −0.12699 | 0.102 |
| 54 619 057 | 4 | 46.44 | −0.13372 | 2.24 |
| 92 640 649 | 6 | 52.40 | −0.13790 | 3.78 |

* Margin = −X − (5/(4π²))L². These margins exceed any long-double rounding error by many orders.
* The count is a lower bound for (10⁷, 10⁸]: primes with R > 8 were not tested.
* On the tested set: M_gen/L² ∈ [0.101, 0.157]; min R/M_gen = 0.049 (19 071 769).
* Near 10⁹ the two hardest primes of PRIMET1 satisfy L6:
  * 1 397 190 001: R = 2, M_gen = 51.63, X/L² = −0.112;
  * 1 327 670 401: R = 6, M_gen = 58.14, X/L² = −0.118 (`mgen_hard1e9.txt`).

So the hardest primes there are also genus-depleted. Theorem V is asymptotic, so none of this contradicts it.

*Reading (Assessment).* L6 needs R(p) ≥ (M_gen(p)/L² − 0.1267)L², up to ≈ 0.03 L² (≈ 16 at 10¹⁰). Observed minima of R
in (10⁹, 10¹⁰] are 2–6 (PRIMET1 census). L6 at threshold 10¹⁰ is therefore unsupported, and a proof cannot rely on the
proved constant with any slack. The adaptive form X > −M_gen, i.e. (MS) itself, is the right target.

## 3. Three mechanisms not tried in z53–z56

Novelty check (Assessment, search-limited; `git grep` over the memos plus the z53–z56 SUMMARY files):
* No z53–z56 memo computes an effective threshold for any main-term theorem. "Effective p₀" is asserted
  (GENUSLVAL, FAMDESIGN) but never sized. The only "astronomical" remarks in DISCOVERIES concern other results.
* No memo splits (★) by the parity of C, and none identifies the C-even half with numerator 8.
* Covering rigidity via the least non-residue appears in `Z55_HCF.md` §3 for fixed finite certificate families, with
  the remark that "the GRH route cannot be completed by coverings". Mechanism III is the growing-modulus, (★)-specific,
  size-relative continuation. It is labelled as overlapping z55.

### 3.I Effective explicit closure — the effectivity pincer (PUSHED)

*Mechanism.* Prove MS_eff by an analytic main-term-plus-remainder argument with explicit constants and threshold ≤ 10¹⁷,
fed by certified computation below.

**Lemma E1 (PROVED, elementary).** Let a ≥ 0 and μ > 0, and for real r ≥ 1 put δ(r) := (1/r)(μ − (1 + a)/(4r)). Then
δ(r) ≤ μ²/(1 + a), with equality iff r = (1 + a)/(2μ).
*Proof.* δ(r) = μx − ((1 + a)/4)x² with x = 1/r. The quadratic is maximised at x = 2μ/(1 + a) with value μ²/(1 + a). ∎

*Meaning (PROVED arithmetic).* Burgess for a primitive character of cube-free conductor f gives
|Σ_{M<n≤M+N}χ(n)| ≤ C_r N^{1−1/r} f^{(r+1)/(4r²)+ε}.
* On a Theorem-V slice the outer variable has length N = p^b and the conductor is f ≤ 64·p^{1+a} (FAMDESIGN Prop 3.4(2):
  f_F f_G ≤ 16op, resp. 64e′p).
* The bound is therefore ≤ C′_r·N·p^{−δ(r)+O(ε)} with μ := b − (1 + a)/4, the distance from the Burgess line.
* By E1 no choice of r saves more than p^{−μ²/(1+a)} on that slice.
* In Theorem V's actual proof the saving is p^{−κε/2} (κ = 1/r, ε < 1/100; Prop 3.4 step (3)), and the 2^{O(ω(2op))} and
  τ factors are absorbed as p^{o(1)} (Prop 3.4 step (1)). That is smaller still.

**Lemma E2 (PROVED, geometry).** For 0 < μ ≤ 1/12 the set of points of G within horizontal (resp. vertical) distance μ
of the Burgess boundary ∂K has area (2/3)μ + O(μ²). Here ∂K is the two segments a = (1 + b)/4 and b = (1 + a)/4,
0 ≤ min ≤ 1/3. The excluded strip carries density (3/π²)·(2/3)μ = (2/π²)μ ≈ 0.203μ per L².
Therefore a slice-by-slice Burgess argument with saving ≥ p^{−δ} on every slice discards at least
(2/π²)√δ·(1 + o(1))·L² of the main-term density, since μ ≥ √δ by E1 with a ≥ 0.
*Proof.* Each strip is {(1 + b)/4 ≤ a < (1 + b)/4 + μ, 0 ≤ b ≤ 1/3} up to O(μ²) boundary pieces. ∎

**Proposition E3 (PROVED arithmetic; the saving an analytic proof of MS_eff needs).** Suppose an argument shows
R(p) ≥ M(p) − E(p) with E(p) ≤ K·L^k·p^{−δ}, at primes where M(p) ≥ m·L². For this to give R(p) ≥ 1 at p = 10^N
one needs δ ≥ [log(K/m) + (k − 2)·log L]/log p.
With m = 0.10 (the smallest observed M_gen/L², §2.3):

| (K, k) | δ needed at p = 10¹⁷ | at 10¹⁸ |
|---|---|---|
| (1, 2) | 0.059 | 0.056 |
| (10, 2) | 0.118 | 0.111 |
| (10, 3) | 0.212 | 0.201 |
| (100, 4) | 0.364 | 0.346 |

*Proof.* R ≥ 1 ⟸ mL² − K L^k p^{−δ} > 0 ⟺ δ > [log(K/m) + (k − 2) log L]/log p. The table is evaluation (L = 39.14,
41.45). ∎

**Assessment E4 (the pincer).**
* (P1) *Tools reaching a polylog main term at one p have tiny δ.*
  * Burgess on slices (GENUSLVAL, GENUSX, FAMDESIGN): δ ≤ μ²/(1+a). Keeping half of Theorem V's Burgess-only constant
    (area 29/180 of G_{1/15}) allows discarding a strip of width μ ≈ 0.24 along ∂K (E2), so the weakest kept slices have
    δ ≲ 0.24²/(1 + 1/15) ≈ 0.05. The proof as written has δ = κε/2 ≲ 10⁻⁴.
  * Heath-Brown's quadratic large sieve has unaudited effectivity.
  * EXACTSUM's exponent-pair windows certify only conductors ≤ p^{1/2800}.
  * Solving p^{δ} ≥ K L^k for (K, k) between (1, 2) and (100, 3): δ = 0.05 gives p ≳ 10^{100}–10^{200}; δ ≈ 2·10⁻³
    (near Theorem V's constant, μ ≈ 0.05) gives p ≳ 10^{4000}–10^{8000}. If the 2^{O(ω)} factors are bounded by their
    maximal order, p₀ becomes doubly exponential (log log p₀ ≳ 1/(κε)).
* (P2) *Tools with δ ≥ 0.1 and explicit constants do not reach the (★) count.*
  * Pólya–Vinogradov, Weil/Deligne, and Montgomery's large sieve either need power-size main terms (B3; Weil on the
    modular hyperbola costs p^{1/2} per box against a main term ≤ 1, PARITY_AUDIT) or reduce to congruence data (B1/HCF).
  * PV-strength main terms exist only on thin regions b > (1 + a)/2, and those cover only part of the density.
  * No δ ≥ 0.1 input bears on the remainder X at all.
* Hence neither half of "main term − error" is available at p ≤ 10¹⁸ with the campaign's tools. Below 10¹⁸ the arithmetic
  is benign: M_gen ≥ 0.10 L² on every tested prime, and FAMDESIGN's slice ratios agree with their main terms to within
  10 % at 10⁸–10⁹. The proofs are what fail.
* **Escape hatches** (none developed):
  1. GRH-explicit character-sum bounds. LOWERTAIL_DEEP_ASTRA Thm 5.4 gives M_gen ≫ L² from zero-free strips. With
     explicit GRH constants the main-term threshold should drop dramatically (CONDITIONAL; the remainder is untouched).
  2. A high-multiplicity encoding that preserves the tie (B3 Remark 2.4 allows it). Congruence-coset relaxations
     (Γ(c)-cosets of the SL₂ form) lose the tie, since they fix the lower-left entry only mod c. No tie-preserving
     encoding is known.
  3. Extending certification. Salez needed ≈ 16 h for 10¹⁷ (abstract). Linear scaling puts 10²¹ at ≈ 10⁵ CPU-hours.
     Certification past ≈ 10²¹ is infeasible, so certification cannot meet thresholds of 10^{100}.
  4. A structural, non-counting proof. Such a proof is B1/B2-limited (FRONTIER §3).

*Falsifier for I.* The pincer is refuted by exhibiting one explicit-constant input with δ ≥ 0.1 that controls a
polylog-main-term (★) sub-count at one p. The z53–z56 inputs listed above contain none (Assessment). A cheap partial
test, the explicit constant of Theorem V's Burgess-only version, is not computed here. The scaling in E1–E3 makes its
order of magnitude (≥ 10^{100}) robust to constants within a factor 10^{10}. That robustness is Assessment, not a
theorem.

### 3.II Split-and-complement (killed, EVIDENCE)

*Mechanism.* Partition (★) into sub-lotteries with different local or arithmetic obstructions and prove their zero sets
are disjoint (complementarity), so that each needs only a weaker positivity statement. Natural splits: C odd / C even
(Lemma 2.1); (★) against the López b-line on the shared integers p + 4d.

**Lemma S1 (PROVED).**
(a) R = R_odd + R₈ (Lemma 2.1).
(b) A (★) hit at u = 4d, i.e. a divisor of p + 4d that is ≡ −1 (mod 16d), is a López hit at d (≡ −1 (mod 4d)).
A López hit at d lies in one of the four classes −1 + 4dj (mod 16d), j ∈ ℤ/4, and is a (★) hit iff j = 0.
(c) If δ₁, δ₂, δ₃ are pairwise coprime López divisors of p + 4d in classes j₁, j₂, j₃, then δ₁δ₂δ₃ divides p + 4d and
lies in class j₁ + j₂ + j₃.
Products of an odd number of pairwise coprime López divisors therefore reach j = 0 iff some odd sub-multiset of the j's
sums to 0 mod 4; constant j ≡ 1 or j ≡ 2 never does.
*Proof of (c).* (−1 + 4dj₁)(−1 + 4dj₂) ≡ 1 − 4d(j₁ + j₂) (mod 16d) since 16d² ≡ 0. Multiplying by −1 + 4dj₃ gives
−1 + 4d(j₁ + j₂ + j₃) (mod 16d). ∎

*Falsifiers (run).*
(i) Overlap: the 14 R-zeros are zeros of both halves (CERTIFIED), so the zero sets are not disjoint.
(ii) Positive coupling: corr(R_odd, R₈) = +0.29 at 10⁷–10⁸ and rising with p (EVIDENCE, §2.1). Complementarity would
need negative correlation.
(iii) Each half fails alone beyond the respective ranges (§2.1).
The lifting of (b)–(c) is the Davenport-forcing shape (board-refuted, FRONTIER §6) on one integer. The constant-class
counterexample shows that no odd-zero-sum statement is forced.
*Verdict:* dead as a mechanism (EVIDENCE; no theorem excludes subtler splits). By-product: the numerator-8 screen (§2.1).

### 3.III Growing-modulus covering rigidity with explicit least non-residue (killed; overlaps z55 HCF)

*Mechanism.* The (★) hits are pure congruence events in p (Lemma A.1). If every "avoider" of all hit classes of modulus
≤ D were a quadratic residue modulo all primes ≤ g(D), the explicit least-non-residue bounds would force a hit:
* Bach, *Math. Comp.* 55 (1990), n_p ≤ 2 log²p under GRH (bound "at most 2 log² m" checked in the ADS abstract);
* Burgess–Vinogradov unconditionally.
The mechanism is effective by design and T1-native: squares are residues everywhere.

**Lemma A.1 (PROVED).** For d ≡ 3 (mod 4) put H_d := {−k mod d : k | (d + 1)/4}.
(a) For every integer n ≥ 1, R(n) = #{d ≡ 3 (4) : n mod d ∈ H_d}.
(b) Every element of H_d is a unit mod d with Jacobi symbol (·/d) = −1. In particular odd squares avoid every H_d (T1).
*Proof.*
* (a) A solution gives d := 4uC − 1 ≡ 3 (4), n + u = Bd, so n ≡ −u (mod d) with u ≤ (d + 1)/4 < d and u | (d + 1)/4;
  hence n mod d = −u ∈ H_d. Conversely, let n ≡ −k (mod d) with k | (d + 1)/4. Then u := k, C := (d + 1)/(4k), and
  B := (n + k)/d ≥ 1 (n + k is a positive multiple of d) is a solution with 4uC − 1 = d. The two maps are mutually
  inverse because d determines k = (−n mod d) (k ≤ (d + 1)/4 < d), and then C and B.
* (b) Write d = 4kC − 1. Then d ≡ −1 (mod k), so gcd(k, d) = 1, and (−k/d) = (−1/d)(k/d) = −(k/d). With k = 2^s k′
  (k′ odd): if s ≥ 1 then 8 | 4k, so d ≡ −1 (mod 8) and (2/d) = 1. By reciprocity, d ≡ −1 (mod k′) and
  (d − 1)/2 odd give (k′/d) = (−1/k′)·(−1)^{(k′−1)/2} = 1. Hence (−k/d) = −1. ∎
* CERTIFIED check: all 548 725 classes with d ≤ 2·10⁵ (`hitjacobi.txt`).

**Proposition A.2 (PROVED implication).** Let L_D := lcm{d ≤ D : d ≡ 3 (4)} and P_g := ∏_{ℓ ≤ g} ℓ.
SMCR(D, g) states: every unit class a mod lcm(L_D, P_g) with a mod d ∉ H_d for all d ≤ D is a quadratic residue
modulo every prime ℓ ≤ g.
If SMCR(D, g) holds and p > max(D, g) is a prime with n_p ≤ g, then R(p) ≥ 1.
*Proof.* p mod lcm(L_D, P_g) is a unit class, and it is a non-residue mod n_p ≤ g. By SMCR it is not an avoider, so
some d ≤ D has p mod d ∈ H_d, and Lemma A.1(a) gives a solution. ∎

**Proposition A.3 (PROVED, relative to `Z55_HCF.md` Theorem 3.1).** For every D ≥ 3 and every g ≥ 11, SMCR(D, g) is false.
*Proof.*
* A (★) hit with divisor d ≤ D at level C is an HCF line-T certificate (c, d) with c = 4C ∈ 4ℕ ⊂ 𝒞_p, d ≡ −1 (mod c),
  d | cp + 1, c ≤ d + 1 ≤ D + 1, and d supported on primes ≤ D.
* Apply T3.1 with S = {11}, R = 2 (1 ≤ 2 < 10/3), C_HCF = D + 1, Y = max(D, 11). It gives infinitely many primes p ≡ 1
  (mod M), p ≡ 2 (mod 11^J), none of which has such a certificate. So p avoids H_d for all d ≤ D.
* Such p are coprime to lcm(L_D, P_g) for large p, and (p/11) = (2/11) = −1. Their class mod lcm(L_D, P_g) is a unit
  avoider that is a non-residue mod 11 ≤ g. ∎
*CERTIFIED complement for g ∈ [5, 10]:* R(329 617) = 0 with (329 617/5) = −1. Hence SMCR(D, g) is false for g ≥ 5 and
every D with gcd(329 617, L_D) = 1, which includes every D < 3·329 617.

**Remark A.4 (size-relative rigidity is MS-strength; Assessment + CERTIFIED data).** The only non-refuted variant lets
the depth depend on the size of the avoider: "R(p) = 0 ⟹ n_p > h(p)".
* With h(p) = 2 log²p (GRH-Bach) or h(p) = p^{1/(4√e)+ε} (Burgess) it would imply (MS) for all large p.
* It is false at all 14 (★)-zeros: n_p ≤ 23 < 2 log²p there (§2.2).
* So it can hold only above 8 813 281, where (conjecturally) R has no zeros. On that range it is equivalent to (MS) for
  p with n_p ≤ h(p), i.e. under GRH to (MS) itself.
No intermediate, non-vacuous rigidity statement was found.

*Verdict:* III is dead as a mechanism. Its fixed-modulus form is refuted for every D (A.3, via z55 HCF), and its
size-relative form is (MS) restated. Lemma A.1(b) records why: the hit classes sit inside the quadratic non-residue
coset, so quadratic data decide only the coset (genus/BM). The zeros are class-layer events: their G-part genus mass is about 0.83–0.88 of
typical (FAMDESIGN §4.5), and their n_p are ordinary (§2.2).

## 4. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict: narrowed.**
* (1) The minimal missing statement is (MS), and in effective form MS_eff (threshold ≤ 10¹⁷, all constants explicit).
  The proved main terms do not weaken it logically (Lemma 1.2). Its uniform form L6 is false at moderate p (§2.3). Its
  numerator-8 half is CERTIFIED false above the certified range (§2.1).
* (2) Three mechanisms new to z53–z56 (III overlapping z55).
  * I, pushed: an effectivity pincer (E1–E4). Any analytic route must supply relative savings δ ≳ 0.06–0.3 with explicit
    constants at p ≈ 10¹⁷, but the tools that reach polylog main terms give δ ≲ 0.05 (Assessment).
  * II: killed by positive coupling and shared zeros (EVIDENCE).
  * III: killed by proof (A.3) and data, with its size-relative remainder MS-strength (A.4).
* (3) B2 did not move; nothing here is positivity at a prescribed prime.

**FRONTIER §4 hard screens for mechanism I (the pushed one).**
1. *T1:* not applicable as a positivity mechanism. The pincer is a statement about error terms. Lemma A.1(b) records
   the T1 structure of the hit classes.
2. *8/131:* sharpened (§2.1). An argument at threshold 10¹⁰ must fail for the C-even sub-line, which has CERTIFIED zeros
   up to at least 1.09·10¹⁰.
3. *Tied modulus:* I does not break it. It shows that even the untied main-term half cannot be made effective below
   ≈ 10^{100} with the current tools.
4. *Fixed p:* passes. Every statement concerns one p (§2.3 tests pointwise inequalities).

**Proposed FRONTIER text (do not apply here; for the summary lane).**
* §2.4, append: *(z57, `Z57_SYNTH.md`.)*
  * (MS) is the weakest statement on which the (★) machinery bears: R(p) ≥ 1 for primes p > 10¹⁷ in Mordell's classes,
    equivalently ∃d ≡ 3 (4) with (−p mod d) | (d+1)/4.
  * Main-term theorems do not weaken it (R ≥ 1 ⟺ X > −M_gen).
  * The uniform form X ≥ −(5/(4π²))L² fails at ≥ 7 primes in (10⁷, 10⁸] (numerics).
  * The C-even half of (★) is the c = 1 line of 8/p. It has CERTIFIED zeros at 12 primes in [10¹⁰, 1.1·10¹⁰], so any
    argument at threshold 10¹⁰ must fail for that sub-line (screen 2 made concrete).
* §3, new barrier entry, **"Effectivity pincer"** (Assessment, `Z57_SYNTH.md` §3.I):
  * ES needs (★)-positivity with explicit constants at p ≈ 10¹⁷.
  * A "main term − error" proof there needs relative savings p^{−δ}, δ ≳ 0.06–0.3 (Prop E3).
  * Burgess on a slice at margin μ saves at most p^{−μ²/(1+a)} (Lemma E1, PROVED). Theorem V-type main terms are
    therefore effective only beyond ≈ 10^{100}–10^{8000} (Assessment).
  * Tools with δ ≥ 0.1 hit B3/B1.
  * Escapes: GRH-explicit (main term only), tie-preserving high-multiplicity encodings, structural proofs.
* §6, add:
  * (z57) Split-and-complement of (★) by C-parity or by line: positively coupled sub-lotteries with shared zeros (EVIDENCE).
  * (z57) Covering rigidity with growing moduli plus least non-residue: false for every D at depth 11 (PROVED via HCF
    T3.1; CERTIFIED at depth 5 via 329 617); its size-relative form is (MS) restated.

**Bottom line.** Given everything proved through z56, the missing statement for ES at large primes is one sentence: every
prime p > 10¹⁷ in Mordell's classes has some d ≡ 3 (mod 4) for which the remainder of −p mod d divides (d + 1)/4. It must
be proved with explicit constants. The 5/6 genus main term does not shorten that sentence. It only shows what an
asymptotic proof would look like, and it would itself have to be made effective at a threshold that the Burgess-type
inputs cannot reach (Assessment). The checks expose two traps. The uniform form fails at small primes, and the C-even half
of (★) (the numerator-8 line) keeps failing past 10¹⁰. Two natural escape mechanisms are dead: splitting the lottery
into complementary halves, and forcing hits from small non-residues. A positivity mechanism at one prime remains missing,
and it would also have to be effective. **ES is OPEN.**

## 5. Commands, files, ranges (all with `ulimit -v 6000000`, `timeout`)

* `gcc -O2 -o /tmp/z57tri scripts/z57_synth_tri.c -lm; /tmp/z57tri 100000000 8 > data/z57/synth/tri_1e8.txt 2> …log`
  (≈ 3 min).
* `uv run --with numpy --with scipy python scripts/z57_synth_zerofit8.py data/z57/synth/tri_1e8.txt` → `zerofit8.txt`.
* `gcc -O2 -fopenmp -o /tmp/z57dec8 scripts/z57_synth_dec8.c -lm`, then
  `OMP_NUM_THREADS=20 /tmp/z57dec8 10000000000 11000000000` → `dec8_1e10.{txt,log}` (≈ 4 min). Validation:
  `/tmp/z57dec8 1000 2000000` equals the tri output on that range.
* `uv run --with sympy python scripts/z57_synth_check8.py 10156800001 10532106649 10000000097 1397190001` → `check8.txt`.
* `python3 scripts/z57_synth_lnr.py` → `lnr_zeros.txt`; `python3 scripts/z57_synth_hitjacobi.py 200000` →
  `hitjacobi.txt`.
* `gcc -O2 -o /tmp/z56mgen scripts/z56_famdesign_mgen.c -lm`. Then `/tmp/z56mgen` on the 334 primes with R ≤ 8 in
  (10⁷, 10⁸] → `mgen_lowR.txt`, and on 1 397 190 001 and 1 327 670 401 → `mgen_hard1e9.txt`.
  Then `python3 scripts/z57_synth_uniform.py` → `uniform.txt`.

## 6. Literature used (checked at source level as stated)

* Salez, arXiv:1406.6307 (abstract: verification to N = 10¹⁷, ≈ 16 h).
* Mihnea–Bogdan, arXiv:2509.00128 (abstract: 10¹⁸; unrefereed).
* Bach, "Explicit bounds for primality testing and related problems", Math. Comp. 55 (1990) 355–380. Abstract (ADS):
  under ERH the least element outside a proper subgroup is "at most 2 log² m". Used only in the conditional Remark A.4.
* Burgess's bound as quoted in `Z56_FAMDESIGN.md` §3.1 (Bu). Used only for the exponent in Lemma E1.

## 7. Review log

[pending: internal hostile review]
